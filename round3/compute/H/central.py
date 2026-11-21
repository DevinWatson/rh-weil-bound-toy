"""H: exact test of  q N = M^k + R,  |R| <= (p-1) p^((k+1)/2)  for y^2=f(x), f cubic, over F_p, k=2,4,6.
R computed as p*N - M^k with exact Python ints (N from core.N_zero, M = sum t).  Also checks the k=2 closed form
p*N = 2 p t0 M - p and the Lean bound R^2 <= (p-1)^2 p^(k+1) exactly (integers).  Genericity (G_k) is tested over F_p only
(ratios of roots that lie in F_p), via gcd(f(x), f(r x)).
"""
import sys, ctypes, random
sys.path.insert(0, './compute/B')
import numpy as np
from core import tvec, N_zero
import sympy
from sympy import Poly, GF, symbols
x = symbols('x')
POLY = {"x^3+x+1": [1,1,0,1], "x^3+2x+5": [5,2,0,1], "x^3-x+2":[2,-1,0,1]}
def ratios_in_Fp(coeffs, p):
    f = Poly(sum(c*x**i for i,c in enumerate(coeffs)), x, modulus=p)
    S = set([1])
    for r in range(2, p):
        g = Poly(f.as_expr().subs(x, r*x), x, modulus=p)
        if sympy.gcd(f, g).degree() > 0: S.add(r)
    return S
def generic_c(k, p, R, rng):
    for _ in range(100000):
        c = [rng.randrange(1,p) for _ in range(k-1)]
        rho = {i: (-c[i-2]*pow(c[i-1],-1,p))%p for i in range(2,k)}  # rho_i = -c_{i-1}/c_i
        bad = False
        for i in range(2, k):
            # products rho_i rho_{i-2} ... rho_{i-2m}, m<= floor(i/2)-1 ; rho_1 not defined (Sigma_1={0})
            prod = 1; j = i
            while j >= 2:
                prod = prod*rho[j] % p
                if prod in R: bad = True
                j -= 2
        if not bad: return c
    return None
rng = random.Random(1)
rows = []
for name, co in POLY.items():
    for p in [7, 11, 13, 17, 19]:
        if any(sympy.discriminant(Poly(sum(c*x**i for i,c in enumerate(co)),x),x) % p == 0 for _ in [0]): continue
        if co[0] % p == 0: continue
        t = tvec(co, p); M = int(t.sum()); t0 = int(t[0])
        Rr = ratios_in_Fp(co, p)
        for k in [2, 4, 6]:
            for mode in ['generic', 'ones']:
                if mode == 'ones': c = [1]*(k-1)
                else:
                    c = generic_c(k, p, Rr, rng)
                    if c is None: continue
                N = N_zero(t, c, k, p)
                R = p*N - M**k
                bound = (p-1)*p**((k+1)//2) * (1 if (k+1)%2==0 else 0)
                # exact integer test of R^2 <= (p-1)^2 p^(k+1)
                ok = R*R <= (p-1)**2 * p**(k+1)
                extra = ''
                if k == 2:
                    extra = ' k2form=%s' % (p*N == 2*p*t0*M - p)
                rows.append((name, p, k, mode, c, M, N, R, ok))
                print(name, 'p', p, 'k', k, mode, 'c', c, 'M', M, 'N', N, 'R', R, 'R^2<=(p-1)^2p^(k+1):', ok, extra, 'ratio R/((p-1)p^((k+1)/2)) %.4f' % (R/((p-1)*p**((k+1)/2))), flush=True)
print('violations:', sum(1 for r in rows if not r[-1]), 'of', len(rows))
