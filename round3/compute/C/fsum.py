"""Exact fibre sums S_n(h) over F_{p^n}, k=2 and k=3, as elements of Z[zeta_p]; Newton identities in Q(zeta_p).
Integer arithmetic only. Usage: python fsum.py p dpoly(list of coeffs low->high, f over F_p) k c1 [c2] h nmax
"""
import os, sys, ctypes, random
os.environ.setdefault("OPENBLAS_NUM_THREADS", "2"); os.environ.setdefault("OMP_NUM_THREADS", "2")
ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x4000)
import numpy as np
from fractions import Fraction

def pmulmod(a, b, g, p):
    n = len(g) - 1
    r = [0] * (2 * n)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] = (r[i + j] + x * y) % p
    for k in range(2 * n - 1, n - 1, -1):
        c = r[k]
        if c:
            for j in range(n + 1):
                r[k - n + j] = (r[k - n + j] - c * g[j]) % p
    return r[:n]

def ppow(e, g, p):
    n = len(g) - 1
    res = [1] + [0] * (n - 1)
    base = [0, 1] + [0] * (n - 2) if n > 1 else [(-g[0]) % p]
    while e:
        if e & 1: res = pmulmod(res, base, g, p)
        base = pmulmod(base, base, g, p); e >>= 1
    return res

def factor(m):
    fs = set(); d = 2
    while d * d <= m:
        while m % d == 0: fs.add(d); m //= d
        d += 1
    if m > 1: fs.add(m)
    return fs

