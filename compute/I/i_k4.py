# Report I checks. Exact integer arithmetic only. One process, below normal priority.
import ctypes, itertools, random, sys
ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x4000)
import numpy as np
import sympy

def chi_table(p):
    t = np.zeros(p, dtype=np.int64)
    sq = {(x * x) % p for x in range(1, p)}
    for a in range(1, p):
        t[a] = 1 if a in sq else -1
    return t

def polyval_all(coefs, p):  # coefs low->high
    xs = np.arange(p, dtype=np.int64)
    v = np.zeros(p, dtype=np.int64)
    for c in reversed(coefs):
        v = (v * xs + c) % p
    return v

def random_f(p, d, rng):
    while True:
        co = [rng.randrange(p) for _ in range(d)] + [1]
        if co[0] == 0:
            continue
        x = sympy.symbols('x')
        P = sympy.Poly(sum(c * x**i for i, c in enumerate(co)), x, modulus=p)
        if sympy.gcd(P, P.diff(x)).degree() == 0:
            return co

def tvec(co, p):
    return chi_table(p)[polyval_all(co, p)]

def brute_N(t, p, c):
    k = len(c) + 1
    tot = 0
    for x in itertools.product(range(p), repeat=k):
        if sum(c[i] * x[i] * x[i + 1] for i in range(k - 1)) % p == 0:
            w = 1
            for xi in x:
                w *= int(t[xi])
                if w == 0:
                    break
            tot += w
    return tot

def Cfun(t, p):  # C(r) = sum_x t(x) t(r x)
    xs = np.arange(p)
    C = np.zeros(p, dtype=np.int64)
    for r in range(p):
        C[r] = int(np.dot(t, t[(r * xs) % p]))
    return C

def N3_formula(t, p, c):
    M = int(t.sum()); t0 = int(t[0])
    lam = (c[0] * pow(c[1], -1, p)) % p
    xs = np.arange(p)
    Cl = int(np.dot(t, t[(-lam * xs) % p]))
    return t0 * M * M + (M - t0) * Cl

def N4_formula(t, p, c):
    M = int(t.sum()); t0 = int(t[0])
    C = Cfun(t, p)
    tot = 0
    for r in range(p):
        tr = (-(c[2] * r + c[1]) * pow(c[0], -1, p)) % p
        tot += int(C[r]) * int(C[tr])
    return -p + t0 * t0 * M * M + tot

