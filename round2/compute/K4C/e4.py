"""E4: sum_r C(r) = M^2 - t0 M + q t0^2   (q = p).  Derivation (exact, no weights):
 sum_r C(r) = sum_x t(x) sum_r t(r x).  For x != 0, r -> r x permutes F_p, so sum_r t(r x) = M.  For x = 0, sum_r t(0) = p t0.
 Hence sum_r C(r) = (M - t0) M + t0 * p t0.   Also sum over r != 0 = M^2 - 2 t0 M + p t0^2   (C(0) = t0 M),
 and when f(0) != 0 (t0^2 = 1) this reads M^2 - t0 M + p.
Checked here for every prime p <= 199 and several polynomials (including f(0) = 0 and non-squarefree ones, where the identity
is still an identity about t)."""
from core import *

POLYS = {"x^3+x+1": [1, 1, 0, 1], "x^3-x+3": [3, -1, 0, 1], "x^5+x+1": [1, 1, 0, 0, 0, 1], "x^3-x": [0, -1, 0, 1],
         "x^3+2x+5": [5, 2, 0, 1], "(x-1)(x-2)(x-4)": None, "x^7+3x+2": [2, 3, 0, 0, 0, 0, 0, 1]}
tot = bad = 0
out = []
for name, co in POLYS.items():
    n = nb = 0
    for p in primes_upto(199):
        if p < 3:
            continue
        c = co if co is not None else poly_from_roots([1, 2, 4], p)
        t = t_table(p, c)
        M, t0 = int(t.sum()), int(t[0])
        C = Cvec(p, t)
        S = int(C.sum())
        ok1 = S == M * M - t0 * M + p * t0 * t0
        ok2 = S - int(C[0]) == M * M - 2 * t0 * M + p * t0 * t0
        # also the closed form's other reading:  sum_{r!=0} C(r) = (M - t0)^2 + (p-1) t0^2 ... compare:
        ok3 = S - int(C[0]) == (M - t0) ** 2 + (p - 1) * t0 * t0
        n += 1
        if not (ok1 and ok2 and ok3):
            nb += 1
            out.append(f"  FAIL {name} p={p}")
    tot += n
    bad += nb
    out.append(f"{name}: primes checked {n}, failures {nb}")
out.append(f"TOTAL checks {tot}, failures {bad}")
open("e4_out.txt", "w", encoding="utf-8").write("\n".join(out) + "\n")
print("\n".join(out))
