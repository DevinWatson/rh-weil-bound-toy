"""k=6: the three one-parameter families of c with c1=1 predicted by the brief's matchings (3 of the 5; the other two need c1=0).
A: 1-3 2-5 4-6 : c=(1,-1,0,u,-u)   B: 1-4 2-5 3-6 : c=(1,u,0,-1,-u)   D: 1-5 2-4 3-6 : c=(1,u,-u,-1,0)
Compare N with (p-r0)^3 (the plane) and with (p-r0)^2 M^2 (a 4-dim component whose two free coordinates carry t, summing to M each).
Exact ratios are Fractions; the medians printed are floats (hints)."""
import collections, statistics
from fractions import Fraction
G = collections.defaultdict(list)
for ln in open("m2d_large_p.tsv").read().splitlines()[1:]:
    a = ln.split("\t")
    if a[2] != "plane": continue
    nm, p = a[0], int(a[1]); c2, c3, c4, c5 = map(int, a[3:7]); N = int(a[7]); M = int(a[8]); r0 = int(a[9])
    for fam, ok in (("A", c2 == p-1 and c3 == 0 and (c4+c5) % p == 0), ("B", c3 == 0 and c4 == p-1 and (c2+c5) % p == 0), ("D", c4 == p-1 and c5 == 0 and (c2+c3) % p == 0)):
        if ok and not (c2 == p-1 and c3 == 0 and c4 == p-1) :   # skip overlap points
            G[(nm, p, fam)].append((N, M, r0, Fraction(N, (p-r0)**3), Fraction(N, (p-r0)**2*M**2) if M else None))
out = ["poly p family | n | median N/(p-r0)^3 | median N/((p-r0)^2 M^2) (M=0 -> n/a) | M"]
for k in sorted(G):
    v = G[k]
    m1 = statistics.median([float(x[3]) for x in v])
    r2 = [float(x[4]) for x in v if x[4] is not None]
    m2 = statistics.median(r2) if r2 else float("nan")
    out.append(f"{k[0]} p={k[1]} {k[2]} | {len(v)} | {m1:.3f} | {m2:.3f} | M={v[0][1]}")
open("m2e_family_ratio.txt", "w").write("\n".join(out) + "\n"); print("\n".join(out))
