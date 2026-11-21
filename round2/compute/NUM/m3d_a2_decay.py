import glob, math, statistics
rows=[]
for f in sorted(glob.glob("m3_f1_k*.tsv"))+sorted(glob.glob("m3_f2_k*.tsv"))+sorted(glob.glob("m3_f4_k*.tsv")):
    for ln in open(f).read().splitlines()[1:]:
        a=ln.split("\t"); rows.append(dict(poly=a[0],k=int(a[1]),ct=a[2],p=int(a[3]),A2=float(a[11])))
out=["A2: per k and c type (f1,f2,f4 pooled), mean over primes in p-windows, and mean |A2 - target| with target 2 for c = ones and 1 for random c; log-log slope of binned mean|A2-target| (bins of 8 primes, p>=11) (floats are hints)"]
for k in (2,3,4,5,6,7,8):
    for ct,tg in (("ones",2),("rand1",1),("rand2",1)):
        G=sorted([r for r in rows if r["k"]==k and r["ct"]==ct and r["p"]>=11],key=lambda r:r["p"])
        if not G: continue
        ps=sorted(set(r["p"] for r in G)); xs=[];ys=[]
        for i in range(0,len(ps)-7,8):
            b=ps[i:i+8]; v=[abs(r["A2"]-tg) for r in G if r["p"] in b]
            xs.append(math.log(statistics.mean(b))); ys.append(math.log(statistics.mean(v)))
        n=len(xs); mx=sum(xs)/n; my=sum(ys)/n
        sl=sum((x-mx)*(y-my) for x,y in zip(xs,ys))/sum((x-mx)**2 for x in xs)
        last=[r["A2"] for r in G if r["p"]>=200 and r["poly"]=="f1"]
        out.append(f"k={k} {ct}: target {tg}; mean A2 over all p>=11: {statistics.mean(r['A2'] for r in G):.3f}; f1 p>=200: mean {statistics.mean(last):.3f} (n={len(last)}); mean|A2-target| first bin {math.exp(ys[0]):.3f} last bin {math.exp(ys[-1]):.3f}; slope {sl:+.2f}")
open("m3d_a2_decay.txt","w").write("\n".join(out)+"\n"); print("\n".join(out))
