"""Library for A3: primitive polynomials, running zfour3.exe, exact Newton identities in Z[omega], predictions from S5.
Everything exact (integers / Fractions). No floating point."""
import subprocess, os, json, random, itertools, sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
EXE = os.path.join(HERE, "zfour3.exe")

# ---------------- primitive polynomials over F_p (exact) ----------------
def factorize(m):
    f = {}
    d = 2
    while d * d <= m:
        while m % d == 0:
            f[d] = f.get(d, 0) + 1
            m //= d
        d += 1
    if m > 1:
        f[m] = f.get(m, 0) + 1
    return f

def polymulmod(a, b, mod, p):
    # a,b lists length N (low->high); mod = monic poly coefficients m_0..m_{N-1} (X^N = -sum m_i X^i)
    N = len(mod)
    res = [0] * (2 * N - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    res[i + j] = (res[i + j] + x * y) % p
    for k in range(2 * N - 2, N - 1, -1):
        c = res[k]
        if c:
            res[k] = 0
            for i in range(N):
                res[k - N + i] = (res[k - N + i] - c * mod[i]) % p
    return res[:N]

def polypowmod(e, mod, p):
    N = len(mod)
    result = [1] + [0] * (N - 1)
    base = [0, 1] + [0] * (N - 2) if N > 1 else [(-mod[0]) % p]
    while e:
        if e & 1:
            result = polymulmod(result, base, mod, p)
        base = polymulmod(base, base, mod, p)
        e >>= 1
    return result

def find_primitive(p, N, seed=1):
    Qm1 = p ** N - 1
    primes = list(factorize(Qm1).keys())
    rnd = random.Random(seed * 1000 + N * 10 + p)
    one = [1] + [0] * (N - 1)
    while True:
        mod = [rnd.randrange(p) for _ in range(N)]
        if mod[0] == 0:
            continue
        if polypowmod(Qm1, mod, p) != one:
            continue
        if all(polypowmod(Qm1 // r, mod, p) != one for r in primes):
            return mod

_polycache = os.path.join(HERE, "prim_polys.json")
def primitive_poly(p, N):
    try:
        cache = json.load(open(_polycache))
    except Exception:
        cache = {}
    key = f"{p},{N}"
    if key not in cache:
        cache[key] = find_primitive(p, N)
        json.dump(cache, open(_polycache, "w"))
    return cache[key]

# ---------------- Z[omega] exact arithmetic ----------------
class ZW:
    __slots__ = ("a", "b")
    def __init__(self, a=0, b=0):
        self.a = Fraction(a); self.b = Fraction(b)
    def __add__(s, o): return ZW(s.a + o.a, s.b + o.b)
    def __sub__(s, o): return ZW(s.a - o.a, s.b - o.b)
    def __neg__(s): return ZW(-s.a, -s.b)
    def __mul__(s, o):
        if not isinstance(o, ZW):
            return ZW(s.a * o, s.b * o)
        return ZW(s.a * o.a - s.b * o.b, s.a * o.b + s.b * o.a - s.b * o.b)
    def divint(s, k): return ZW(s.a / k, s.b / k)
    def iszero(s): return s.a == 0 and s.b == 0
    def isint(s): return s.a.denominator == 1 and s.b.denominator == 1
    def __repr__(s): return f"({s.a}+{s.b}w)"

def newton_series(ps, maxj):
    """ps[m-1] = p_m (power sums) as ZW. Returns coefficients c_0..c_maxj of prod(1 - gamma T) (exact, rational)."""
    e = [ZW(1, 0)]
    for j in range(1, maxj + 1):
        acc = ZW(0, 0)
        for m in range(1, j + 1):
            term = e[j - m] * ps[m - 1]
            acc = acc + term if (m % 2 == 1) else acc - term
        e.append(acc.divint(j))
    return [e[j] * (1 if j % 2 == 0 else -1) for j in range(maxj + 1)]

def degree_report(ps):
    """Return dict: degree = largest j<=N with coefficient nonzero provided all coefficients beyond are zero up to N;
    plus flags: integral (all coefficients in Z[omega])."""
    N = len(ps)
    c = newton_series(ps, N)
    nz = [j for j in range(N + 1) if not c[j].iszero()]
    deg = max(nz)
    integral = all(x.isint() for x in c)
    return {"N": N, "last_nonzero": deg, "integral": integral, "coeffs": c}

# ---------------- running the C engine ----------------
def run_engine(p, u, n, cfg_lines, tag, xi_poly=None):
    N = u * n
    poly = primitive_poly(p, N)
    cfg_path = os.path.join(HERE, f"cfg_{tag}.txt")
    open(cfg_path, "w").write("\n".join(cfg_lines) + "\n")
    args = [EXE, str(p), str(u), str(n), "".join(map(str, poly)), cfg_path]
    if xi_poly: args.append(xi_poly)
    out = subprocess.run(args, capture_output=True, text=True)
    if out.returncode != 0:
        raise RuntimeError(f"engine failed p={p} n={n}: {out.stderr[-500:]}")
    res = {}
    for line in out.stdout.splitlines():
        t = line.split()
        if t[0] == "R":
            res[(t[1], int(t[2]), int(t[3]), int(t[4]))] = (int(t[5]), int(t[6]))
    return res

# ---------------- F_q element codes and predictions ----------------
# element code: None = 0, else exponent a (mod q-1) of xi.
def make_field(p, u):
    q = p ** u
    def mul(x, y):
        if x is None or y is None: return None
        return (x + y) % (q - 1)
    def inv(x): return (-x) % (q - 1)
    minus1 = ((q - 1) // 2) % (q - 1) if p != 2 else 0
    return q, mul, inv, minus1

def predict(p, u, Z, h, cs, K):
    """Predict, from invariant (I_i) of S5 (draft sections S3, S5 as re-derived in the report), for i=1..K:
    ranks r_i, singular dictionaries Sigma_i (w -> drop of the stalk of Q_i at w), generic rank r_{i+1} of Q_i, and flags."""
    q, mul, inv, minus1 = make_field(p, u)
    rho = {}
    for i in range(1, K + 1):
        if i == 1: rho[i] = 0
        else: rho[i] = mul(minus1, mul(cs[i - 2], inv(cs[i - 1])))   # -c_{i-1}/c_i, cs 0-based
    S = {0: {None: 1}}                      # S_0
    Sig = {}
    r = {}
    flags = {}
    for i in range(1, K + 1):
        # Sigma_i = rho_i * S_{i-1}
        sg = {}
        for s, ev in S[i - 1].items():
            w = None if s is None else mul(s, rho[i])
            if i == 1: w = None
            sg[w] = sg.get(w, 0) + ev
        Sig[i] = sg
        # S_i = Z (e = r_i) plus Sigma_{i-1} (e = drop)
        r[i] = sum(S[i - 1].values())
        Si = {}
        if i >= 2:
            for w, d in Sig[i - 1].items(): Si[w] = Si.get(w, 0) + d
        conflict = False
        for z in Z:
            if z in Si and i >= 2: conflict = True
            Si[z] = Si.get(z, 0) + r[i]
        S[i] = Si
        flags[i] = conflict
    r[K + 1] = sum(S[K].values())
    return {"r": r, "Sigma": Sig, "S": S, "conflict": flags}

def hyp_G(pred, K):
    """(G_i') : Z disjoint from Sigma_j for 1<=j<=i-1, i.e. the structure of P_i is as in S5."""
    out = {}
    ok = True
    for i in range(1, K + 2):
        out[i] = ok
        if i <= K and pred["conflict"].get(i + 1, False): pass
    # conflict at stage i+1 means Z meets Sigma_i
    ok = True
    res = {}
    for i in range(1, K + 2):
        res[i] = ok
        if i <= K and pred["conflict"].get(i + 1, False):
            ok = False
    return res

# ---------------- general prediction with roots in an extension field ----------------
def predict_gen(Z, scal, K):
    """Z: iterable of hashable nonzero elements; scal[i](s): multiplication by rho_i (i>=2); the zero element is the int 0."""
    S = {0: {0: 1}}
    Sig = {}; r = {}; conflict = {}
    for i in range(1, K + 1):
        sg = {}
        for s, ev in S[i - 1].items():
            w = 0 if i == 1 else scal[i](s)
            sg[w] = sg.get(w, 0) + ev
        Sig[i] = sg
        r[i] = sum(S[i - 1].values())
        Si = {}
        if i >= 2:
            for w, d in Sig[i - 1].items(): Si[w] = Si.get(w, 0) + d
        c = False
        for z in Z:
            if z in Si and i >= 2: c = True
            Si[z] = Si.get(z, 0) + r[i]
        S[i] = Si; conflict[i] = c
    r[K + 1] = sum(S[K].values())
    return {"r": r, "Sigma": Sig, "S": S, "conflict": conflict}

class BigField:
    """F_{p^N} with log tables, own code (python). Elements = ints (index = base-p digits)."""
    def __init__(self, p, N):
        self.p, self.N, self.Q = p, N, p ** N
        poly = primitive_poly(p, N)
        self.poly = poly
        cur = [1] + [0] * (N - 1); X = [0, 1] + [0] * (N - 2) if N > 1 else [(-poly[0]) % p]
        self.exp = []; self.log = {}
        for k in range(self.Q - 1):
            idx = sum(d * p ** i for i, d in enumerate(cur))
            self.exp.append(idx); self.log[idx] = k
            cur = polymulmod(cur, X, poly, p)
    def add(self, a, b):
        p = self.p; r = 0; m = 1
        for _ in range(self.N):
            r += ((a % p + b % p) % p) * m; a //= p; b //= p; m *= p
        return r
    def mul(self, a, b):
        if a == 0 or b == 0: return 0
        return self.exp[(self.log[a] + self.log[b]) % (self.Q - 1)]
    def inv(self, a): return self.exp[(-self.log[a]) % (self.Q - 1)]
    def neg(self, a):
        p = self.p; r = 0; m = 1
        for _ in range(self.N):
            r += ((-(a % p)) % p) * m; a //= p; m *= p
        return r
    def codeq(self, q, c):
        return 0 if c is None or c < 0 else self.exp[(c * ((self.Q - 1) // (q - 1))) % (self.Q - 1)]
    def polyval(self, coefs, y):
        acc = 0
        for a in reversed(coefs): acc = self.add(self.mul(acc, y), a)
        return acc

def predict_poly(p, u, m, fcodes, h, cs, K):
    """f given by coefficient codes (low->high, -1 = 0) over F_q; roots found in F_{q^m}. Returns prediction (rho_i = -c_{i-1}/c_i)."""
    q = p ** u
    F = BigField(p, u * m)
    coefs = [F.codeq(q, c) for c in fcodes]
    Z = [y for y in range(1, F.Q) if F.polyval(coefs, y) == 0]
    deg = len(fcodes) - 1
    assert len(Z) == deg, (len(Z), deg)
    minus1 = F.neg(1)
    scal = {}
    for i in range(2, K + 1):
        rho = F.mul(minus1, F.mul(F.codeq(q, cs[i - 2]), F.inv(F.codeq(q, cs[i - 1]))))
        scal[i] = (lambda r: (lambda s: F.mul(s, r)))(rho)
    pr = predict_gen(Z, scal, K)
    # translate W keys (F_q codes) to field elements for lookup
    pr["F"] = F; pr["q"] = q
    return pr
