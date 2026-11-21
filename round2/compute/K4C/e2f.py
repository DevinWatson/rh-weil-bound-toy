"""E2 (fifth pass): do palindromic c (c1 = c3, i.e. a = -1, tau an involution; Q invariant under the reversal
x_i -> x_{5-i}) have a systematically larger E?  For p in 31..101, four f, b != 0, outside the line a+b=1:
mean of E/p^2 (exact Fraction) in the classes a=-1, a=1, other.  Report the mean over (p,f) of the class means,
and the number of (p,f) with class mean > overall other-mean."""
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


lines = []
acc = {"a=-1": [], "a=1": [], "other": []}
for p in PR:
    r = np.arange(p, dtype=np.int64)
    for name, (co, roots) in ftypes(p).items():
        t = t_table(p, co)
        C = Cvec(p, t)
        cls = {"a=-1": [0, 0], "a=1": [0, 0], "other": [0, 0]}
        for a in range(1, p):
            idx = (a * r[None, :] + r[:, None]) % p
            Ea = (C[None, :] * C[idx]).sum(axis=1)
            k = "a=-1" if a == p - 1 else ("a=1" if a == 1 else "other")
            for b in range(1, p):
                if (a + b) % p == 1:
                    continue
                cls[k][0] += int(Ea[b])
                cls[k][1] += 1
        row = {k: Fraction(v[0], v[1] * p * p) for k, v in cls.items()}
        for k in acc:
            acc[k].append(row[k])
        lines.append(f"p={p} {name}: " + "  ".join(f"{k}: {float(row[k]):+.4f}" for k in row) + "  (floats for reading only)")
n = len(acc["a=-1"])
for k in acc:
    m = sum(acc[k]) / n
    lines.append(f"mean over {n} (p,f) of the class mean of E/p^2: {k}: {float(m):+.4f}")
pos = sum(1 for x, y in zip(acc["a=-1"], acc["other"]) if x > y)
lines.append(f"(p,f) with mean(a=-1) > mean(other): {pos} of {n}")
pos0 = sum(1 for x in acc["a=-1"] if x > 0)
lines.append(f"(p,f) with mean(a=-1) > 0: {pos0} of {n}")
open("e2f_out.txt", "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("\n".join(lines[-6:]))
