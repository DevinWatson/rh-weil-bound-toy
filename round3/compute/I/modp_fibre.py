"""Referee I: independent test of the fibre statement for f = x - a over F_5 (d = 1), k = 2..5, by arithmetic in F_P
(P a prime = 1 mod 5, so that a primitive 5th root of unity omega exists in F_P).

S_h(F_{5^n}) = sum over x in F_{5^n}^k of t(x_1)...t(x_k) psi_n(h Q_c(x)),  t = chi(x - a),  psi_n(u) = omega^{Tr_{F_{5^n}/F_5}(u)}.
All sums are computed in the ring homomorphic image Z[zeta_5] -> F_P, zeta_5 -> omega.  A relation that holds in Z[zeta_5] holds mod P;
a relation mod P is only a necessary condition for the exact relation (so zeros mod two different primes are evidence, not proof).
The L-series L(T) = exp((-1)^(k+1) sum S_n T^n / n) is computed mod P by Newton's recursion.  If H^j_c vanishes for j != k, L is a polynomial of
degree D_k = dim H^k_c.  A nonzero coefficient beyond the predicted degree (mod P) REFUTES the polynomial statement.
No floating point is used.  Machine rules: one process, below normal priority.
"""
import os, sys, json, time, itertools, random
os.environ.setdefault('OMP_NUM_THREADS', '2')
os.environ.setdefault('OPENBLAS_NUM_THREADS', '2')
import ctypes
try:
    ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x4000)
except Exception:
    pass
import numpy as np
from sympy import ZZ, isprime
from sympy.polys.galoistools import gf_irreducible_p

p = 5

def find_prime(start):
    P = start - (start % 5) + 1
    while True:
        if isprime(P):
            return P
        P += 5

