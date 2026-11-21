"""Exact fibre sums S_h(n) over F_Q, Q = q^n, p = 3, values in Z[omega] (pairs of int64, overflow tracked).
omega = exp(2 pi i/3), represented as a + b*omega, omega^2 = -1 - omega.
Field F_{3^m}: elements as base-3 digit vectors (coefficients of 1,x,..,x^{m-1}); log/exp tables from a primitive polynomial.
"""
import ctypes, itertools, sys
import numpy as np
try:
    ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x4000)
except Exception:
    pass

LIMIT = (1 << 63) // 5 - 1   # before each DFT stage max|coord| must be below this (stage multiplies by <=5)


class Field:
    def __init__(self, m):
        self.m = m
        self.Q = 3 ** m
        self.pows = 3 ** np.arange(m, dtype=np.int64)
        self._build()

    def _build(self):
        m, Q = self.m, self.Q
        if m == 1:
            # F_3, generator 2
            polys = [None]
        rng = np.random.default_rng(12345 + m)
        tries = 0
        while True:
            tries += 1
            # monic x^m = -(low) ; low coefficients vector
            low = rng.integers(0, 3, size=m)
            if m == 1:
                low = np.array([1])  # x = -1 = 2 is primitive in F_3 (x + 1 = 0)
            if low[0] == 0:
                continue
            # matrix of multiplication by x on digit vectors (row vector convention v -> v @ Mx)
            Mx = np.zeros((m, m), dtype=np.int64)
            for i in range(m - 1):
                Mx[i, i + 1] = 1
            Mx[m - 1, :] = (-low) % 3
            E = np.zeros((Q - 1, m), dtype=np.int8)
            E[0, 0] = 1
            L = 1
            Mp = Mx.copy()  # mult by x^L
            while L < Q - 1:
                n2 = min(L, Q - 1 - L)
                E[L:L + n2] = ((E[:n2].astype(np.int64) @ Mp) % 3).astype(np.int8)
                L += n2
                Mp = (Mp @ Mp) % 3 if n2 == L // 2 or True else Mp
                # Mp must be x^L for new L; when L doubles exactly this holds; final partial block ends loop
            codes = E.astype(np.int64) @ self.pows
            cnt = np.bincount(codes, minlength=Q)
            if cnt[0] == 0 and cnt.max() == 1:
                # also need consistency x^(Q-1) = 1: E[Q-2]*x == E[0]
                last = (E[Q - 2].astype(np.int64) @ Mx) % 3
                if int(last @ self.pows) == 1:
                    break
            if m == 1:
                break
        self.low = low
        self.E = E
        self.codes_of_log = codes  # code of g^l
        LOG = np.full(Q, -1, dtype=np.int64)
        LOG[codes] = np.arange(Q - 1)
        self.LOG = LOG
        # trace table over exponents: TR[e] = Tr(g^e) in F_3 (int 0..2)
        e = np.arange(Q - 1, dtype=np.int64)
        acc = np.zeros(Q - 1, dtype=np.int64)
        for s in range(m):
            idx = (e * (3 ** s)) % (Q - 1)
            acc += E[idx, 0].astype(np.int64)
            # higher digits must cancel; check below on a sample
            if s == m - 1:
                pass
        # trace is element of F_3, so digits>0 of the sum vanish; verify
        accv = np.zeros((Q - 1, m), dtype=np.int64)
        for s in range(m):
            accv += E[(e * (3 ** s)) % (Q - 1)].astype(np.int64)
        accv %= 3
        assert not accv[:, 1:].any(), "trace not in F_3"
        self.TR = accv[:, 0].copy()

    # ---- element helpers (element = code, 0 = zero element) ----
    def digits(self, codes):
        return (codes[:, None] // self.pows[None, :]) % 3

    def mul(self, a, b):
        la, lb = self.LOG[a], self.LOG[b]
        r = self.codes_of_log[(la + lb) % (self.Q - 1)]
        return np.where((a == 0) | (b == 0), 0, r)

    def add(self, a, b):
        d = (self.digits(np.atleast_1d(a)) + self.digits(np.atleast_1d(b))) % 3
        return d @ self.pows

    def power(self, a, k):
        a = np.atleast_1d(a)
        r = self.codes_of_log[(self.LOG[a] * k) % (self.Q - 1)]
        return np.where(a == 0, 0 if k > 0 else 1, r)

    def elem(self, lg):
        return int(self.codes_of_log[lg % (self.Q - 1)])

    def neg(self, a):
        d = (-self.digits(np.atleast_1d(a))) % 3
        return d @ self.pows

    def inv(self, a):
        return int(self.codes_of_log[(-self.LOG[a]) % (self.Q - 1)])

    def trace(self, a):
        """a: array of codes -> int array in 0..2"""
        a = np.atleast_1d(a)
        out = np.where(a == 0, 0, self.TR[np.where(a == 0, 0, self.LOG[a])])
        return out


_fields = {}
def field(m):
    if m not in _fields:
        _fields[m] = Field(m)
    return _fields[m]


# ---------- subfield embedding F_q in F_{q^n}: gamma_n root of a fixed primitive poly of degree e ----------
_prim_poly = {}
def base_poly(e):
    """fixed polynomial (coeff list low->high, monic) = minimal polynomial of the generator of Field(e) w.r.t. its own table"""
    if e not in _prim_poly:
        F = field(e)
        # min poly of g over F_3: product (X - g^{3^s}); compute by evaluation consistency: use F.low relation: x^e = -low . x
        _prim_poly[e] = [int(v) for v in F.low] + [1]
    return _prim_poly[e]


def gamma(m, e):
    """element of F_{3^m} (code) that is a root of base_poly(e), with e | m. For e==1: -1 (poly x+1)."""
    F = field(m)
    poly = base_poly(e)
    q = 3 ** e
    step = (F.Q - 1) // (q - 1)
    for j in range(1, q - 1):
        from math import gcd
        if gcd(j, q - 1) != 1:
            continue
        g = F.elem(j * step)
        # evaluate poly at g
        acc = np.array([0], dtype=np.int64)
        for cf in reversed(poly):
            acc = F.add(F.mul(acc, np.array([g])), np.array([cf % 3]))
        if int(acc[0]) == 0:
            return g
    if e == 1:
        return F.elem((F.Q - 1) // 2)
    raise RuntimeError("no gamma")


def fq_element(m, e, exp):
    """gamma^exp in F_{3^m}; exp None -> 0"""
    if exp is None:
        return 0
    F = field(m)
    g = gamma(m, e)
    if exp % (3 ** e - 1) == 0:
        return 1
    return int(F.codes_of_log[(F.LOG[g] * exp) % (F.Q - 1)])


# ---------- Z[omega] arithmetic on arrays ----------
def w_mul(a, b):      # (a + b w) * w = -b + (a-b) w
    return -b, a - b


def w_mul2(a, b):     # * w^2 = (b-a) - a w
    return b - a, -a


def dft3_axis(A, B, axis):
    """3-point DFT along axis: out_u = v0 + w^u v1 + w^{2u} v2 ; A,B int64 arrays (shape (3,)*m)"""
    sl = [slice(None)] * A.ndim
    def part(X, i):
        s = list(sl); s[axis] = i; return X[tuple(s)]
    a0, a1, a2 = part(A, 0), part(A, 1), part(A, 2)
    b0, b1, b2 = part(B, 0), part(B, 1), part(B, 2)
    w1a, w1b = w_mul(a1, b1); w2a, w2b = w_mul2(a2, b2)       # w v1, w^2 v2
    x1a, x1b = w_mul2(a1, b1); x2a, x2b = w_mul(a2, b2)        # w^2 v1, w v2 (w^4 = w)
    OA = np.stack([a0 + a1 + a2, a0 + w1a + w2a, a0 + x1a + x2a], axis=axis)
    OB = np.stack([b0 + b1 + b2, b0 + w1b + w2b, b0 + x1b + x2b], axis=axis)
    return OA, OB


def dft(A, B, m, track):
    A = A.reshape((3,) * m); B = B.reshape((3,) * m)
    for ax in range(m):
        mx = max(int(np.abs(A).max()), int(np.abs(B).max()))
        track[0] = max(track[0], mx)
        if mx >= LIMIT:
            raise OverflowError("int64 margin exceeded: max coord %d" % mx)
        A, B = dft3_axis(A, B, ax)
    mx = max(int(np.abs(A).max()), int(np.abs(B).max()))
    track[0] = max(track[0], mx)
    return A.reshape(-1), B.reshape(-1)


def bilinear_index(F, a):
    """For element a (code), the permutation u(y): index of the dual vector (Tr(a x_j y))_j, for all y (codes 0..Q-1)."""
    m, Q = F.m, F.Q
    # B[j][i] = Tr(a * x^j * x^i)
    B = np.zeros((m, m), dtype=np.int64)
    la = F.LOG[a]
    for i in range(m):
        for j in range(m):
            B[j, i] = F.TR[(la + i + j) % (Q - 1)]
    Y = F.digits(np.arange(Q, dtype=np.int64))
    U = (Y @ B.T) % 3          # U[y, j] = sum_i B[j,i] y_i
    return U @ F.pows


def chi_array(F, fcoef_codes):
    """t(y) = chi_Q(f(y)) for all y codes; f coefficients as list of codes (low->high). returns int8 array in {-1,0,1}"""
    Q, m = F.Q, F.m
    y = np.arange(Q, dtype=np.int64)
    ly = F.LOG[y]  # -1 at y=0
    acc = np.zeros((Q, m), dtype=np.int64)
    for i, cf in enumerate(fcoef_codes):
        if cf == 0:
            continue
        lc = F.LOG[cf]
        if i == 0:
            acc += F.E[lc % (Q - 1)].astype(np.int64)[None, :]
        else:
            e = (lc + i * ly) % (Q - 1)
            term = F.E[e].astype(np.int64)
            term[0] = 0  # y=0 (ly=-1) gives garbage; y=0 contributes 0 for i>0
            acc += term
    acc %= 3
    code = acc @ F.pows
    lg = F.LOG[code]
    t = np.where(code == 0, 0, np.where(lg % 2 == 0, 1, -1))
    return t.astype(np.int64)


def fibre_sum(F, t, c_codes, h_code):
    """S_h = sum t(x1)..t(xk) psi(h sum c_i x_i x_{i+1}); returns (a,b) python ints meaning a + b*omega, and max coordinate seen"""
    Q = F.Q
    A = t.copy(); B = np.zeros(Q, dtype=np.int64)
    track = [0]
    for c in c_codes:
        a = int(F.mul(np.array([h_code]), np.array([c]))[0])
        u = bilinear_index(F, a)
        Ah, Bh = dft(A, B, F.m, track)
        A = Ah[u] * t
        B = Bh[u] * t
    def exact_sum(X):
        lo = int((X & 0xFFFFFFFF).sum()); hi = int((X >> 32).sum())   # both partial sums fit in int64
        return (hi << 32) + lo
    return exact_sum(A), exact_sum(B), track[0]
