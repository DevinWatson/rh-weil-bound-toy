"""K4T exact checks (integers only). One process, below normal priority.
Output: k4t_checks_out.txt (written by the caller redirect or by this script).
Checks
 A. N_4 = -q + t0^2 M^2 + sum_r C(r) C(tau r) against brute force (p = 5, 7).
 B. sum_r C(r) = M^2 - t0*M + q  (point count of the total space T of section S-d).
 C. Euler characteristic polynomial 1-4d+3d^2-4d^3 re-derived from stalk dimensions (sympy, exact).
 D. Total-space Euler characteristic balance: Swan sum = 0 (symbolic, exact).
 E. f = x^3 - a over F_p, p = 1 mod 3: planes with rho, rho' in mu_3 give N_4 ~ +p^2.
 F. generic f with roots in F_p: c on the line c2 + c3 s + c1 s' = 0 (s, s' ratios): size of N_4/p^2.
"""
import ctypes, itertools, random, sys
ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x4000)
from fractions import Fraction

out = []
def P(*a):
    s = " ".join(str(x) for x in a)
    print(s); out.append(s)

def chi_table(p):
    t = [0]*p
    for x in range(1, p):
        t[x*x % p] = 1
    return [0] + [1 if t[x] else -1 for x in range(1, p)]   # quadratic character, chi(0)=0

def make_t(p, coeffs, chi):
    # coeffs: f = sum coeffs[i] x^i
    t = []
    for x in range(p):
        v = 0
        for c in reversed(coeffs):
            v = (v*x + c) % p
        t.append(chi[v])
    return t

def Cfun(p, t):
    # C(r) = sum_x t(x) t(r x)
    return [sum(t[x]*t[(r*x) % p] for x in range(p)) for r in range(p)]

def N4_formula(p, t, c):
    c1, c2, c3 = c
    M = sum(t)
    t0 = t[0]
    C = Cfun(p, t)
    inv = lambda a: pow(a, p-2, p)
    e = c2*inv(c3) % p
    tot = -p + t0*t0*M*M
    for r in range(p):
        tau = (-(c3*inv(c1)) * (r+e)) % p
        tot += C[r]*C[tau]
    return tot

def N4_brute(p, t, c):
    c1, c2, c3 = c
    tot = 0
    for x1 in range(p):
        for x2 in range(p):
            for x3 in range(p):
                for x4 in range(p):
                    if (c1*x1*x2 + c2*x2*x3 + c3*x3*x4) % p == 0:
                        tot += t[x1]*t[x2]*t[x3]*t[x4]
    return tot

random.seed(20261120)
# ---- A
badA = 0; nA = 0
for p in (5, 7):
    chi = chi_table(p)
    for _ in range(6):
        while True:
            co = [random.randrange(p) for _ in range(3)] + [1]
            if co[0] == 0: continue
            # squarefree check: gcd(f, f') = 1 via discriminant-free brute: no repeated root in F_p-bar for deg 3:
            # use resultant-free test by trying extension-free: f squarefree iff disc != 0
            a, b, cc = co[2], co[1], co[0]   # x^3 + a x^2 + b x + cc
            disc = (a*a*b*b - 4*b**3 - 4*a**3*cc - 27*cc*cc + 18*a*b*cc) % p
            if disc != 0: break
        t = make_t(p, co, chi)
        for c in [(1, 1, 1), (1, 2, 3), (1, 1, p-2), (2, 1, 3)]:
            c = tuple(x % p for x in c)
            if 0 in c: continue
            nA += 1
            if N4_formula(p, t, c) != N4_brute(p, t, c): badA += 1
P("A: N4 formula vs brute force: cases", nA, "mismatches", badA)

# ---- B
badB = 0; nB = 0
for p in (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103):
    chi = chi_table(p)
    for _ in range(6):
        d = random.choice((3, 5))
        while True:
            co = [random.randrange(p) for _ in range(d)] + [1]
            if co[0] == 0: continue
            # squarefree over F_p-bar: gcd(f,f')=1 using sympy-free euclid mod p
            def pmod(a, b):
                a = a[:]
                while len(a) >= len(b) and any(a):
                    if a[-1] == 0: a.pop(); continue
                    k = a[-1]*pow(b[-1], p-2, p) % p
                    sh = len(a)-len(b)
                    for i in range(len(b)):
                        a[sh+i] = (a[sh+i]-k*b[i]) % p
                    a.pop()
                while a and a[-1] == 0: a.pop()
                return a
            def gcd(a, b):
                while b:
                    a, b = b, pmod(a, b)
                return a
            fd = [(i*co[i]) % p for i in range(1, len(co))]
            g = gcd(co[:], fd[:])
            if len(g) == 1: break
        t = make_t(p, co, chi)
        M = sum(t); t0 = t[0]; C = Cfun(p, t)
        nB += 1
        if sum(C) != M*M - t0*M + p: badB += 1
P("B: sum_r C(r) = M^2 - t0 M + q : cases", nB, "failures", badB)

