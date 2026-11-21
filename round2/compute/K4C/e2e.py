"""E2 (fourth pass): the 'spike term'.  C(1) = p - rho is the only value of size p (rho = number of roots of f in F_p).
E(a,b) = C(1) [C(tau 1) + C(tau^{-1} 1)] + (rest)   (the two spike terms merge when tau(1) = 1, and a double
count is avoided when tau(1) = 1).  Test, for b != 0 and outside the line a+b=1, p in 31..101, four f each:
 flagged := 2|E_c| > p^2  (E_c = E - S^2/p, exact)
 Sp := (p - rho) * (C(tau 1) + C(tau^{-1} 1))   (a+b != 1 so tau 1 != 1 and the terms are distinct)
Contingency of flagged against 2|Sp| > p^2/2 and against a = -1.  Exact integers."""
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


tab = {}  # (flagged, spike_pred, a=-1) -> count
rem_ss = tot_ss = 0
n = 0
for p in PR:
    r = np.arange(p, dtype=np.int64)
    for name, (co, roots) in ftypes(p).items():
        t = t_table(p, co)
        C = Cvec(p, t)
        S = int(C.sum())
        rho = int((t == 0).sum())
        assert int(C[1]) == p - rho
        for a in range(1, p):
            ainv = pow(a, p - 2, p)
            idx = (a * r[None, :] + r[:, None]) % p
            Ea = (C[None, :] * C[idx]).sum(axis=1)
            for b in range(1, p):
                if (a + b) % p == 1:
                    continue
                E = int(Ea[b])
                tau1 = (a + b) % p
                taum1 = ((1 - b) * ainv) % p
                Sp = (p - rho) * (int(C[tau1]) + int(C[taum1]))
                fl = 4 * abs(p * E - S * S) > 2 * p ** 3 and True  # 2|E_c| > p^2  <=>  2|pE - S^2| > p^3
                fl = 2 * abs(p * E - S * S) > p ** 3
                sp = 4 * abs(Sp) > p * p       # |Sp| > p^2/4
                key = (bool(fl), bool(sp), a == p - 1)
                tab[key] = tab.get(key, 0) + 1
                rem_ss += (E - Sp) ** 2 * 1
                tot_ss += E ** 2
                n += 1
print("pairs", n)
print("(flagged, spike>p^2/4, a=-1) : count")
for k in sorted(tab):
    print(k, tab[k])
fl_tot = sum(v for k, v in tab.items() if k[0])
fl_sp = sum(v for k, v in tab.items() if k[0] and k[1])
fl_inv = sum(v for k, v in tab.items() if k[0] and k[2])
fl_expl = sum(v for k, v in tab.items() if k[0] and (k[1] or k[2]))
print(f"flagged {fl_tot}; with spike {fl_sp}; with a=-1 {fl_inv}; explained by spike or a=-1: {fl_expl} = {Fraction(fl_expl, fl_tot)}")
sp_tot = sum(v for k, v in tab.items() if k[1])
print(f"spike predicted {sp_tot}; of which flagged {fl_sp} = {Fraction(fl_sp, sp_tot)}")
print(f"sum E^2 = {tot_ss}, sum (E-Sp)^2 = {rem_ss}, ratio {Fraction(rem_ss, tot_ss)} ~ {rem_ss/tot_ss:.3f} (float for reading only)")
