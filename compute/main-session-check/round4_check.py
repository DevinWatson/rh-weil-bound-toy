"""Round four, main-session check: stalk dimensions of the iterated Fourier transforms, recomputed.

Independent of round4/compute/A3 (own field arithmetic, own transforms, own prediction code).
Character sums over finite fields only. Nothing here says anything about the Riemann Hypothesis.

What is computed.  F = F_(q^n), t(x) = chi_n(f(x)), g_1 = t,
    tau_i(y)  = sum over x in F of g_i(x) * psi_n(h c_i x y),      g_(i+1)(y) = t(y) * tau_i(y).
For y in F_q the numbers p_n = (-1)^i tau_i over F_(q^n), n = 1..N, are (if the stalk of the i-th
transform Q_i at y sits in one degree) the power sums of the Frobenius eigenvalues on that stalk.
Newton's identities turn p_1..p_N into e_1..e_N exactly; the stalk dimension D is read off as the
last nonzero e_m, and is DETERMINED only when D < N (so at least e_N = 0 is observed).

What it is compared with.  The invariant of PROOF_V2 section S5 (J1 to J4, Lemmas A and B):
    rank Q_i = sum over s in S_i of m_i(s);  Q_i drops at rho_i * s (s in S_(i-1)) by m_(i-1)(s);
    S_(i+1) = Z union Sigma_i, m_(i+1) = rank Q_i on Z and the drop on Sigma_i;  Sigma_1 = {0}, drop 1.

Arithmetic.  Exact.  Values live in Z[w], w a primitive cube root of unity, stored as integer pairs
(a, b) = a + b w.  The transforms run in int64 with wraparound, which is exact modulo 2^64; the
recorded values tau_i(y) are recovered exactly because of the elementary bound
|tau_i(y)| <= |F|^((i+1)/2) (step S1 of the proof, checked in Lean), which is tested as an integer
inequality before a value is used.  Newton's identities use Fractions.  No floating point.

This is a net (Euler characteristic) count.  It cannot see cancellation between two cohomology degrees.

  python round4_check.py <outfile>
"""
import ctypes
import os
import sys
from fractions import Fraction

os.environ.setdefault("OMP_NUM_THREADS", "2")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "2")
os.environ.setdefault("MKL_NUM_THREADS", "2")
import numpy as np  # noqa: E402

try:  # below-normal priority on Windows
    ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x4000)
except Exception:
    pass

OUT = []
QUICK = int(os.environ.get("R4_QUICK", "0"))


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True)
    OUT.append(s)


# ----------------------------------------------------------------------------- Z[w] exact
def zmul(u, v):
    a, b = u
    c, d = v
    return (a * c - b * d, a * d + b * c - b * d)


def zadd(u, v):
    return (u[0] + v[0], u[1] + v[1])


def zscal(u, r):
    return (u[0] * r, u[1] * r)


W_POW = [(1, 0), (0, 1), (-1, -1)]  # 1, w, w^2


def newton(p):
    """p[1..N] power sums in Z[w] (index 0 unused) -> e[0..N] as Fraction pairs."""
    N = len(p) - 1
    e = [(Fraction(1), Fraction(0))]
    for m in range(1, N + 1):
        acc = (Fraction(0), Fraction(0))
        for i in range(1, m + 1):
            term = zmul(e[m - i], (Fraction(p[i][0]), Fraction(p[i][1])))
            acc = zadd(acc, zscal(term, 1 if i % 2 == 1 else -1))
        e.append((acc[0] / m, acc[1] / m))
    return e


def bound_ok(F, i):
    """(2/sqrt 3) |F|^((i+1)/2) < 2^62, as integers: 4 |F|^(i+1) < 3 * 2^124."""
    return 4 * F ** (i + 1) < 3 * (1 << 124)


