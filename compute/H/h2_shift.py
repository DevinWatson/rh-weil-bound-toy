"""H2: does the 'odd f' anomaly (N_k ~ p^(k/2) for x^3-x) come from f(0)=0 (the cone vertex lies on a root hyperplane)?
Test: compare x^3-x with its translate f(x+2) = (x+2)^3-(x+2) (isomorphic curve, same M, f(0)=6 != 0, roots -1,-2,-3 not symmetric)
and with a generic cubic x^3+2x+5.  Path quadric, all c=1.  Exact integer DP (int64, p^k < 2^62), Fractions for ratios.
Output is exact integers N_k; ratios are printed as exact fractions and as floats (floats are HINT only).
"""
import ctypes, os, sys
ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x4000)
os.environ["OMP_NUM_THREADS"] = "1"
import numpy as np
from fractions import Fraction

def legendre_table(p, coeffs):
    ar = np.arange(p, dtype=object)
    t = np.zeros(p, dtype=np.int64)
    for x in range(p):
        v = 0
        for c in coeffs:           # highest degree first
            v = (v * x + c) % p
        t[x] = 0 if v == 0 else (1 if pow(v, (p - 1) // 2, p) == 1 else -1)
    return t

def N_k(p, t, k):
    assert p ** k < 2 ** 62
    ar = np.arange(p)
    vec = np.zeros((p, p), dtype=np.int64)
    vec[:, 0] = t
    for step in range(k - 1):
        last = (step == k - 2)
        new = np.zeros((p, p), dtype=np.int64)
        for xp in range(p):
            if t[xp] == 0:
                continue
            if last:
                s_idx = (-(ar * xp)) % p
                new[xp, 0] = t[xp] * vec[ar, s_idx].sum()
            else:
                cols = (ar[None, :] - (ar * xp)[:, None]) % p
                new[xp] = t[xp] * vec[ar[:, None], cols].sum(axis=0)
        vec = new
    return int(vec[:, 0].sum())

def shift_poly(coeffs, a, p):
    # coefficients (highest first) of f(x+a) mod p
    from numpy.polynomial import polynomial as P
    n = len(coeffs)
    res = [0] * n
    # Horner in Python ints: f(x+a) = sum c_i (x+a)^(deg-i)
    poly = [0]
    for c in coeffs:
        # poly = poly*(x+a) + c ; list low->high
        new = [0] * (len(poly) + 1)
        for i, u in enumerate(poly):
            new[i + 1] += u
            new[i] += a * u
        new[0] += c
        poly = [v % p for v in new]
    return list(reversed(poly))[-n:] if len(poly) > n else list(reversed(poly))

if __name__ == "__main__":
    primes = [int(a) for a in sys.argv[1].split(',')]
    ks = [int(a) for a in sys.argv[2].split(',')]
    funcs = {"x^3-x": [1, 0, -1, 0], "x^3-x shifted by 2": None, "x^3+2x+5": [1, 0, 2, 5]}
    print("f\tp\tk\tM\tN_k\tN^2/p^(k-1)\tN^2/p^k")
    for p in primes:
        base = [c % p for c in funcs["x^3-x"]]
        sh = shift_poly(base, 2, p)
        # shift_poly returns highest-first coefficients incl. leading
        co = {"x^3-x": base, "x^3-x shifted by 2": sh, "x^3+2x+5": [c % p for c in funcs["x^3+2x+5"]]}
        for name, cf in co.items():
            t = legendre_table(p, cf)
            M = int(t.sum())
            for k in ks:
                N = N_k(p, t, k)
                r1 = Fraction(N * N, p ** (k - 1)); r2 = Fraction(N * N, p ** k)
                print("%s\t%d\t%d\t%d\t%d\t%s\t%s" % (name, p, k, M, N, "%.3f" % float(r1), "%.3f" % float(r2)), flush=True)
