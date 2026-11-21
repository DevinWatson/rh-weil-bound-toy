"""M3: first and second moments over h.  usage: m3_moments.py POLY K PMAX BUDGET_S
A_1 = (p N_k(0) - M^k) / ((p-1) p^(k/2)) ,  A_2 = (p * sum_s N_k(s)^2 - M^(2k)) / ((p-1) p^k) .
c types: ones; rand1, rand2 = entries uniform in F_p^* from random.Random(f"{poly}-{k}-{p}-{j}").
Exact Fractions; floats are hints.  Note sum_s N(s) = M^k and sum_s N(s)^2 = (1/p) sum_h |S(h)|^2 (Plancherel), so
A_2 = mean over h != 0 of |S(h)|^2 / p^k and (p-1) A_2 p^k = sum_{h != 0}|S(h)|^2."""
import sys, random
from fractions import Fraction
from lib import *

poly, K, PMAX, BUDGET = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4])
t_start = now()
fn = f"m3_{poly}_k{K}.tsv"
fh = open(fn, "w")
fh.write("poly\tk\tctype\tp\tM\tN0\tsumNsq\tR/(p-1)=mean_h S(h)\tA1(float hint)\tA1 exact (even k only)\tA2 exact\tA2(float hint)\tnearest int\tA2-nearest int (float hint)\tp-1 divides p*sumNsq-M^2k\n")
last_p = None
for p in primes_upto(PMAX):
    if not good(poly, p):
        continue
    if now() - t_start > BUDGET:
        break
    try:
        check_bound(p, K)
    except AssertionError:
        print("bound stops at p =", p); break
    t = tv(poly, p); M = int(t.sum())
    for ct in ("ones", "rand1", "rand2"):
        if ct == "ones":
            c = [1] * (K - 1)
        else:
            rng = random.Random(f"{poly}-{K}-{p}-{ct}")
            c = [rng.randrange(1, p) for _ in range(K - 1)]
        N = [int(v) for v in Nall(t, c, K, p)]
        assert sum(N) == M ** K
        N0 = N[0]
        ss = sum(v * v for v in N)
        R = p * N0 - M ** K
        num2 = p * ss - M ** (2 * K)
        A2 = Fraction(num2, (p - 1) * p ** K)
        A1f = R / ((p - 1) * p ** (K / 2))  # float of exact ints (hint)
        A1e = str(Fraction(R, (p - 1) * p ** (K // 2))) if K % 2 == 0 else ""
        ni = round(float(A2))
        fh.write(f"{poly}\t{K}\t{ct}\t{p}\t{M}\t{N0}\t{ss}\t{Fraction(R, p-1)}\t{A1f:.6f}\t{A1e}\t{A2}\t{float(A2):.6f}\t{ni}\t{float(A2 - ni):.6f}\t{int(num2 % (p-1) == 0)}\n")
    fh.flush()
    last_p = p
fh.close()
print(f"{poly} k={K}: finished primes up to {last_p}, elapsed {now()-t_start:.0f}s", flush=True)
with open("m3_progress.txt", "a") as pf:
    pf.write(f"{poly} k={K}: last prime {last_p} (PMAX {PMAX}, budget {BUDGET}s) elapsed {now()-t_start:.0f}s\n")
