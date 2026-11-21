"""E2 (third pass): test candidate descriptions of the set where |E_c(a,b)| > p^2/2 (centred, exact), outside the line a+b=1.
Prints, for each predicate, (flagged-outside with predicate)/(outside pairs with predicate) against the overall rate.
Also the exact sums of squares (for the r.m.s. scaling) as integers."""
from fractions import Fraction
from core import *

PR = (31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101)
FT = [("3roots(1,2,4)", [1, 2, 4]), ("3roots(1,3,9)", [1, 3, 9])]


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


preds = {
    "a=1": lambda a, b, p, R: a == 1,
    "a=-1": lambda a, b, p, R: a == p - 1,
    "b=0": lambda a, b, p, R: b == 0,
    "a=1,b=0": lambda a, b, p, R: a == 1 and b == 0,
    "a=-1,b=0": lambda a, b, p, R: a == p - 1 and b == 0,
    "tau(1)=-1 (a+b=-1)": lambda a, b, p, R: (a + b) % p == p - 1,
    "tau(-1)=1 (b-a=1)": lambda a, b, p, R: (b - a) % p == 1,
    "tau(-1)=-1 (b-a=-1)": lambda a, b, p, R: (b - a) % p == p - 1,
    "tau(1)=0 (a+b=0)": lambda a, b, p, R: (a + b) % p == 0,
    "tau(0)=1 (b=1)": lambda a, b, p, R: b == 1,
    "a in root-ratios": lambda a, b, p, R: a in R,
    "b in root-ratios": lambda a, b, p, R: b in R,
    "tau(1) in root-ratios": lambda a, b, p, R: (a + b) % p in R,
    "tau(R) meets R (>=1)": lambda a, b, p, R: any(((a * r + b) % p) in R for r in R),
}
cnt = {k: [0, 0] for k in preds}   # [outside pairs with pred, flagged outside with pred]
tot_out = tot_fl = 0
ss_rows = []
for p in PR:
    r = np.arange(p, dtype=np.int64)
    for name, (co, roots) in ftypes(p).items():
        R = {(ej * pow(ei, p - 2, p)) % p for ei in roots for ej in roots if ei != ej} if roots else set()
        t = t_table(p, co)
        C = Cvec(p, t)
        S = int(C.sum())
        ssq = 0
        npairs = 0
        for a in range(1, p):
            idx = (a * r[None, :] + r[:, None]) % p
            Ea = (C[None, :] * C[idx]).sum(axis=1)
            for b in range(p):
                if (a + b) % p == 1:
                    continue
                vc2 = p * int(Ea[b]) - S * S   # p * E_c, exact integer
                ssq += vc2 * vc2
                npairs += 1
                fl = 2 * abs(vc2) > p ** 3
                tot_out += 1
                tot_fl += fl
                for k, f in preds.items():
                    if (not R) and "root" in k or ((not R) and k.startswith("tau(R)")):
                        continue
                    if f(a, b, p, R):
                        cnt[k][0] += 1
                        cnt[k][1] += fl
        # mean square of E_c/p^2 = ssq / (npairs p^6)  (since vc2 = p E_c)
        ss_rows.append((p, name, ssq, npairs, Fraction(ssq, npairs * p ** 6)))
print(f"overall: flagged outside line {tot_fl} of {tot_out} = {Fraction(tot_fl, tot_out)}  (~{tot_fl/tot_out:.4f})")
for k, (n, f) in cnt.items():
    if n:
        print(f"{k:28s} outside pairs {n:7d} flagged {f:6d} rate {f/n:.4f} lift {(f/n)/(tot_fl/tot_out):.2f}")
print("mean of (E_c/p^2)^2 outside line, and times p:")
out = ["p,f,sum_sq(p E_c)^2,npairs,mean (E_c/p^2)^2 as fraction"]
for p, name, ssq, n, fr in ss_rows:
    out.append(f"{p} {name} {ssq} {n} {fr}  p*mean={float(fr)*p:.3f}")
open("e2c_out.txt", "w", encoding="utf-8").write("\n".join(out) + "\n")
print("\n".join(out[:12]))
