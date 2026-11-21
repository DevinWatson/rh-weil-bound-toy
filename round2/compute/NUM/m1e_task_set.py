from fractions import Fraction
rows=[]
for ln in open("m1_all.tsv").read().splitlines()[1:]:
    a=ln.split("\t"); rows.append((a[0],*map(int,a[1:10])))
out=["Task set p in {5,7,11,13,17,19,23}: per poly: p, #good c, #bad(2N>=p^2), bad on c1+c2+c3=0 (any c3), bad on plane with c3!=0, bad off plane"]
tot=[0,0,0,0]
for nm in ("f1","f2","f3","f4"):
    for p in (5,7,11,13,17,19,23):
        R=[r for r in rows if r[0]==nm and r[1]==p]
        if not R: out.append(f"{nm} p={p} excluded"); continue
        bad=[r for r in R if r[9]]; onp=[r for r in bad if r[8]]; onp3=[r for r in onp if r[3]!=0]
        out.append(f"{nm} p={p}: c={len(R)} bad={len(bad)} bad_on_plane={len(onp)} (c3!=0: {len(onp3)}) off={len(bad)-len(onp)}")
        tot[0]+=len(bad); tot[1]+=len(onp); tot[2]+=len(onp3); tot[3]+=len(bad)-len(onp)
out.append(f"TOTAL bad={tot[0]} on plane={tot[1]} (c3!=0 {tot[2]}) off plane={tot[3]}")
open("m1_task_set.txt","w").write("\n".join(out)+"\n"); print("\n".join(out))
