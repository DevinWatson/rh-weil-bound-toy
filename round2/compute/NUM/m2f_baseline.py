from fractions import Fraction
files=["m2_exhaustive_11_13.tsv","m2_exhaustive_17.tsv"]
rows=[]
for f in files:
    for ln in open(f).read().splitlines()[1:]:
        a=ln.split("\t")
        rows.append(dict(poly=a[0],p=int(a[1]),c=[1]+list(map(int,a[2:6])),N=int(a[6]),M=int(a[7]),badE=int(a[12]),pa=[x for x in a[14].split(",") if x]))
def anyz(c,p): return any(x%p==0 for x in c[1:])
def anys(c,p):
    for i in range(5):
        for j in range(i+1,6):
            if sum(c[i:j])%p==0 and j-i>=2: return True
    return False
def anyz2(c,p):  # a zero c_i or a consecutive-block sum zero
    return anyz(c,p) or anys(c,p)
out=["Enrichment of simple predicates among 'unexplained excess-bad' c (2(N-M^6/p)>=p^3, not on any of the 15 matching subspaces) vs all c, p=11,13,17 exhaustive"]
for key in sorted(set((r["poly"],r["p"]) for r in rows)):
    G=[r for r in rows if (r["poly"],r["p"])==key]; U=[r for r in G if r["badE"] and not r["pa"]]
    p=key[1]
    if not U: out.append(f"{key}: none"); continue
    b1=sum(anyz(r["c"],p) for r in G)/len(G); u1=sum(anyz(r["c"],p) for r in U)/len(U)
    b2=sum(anyz2(r["c"],p) for r in G)/len(G); u2=sum(anyz2(r["c"],p) for r in U)/len(U)
    out.append(f"{key}: unexplained n={len(U)} of {len(G)} ({len(U)/len(G):.4f}); some c_i=0 (i>=2): {u1:.3f} vs baseline {b1:.3f}; some c_i=0 or zero consecutive-block sum (length>=2): {u2:.3f} vs baseline {b2:.3f}")
open("m2f_baseline.txt","w").write("\n".join(out)+"\n"); print("\n".join(out))
