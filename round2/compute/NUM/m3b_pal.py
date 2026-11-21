"""palindromic c (c_i = c_{k-i}), random entries, f1: does A2 go to 2 like c = ones (reversal symmetry x_i <-> x_{k+1-i})?"""
import sys, random
from fractions import Fraction
from lib import *
poly="f1"; out=open("m3b_pal.tsv","w"); out.write("poly\tk\tp\tM\tA1(float)\tA2 exact\tA2(float)\n")
for K in (4,5,6,7,8):
    for p in primes_upto(311):
        if not good(poly,p) or p<5: continue
        rng=random.Random(f"pal-{poly}-{K}-{p}")
        half=[rng.randrange(1,p) for _ in range((K)//2)]
        c=[0]*(K-1)
        for i in range(K-1):
            j=min(i,K-2-i); c[i]=half[j]
        assert all(c[i]==c[K-2-i] for i in range(K-1))
        t=tv(poly,p); M=int(t.sum()); N=[int(v) for v in Nall(t,c,K,p)]; assert sum(N)==M**K
        R=p*N[0]-M**K; ss=sum(v*v for v in N); A2=Fraction(p*ss-M**(2*K),(p-1)*p**K)
        out.write(f"{poly}\t{K}\t{p}\t{M}\t{R/((p-1)*p**(K/2)):.6f}\t{A2}\t{float(A2):.6f}\n")
out.close()
import statistics
rows=[ln.split("\t") for ln in open("m3b_pal.tsv").read().splitlines()[1:]]
res=[]
for K in (4,5,6,7,8):
    for lo,hi in ((5,50),(51,150),(151,311)):
        G=[float(r[6]) for r in rows if int(r[1])==K and lo<=int(r[2])<=hi]
        res.append(f"palindromic random c, f1, k={K}, p in [{lo},{hi}]: n={len(G)} mean A2={statistics.mean(G):.3f} min {min(G):.3f} max {max(G):.3f}")
open("m3b_pal_summary.txt","w").write("\n".join(res)+"\n"); print("\n".join(res))
