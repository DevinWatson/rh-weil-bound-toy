"""E3: split C(r) = -a(r) - chi(r) (r != 0) and report the four pieces of E = sum_r C(r) C(tau r), tau(r) = -c3 r - c2 (c1 = 1).
Definition (exact): for r != 0, a(r) := -C(r) - chi(r) with C(r) = sum_x t(x) t(r x).  For r with f(x)f(rx) squarefree
(r != 1 and r not a ratio of roots) this is the Frobenius trace on the genus d-1 curve y^2 = f(x) f(rx) by the
point count (affine points p + C(r), two points at infinity when chi(r)=1 and none when chi(r)=-1, i.e. 1 + chi(r);
the number of points is p + 1 - a(r)).  For the other r the same formula DEFINES a(r).
Pieces:  S_aa = sum a(r)a(tau r), S_ach = sum a(r) chi(tau r), S_cha = sum chi(r) a(tau r), S_chch = sum chi(r) chi(tau r)
over r with r != 0 and tau(r) != 0;   B = boundary terms with r = 0 or tau(r) = 0 (C(0) = t0 M).
Check: S_aa + S_ach + S_cha + S_chch + B = E exactly.  Also reports the spike term of a(1) = -(p - rho) - 1."""
from fractions import Fraction
from core import *

PR = [p for p in primes_upto(199) if p >= 5]
POLYS = {"x^3+x+1": [1, 1, 0, 1], "x^3-x+3": [3, -1, 0, 1], "x^5+x+1": [1, 1, 0, 0, 0, 1]}
CS = {"c=(1,1,1)": lambda p: (1, 1, 1), "c=(1,2,3)": lambda p: (1, 2, 3), "c=(1,3,5)": lambda p: (1, 3, 5),
      "c=(1,1,-2) [c1+c2+c3=0]": lambda p: (1, 1, p - 2)}
rows = []
agg = {}
for fname, co in POLYS.items():
    for p in PR:
        if not squarefree_mod_p(co, p) or co[0] % p == 0:
            continue
        chi = chi_table(p)
        t = chi[poly_vals(p, co)]
        C = Cvec(p, t)
        M, t0 = int(t.sum()), int(t[0])
        a_ = -C - chi            # a(r) for r != 0 ; entry 0 unused
        r = np.arange(p, dtype=np.int64)
        for cname, cf in CS.items():
            c = cf(p)
            if any(x % p == 0 for x in c):
                continue
            A, B_ = (-c[2]) % p, (-c[1]) % p
            tau = (A * r + B_) % p
            E = int((C * C[tau]).sum())
            mask = (r != 0) & (tau != 0)
            Saa = int((a_[r[mask]] * a_[tau[mask]]).sum())
            Sach = int((a_[r[mask]] * chi[tau[mask]]).sum())
            Scha = int((chi[r[mask]] * a_[tau[mask]]).sum())
            Scc = int((chi[r[mask]] * chi[tau[mask]]).sum())
            Bnd = int((C[r[~mask]] * C[tau[~mask]]).sum())
            assert Saa + Sach + Scha + Scc + Bnd == E, (fname, p, c)
            N4 = -p + t0 * t0 * M * M + E
            # spike: contribution of r = 1 and r = tau^{-1}(1) to S_aa, separately
            rho = int((t == 0).sum())
            rows.append((fname, cname, p, M, t0, rho, E, Saa, Sach, Scha, Scc, Bnd, N4))
            agg.setdefault((fname, cname), []).append((p, E, Saa, Sach, Scha, Scc, Bnd, N4))
with open("e3_rows.tsv", "w", encoding="utf-8") as fh:
    fh.write("f\tc\tp\tM\tt0\trho\tE\tS_aa\tS_ach\tS_cha\tS_chch\tB\tN4\n")
    for row in rows:
        fh.write("\t".join(map(str, row)) + "\n")
out = []
for (fname, cname), L in agg.items():
    n = len(L)
    names = ["E", "S_aa", "S_ach", "S_cha", "S_chch", "B", "N4"]
    out.append(f"{fname} {cname}: {n} primes (5..199)")
    for j, nm in enumerate(names):
        vals = [x[1 + j] for x in L]
        pos = sum(v > 0 for v in vals)
        neg = sum(v < 0 for v in vals)
        zero = n - pos - neg
        ratios = [Fraction(v, x[0] ** 2) for v, x in zip(vals, L)]
        hi = [Fraction(v, x[0] ** 2) for v, x in zip(vals, L) if x[0] > 100]
        mean_hi = sum(hi) / len(hi)
        mx = max(ratios, key=abs)
        # also sizes against p^(3/2)
        r32 = [abs(v) * abs(v) / x[0] ** 3 for v, x in zip(vals, L)]  # (v/p^1.5)^2
        out.append(f"   {nm:7s} pos {pos:3d} neg {neg:3d} zero {zero:2d}  mean over p>100 of piece/p^2 = {float(mean_hi):+.4f}  max|piece|/p^2 = {float(abs(mx)):.4f} (floats for reading only; integers are in e3_rows.tsv)")
open("e3_summary.txt", "w", encoding="utf-8").write("\n".join(out) + "\n")
print("\n".join(out))
