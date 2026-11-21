import itertools, json
from modp_fibre import hypothesis_k, rho, p
def cl(c):
    k=len(c)+1
    return hypothesis_k(list(c),k)
cfg=[[1]]
# k=3
for c in [(1,1),(1,2),(1,4)]: cfg.append(list(c))
# k=4: one good, one with rho_2=1 (c1=-c2), one with rho_3=1
good4=[c for c in itertools.product(range(1,5),repeat=3) if not cl(c)]
b2=[c for c in itertools.product(range(1,5),repeat=3) if (2,0) in cl(c) and (3,0) not in cl(c)]
b3=[c for c in itertools.product(range(1,5),repeat=3) if (3,0) in cl(c) and (2,0) not in cl(c)]
print(len(good4),len(b2),len(b3))
cfg += [list(good4[0]),list(good4[5]),list(b2[0]),list(b3[0])]
# k=5
all5=list(itertools.product(range(1,5),repeat=4))
good5=[c for c in all5 if not cl(c)]
A=[c for c in all5 if cl(c)==[(4,1)]]
B2=[c for c in all5 if (2,0) in cl(c) and (4,1) not in cl(c) and (3,0) not in cl(c) and (4,0) not in cl(c)]
B3=[c for c in all5 if (3,0) in cl(c) and (2,0) not in cl(c) and (4,0) not in cl(c)]
B4=[c for c in all5 if (4,0) in cl(c) and (2,0) not in cl(c) and (3,0) not in cl(c)]
print(len(good5),len(A),len(B2),len(B3),len(B4), good5[:3], A[:3])
cfg += [list(good5[0]),list(good5[7]),list(A[0]),list(A[3]),list(B2[0]),list(B3[0]),list(B4[0]),[1,1,1,1]]
print([ (c,cl(c)) for c in cfg if len(c)==4])
json.dump(cfg,open('cfg.json','w'))
