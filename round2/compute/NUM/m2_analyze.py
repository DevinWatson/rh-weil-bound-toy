from fractions import Fraction
import collections, glob
files = ["m2_exhaustive.tsv", "m2_exhaustive_11_13.tsv", "m2_exhaustive_17.tsv", "m2_random.tsv", "m2_predicted.tsv"]
out = []
def load(f):
    R = []
    for ln in open(f).read().splitlines()[1:]:
        a = ln.split("\t")
        R.append(dict(poly=a[0], p=int(a[1]), c=[1] + list(map(int, a[2:6])), N=int(a[6]), M=int(a[7]), r0=int(a[8]),
                      bad=int(a[10]), E=Fraction(a[11]), badE=int(a[12]), pb=[x for x in a[13].split(",") if x], pa=[x for x in a[14].split(",") if x]))
    return R
out.append("per file, poly, p: n | bad(2N>=p^3) | badE(2(N-M^6/p)>=p^3) | brief-predicted | any-matching-predicted | bad&brief | badE&brief | brief&!bad | badE&!any (unexplained) | bad&!any | planeN/p^3 min..max on brief-predicted (c3..c5 free) vs (p-r0)^3/p^3")
for f in files:
    R = load(f)
    groups = sorted(set((r["poly"], r["p"]) for r in R))
    for (nm, p) in groups:
        G = [r for r in R if r["poly"] == nm and r["p"] == p]
        n = len(G); bad = [r for r in G if r["bad"]]; badE = [r for r in G if r["badE"]]
        pb = [r for r in G if r["pb"]]; pa = [r for r in G if r["pa"]]
        s = f"{f} {nm} p={p}: n={n} | {len(bad)} | {len(badE)} | {len(pb)} | {len(pa)} | {len([r for r in bad if r['pb']])} | {len([r for r in badE if r['pb']])} | {len([r for r in pb if not r['bad']])} | {len([r for r in badE if not r['pa']])} | {len([r for r in bad if not r['pa']])}"
        if pb:
            rat = [Fraction(r["N"], p ** 3) for r in pb]
            s += f" | {float(min(rat)):.3f}..{float(max(rat)):.3f} vs {(p-G[0]['r0'])**3/p**3:.3f}"
        out.append(s)
open("m2_summary.txt", "w").write("\n".join(out) + "\n")
print("\n".join(out))
