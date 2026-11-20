"""usage: python t3_run.py k budget_seconds   -> t3_k{k}.tsv (f, p, M, N_k), all five f per prime, primes ascending."""
import sys, time
sys.path.insert(0, './compute/B')
from core import *
B = './compute/B/'
k = int(sys.argv[1]); budget = float(sys.argv[2])
T0 = time.time()
last = 0.0
done_to = 0
with open(B + f't3_k{k}.tsv', 'w') as fo:
    fo.write("f\tp\tM\tN_k\n")
    for p in primes_upto(1400):
        if p < 3:
            continue
        if (time.time() - T0) + 1.6 * last > budget:
            break
        s = time.time()
        for name, co in POLYS.items():
            if not good_prime(name, p):
                continue
            t = tvec(co, p)
            fo.write(f"{name}\t{p}\t{int(t.sum())}\t{N_zero(t, [1]*(k-1), k, p)}\n")
        fo.flush()
        last = time.time() - s
        done_to = p
print(f"k={k} budget={budget}s: all good primes 3..{done_to} done, elapsed {time.time()-T0:.1f}s")
open(B + f't3_k{k}_progress.txt', 'w').write(f"k={k} P_k={done_to} elapsed={time.time()-T0:.1f}s budget={budget}\n")
