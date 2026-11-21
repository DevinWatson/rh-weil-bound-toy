from fractions import Fraction
import collections, itertools
rows = []
for ln in open("m1_all.tsv").read().splitlines()[1:]:
    a = ln.split("\t")
    rows.append((a[0], int(a[1]), int(a[2]), int(a[3]), int(a[4]), int(a[5]), int(a[6]), int(a[7]), int(a[8]), int(a[9])))
out = []
out.append("poly p | #c | #bad | bad&sum0 | sum0 total | sum0 & not bad | bad off-plane")
tot = collections.Counter()
offs = []
for key in sorted(set((r[0], r[1]) for r in rows)):
    R = [r for r in rows if (r[0], r[1]) == key]
    bad = [r for r in R if r[9]]
    s0 = [r for r in R if r[8]]
    bs = [r for r in bad if r[8]]
    nb = [r for r in s0 if not r[9]]
    off = [r for r in bad if not r[8]]
    out.append(f"{key[0]} p={key[1]:2d} | {len(R):4d} | {len(bad):3d} | {len(bs):3d} | {len(s0):3d} | {len(nb):3d} | {len(off):3d}")
    for r in off:
        offs.append(r)
    for r in nb:
        out.append(f"   on-plane NOT bad: c=(1,{r[2]},{r[3]}) N={r[4]} N/p^2={Fraction(r[4], r[1]**2)} (M={r[5]}, roots={r[7]})")
out.append("")
out.append(f"total off-plane bad: {len(offs)}")
for r in offs:
    out.append(f"   {r[0]} p={r[1]} c=(1,{r[2]},{r[3]}) N={r[4]} N/p^2={Fraction(r[4], r[1]**2)} 1+c2+c3={(1+r[2]+r[3])%r[1]}")
# on-plane bad statistics: min N/p^2 over on-plane with c2,c3 != 0
out.append("")
out.append("min and max of N/p^2 over c on the plane (all, c2c3!=0), per poly,p:")
for key in sorted(set((r[0], r[1]) for r in rows)):
    R = [r for r in rows if (r[0], r[1]) == key and r[8]]
    mn = min(Fraction(r[4], r[1] ** 2) for r in R); mx = max(Fraction(r[4], r[1] ** 2) for r in R)
    # reference (p-r)^2/p^2
    out.append(f"  {key} min {mn} ({float(mn):.4f}) max {mx} ({float(mx):.4f}); (p-r0)^2/p^2 = {Fraction((key[1]-R[0][7])**2, key[1]**2)}")
# off-plane max N/p^2 per poly,p
out.append("")
out.append("max N/p^2 over c off the plane, per poly,p (float is a hint):")
for key in sorted(set((r[0], r[1]) for r in rows)):
    R = [r for r in rows if (r[0], r[1]) == key and not r[8]]
    mx = max(R, key=lambda r: Fraction(r[4], r[1] ** 2))
    out.append(f"  {key} max {Fraction(mx[4], mx[1]**2)} ({float(Fraction(mx[4], mx[1]**2)):.4f}) at c=(1,{mx[2]},{mx[3]})")
open("m1_summary.txt", "w").write("\n".join(out) + "\n")
print("\n".join(out))
