"""Shared exact-integer helpers for the k = 4 computation (agent K4C, round two).
Prime fields F_p only. No floating point is used for any CHECKED figure."""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_v] = "1"
import ctypes
try:
    ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x4000)
except Exception:
    pass
import itertools
import numpy as np


def primes_upto(n):
    s = [True] * (n + 1)
    s[0] = s[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            for j in range(i * i, n + 1, i):
                s[j] = False
    return [i for i in range(n + 1) if s[i]]


def chi_table(p):
    chi = -np.ones(p, dtype=np.int64)
    chi[(np.arange(1, p) ** 2) % p] = 1
    chi[0] = 0
    return chi


def poly_vals(p, coefs):
    """coefs low degree first (ints, any sign); values at 0..p-1 mod p."""
    x = np.arange(p, dtype=np.int64)
    v = np.zeros(p, dtype=np.int64)
    for c in reversed(coefs):
        v = (v * x + c) % p
    return v


def t_table(p, coefs):
    return chi_table(p)[poly_vals(p, coefs)]


def _trim(a):
    while a and a[-1] == 0:
        a.pop()
    return a


def _polymod(a, b, p):
    a = a[:]
    inv = pow(b[-1], p - 2, p)
    while len(a) >= len(b):
        c = (a[-1] * inv) % p
        if c:
            for i in range(len(b)):
                a[len(a) - len(b) + i] = (a[len(a) - len(b) + i] - c * b[i]) % p
        a.pop()
        _trim(a)
    return a


def squarefree_mod_p(coefs, p):
    f = _trim([c % p for c in coefs])
    df = _trim([(i * f[i]) % p for i in range(1, len(f))])
    a, b = f, df
    while b:
        a, b = b, _polymod(a, b, p)
    return len(a) == 1  # gcd is a nonzero constant


def Cvec(p, t):
    """C[r] = sum_x t(x) t(r x), r = 0..p-1 (exact ints)."""
    r = np.arange(p, dtype=np.int64)
    idx = (r[:, None] * r[None, :]) % p
    return (t[idx] * t[None, :]).sum(axis=1)


def N4_brute(p, t, c):
    """direct: sum of t(x1)..t(x4) over x in F_p^4 with c1 x1x2 + c2 x2x3 + c3 x3x4 = 0 mod p."""
    x1, x2, x3, x4 = np.indices((p,) * 4).reshape(4, -1)
    Q = (c[0] * x1 * x2 + c[1] * x2 * x3 + c[2] * x3 * x4) % p
    w = t[x1] * t[x2] * t[x3] * t[x4]
    return int(w[Q == 0].sum())


def E_ab(p, C, a, b):
    r = np.arange(p, dtype=np.int64)
    return int((C * C[(a * r + b) % p]).sum())


def roots_mod_p(coefs, p):
    v = poly_vals(p, coefs)
    return [int(x) for x in np.nonzero(v == 0)[0]]


def poly_from_roots(roots, p):
    co = [1]
    for r in roots:
        new = [0] * (len(co) + 1)
        for i, c in enumerate(co):
            new[i + 1] = (new[i + 1] + c) % p
            new[i] = (new[i] - r * c) % p
        co = new
    return co


def first_irreducible_cubic(p):
    for c in range(1, p):
        for b in range(p):
            for a in range(p):
                co = [c, b, a, 1]
                if not roots_mod_p(co, p):
                    return co
    return None


def pick_quintic(p):
    for c in range(1, p):
        co = [c, 1, 0, 0, 0, 1]
        if squarefree_mod_p(co, p):
            return co
    return None
