# REF2 library: exact N_4 for the path quadric c1 x1x2 + c2 x2x3 + c3 x3x4 over F_p, weights t = chi(f).
# Formula under test (K4C E1, K4T A): N4 = -p + t0^2 M^2 + sum_r C(r) C(tau r), tau(r) = -(c3/c1) r - c2/c1.
# All integer arithmetic. FFT is used only as a fast route and is re-verified by direct integer sums on samples.
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
import ctypes
try:
    ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x4000)
except Exception:
    pass
import numpy as np

def chi_table(p):
    tab = np.full(p, -1, dtype=np.int64)
    tab[0] = 0
    for x in range(1, p):
        tab[(x * x) % p] = 1
    return tab

def poly_vals(p, coeffs):
    # coeffs highest first
    x = np.arange(p, dtype=np.int64)
    v = np.zeros(p, dtype=np.int64)
    for c in coeffs:
        v = (v * x + c) % p
    return v

def t_from_poly(p, coeffs):
    return chi_table(p)[poly_vals(p, coeffs)]

def Carray(p, t):
    r = np.arange(p, dtype=np.int64)
    x = np.arange(p, dtype=np.int64)
    idx = (np.outer(r, x)) % p
    return (t[idx] * t[None, :]).sum(axis=1)

def brute_N4(p, t, c):
    c1, c2, c3 = c
    tot = 0
    for x1 in range(p):
        for x2 in range(p):
            for x3 in range(p):
                # c3 x3 x4 = -(c1 x1 x2 + c2 x2 x3)
                rhs = (-(c1 * x1 * x2 + c2 * x2 * x3)) % p
                w = t[x1] * t[x2] * t[x3]
                if w == 0:
                    continue
                if (c3 * x3) % p == 0:
                    if rhs == 0:
                        tot += w * int(t.sum())
                else:
                    x4 = (rhs * pow(c3 * x3, -1, p)) % p
                    tot += w * t[x4]
    return int(tot)

def N4_formula(p, t, C, c):
    c1, c2, c3 = c
    inv1 = pow(c1, -1, p)
    r = np.arange(p, dtype=np.int64)
    tau = (-(c3 * inv1) * r - c2 * inv1) % p
    M = int(t.sum())
    t0 = int(t[0])
    return -p + t0 * t0 * M * M + int((C * C[tau]).sum())

def N4_table_c1_is_1(p, t, C):
    """returns array N[c2][c3] (c1 = 1) for c2,c3 in 0..p-1 via FFT, rounded; entries with c2=0 or c3=0 meaningless."""
    M = int(t.sum()); t0 = int(t[0])
    base = -p + t0 * t0 * M * M
    fa = np.conj(np.fft.fft(C.astype(np.float64)))
    N = np.zeros((p, p), dtype=np.int64)
    r = np.arange(p, dtype=np.int64)
    for c3 in range(1, p):
        g = C[(-c3 * r) % p].astype(np.float64)
        R = np.fft.ifft(fa * np.fft.fft(g)).real
        Ri = np.rint(R).astype(np.int64)
        u = np.arange(p, dtype=np.int64)
        c2 = (u * c3) % p
        N[c2, c3] = base + Ri[u]
    return N
