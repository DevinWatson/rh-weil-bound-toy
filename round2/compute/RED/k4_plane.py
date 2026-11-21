import ctypes, itertools, sys
ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x4000)
from fractions import Fraction

def chi_table(p, coeffs):
    # f(x)=sum coeffs[i] x^i ; returns t[x]=chi(f(x)) in {-1,0,1}, r=#roots
    sq = {(y*y) % p for y in range(1, p)}
    t = []
    for x in range(p):
        v = sum(c * pow(x, i, p) for i, c in enumerate(coeffs)) % p
        t.append(0 if v == 0 else (1 if v in sq else -1))
    return t

def squarefree(p, coeffs):
    # discriminant check by brute force: f and f' have no common root in closure -> use gcd via sympy-free poly gcd
    from sympy import Poly, symbols, GF, gcd
    X = symbols('X')
    f = Poly(sum(c * X**i for i, c in enumerate(coeffs)), X, modulus=p)
    return gcd(f, f.diff(X)).degree() == 0

def N4_fast(p, t, c):
    c1, c2, c3 = c
    M = sum(t); t0 = t[0]
    inv = [0] + [pow(a, p - 2, p) for a in range(1, p)]
    Ccache = {}
    def C(s):
        if s not in Ccache:
            Ccache[s] = sum(t[x] * t[(s * x) % p] for x in range(p))
        return Ccache[s]
    total = t0 * t0 * (M * M + M * (M - t0))
    for x3 in range(1, p):
        w = c3 * x3 % p
        xs = (-c2 * x3 * inv[c1]) % p
        total += t[x3] * t[xs] * t0 * M
        for x1 in range(p):
            if x1 == xs: continue
            u = (c1 * x1 + c2 * x3) % p
            total += t[x3] * t[x1] * C((-u * inv[w]) % p)
    return total

def N4_brute(p, t, c):
    c1, c2, c3 = c
    tot = 0
    for x1, x2, x3, x4 in itertools.product(range(p), repeat=4):
        if (c1*x1*x2 + c2*x2*x3 + c3*x3*x4) % p == 0:
            tot += t[x1]*t[x2]*t[x3]*t[x4]
    return tot

fs = {'x3+x+1': [1, 1, 0, 1], 'x3+2x+5': [5, 2, 0, 1]}
out = []
def P(*a):
    s = ' '.join(str(x) for x in a); print(s); out.append(s)

# validation against brute force
fails = 0; cases = 0
for p in (5, 7, 11, 13):
    for name, co in fs.items():
        if not squarefree(p, co) or co[0] % p == 0: continue
        t = chi_table(p, co)
        for c in [(1,1,1),(1,2,3),(1,1,p-2),(2,1,p-3),(3,5,1)]:
            if any(ci % p == 0 for ci in c): continue
            cases += 1
            if N4_fast(p, t, c) != N4_brute(p, t, c): fails += 1
P('validation vs brute force: cases', cases, 'failures', fails)

def primes(a, b):
    return [n for n in range(a, b) if n > 2 and all(n % d for d in range(2, int(n**.5)+1))]

P('p f c sumc N4 r planeterm D=N4-(p-r)^2  D^2/p^3  N4^2/p^4  (exact fractions; decimals for display only)')
for name, co in fs.items():
    for p in primes(11, 400):
        if p in (31, 7, 101) and False: pass
        if not squarefree(p, co): continue
        t = chi_table(p, co); r = sum(1 for a in t if a == 0)
        for label, c in [('c1+c2+c3=0', (1, 1, p-2)), ('(1,2,3)', (1, 2, 3)), ('(1,1,1)', (1, 1, 1))]:
            if any(ci % p == 0 for ci in c): continue
            N = N4_fast(p, t, c)
            plane = (p - r) ** 2
            D = N - plane
            fD = Fraction(D * D, p ** 3); fN = Fraction(N * N, p ** 4)
            P(name, p, label, 'sum', sum(c) % p, 'N4', N, 'r', r, 'plane', plane, 'D', D,
              'D2/p3', f'{float(fD):.3f}', 'N2/p4', f'{float(fN):.3f}')
open('./round2/compute/RED/k4_plane_out.txt', 'w').write('\n'.join(out) + '\n')
