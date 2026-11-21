import glob, statistics, collections
out=[]
wins=[(5,50),(51,150),(151,300),(301,700)]
out.append("A1 = (pN-M^k)/((p-1)p^(k/2)),  A2 = mean_{h!=0}|S(h)|^2/p^k.  Windows of p; per (poly,k,ctype): n, mean A1, mean |A1|, max |A1|; A2: n, mean, min, max, mean |A2 - nearest int|, (floats are hints computed from exact Fractions)")
rows=[]
for f in sorted(glob.glob("m3_f*_k*.tsv")):
    for ln in open(f).read().splitlines()[1:]:
        a=ln.split("\t"); rows.append(dict(poly=a[0],k=int(a[1]),ct=a[2],p=int(a[3]),A1=float(a[8]),A2=float(a[11]),A2dev=float(a[13]),dv=int(a[14])))
out.append("divisibility of p*sum N^2 - M^(2k) by (p-1): "+str(collections.Counter((r['dv']) for r in rows)))
for poly in ("f1","f2","f4"):
  for k in (4,5,6,7,8):
    for ct in ("ones","rand1","rand2"):
        for lo,hi in wins:
            G=[r for r in rows if r['poly']==poly and r['k']==k and r['ct']==ct and lo<=r['p']<=hi]
            if not G: continue
            a1=[r['A1'] for r in G]; a2=[r['A2'] for r in G]; dv=[abs(r['A2dev']) for r in G]
            out.append(f"{poly} k={k} {ct:5s} p[{lo},{hi}] n={len(G):3d} | A1 mean {statistics.mean(a1):+.3f} mean|.| {statistics.mean(map(abs,a1)):.3f} max|.| {max(map(abs,a1)):.3f} | A2 mean {statistics.mean(a2):.3f} min {min(a2):.3f} max {max(a2):.3f} mean|A2-int| {statistics.mean(dv):.3f}")
open("m3_summary.txt","w").write("\n".join(out)+"\n"); print(len(out))
