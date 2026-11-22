"""Exact finite-field character sums over F_{3^n}, values in Z[omega] (omega = primitive cube root of 1).
Elements of Z[omega] are held as integer 3-vectors (coeff of 1, w, w^2), reduced by w^2 = -1 - w only at the end.
No floating point anywhere. Used by check_S1.py and check_k2.py.
"""
import itertools, numpy as np

def find_irred(n):
    # monic irreducible polynomial of degree n over F_3, as list of coeffs low->high (length n+1)
    for tail in itertools.product(range(3), repeat=n):
        poly = list(tail) + [1]
        if poly[0] == 0:
            continue
        if is_irred(poly):
            return poly
    raise RuntimeError

def polymulmod(a, b, mod):
    n = len(mod) - 1
    res = [0] * (2 * n - 1 if n > 0 else 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                res[i + j] = (res[i + j] + x * y) % 3
    # reduce
    for i in range(len(res) - 1, n - 1, -1):
        c = res[i]
        if c:
            for j in range(n + 1):
                res[i - n + j] = (res[i - n + j] - c * mod[j]) % 3
    return (res + [0] * n)[:n]

def is_irred(poly):
    n = len(poly) - 1
    if n == 1:
        return True
    # brute: no roots/factors up to degree n//2 by checking x^(3^n) = x mod poly and gcd conditions via simple trial division
    # trial division by all monic polys of degree 1..n//2
    def pdivmod_rem(a, b):
        a = a[:]
        db = len(b) - 1
        inv = 1  # b monic
        for i in range(len(a) - 1, db - 1, -1):
            c = a[i] % 3
            if c:
                for j in range(db + 1):
                    a[i - db + j] = (a[i - db + j] - c * b[j]) % 3
        return a[:db]
    for dg in range(1, n // 2 + 1):
        for tail in itertools.product(range(3), repeat=dg):
            b = list(tail) + [1]
            if all(x == 0 for x in pdivmod_rem(poly, b)):
                return False
    return True

class Field:
    def __init__(self, n):
        self.n = n
        self.N = 3 ** n
        self.mod = find_irred(n) if n > 1 else [0, 1]  # n=1: dummy
        N = self.N
        def dec(v):
            return [(v // 3 ** i) % 3 for i in range(n)]
        def enc(c):
            return sum(int(c[i]) * 3 ** i for i in range(n))
        self.dec, self.enc = dec, enc
        if n == 1:
            self.mul = np.array([[(a * b) % 3 for b in range(3)] for a in range(3)], dtype=np.int64)
            self.add = np.array([[(a + b) % 3 for b in range(3)] for a in range(3)], dtype=np.int64)
        else:
            mul = np.zeros((N, N), dtype=np.int64)
            for a in range(N):
                da = dec(a)
                for b in range(a, N):
                    r = enc(polymulmod(da, dec(b), self.mod))
                    mul[a, b] = r; mul[b, a] = r
            self.mul = mul
            add = np.zeros((N, N), dtype=np.int64)
            digs = np.array([dec(v) for v in range(N)])
            pw = np.array([3 ** i for i in range(n)])
            for a in range(N):
                add[a] = ((digs[a][None, :] + digs) % 3) @ pw
            self.add = add
        # trace to F_3: Tr(x) = x + x^3 + ... + x^(3^(n-1)), computed by Frobenius = cube
        self.tr = np.zeros(N, dtype=np.int64)
        for x in range(N):
            s = 0; y = x
            for _ in range(n):
                s = int(self.add[s, y]); y = int(self.mul[y, self.mul[y, y]])
            assert s in (0, 1, 2)  # element of F_3 is encoded as 0,1,2 (constant poly)
            self.tr[x] = s
        self.neg = np.array([int(np.where(self.add[x] == 0)[0][0]) for x in range(N)])

def chi_table(F, fcoef):
    """chi_n(f(x)) for all x in F, f given by integer coeffs (low->high) over F_3. Quadratic character of F_{3^n}."""
    N = F.N
    # squares
    sq = np.zeros(N, dtype=np.int64)
    for x in range(1, N):
        sq[F.mul[x, x]] = 1
    t = np.zeros(N, dtype=np.int64)
    for x in range(N):
        v = 0; xp = 1
        for c in fcoef:
            term = int(F.mul[c % 3, xp]) if c % 3 else 0
            v = int(F.add[v, term]); xp = int(F.mul[xp, x])
        if v == 0:
            t[x] = 0
        else:
            t[x] = 1 if sq[v] else -1
    return t

def z_reduce(v):
    a, b, c = v
    return (a - c, b - c)

def norm2(a, b):
    return a * a - a * b + b * b  # |a + b w|^2

def Smat_sum(F, t, hcs, h):
    """S_h = sum_x prod t(x_i) psi(h sum c_i x_i x_{i+1}); psi(y) = w^{Tr y}. hcs = [c_1..c_{k-1}] in F (encoded)."""
    N = F.N
    k = len(hcs) + 1
    idx = np.arange(N)
    # u_k = t as Z[w]-vector: (N,3) with coefficient on w^0
    u = np.zeros((N, 3), dtype=object)
    u[:, 0] = t.astype(object)
    for i in range(k - 1, 0, -1):  # i = k-1 .. 1, coefficient c_i couples x_i, x_{i+1}
        hc = int(F.mul[h, hcs[i - 1]])
        E = F.tr[F.mul[hc][np.ix_(idx, idx)]] if False else F.tr[F.mul[F.mul[hc, idx][:, None], idx[None, :]]]
        w = np.zeros((N, 3), dtype=object)
        for e in range(3):
            M = (E == e).astype(object)
            sh = np.roll(u, e, axis=1)  # multiply by w^e
            w = w + M.dot(sh)
        u = w * t.astype(object)[:, None]
    tot = u.sum(axis=0)
    return z_reduce(tot)

def Nsum_bruteforce(F, t, cs):
    """N = sum over x in Y of prod t(x_i), Y={sum c_i x_i x_{i+1} = 0}: DP over (x_i, partial sum)."""
    N = F.N
    k = len(cs) + 1
    # a[x][s] = sum over x_1..x_{i-1} of prod t(x_1..x_i) with x_i = x, partial sum s
    a = np.zeros((N, N), dtype=object)
    for x in range(N):
        a[x, 0] = int(t[x])
    for i in range(1, k):
        c = cs[i - 1]
        nxt = np.zeros((N, N), dtype=object)
        for x in range(N):
            for y in range(N):
                ty = int(t[y])
                if ty == 0:
                    continue
                inc = int(F.mul[c, F.mul[x, y]])
                # new s = s + inc
                shifted = F.add[np.arange(N), inc]  # s -> s+inc
                nxt[y, shifted] += a[x, :] * ty
        a = nxt
    return int(a[:, 0].sum())