def primitive_poly(p, n, rng):
    Q = p ** n; fs = factor(Q - 1); one = [1] + [0] * (n - 1)
    while True:
        g = [rng.randrange(p) for _ in range(n)] + [1]
        if g[0] == 0: continue
        if ppow(Q - 1, g, p) != one: continue
        if all(ppow((Q - 1) // r, g, p) != one for r in fs): return g

class Field:
    def __init__(self, p, n):
        self.p, self.n = p, n; Q = self.Q = p ** n
        g = primitive_poly(p, n, random.Random(12345 + n))
        self.pw = np.array([p ** j for j in range(n)], dtype=np.int64)
        exp = np.zeros(Q - 1, dtype=np.int64)
        v = [0] * n; v[0] = 1
        for i in range(Q - 1):
            exp[i] = sum(v[j] * p ** j for j in range(n))
            c = v[n - 1]
            v = [0] + v[:n - 1]
            if c:
                v = [(v[j] - c * g[j]) % p for j in range(n)]
        self.exp = exp
        self.log = -np.ones(Q, dtype=np.int64); self.log[exp] = np.arange(Q - 1)
        assert (self.log[1:] >= 0).all() and exp[0] == 1
    def dig(self, A):
        return (A[:, None] // self.pw[None, :]) % self.p
    def enc(self, D):
        return (D % self.p) @ self.pw
    def add(self, A, B):
        return self.enc(self.dig(A) + self.dig(B))
    def mul(self, A, B):
        Z = (A == 0) | (B == 0)
        r = self.exp[(self.log[A] + self.log[B]) % (self.Q - 1)]
        return np.where(Z, 0, r)
    def trace_table(self):
        p, n, Q = self.p, self.n, self.Q
        trx = []
        for m in range(n):
            tot = np.zeros(n, dtype=np.int64)
            for s in range(n):
                e = self.exp[(m * p ** s) % (Q - 1)]
                tot += (e // self.pw) % p
            tot %= p
            assert (tot[1:] == 0).all()
            trx.append(int(tot[0]))
        return np.array(trx, dtype=np.int64)

def group_ring_dft(t, p, n):
    """t: int64 array length p^n. returns V of shape (p^n, p): V[u] = sum_y t(y) zeta^{u.y} as group-ring vector."""
    V = np.zeros((p,) * n + (p,), dtype=np.int64)
    V[..., 0] = t.reshape((p,) * n)
    for ax in range(n):
        W = np.zeros_like(V)
        for u in range(p):
            acc = np.zeros_like(np.take(V, 0, axis=ax))
            for y in range(p):
                acc += np.roll(np.take(V, y, axis=ax), (u * y) % p, axis=-1)
            idx = [slice(None)] * V.ndim; idx[ax] = u
            W[tuple(idx)] = acc
        V = W
    return V.reshape(p ** n, p)

def cyc_mul(A, B, p):
    C = np.zeros_like(A)
    for i in range(p):
        for j in range(p):
            C[:, (i + j) % p] += A[:, i] * B[:, j]
    return C

def sums(p, fco, k, cs, h, n, brute=False):
    F = Field(p, n); Q = F.Q
    X = np.arange(Q, dtype=np.int64)
    acc = np.full(Q, fco[-1] % p, dtype=np.int64)
    for c in reversed(fco[:-1]):
        acc = F.add(F.mul(acc, X), np.full(Q, c % p, dtype=np.int64))
    t = np.where(acc == 0, 0, np.where(F.log[acc] % 2 == 0, 1, -1)).astype(np.int64)
    trx = F.trace_table()
    G = np.zeros((n, n), dtype=np.int64)
    for i in range(n):
        for j in range(n): G[i, j] = trx[i + j] if i + j < n else None or 0
    # Tr(x^m) for m up to 2n-2
    trfull = []
    for m in range(2 * n - 1):
        tot = np.zeros(n, dtype=np.int64)
        for s in range(n):
            e = F.exp[(m * p ** s) % (Q - 1)]; tot += (e // F.pw) % p
        tot %= p; assert (tot[1:] == 0).all(); trfull.append(int(tot[0]))
    for i in range(n):
        for j in range(n): G[i, j] = trfull[i + j]
    V = group_ring_dft(t, p, n)
    D = F.dig(X)
    def Tof(b):
        U = ((b * D) % p) @ G % p
        return V[U @ F.pw]
    if k == 2:
        S = (t[:, None] * Tof(h * cs[0])).sum(axis=0)
    else:
        S = (t[:, None] * cyc_mul(Tof(h * cs[0]), Tof(h * cs[1]), p)).sum(axis=0)
    if brute:
        zs = np.zeros(p, dtype=np.int64)
        def trel(E): return (F.dig(E) @ np.array(trfull[:n], dtype=np.int64)) % p
        SB = np.zeros(p, dtype=np.int64)
        for x1 in range(Q):
            for x2 in range(Q):
                a = F.mul(np.array([x1]), np.array([x2]))
                for x3 in (range(Q) if k == 3 else [0]):
                    if k == 2:
                        e = (h * cs[0] * trel(a)[0]) % p
                        SB[e] += t[x1] * t[x2]
                    else:
                        b2 = F.mul(np.array([x2]), np.array([x3]))
                        e = (h * cs[0] * trel(a)[0] + h * cs[1] * trel(b2)[0]) % p
                        SB[e] += t[x1] * t[x2] * t[x3]
        return S, SB
    return S

# ---- exact arithmetic in Q(zeta_p): elements lists of Fractions length p-1 (basis 1..zeta^{p-2})
def reduce_gr(v, p):
    return [Fraction(int(v[i]) - int(v[p - 1])) for i in range(p - 1)]
def qmul(a, b, p):
    r = [Fraction(0)] * (2 * p)
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i + j] += x * y
    # reduce: zeta^p = 1 then zeta^{p-1} = -(1+...+zeta^{p-2})
    r2 = [Fraction(0)] * p
    for k, x in enumerate(r): r2[k % p] += x
    return [r2[i] - r2[p - 1] for i in range(p - 1)]
def qadd(a, b): return [x + y for x, y in zip(a, b)]
def qsc(a, c): return [x * c for x in a]
def qzero(p): return [Fraction(0)] * (p - 1)
def qone(p): return [Fraction(1)] + [Fraction(0)] * (p - 2)

def newton(ps, p):
    N = len(ps); e = [qone(p)]
    for k in range(1, N + 1):
        s = qzero(p)
        for i in range(1, k + 1):
            term = qmul(e[k - i], ps[i - 1], p)
            s = qadd(s, qsc(term, (-1) ** (i - 1)))
        e.append(qsc(s, Fraction(1, k)))
    return e

if __name__ == "__main__":
    p = int(sys.argv[1]); fco = eval(sys.argv[2]); k = int(sys.argv[3])
    cs = eval(sys.argv[4]); h = int(sys.argv[5]); nmax = int(sys.argv[6]); brute = len(sys.argv) > 7
    sign = 1 if k == 2 else -1
    print(f"p={p} f={fco} k={k} c={cs} h={h} nmax={nmax}")
    ps = []
    for n in range(1, nmax + 1):
        if brute and n <= 2:
            S, SB = sums(p, fco, k, cs, h, n, brute=True)
            print(" brute check n=%d: %s" % (n, "OK" if list(S) == list(SB) else "MISMATCH %s %s" % (list(S), list(SB))))
        else:
            S = sums(p, fco, k, cs, h, n)
        v = reduce_gr(S, p)
        print(f" S_{n} group-ring={list(map(int, S))} in Z[zeta]={[str(x) for x in v]}", flush=True)
        ps.append(qsc(v, sign))
    e = newton(ps, p)
    nz = [k2 for k2 in range(1, nmax + 1) if any(x != 0 for x in e[k2])]
    print(" e_k nonzero for k in", nz)
    print(" largest nonzero e_k (= number of eigenvalues if < nmax):", max(nz) if nz else 0)
