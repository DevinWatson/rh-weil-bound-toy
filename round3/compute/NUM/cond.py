"""Check the hypothesis of Claim B: Z disjoint from Sigma_i, i <= k-1.
Sigma_1={0}, Sigma_2=rho_2 Z, Sigma_i = rho_i (Z u Sigma_{i-2}), rho_i = -c_{i-1}/c_i (2<=i<=k-1).
c_i = gamma^cexp[i-1] in F_q (q=3^e). Z = roots of f (coeffs in F_3) in the splitting field, done in F_{3^M}."""
from math import lcm
import numpy as np
from ffl import *

def split_field(f, e):
    for M in range(e, 13, e):
        F = field(M)
        y = np.arange(F.Q, dtype=np.int64)
        fy = np.zeros(F.Q, dtype=np.int64)
        for cf in reversed(f):
            fy = F.add(F.mul(fy, y), np.full(F.Q, cf % 3))
        roots = [int(v) for v in y[fy == 0]]
        if len(roots) == len(f) - 1:
            return M, F, roots
    raise RuntimeError('no splitting field found')

def claimB_ok(f, e, cexp, verbose=False):
    k = len(cexp) + 1
    M, F, Z = split_field(f, e)
    c = [fq_element(M, e, x) for x in cexp]
    rho = {}
    for i in range(2, k):
        # rho_i = -c_{i-1}/c_i ; c list index i-1 is c_i
        num = int(F.neg(np.array([c[i - 2]]))[0])
        rho[i] = int(F.mul(np.array([num]), np.array([F.inv(c[i - 1])]))[0])
    Sig = {1: {0}}
    for i in range(2, k):
        base = set(Z) | (Sig[i - 2] if i >= 3 else set())
        Sig[i] = {int(F.mul(np.array([rho[i]]), np.array([z]))[0]) for z in base}
    bad = [i for i in range(1, k) if set(Z) & Sig[i]]
    return (len(bad) == 0), bad, M

def find_c(f, e, k, seed=0):
    import itertools, random
    rnd = random.Random(seed)
    q = 3 ** e
    for _ in range(5000):
        cexp = [rnd.randrange(q - 1) for _ in range(k - 1)]
        ok, bad, M = claimB_ok(f, e, cexp)
        if ok:
            return cexp
    return None

if __name__ == '__main__':
    import sys
    for f, name in [([2, 1], 'x-1'), ([1, 2, 0, 1], 'x^3-x+1')]:
        for k in range(2, 7):
            for e in (1, 2, 3):
                c = find_c(f, e, k)
                print(name, 'k', k, 'e', e, 'c-exps', c)
                if c is not None:
                    break
    # explicit checks
    print('x-1 k3 e1 c=(1,1):', claimB_ok([2,1],1,[0,0]))     # gamma^0 = 1
    print('x-1 k3 e1 c=(1,-1):', claimB_ok([2,1],1,[0,1]))
    print('x-1 k5 e1 all ones:', claimB_ok([2,1],1,[0,0,0,0]))
    print('x-1 k6 e1 all ones:', claimB_ok([2,1],1,[0]*5))
    print('x^3-x+1 k3 e1 (1,1):', claimB_ok([1,2,0,1],1,[0,0]))
    print('x^3-x+1 k5 e1 all ones:', claimB_ok([1,2,0,1],1,[0]*4))
