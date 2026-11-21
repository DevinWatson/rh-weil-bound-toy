"""Combine base (p<=31) and extension (37..73) k=4 tables; classify bad c; plane statistics."""
from fractions import Fraction
from lib import *
import collections, glob

files = ["m1_all.tsv", "m1_all_extA.tsv", "m1_all_extB.tsv"]
rows = []
for f in files:
    for ln in open(f).read().splitlines()[1:]:
        a = ln.split("\t")
        rows.append((a[0], *map(int, a[1:10])))
keys = sorted(set((r[0], r[1]) for r in rows), key=lambda k: (k[0], k[1]))
cache = {}
lines = []
lines.append("Per (poly,p): bad = #c with 2N>=p^2.  Classes: P plane (1+c2+c3=0,c3!=0), Z (c3=0), MT main term M^4/p explains, T plane-like terms C(1)C(tau1), C(r*)C(1) explain, U unexplained.")
lines.append("plane stats over c on the plane with c3!=0: min and max of N/p^2 (exact), (p-r0)^2/p^2, and max |N-(p-r0)^2| / p^(3/2) as float hint")
lines.append("poly p | bad | P Z MT T U | #P total | P not bad | plane N/p^2 min..max | (p-r0)^2/p^2 | max|N-(p-r0)^2|/p^1.5 | max N/p^2 off-plane")
agg = collections.Counter()
Urows = []
for (nm, p) in keys:
    R = [r for r in rows if r[0] == nm and r[1] == p]
    if (nm, p) not in cache:
        t = tv(nm, p); x = np.arange(p)
        cache[(nm, p)] = [int((t * t[(r * x) % p]).sum()) for r in range(p)]
    C = cache[(nm, p)]
    cnt = collections.Counter()
    plane = [r for r in R if r[8] and r[3] != 0]
    for r in R:
        _, _, c2, c3, N, M, t0, r0, s0, bad = r
        if not bad:
            continue
        if c3 == 0:
            cls = "Z"
        elif s0:
            cls = "P"
        else:
            E = Fraction(N) - Fraction(M ** 4, p)
            tau1 = (-(c2 + c3)) % p
            rstar = (-(1 + c2) * pow(c3, -1, p)) % p
            t1 = C[1] * C[tau1]; t2 = C[rstar] * C[1] if rstar != 1 else 0
            if 2 * E < p * p:
                cls = "MT"
            elif 2 * (E - t1 - t2) < p * p:
                cls = "T"
            else:
                cls = "U"; Urows.append(r)
        cnt[cls] += 1; agg[cls] += 1
    nbad = sum(cnt.values())
    pn = [Fraction(r[4], p * p) for r in plane]
    r0 = R[0][7]
    dev = max(abs(r[4] - (p - r0) ** 2) for r in plane) / p ** 1.5
    pnb = sum(1 for r in plane if not r[9])
    off = [Fraction(r[4], p * p) for r in R if not r[8]]
    lines.append(f"{nm} p={p:2d} | {nbad:4d} | {cnt['P']:3d} {cnt['Z']:3d} {cnt['MT']:3d} {cnt['T']:3d} {cnt['U']:3d} | {len(plane):3d} | {pnb:2d} | {float(min(pn)):.3f}..{float(max(pn)):.3f} | {(p-r0)**2/p**2:.3f} | {dev:.2f} | {float(max(off)):.3f}")
lines.append("TOTALS by class: " + str(dict(agg)))
lines.append(f"unexplained rows: {len(Urows)}")
open("m1c_all_primes.txt", "w").write("\n".join(lines) + "\n")
with open("m1c_unexplained.tsv", "w") as fh:
    fh.write("poly\tp\tc2\tc3\tN4\tM\n")
    for r in Urows:
        fh.write(f"{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}\t{r[4]}\t{r[5]}\n")
print("\n".join(lines))
