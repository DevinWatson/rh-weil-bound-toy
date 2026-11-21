F1=[2,1]; F3=[1,2,0,1]
def C(name,f,e,cexp,hexp): return dict(name=name,e=e,f=f,cexp=cexp,hexp=hexp,k=len(cexp)+1)
CONFIGS=[
 C('f1_k3_bad',F1,1,[0, 1],0),
 C('f3_k3_bad',F3,1,[0, 1],0),
 C('f1_k4_bad_a',F1,1,[0, 0, 1],0),
 C('f1_k4_bad_b',F1,1,[0, 1, 0],0),
 C('f3_k4_bad_a',F3,1,[0, 0, 1],0),
 C('f3_k4_bad_b',F3,1,[0, 1, 0],0),
 C('f1_k5_ones',F1,1,[0, 0, 0, 0],0),
 C('f1_k6_ones',F1,1,[0, 0, 0, 0, 0],0),
 C('f3_k5_ones',F3,1,[0, 0, 0, 0],0),
 C('f3_k6_ones',F3,1,[0, 0, 0, 0, 0],0),
 C('f1_k7_ones',F1,1,[0, 0, 0, 0, 0, 0],0),
 C('f1_k5_ones_h',F1,1,[0, 0, 0, 0],1),
]
