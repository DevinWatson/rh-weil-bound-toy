"""Validate stalk outputs Ghat_i(w), w != 0, against the definition sum_y G_i(y) psi(Tr(b_i w y)) computed independently."""
import itertools
from a3lib import *
from validate import field
def check(p,u,n,Z,h,cs,K,ws):
    N=u*n;q=p**u;Q=p**N
    poly=primitive_poly(p,N)
    mul,add,zero,one,X=field(p,N,poly)
    elems={};cur=one;pw=[]
    for i in range(Q-1):
        elems[cur]=i;pw.append(cur);cur=mul(cur,X)
    pw_=lambda l:pw[l%(Q-1)]
    code=lambda c: zero if c is None else pw_(c*((Q-1)//(q-1)))
    def mulpow(z):
        r=one
        for _ in range(p): r=mul(r,z)
        return r
    def tr(z):
        acc=zero;cur=z
        for _ in range(N):
            acc=add(acc,cur);cur=mulpow(cur)
        return acc[0]
    e=2 if p==3 else 3
    allel=[tuple(x) for x in itertools.product(range(p),repeat=N)]
    def t(y):
        s=0
        for z in Z:
            d=tuple((a-b)%p for a,b in zip(y,code(z)))
            if d==zero:return ZW(0,0)
            s+=elems[d]
        j=s%e
        if p==3:return ZW(1,0) if j==0 else ZW(-1,0)
        return [ZW(1,0),ZW(0,1),ZW(-1,-1)][j]
    psi=(lambda a:[ZW(1,0),ZW(0,1),ZW(-1,-1)][a%3]) if p==3 else (lambda a: ZW(1,0) if a%2==0 else ZW(-1,0))
    tv={y:t(y) for y in allel}
    G=dict(tv)
    cfg=[f"w {h} {len(Z)} {' '.join(map(str,Z))} {K} {' '.join(map(str,cs))} {len(ws)} {' '.join(map(str,ws))}"]
    res=run_engine(p,u,n,cfg,"valw")
    bad=0
    for i in range(1,K+1):
        b=mul(code(h),code(cs[i-1]))
        Gh={}
        for y in allel:
            acc=ZW(0,0)
            for x in allel:
                if G[x].iszero():continue
                acc=acc+G[x]*psi(tr(mul(b,mul(x,y))))
            Gh[y]=acc
        for w in ws:
            eng=ZW(*res[("w",n,i,w)]); dp=Gh[code(None if w<0 else w)]
            ok=(eng-dp).iszero(); bad+= (not ok)
        G={y:tv[y]*Gh[y] for y in allel}
    return bad
tot=0
for (p,u,Z,h,cs,K) in [(3,1,[0],0,[0,1,0,0],4),(3,1,[0],1,[0,0,0],3),(2,2,[0,1],0,[0,1,2,1],4),(2,2,[1],2,[2,1,0],3)]:
    for n in (1,2,3):
        if (p**(u*n))**2>5000: continue
        ws=[-1]+list(range(0,p**u-1))
        b=check(p,u,n,Z,h,cs,K,ws); tot+=b
        print(p,u,n,Z,h,cs,"mismatches",b)
print("TOTAL MISMATCHES",tot)
