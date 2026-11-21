import glob, math, statistics
rows=[]
for f in sorted(glob.glob("m3_f*_k*.tsv")):
    for ln in open(f).read().splitlines()[1:]:
        a=ln.split("\t"); rows.append(dict(poly=a[0],k=int(a[1]),ct=a[2],p=int(a[3]),A1=float(a[8]),A2=float(a[11])))
out=["log-log least-squares fit of binned mean|A1| against p (bins of 8 consecutive primes, p>=11), all three c types pooled, per (poly,k): slope (hint; -0.5 means A1 ~ p^(-1/2))"]
for poly in ("f1","f2","f4"):
    for k in (4,5,6,7,8):
        G=sorted([r for r in rows if r["poly"]==poly and r["k"]==k and r["p"]>=11], key=lambda r:r["p"])
        ps=sorted(set(r["p"] for r in G)); xs=[];ys=[]
        for i in range(0,len(ps)-7,8):
            b=ps[i:i+8]; v=[abs(r["A1"]) for r in G if r["p"] in b]
            xs.append(math.log(statistics.mean(b))); ys.append(math.log(statistics.mean(v)))
        n=len(xs); mx=sum(xs)/n; my=sum(ys)/n
        sl=sum((x-mx)*(y-my) for x,y in zip(xs,ys))/sum((x-mx)**2 for x in xs)
        out.append(f"{poly} k={k}: slope {sl:+.2f} over {n} bins (p from {ps[0]} to {ps[-1]}); first bin mean|A1| {math.exp(ys[0]):.3f}, last {math.exp(ys[-1]):.3f}")
open("m3c_fit.txt","w").write("\n".join(out)+"\n"); print("\n".join(out))
