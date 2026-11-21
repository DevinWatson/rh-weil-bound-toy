"""E1: N_4 = -q + t0^2 M^2 + sum_r C(r) C(tau(r)),  tau(r) = -(c3/c1)(r + c2/c3),
checked against a direct count of N_4, for every c in (F_p^*)^3 with c1 = 1, p in {5,7,11,13}, two cubics."""
from core import *

polys = {"x^3+x+1": [1, 1, 0, 1], "x^3-x+3": [3, -1, 0, 1]}
out = []
total = bad = 0
for p in (5, 7, 11, 13):
    for name, co in polys.items():
        if not squarefree_mod_p(co, p) or co[0] % p == 0:
            out.append(f"p={p} {name}: SKIPPED (not squarefree or f(0)=0)")
            continue
        t = t_table(p, co)
        M, t0 = int(t.sum()), int(t[0])
        C = Cvec(p, t)
        n = nb = 0
        for c2 in range(1, p):
            for c3 in range(1, p):
                c = (1, c2, c3)
                direct = N4_brute(p, t, c)
                # tau(r) = -(c3/c1)(r + c2/c3) = -c3 r - c2   (c1 = 1)
                a, b = (-c3) % p, (-c2) % p
                # check against the formula in its stated form with explicit inverses
                inv_c1 = pow(c[0], p - 2, p)
                inv_c3 = pow(c3, p - 2, p)
                a2 = (-(c3 * inv_c1)) % p
                b2 = (-(c3 * inv_c1) * (c2 * inv_c3)) % p
                assert (a, b) == (a2, b2)
                S = E_ab(p, C, a, b)
                formula = -p + t0 * t0 * M * M + S
                n += 1
                if formula != direct:
                    nb += 1
                    out.append(f"  MISMATCH p={p} {name} c={c} direct={direct} formula={formula}")
        total += n
        bad += nb
        out.append(f"p={p} {name}: M={M} t0={t0}  cases={n}  mismatches={nb}")
out.append(f"TOTAL cases {total}, mismatches {bad}")
open("e1_out.txt", "w", encoding="utf-8").write("\n".join(out) + "\n")
print("\n".join(out))
