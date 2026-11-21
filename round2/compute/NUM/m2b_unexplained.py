"""For k=6 exhaustive tables (p=11,13,17): characterise the excess-bad c (2(N-M^6/p) >= p^3) that no full-matching plane explains."""
from fractions import Fraction
import collections
files = ["m2_exhaustive_11_13.tsv", "m2_exhaustive_17.tsv"]
rows = []
for f in files:
    for ln in open(f).read().splitlines()[1:]:
        a = ln.split("\t")
        rows.append(dict(poly=a[0], p=int(a[1]), c=[1] + list(map(int, a[2:6])), N=int(a[6]), M=int(a[7]), r0=int(a[8]),
                         badE=int(a[12]), pa=[x for x in a[14].split(",") if x]))
def preds(c, p):
    P = {}
    for i in range(5):
        P[f"c{i+1}=0"] = c[i] % p == 0
    for i in range(4):
        P[f"c{i+1}+c{i+2}=0"] = (c[i] + c[i + 1]) % p == 0
    for i in range(3):
        P[f"c{i+1}+c{i+2}+c{i+3}=0"] = (c[i] + c[i + 1] + c[i + 2]) % p == 0
    for i in range(2):
        P[f"c{i+1}..c{i+4} sum=0"] = sum(c[i:i + 4]) % p == 0
    P["c1..c5 sum=0"] = sum(c) % p == 0
    return P
out = []
U = [r for r in rows if r["badE"] and not r["pa"]]
out.append(f"excess-bad and not on any full-matching plane ('unexplained'): {len(U)} of {sum(r['badE'] for r in rows)} excess-bad c over {len(rows)} c (p=11,13,17 exhaustive, polys f1..f4 where good)")
names = list(preds([1, 2, 3, 4, 5], 7).keys())
st = {n: [0, 0, 0] for n in names}  # n_pred, n_pred&U, n_pred&badE
anyU = 0
for r in rows:
    P = preds(r["c"], r["p"])
    hit = any(P.values())
    for n, v in P.items():
        if v:
            st[n][0] += 1
            if r["badE"] and not r["pa"]:
                st[n][1] += 1
            if r["badE"]:
                st[n][2] += 1
    if r["badE"] and not r["pa"] and hit:
        anyU += 1
out.append("predicate | #c satisfying | #unexplained satisfying | recall of unexplained | precision (satisfying that are excess-bad)")
for n in names:
    a, b, c = st[n]
    out.append(f"{n} | {a} | {b} | {b/len(U):.3f} | {(c/a if a else float("nan")):.4f}")
out.append(f"union of all predicates covers {anyU} of {len(U)} unexplained = {anyU/len(U):.3f}")
# the rest: unexplained with none of the predicates
rest = [r for r in U if not any(preds(r["c"], r["p"]).values())]
out.append(f"unexplained and satisfying none: {len(rest)}")
# scaling: for unexplained rows, N/p^3 and N/p^(5/2) maxima per (poly,p)
out.append("per (poly,p): max over c not on any full-matching plane of N/p^3 and of N/p^(5/2) (floats are hints); and the same among the rest")
for key in sorted(set((r["poly"], r["p"]) for r in rows)):
    G = [r for r in rows if (r["poly"], r["p"]) == key and not r["pa"]]
    p = key[1]
    m3 = max(r["N"] / p ** 3 for r in G); m25 = max(r["N"] / p ** 2.5 for r in G)
    Gr = [r for r in G if r in rest]
    m3r = max([r["N"] / p ** 3 for r in Gr], default=float("nan")); m25r = max([r["N"] / p ** 2.5 for r in Gr], default=float("nan"))
    out.append(f"{key}: all-off-plane max N/p^3={m3:.3f} N/p^2.5={m25:.3f}; unexplained-none max N/p^3={m3r:.3f} N/p^2.5={m25r:.3f} (n={len(Gr)})")
open("m2b_unexplained.txt", "w").write("\n".join(out) + "\n")
print("\n".join(out))
