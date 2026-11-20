"""T4. For each (f,p,k): N_k(s) for all s (exact DP).  Exact: sum_s N(s) = M^k  (h=0 term), Z = p*sum N(s)^2.
|S_h|^2 enclosed with mpmath interval arithmetic (iv, 100 bits): S_h = sum_s N(s) exp(2 pi i h s/p).
Certified: (a) Z lies in the enclosure of M^(2k) + sum_{h!=0}|S_h|^2 ; (b) upper bound of max_{h!=0}|S_h|^2 versus
B = p^(k-1) m^2, m = sum_x t(x)^2 (=p - #roots of f), ratio taken from the interval UPPER endpoint."""
import sys, time
from fractions import Fraction as F
import mpmath
sys.path.insert(0, './compute/B')
from core import *
iv = mpmath.iv
iv.prec = 100
B = './compute/B/'
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 101


def fr(x):  # mpf -> exact Fraction
    s, man, ex, bc = x
    v = F(int(man)) * (F(2) ** int(ex))
    return -v if s else v


T0 = time.time()
fo = open(B + 't4_parseval.tsv', 'w')
fo.write("f\tp\tk\tm\tsumN_eq_Mk\tparseval_in_enclosure\tmax_h_S2_upper\tmax_h_S2_lower\targmax_h\tratio_upper_to_p^(k-1)m^2\tratio_upper_to_p^k\tbound_holds\n")
nrows = 0; allok = True; worst = {}
for p in primes_upto(PMAX):
    if p < 3: continue
    cs = [iv.cos(2 * iv.pi * j / p) for j in range(p)]
    sn = [iv.sin(2 * iv.pi * j / p) for j in range(p)]
    for name, co in POLYS.items():
        if not good_prime(name, p): continue
        t = tvec(co, p)
        m = int((t * t).sum()); M = int(t.sum())
        if m == 0: continue  # t identically 0 (x^3-x at p=3)
        for k in (4, 5, 6):
            Nv = [int(z) for z in N_all(t, [1] * (k - 1), k, p)]
            ok1 = (sum(Nv) == M ** k)
            Z = p * sum(z * z for z in Nv)
            vals = []
            tot = iv.mpf(0)
            for h in range(1, p):
                re = iv.mpf(0); im = iv.mpf(0)
                for s in range(p):
                    if Nv[s]:
                        j = (h * s) % p
                        re += Nv[s] * cs[j]; im += Nv[s] * sn[j]
                v = re ** 2 + im ** 2
                vals.append(v); tot += v
            tot = tot + M ** (2 * k)
            in_enc = (fr(tot._mpi_[0]) <= Z <= fr(tot._mpi_[1]))
            ub = max(fr(v._mpi_[1]) for v in vals); lb = max(fr(v._mpi_[0]) for v in vals)
            hmax = 1 + max(range(len(vals)), key=lambda i: fr(vals[i]._mpi_[1]))
            bound = F(p ** (k - 1) * m * m)
            holds = ub <= bound
            if not holds and ub <= bound * (1 + F(1, 10 ** 20)): holds = 'TIGHT(ub exceeds bound by <1e-20 rel: equality case, interval cannot separate)'
            r1 = ub / bound; r2 = ub / F(p ** k)
            allok &= ok1 and in_enc and bool(holds)
            fo.write(f"{name}\t{p}\t{k}\t{m}\t{ok1}\t{in_enc}\t{float(ub):.6e}\t{float(lb):.6e}\t{hmax}\t{float(r1):.5f}\t{float(r2):.5f}\t{holds}\n")
            nrows += 1
            key = (name, k)
            if key not in worst or r2 > worst[key][0]:
                worst[key] = (r2, p)
    fo.flush()
fo.close()
msg = [f"T4: {nrows} (f,p,k) cases, p<=101; sumN=M^k and Parseval-in-enclosure and bound |S_h|^2 <= p^(k-1) m^2 all true: {allok}; elapsed {time.time()-T0:.0f}s"]
for (name, k), (r2, p) in sorted(worst.items()):
    msg.append(f"  {name:10s} k={k}: max over p<=101,h!=0 of |S_h|^2/p^k <= {float(r2):.4f} (upper endpoint, at p={p})")
open(B + 't4_summary.txt', 'w').write("\n".join(msg) + "\n")
print("\n".join(msg))



