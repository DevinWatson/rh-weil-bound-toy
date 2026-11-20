import sys, random
import numpy as np
sys.path.insert(0, './compute/B')
from core import *
P = {**POLYS, "x^2+1": [1, 0, 1], "x^4+x^2-1": [-1, 0, 1, 0, 1]}
random.seed(7)
out = []
cnt = 0
bad = 0
for p in primes_upto(199):
    if p == 2:
        continue
    for name, co in P.items():
        t = tvec(co, p)
        t0 = int(t[0]); M = int(t.sum())
        xs = np.arange(p)
        Cc = int((t * t[(-xs) % p]).sum())
        # k=2, c=1: N_2 = 2 t0 M - t0^2
        n2 = [int(z) for z in N_all(t, [1], 2, p)]
        # k=2 any c: N_2(0) same; N_2(s), s!=0 = sum_{x!=0} t(x) t(s/(c x))
        c1 = random.randrange(1, p)
        n2c = N_zero(t, [c1], 2, p)
        # k=3, c=1: N_3 = t0 M^2 + (M - t0) C
        n3 = N_zero(t, [1, 1], 3, p)
        # k=3 general c: x3 = -(c1/c2) x1: N_3 = t0 M^2 + (M - t0) C_lam
        d1, d2 = random.randrange(1, p), random.randrange(1, p)
        lam = d1 * pow(d2, -1, p) % p
        Clam = int((t * t[(-lam * xs) % p]).sum())
        n3c = N_zero(t, [d1, d2], 3, p)
        ok = (n2[0] == 2 * t0 * M - t0 * t0 and n2c == 2 * t0 * M - t0 * t0
              and n3 == t0 * M * M + (M - t0) * Cc and n3c == t0 * M * M + (M - t0) * Clam)
        # N_2(s) s != 0
        for s in range(1, p):
            ex = sum(int(t[x]) * int(t[(s * pow(x, -1, p)) % p]) for x in range(1, p))
            if ex != n2[s]:
                ok = False
        cnt += 1
        if not ok:
            bad += 1
            out.append(f"FAIL p={p} f={name}")
out.append(f"T2: checked {cnt} (p,f) pairs, all odd primes p<=199, {len(P)} polys (x^3-x has f(0)=0; x^2+1 and x^4+x^2-1 included; bad primes not skipped since t is just a function); failures: {bad}")
out.append("N_2(0) = 2 t(0) M - t(0)^2   [c any nonzero];  N_2(s) = sum_{x!=0} t(x) t(s/(c x)) for s != 0")
out.append("N_3 = t(0) M^2 + (M - t(0)) C, C = sum_x t(x)t(-x)   [c=1];  general c: C replaced by C_lam = sum t(x)t(-lam x), lam=c1/c2")
open('./compute/B/t2_output.txt', 'w').write("\n".join(out) + "\n")
print("\n".join(out))
