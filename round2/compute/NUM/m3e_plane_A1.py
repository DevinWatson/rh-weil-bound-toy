import statistics
from fractions import Fraction
rows=[]
for f in ("m1_all_extA.tsv","m1_all_extB.tsv"):
    for ln in open(f).read().splitlines()[1:]:
        a=ln.split("\t"); rows.append((a[0],*map(int,a[1:10])))
out=["k=4, A1 = (pN-M^4)/((p-1)p^2) exactly from the M1 tables, p in 37..73: c on the plane (c1+c2+c3=0, c3!=0) versus all other c with c3 != 0 (floats are hints from exact Fractions)"]
for p in sorted(set(r[1] for r in rows)):
    pl=[];ot=[]
    for r in rows:
        if r[1]!=p: continue
        nm,_,c2,c3,N,M,t0,r0,s0,bad=r
        A1=float(Fraction(p*N-M**4,(p-1)*p*p))
        if c3==0: continue
        (pl if s0 else ot).append(A1)
    out.append(f"p={p}: plane n={len(pl)} median A1={statistics.median(pl):.3f} min {min(pl):.3f} max {max(pl):.3f} | other n={len(ot)} median {statistics.median(ot):+.3f} RMS {statistics.mean([x*x for x in ot])**0.5:.3f}")
open("m3e_plane_A1.txt","w").write("\n".join(out)+"\n"); print("\n".join(out))
