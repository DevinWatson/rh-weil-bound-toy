import sys, random, itertools
import numpy as np
sys.path.insert(0, './compute/B')
from core import *

polys = {"x^3+x+1": [1, 1, 0, 1], "x^3-x": [0, -1, 0, 1], "x^2+3": [3, 0, 1], "x^5+x+1": POLYS["x^5+x+1"]}
random.seed(20261120)
out = []
ok = True
n = 0
for p in [3, 5, 7, 11]:
    for name, co in polys.items():
        t = tvec(co, p)
        for k in [1, 2, 3, 4]:
            cs = [[1] * (k - 1)] + [[random.randrange(1, p) for _ in range(k - 1)] for _ in range(2)]
            for c in cs:
                b = brute(t, c, k, p)
                a = [int(z) for z in N_all(t, c, k, p)]
                z = N_zero(t, c, k, p)
                good = (a == b) and (z == b[0])
                n += 1
                if not good:
                    ok = False
                    out.append(f"MISMATCH p={p} f={name} k={k} c={c} dp={a} brute={b}")
out.append(f"T1: {n} cases (p in 3,5,7,11; 4 polys; k=1..4; c all-1 and two random c) ; all equal = {ok}")
# skew-sum DP vs a naive gather DP for larger p
def naive_all(t, c, k, p):
    old = np.zeros((p, p), dtype=object)
    for v in range(p): old[v][0] = int(t[v])
    for st in range(k - 1):
        new = np.zeros((p, p), dtype=object)
        for v in range(p):
            for w in range(p):
                for r in range(p):
                    new[w][(r + int(c[st]) * v * w) % p] += old[v][r] * int(t[w])
        old = new
    return [int(x) for x in old.sum(axis=0)]
m = 0
for p in [13, 17, 23]:
    for name, co in polys.items():
        t = tvec(co, p)
        for k in [3, 5]:
            c = [random.randrange(1, p) for _ in range(k - 1)]
            assert naive_all(t, c, k, p) == [int(z) for z in N_all(t, c, k, p)]
            m += 1
out.append(f"T1b: {m} extra cases p in 13,17,23, k in 3,5 random c: DP equals pure-Python-int object DP")
out.append("overflow margin: assert p^k < 2^62 in core._guard; max used p^k below, k=6 needs p < 1448, k=5 p < 4000+")
open('./compute/B/t1_output.txt', 'w').write("\n".join(out) + "\n")
print("\n".join(out))
