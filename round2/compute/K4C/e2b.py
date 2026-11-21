"""E2 (second pass): raw and centred E(a,b).  Centred: E_c(a,b) = sum_r (C(r)-S/p)(C(ar+b)-S/p) = E(a,b) - S^2/p exactly,
where S = sum_r C(r) (tau is a bijection of F_p).  All exact rationals (Fraction)."""
import sys
from fractions import Fraction
from core import *

PR = (11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101)
FT = [("3roots(1,2,4)", [1, 2, 4]), ("3roots(1,3,9)", [1, 3, 9])]
lines = []
tab = []


def ftypes(p):
    d = {}
    for name, roots in FT:
        co = poly_from_roots(roots, p)
        if squarefree_mod_p(co, p) and co[0] % p:
            d[name] = (co, roots)
    d["irred_cubic"] = (first_irreducible_cubic(p), [])
    q5 = pick_quintic(p)
    d["quintic"] = (q5, roots_mod_p(q5, p))
    return d


for p in PR:
    r = np.arange(p, dtype=np.int64)
    for name, (co, roots) in ftypes(p).items():
        t = t_table(p, co)
        C = Cvec(p, t)
        M, t0 = int(t.sum()), int(t[0])
        S = int(C.sum())
        assert S == M * M - t0 * M + p * t0 * t0
        E = np.zeros((p, p), dtype=object)
        for a in range(1, p):
            idx = (a * r[None, :] + r[:, None]) % p  # [b, r]
            E[a, :] = (C[None, :] * C[idx]).sum(axis=1)
        flagged_raw = []
        flagged_c = []
        for a in range(1, p):
            for b in range(p):
                v = int(E[a, b])
                if 2 * abs(v) > p * p:
                    flagged_raw.append((a, b))
                vc = Fraction(v) - Fraction(S * S, p)
                if 2 * abs(vc) > p * p:
                    flagged_c.append((a, b, vc))
        line = lambda a, b: (a + b) % p == 1
        out_c = [(a, b, vc) for a, b, vc in flagged_c if not line(a, b)]
        n_line_flag = sum(1 for a, b, vc in flagged_c if line(a, b))
        has10 = any((a, b) == (1, 0) for a, b, _ in flagged_c)
        v10 = Fraction(int(E[1, 0]), p * p)
        lines.append(f"p={p} {name} M={M} S={S} S^2/p^3={Fraction(S*S, p**3)} raw_flagged={len(flagged_raw)}/{p*(p-1)} "
                     f"centred_flagged={len(flagged_c)} on_line(a+b=1)={n_line_flag}/{p-1} outside_line={[(a, b, str(vc / (p * p))) for a, b, vc in out_c]}")
        tab.append((p, name, len(flagged_raw), len(flagged_c), n_line_flag, len(out_c)))
open("e2b_out.txt", "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("p, f, raw_flagged, centred_flagged, line_flagged(of p-1), centred_outside_line")
for x in tab:
    print(x)
