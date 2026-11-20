"""H1: exact Euler characteristic check of Y^0 = {x in (F_p \ Z)^k : Q(x)=0}, path quadric, all c=1.
chi_c(Y,K) = chi_c(Y^0) for tame rank-one K (cited: GOS-type formula). We fit the generic point-count polynomial
P_k(q) (mode over root sets) and evaluate P_k(1).  Exact integer arithmetic only.
Claims tested: k=2 -> 1-2d ; k=3 -> 3d^2-3d+1 ; k=4 -> 1-4d+3d^2-4d^3 (A's hand count).
"""
import ctypes, itertools, random, sys
ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x4000)
import os
os.environ["OMP_NUM_THREADS"] = "1"
import numpy as np
from collections import Counter
from fractions import Fraction

def count_Y0(p, k, roots):
    w = np.ones(p, dtype=np.int64)
    for r in roots:
        w[r] = 0
    ar = np.arange(p)
    vec = np.zeros((p, p), dtype=np.int64)   # vec[x_j, s]
    vec[:, 0] = w
    for _ in range(k - 1):
        new = np.zeros((p, p), dtype=np.int64)
        for xp in range(p):
            if w[xp] == 0:
                continue
            cols = (ar[None, :] - (ar * xp)[:, None]) % p   # s' - x*xp
            new[xp] = vec[ar[:, None], cols].sum(axis=0)
        vec = new
    return int(vec[:, 0].sum())

def mode_count(p, k, d, ntrials, rng):
    cnt = Counter()
    seen = set()
    for _ in range(ntrials):
        roots = tuple(sorted(rng.sample(range(p), d)))
        if roots in seen:
            continue
        seen.add(roots)
        cnt[count_Y0(p, k, roots)] += 1
    return cnt

def fit_poly(points, deg):
    # exact Lagrange/least-determined fit through first deg+1 points, check the rest
    from sympy import symbols, interpolate, Rational
    x = symbols('x')
    pts = points[:deg + 1]
    poly = interpolate([(a, b) for a, b in pts], x)
    ok = all(poly.subs(x, a) == b for a, b in points)
    return poly, ok

if __name__ == "__main__":
    d = int(sys.argv[1]); k = int(sys.argv[2])
    primes = [int(a) for a in sys.argv[3].split(',')]
    ntr = int(sys.argv[4])
    rng = random.Random(20261120)
    pts = []
    for p in primes:
        cnt = mode_count(p, k, d, ntr, rng)
        top = cnt.most_common(3)
        print("p=%d d=%d k=%d  top counts (value,freq): %s  trials=%d" % (p, d, k, top, sum(cnt.values())), flush=True)
        pts.append((p, top[0][0]))
    poly, ok = fit_poly(pts, k - 1)
    print("fitted P(q) =", poly, " consistent with all points:", ok)
    print("P(1) =", poly.subs('x', 1) if False else poly.subs(list(poly.free_symbols)[0], 1))
    print("claimed chi_c:", {2: 1 - 2 * d, 3: 3*d*d - 3*d + 1, 4: 1 - 4*d + 3*d*d - 4*d**3}.get(k))
