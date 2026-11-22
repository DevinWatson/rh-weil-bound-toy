import sys, itertools, time
from fractions import Fraction
import numpy as np
sys.path.insert(0, r"./round4/compute/A4")
from ff3 import *

polys = {"x^3-x+1": [1, 2, 0, 1], "x-1": [2, 1], "x^3-x-1": [2, 2, 0, 1]}
cases = []
for name in polys:
    for n in (1, 2, 3):
        for k in (2, 3, 4):
            cases.append((name, n, k))
# bigger n for small k only
for name in ("x^3-x+1",):
    cases.append((name, 4, 2)); cases.append((name, 4, 3))
out = open(r"./round4/compute/A4/check_S1_out.txt", "w")
def P(*a):
    s = " ".join(str(x) for x in a); print(s); out.write(s + "\n"); out.flush()
Fs = {}
for name, n, k in cases:
    if n not in Fs: Fs[n] = Field(n)
    F = Fs[n]; N = F.N
    t = chi_table(F, polys[name])
    st2 = int((t * t).sum())
    M = int(t.sum())
    # coefficient patterns in F_3^* (constants 1 or 2)
    pats = [tuple([1] * (k - 1)), tuple(([1, 2] * k)[:k - 1]), tuple(([2, 1, 1] * k)[:k - 1])]
    for cs in dict.fromkeys(pats):
        t0 = time.time()
        Rz = [0, 0]; worst = Fraction(0); allok = True
        for h in range(1, N):
            a, b = Smat_sum(F, t, list(cs), h)
            Rz[0] += a; Rz[1] += b
            lhs = norm2(a, b)
            bound = (Fraction(N) ** (k - 1)) * st2 * st2   # (Q^{(k-1)/2} sum t^2)^2
            if lhs > bound: allok = False
            worst = max(worst, Fraction(lhs) / bound)
        Nn = Nsum_bruteforce(F, t, list(cs))
        # QN = M^k + R, R in Z[w] must be a rational integer (b == 0)
        lhs_id = N * Nn
        rhs_id_a = M ** k + Rz[0]
        ok_id = (Rz[1] == 0 and lhs_id == rhs_id_a)
        P(f"f={name} n={n} Q^n={N} k={k} c={cs} M={M} sum t^2={st2} N={Nn} R={tuple(Rz)} identity_ok={ok_id} fibre_bound_ok={allok} max|S|^2/bound={float(worst):.4f} ({time.time()-t0:.1f}s)")
P("done")
