"""T6: k=4, three random nonzero coefficient vectors (c1,c2,c3) per (f,p), seed 20261120. usage: python t6_randc.py budget_s"""
import sys, time, random
sys.path.insert(0, './compute/B')
from core import *
B = './compute/B/'
budget = float(sys.argv[1]); SEED = 20261120
rng = random.Random(SEED)
T0 = time.time(); last = 0.0; done_to = 0
with open(B + 't6_k4_randc.tsv', 'w') as fo:
    fo.write("f\tp\tc1\tc2\tc3\tM\tN_4\n")
    for p in primes_upto(1400):
        if p < 3: continue
        if (time.time() - T0) + 1.6 * last > budget: break
        s = time.time()
        for name, co in POLYS.items():
            if not good_prime(name, p): continue
            t = tvec(co, p)
            for _ in range(3):
                c = [rng.randrange(1, p) for _ in range(3)]
                fo.write(f"{name}\t{p}\t{c[0]}\t{c[1]}\t{c[2]}\t{int(t.sum())}\t{N_zero(t, c, 4, p)}\n")
        fo.flush(); last = time.time() - s; done_to = p
open(B + 't6_progress.txt', 'w').write(f"seed={SEED} P={done_to} elapsed={time.time()-T0:.1f}s budget={budget}\n")
print(f"T6 seed {SEED}: all good primes 3..{done_to} done, {time.time()-T0:.1f}s")
