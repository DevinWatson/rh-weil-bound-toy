"""M1: k=4, all c=(1,c2,c3) in F_p^2, p in 5..23 (+29,31 extension), four polynomials. Exact integers."""
from fractions import Fraction
from lib import *
import itertools, sys

PR = [5, 7, 11, 13, 17, 19, 23, 29, 31]
TAG = ""
if len(sys.argv) > 2:  # usage: m1_k4.py TAG p1,p2,...
    TAG = sys.argv[1]
    PR = [int(s) for s in sys.argv[2].split(",")]
rows = []
skipped = []
t_start = now()
for nm in POLYS:
    for p in PR:
        if not good(nm, p):
            skipped.append((nm, p)); continue
        t = tv(nm, p); M = int(t.sum()); t0 = int(t[0]); r0 = int((t == 0).sum())
        x = np.arange(p)
        C = [int((t * t[(r * x) % p]).sum()) for r in range(p)]
        for c2 in range(p):
            for c3 in range(p):
                N = int(Nzero(t, [1, c2, c3], 4, p))
                s0 = int((1 + c2 + c3) % p == 0)
                bad = int(2 * N >= p * p)
                rows.append((nm, p, c2, c3, N, M, t0, r0, s0, bad))
print("done computing", len(rows), "rows in", round(now() - t_start, 1), "s")
with open(f"m1_all{TAG}.tsv", "w") as fh:
    fh.write("poly\tp\tc2\tc3\tN4\tM\tt0\troots\tsum_zero\tbad(2N>=p^2)\tN/p^2\n")
    for r in rows:
        fh.write("\t".join(map(str, r)) + "\t" + str(Fraction(r[4], r[1] ** 2)) + "\n")
with open(f"m1_bad{TAG}.tsv", "w") as fh:
    fh.write("poly\tp\tc2\tc3\tN4\tN/p^2\tsum_zero\n")
    for r in rows:
        if r[9]:
            fh.write(f"{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}\t{r[4]}\t{Fraction(r[4], r[1]**2)}\t{r[8]}\n")
with open(f"m1_skipped{TAG}.txt", "w") as fh:
    for s in skipped:
        fh.write(f"{s[0]} p={s[1]} excluded (p | disc or f(0)=0 mod p); disc={DISC[s[0]]}\n")
print("skipped", skipped)
