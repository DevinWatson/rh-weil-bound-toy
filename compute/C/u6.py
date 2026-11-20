import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction
from ff import *

HERE = os.path.dirname(os.path.abspath(__file__))
CUBICS = {"x^3+x+1": ([1, 1, 0, 1], 31), "x^3-x": ([0, -1, 0, 1], 2)}   # (coeffs, bad prime from discriminant: -31, 4)
PRIMES = [p for p in range(3, 98) if all(p % d for d in range(2, int(p ** 0.5) + 1))]
mode = sys.argv[1] if len(sys.argv) > 1 else "cross"
if mode == "cross":
    path = os.path.join(HERE, "crosscheck.tsv")
    plist = PRIMES
else:  # extra scan, larger primes, display of growth
    path = os.path.join(HERE, "scan_N4_to_%s.tsv" % sys.argv[2])
    top = int(sys.argv[2])
    plist = [p for p in range(3, top + 1) if all(p % d for d in range(2, int(p ** 0.5) + 1))]
    plist = [p for p in plist if p > 97]
fh = open(path, "w")
fh.write("f\tp\tM\tN_4\n")
for name, (co, bad) in CUBICS.items():
    for p in plist:
        if p == bad:
            continue
        F = Field(p, 1)
        t = F.t_of([c % p for c in co])
        M = int(t.sum())
        N4 = N_fast(F, t, [1, 1, 1], 4)
        fh.write("%s\t%d\t%d\t%d\n" % (name, p, M, N4))
        fh.flush()
fh.close()
print("wrote", path)
