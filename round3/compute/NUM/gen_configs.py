from cond import *
from predicted import predict
F1=[2,1]; F3=[1,2,0,1]
lines=["F1=[2,1]; F3=[1,2,0,1]","def C(name,f,e,cexp,hexp): return dict(name=name,e=e,f=f,cexp=cexp,hexp=hexp,k=len(cexp)+1)","CONFIGS=["]
cfgs2=[]
for k in (3,4,5,6):
    c=find_c(F1,2,k,seed=k)
    ok=claimB_ok(F1,2,c)
    print('f1 e2 k',k,c,ok,predict(F1,2,c))
    lines.append(" C('f1_k%d_e2gen',F1,2,%s,0),"%(k,c))
    lines.append(" C('f1_k%d_e2gen_h',F1,2,%s,3),"%(k,c))
lines.append("]")
open('configs2.py','w').write("\n".join(lines)+"\n")
# bad configs
bad=[('f1_k3_bad',F1,1,[0,1]),('f3_k3_bad',F3,1,[0,1]),('f1_k4_bad_a',F1,1,[0,0,1]),('f1_k4_bad_b',F1,1,[0,1,0]),('f3_k4_bad_a',F3,1,[0,0,1]),('f3_k4_bad_b',F3,1,[0,1,0]),
 ('f1_k5_ones',F1,1,[0]*4),('f1_k6_ones',F1,1,[0]*5),('f3_k5_ones',F3,1,[0]*4),('f3_k6_ones',F3,1,[0]*5),('f1_k7_ones',F1,1,[0]*6),
 ('f1_k5_ones_h',F1,1,[0]*4),]
lines=["F1=[2,1]; F3=[1,2,0,1]","def C(name,f,e,cexp,hexp): return dict(name=name,e=e,f=f,cexp=cexp,hexp=hexp,k=len(cexp)+1)","CONFIGS=["]
for n,f,e,c in bad:
    h=1 if n.endswith('_h') else 0
    ok=claimB_ok(f,e,c); print(n,c,ok)
    lines.append(" C('%s',%s,%d,%s,%d),"%(n,'F1' if f==F1 else 'F3',e,c,h))
lines.append("]")
open('configs3.py','w').write("\n".join(lines)+"\n")
