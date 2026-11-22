"""Validate zfour.exe against the brute-force definition S_h = sum_{x in F^k} prod t(x_i) psi(Tr(h sum c_i x_i x_{i+1})).
The brute force uses an independent Python implementation of the field (digit tuples, own multiplication, own trace)."""
import itertools, sys
from a3lib import *

def field(p, N, poly):
    # elements: tuples of N digits; multiplication by polynomial arithmetic; independent of the C code
    def mul(a, b):
        r = polymulmod(list(a), list(b), poly, p)
        return tuple(r)
    def add(a, b): return tuple((x + y) % p for x, y in zip(a, b))
    zero = tuple([0] * N); one = tuple([1] + [0] * (N - 1)); X = tuple([0, 1] + [0] * (N - 2)) if N > 1 else tuple([(-poly[0]) % p])
    return mul, add, zero, one, X

def brute(p, u, n, Z, h, cs, k, poly):
    N = u * n; q = p ** u; Q = p ** N
    mul, add, zero, one, X = field(p, N, poly)
    # discrete log table by powers of X
    elems = {}; cur = one; pw = []
    for i in range(Q - 1):
        elems[cur] = i; pw.append(cur); cur = mul(cur, X)
    assert cur == one
    def pw_(l): return pw[l % (Q - 1)]
    xi = pw_((Q - 1) // (q - 1))   # xi = g^((Q-1)/(q-1))
    def code(c): return zero if c is None else pw_(c * ((Q - 1) // (q - 1)))
    def trace(z):
        acc = zero; cur = z
        for _ in range(N):
            acc = add(acc, cur); cur = tuple(cur)  # frobenius: z -> z^p
            # z^p via power
            cur = mul_pow(cur)
        return acc
    def mul_pow(z):
        r = one
        for _ in range(p): r = mul(r, z)
        return r
    def tr(z):
        acc = zero; cur = z
        for _ in range(N):
            acc = add(acc, cur); cur = mul_pow(cur)
        assert all(d == 0 for d in acc[1:])
        return acc[0]
    e = 2 if p == 3 else 3
    allel = [tuple(x) for x in itertools.product(range(p), repeat=N)]
    def t(y):
        s = 0
        for z in Z:
            d = tuple((a - b) % p for a, b in zip(y, code(z)))
            if d == zero: return ZW(0, 0)
            s += elems[d]
        j = s % e
        if p == 3: return ZW(1, 0) if j == 0 else ZW(-1, 0)
        return [ZW(1, 0), ZW(0, 1), ZW(-1, -1)][j]
    hc = code(h)
    cc = [code(c) for c in cs]
    tv = {y: t(y) for y in allel}
    def psi_pow(a):  # psi(a) as ZW
        if p == 3: return [ZW(1, 0), ZW(0, 1), ZW(-1, -1)][a % 3]
        return ZW(1, 0) if a % 2 == 0 else ZW(-1, 0)
    # S = sum over x in K^k of prod t * psi(Tr(h sum c_i x_i x_{i+1})); do by dynamic programming over a path (still brute force over x_i pairs)
    # G_1(x) = t(x); G_{i+1}(y) = t(y) sum_x G_i(x) psi(Tr(h c_i x y))
    G = dict(tv)
    out = {}
    for i in range(1, k + 1):
        b = mul(hc, cc[i - 1])
        # Ghat(y) for all y
        Gh = {}
        for y in allel:
            acc = ZW(0, 0)
            for x in allel:
                g = G[x]
                if g.iszero(): continue
                acc = acc + g * psi_pow(tr(mul(b, mul(x, y))))
            Gh[y] = acc
        out[i] = Gh[zero]   # sum_y G_i(y) = Ghat_i(0)
        G = {y: tv[y] * Gh[y] for y in allel}
    return out

def fullbrute(p, u, n, Z, h, cs, k, poly):
    """truly naive: sum over all x in K^k (no dynamic programming) of the k-fold product. Only for tiny sizes."""
    N = u * n; q = p ** u; Q = p ** N
    mul, add, zero, one, X = field(p, N, poly)
    elems = {}; cur = one; pw = []
    for i in range(Q - 1):
        elems[cur] = i; pw.append(cur); cur = mul(cur, X)
    def pw_(l): return pw[l % (Q - 1)]
    def code(c): return zero if c is None else pw_(c * ((Q - 1) // (q - 1)))
    def mul_pow(z):
        r = one
        for _ in range(p): r = mul(r, z)
        return r
    def tr(z):
        acc = zero; cur = z
        for _ in range(N):
            acc = add(acc, cur); cur = mul_pow(cur)
        return acc[0]
    e = 2 if p == 3 else 3
    allel = [tuple(x) for x in itertools.product(range(p), repeat=N)]
    def t(y):
        s = 0
        for z in Z:
            d = tuple((a - b) % p for a, b in zip(y, code(z)))
            if d == zero: return ZW(0, 0)
            s += elems[d]
        j = s % e
        if p == 3: return ZW(1, 0) if j == 0 else ZW(-1, 0)
        return [ZW(1, 0), ZW(0, 1), ZW(-1, -1)][j]
    tv = {y: t(y) for y in allel}
    def psi_pow(a):
        if p == 3: return [ZW(1, 0), ZW(0, 1), ZW(-1, -1)][a % 3]
        return ZW(1, 0) if a % 2 == 0 else ZW(-1, 0)
    hc = code(h); cc = [code(c) for c in cs]
    tot = ZW(0, 0)
    for xs in itertools.product(allel, repeat=k):
        pr = ZW(1, 0)
        for x in xs:
            pr = pr * tv[x]
            if pr.iszero(): break
        if pr.iszero(): continue
        a = 0
        for i in range(k - 1):
            a += tr(mul(hc, mul(cc[i], mul(xs[i], xs[i + 1]))))
        tot = tot + pr * psi_pow(a)
    return tot

if __name__ == "__main__":
    cases = [
        (3, 1, [0], 0, [0, 0, 1], 3, [1, 2, 3]),     # q=3, f=x-1 (root xi^0 = 1), h=1, c=(1,1,xi)?? codes
        (3, 1, [0], 0, [0, 0, 0], 3, [1, 2, 3]),
        (2, 2, [0, 1], 0, [0, 1, 2], 3, [1, 2]),     # q=4, Z={1,xi}, c=(1,xi,xi^2)
        (2, 2, [0], 1, [2, 1, 0], 3, [1, 2]),
    ]
    bad = 0
    for (p, u, Z, h, cs, k, ns) in cases:
        for n in ns:
            N = u * n
            poly = primitive_poly(p, N)
            cfg = [f"v 0 {len(Z)} {' '.join(map(str, Z))} {k} {' '.join(map(str, cs[:k]))} 1 -1".replace("v 0", f"v {h}")]
            # cfg format: id h nz z.. K c.. nw w..
            cfg = [f"v {h} {len(Z)} {' '.join(map(str, Z))} {k} {' '.join(map(str, cs[:k]))} 1 -1"]
            res = run_engine(p, u, n, cfg, "val")
            dp = brute(p, u, n, Z, h, cs, k, poly)
            eng = {i: ZW(*res[("v", n, i, -1)]) for i in range(1, k + 1)}
            for i in range(1, k + 1):
                same = (eng[i] - dp[i]).iszero()
                if not same: bad += 1
                print(f"p={p} u={u} n={n} Z={Z} h={h} c={cs} stage {i}: engine={eng[i]} dp={dp[i]} {'OK' if same else 'MISMATCH'}")
            # full naive sum for k up to 3 when small, using c_1..c_{k-1}
            if (p ** N) ** k <= 300000:
                fb = fullbrute(p, u, n, Z, h, cs, k, poly)
                same = (fb - eng[k]).iszero()
                if not same: bad += 1
                print(f"   fullbrute k={k}: {fb} vs engine {eng[k]} {'OK' if same else 'MISMATCH'}")
    print("MISMATCHES:", bad)
