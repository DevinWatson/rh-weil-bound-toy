F1=[2,1]; F3=[1,2,0,1]
def C(name,f,e,cexp,hexp): return dict(name=name,e=e,f=f,cexp=cexp,hexp=hexp,k=len(cexp)+1)
CONFIGS=[
 C('f1_k3_e2gen',F1,2,[3, 2],0),
 C('f1_k3_e2gen_h',F1,2,[3, 2],3),
 C('f1_k4_e2gen',F1,2,[3, 4, 1],0),
 C('f1_k4_e2gen_h',F1,2,[3, 4, 1],3),
 C('f1_k5_e2gen',F1,2,[3, 0, 2, 1],0),
 C('f1_k5_e2gen_h',F1,2,[3, 0, 2, 1],3),
 C('f1_k6_e2gen',F1,2,[2, 7, 5, 5, 0],0),
 C('f1_k6_e2gen_h',F1,2,[2, 7, 5, 5, 0],3),
]
