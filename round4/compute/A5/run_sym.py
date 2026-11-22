import itertools, random, sys
from fractions import Fraction
from lfun import *
random.seed(20261121)
def pgcd(F,a,b):
    a=trim(a);b=trim(b)
    while b: a,b=b,pmod(F,a,b)
    return a
def deriv(F,f):
    out=[]
    for i in range(1,len(f)):
        c=0
        for _ in range(i%F.p): c=F.add[c][f[i]]
        out.append(c)
    return out
def randf(F,d):
    while True:
        f=[random.randrange(F.q) for _ in range(d)]+[random.randrange(1,F.q)]
        if f[0]==0: continue
        g=pgcd(F,f,deriv(F,f))
        if len(trim(g))==1: return f
def main():
    cases=[(3,1,3),(3,1,5),(3,1,7),(5,1,3),(5,1,5),(7,1,3),(7,1,5),(11,1,3),(13,1,3),(3,2,3),(3,2,5),(5,2,3),(5,1,7)]
    print("odd d: coefficients a_0..a_{d+1} of D(u)=sum_g chi(Res(g,f))u^deg g; expect zero for n>=d, a_{2g-i}=q^{g-i}a_i")
    allok=True
    for (p,e,d) in cases:
        F=GF(p,e); q=F.q; g=(d-1)//2
        for trial in range(3 if q**(d+1)<2e5 else 1):
            f=randf(F,d)
            a=Dcoeffs(F,f,d+1)
            poly=a[:d]; tail=a[d:]
            sym=all(poly[2*g-i]==q**(g-i)*poly[i] for i in range(g+1))
            # a_{2g}=q^g a_0 is part of the check (i=0)
            ok=sym and all(t==0 for t in tail)
            allok&=ok
            print(f"q={q} d={d} f={f} D={a} sym={sym} tail_zero={all(t==0 for t in tail)}")
    print("ALL OK" if allok else "FAILURE")

if __name__=='__main__': main()
