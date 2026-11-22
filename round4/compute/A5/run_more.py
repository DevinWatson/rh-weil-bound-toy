import itertools, random
from fractions import Fraction
from lfun import *
from run_sym import pgcd, deriv, randf
def powersums(a,N):
    # D(u)=sum a_i u^i (poly), p_n from -u D'/D = sum p_n u^n
    a=[Fraction(x) for x in a]+[Fraction(0)]*(N+1)
    p=[Fraction(0)]*(N+1)
    for n in range(1,N+1):
        s=-n*a[n]
        for k in range(1,n): s-=a[n-k]*p[k]
        p[n]=s
    return p
def count_Sn(p,f,n):
    # prime p; field F_{p^n}=F_p[x]/m ; returns sum chi_n(f(x)) via counting sqrt
    m=irreducible_poly_over_Fp(p,n) if n>1 else [0,1]
    def mul(A,B):
        r=[0]*(2*n-1)
        for i,x in enumerate(A):
            if x:
                for j,y in enumerate(B): r[i+j]+=x*y
        r=[t%p for t in r]
        if n==1: return r[:1]
        r=polymod_p(r,m,p); return r+[0]*(n-len(r))
    from collections import Counter
    sq=Counter()
    els=list(itertools.product(range(p),repeat=n))
    for x in els: sq[tuple(mul(list(x),list(x)))]+=1
    tot=0
    for x in els:
        v=[0]*n
        for c in reversed(f):
            v=mul(v,list(x)); v[0]=(v[0]+c)%p
        tot+=sq[tuple(v)]
    return tot-p**n
random.seed(7)
print("== point-count cross check: S_n from F_{p^n} counting vs -p_n from D(u) ==")
for (p,d,N) in [(3,3,6),(3,5,6),(5,3,4),(7,3,4),(5,5,4)]:
    F=GF(p,1); f=randf(F,d); a=Dcoeffs(F,f,d+1); ps=powersums(a,N)
    S=[count_Sn(p,f,n) for n in range(1,N+1)]
    ok=all(S[n-1]==-ps[n] for n in range(1,N+1))
    print(f"p={p} d={d} f={f} D={a} S_n={S} -p_n={[int(-ps[n]) for n in range(1,N+1)]} match={ok}")
print("== even d control (d=4,6): D degree d-1 but symmetry alpha<->q/alpha ==")
for (p,d) in [(3,4),(5,4),(7,4),(3,6),(5,6)]:
    F=GF(p,1)
    for t in range(2):
        f=randf(F,d); a=Dcoeffs(F,f,d+1)
        deg=d-1
        symfull=all(a[deg-i]==a[i]*Fraction(p)**(deg-2*i)/1 if False else True for i in range(1))
        # test: is D(u) divisible by (1-eps u) with eps=+-1 and quotient symmetric of degree d-2 ?
        res=None
        for eps in (1,-1):
            # divide D by (1-eps u): synthetic
            q_=[];r=0
            # D(u)=(1-eps u)Q(u): Q_i = a_i + eps Q_{i-1}
            Q=[a[0]]
            for i in range(1,deg): Q.append(a[i]+eps*Q[-1])
            if a[deg]==-eps*Q[-1]:  # remainder zero
                g2=(d-2)//2
                sym=all(Q[2*g2-i]==p**(g2-i)*Q[i] for i in range(g2+1))
                res=(eps,Q,sym); break
        print(f"q={p} d={d} f={f} D={a[:d]} tail={a[d:]} factor(1-eps u)*symmetric: {res}; D itself pairs alpha<->q/alpha? {a[deg]==p**(deg//2)*a[0] if deg%2==0 else 'n/a (odd degree: cannot pair all)'}")
print("== S0: base change and translation, q=3 -> Q=9 ==")
F3=GF(3,1); F9=GF(3,2)
for f in ([0,2,0,1],[1,1,0,1],[2,2,1,0,1,1]):  # x^3-x ; ... ; degree 5 case
    d=len(f)-1
    if d==5:
        # find squarefree degree 5 over F3
        f=randf(F3,5)
    D3=Dcoeffs(F3,f,d+1)
    D9=Dcoeffs(F9,f,d+1)          # f has coefficients in F_3 subset F_9 (ints 0,1,2 are the prime field elements)
    # predicted: D9(u^2)=D3(u)D3(-u)
    prod=[0]*(2*d)
    for i,x in enumerate(D3[:d]):
        for j,y in enumerate(D3[:d]): prod[i+j]+=x*y*(-1)**j
    pred=[prod[2*i] for i in range(d)]
    # translation by every a in F9 with f(a)!=0
    def ev(F,f,x):
        v=0
        for c in reversed(f): v=F.add[F.mul[v][x]][c]
        return v
    trans_ok=True; na=0
    for a_ in range(9):
        if ev(F9,f,a_)==0: continue
        # f_a(x)=f(x+a): compute coefficients by Horner expansion in polynomial arithmetic over F9
        fa=[0]
        for c in reversed(f):
            # fa = fa*(x+a)+c
            new=[0]*(len(fa)+1)
            for i,t in enumerate(fa):
                new[i+1]=F9.add[new[i+1]][t]
                new[i]=F9.add[new[i]][F9.mul[t][a_]]
            new[0]=F9.add[new[0]][c]; fa=trim(new)
        Da=Dcoeffs(F9,fa,d+1)
        na+=1; trans_ok&= (Da==D9)
    print(f"f={f} D3={D3[:d]} D9={D9[:d]} tail9={D9[d:]} D3(u)D3(-u) at u^2={pred} match={pred==D9[:d]}; translations tested={na} all equal D9: {trans_ok}; roots of f in F3: {[x for x in range(3) if ev(F3,f,x)==0]}")
