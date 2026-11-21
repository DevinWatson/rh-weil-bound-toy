"""M4: odd k vs even k.
(a) size statistics of N_k(0) and E_k = N_k(0) - M^k/p over random c, primes 61..311, polys f1,f2,f4, k = 3..8
(b) exhaustive k=5, c=(1,c2,c3,c4), p = 11, 13 (all four polys when good), with the subspace test (Z zero coordinates + matching)
(c) radical of the path form for odd k (exact check over Q with sympy, k=3,5,7,9)."""
import random, statistics, itertools, sys
from fractions import Fraction
from lib import *

out = []
# (c) radical
import sympy
for k in (3, 4, 5, 6, 7, 9):
    cs = sympy.symbols("c1:%d" % k)
    A = sympy.zeros(k, k)
    for i in range(k - 1):
        A[i, i + 1] = cs[i]; A[i + 1, i] = cs[i]
    d = sympy.factor(A.det())
    ns = A.nullspace() if k % 2 == 1 else []
    out.append(f"k={k}: det of the Gram matrix (twice the form) of the path form = {d}; nullspace dimension {len(ns)}" + (f"; radical vector {list(ns[0].T)}" if ns else ""))

# (a)
rng_seed = "m4a"
rows = {}
for poly in ("f1", "f2", "f4"):
    for p in primes_upto(311):
        if p < 61 or not good(poly, p):
            continue
        t = tv(poly, p); M = int(t.sum())
        for k in (3, 4, 5, 6, 7, 8):
            for j in range(10):
                rng = random.Random(f"{rng_seed}-{poly}-{k}-{p}-{j}")
                c = [rng.randrange(1, p) for _ in range(k - 1)]
                N0 = int(Nzero(t, c, k, p))
                E = Fraction(N0) - Fraction(M ** k, p)
                rows.setdefault(k, []).append((poly, p, N0, float(E) / p ** ((k - 1) / 2), N0 / p ** ((k - 1) / 2)))
out.append("")
out.append("(a) random c (entries uniform in F_p^*), 10 per (poly,p), primes 61..311, f1,f2,f4. Statistics of Z = E/p^((k-1)/2), E = N_k(0) - M^k/p (exact, converted to float for the ratio):")
out.append("k | n | mean Z | RMS Z | max|Z| | fraction Z>0 | RMS of N/p^((k-1)/2) | max |N|/p^((k-1)/2)")
with open("m4a_random.tsv", "w") as fh:
    fh.write("k\tpoly\tp\tN0\tE/p^((k-1)/2) (hint)\tN0/p^((k-1)/2) (hint)\n")
    for k in sorted(rows):
        for r in rows[k]:
            fh.write(f"{k}\t{r[0]}\t{r[1]}\t{r[2]}\t{r[3]:.5f}\t{r[4]:.5f}\n")
for k in sorted(rows):
    Z = [r[3] for r in rows[k]]; Nn = [r[4] for r in rows[k]]
    out.append(f"{k} | {len(Z)} | {statistics.mean(Z):+.3f} | {statistics.mean([z*z for z in Z])**0.5:.3f} | {max(abs(z) for z in Z):.2f} | {sum(z>0 for z in Z)/len(Z):.3f} | {statistics.mean([z*z for z in Nn])**0.5:.3f} | {max(abs(z) for z in Nn):.2f}")

# (b) exhaustive k=5
K = 5
def subspace_conditions(Z, m):
    """Z: tuple of coordinates forced to 0 ; m: matching of the other coordinates as list of pairs. returns list of sets of edge indices (sum of c_i = 0)"""
    pid = {}
    for a, (u, v) in enumerate(m):
        pid[u] = a; pid[v] = a
    cond = {}
    for i in range(1, K):
        if i in Z or (i + 1) in Z:
            continue
        a, b = pid[i], pid[i + 1]
        cond.setdefault((min(a, b), max(a, b)), []).append(i)
    return list(cond.values())
def matchings_of(lst):
    if not lst:
        yield []; return
    a = lst[0]
    for j in range(1, len(lst)):
        for m in matchings_of(lst[1:j] + lst[j + 1:]):
            yield [(a, lst[j])] + m
SUBS = []
for z in range(1, K + 1):
    rest = [i for i in range(1, K + 1) if i != z]
    for m in matchings_of(rest):
        SUBS.append(((z,), m, subspace_conditions((z,), m)))
def holds(cond, c, p):
    return all(sum(c[i - 1] for i in idx) % p == 0 for idx in cond)
out.append("")
out.append(f"(b) k=5 exhaustive over c=(1,c2,c3,c4): {len(SUBS)} subspaces (one coordinate zero + perfect matching of the other four, dim 2, weight t0 (p-r0)^2)")
out.append("poly p | #c | #(2N>=p^2) | #(2E>=p^2) | #c on some subspace | excess-bad on subspace | excess-bad off subspace")
with open("m4b_k5_exhaustive.tsv", "w") as fh:
    fh.write("poly\tp\tc2\tc3\tc4\tN5\tM\tN/p^2\t2N>=p^2\t2E>=p^2\ton_subspace\n")
    for poly in ("f1", "f2", "f3", "f4"):
        for p in (11, 13, 17):
            if not good(poly, p):
                continue
            t = tv(poly, p); M = int(t.sum()); r0 = int((t == 0).sum())
            nb = nbE = nS = nbES = nbEo = n = 0
            for c2, c3, c4 in itertools.product(range(p), repeat=3):
                c = [1, c2, c3, c4]
                N = int(Nzero(t, c, K, p)); E = Fraction(N) - Fraction(M ** K, p)
                on = any(holds(s[2], c, p) for s in SUBS)
                b = int(2 * N >= p * p); bE = int(2 * E >= p * p)
                fh.write(f"{poly}\t{p}\t{c2}\t{c3}\t{c4}\t{N}\t{M}\t{Fraction(N,p*p)}\t{b}\t{bE}\t{int(on)}\n")
                n += 1; nb += b; nbE += bE; nS += on; nbES += (bE and on); nbEo += (bE and not on)
            out.append(f"{poly} p={p} | {n} | {nb} | {nbE} | {nS} | {nbES} | {nbEo}")
open("m4_odd_summary.txt", "w").write("\n".join(out) + "\n")
print("\n".join(out))
