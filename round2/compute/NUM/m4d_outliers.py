import random, collections
rows=[ln.split("\t") for ln in open("m4a_random.tsv").read().splitlines()[1:]]
out=["Outliers of Z (random c regenerated from the recorded seeds 'm4a-poly-k-p-j'): which plain contiguous-block sums c_i+...+c_j vanish mod p ?  Predicates tested: block sums (i<=j), c_i = 0 is impossible (entries drawn nonzero).",
"k | threshold |Z|> | #outliers | #outliers with some block sum = 0 | baseline fraction of all samples with some block sum = 0 | most frequent satisfied block among outliers (count)"]
thr={3:4.0,4:4.0,5:3.0,6:2.5,7:2.5,8:2.5}
# recompute index j: file order is poly, p, k, j (loop nesting poly->p->k->j)
idx=collections.defaultdict(int)
data=[]
for r in rows:
    k=int(r[0]); poly=r[1]; p=int(r[2]); 
    key=(poly,p,k); j=idx[key]; idx[key]+=1
    rng=random.Random(f"m4a-{poly}-{k}-{p}-{j}")
    c=[rng.randrange(1,p) for _ in range(k-1)]
    Z=float(r[4])
    blocks=[(i,jj) for i in range(k-1) for jj in range(i,k-1) if jj>i]  # length>=2
    sat=[(i+1,jj+1) for i,jj in blocks if sum(c[i:jj+1])%p==0]
    data.append((k,Z,sat,c,p))
for k in (3,4,5,6,7,8):
    D=[d for d in data if d[0]==k]; O=[d for d in D if abs(d[1])>thr[k]]
    base=sum(1 for d in D if d[2])/len(D); hit=sum(1 for d in O if d[2])
    cnt=collections.Counter(b for d in O for b in d[2])
    out.append(f"{k} | {thr[k]} | {len(O)} | {hit} | {base:.3f} | {cnt.most_common(3)}")
open("m4d_outliers.txt","w").write("\n".join(out)+"\n"); print("\n".join(out))
