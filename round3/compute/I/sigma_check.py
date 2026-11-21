"""Referee I.  Three independent checks of the Fourier induction bookkeeping (exact arithmetic only).

Part 1: singular-set recursion.  Points are symbolic: (sign, exponent tuple of c_1..c_{k-1}, root label or None for 0).
        The rule used (from the frequency/stationary-phase statement, derived independently in the report):
          P_1 : finite singular set S_1 = Z, slope-0 part at infinity present (T0), no nonzero frequencies.
          Q_i = FT_{h c_i}(P_i): Sing(Q_i)\{0} = { -a/(h c_i) : a a nonzero frequency of P_i at infinity }, 0 in Sing iff T0(P_i).
          P_{i+1} = j_!L (x) Q_i : S_{i+1} = Z u Sing(Q_i); nonzero frequencies of P_{i+1} = { h c_i s : s in S_i\{0} };
                                   T0(P_{i+1}) iff 0 in S_i.
        Compare with Sigma_i of the brief and with B's closed form.
Part 2: dimension bookkeeping with exact Fractions, generic values, compare with D_k = r_{k+1} - [k odd].
Part 3: explicit choice c_j = g^(2^j) in F_Q^*, Q = q^(m*l): check, in exponent arithmetic mod Q-1 (exact big integers),
        that no condition 'pi in R' holds.
"""
import itertools, sys
from fractions import Fraction

# ---------------- Part 1 -----------------
def sigma_symbolic(k, nroots):
    # point = (sign, exps tuple length k-1 (index j-1 for c_j), root) ; root None = 0 point
    zero_exp = tuple([0] * (k - 1))
    Z = [(1, zero_exp, ('z', r)) for r in range(nroots)]
    S = {1: set(Z)}
    T0 = {1: True}
    freq = {1: set()}          # frequencies / h  as points  c_{i-1} * s
    Sing = {}
    for i in range(1, k):      # Q_i
        sing = set()
        for a in freq[i]:      # a = (sign, exps, root) represents a/h ; w = -a/(c_i)
            sg, ex, rt = a
            ex = list(ex); ex[i - 1] -= 1
            sing.add((-sg, tuple(ex), rt))
        if T0[i]:
            sing.add((1, zero_exp, None))
        Sing[i] = sing
        # P_{i+1}
        S[i + 1] = set(Z) | sing
        T0[i + 1] = any(p[2] is None for p in S[i])
        fr = set()
        for (sg, ex, rt) in S[i]:
            if rt is None:
                continue
            ex = list(ex); ex[i - 1] += 1
            fr.add((sg, tuple(ex), rt))
        freq[i + 1] = fr
    return Sing, S

def brief_sigma(k, nroots):
    # Sigma_1={0}, Sigma_2 = rho_2 Z, Sigma_i = rho_i (Z u Sigma_{i-2}); rho_i = -c_{i-1}/c_i
    zero_exp = tuple([0] * (k - 1))
    Z = [(1, zero_exp, ('z', r)) for r in range(nroots)]
    def mulrho(i, pts):
        out = set()
        for (sg, ex, rt) in pts:
            ex = list(ex)
            ex[i - 2] += 1   # c_{i-1}
            ex[i - 1] -= 1   # c_i
            out.add((-sg, tuple(ex), rt))
        return out
    Sig = {1: {(1, zero_exp, None)}}
    if k >= 3 or True:
        pass
    for i in range(2, k):
        base = set(Z)
        if i >= 3:
            base |= Sig[i - 2]
        # 0 is carried to 0 : rho_i*0 = 0 (sign/exps irrelevant for the zero point)
        pts = set()
        for p in base:
            if p[2] is None:
                pts.add((1, zero_exp, None))
            else:
                pts |= mulrho(i, {p})
        Sig[i] = pts
    return Sig

def show(pt):
    sg, ex, rt = pt
    if rt is None:
        return '0'
    mon = ''.join('c%d^%d*' % (j + 1, e) for j, e in enumerate(ex) if e)
    return ('-' if sg < 0 else '+') + mon + 'z%d' % rt[1]

def part1():
    out = []
    for k in range(2, 7):
        Sing, S = sigma_symbolic(k, 1)
        Sig = brief_sigma(k, 1)
        ok = all(Sing[i] == Sig[i] for i in range(1, k))
        out.append('k=%d  (recursion rederived == brief Sigma_i for i<=k-1): %s' % (k, ok))
        for i in range(1, k):
            out.append('   Sigma_%d = {%s}' % (i, ', '.join(sorted(show(p) for p in Sing[i]))))
    return out

