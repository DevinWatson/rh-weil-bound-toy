import itertools, sys
import numpy as np
from ffl import *

out = open('validate_out.txt', 'w')
def P(*a):
    s = ' '.join(str(x) for x in a); print(s); out.write(s + '\n'); out.flush()

def wmul(x, y):  # (a+bw)(c+dw) = ac + (ad+bc) w + bd w^2 = (ac - bd) + (ad+bc-bd) w
    a, b = x; c, d = y
    return (a*c - b*d, a*d + b*c - b*d)
def wadd(x, y): return (x[0]+y[0], x[1]+y[1])
WP = [(1,0),(0,1),(-1,-1)]   # omega^0,1,2

# 1. field sanity: tables, mul, trace additivity, trace linear
for m in (1,2,3,4,6):
    F = field(m)
    Q = F.Q
    el = np.arange(Q)
    rng = np.random.default_rng(1)
    a = rng.integers(0, Q, 200); b = rng.integers(0, Q, 200)
    assert np.all(F.trace(F.add(a,b)) == (F.trace(a)+F.trace(b)) % 3)
    # distributivity
    c = rng.integers(0, Q, 200)
    assert np.all(F.mul(a, F.add(b,c)) == F.add(F.mul(a,b), F.mul(a,c)))
    # multiplicative group order
    nz = a[a != 0]
    assert np.all(F.power(nz, Q-1) == 1)
    # Frobenius is additive
    assert np.all(F.power(F.add(a,b), 3) == F.add(F.power(a,3), F.power(b,3)))
    # trace equals sum of conjugates computed via power
    tr = a.copy()
    s = a.copy()
    for _ in range(m-1):
        s = F.power(s, 3); tr = F.add(tr, s)
    assert np.all(tr == F.trace(a)), "trace mismatch"
    P('field', m, 'ok')

# 2. fast transform vs direct double sum, Q = 9, 27 (and 3,81)
for m in (1, 2, 3, 4):
    F = field(m); Q = F.Q
    rng = np.random.default_rng(7 + m)
    g = rng.integers(-5, 6, Q);
    for a in [1, 2, 5 % Q or 1, Q-1]:
        a = int(a)
        if a == 0: continue
        u = bilinear_index(F, a)
        Ah, Bh = dft(g.astype(np.int64), np.zeros(Q, np.int64), m, [0])
        fa = Ah[u]; fb = Bh[u]
        # direct: sum_x g(x) w^{Tr(a x y)}
        for y in range(Q):
            tot = (0, 0)
            for x in range(Q):
                tr = int(F.trace(F.mul(F.mul(np.array([a]), np.array([x])), np.array([y])))[0])
                w = WP[tr]
                tot = wadd(tot, (int(g[x]) * w[0], int(g[x]) * w[1]))
            assert tot == (int(fa[y]), int(fb[y])), (m, a, y, tot, fa[y], fb[y])
    P('transform vs direct double sum, Q =', Q, 'ok')

# 3. S_h vs brute k-fold sum
def brute(F, fcodes, c_codes, h):
    Q = F.Q
    t = chi_array(F, fcodes)
    k = len(c_codes) + 1
    tot = (0, 0)
    for xs in itertools.product(range(Q), repeat=k):
        w = 1
        for x in xs:
            w *= int(t[x])
            if w == 0: break
        if w == 0: continue
        # Q_c = sum c_i x_i x_{i+1}
        acc = 0
        s = np.array([0])
        for i, c in enumerate(c_codes):
            term = F.mul(F.mul(np.array([c]), np.array([xs[i]])), np.array([xs[i+1]]))
            s = F.add(s, term)
        hv = F.mul(np.array([h]), s)
        tr = int(F.trace(hv)[0])
        tot = wadd(tot, (w * WP[tr][0], w * WP[tr][1]))
    return tot

cases = [
  # (m, f coefficient codes (low->high), c codes, h code, label)
  (1, [2, 1], [1], 1, 'F3 f=x-1,k=2'),
  (1, [2, 1], [1, 2], 1, 'F3 f=x-1,k=3'),
  (1, [1, 2, 0, 1], [1], 2, 'F3 f=x^3-x+1,k=2'),
  (2, [2, 1], [3, 5], 1, 'F9 f=x-1,k=3'),
  (2, [1, 2, 0, 1], [4], 1, 'F9 f=x^3-x+1,k=2'),
  (2, [2, 1], [1, 2, 3], 7, 'F9 f=x-1,k=4'),
  (3, [2, 1], [1], 1, 'F27 f=x-1,k=2'),
  (3, [1, 2, 0, 1], [1], 2, 'F27 f=x^3-x+1,k=2'),
  (3, [2, 1], [1, 2], 1, 'F27 f=x-1,k=3 (27^3 terms)'),
]
for m, fc, cc, h, lab in cases:
    F = field(m)
    t = chi_array(F, fc)
    # independent chi: z^((Q-1)/2)
    ys = np.arange(F.Q)
    fy = np.zeros(F.Q, dtype=np.int64)
    for i in reversed(range(len(fc))):
        fy = F.add(F.mul(fy, ys), np.full(F.Q, fc[i]))
    pw = F.power(fy, (F.Q-1)//2)
    chi2 = np.where(fy == 0, 0, np.where(pw == 1, 1, -1))
    assert np.all(chi2 == t), 'chi mismatch'
    fast = fibre_sum(F, t, cc, h)[:2]
    b = brute(F, fc, cc, h)
    P(lab, 'fast', fast, 'brute', b, 'OK' if fast == b else 'MISMATCH')
    assert fast == b
P('all validation passed')