def main():
    out = []
    rng = random.Random(20261120)
    # (1) brute-force verification of the k=3 and k=4 formulas, random c, random f
    bad3 = bad4 = n3 = n4 = 0
    for p in (3, 5, 7):
        for d in (3, 5):
            for _ in range(6):
                co = random_f(p, d, rng)
                t = tvec(co, p)
                c3 = [rng.randrange(1, p) for _ in range(2)]
                n3 += 1
                if brute_N(t, p, c3) != N3_formula(t, p, c3):
                    bad3 += 1
                c4 = [rng.randrange(1, p) for _ in range(3)]
                n4 += 1
                if brute_N(t, p, c4) != N4_formula(t, p, c4):
                    bad4 += 1
    out.append(f"E0 formula check vs brute force: k=3 {n3} cases, {bad3} mismatches; k=4 {n4} cases, {bad4} mismatches")
    # p = 11, 13 spot checks for k=4
    for p in (11, 13):
        for _ in range(2):
            co = random_f(p, 3, rng)
            t = tvec(co, p)
            c4 = [rng.randrange(1, p) for _ in range(3)]
            ok = brute_N(t, p, c4) == N4_formula(t, p, c4)
            out.append(f"   p={p} f={co} c={c4} brute==formula: {ok}")
    # (2) sum(c)=0 versus sum(c)!=0
    out.append("")
    out.append("E1 N_4 - p^2 for c with c1+c2+c3 = 0 versus c1+c2+c3 != 0 (exact integers; t0=chi(f(0)))")
    out.append("p, class, mean of N4/p^2 over f, mean of (N4-p^2)/p^1.5 , min/max N4/p^2, number of f")
    primes = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]
    rows = []
    for p in primes:
        fs = [random_f(p, d, rng) for d in (3, 3, 3, 5, 5, 5, 3, 5)]
        for cls, ctr in (("sum=0", (1, 1, (-2) % p)), ("sum!=0", (1, 1, 1)), ("sum!=0b", (1, 2, 3 % p if 3 % p else 4))):
            vals = []
            for co in fs:
                t = tvec(co, p)
                vals.append(N4_formula(t, p, list(ctr)))
            r2 = [v / p**2 for v in vals]
            r15 = [(v - p * p) / p**1.5 for v in vals]
            line = f"{p}, {cls} c={ctr}, mean N4/p^2={np.mean(r2):.3f}, mean (N4-p^2)/p^1.5={np.mean(r15):.3f}, range N4/p^2 [{min(r2):.3f},{max(r2):.3f}], nf={len(fs)}"
            out.append(line)
            rows.append((p, cls, vals))
    # (3) p = 3 special case: c = (1,1,1) has sum 0
    out.append("")
    out.append("E2 p=3: N_4 over F_3 for c=(1,1,1) (sum=0) and c=(1,1,2) (sum=1), all squarefree f of degree 3 and 5 with f(0)!=0 (random, up to 12)")
    p = 3
    for ctr in ((1, 1, 1), (1, 1, 2), (1, 2, 2)):
        res = []
        seen = set()
        for _ in range(60):
            co = random_f(p, rng.choice((3, 5)), rng)
            key = tuple(co)
            if key in seen:
                continue
            seen.add(key)
            t = tvec(co, p)
            res.append((co, int(t.sum()), N4_formula(t, p, list(ctr))))
            if len(res) >= 12:
                break
        out.append(f" c={ctr} (sum={sum(ctr)%3}): " + "; ".join(f"N={r[2]}" for r in res))
    # (4) k=3 with lambda = -1 (c1 = -c2): g = f(x)^2 is a square
    out.append("")
    out.append("E3 k=3, c=(1,-1): g(x)=f(x)f(x)=f^2 is a square; compare N_3 with c=(1,1) and C_lambda")
    for p in (7, 11, 13, 17):
        co = random_f(p, 3, rng)
        t = tvec(co, p)
        M = int(t.sum()); t0 = int(t[0])
        n_gen = N3_formula(t, p, [1, 1])
        n_bad = N3_formula(t, p, [1, p - 1])
        xs = np.arange(p)
        Clam = int(np.dot(t, t[(xs * 1) % p]))
        out.append(f" p={p} M={M} t0={t0} N3(c=(1,1))={n_gen} N3(c=(1,-1))={n_bad} C_{{lambda=-1}}={Clam} (= q - #roots = {p - sum(1 for x in range(p) if t[x]==0)})")
    # (5) Euler characteristic by the fibration over P^1 (symbolic) against 1-4d+3d^2-4d^3
    d = sympy.symbols('d')
    D = -2*d*(2*d-1) - d*(3*d-2) - 2*(2*d-1)*(d-1) - 2*d*(d-1)*(2*d-1)
    chiR2 = 2*(2*d-1)**2 + D
    chiR3 = 2*(2*d-1)
    chi = -2 + chiR2 - chiR3 + 1
    out.append("")
    out.append("E4 Euler characteristic from the fibration: chi_c(Y,K) = " + str(sympy.expand(chi)) + " ; A's hand count 1-4d+3d^2-4d^3 ; difference = " + str(sympy.expand(chi - (1 - 4*d + 3*d**2 - 4*d**3))))
    open("./compute/I/i_k4_out.txt", "w", encoding="utf8").write("\n".join(out) + "\n")
    print("\n".join(out))

main()
