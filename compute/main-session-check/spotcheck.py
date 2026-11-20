"""Main-session spot check of the swarm's figures, written without reading the agents' code.

Exact integer arithmetic throughout. Path quadric Q_c(x) = c1 x1 x2 + ... + c_{k-1} x_{k-1} x_k,
N_k = sum over zeros of Q_c of t(x1)...t(xk), t = quadratic character of f.
"""
import ctypes
import itertools
import sys

import numpy as np

try:
    ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x4000)
except Exception:
    pass

fails = 0


def check(label, ok, detail=""):
    global fails
    if not ok:
        fails += 1
    print(f"  {'ok  ' if ok else 'FAIL'} {label} {detail}")


# ---------------------------------------------------------------- finite fields by tables
class Field:
    """F_q, q = p^n, elements 0..q-1 as base-p digit vectors modulo a monic irreducible polynomial."""

    def __init__(self, p, n):
        self.p, self.n, self.q = p, n, p ** n
        self.mod = self._irreducible()
        q = self.q
        self.add = np.zeros((q, q), dtype=np.int64)
        self.mul = np.zeros((q, q), dtype=np.int64)
        vecs = [self._vec(a) for a in range(q)]
        for a in range(q):
            for b in range(q):
                self.add[a, b] = self._int([(x + y) % p for x, y in zip(vecs[a], vecs[b])])
                self.mul[a, b] = self._int(self._polymul(vecs[a], vecs[b]))
        self.neg = np.array([self._int([(-x) % p for x in v]) for v in vecs], dtype=np.int64)
        # quadratic character: squares
        sq = set(int(self.mul[a, a]) for a in range(1, q))
        self.chi = np.array([0] + [1 if a in sq else -1 for a in range(1, q)], dtype=np.int64)

    def _vec(self, a):
        return [(a // self.p ** i) % self.p for i in range(self.n)]

    def _int(self, v):
        return sum(d * self.p ** i for i, d in enumerate(v))

    def _polymul(self, u, v):
        p, n = self.p, self.n
        prod = [0] * (2 * n - 1)
        for i, a in enumerate(u):
            for j, b in enumerate(v):
                prod[i + j] = (prod[i + j] + a * b) % p
        for d in range(2 * n - 2, n - 1, -1):  # reduce by x^n = -(lower terms of mod)
            c = prod[d]
            if c:
                prod[d] = 0
                for i in range(n):
                    prod[d - n + i] = (prod[d - n + i] - c * self.mod[i]) % p
        return prod[:n]

    def _irreducible(self):
        p, n = self.p, self.n
        if n == 1:
            return [0]
        for low in itertools.product(range(p), repeat=n):
            # monic x^n + low; irreducible iff no monic factor of degree 1..n//2
            poly = list(low) + [1]
            if all(not self._divides(g, poly) for d in range(1, n // 2 + 1)
                   for g in ([*g0, 1] for g0 in itertools.product(range(p), repeat=d))):
                return list(low)
        raise RuntimeError("no irreducible polynomial")

    def _divides(self, g, f):
        p = self.p
        f = f[:]
        dg = len(g) - 1
        for d in range(len(f) - 1, dg - 1, -1):
            c = f[d]
            if c:
                for i in range(dg + 1):
                    f[d - dg + i] = (f[d - dg + i] - c * g[i]) % p
        return not any(f[:dg])

    def poly(self, coeffs):
        """values of a polynomial with coefficients in F_p (list, low degree first) at every element"""
        vals = np.zeros(self.q, dtype=np.int64)
        xs = np.arange(self.q)
        for c in reversed(coeffs):
            vals = self.add[self.mul[vals, xs], c % self.p]
        return vals

    def embed(self, c):
        return c % self.p


def N_path(F, t, c, k, all_s=False):
    """DP over (last variable, running value of Q). W[y, s]."""
    q = F.q
    W = np.zeros((q, q), dtype=object) if q ** k > 2 ** 62 else np.zeros((q, q), dtype=np.int64)
    W[:, 0] = t
    sub = F.add[:, F.neg]  # sub[a, b] = a - b
    xs = np.arange(q)
    for i in range(k - 1):
        ci = c[i]
        Wn = np.zeros_like(W)
        for y in range(q):
            if t[y] == 0:
                continue
            inc = F.mul[ci, F.mul[xs, y]]            # c_i x y for every x
            idx = sub[np.arange(q)[:, None], inc[None, :]]   # [s', x] -> s' - c x y
            Wn[y, :] = t[y] * W[xs[None, :], idx].sum(axis=1)
        W = Wn
    tot = W.sum(axis=0)
    return tot if all_s else int(tot[0])


def brute(F, t, c, k):
    q = F.q
    total = 0
    for x in itertools.product(range(q), repeat=k):
        s = 0
        for i in range(k - 1):
            s = int(F.add[s, F.mul[c[i], F.mul[x[i], x[i + 1]]]])
        if s == 0:
            w = 1
            for xi in x:
                w *= int(t[xi])
            total += w
    return total


print("1. my DP against brute force")
for (p, n, k) in ((5, 1, 3), (7, 1, 4), (3, 2, 3), (3, 2, 4), (11, 1, 3)):
    F = Field(p, n)
    t = F.chi[F.poly([1, 1, 0, 1])]          # x^3 + x + 1
    c = [1] * (k - 1)
    check(f"q={F.q} k={k}", N_path(F, t, c, k) == brute(F, t, c, k))

print("2. closed forms N_2 = 2 t0 M - t0^2 and N_3 = t0 M^2 + (M - t0) C")
for coeffs, name in (([1, 1, 0, 1], "x^3+x+1"), ([5, 2, 0, 1], "x^3+2x+5"), ([0, -1, 0, 1], "x^3-x")):
    bad = 0
    for p in (5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        F = Field(p, 1)
        t = F.chi[F.poly(coeffs)]
        M, t0 = int(t.sum()), int(t[0])
        C = int((t * t[F.neg]).sum())
        bad += N_path(F, t, [1], 2) != 2 * t0 * M - t0 * t0
        bad += N_path(F, t, [1, 1], 3) != t0 * M * M + (M - t0) * C
    check(name, bad == 0, f"mismatches {bad} of 20")

print("3. the write-up's largest k=4 ratio: f = x^3+2x+5, p = 31, N_4 = 1448")
F = Field(31, 1)
t = F.chi[F.poly([5, 2, 0, 1])]
n4 = N_path(F, t, [1, 1, 1], 4)
check("N_4", n4 == 1448, f"got {n4}; N^2 = {n4 * n4}, p^3 = {31 ** 3}")

print("4. agent B's n4_table.tsv, rows with p <= 61")
rows = [l.rstrip("\n").split("\t") for l in open("./compute/B/n4_table.tsv", encoding="utf-8")][1:]
POLY = {"x^3+x+1": [1, 1, 0, 1], "x^3-x": [0, -1, 0, 1], "x^3+2x+5": [5, 2, 0, 1], "x^5+x+1": [1, 1, 0, 0, 0, 1], "x^5-5x+3": [3, -5, 0, 0, 0, 1]}
n = bad = 0
for fname, p, M, N4 in rows:
    p = int(p)
    if p > 61 or fname not in POLY:
        continue
    F = Field(p, 1)
    t = F.chi[F.poly(POLY[fname])]
    n += 1
    if int(t.sum()) != int(M) or N_path(F, t, [1, 1, 1], 4) != int(N4):
        bad += 1
check("rows recomputed", bad == 0 and n > 0, f"{n} rows, mismatches {bad}")

print("5. characteristic 3, f = x^3+x+1, all c = 1: write-up says N_4 = 195, 553, 6147, 43681, 520851 for n = 2..6")
claimed = {2: 195, 3: 553, 4: 6147, 5: 43681, 6: 520851}
nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 5
for nn in range(2, nmax + 1):
    F = Field(3, nn)
    t = F.chi[F.poly([1, 1, 0, 1])]
    v = N_path(F, t, [1, 1, 1], 4)
    check(f"n={nn} q={F.q}", v == claimed[nn], f"got {v}; N/q^2 = {v / F.q ** 2:.3f} (float, for reading only)")

print("6. k = 4 with c1 + c2 + c3 = 0 against c = (1,1,1) and (1,2,3): N_4 / p^2 (floats for reading only)")
for p in (53, 59, 61):
    for coeffs, name in (([1, 1, 0, 1], "x^3+x+1"), ([5, 2, 0, 1], "x^3+2x+5")):
        F = Field(p, 1)
        t = F.chi[F.poly(coeffs)]
        r = int((t == 0).sum())
        vals = {c: N_path(F, t, list(c), 4) for c in ((1, 1, p - 2), (1, 1, 1), (1, 2, 3))}
        print(f"     p={p} {name}: roots in F_p = {r}, (p-r)^2 = {(p - r) ** 2}; " + "; ".join(f"c={c}: N_4={v} ({v / p / p:+.3f})" for c, v in vals.items()))

print("7. the plane x1 = x3, x2 = x4 lies in the quadric exactly when c1+c2+c3 = 0, and t(x1)^2 t(x2)^2 sums to (p-r)^2 on it")
F = Field(53, 1)
t = F.chi[F.poly([1, 1, 0, 1])]
r = int((t == 0).sum())
on_plane = sum(int(t[a]) ** 2 * int(t[b]) ** 2 for a in range(53) for b in range(53))
check("plane sum", on_plane == (53 - r) ** 2, f"{on_plane}")

print("8. trivial weight t = 1, k = 4: number of points of x1x2+x2x3+x3x4 = 0 is q^3 + q^2 - q")
for p in (5, 7, 11):
    F = Field(p, 1)
    one = np.ones(p, dtype=np.int64)
    v = N_path(F, one, [1, 1, 1], 4)
    check(f"p={p}", v == p ** 3 + p ** 2 - p, f"{v}")

print(f"\nFAILURES: {fails}")