# ----------------------------------------------------------------------------- F_3[x]/m, pure python
def p3_mulmod(a, b, mod):
    n = len(mod)
    z = [0] * (2 * n - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                z[i + j] += ai * bj
    for deg in range(2 * n - 2, n - 1, -1):
        c = z[deg] % 3
        if c:
            for l in range(n):
                z[deg - n + l] -= c * mod[l]
        z[deg] = 0
    return [v % 3 for v in z[:n]]


def p3_polydivmod(a, b):
    a = [v % 3 for v in a]
    while b and b[-1] % 3 == 0:
        b = b[:-1]
    inv = 1 if b[-1] % 3 == 1 else 2
    while len(a) >= len(b) and any(a):
        while a and a[-1] == 0:
            a = a[:-1]
        if len(a) < len(b):
            break
        c = (a[-1] * inv) % 3
        sh = len(a) - len(b)
        for l in range(len(b)):
            a[sh + l] = (a[sh + l] - c * b[l]) % 3
    while a and a[-1] == 0:
        a = a[:-1]
    return a


def p3_gcd_is_one(a, b):
    a = [v % 3 for v in a]
    b = [v % 3 for v in b]
    while a and a[-1] == 0:
        a = a[:-1]
    while b and b[-1] == 0:
        b = b[:-1]
    while b:
        a, b = b, p3_polydivmod(a, b)
    return len(a) == 1


def p3_irreducible(mod):
    """mod = low coefficients of a monic polynomial of degree n. Test: coprime to x^(3^j) - x for j <= n/2."""
    n = len(mod)
    if n == 1:
        return True
    full = list(mod) + [1]
    x = [0, 1] + [0] * (n - 2) if n >= 2 else None
    cur = x[:]
    for j in range(1, n // 2 + 1):
        cur = p3_mulmod(cur, p3_mulmod(cur, cur, mod), mod)
        diff = [(cur[l] - x[l]) % 3 for l in range(n)]
        if not any(diff) or not p3_gcd_is_one(full, diff):
            return False
    return True


def p3_find_modulus(n):
    if n == 1:
        return [0]  # F_3 = F_3[x]/(x)
    for code in range(3 ** n):
        mod = [(code // 3 ** l) % 3 for l in range(n)]
        if mod[0] and p3_irreducible(mod):
            return mod
    raise RuntimeError("no irreducible polynomial")


def p3_trace(a, mod):
    n = len(mod)
    s = [0] * n
    cur = a[:]
    for _ in range(n):
        s = [(s[l] + cur[l]) % 3 for l in range(n)]
        cur = p3_mulmod(cur, p3_mulmod(cur, cur, mod), mod)
    assert not any(s[1:]), "trace not in F_3"
    return s[0]


# ----------------------------------------------------------------------------- F_3 side, vectorised
def p3_vecmul(X, Y, mod):
    N, n = X.shape
    Z = np.zeros((N, 2 * n - 1), dtype=np.int16)
    for i in range(n):
        xi = X[:, i].astype(np.int16)
        if not xi.any():
            continue
        for j in range(n):
            Z[:, i + j] += xi * Y[:, j]
    Z %= 3
    for deg in range(2 * n - 2, n - 1, -1):
        c = Z[:, deg].copy()
        for l in range(n):
            if mod[l]:
                Z[:, deg - n + l] -= c * mod[l]
        Z[:, deg - n:deg] %= 3
    return Z[:, :n].astype(np.int8)


def p3_index(D):
    n = D.shape[1]
    wts = np.array([3 ** j for j in range(n)], dtype=np.int64)
    return D.astype(np.int64) @ wts


def fft3(A, B, n):
    """In place: G(xi) = sum_x g(x) w^(xi . x) over F_3^n, values a + b w."""
    for j in range(n):
        a = A.reshape(-1, 3, 3 ** j)
        b = B.reshape(-1, 3, 3 ** j)
        a0, a1, a2 = a[:, 0, :].copy(), a[:, 1, :].copy(), a[:, 2, :].copy()
        b0, b1, b2 = b[:, 0, :].copy(), b[:, 1, :].copy(), b[:, 2, :].copy()
        # w*(a+bw) = -b + (a-b) w ;  w^2*(a+bw) = (b-a) + (-a) w
        a[:, 0, :] = a0 + a1 + a2
        b[:, 0, :] = b0 + b1 + b2
        a[:, 1, :] = a0 - b1 + (b2 - a2)
        b[:, 1, :] = b0 + (a1 - b1) - a2
        a[:, 2, :] = a0 + (b1 - a1) - b2
        b[:, 2, :] = b0 - a1 + (a2 - b2)


def p3_setup(n, fcoef):
    """fcoef: coefficients of f in F_3, low to high."""
    mod = p3_find_modulus(n)
    N = 3 ** n
    D = np.empty((N, n), dtype=np.int8)
    ar = np.arange(N, dtype=np.int64)
    for j in range(n):
        D[:, j] = (ar // 3 ** j) % 3
    # quadratic character from the set of squares
    sq = p3_index(p3_vecmul(D, D, mod))
    chi = np.full(N, -1, dtype=np.int64)
    chi[sq] = 1
    chi[0] = 0
    assert int((chi == 1).sum()) == (N - 1) // 2, "squares count"
    # f(y) by Horner
    acc = np.zeros((N, n), dtype=np.int8)
    acc[:, 0] = fcoef[-1] % 3
    for cf in reversed(fcoef[:-1]):
        acc = p3_vecmul(acc, D, mod)
        acc[:, 0] = (acc[:, 0] + cf) % 3
    t = chi[p3_index(acc)]
    # trace form: xi(y)_j = sum_l y_l Tr(theta^(j+l))
    theta_pows = []
    cur = [1] + [0] * (n - 1)
    xel = ([0, 1] + [0] * (n - 2)) if n >= 2 else [(-mod[0]) % 3]
    for m in range(2 * n - 1):
        theta_pows.append(p3_trace(cur, mod))
        cur = p3_mulmod(cur, xel, mod)
    Amat = np.array([[theta_pows[j + l] for l in range(n)] for j in range(n)], dtype=np.int64)
    Xi = (D.astype(np.int64) @ Amat.T) % 3
    wts = np.array([3 ** j for j in range(n)], dtype=np.int64)
    perm = {1: Xi @ wts, 2: ((2 * Xi) % 3) @ wts}
    return dict(mod=mod, N=N, t=t, perm=perm, D=D)


_P3 = {}


def p3_run(n, fcoef, h, c, K):
    """Returns tau[i][y] for i = 1..K, y in F_3, as exact pairs, or None where the bound test fails."""
    key = (n, tuple(fcoef))
    if key not in _P3:
        _P3.clear()
        _P3[key] = p3_setup(n, fcoef)
    S = _P3[key]
    N, t = S["N"], S["t"]
    A = t.copy()
    B = np.zeros(N, dtype=np.int64)
    res = {}
    for i in range(1, K + 1):
        b = (h * c[i - 1]) % 3
        fft3(A, B, n)
        Ah, Bh = A[S["perm"][b]], B[S["perm"][b]]
        res[i] = {str(y): (int(Ah[y]), int(Bh[y])) for y in range(3)} if bound_ok(N, i) else None
        A, B = t * Ah, t * Bh
    return res, S


def p3_brute(n, fcoef, h, c, K):
    """Direct sums in pure python with separate field code (small n only)."""
    mod = p3_find_modulus(n)
    N = 3 ** n
    els = [[(v // 3 ** j) % 3 for j in range(n)] for v in range(N)]
    idx = lambda a: sum(a[j] * 3 ** j for j in range(n))
    squares = {idx(p3_mulmod(a, a, mod)) for a in els if any(a)}

    def chi(a):
        if not any(a):
            return 0
        return 1 if idx(a) in squares else -1

    def feval(a):
        acc = [fcoef[-1] % 3] + [0] * (n - 1)
        for cf in reversed(fcoef[:-1]):
            acc = p3_mulmod(acc, a, mod)
            acc[0] = (acc[0] + cf) % 3
        return acc

    t = [chi(feval(a)) for a in els]
    g = [(v, 0) for v in t]
    res = {}
    for i in range(1, K + 1):
        b = (h * c[i - 1]) % 3
        tau = []
        for y in els:
            acc = (0, 0)
            for xi, x in enumerate(els):
                e = (b * p3_trace(p3_mulmod(x, y, mod), mod)) % 3
                acc = zadd(acc, zmul(g[xi], W_POW[e]))
            tau.append(acc)
        res[i] = {y: tau[y] for y in range(3)}
        g = [zscal(tau[v], t[v]) for v in range(N)]
    return res


# ----------------------------------------------------------------------------- F_2[x]/m, pure python
def p2_mulmod(a, b, mod, m):
    z = 0
    while b:
        if b & 1:
            z ^= a
        b >>= 1
        a <<= 1
    for deg in range(2 * m - 2, m - 1, -1):
        if (z >> deg) & 1:
            z ^= mod << (deg - m)
    return z


def p2_polymod(a, b):
    db = b.bit_length()
    while a.bit_length() >= db:
        a ^= b << (a.bit_length() - db)
    return a


def p2_gcd(a, b):
    while b:
        a, b = b, p2_polymod(a, b)
    return a


def p2_irreducible(mod, m):
    cur = 2
    for j in range(1, m // 2 + 1):
        cur = p2_mulmod(cur, cur, mod, m)
        if p2_gcd(mod, cur ^ 2) != 1:
            return False
    return True


def p2_find_modulus(m):
    for low in range(1, 1 << m, 2):
        mod = (1 << m) | low
        if p2_irreducible(mod, m):
            return mod
    raise RuntimeError("no irreducible polynomial")


def p2_pow(a, e, mod, m):
    r = 1
    while e:
        if e & 1:
            r = p2_mulmod(r, a, mod, m)
        a = p2_mulmod(a, a, mod, m)
        e >>= 1
    return r


def p2_trace(a, mod, m):
    s, cur = 0, a
    for _ in range(m):
        s ^= cur
        cur = p2_mulmod(cur, cur, mod, m)
    assert s in (0, 1)
    return s


# ----------------------------------------------------------------------------- F_4 side, vectorised
def p2_vecmul(X, Y, mod, m):
    acc = np.zeros_like(X)
    for j in range(m):
        acc ^= (X << j) * ((Y >> j) & 1)
    for deg in range(2 * m - 2, m - 1, -1):
        acc ^= ((acc >> deg) & 1) * (mod << (deg - m))
    return acc


def parity(v):
    v = v.copy()
    for s in (32, 16, 8, 4, 2, 1):
        v ^= v >> s
    return v & 1


def wht(A, m):
    for j in range(m):
        a = A.reshape(-1, 2, 1 << j)
        a0 = a[:, 0, :].copy()
        a[:, 0, :] += a[:, 1, :]
        a[:, 1, :] = a0 - a[:, 1, :]


def p4_field(n):
    m = 2 * n
    mod = p2_find_modulus(m)
    E = (4 ** n - 1) // 3
    w = None
    for cand in range(2, 1 << m):
        w = p2_pow(cand, E, mod, m)
        if w != 1:
            break
    w2 = p2_mulmod(w, w, mod, m)
    assert p2_mulmod(w, w2, mod, m) == 1 and w not in (0, 1) and w2 == (w ^ 1), "w is not a cube root of 1"
    return m, mod, E, w, w2


def p4_setup(n, z0exp):
    """Field F_(4^n); f = x + z with z = w^z0exp (a single root, d = 1), or a list of exponents for several roots."""
    m, mod, E, w, w2 = p4_field(n)
    N = 1 << m
    f4 = [1, w, w2]  # w^0, w^1, w^2
    Y = np.arange(N, dtype=np.int64)
    roots = [f4[e % 3] for e in (z0exp if isinstance(z0exp, (list, tuple)) else [z0exp])]
    V = Y ^ roots[0]
    for r in roots[1:]:
        V = p2_vecmul(V, Y ^ r, mod, m)
    # cubic character: u = v^E, E = sum_{j<n} 4^j
    s = V.copy()
    u = V.copy()
    for _ in range(n - 1):
        s = p2_vecmul(s, s, mod, m)
        s = p2_vecmul(s, s, mod, m)
        u = p2_vecmul(u, s, mod, m)
    te = np.full(N, -1, dtype=np.int64)  # exponent of w, -1 where f = 0
    te[u == 1] = 0
    te[u == w] = 1
    te[u == w2] = 2
    assert int((te == -1).sum()) == len(set(roots)), "character values outside {0,1,w,w^2}"
    trmask = 0
    for l in range(m):
        if p2_trace(1 << l, mod, m):
            trmask |= 1 << l
    return dict(m=m, mod=mod, N=N, te=te, f4=f4, Y=Y, trmask=trmask)


def p4_perm(S, b):
    """index of xi(y), xi(y)_j = Tr(b y theta^j)."""
    m, mod, Y = S["m"], S["mod"], S["Y"]
    idx = np.zeros(S["N"], dtype=np.int64)
    for j in range(m):
        bt = p2_mulmod(b, 1 << j, mod, m)
        row = 0
        for l in range(m):
            if p2_trace(p2_mulmod(bt, 1 << l, mod, m), mod, m):
                row |= 1 << l
        idx |= parity(Y & row) << j
    return idx


def mul_t(A, B, te):
    """(a + b w) * w^te, zero where te = -1."""
    A2 = np.where(te == 0, A, np.where(te == 1, -B, np.where(te == 2, B - A, 0)))
    B2 = np.where(te == 0, B, np.where(te == 1, A - B, np.where(te == 2, -A, 0)))
    return A2, B2


_P4 = {}


def p4_run(n, z0exp, hexp, cexp, K):
    """h = w^hexp, c_i = w^cexp[i-1]. Returns tau[i][name] for name in 0, 1, w, w2."""
    key = (n, tuple(z0exp) if isinstance(z0exp, (list, tuple)) else z0exp)
    if key not in _P4:
        _P4.clear()
        _P4[key] = p4_setup(n, z0exp)
        _P4[key]["perms"] = {}
    S = _P4[key]
    m, N, te, f4 = S["m"], S["N"], S["te"], S["f4"]
    A = np.where(te == 0, 1, np.where(te == 1, 0, np.where(te == 2, -1, 0))).astype(np.int64)
    B = np.where(te == 0, 0, np.where(te == 1, 1, np.where(te == 2, -1, 0))).astype(np.int64)
    pts = {"0": 0, "1": 1, "w": f4[1], "w2": f4[2]}
    res = {}
    perms = S["perms"]
    for i in range(1, K + 1):
        bexp = (hexp + cexp[i - 1]) % 3
        if bexp not in perms:
            perms[bexp] = p4_perm(S, f4[bexp])
        wht(A, m)
        wht(B, m)
        Ah, Bh = A[perms[bexp]], B[perms[bexp]]
        res[i] = {k: (int(Ah[v]), int(Bh[v])) for k, v in pts.items()} if bound_ok(N, i) else None
        A, B = mul_t(Ah, Bh, te)
    return res, S


def p4_brute(n, z0exp, hexp, cexp, K):
    m, mod, E, w, w2 = p4_field(n)
    N = 1 << m
    f4 = [1, w, w2]
    roots = [f4[e % 3] for e in (z0exp if isinstance(z0exp, (list, tuple)) else [z0exp])]

    def tval(y):
        v = 1
        for r in roots:
            v = p2_mulmod(v, y ^ r, mod, m)
        if v == 0:
            return None
        u = p2_pow(v, E, mod, m)
        return {1: 0, w: 1, w2: 2}[u]

    te = [tval(y) for y in range(N)]
    g = [(0, 0) if e is None else W_POW[e] for e in te]
    pts = {"0": 0, "1": 1, "w": w, "w2": w2}
    res = {}
    for i in range(1, K + 1):
        b = f4[(hexp + cexp[i - 1]) % 3]
        tau = []
        for y in range(N):
            by = p2_mulmod(b, y, mod, m)
            acc = (0, 0)
            for x in range(N):
                if p2_trace(p2_mulmod(by, x, mod, m), mod, m):
                    acc = (acc[0] - g[x][0], acc[1] - g[x][1])
                else:
                    acc = zadd(acc, g[x])
            tau.append(acc)
        res[i] = {k: tau[v] for k, v in pts.items()}
        g = [(0, 0) if te[y] is None else zmul(tau[y], W_POW[te[y]]) for y in range(N)]
    return res


# ----------------------------------------------------------------------------- prediction (PROOF_V2 S5)
def predict(Z, rho, K, mul):
    """Z: list of rational points that are roots (hashable field elements); rho[i] for i >= 2;
    mul(a, b): product in the field. Points not rational are passed as opaque tags that never equal
    a rational point. Returns per stage i: (rank, drops dict, hypothesis_ok)."""
    out = {}
    S_prev = {"ZERO_TAG": 1}  # convention S_0 = {0}, m = 1: gives Sigma_1 = {0} with drop 1
    S_cur = {z: 1 for z in Z}  # S_1 = Z, m_1 = 1
    ok = True
    for i in range(1, K + 1):
        rank = sum(S_cur.values())
        drops = {}
        if i == 1:
            drops[0] = 1
        else:
            for s, mult in S_prev.items():
                pt = mul(rho[i], s)
                drops[pt] = drops.get(pt, 0) + mult
        out[i] = (rank, dict(drops), ok)
        if any(z in drops for z in Z):
            ok = False  # (G) fails for the next sheaf
        S_next = {z: rank for z in Z}
        for pt, mult in drops.items():
            if pt not in S_next:
                S_next[pt] = mult
        S_prev, S_cur = S_cur, S_next
    return out


def degree_from(e):
    """last m with e_m != 0."""
    D = 0
    for m in range(1, len(e)):
        if e[m] != (0, 0):
            D = m
    return D


def integral(e):
    return all(x.denominator == 1 and y.denominator == 1 for x, y in e)


TOTAL = {"valid_agree": 0, "valid_undet": 0, "valid_disagree": 0,
         "control_agree": 0, "control_undet": 0, "control_disagree": 0, "nonintegral": 0}


def compare(label, taus_by_n, K, pred, points, valid_upto):
    """taus_by_n[n][i][pt]; pred[i] = (rank, drops, ok); points: name -> field key for the drops dict."""
    nmax = max(taus_by_n)
    for i in range(1, K + 1):
        Ni = max(n for n in taus_by_n if all(taus_by_n[k][i] is not None for k in range(1, n + 1)))
        rank, drops, ok = pred[i]
        for name, key in points.items():
            p = [None] + [zscal(taus_by_n[n][i][name], (-1) ** i) for n in range(1, Ni + 1)]
            e = newton(p)
            if not integral(e):
                TOTAL["nonintegral"] += 1
            Dc = degree_from(e)
            Dp = rank - drops.get(key, 0)
            determined = Dc < Ni
            kind = "valid" if (ok and i <= valid_upto) else "control"
            # A stalk of dimension D < N forces e_m = 0 for D < m <= N. So the prediction is testable when
            # Dp < N (then it holds iff the computed degree equals Dp), and also refuted when Dp >= N but the
            # computed series stops below N. Otherwise nothing can be said.
            if Dp < Ni:
                verdict = "AGREE" if Dc == Dp else "DISAGREE"
            else:
                verdict = "UNDET" if Dc == Ni else "DISAGREE"
            TOTAL[kind + "_" + verdict.lower()] += 1
            say("  %-22s Q_%d at y=%-2s N=%2d predicted %3d computed %s%-3d %s (%s)%s" % (
                label, i, name, Ni, Dp, "" if determined else ">=", Dc, verdict, kind,
                "" if integral(e) else " NONINTEGRAL"))
    return nmax


def main():
    out_path = sys.argv[1]
    say("round4_check.py: main-session recomputation of stalk dimensions (exact, net counts only)")

    # ---- validation of the engines against direct sums
    say("== validation against direct double sums (pure python, separate trace code)")
    bad = 0
    cases = 0
    for n in (1, 2, 3):
        for fcoef, h, c in (([2, 1], 1, [1, 1, 1]), ([1, 2, 0, 1], 2, [1, 2, 1]), ([2, 1], 2, [2, 1, 1])):
            fast, _ = p3_run(n, fcoef, h, c, 3)
            slow = p3_brute(n, fcoef, h, c, 3)
            for i in (1, 2, 3):
                for y in range(3):
                    cases += 1
                    if fast[i][str(y)] != slow[i][y]:
                        bad += 1
    say("  F_3 engine: %d values compared, %d mismatches" % (cases, bad))
    bad4 = 0
    cases4 = 0
    for n in (1, 2, 3):
        for z0, hexp, cexp in ((0, 0, [0, 2, 1]), (0, 1, [0, 1, 1]), ([0, 1], 0, [0, 2, 1])):
            fast, _ = p4_run(n, z0, hexp, cexp, 3)
            slow = p4_brute(n, z0, hexp, cexp, 3)
            for i in (1, 2, 3):
                for k in ("0", "1", "w", "w2"):
                    cases4 += 1
                    if fast[i][k] != slow[i][k]:
                        bad4 += 1
    say("  F_4 engine: %d values compared, %d mismatches" % (cases4, bad4))
    if bad or bad4:
        say("VALIDATION FAILED")
        open(out_path, "w", encoding="utf-8").write("\n".join(OUT) + "\n")
        sys.exit(1)

    def mul3(a, b):
        """a in F_3^*, b a rational point (int) or a non-rational root scaled by a constant of F_3^*."""
        if isinstance(b, tuple):
            return ("root", b[1], (a * b[2]) % 3)
        return (a * b) % 3

    # ---- case 1: p = 3, quadratic character, d = 1, f = x - 1, plain quadric (rho_i = -1), h = 1 and 2
    say("== case 1: q = 3, quadratic chi, f = x - 1 (d = 1), c = (1,1,1,1), rho_i = -1; valid to Q_4")
    for h in (1, 2):
        NM = QUICK or 12
        taus = {n: p3_run(n, [2, 1], h, [1, 1, 1, 1], 4)[0] for n in range(1, NM + 1)}
        pred = predict([1], {i: 2 for i in range(2, 6)}, 4, mul3)
        compare("q3 d1 h=%d" % h, taus, 4, pred, {"0": 0, "1": 1, "2": 2}, 4)

    # ---- case 2: p = 3, d = 3, f = x^3 - x + 1 (irreducible; roots outside F_3), plain quadric
    say("== case 2: q = 3, quadratic chi, f = x^3 - x + 1 (d = 3), c = (1,1), rho_2 = -1; Q_1, Q_2")
    for h in (1, 2):
        NM = QUICK or 13
        taus = {n: p3_run(n, [1, 2, 0, 1], h, [1, 1], 2)[0] for n in range(1, NM + 1)}
        # roots are not rational: tags that never equal a point of F_3
        pred = predict([("root", "z1", 1), ("root", "z2", 1), ("root", "z3", 1)], {2: 2}, 2, mul3)
        compare("q3 d3 h=%d" % h, taus, 2, pred, {"0": 0, "1": 1, "2": 2}, 2)
        # anchor: the stalk of Q_1 at 0 is H^1_c(A^1, j_!L); its determinant is q = 3
        e = newton([None] + [zscal(taus[n][1]["0"], -1) for n in range(1, NM + 1)])
        say("  anchor: Q_1 at 0 has e_1 = %s, e_2 = %s (expected e_2 = (3, 0))" % (e[1], e[2]))

    # ---- case 3: control, (G) fails: c_2 = -c_1 so rho_2 = 1 and Sigma_2 meets Z
    say("== case 3 (control): q = 3, f = x - 1, c = (1,2,2,2): rho_2 = 1, so the hypothesis fails from P_3 on")
    NM = QUICK or 12
    taus = {n: p3_run(n, [2, 1], 1, [1, 2, 2, 2], 4)[0] for n in range(1, NM + 1)}
    pred = predict([1], {2: 1, 3: 2, 4: 2}, 4, mul3)
    compare("q3 d1 control", taus, 4, pred, {"0": 0, "1": 1, "2": 2}, 4)

    # ---- case 3b: control, plain quadric one stage further: rho_4 rho_2 = 1, Sigma_4 meets Z, so P_5 is outside (G)
    say("== case 3b (control): q = 3, f = x - 1, c = (1,1,1,1,1): Sigma_4 contains the root, hypothesis fails for P_5")
    NM = QUICK or 12
    taus = {n: p3_run(n, [2, 1], 1, [1, 1, 1, 1, 1], 5)[0] for n in range(1, NM + 1)}
    pred = predict([1], {i: 2 for i in range(2, 7)}, 5, mul3)
    compare("q3 d1 plain K=5", taus, 5, pred, {"0": 0, "1": 1, "2": 2}, 5)
    say("  (the hypothesis-valid value for Q_5 would be rank r_6 = 8; the prediction above treats the sheaf at the root as an extension by zero)")

    # ---- case 3c: control, f(0) = 0
    say("== case 3c (control): q = 3, f = x (d = 1, f(0) = 0), c = (1,1,1): Sigma_1 = {0} is the root")
    NM = QUICK or 12
    taus = {n: p3_run(n, [0, 1], 1, [1, 1, 1], 3)[0] for n in range(1, NM + 1)}
    pred = predict([0], {i: 2 for i in range(2, 5)}, 3, mul3)
    compare("q3 f=x", taus, 3, pred, {"0": 0, "1": 1, "2": 2}, 3)
    e = newton([None] + [taus[n][2]["0"] for n in range(1, NM + 1)])
    say("  Q_2 at y = 0, e_1..e_%d: %s" % (NM, " ".join("(%s,%s)" % (x, y) for x, y in e[1:])))

    # ---- case 4: q = 4, cubic character, d = 1, f = x + 1, rho_i = w for all i (c_i = w^(-(i-1)))
    say("== case 4: q = 4, cubic chi, f = x + 1 (d = 1), rho_i = w; valid to Q_5 (and Q_6, not run)")
    # exponents mod 3: points are 0 or w^e; represent field points for the prediction as "0" or exponent
    # prediction with multiplicative exponents; the point 0 is the tag "Z"
    def predict4(Zexp, rhoexp, K):
        out = {}
        S_prev = {"Z": 1}
        S_cur = {z: 1 for z in Zexp}
        ok = True
        for i in range(1, K + 1):
            rank = sum(S_cur.values())
            drops = {}
            if i == 1:
                drops["Z"] = 1
            else:
                for s, mult in S_prev.items():
                    pt = "Z" if s == "Z" else (rhoexp[i] + s) % 3
                    drops[pt] = drops.get(pt, 0) + mult
            out[i] = (rank, dict(drops), ok)
            if any(z in drops for z in Zexp):
                ok = False
            S_next = {z: rank for z in Zexp}
            for pt, mult in drops.items():
                if pt not in S_next:
                    S_next[pt] = mult
            S_prev, S_cur = S_cur, S_next
        return out
    K = 5
    cexp = [(-(i - 1)) % 3 for i in range(1, K + 1)]  # c_i = w^(-(i-1)), so rho_i = c_(i-1)/c_i = w
    for hexp in (0, 1):
        NM = QUICK or 11
        taus = {}
        for n in range(1, NM + 1):
            taus[n] = p4_run(n, 0, hexp, cexp, K)[0]
        pred = predict4([0], {i: 1 for i in range(2, K + 2)}, K)
        compare("q4 cubic d1 h=w^%d" % hexp, taus, K, pred, {"0": "Z", "1": 0, "w": 1, "w2": 2}, K)

    # ---- case 5: q = 4, cubic character, d = 2, f = (x + 1)(x + w), rho_2 = w^2 ... only Q_1, Q_2, Q_3
    say("== case 5: q = 4, cubic chi, f = (x + 1)(x + w) (d = 2): root ratios are all of F_4^*, so (G) fails at Sigma_2 for every rho_2")
    K = 3
    cexp = [0, 2, 1]  # rho_2 = c_1/c_2 = w^(0-2) = w, rho_3 = c_2/c_3 = w^(2-1) = w
    NM = QUICK or 11
    taus = {n: p4_run(n, [0, 1], 0, cexp, K)[0] for n in range(1, NM + 1)}
    pred = predict4([0, 1], {2: 1, 3: 1}, K)
    compare("q4 cubic d2", taus, K, pred, {"0": "Z", "1": 0, "w": 1, "w2": 2}, K)

    say("== totals")
    for k, v in TOTAL.items():
        say("  %-18s %d" % (k, v))
    open(out_path, "w", encoding="utf-8").write("\n".join(OUT) + "\n")


if __name__ == "__main__":
    main()
