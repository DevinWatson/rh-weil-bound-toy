import numpy as np
from fractions import Fraction as F
B = './compute/B/'
rows = []
for ln in open(B + 't5_strata.tsv').read().splitlines()[1:]:
    z = ln.split('\t'); rows.append((z[0], *map(int, z[1:12])))
# f p M t0 Cs A B Cst C1 C2 E N4
out = []
fs = sorted(set(r[0] for r in rows))
for f in fs:
    rr = [r for r in rows if r[0] == f]
    n = len(rr)
    pos = lambda i: sum(1 for r in rr if r[i] > 0)
    neg = lambda i: sum(1 for r in rr if r[i] < 0)
    nzt0 = sum(1 for r in rr if r[3] != 0)
    out.append(f"{f:10s} {n} primes<=199, t0!=0 in {nzt0}.  sign counts (+/-/0): " + "; ".join(
        f"{lab} {pos(i)}/{neg(i)}/{n-pos(i)-neg(i)}" for lab, i in [("A", 5), ("B", 6), ("C1", 8), ("C2", 9), ("E", 10), ("N4", 11)]))
    # A+B+C1 = t0^2 (3M^2 - 2 t0 M) ; sign counts
    s3 = [r[5] + r[6] + r[8] for r in rr]
    out.append(f"     A+B+C1 = t0^2(3M^2-2 t0 M): +/-/0 = {sum(1 for x in s3 if x>0)}/{sum(1 for x in s3 if x<0)}/{sum(1 for x in s3 if x==0)}; "
               f"mean E/p^1.5 = {np.mean([r[10]/r[1]**1.5 for r in rr]):+.3f} sd {np.std([r[10]/r[1]**1.5 for r in rr]):.3f}; "
               f"mean E/p = {np.mean([r[10]/r[1] for r in rr]):+.3f}; mean N4/p^1.5 = {np.mean([r[11]/r[1]**1.5 for r in rr]):+.3f}")
    big = [r for r in rr if r[1] > 100]
    out.append(f"     p>100 ({len(big)} primes): mean (A+B+C1+C2)/p^1.5 = {np.mean([(r[5]+r[6]+r[8]+r[9])/r[1]**1.5 for r in big]):+.3f}, mean E/p^1.5 = {np.mean([r[10]/r[1]**1.5 for r in big]):+.3f}, max |E|/p^1.5 = {max(abs(r[10])/r[1]**1.5 for r in big):.3f}")
# exact identity check: sum over rows? test candidate: E vs -p*something? regression (HINT only) of E on monomials
out.append("")
out.append("Least-squares HINT (float64) of E on [p, M^2, t0*M, t0*p, 1] pooled over f with t0 != 0 (E = stratum with all x2,x3,u nonzero):")
rr = [r for r in rows if r[3] != 0]
X = np.array([[r[1], r[2] ** 2, r[3] * r[2], r[3] * r[1], 1.0] for r in rr], dtype=float)
y = np.array([r[10] for r in rr], dtype=float)
co, res, rk, sv = np.linalg.lstsq(X, y, rcond=None)
out.append("  coefficients [p, M^2, t0 M, t0 p, 1] = " + ", ".join(f"{c:+.3f}" for c in co) + f"; residual rms {np.sqrt(np.mean((X@co-y)**2)):.1f} vs rms E {np.sqrt(np.mean(y**2)):.1f}")
out.append("Same for the pooled full N4 on [M^2, t0 M, p, t0 p, 1]:")
X = np.array([[r[2] ** 2, r[3] * r[2], r[1], r[3] * r[1], 1.0] for r in rr], dtype=float)
y = np.array([r[11] for r in rr], dtype=float)
co, *_ = np.linalg.lstsq(X, y, rcond=None)
out.append("  coefficients = " + ", ".join(f"{c:+.3f}" for c in co) + f"; residual rms {np.sqrt(np.mean((X@co-y)**2)):.1f} vs rms N4 {np.sqrt(np.mean(y**2)):.1f}")
open(B + 't5_analysis.txt', 'w').write("\n".join(out) + "\n")
print("\n".join(out))
