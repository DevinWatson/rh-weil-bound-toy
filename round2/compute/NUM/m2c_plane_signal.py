from fractions import Fraction
import statistics
rows=[]
for f in ["m2_exhaustive_11_13.tsv","m2_exhaustive_17.tsv"]:
    for ln in open(f).read().splitlines()[1:]:
        a=ln.split("\t")
        rows.append(dict(poly=a[0],p=int(a[1]),N=int(a[6]),M=int(a[7]),r0=int(a[8]),E=Fraction(a[11]),pb=[x for x in a[13].split(",") if x],pa=[x for x in a[14].split(",") if x]))
out=["k=6, exhaustive p=11,13,17.  E = N - M^6/p (exact).  Compare, per (poly,p):",
"  planes (brief-set predicted c): median of (E-(p-r0)^3)/p^(5/2)  [if the plane mechanism holds this stays O(1)]  and median of E/p^3 (should be near (p-r0)^3/p^3)",
"  rest (not predicted by any of the 15 matchings): median, 99th percentile and max of E/p^(5/2)"]
for key in sorted(set((r["poly"],r["p"]) for r in rows)):
    G=[r for r in rows if (r["poly"],r["p"])==key]; p=key[1]; r0=G[0]["r0"]
    P=[r for r in G if r["pb"]]; R=[r for r in G if not r["pa"]]
    d=[float((r["E"]-(p-r0)**3)/Fraction(p)**2/Fraction(p**1)**0)/p**0.5 for r in P]  # /p^(5/2)
    e=sorted(float(r["E"])/p**2.5 for r in R)
    out.append(f"{key}: n_planes={len(P)} median (E-(p-r0)^3)/p^2.5={statistics.median(d):.2f} (min {min(d):.2f}, max {max(d):.2f}); median E/p^3={statistics.median([float(r['E'])/p**3 for r in P]):.3f} vs (p-r0)^3/p^3={(p-r0)**3/p**3:.3f} | rest n={len(R)} median E/p^2.5={statistics.median(e):.2f} q99={e[int(0.99*len(e))]:.2f} max={e[-1]:.2f}")
open("m2c_plane_signal.txt","w").write("\n".join(out)+"\n"); print("\n".join(out))
