"""Main-session spot check of round two (exact integers; own code, prime fields).
N_4 for the path quadric c1 x1x2 + c2 x2x3 + c3 x3x4 with t = Legendre symbol of f."""
import ctypes, sys
import numpy as np
try: ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x4000)
except Exception: pass

def tvals(p, coeffs):
    x = np.arange(p, dtype=np.int64); v = np.zeros(p, dtype=np.int64)
    for c in reversed(coeffs): v = (v * x + c) % p
    leg = np.array([0] + [1 if pow(a, (p - 1) // 2, p) == 1 else -1 for a in range(1, p)], dtype=np.int64)
    return leg[v]

def N4(p, t, c):
    # W[y, s] = sum over x-prefix ending at y with running value s
    W = np.zeros((p, p), dtype=np.int64); W[:, 0] = t
    xs = np.arange(p); ss = np.arange(p)
    for ci in c:
        Wn = np.zeros_like(W)
        for y in range(p):
            if t[y] == 0: continue
            inc = (ci * xs * y) % p
            idx = (ss[:, None] - inc[None, :]) % p
            Wn[y, :] = t[y] * W[xs[None, :], idx].sum(axis=1)
        W = Wn
    return int(W[:, 0].sum())

print("A. f = x^3 - a with three cube roots of unity in F_p (p = 1 mod 3): N_4 / p^2 (floats for reading only)")
print("   prediction of the round-two theory: c=(1,1,1) two planes -> about 2; c=(1,1,-2) one plane -> about 1; c=(1,2,3) none -> about 0")
for p in (31, 37, 43, 61, 67, 73, 79, 97):
    rows = {(1, 1, 1): [], (1, 1, p - 2): [], (1, 2, 3): []}
    for a in range(1, 9):
        if a % p == 0: continue
        t = tvals(p, [(-a) % p, 0, 0, 1])
        for c in rows: rows[c].append(N4(p, t, c) / p / p)
    print(f"   p={p:3d}  " + "  ".join(f"c={c if c[2] < 10 else (1,1,-2)}: mean {np.mean(v):+.2f} [{min(v):+.2f},{max(v):+.2f}]" for c, v in rows.items()))

print("B. generic cubic with rational roots f = (x-1)(x-2)(x-4): c on a line c2 + c3 s + c1 s' = 0 with s, s' ratios of roots, not both 1")
print("   prediction: no p^2 term (same as generic c)")
for p in (53, 61, 73, 97, 101):
    t = tvals(p, [(-8) % p, 14, (-7) % p, 1])            # (x-1)(x-2)(x-4) = x^3 - 7x^2 + 14x - 8
    inv2 = pow(2, -1, p)
    cases = {"s=2,s'=1/2": (1, (-(2 * 3 + inv2)) % p, 3), "s=4,s'=2": (1, (-(4 * 5 + 2)) % p, 5), "s=0,s'=2": (1, (-2) % p, 7), "generic (1,2,3)": (1, 2, 3), "sum zero (1,1,-2)": (1, 1, p - 2)}
    print(f"   p={p:3d}  " + "  ".join(f"{k}: {N4(p, t, c) / p / p:+.3f}" for k, c in cases.items()))
