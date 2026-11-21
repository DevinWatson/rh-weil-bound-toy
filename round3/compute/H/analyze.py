"""Exact analysis in Q(omega): L-series, trailing zeros, Hankel ranks; floating roots as HINT.
usage: python analyze.py results.jsonl out.txt"""
import sys, json, math
from fractions import Fraction as Fr
import numpy as np

class W:
    """a + b*omega, omega^2 = -1 - omega, exact rationals"""
    __slots__ = ('a', 'b')
    def __init__(s, a=0, b=0): s.a = Fr(a); s.b = Fr(b)
    def __add__(s, o): return W(s.a + o.a, s.b + o.b)
    def __sub__(s, o): return W(s.a - o.a, s.b - o.b)
    def __mul__(s, o):
        if not isinstance(o, W): return W(s.a * o, s.b * o)
        return W(s.a * o.a - s.b * o.b, s.a * o.b + s.b * o.a - s.b * o.b)
    def inv(s):
        N = s.a * s.a - s.a * s.b + s.b * s.b
        return W((s.a - s.b) / N, -s.b / N)
    def iszero(s): return s.a == 0 and s.b == 0
    def c(s): return complex(float(s.a) - 0.5 * float(s.b), float(s.b) * math.sqrt(3) / 2)
    def __repr__(s): return '(%s %+s w)' % (s.a, s.b) if s.a.denominator == 1 and s.b.denominator == 1 else '(%s,%s)' % (s.a, s.b)

def series(S, k, N):
    sgn = 1 if (k + 1) % 2 == 0 else -1
    a = {j: W(sgn * S[j][0], sgn * S[j][1]) for j in range(1, N + 1)}
    L = [W(1, 0)]
    for n in range(1, N + 1):
        acc = W(0, 0)
        for j in range(1, n + 1):
            acc = acc + a[j] * L[n - j]
        L.append(acc * Fr(1, n))
    return L

def rank(M):
    M = [row[:] for row in M]
    r = 0
    rows, cols = len(M), len(M[0]) if M else 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if not M[i][c].iszero(): piv = i; break
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        iv = M[r][c].inv()
        for i in range(r + 1, rows):
            if not M[i][c].iszero():
                fct = M[i][c] * iv
                M[i] = [M[i][j] - fct * M[r][j] for j in range(cols)]
        r += 1
        if r == rows: break
    return r

def hankel_info(S, N):
    # sequence S_1..S_N ; matrix p x (N-p+1) entries S_{i+j-1}; report rank for p = floor((N+1)/2)
    p = (N + 1) // 2
    cols = N - p + 1
    M = [[W(*S[i + j + 1]) for j in range(cols)] for i in range(p)]
    return rank(M), p, cols

def main():
    inf, outf = sys.argv[1], sys.argv[2]
    recs = {}
    for line in open(inf):
        r = json.loads(line)
        recs.setdefault(r['name'], {})[r['n']] = r
    out = open(outf, 'w')
    def P(*a):
        s = ' '.join(str(x) for x in a); print(s); out.write(s + '\n'); out.flush()
    summary = {}
    for name, d in recs.items():
        ns = sorted(d)
        N = 0
        while (N + 1) in d: N += 1
        r0 = d[ns[0]]
        k, e = r0['k'], r0['e']
        q = 3 ** e
        S = {n: (d[n]['a'], d[n]['b']) for n in range(1, N + 1)}
        L = series(S, k, N)
        nz = [j for j in range(N + 1) if not L[j].iszero()]
        last = nz[-1]
        trailing = N - last
        # coefficient integrality: L_j in Z[omega]?
        integral = all(x.a.denominator == 1 and x.b.denominator == 1 for x in L)
        rk, p, cols = hankel_info(S, N)
        P('=' * 70)
        P(name, ' k=%d q=%d f=%s cexp=%s hexp=%s  n=1..%d' % (k, q, r0['f'], r0['cexp'], r0['hexp'], N))
        P('  L coefficients (Z[omega] pairs a + b w), j=0..%d:' % N)
        for j in range(N + 1):
            P('    L_%d = %s' % (j, L[j]))
        P('  all L_j in Z[omega]:', integral)
        P('  last nonzero index = %d, trailing exact zeros = %d' % (last, trailing))
        P('  Hankel rank of S_1..S_%d (%dx%d matrix): %d %s' % (N, p, cols, rk,
          '(full rank: no recurrence of order < %d detected)' % p if rk == p else '(rank deficient: recurrence of order %d)' % rk))
        # floating roots HINT, only if polynomial claimed (>=1 trailing zero) - report anyway for degree=last
        deg = last
        w_max = None
        if deg >= 1:
            coeffs = [L[j].c() for j in range(deg + 1)]   # L(T) = sum L_j T^j
            # reciprocal roots beta: roots of z^deg * L(1/z) = sum L_j z^(deg-j)
            rts = np.roots(coeffs)  # highest degree coeff first == L_0 z^deg ... need L_j z^(deg-j): poly with coeff[0]=L_0 for z^deg
            mods = np.abs(rts)
            if len(mods):
                w_max = 2 * math.log(mods.max()) / math.log(q)
                P('  HINT (floating): %d reciprocal roots, largest |beta| = q^(%.4f/2)  (Claim A needs <= q^((k+1)/2) = q^(%d/2)); smallest = q^(%.4f/2)'
                  % (len(mods), w_max, k + 1, 2 * math.log(max(mods.min(), 1e-300)) / math.log(q)))
        summary[name] = dict(k=k, e=e, N=N, last_nonzero=last, trailing_zeros=trailing, hankel_rank=rk, hankel_p=p, integral=integral, wmax=w_max)
    json.dump(summary, open(outf + '.summary.json', 'w'), indent=1)

main()
