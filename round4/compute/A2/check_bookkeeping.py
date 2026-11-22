# A2 exact bookkeeping checks (exact Fractions only; no floating point).
# This checks ARITHMETIC CONSISTENCY of formulas read from Laumon's page images; it does not prove them.
import random, sys
from fractions import Fraction as Fr
out=[]
def P(*a):
    s=' '.join(str(x) for x in a); out.append(s); print(s)

# ---- Part 1: local Fourier transform rank/Swan/slope maps (Laumon 2.4.3, journal pp. 163-164) ----
def A(r,s):  return (r+s, s)        # (0,inf'): r' = r+s, s' = s            (i)b
def B(r,s):  return (r-s, s)        # (inf,0'): r' = r-s, s' = s, slopes<1  (ii)b
def C(r,s):  return (s-r, s)        # (inf,inf'): r' = s-r, s' = s, slopes>1 (iii)b
ok=True; n=0
for r in range(1,40):
    for s in range(0,120):
        lam=Fr(s,r)
        # (0,inf') then (inf',0): identity on every V (slope any)
        r1,s1=A(r,s); assert Fr(s1,r1)<1              # image has slopes in [0,1[
        r2,s2=B(r1,s1); assert (r2,s2)==(r,s); n+=1  # quasi-inverse formula (i)c
        assert Fr(s1,r1)==lam/(1+lam)                 # slope map lambda/(1+lambda)
        if lam<1:                                      # (inf,0') on slopes in [0,1[
            r3,s3=B(r,s); assert Fr(s3,r3)==lam/(1-lam)
            r4,s4=A(r3,s3); assert (r4,s4)==(r,s); n+=1  # quasi-inverse (ii)c: back via (0',inf)
        if lam>1:                                      # (inf,inf') on slopes >1
            r5,s5=C(r,s); assert Fr(s5,r5)==lam/(lam-1) and Fr(s5,r5)>1
            r6,s6=C(r5,s5); assert (r6,s6)==(r,s); n+=1  # involution (iii)c
        if lam==1: assert B(r,s)[0]==0 and C(r,s)[0]==0   # slope exactly 1 killed by (inf,0') and (inf,inf')
        if lam<=1: assert C(r,s)[0]<=0                # (iii)b zero on [0,1]: formula would give nonpositive rank
        if lam>=1: assert B(r,s)[0]<=0                # (ii)b zero on [1,inf[
P('part1: slope/rank maps consistent with quasi-inverses and vanishing ranges; cases checked:',n)
# round-3 report D wrote F^(inf,0') zero on ]1,inf[ ; the page (journal 163, (ii)b) says [1,inf[ and the formula r-s forces it:
P('part1: at slope exactly 1 the formula r-s gives 0, so zero on [1,inf[ (not only ]1,inf[) is forced by (ii)b')

# ---- Part 2: toy dictionary: rank recursion rho_i = d rho_{i-1} + rho_{i-2} from 2.3.1.1 (i)-(iii) bookkeeping ----
def run(d,kmax,seed):
    rnd=random.Random(seed)
    # generic rational data: roots Z (distinct nonzero), scalings c_i nonzero
    while True:
        Z=[Fr(rnd.randint(1,10**6),rnd.randint(1,10**3)) for _ in range(d)]
        if len(set(Z))==d: break
    # P_1: rank 1, finite singular {z:1}, freq dict at infinity {0:1} (tame T^0 rank 1)
    rank=1; fin={z:Fr(1) for z in Z}; freq={Fr(0):1}
    rhos=[]
    for i in range(1,kmax):
        b=Fr(rnd.randint(1,10**6),rnd.randint(1,10**3))*(1 if rnd.random()<.5 else -1)  # b_i = h c_i
        rho=sum(fin.values())                                   # (i): rank of Q_i = sum a_s(P_i) (no slope>1 part)
        # Sing(Q_i) finite: -a/b for a in freq (a!=0) with a_w = rank T^a ; and 0 with a_0 = rank T^0
        sing={}
        for a,m in freq.items():
            w = (-a)/b
            sing[w]=sing.get(w,0)+m                              # (ii)/(iii)
        # Q_i at infinity': frequencies b*s with rank a_s(P_i)
        newfreq={}
        for s,a_s in fin.items():
            newfreq[b*s]=newfreq.get(b*s,0)+a_s
        # genericity (G_k): Z must not meet Sing(Q_i)
        if any(z in sing for z in Z): return None
        # P_{i+1} = j_!L (x) Q_i
        fin={z:Fr(rho) for z in Z}
        for w,m in sing.items(): fin[w]=Fr(m)
        freq=newfreq; rhos.append(rho)
        # internal check by involutivity: sum of a_w over Sing(Q_i) must equal rank of P_i (rank of FT FT P_i)
        assert sum(sing.values())==rank, (sum(sing.values()),rank)
        rank=rho
    return rhos
for d in (1,2,3,4,5,7):
    for seed in (1,2,3):
        rh=run(d,9,seed)
        if rh is None: P('d=%d seed=%d: genericity (G_k) failed for the random draw'%(d,seed)); continue
        rec=[1,]+rh   # rho_0 = rank P_1 = 1
        good=all(rec[j]==d*rec[j-1]+(rec[j-2] if j>=2 else 0) for j in range(1,len(rec)))
        P('d=%d seed=%d ranks rho_0..%d = %s recursion %s'%(d,seed,len(rec)-1,rec,'OK' if good else 'FAIL'))
open('check_bookkeeping_out.txt','w').write('\n'.join(out)+'\n')
