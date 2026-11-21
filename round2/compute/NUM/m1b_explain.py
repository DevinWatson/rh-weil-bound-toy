"""Explain the k=4 bad set exactly.  N = M^4/p + E (E = R/p exact rational, R = sum_{h != 0} S(h)).
With c1=1, tau(1) = -(c2+c3), r* = -(1+c2)/c3 (tau(r*) = 1).  term1 = C(1) C(tau(1)), term2 = C(r*) C(1) (r* != 1 off the plane).
These are the two 'plane-like' summands of N = -p + t0^2 M^2 + sum_r C(r) C(tau r) (validated identity, v1_out.txt).
Classes for a bad c (2N >= p^2):
  P  : c1+c2+c3 = 0 and c3 != 0           (plane x1=x3, x2=x4)
  Z  : c3 = 0                              (degenerate: x4 decouples)
  MT : not P/Z, and E = N - M^4/p < p^2/2  (main term M^4/p explains the hit)
  T  : not P/Z/MT, and E - term1 - term2 - (-p + 0) < p^2/2 ... (one of the two plane-like terms explains)
  U  : none of the above (unexplained)"""
from fractions import Fraction
from lib import *
import collections

rows = [ln.split("\t") for ln in open("m1_all.tsv").read().splitlines()[1:]]
cache = {}
cnt = collections.Counter()
out_rows = []
unexpl = []
for a in rows:
    nm, p, c2, c3, N, M, t0, r0, s0, bad = a[0], *map(int, a[1:10])
    if (nm, p) not in cache:
        t = tv(nm, p); x = np.arange(p)
        cache[(nm, p)] = [int((t * t[(r * x) % p]).sum()) for r in range(p)]
    C = cache[(nm, p)]
    if not bad:
        continue
    if c3 == 0:
        cls = "Z"
        t1 = t2 = None
    else:
        tau1 = (-(c2 + c3)) % p
        rstar = (-(1 + c2) * pow(c3, -1, p)) % p
        t1 = C[1] * C[tau1]
        t2 = C[rstar] * C[1] if rstar != 1 else 0
        E = Fraction(N) - Fraction(M ** 4, p)
        if s0:
            cls = "P"
        elif 2 * E < p * p:
            cls = "MT"
        else:
            # remove the two plane-like terms (they are p*C(.)-sized)
            E2 = E - t1 - t2
            cls = "T" if 2 * E2 < p * p else "U"
    cnt[(nm, p, cls)] += 1
    cnt[("all", "all", cls)] += 1
    out_rows.append((nm, p, c2, c3, N, M, cls, t1, t2))
    if cls == "U":
        unexpl.append(out_rows[-1])
with open("m1_classes.tsv", "w") as fh:
    fh.write("poly\tp\tc2\tc3\tN4\tM\tclass\tterm1=C(1)C(tau1)\tterm2=C(r*)C(1)\n")
    for r in out_rows:
        fh.write("\t".join(map(str, r)) + "\n")
lines = []
keys = sorted(set((k[0], k[1]) for k in cnt if k[0] != "all"))
lines.append("poly p : #bad by class P / Z / MT / T / U")
for (nm, p) in keys:
    lines.append(f"{nm} p={p:2d}: " + " / ".join(str(cnt[(nm, p, c)]) for c in ("P", "Z", "MT", "T", "U")))
lines.append("ALL: " + " / ".join(f"{c}={cnt[('all','all',c)]}" for c in ("P", "Z", "MT", "T", "U")))
lines.append("unexplained (class U):")
for r in unexpl:
    lines.append("  " + str(r))
open("m1_classes_summary.txt", "w").write("\n".join(lines) + "\n")
print("\n".join(lines[:60]))
