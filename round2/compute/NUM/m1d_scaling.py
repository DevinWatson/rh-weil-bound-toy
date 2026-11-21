from fractions import Fraction
import collections
rows = []
for f in ["m1_all.tsv", "m1_all_extA.tsv", "m1_all_extB.tsv"]:
    for ln in open(f).read().splitlines()[1:]:
        a = ln.split("\t"); rows.append((a[0], *map(int, a[1:10])))
out = []
out.append("Predicate PLANE = (c1+c2+c3=0 and c3!=0) vs BAD = (2N>=p^2), over all c=(1,c2,c3)")
for lo, hi in ((5, 31), (37, 73), (59, 73), (5, 73)):
    R = [r for r in rows if lo <= r[1] <= hi]
    tot = len(R)
    bad = [r for r in R if r[9]]
    pl = [r for r in R if r[8] and r[3] != 0]
    both = [r for r in pl if r[9]]
    out.append(f"p in [{lo},{hi}]: #c={tot} bad={len(bad)} plane={len(pl)} plane&bad={len(both)} recall(bad covered by plane)={len(both)}/{len(bad)}={len(both)/len(bad):.3f} precision(plane that is bad)={len(both)}/{len(pl)}={len(both)/len(pl):.4f}")
out.append("")
out.append("Scaling of off-plane c (c3 != 0, 1+c2+c3 != 0): max N/p^(3/2) and min N/p^(3/2), and max |N - M^4/p|/p^(3/2) (floats are hints)")
out.append("poly p | max N/p^1.5 | min N/p^1.5 | max (N-M^4/p)/p^1.5")
for key in sorted(set((r[0], r[1]) for r in rows)):
    R = [r for r in rows if (r[0], r[1]) == key and not r[8] and r[3] != 0]
    p = key[1]
    mx = max(r[4] for r in R) / p ** 1.5; mn = min(r[4] for r in R) / p ** 1.5
    me = max(r[4] - r[5] ** 4 / p for r in R) / p ** 1.5
    out.append(f"{key[0]} p={p:2d} | {mx:6.2f} | {mn:6.2f} | {me:6.2f}")
open("m1d_scaling.txt", "w").write("\n".join(out) + "\n")
print("\n".join(out[:6]))
