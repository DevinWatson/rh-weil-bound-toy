import sys, os, csv
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ctypes
try:
    ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x4000)
except Exception:
    pass
import sympy

HERE = os.path.dirname(os.path.abspath(__file__))
rows = list(csv.DictReader(open(os.path.join(HERE, "N_table.tsv")), delimiter="\t"))
AB = {"x^3+x+1": (1, 1), "x^3-x": (-1, 0)}  # f = x^3 + a x + b
out = open(os.path.join(HERE, "u4_out.txt"), "w")
def P(*a):
    s = " ".join(str(x) for x in a)
    print(s); out.write(s + "\n"); out.flush()

def chi_p(a, p):
    a %= p
    return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)

def power_sums(s1, p, nmax):
    s = [2, s1]
    for n in range(2, nmax + 1):
        s.append(s1 * s[n - 1] - p * s[n - 2])
    return s

fails = 0
for p in (3, 5, 7):
    for name in AB:
        a, b = AB[name]
        R = [r for r in rows if int(r["p"]) == p and r["f"] == name]
        nmax = max(int(r["n"]) for r in R)
        # M-eigenvalue power sums: s_n(alpha) = -M_n ; eps = chi_p(f(0)) = chi_p(b)
        eps = chi_p(b, p)
        lam = chi_p(-1, p)
        G = [(b * b) % p, (-a * a) % p, (-2 * a) % p, (-1) % p]       # G(u) = b^2 - u (u+a)^2
        uG = [0] + G
        A1 = sum(chi_p(sum(G[i] * pow(u, i, p) for i in range(4)), p) for u in range(p))
        B1 = sum(chi_p(sum(uG[i] * pow(u, i, p) for i in range(5)), p) for u in range(p))
        u_ = sympy.symbols("u")
        PG = sympy.Poly(sum(G[i] * u_ ** i for i in range(4)), u_, modulus=p)
        PuG = sympy.Poly(sum(uG[i] * u_ ** i for i in range(5)), u_, modulus=p)
        sqf1 = sympy.gcd(PG, PG.diff(u_)).degree() == 0
        sqf2 = sympy.gcd(PuG, PuG.diff(u_)).degree() == 0
        s1E1 = -A1
        s1E2 = -B1 - lam
        sE1 = power_sums(s1E1, p, nmax)
        sE2 = power_sums(s1E2, p, nmax)
        P("=== p=%d f=%s  eps=chi_p(f(0))=%d lambda=chi_p(-1)=%d  G squarefree:%s uG squarefree:%s  s1(E1)=%d s1(E2)=%d"
          % (p, name, eps, lam, sqf1, sqf2, s1E1, s1E2))
        for r in R:
            n = int(r["n"]); q = int(r["q"]); M = int(r["M"]); t0 = int(r["t0"]); C = int(r["C"])
            N2 = int(r["N2"]); N3 = int(r["N3"])
            en = eps ** n if eps != 0 else 0
            c1 = (t0 == en)
            c2 = (N2 == 2 * t0 * M - t0 * t0)
            c3 = (N3 == t0 * M * M + (M - t0) * C)
            # C through the two genus-1 curves (valid when both polys squarefree)
            Cpred = -sE1[n] - sE2[n] - lam ** n
            c4 = (C == Cpred) if (sqf1 and sqf2) else None
            if name == "x^3-x":
                c5 = (C == lam ** n * (q - 3))
            else:
                c5 = None
            sal = -M
            S_plus = -C  # = s(E1)+s(E2)+lam^n in the generic case
            # spectral form of N3, generic case: all coefficients are positive integers
            N3spec = en * sal * sal + sal * S_plus + en * S_plus
            c6 = (N3 == N3spec) if (sqf1 and sqf2 and eps != 0) else None
            N2spec = 2 * en * sal + en * en
            c7 = (-N2 == N2spec)
            if not (c1 and c2 and c3) or c4 is False or c5 is False or c6 is False or not c7:
                fails += 1
            P("n=%d q=%d  t0=eps^n:%s  N2=2t0M-t0^2:%s  N3=t0M^2+(M-t0)C:%s  C=-s(E1)-s(E2)-lam^n:%s  C=lam^n(q-3):%s  N3 spectral:%s  -N2=2eps^n s+eps^2n:%s   [M=%d C=%d N2=%d N3=%d]"
              % (n, q, c1, c2, c3, c4, c5, c6, c7, M, C, N2, N3))
P("TOTAL failures:", fails)