# ---------------- Part 2 -----------------
def bookkeeping(d, k, seed=1):
    import random
    random.seed(seed)
    # generic rationals: distinct nonzero roots, random c_i
    Z = [Fraction(random.randint(2, 10 ** 6), random.randint(1, 10 ** 3)) for _ in range(d)]
    c = [Fraction(random.randint(2, 10 ** 6), random.randint(1, 10 ** 3)) for _ in range(k - 1)]
    r = 1
    sing = {z: 1 for z in Z}   # drops
    freq = {}
    T0 = 1                     # dim of slope-0 part at infinity (P_1: L_inf)
    out = [sum(sing.values()) + sum(freq.values()) - r]
    for i in range(1, k):
        ci = c[i - 1]
        rnew = sum(sing.values())
        newsing = {}
        for a, dim in freq.items():
            newsing[-a / ci] = newsing.get(-a / ci, 0) + dim
        if T0:
            newsing[Fraction(0)] = newsing.get(Fraction(0), 0) + T0
        for z in Z:
            assert z not in newsing, 'coincidence'
            newsing[z] = rnew
        newfreq = {}
        newT0 = 0
        for s, dim in sing.items():
            if s == 0:
                newT0 += dim
            else:
                newfreq[ci * s] = newfreq.get(ci * s, 0) + dim
        r, sing, freq, T0 = rnew, newsing, newfreq, newT0
        out.append(sum(sing.values()) + sum(freq.values()) - r)
    return out

def formula(d, kmax):
    rr = [None, 1, d]
    for i in range(2, kmax + 2):
        rr.append(d * rr[i] + rr[i - 1])
    return [rr[k + 1] - (1 if k % 2 == 1 else 0) for k in range(1, kmax + 1)]

def part2():
    out = []
    for d in (1, 2, 3, 5, 7):
        got = bookkeeping(d, 8)
        want = formula(d, 8)
        out.append('d=%d  bookkeeping D_1..D_8 = %s ; formula = %s ; equal: %s' % (d, got, want, got == want))
    return out

# ---------------- Part 3 -----------------
def isprime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def part3():
    out = []
    import random
    random.seed(7)
    for (q, m, k) in [(3, 1, 5), (3, 3, 5), (5, 2, 6), (7, 3, 7), (3, 4, 8)]:
        N0 = q ** m - 1
        l = 2 ** k + 1
        while not (isprime(l) and N0 % l != 0):
            l += 1
        s = m * l
        Qm1 = q ** s - 1               # |F_Q^*|
        # roots: d distinct elements of mu_{N0}, written as exponents of g: g^((Qm1//N0)*u)
        step = Qm1 // N0
        d = min(5, N0)
        us = random.sample(range(1, N0), d) if N0 > d else list(range(1, N0 + 1))
        # R = ratios z'/z, as set of exponents mod Qm1
        R = {(step * (u2 - u1)) % Qm1 for u1 in us for u2 in us}
        e = [None] + [2 ** j for j in range(1, k)]     # c_j = g^(2^j), j=1..k-1
        half = Qm1 // 2                              # -1 = g^half
        bad = 0
        nconds = 0
        for i in range(2, k):            # i = 2..k-1
            for mm in range(0, i // 2):  # m = 0..floor(i/2)-1
                # pi = rho_i rho_{i-2} ... rho_{i-2m},  rho_j = -c_{j-1}/c_j
                ex = 0
                sgn = 0
                for a in range(mm + 1):
                    j = i - 2 * a
                    ex += e[j - 1] - e[j]
                    sgn += 1
                ex = (ex + (half if sgn % 2 == 1 else 0)) % Qm1
                nconds += 1
                if ex in R:
                    bad += 1
        # also check g^(2^j) all distinct nonzero exponents mod Qm1 (c_j nonzero automatically)
        out.append('q=%d m=%d k=%d  l=%d (prime > 2^k, l not | q^m-1)  Q=q^%d  conditions checked=%d  violations=%d  |R|=%d' %
                   (q, m, k, l, s, nconds, bad, len(R)))
    return out

if __name__ == '__main__':
    lines = ['PART 1  singular-set recursion (symbolic, exact)'] + part1()
    lines += ['', 'PART 2  dimension bookkeeping with exact Fractions'] + part2()
    lines += ['', 'PART 3  explicit c_j = g^(2^j)'] + part3()
    txt = '\n'.join(lines)
    print(txt)
    open('sigma_check_out.txt', 'w', encoding='utf-8').write(txt + '\n')
