"""Finite fields F_{p^n} by explicit tables (q <= 729), quadratic character, path-quadric sums N_k.
All arithmetic is exact integer arithmetic (numpy int tables / python ints). No floating point.
Independent implementation (agent C)."""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_v] = "1"
import ctypes
try:
    ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x4000)
except Exception:
    pass
import itertools
import numpy as np


class Field:
    def __init__(self, p, n):
        self.p, self.n = p, n
        q = p ** n
        self.q = q
        pw = np.array([p ** i for i in range(n)], dtype=np.int64)
        found = None
        for co in itertools.product(range(p), repeat=n):
            if co[0] == 0:
                continue
            # m(x) = x^n + sum co[i] x^i ; list powers of x
            cur = [0] * n
            cur[0] = 1
            seen = {}
            ok = True
            exp = []
            for i in range(q - 1):
                code = sum(cur[j] * p ** j for j in range(n))
                if code in seen:
                    ok = False
                    break
                seen[code] = i
                exp.append(code)
                carry = cur[n - 1]
                new = [0] * n
                for j in range(1, n):
                    new[j] = cur[j - 1]
                for j in range(n):
                    new[j] = (new[j] - carry * co[j]) % p
                cur = new
            if ok and cur == [1] + [0] * (n - 1):
                found = (co, exp)
                break
        assert found is not None, (p, n)
        self.modpoly = found[0]
        exp = np.array(found[1], dtype=np.int64)
        self.exp = exp
        log = -np.ones(q, dtype=np.int64)
        log[exp] = np.arange(q - 1)
        self.log = log
        D = np.array([[(a // p ** j) % p for j in range(n)] for a in range(q)], dtype=np.int64)
        self.add = (((D[:, None, :] + D[None, :, :]) % p) @ pw).astype(np.int32)
        self.neg = (((-D) % p) @ pw).astype(np.int32)
        lg = log
        m = exp[(lg[:, None] + lg[None, :]) % (q - 1)]
        m[0, :] = 0
        m[:, 0] = 0
        self.mul = m.astype(np.int32)
        inv = np.zeros(q, dtype=np.int32)
        inv[1:] = exp[(-lg[1:]) % (q - 1)]
        self.inv = inv
        chi = np.zeros(q, dtype=np.int64)
        for i in range(q - 1):
            chi[exp[i]] = 1 if i % 2 == 0 else -1
        self.chi = chi

    def poly_eval_all(self, coefs):
        """coefs lowest degree first, entries are ints in F_p (embedded as codes 0..p-1)."""
        x = np.arange(self.q)
        r = np.zeros(self.q, dtype=np.int32)
        for c in reversed(coefs):
            r = self.add[self.mul[r, x], np.int32(c % self.p)]
        return r

    def t_of(self, coefs):
        return self.chi[self.poly_eval_all(coefs)]


def N_fast(F, t, c, k):
    """N_k = sum over x in F^k with sum c_i x_i x_{i+1} = 0 of prod t(x_i).
    Method: x2 != 0 -> solve for x1; x2 = 0 -> x1 free and recurse on x3..xk."""
    q = F.q
    assert len(c) == max(k - 1, 0)
    if k == 0:
        return 1
    if k == 1:
        return int(t.sum())
    add, mul, neg, inv = F.add, F.mul, F.neg, F.inv
    tsum = int(t.sum())
    sub = N_fast(F, t, c[2:], k - 2)
    total = int(t[0]) * tsum * sub  # x2 = 0
    m = k - 2
    x = np.arange(q)
    if m == 0:
        # Q = c1 x1 x2, x2 != 0 forces x1 = 0
        total += int(t[0]) * int(t[1:].sum())
        return total
    shp = lambda j: tuple(q if i == j else 1 for i in range(m))
    X = [x.reshape(shp(j)).astype(np.int32) for j in range(m)]
    W = np.zeros((1,) * m, dtype=np.int32)
    for j in range(m - 1):
        term = mul[np.int32(c[2 + j]), mul[X[j], X[j + 1]]]
        W = add[W, term]
    wt = np.ones((1,) * m, dtype=np.int64)
    for j in range(m):
        wt = wt * t.reshape(shp(j))
    for x2 in range(1, q):
        term1 = mul[mul[np.int32(c[1]), np.int32(x2)], X[0]] if k >= 3 else None
        T = add[term1, W]
        scale = neg[inv[mul[np.int32(c[0]), np.int32(x2)]]]
        x1 = mul[T, scale]
        s = int((t[x1] * wt).sum())
        total += int(t[x2]) * s
    return total


def N_brute(F, t, c, k):
    q = F.q
    idx = np.indices((q,) * k).reshape(k, -1)
    Q = np.zeros(idx.shape[1], dtype=np.int32)
    for i in range(k - 1):
        Q = F.add[Q, F.mul[np.int32(c[i]), F.mul[idx[i], idx[i + 1]]]]
    w = np.ones(idx.shape[1], dtype=np.int64)
    for i in range(k):
        w = w * t[idx[i]]
    return int(w[Q == 0].sum())


def N_brute_prime(p, fco, c, k):
    """Table-free brute force for prime fields: plain mod-p arithmetic and Euler criterion."""
    def chi(a):
        a %= p
        if a == 0:
            return 0
        return 1 if pow(a, (p - 1) // 2, p) == 1 else -1
    tt = [chi(sum(fco[i] * pow(x, i, p) for i in range(len(fco)))) for x in range(p)]
    tot = 0
    for xs in itertools.product(range(p), repeat=k):
        if sum(c[i] * xs[i] * xs[i + 1] for i in range(k - 1)) % p == 0:
            w = 1
            for v in xs:
                w *= tt[v]
            tot += w
    return tot
