import ctypes, itertools
ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x4000)
import numpy as np
from fractions import Fraction

def legendre(a, p):
    a %= p
    if a == 0: return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1

def theta_dp(k, Q, t0, M):
    # Theta = sum_x prod t(x_i) (-1)^j (Q-1)^(k-j), j = # adjacent pairs with both x nonzero
    A = M - t0   # sum of t over nonzero x
    # state 0: last x is zero, state 1: last nonzero
    s0 = Fraction(t0 * (Q - 1)); s1 = Fraction(A * (Q - 1))
    for _ in range(k - 1):
        n0 = (s0 + s1) * t0 * (Q - 1)
        n1 = (s0 + s1 * Fraction(-1, Q - 1)) * A * (Q - 1)
        s0, s1 = n0, n1
    return s0 + s1

def check(k, p, coeffs):
    f = lambda x: sum(c * pow(x, i, p) for i, c in enumerate(coeffs)) % p
    t = np.array([legendre(f(x), p) for x in range(p)], dtype=np.int64)
    M = int(t.sum()); t0 = int(t[0])
    pts = np.array(list(itertools.product(range(p), repeat=k)), dtype=np.int64)
    wt = np.ones(len(pts), dtype=np.int64)
    for i in range(k):
        wt *= t[pts[:, i]]
    total = 0
    for c in itertools.product(range(1, p), repeat=k - 1):
        Qv = np.zeros(len(pts), dtype=np.int64)
        for i in range(k - 1):
            Qv += c[i] * pts[:, i] * pts[:, i + 1]
        total += int(wt[Qv % p == 0].sum())
    th = theta_dp(k, p, t0, M)
    rhs = Fraction((p - 1) ** (k - 1) * M ** k, 1) + th
    lhs = Fraction(p * total)
    return lhs, rhs, M, th

if __name__ == '__main__':
    out = []
    cases = [(4, 7, [5, 2, 0, 1]), (4, 5, [1, 1, 0, 1]), (5, 5, [1, 1, 0, 1]), (5, 7, [5, 2, 0, 1]), (6, 5, [1, 1, 0, 1]), (6, 5, [2, 3, 0, 1])]
    bad = 0
    for k, p, co in cases:
        lhs, rhs, M, th = check(k, p, co)
        ok = (lhs == rhs)
        bad += (not ok)
        out.append(f"k={k} p={p} f={co}: M={M} sum_c qN_c={lhs} formula (q-1)^(k-1) M^k + Theta = {rhs} Theta={th} match={ok}")
    out.append(f"mismatches: {bad}")
    open('cavg_out.txt', 'w').write('\n'.join(out) + '\n')
    print('\n'.join(out))
