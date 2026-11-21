def C(name,f,e,cexp,hexp):
    return dict(name=name,e=e,f=f,cexp=cexp,hexp=hexp,k=len(cexp)+1)
CONFIGS=[
 C('x2m1_k2',[2,0,1],1,[0],0),
 C('x2p1_k2',[1,0,1],1,[0],0),
 C('x4p..x_k2',[2,1,0,0,1],1,[0],0),
]
