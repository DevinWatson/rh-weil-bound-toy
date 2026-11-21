import ctypes, itertools, sys
ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x4000)
import os
os.environ["OMP_NUM_THREADS"] = "1"
import numpy as np

# Exact integer arithmetic only. Fields F_P, P = p^n, n in {1,2}. Elements of F_{p^2}: a + b w, w^2 = g (g nonresidue mod p), index a + p b.

class GF:
    def __init__(self, p, n):
        self.p, self.n, self.P = p, n, p ** n
        P = self.P
        if n == 1:
            idx = np.arange(P)
            self.add = (idx[:, None] + idx[None, :]) % p
            self.mul = (idx[:, None] * idx[None, :]) % p
            self.neg = (-idx) % p
            self.one = 1
            self.emb = lambda a: a % p
        else:
            g = next(x for x in range(2, p) if pow(x, (p - 1) // 2, p) == p - 1)
            idx = np.arange(P)
            a, b = idx % p, idx // p
            self.add = ((a[:, None] + a[None, :]) % p) + p * ((b[:, None] + b[None, :]) % p)
            self.mul = ((a[:, None] * a[None, :] + g * b[:, None] * b[None, :]) % p) + p * ((a[:, None] * b[None, :] + b[:, None] * a[None, :]) % p)
            self.neg = ((-a) % p) + p * ((-b) % p)
            self.one = 1
            self.emb = lambda x: x % p
        # quadratic character by exponentiation (table), exact
        self.chi = np.zeros(P, dtype=np.int64)
        for x in range(1, P):
            r = 1
            for _ in range((P - 1) // 2):
                r = self.mul[r, x]
            self.chi[x] = 1 if r == 1 else -1
        assert all(self.chi[x] in (1, -1) for x in range(1, P))

    def poly(self, coeffs, xs):
        # coeffs in F_p (embedded), Horner on array xs
        res = np.zeros_like(xs)
        for c in reversed(coeffs):
            res = self.add[self.mul[res, xs], np.full_like(xs, self.emb(c))]
        return res

def squarefree_cubic_ok(coeffs, p):
    # f = coeffs[0] + coeffs[1] x + coeffs[2] x^2 + x^3 : squarefree over F_p iff disc != 0 mod p
    c0, c1, c2 = coeffs[0], coeffs[1], coeffs[2]
    a, b, c, d = 1, c2, c1, c0
    disc = b*b*c*c - 4*a*c**3 - 4*b**3*d - 27*a*a*d*d + 18*a*b*c*d
    return disc % p != 0

def Nk(F, tvals, cs):
    """sum over x in F^k of prod t(x_i) over Q_c(x)=0, DP over the path, exact integers."""
    P = F.P
    k = len(cs) + 1
    # state[x_last, s] = weighted count
    state = np.zeros((P, P), dtype=object)
    for x in range(P):
        state[x, 0] = int(tvals[x])
    for i, c in enumerate(cs):
        new = np.zeros((P, P), dtype=object)
        cc = F.emb(c)
        for xl in range(P):
            row = state[xl]
            if not any(row):
                continue
            for xn in range(P):
                inc = F.mul[F.mul[cc, xl], xn]
                tv = int(tvals[xn])
                if tv == 0:
                    continue
                # s -> s + inc
                shifted = row[F.add[np.arange(P), inc]] if False else None
                for s in range(P):
                    if row[s]:
                        new[xn, F.add[s, inc]] += row[s] * tv
        state = new
    return int(sum(state[x, 0] for x in range(P)))

def tvals_of(F, fco):
    xs = np.arange(F.P)
    fv = F.poly(fco, xs)
    return F.chi[fv] * (fv != 0)

def roots_count(F, fco):
    xs = np.arange(F.P)
    return int((F.poly(fco, xs) == 0).sum())

def Bsum(F, fco, rho):
    xs = np.arange(F.P)
    fx = F.poly(fco, xs)
    rx = F.mul[np.full_like(xs, F.emb(rho)), xs]
    frx = F.poly(fco, rx)
    prod = F.mul[fx, frx]
    return int((F.chi[prod] * (prod != 0)).sum())

out = []
def log(s):
    print(s); out.append(s)

cubics = {5: [(1, 1, 0), (2, 1, 1)], 7: [(1, 1, 0), (2, 1, 1)], 11: [(1, 1, 0)]}
# k=2 and k=3 closed forms, n = 1, 2
log("== closed forms k=2,3 (exact): N2 = 2 t0 M - 1 ; N3 = t0 M^2 + (M - t0) B(rho), rho = -c2/c1 ==")
allok = True
for p in (5, 7):
    for coeffs in cubics[p]:
        if not squarefree_cubic_ok(coeffs, p) or coeffs[0] % p == 0:
            continue
        for n in (1, 2):
            F = GF(p, n)
            P = F.P
            tv = tvals_of(F, coeffs)
            M = int(tv.sum())
            t0 = int(tv[0])
            assert t0 == (1 if pow(coeffs[0], (p - 1) // 2, p) == 1 else -1) ** n
            for c in [(1, 1), (1, 2), (1, p - 1), (2, 3)]:
                N2 = Nk(F, tv, [c[0]])
                ok2 = (N2 == 2 * t0 * M - 1)
                c1, c2 = c
                rho = (-c2 * pow(c1, -1, p)) % p
                N3 = Nk(F, tv, [c1, c2])
                B = Bsum(F, coeffs, rho)
                ok3 = (N3 == t0 * M * M + (M - t0) * B)
                extra = ""
                if rho == 1:
                    r = roots_count(F, coeffs)
                    extra = " rho=1: B == P - r : %s" % (B == P - r)
                    ok3 = ok3 and (B == P - r)
                allok &= ok2 and ok3
                log("p=%d n=%d f=%s c=%s M=%d t0=%d N2 ok=%s N3 ok=%s%s" % (p, n, coeffs, c, M, t0, ok2, ok3, extra))
log("ALL closed forms agree: %s" % allok)

# Trivial sheaf, k=4 and k=2,3, over F_p: R = q N - q^k
log("== trivial sheaf t=1 (f constant), c = all ones ==")
for p in (5, 7, 11, 13):
    F = GF(p, 1)
    tv = np.ones(p, dtype=np.int64)
    for k in (2, 3, 4, 5, 6):
        N = Nk(F, tv, [1] * (k - 1))
        M = p
        R = p * N - M ** k
        # exact test of bounds: R^2 <= ((p-1)^2) p^(k+1) (the |S_h|<=p^((k+1)/2) bound)  and R^2 <= p^(k+3)
        log("p=%d k=%d N=%d R=qN-M^k=%d  R^2<=p^(k+3): %s   M^k = p^k exceeds p^((k+3)/2): %s   R/(q^(k/2)(q-1))=%s" % (
            p, k, N, R, R * R <= p ** (k + 3), p ** k > 0 and (2 * k > k + 3), (R / (p ** (k / 2) * (p - 1)))))

# k = 3, rho = 1: wrong-parity classes predicted q^2 alpha_i and t0 q^2: R_n = u^3 + P t0^n u^2 - P(P - r) u - P t0^n (P - r)... check the formula, u = -M
log("== k=3, c1=-c2 : R_n formula with wrong-parity terms -P^2 u and -t0 P^2 (u=-M_n), n=1,2 ==")
for p in (5, 7):
    for coeffs in cubics[p]:
        if not squarefree_cubic_ok(coeffs, p) or coeffs[0] % p == 0:
            continue
        for n in (1, 2):
            F = GF(p, n); P = F.P
            tv = tvals_of(F, coeffs)
            M = int(tv.sum()); t0 = int(tv[0]); u = -M
            r = roots_count(F, coeffs)
            N3 = Nk(F, tv, [1, p - 1])
            R = P * N3 - M ** 3
            pred = u**3 + P * t0 * u**2 - P * (P - r) * u - P * t0 * (P - r)
            wrong = -P * P * u - t0 * P * P
            log("p=%d n=%d f=%s R=%d pred=%d equal=%s ; wrong-parity part=%d ; right part=%d ; R^2<=(P-1)^2 P^4: %s" % (
                p, n, coeffs, R, pred, R == pred, wrong, R - wrong, R * R <= (P - 1) ** 2 * P ** 4))

# k=4, c = (1,1,-2) vs (1,2,3) vs (1,1,1): exact N, R and the bounds
log("== k=4 cubics: R = P N - M^4 ; bound R^2 <= (P-1)^2 P^5 (Parseval, E1) and plane count D = N - (P-r)^2 ==")
for p in (5, 7, 11):
    for coeffs in cubics[p][:1]:
        for n in (1, 2) if p <= 7 else (1,):
            F = GF(p, n); P = F.P
            tv = tvals_of(F, coeffs)
            M = int(tv.sum())
            r = roots_count(F, coeffs)
            for c in [(1, 1, p - 2), (1, 1, 1), (1, 2, 3)]:
                N4 = Nk(F, tv, list(c))
                R = P * N4 - M ** 4
                D = N4 - (P - r) ** 2
                log("p=%d n=%d f=%s c=%s sum(c)%%p=%d N4=%d R=%d  R^2<=(P-1)^2P^5:%s  D=%d D^2/P^3=%.3f(display)" % (
                    p, n, coeffs, c, sum(c) % p, N4, R, R * R <= (P - 1) ** 2 * P ** 5, D, D * D / P ** 3))

open("./round3/compute/A/check_A_out.txt", "w").write("\n".join(out) + "\n")
