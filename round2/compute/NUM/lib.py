"""Shared exact routines for the NUM agent.  Wraps validated B/core.py (guard replaced by an explicit
bound check: int64 wraparound is exact ring arithmetic mod 2^64, and N_k(s) is bounded by 2 p^(k-1))."""
import sys, time
sys.path.insert(0, r"./compute/B")
import numpy as np
import core
import sympy

core._guard = lambda p, k: None  # replaced by check_bound below

X = sympy.Symbol("x")
POLYS = {  # lowest degree first
    "f1": [5, 2, 0, 1],            # x^3+2x+5
    "f2": [3, 0, 1, 1],            # x^3+x^2+3
    "f3": [-8, 14, -7, 1],         # (x-1)(x-2)(x-4) = x^3-7x^2+14x-8
    "f4": [1, 1, 0, 0, 0, 1],      # x^5+x+1
}
assert sympy.expand((X - 1) * (X - 2) * (X - 4)) == X**3 - 7 * X**2 + 14 * X - 8
DISC = {}
for nm, co in POLYS.items():
    P = sympy.Poly(sum(a * X**i for i, a in enumerate(co)), X)
    DISC[nm] = int(sympy.discriminant(P))


def good(nm, p):
    """p odd, f squarefree mod p (p does not divide disc, leading coeff 1), f(0) != 0 mod p."""
    return p > 2 and DISC[nm] % p != 0 and POLYS[nm][0] % p != 0


def tv(nm, p):
    return core.tvec(POLYS[nm], p)


def check_bound(p, k):
    assert 2 * p ** (k - 1) < 2 ** 63, "N_k(s) may not fit int64"


from numpy.lib.stride_tricks import as_strided


def dp_state(t, c, j, p):
    """as core.dp_state but any c_i mod p allowed (c_i = 0: the two variables decouple)."""
    old = np.zeros((p, p), dtype=np.int64)
    old[:, 0] = t
    v = np.arange(p, dtype=np.int64)
    Ad = np.empty((p, 2 * p), dtype=np.int64)
    flat = Ad.reshape(-1)
    sub = flat[p:]
    sv = as_strided(sub, shape=(p, p), strides=((2 * p - 1) * 8, 8))
    for step in range(j - 1):
        ci = int(c[step]) % p
        new = np.zeros_like(old)
        s0 = old.sum(axis=0)
        new[0] = t[0] * s0
        if ci == 0:
            for w in range(1, p):
                new[w] = t[w] * s0
        else:
            for w in range(1, p):
                if t[w] == 0:
                    continue
                inv = pow(ci * w % p, -1, p)
                perm = (v * inv) % p
                Ad[:, :p] = old[perm]
                Ad[:, p:] = Ad[:, :p]
                new[w] = t[w] * sv.sum(axis=0)
        old = new
    return old


def Nall(t, c, k, p):
    check_bound(p, k)
    if k == 1:
        r = np.zeros(p, dtype=np.int64); r[0] = int(t.sum()); return r
    return dp_state(t, c, k, p).sum(axis=0)


def Nzero(t, c, k, p):
    """N_k(0); equals Nall(...)[0] (last transition done directly, cost p^2)."""
    check_bound(p, k)
    if k == 1:
        return int(t.sum())
    st = dp_state(t, c, k - 1, p)
    ci = int(c[k - 2]) % p
    v = np.arange(p, dtype=np.int64)
    tot = 0
    for w in range(p):
        if t[w] == 0:
            continue
        tot += int(t[w]) * int(st[v, (-ci * v * w) % p].sum())
    return tot


def moment_data(t, N):
    """exact python ints"""
    return [int(v) for v in N]


def primes_upto(n):
    return core.primes_upto(n)


def now():
    return time.time()
