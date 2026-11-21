import itertools
import numpy as np

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


