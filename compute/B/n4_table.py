import sys, time
sys.path.insert(0, './compute/B')
from core import *
B = './compute/B/'
t0 = time.time()
with open(B + 'n4_table.tsv', 'w') as fo:
    fo.write("f\tp\tM\tN_4\n")
    for name, co in POLYS.items():
        for p in primes_upto(199):
            if not good_prime(name, p):
                continue
            t = tvec(co, p)
            fo.write(f"{name}\t{p}\t{int(t.sum())}\t{N_zero(t, [1,1,1], 4, p)}\n")
        fo.flush()
print("done", time.time() - t0)
