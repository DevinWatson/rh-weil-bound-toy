F1=[2,1]; F3=[1,2,0,1]
def C(name,f,e,cexp,hexp,k=None):
    return dict(name=name,e=e,f=f,cexp=cexp,hexp=hexp,k=len(cexp)+1)
CONFIGS=[
 C('f1_k2_e1',F1,1,[0],0),
 C('f1_k3_e1',F1,1,[0,0],0),
 C('f1_k3_e1_h-',F1,1,[0,0],1),
 C('f1_k4_e1_sum0',F1,1,[0,0,0],0),
 C('f1_k4_e1_c11m1',F1,1,[0,0,1],0),
 C('f3_k2_e1',F3,1,[0],0),
 C('f3_k2_e1_h-',F3,1,[0],1),
 C('f3_k3_e1',F3,1,[0,0],0),
 C('f3_k4_e1_sum0',F3,1,[0,0,0],0),
]