# ---- C, D
import sympy as sp
d, A = sp.symbols('d A')
Av = 2*d-1
deficits = (2*Av*d            # r = 0 and r = -e
            + 2*d*(d-1)*Av    # ratio points and their tau-preimages
            + 2*Av*(d-1)      # r = 1 and tau^{-1}(1)
            + d*(3*d-2))      # [0:1] fibre
chiR2 = 2*Av**2 - deficits
chiY = 1 - 2 + chiR2 - 2*Av
P("C: chi_c(Y,K) =", sp.expand(chiY), " at d=3:", sp.expand(chiY).subs(d, 3), " at d=5:", sp.expand(chiY).subs(d, 5))
mu = sp.symbols('mu')
drops = d + (d**2 - mu)                 # r=0 drop d ; sum over r != 0 of (c_r - h2_r) = d^2 - |mu|
chiR1 = (2*d-1) - drops
chiT = mu - chiR1                       # chi_c(R^2) - chi_c(R^1) - Swan sum
P("D: chi_c(T) from fibration (Swan 0) =", sp.expand(chiT), " ; chi_c(T) from product + line =", sp.expand(d*(d-1)+1),
  " ; difference (= total Swan):", sp.simplify(chiT - (d*(d-1)+1)))

# ---- E
def cube_roots_of_unity(p):
    return [x for x in range(2, p) if pow(x, 3, p) == 1]
P("E: f = x^3 - a, mu(Z) = mu_3 (p = 1 mod 3). mean N4/p^2 over a (non-cubes and cubes alike), several c")
for p in (7, 13, 19, 31, 37, 43, 61, 67, 73, 97, 103, 109, 127):
    chi = chi_table(p)
    om = cube_roots_of_unity(p)[0]
    inv = lambda a: pow(a, p-2, p)
    rows = []
    for name, c in (("X1: c2=-(1+w) [rho=w, rho'=1]", (1, (-1-om) % p, 1)),
                    ("X1: c=(1,-(w+w^2)... trivial pair is rho=rho'=1 only if c1+c2+c3=0; here rho=w,rho'=w^2", (1, (-(om+om*om)) % p, 1)),
                    ("generic c=(1,2,3)", (1, 2, 3)),
                    ("c1+c2+c3=0: (1,1,-2)", (1, 1, p-2))):
        vals = []
        for a in range(1, 9):
            co = [(-a) % p, 0, 0, 1]
            t = make_t(p, co, chi)
            vals.append(Fraction(N4_formula(p, t, tuple(x % p for x in c)), p*p))
        rows.append((name, float(sum(vals)/len(vals)), float(min(vals)), float(max(vals))))
    P(" p=%d w=%d" % (p, om))
    for r in rows:
        P("   %-95s mean %.3f  min %.3f  max %.3f" % r)

# ---- F
P("F: generic f = (x-a)(x-b)(x-e) with roots in F_p, c on lines c2 + c3 s + c1 s' = 0, s,s' in S (s,s' ratios of roots), not (1,1)")
for p in (31, 61, 101, 131):
    chi = chi_table(p)
    inv = lambda a: pow(a, p-2, p)
    random.seed(p)
    res = []
    for trial in range(6):
        rts = random.sample(range(1, p), 3)
        co = [1]
        # expand (x-a)(x-b)(x-c)
        poly = [1]
        for r0 in rts:
            new = [0]*(len(poly)+1)
            for i, cf in enumerate(poly):
                new[i+1] += cf
                new[i] -= r0*cf
            poly = [x % p for x in new]
        t = make_t(p, poly, chi)
        S = sorted(set([0] + [(z2*inv(z1)) % p for z1 in rts for z2 in rts]))
        pairs = [(s, sp_) for s in S for sp_ in S if (s, sp_) != (1, 1)]
        random.shuffle(pairs)
        got = 0
        for (s, sp_) in pairs:
            c3 = 1; c1 = random.randrange(1, p)
            c2 = (-(c3*s + c1*sp_)) % p
            if c2 == 0: continue
            if (c1 + c2 + c3) % p == 0: continue
            res.append((s, sp_, float(Fraction(N4_formula(p, t, (c1, c2, c3)), p*p))))
            got += 1
            if got >= 4: break
    vs = [r[2] for r in res]
    P(" p=%d: %d cases on exceptional lines: N4/p^2 mean %.3f, min %.3f, max %.3f" % (p, len(vs), sum(vs)/len(vs), min(vs), max(vs)))
    # compare: random c
    vr = []
    for _ in range(20):
        c = tuple(random.randrange(1, p) for _ in range(3))
        if (c[0]+c[1]+c[2]) % p == 0: continue
        rts = random.sample(range(1, p), 3)
        poly = [1]
        for r0 in rts:
            new = [0]*(len(poly)+1)
            for i, cf in enumerate(poly):
                new[i+1] += cf
                new[i] -= r0*cf
            poly = [x % p for x in new]
        t = make_t(p, poly, chi)
        vr.append(float(Fraction(N4_formula(p, t, c), p*p)))
    P("        random c, random f: N4/p^2 mean %.3f, min %.3f, max %.3f (n=%d)" % (sum(vr)/len(vr), min(vr), max(vr), len(vr)))

open("./round2/compute/K4T/k4t_checks_out.txt", "w").write("\n".join(out) + "\n")
