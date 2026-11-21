"""Main-session check of round three (own code, exact arithmetic in Z[omega]).
Fibre sums over F_(3^n): S(n) = sum_y g_k(y), g_1 = t, g_(j+1)(y) = t(y) sum_x g_j(x) omega^Tr(c_j x y).
If the fibre cohomology is in one degree with D eigenvalues, S(n) is +- a sum of D n-th powers, so S satisfies a
linear recurrence of order D. Test: the Hankel determinant of size D+1 vanishes and that of size D does not."""
import ctypes, sys
from fractions import Fraction
import numpy as np
sys.path.insert(0, ".")
try: ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x4000)
except Exception: pass
from spotcheck_lib import Field

class Zw:  # a + b*omega, omega^2 = -1 - omega, exact rationals
    __slots__ = ("a", "b")
    def __init__(s, a, b=0): s.a, s.b = Fraction(a), Fraction(b)
    def __add__(s, o): return Zw(s.a + o.a, s.b + o.b)
    def __sub__(s, o): return Zw(s.a - o.a, s.b - o.b)
    def __mul__(s, o): return Zw(s.a * o.a - s.b * o.b, s.a * o.b + s.b * o.a - s.b * o.b)
    def iszero(s): return s.a == 0 and s.b == 0
    def inv(s):
        n = s.a * s.a - s.a * s.b + s.b * s.b            # norm
        return Zw((s.a - s.b) / n, -s.b / n)             # conjugate / norm
    def __repr__(s): return f"({s.a}+{s.b}w)"

def det(M):
    M = [row[:] for row in M]; n = len(M); d = Zw(1)
    for i in range(n):
        piv = next((r for r in range(i, n) if not M[r][i].iszero()), None)
        if piv is None: return Zw(0)
        if piv != i: M[i], M[piv] = M[piv], M[i]; d = d * Zw(-1)
        d = d * M[i][i]; inv = M[i][i].inv()
        for r in range(i + 1, n):
            if M[r][i].iszero(): continue
            fct = M[r][i] * inv
            for c in range(i, n): M[r][c] = M[r][c] - fct * M[i][c]
    return d

def fibre_sums(poly, cs, nmax):
    out = []
    for n in range(1, nmax + 1):
        F = Field(3, n); q = F.q
        t = F.chi[F.poly(poly)]
        tr = np.zeros(q, dtype=np.int64); x = np.arange(q); acc = x.copy()
        cur = x.copy()
        for _ in range(n - 1):
            cur = F.mul[F.mul[cur, cur], cur]; acc = F.add[acc, cur]
        tr = acc                                         # trace to F_3, values 0,1,2 (as field elements 0,1,2)
        g0, g1 = t.astype(object), np.zeros(q, dtype=object)   # g = g0 + g1*omega
        for cj in cs:
            E = tr[F.mul[F.mul[cj, x][:, None], x[None, :]]]     # E[y, x] = Tr(c x y)
            A = [(E == r).astype(object) for r in range(3)]
            # sum_x g(x) omega^E = (A0 g) + omega (A1 g) + omega^2 (A2 g), omega^2 = -1 - omega
            s0 = [A[r].dot(g0) for r in range(3)]; s1 = [A[r].dot(g1) for r in range(3)]
            # (u0 + u1 w) * w^r summed: w^0: (u0,u1); w^1: (u0 + u1 w) w = -u1 + (u0 - u1) w; w^2: (-u0+u1... )
            n0 = s0[0] - s1[1] + (-s0[2] + s1[2])
            n1 = s1[0] + (s0[1] - s1[1]) + (-s0[2])
            g0, g1 = t * n0, t * n1
        out.append(Zw(int(g0.sum()), int(g1.sum())))
    return out

def hankel_rank_test(S, D):
    def H(m): return det([[S[i + j] for j in range(m)] for i in range(m)])
    return (not H(D).iszero(), H(D + 1).iszero())

cases = [("f = x-1, k=2, c=(1)", [-1, 1], [1], 2, 6),
         ("f = x-1, k=3, c=(1,1)", [-1, 1], [1, 1], 2, 6),
         ("f = x-1, k=3, c=(1,-1) (hypothesis fails)", [-1, 1], [1, 2], 1, 6)]
for name, poly, cs, D, nmax in cases:
    S = fibre_sums(poly, cs, nmax)
    ok_nonzero, ok_zero = hankel_rank_test(S, D)
    print(f"{name}: predicted D={D}; S(1..{nmax}) = {S}")
    print(f"    Hankel det of size {D} nonzero: {ok_nonzero};  of size {D + 1} zero: {ok_zero}")
