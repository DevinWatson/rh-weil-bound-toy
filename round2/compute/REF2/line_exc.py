# REF2: re-derive the "3 of 60 line exceptions" of K4C E2.2 (centred criterion 2|pE - S^2| > p^3 on the whole line c1+c2+c3 = 0).
# For each (p,f) in K4C's families, list the c on the line where the criterion fails, and the exact size of N_4/p^2 there.
from lib import *
from x4_test import poly_from_roots, ratio_set, mu_set
from fractions import Fraction

def is_prime(n):
    return n > 1 and all(n % q for q in range(2, int(n ** 0.5) + 1))

def squarefree_mod(p, co):
    # gcd(f, f') == 1 over F_p via brute: check no repeated root in F_pbar is hard; use sympy
    import sympy
    x = sympy.symbols('x')
    f = sympy.Poly(co, x, modulus=p)
    return sympy.gcd(f, f.diff(x)).degree() == 0

def irreducible_cubic(p):
    for a in range(p):
        for b in range(p):
            for c in range(1, p):
                co = [1, a, b, c]
                if all(poly_vals(p, co)[x] != 0 for x in range(p)):
                    return co

def quintic(p):
    for c in range(1, p):
        co = [1, 0, 0, 0, 1, c]
        if squarefree_mod(p, co) and poly_vals(p, co)[0] != 0:
            return co

out = open("line_exc_out.txt", "w")
tot = 0; failed = 0
for p in [q for q in range(37, 102) if is_prime(q)]:
    fams = {"f1": poly_from_roots(p, [1, 2, 4]), "f2": poly_from_roots(p, [1, 3, 9]), "cub": irreducible_cubic(p), "quint": quintic(p)}
    for name, co in fams.items():
        if not squarefree_mod(p, co) or poly_vals(p, co)[0] == 0:
            continue
        t = t_from_poly(p, co); C = Carray(p, t)
        S = int(C.sum())
        rho = int((poly_vals(p, co) == 0).sum())
        tot += 1
        nbad = 0; worst = None
        for c3 in range(1, p):
            c2 = (-1 - c3) % p
            if c2 == 0:
                continue
            c = (1, c2, c3)
            # E = sum C(r) C(tau r)
            r = np.arange(p, dtype=np.int64)
            tau = (-c3 * r - c2) % p
            E = int((C * C[tau]).sum())
            Ec2 = 2 * abs(p * E - S * S)   # 2|p E - S^2| compared with p^3
            if not (Ec2 > p ** 3):
                nbad += 1
                ratio = Fraction(E, p * p)
                if worst is None or abs(E) < abs(worst[1]):
                    worst = (c, E, rho, ratio)
        if nbad:
            failed += 1
            print("p=%d %s rho=%d: %d of the line fail the centred criterion; smallest |E| example c=%s E=%d (E/p^2=%.3f)" % (p, name, rho, nbad, worst[0], worst[1], float(worst[3])), file=out)
            # test the extra structure: is c on another exceptional pattern? list all failing c
            fl = []
            for c3 in range(1, p):
                c2 = (-1 - c3) % p
                if c2 == 0: continue
                tau = (-c3 * r - c2) % p
                E = int((C * C[tau]).sum())
                if not (2 * abs(p * E - S * S) > p ** 3):
                    fl.append((c2, c3, E))
            print("   failing (c2,c3,E): %s" % fl[:10], file=out)
print("pairs (p,f) tested: %d ; with at least one failing point on the line: %d" % (tot, failed), file=out)
out.close()
