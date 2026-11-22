# Exact L-polynomial of y^2=f(x) over F_q via D(u)=sum_{g monic} chi_q(Res(g,f)) u^deg g, integers only.
import itertools, sys
from fractions import Fraction

def irreducible_poly_over_Fp(p,e):
    # monic degree e irreducible over F_p by trial division
    for tail in itertools.product(range(p),repeat=e):
        m=list(tail)+[1]   # low->high
        if e==1 or all(has_no_factor(m,p,d) for d in range(1,e//2+1)):
            if e==1 and True: return m
            return m
def polymod_p(a,b,p):
    a=a[:]
    while len(a)>=len(b):
        c=a[-1]
        if c:
            for i in range(len(b)):
                a[len(a)-len(b)+i]=(a[len(a)-len(b)+i]-c*b[i])%p
        a.pop()
    return a
def has_no_factor(m,p,d):
    for tail in itertools.product(range(p),repeat=d):
        dv=list(tail)+[1]
        r=polymod_p(m,dv,p)
        if all(x==0 for x in r): return False
    return True

class GF:
    def __init__(s,p,e):
        s.p,s.e,s.q=p,e,p**e
        if e==1:
            s.add=[[ (a+b)%p for b in range(p)] for a in range(p)]
            s.mul=[[ (a*b)%p for b in range(p)] for a in range(p)]
        else:
            m=irreducible_poly_over_Fp(p,e)
            def dig(a): return [(a//p**i)%p for i in range(e)]
            def und(v): return sum(v[i]*p**i for i in range(e))
            s.add=[[und([(x+y)%p for x,y in zip(dig(a),dig(b))]) for b in range(s.q)] for a in range(s.q)]
            def mulp(a,b):
                A,B=dig(a),dig(b); r=[0]*(2*e-1)
                for i in range(e):
                    for j in range(e): r[i+j]+=A[i]*B[j]
                r=[x%p for x in r]
                r=polymod_p(r,m,p)
                r+= [0]*(e-len(r))
                return und(r)
            s.mul=[[mulp(a,b) for b in range(s.q)] for a in range(s.q)]
        s.neg=[next(b for b in range(s.q) if s.add[a][b]==0) for a in range(s.q)]
        s.inv=[None]+[next(b for b in range(s.q) if s.mul[a][b]==1) for a in range(1,s.q)]
        sq=set(s.mul[a][a] for a in range(1,s.q))
        s.chi=[0]+[1 if a in sq else -1 for a in range(1,s.q)]
    def sub(s,a,b): return s.add[a][s.neg[b]]

def trim(a):
    a=a[:]
    while a and a[-1]==0: a.pop()
    return a
def pmod(F,a,b):
    a=trim(a); b=trim(b); ib=F.inv[b[-1]]
    while len(a)>=len(b):
        c=F.mul[a[-1]][ib]
        sh=len(a)-len(b)
        if c:
            for i in range(len(b)):
                a[sh+i]=F.sub(a[sh+i],F.mul[c][b[i]])
        a.pop(); a=trim(a)
        if not a: break
    return a
def power(F,x,n):
    r=1
    for _ in range(n): r=F.mul[r][x]
    return r
def res(F,a,b):
    # Resultant of a,b (low->high coefficient lists), a,b nonzero
    a=trim(a); b=trim(b)
    m,n=len(a)-1,len(b)-1
    if n==0: return power(F,b[0],m)
    if m==0: return power(F,a[0],n)
    r=pmod(F,a,b)
    if not r: return 0
    # Res(a,b)=(-1)^{mn} Res(b,a); Res(b,a)=lc(b)^{m-deg r} Res(b,r)
    val=power(F,b[-1],m-(len(r)-1))
    val=F.mul[val][res(F,b,r)]
    if (m*n)%2: val=F.neg[val]
    return val

def Dcoeffs(F,f,N):
    out=[]
    for n in range(N+1):
        tot=0
        for tail in itertools.product(range(F.q),repeat=n):
            g=list(tail)+[1]
            tot+=F.chi[res(F,g,f)] if n>0 else 1
        out.append(tot)
    return out

def lpoly_symmetry(a,q,d):
    deg=d-1
    sym=all(a[deg-i]*1==a[i]*Fraction(q)**(deg//2-i)*1 if True else 0 for i in range(deg+1)) if deg%2==0 else None
    return sym

if __name__=="__main__":
    pass
