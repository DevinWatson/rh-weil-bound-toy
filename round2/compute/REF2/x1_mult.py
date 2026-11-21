# REF2: for f = x^d - a, mu = mu_d, test Theorem B quantitatively: N_4/p^2 should be near m(c) = #{(rho,rho') in mu^2 : c2 + c3 rho + c1 rho' = 0}.
import sys
from collections import defaultdict
from lib import *

p = int(sys.argv[1]); d = int(sys.argv[2]); a = int(sys.argv[3])
mud = sorted(x for x in range(1, p) if pow(x, d, p) == 1)
assert len(mud) == d
t = t_from_poly(p, [1] + [0] * (d - 1) + [(-a) % p])
C = Carray(p, t)
N = N4_table_c1_is_1(p, t, C)
mult = np.zeros((p, p), dtype=np.int64)
for r1 in mud:
    for r2 in mud:
        for c3 in range(1, p):
            c2 = (-(c3 * r1) - r2) % p
            if c2:
                mult[c2, c3] += 1
P2 = float(p) * p
groups = defaultdict(list)
for c2 in range(1, p):
    for c3 in range(1, p):
        groups[int(mult[c2, c3])].append(N[c2, c3] / P2)
out = open("x1_mult_out.txt", "a")
print("== x^%d-%d p=%d: multiplicity m(c) vs N_4/p^2 over c=(1,c2,c3)" % (d, a, p), file=out)
for m in sorted(groups):
    v = np.array(groups[m])
    print("  m=%d  n=%d  mean=%.3f  std=%.3f  min=%.3f  max=%.3f" % (m, len(v), v.mean(), v.std(), v.min(), v.max()), file=out)
out.close()
