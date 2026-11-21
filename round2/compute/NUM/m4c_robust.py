import statistics
rows=[ln.split("\t") for ln in open("m4a_random.tsv").read().splitlines()[1:]]
out=["Robust statistics of Z = E/p^((k-1)/2), E = N_k(0) - M^k/p, random c, primes 61..311, polys f1,f2,f4 (hint floats from exact values)",
"k | n | median|Z| | q90 |Z| | q99 |Z| | RMS Z without the top 1% of |Z| | RMS Z for p>=150 (n)"]
for k in (3,4,5,6,7,8):
    Z=[(float(r[4]),int(r[2])) for r in rows if int(r[0])==k]
    A=sorted(abs(z) for z,_ in Z); n=len(A)
    trim=A[:int(0.99*n)]
    big=[z for z,p in Z if p>=150]
    out.append(f"{k} | {n} | {A[n//2]:.3f} | {A[int(0.9*n)]:.3f} | {A[int(0.99*n)]:.3f} | {statistics.mean([a*a for a in trim])**0.5:.3f} | {statistics.mean([z*z for z in big])**0.5:.3f} ({len(big)})")
# the main term relative to the Z scale
out.append("")
out.append("Main term M^k/p relative to p^((k-1)/2): sqrt-mean of (M^k/p^((k+1)/2))^2 over the same (poly,p) pairs (M exact)")
import sys
sys.path.insert(0,'.')
from lib import *
import math
for k in (3,4,5,6,7,8):
    v=[]
    for poly in ("f1","f2","f4"):
        for p in primes_upto(311):
            if p<61 or not good(poly,p): continue
            M=int(tv(poly,p).sum()); v.append((M**k/p**((k+1)/2))**2)
    out.append(f"k={k}: RMS of M^k/p^((k+1)/2) = {statistics.mean(v)**0.5:.3f}")
open("m4c_robust.txt","w").write("\n".join(out)+"\n"); print("\n".join(out))