def primitive_5th_root(P):
    for a in range(2, 1000):
        w = pow(a, (P - 1) // 5, P)
        if w != 1:
            return w

class Field:
    def __init__(self, n, seed=0):
        self.n = n
        self.Q = p ** n
        rng = random.Random(1000 * n + seed)
        while True:
            f0 = [rng.randrange(p) for _ in range(n)]
            if f0[0] == 0:
                continue
            poly = [1] + f0[::-1]            # high -> low, monic
            if not gf_irreducible_p(poly, p, ZZ):
                continue
            if self._try(f0):
                break
    def _mulx(self, d):
        n = self.n
        out = np.zeros(n, dtype=np.int64)
        out[1:] = d[:-1]
        out = (out - d[-1] * self.f0) % p
        return out
    def _try(self, f0):
        n, Q = self.n, self.Q
        self.f0 = np.array(f0, dtype=np.int64)
        Mx = np.zeros((n, n), dtype=np.int64)
        for j in range(n):
            e = np.zeros(n, dtype=np.int64); e[j] = 1
            Mx[:, j] = self._mulx(e)
        self.Mx = Mx
        cur = np.zeros((1, n), dtype=np.int16); cur[0, 0] = 1
        gm = np.zeros(n, dtype=np.int64)
        gm = self._mulx(np.eye(n, dtype=np.int64)[0])   # x
        m = 1
        while m < Q - 1:
            Mu = np.zeros((n, n), dtype=np.int64)
            col = gm.copy()
            for j in range(n):
                Mu[:, j] = col
                col = self._mulx(col)
            new = ((cur.astype(np.int64) @ Mu.T) % p).astype(np.int16)
            cur = np.concatenate([cur, new], axis=0)
            gm = (Mu @ gm) % p
            m *= 2
        cur = cur[:Q - 1]
        pw = np.array([p ** i for i in range(n)], dtype=np.int64)
        codes = np.zeros(Q - 1, dtype=np.int64)
        for i in range(n):
            codes += cur[:, i].astype(np.int64) * pw[i]
        if len(np.unique(codes)) != Q - 1:
            return False
        self.codes = codes
        self.pw = pw
        chi = np.zeros(Q, dtype=np.int8)
        chi[codes] = 1 - 2 * (np.arange(Q - 1) & 1)
        self.chi = chi
        self.logtab = np.full(Q, -1, dtype=np.int64)
        self.logtab[codes] = np.arange(Q - 1)
        # trace of x^s via companion matrix powers
        tr = []
        Mp = np.eye(n, dtype=np.int64)
        for s in range(2 * n - 1):
            tr.append(int(np.trace(Mp)) % p)
            Mp = (Mx @ Mp) % p
        self.tr = tr
        B = np.array([[tr[i + j] for j in range(n)] for i in range(n)], dtype=np.int64)
        self.B = B
        Y = np.zeros((Q, n), dtype=np.int16)
        ar = np.arange(Q, dtype=np.int64)
        for i in range(n):
            Y[:, i] = (ar // p ** i) % p
        self.Y = Y
        self.BY = ((Y.astype(np.int64) @ B) % p).astype(np.int16)
        return True
    def shift_minus_a(self, a):
        Q = self.Q
        ar = np.arange(Q, dtype=np.int64)
        d0 = ar % p
        return ar - a + np.where(d0 >= a, 0, p)
    def ucodes(self, b):
        u = (self.BY.astype(np.int64) * b) % p
        code = np.zeros(self.Q, dtype=np.int64)
        for i in range(self.n):
            code += u[:, i] * self.pw[i]
        return code

def dft_all(A, W, P, n):
    A = A.reshape((p,) * n)
    for _ in range(n):
        A = np.tensordot(A, W, axes=([0], [0])) % P
    return A.reshape(-1)

def fibre_sum(F, a, h, cs, W, P):
    """S_h over F_{5^n} for t = chi(x - a), c = cs (tuple of ints in 1..4), exact mod P."""
    n, Q = F.n, F.Q
    t = F.chi[F.shift_minus_a(a)].astype(np.int64)
    g = t.copy()
    for c in cs:
        b = (h * c) % p
        gh = dft_all(g % P, W, P, n)           # gh[u] = sum_x g(x) omega^{x.u}
        uc = F.ucodes(b)
        g = (t * gh[uc]) % P
    return int(g.sum() % P)

def brute_sum(F, a, h, cs, wp, P):
    n, Q = F.n, F.Q
    # multiplication table via logs, trace table
    MT = np.zeros((Q, Q), dtype=np.int64)
    lg = F.logtab
    nz = np.arange(1, Q)
    L = lg[nz]
    prod = F.codes[(L[:, None] + L[None, :]) % (Q - 1)]
    MT[1:, 1:] = prod
    trc = np.zeros(Q, dtype=np.int64)
    ar = np.arange(Q)
    for i in range(n):
        trc = trc + ((ar // p ** i) % p) * F.tr[i]
    trc %= p
    t = F.chi[F.shift_minus_a(a)].astype(np.int64)
    k = len(cs) + 1
    # iterate by explicit loops using broadcasting on last variable
    total = 0
    xs = np.arange(Q)
    def rec(depth, phase_vec_list):
        pass
    # direct k-fold sum with numpy meshgrid for k <= 4
    grids = np.meshgrid(*([xs] * k), indexing='ij')
    ph = np.zeros(grids[0].shape, dtype=np.int64)
    wt = np.ones(grids[0].shape, dtype=np.int64)
    for i in range(k):
        wt = wt * t[grids[i]]
    for i, c in enumerate(cs):
        ph = ph + (h * c) * trc[MT[grids[i], grids[i + 1]]]
    ph %= p
    vals = np.array(wp, dtype=object)[ph]
    s = 0
    flat_w = wt.reshape(-1); flat_v = vals.reshape(-1)
    for w_, v_ in zip(flat_w.tolist(), flat_v.tolist()):
        s += w_ * v_
    return s % P

def lseries(S, k, P, N):
    a = [None] + [((-1) ** (k + 1) * S[j]) % P for j in range(1, N + 1)]
    L = [1]
    for n in range(1, N + 1):
        acc = 0
        for j in range(1, n + 1):
            acc += a[j] * L[n - j]
        L.append((acc % P) * pow(n, -1, P) % P)
    return L

def degree(L):
    D = None
    for i, v in enumerate(L):
        if v % 1 == 0 and v != 0:
            D = i
    return D

def rho(c, j):      # rho_j = -c_{j-1}/c_j  in F_5, c is the list c_1..c_{k-1}, j>=2
    return (-c[j - 2] * pow(c[j - 1], -1, p)) % p

def hypothesis_k(c, k):
    """Claim B hypothesis for d = 1 (R = {1}): every product rho_i rho_{i-2} ... rho_{i-2m} != 1 for 2<=i<=k-1, 0<=m<=floor(i/2)-1."""
    bad = []
    for i in range(2, k):
        for m in range(0, i // 2):
            prod = 1
            for a_ in range(m + 1):
                prod = prod * rho(c, i - 2 * a_) % p
            if prod == 1:
                bad.append((i, m))
    return bad

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'all'
    NMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 9
    Pn = int(sys.argv[3]) if len(sys.argv) > 3 else 400000000
    P = find_prime(Pn)
    w = primitive_5th_root(P)
    wp = [pow(w, e, P) for e in range(p)]
    W = np.array([[pow(w, (x * u) % p, P) for u in range(p)] for x in range(p)], dtype=np.int64)
    a = int(sys.argv[6]) if len(sys.argv) > 6 else 1
    h = 1
    configs = json.load(open(sys.argv[4])) if len(sys.argv) > 4 else None
    out = {'P': P, 'omega': w, 'a': a, 'h': h, 'NMAX': NMAX, 'configs': configs, 'S': {}}
    t0 = time.time()
    for n in range(1, NMAX + 1):
        F = Field(n)
        # validation by brute force for n <= 2, k <= 3 (and k = 4 for n = 1)
        if n <= 2:
            for cs in [(1,), (1, 1), (1, 4), (2, 3), (1, 1, 1)]:
                k = len(cs) + 1
                if n == 2 and k > 3:
                    continue
                s1 = fibre_sum(F, a, h, cs, W, P)
                s2 = brute_sum(F, a, h, cs, wp, P)
                print('validate n=%d cs=%s fast=%d brute=%d %s' % (n, cs, s1, s2, 'OK' if s1 == s2 else 'MISMATCH'), flush=True)
                assert s1 == s2
        for cs in configs:
            cs = tuple(cs)
            key = ','.join(map(str, cs))
            out['S'].setdefault(key, {})[n] = fibre_sum(F, a, h, cs, W, P)
        print('n=%d done  %.1fs' % (n, time.time() - t0), flush=True)
        json.dump(out, open(sys.argv[5] if len(sys.argv) > 5 else 'modp_out.json', 'w'))
