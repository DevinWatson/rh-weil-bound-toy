"""Core exact integer routines for the path-quadric twisted counts over F_p.

N_k(s) = sum over x in F_p^k with Q_c(x)=s of t(x_1)...t(x_k), Q_c = c_1 x1x2 + ... + c_{k-1} x_{k-1}x_k,
t(x) = chi(f(x)).  All arithmetic is exact int64 (overflow guard asserted) or Python int.
"""
import ctypes
import itertools
import numpy as np
from numpy.lib.stride_tricks import as_strided

try:
    ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x4000)
except Exception:
    pass

# polynomials as coefficient lists, lowest degree first
POLYS = {
    "x^3+x+1": [1, 1, 0, 1],
    "x^3-x": [0, -1, 0, 1],
    "x^3+2x+5": [5, 2, 0, 1],
    "x^5+x+1": [1, 1, 0, 0, 0, 1],
    "x^5-5x+3": [3, -5, 0, 0, 0, 1],
}
DISC = {  # exact discriminants (sympy), bad primes
    "x^3+x+1": [31],
    "x^3-x": [2],
    "x^3+2x+5": [7, 101],
    "x^5+x+1": [3, 7, 23],
    "x^5-5x+3": [5, 7],
}


def tvec(coeffs, p):
    x = np.arange(p, dtype=np.int64)
    v = np.zeros(p, dtype=np.int64)
    for a in reversed(coeffs):
        v = (v * x + a) % p
    chi = -np.ones(p, dtype=np.int64)
    chi[0] = 0
    chi[(x * x) % p] = 1
    chi[0] = 0
    return chi[v]


def good_prime(name, p):
    return p > 2 and p not in DISC[name]


def _guard(p, k):
    assert p ** k < 2 ** 62, "int64 overflow margin violated"


def dp_state(t, c, j, p):
    """state[v][r] after j variables: sum of prod t over x_1..x_j with x_j=v, partial Q = r."""
    _guard(p, j + 1)
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
        new[0] = t[0] * old.sum(axis=0)
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


def N_all(t, c, k, p):
    """vector N_k(s), s=0..p-1 (exact int64)."""
    if k == 1:
        r = np.zeros(p, dtype=np.int64)
        r[0] = int(t.sum())
        return r
    return dp_state(t, c, k, p).sum(axis=0)


def N_zero(t, c, k, p):
    """N_k(0) only; last transition costs p^2."""
    _guard(p, k)
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


def brute(t, c, k, p):
    res = [0] * p
    for x in itertools.product(range(p), repeat=k):
        q = 0
        w = 1
        for i in range(k):
            w *= int(t[x[i]])
            if w == 0:
                break
        if w == 0:
            continue
        for i in range(k - 1):
            q += int(c[i]) * x[i] * x[i + 1]
        res[q % p] += w
    return res


def primes_upto(n):
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return [int(i) for i in np.nonzero(s)[0]]
