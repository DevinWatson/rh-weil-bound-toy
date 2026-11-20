"""T5. k=4, c=1: strata of N_4 = sum_{x1..x4: x1x2+x2x3+x3x4=0} t(x1)..t(x4).
 S_A = {x3=0,x2=0}, S_B = {x3=0,x2!=0}, S_C = {x3!=0}.  Each by direct enumeration of the stratum (O(p^3), independent of the closed forms),
 then compared with closed forms derived by hand (see report):
  A = t0^2 M^2 ; B = t0^2 M (M-t0);
  C = C1 + C2 + E with C1 = t0^2 M (M-t0) (x2=0), C2 = t0 (M-t0)(Csum-t0^2) (x2!=0,x1=-x3), E = sum_{a!=0} G(a)G(1-a), G(a)=sum_{x!=0} t(x)t(-a x).
"""
import sys
import numpy as np
sys.path.insert(0, './compute/B')
from core import *
B = './compute/B/'
P = {**POLYS, "x^3+x+3": [3, 1, 0, 1], "x^2+x+3": [3, 1, 1]}
fo = open(B + 't5_strata.tsv', 'w')
fo.write("f\tp\tM\tt0\tCsum\tA\tB\tCstrat\tC1\tC2\tE\tN4\tclosed_forms_ok\tN4_eq_DP\n")
bad = 0; n = 0
for p in primes_upto(199):
    if p < 3: continue
    xs = np.arange(p, dtype=np.int64)
    for name, co in P.items():
        if name in DISC and not good_prime(name, p): continue
        t = tvec(co, p)
        M = int(t.sum()); t0 = int(t[0])
        Cs = int((t * t[(-xs) % p]).sum())
        # direct stratum sums: x3 fixed, x2 fixed, x1 free, x4 determined when x3 != 0; do by enumeration over (x1,x2,x3,x4) vectorised in x4
        A = B_ = Cst = 0
        # x3 = 0: Q = x1*x2 (x4 free, weight t(x4) summed -> M, t(x3)=t0)
        for x2 in range(p):
            s = t0 * int(t[x2]) * M * int(t[(xs * x2) % p == 0].sum())
            if x2 == 0: A += s
            else: B_ += s
        # x3 != 0: x4 = -x2 (x1+x3)/x3
        W = np.outer(t, t)  # [x1,x2]
        for x3 in range(1, p):
            inv3 = pow(x3, -1, p)
            x4 = (-(xs[None, :] * (xs[:, None] + x3)) * inv3) % p   # [x1,x2]
            Cst += int(t[x3]) * int((W * t[x4]).sum())
        # closed forms
        G = np.array([int((t[1:] * t[(-a * xs[1:]) % p]).sum()) for a in range(p)], dtype=np.int64)
        E = sum(int(G[a]) * int(G[(1 - a) % p]) for a in range(1, p))
        C1 = t0 * t0 * M * (M - t0); C2 = t0 * (M - t0) * (Cs - t0 * t0)
        ok = (A == t0 * t0 * M * M and B_ == t0 * t0 * M * (M - t0) and Cst == C1 + C2 + E)
        N4 = A + B_ + Cst
        dp = N_zero(t, [1, 1, 1], 4, p)
        n += 1; bad += (not ok) or (N4 != dp)
        fo.write(f"{name}\t{p}\t{M}\t{t0}\t{Cs}\t{A}\t{B_}\t{Cst}\t{C1}\t{C2}\t{E}\t{N4}\t{ok}\t{N4 == dp}\n")
    fo.flush()
fo.close()
msg = f"T5: {n} (f,p) cases, p<=199 (7 polys); stratum sums by direct enumeration; closed forms and N4=DP failures: {bad}"
open(B + 't5_check.txt', 'w').write(msg + "\n")
print(msg)

