"""H3: non-characteristic (transversality) test of the path quadric Y={Q=0}, Q=sum c_i x_i x_{i+1}, against the root strata
F_{S,a} = {x_i = a_i for i in S}, a_i in Z (the d roots of f, chosen as random distinct nonzero RATIONALS = 'generic roots').
A critical point of Q restricted to F_{S,a} that lies on Y is a failure of transversality there.
With Q = x^T A x / 2:  critical on F  <=>  (A x)_j = 0 for j notin S;  and then Q(x) = (1/2) a . (A x)_S.
Both are LINEAR in u = x_{S^c}:   A_cc u = -A_cS a ;   a^T A_Sc u = -a^T A_SS a.
We test solvability exactly (sympy Rational, rank test).  S nonempty, every assignment sigma: S -> roots (repeats allowed).
This is an exact linear-algebra computation over Q at random rational roots (so 'consistent' = obstruction for generic roots,
barring a measure-zero accident; 'inconsistent' = no tangency at these roots).  It ignores the extra requirement x_j notin Z
for j notin S (so it can only over-report obstructions).
"""
import ctypes, itertools, random, sys
ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x4000)
from sympy import Matrix, Rational

def path_matrix(k, c):
    A = [[0] * k for _ in range(k)]
    for i in range(k - 1):
        A[i][i + 1] = c[i]; A[i + 1][i] = c[i]
    return Matrix(A)

def tangent_cases(k, roots, c, maxshow=3):
    A = path_matrix(k, c)
    d = len(roots)
    bad = []
    total = 0
    for s in range(1, k + 1):
        for S in itertools.combinations(range(k), s):
            Sc = [j for j in range(k) if j not in S]
            ASS = A.extract(list(S), list(S))
            ASc = A.extract(list(S), Sc) if Sc else None
            AcS = A.extract(Sc, list(S)) if Sc else None
            Acc = A.extract(Sc, Sc) if Sc else None
            for sig in itertools.product(range(d), repeat=s):
                total += 1
                a = Matrix([roots[i] for i in sig])
                const = (a.T * ASS * a)[0, 0]
                if Sc:
                    coef = Acc.col_join(a.T * ASc)
                    rhs = (-AcS * a).col_join(Matrix([[-const]]))
                    aug = coef.row_join(rhs)
                    ok = coef.rank() == aug.rank()
                else:
                    ok = (const == 0)
                if ok:
                    bad.append((S, sig))
    return total, bad

if __name__ == "__main__":
    k = int(sys.argv[1]); d = int(sys.argv[2]); mode = sys.argv[3]  # mode: ones | randc
    rng = random.Random(20261120 + k * 100 + d)
    roots = [Rational(rng.randint(2, 10**6), rng.randint(1, 10**3)) for _ in range(d)]
    c = [1] * (k - 1) if mode == "ones" else [Rational(rng.randint(1, 10**4), rng.randint(1, 10**2)) for _ in range(k - 1)]
    total, bad = tangent_cases(k, roots, c)
    print("k=%d d=%d coeffs=%s : %d (S,sigma) tested, %d generically consistent (tangent) cases" % (k, d, mode, total, len(bad)))
    for S, sig in bad[:6]:
        print("   S(1-based)=%s  roots index=%s" % ([i + 1 for i in S], list(sig)))
