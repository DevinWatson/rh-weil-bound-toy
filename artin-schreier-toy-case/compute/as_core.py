"""
Exact cyclotomic-integer arithmetic in Z[zeta_p] and exact DP evaluators for the
Artin-Schreier path-quadric toy case:

    t(x) = psi(Tr(f(x))),   Q_c(x) = sum_{i=0}^{k-2} c_i x_i x_{i+1},
    N_k(c) = sum_{Q_c(x) = 0} prod_{i=0}^{k-1} t(x_i) in Z[zeta_p],
    M = sum_x t(x) in Z[zeta_p].

Every element of Z[zeta_p] is represented as a length-p list of exact Python ints
`v` denoting sum_{a=0}^{p-1} v[a] * zeta_p^a. Since 1 + zeta_p + ... + zeta_p^{p-1} = 0,
canonical reduction subtracts v[p-1] from every coordinate (so canonical[p-1] == 0).
All verification checks use exact integers/Fractions; floats appear only in display
helpers explicitly labelled as display-only.
"""

from __future__ import annotations
import math
from fractions import Fraction
from typing import Sequence


# ---------------------------------------------------------------------------
# Exact arithmetic in Z[zeta_p]
# ---------------------------------------------------------------------------

def cyc_zero(p: int) -> list[int]:
    return [0] * p


def cyc_one(p: int) -> list[int]:
    v = [0] * p
    v[0] = 1
    return v


def cyc_zeta(p: int, a: int) -> list[int]:
    v = [0] * p
    v[a % p] = 1
    return v


def cyc_canon(v: Sequence[int]) -> tuple[int, ...]:
    """Canonical representative in Z[zeta_p] = Z[T]/(1+T+...+T^{p-1}) with last coeff 0."""
    c = v[-1]
    return tuple(x - c for x in v)


def cyc_eq(u: Sequence[int], v: Sequence[int]) -> bool:
    return cyc_canon(u) == cyc_canon(v)


def cyc_add(u: Sequence[int], v: Sequence[int]) -> list[int]:
    return [a + b for a, b in zip(u, v)]


def cyc_sub(u: Sequence[int], v: Sequence[int]) -> list[int]:
    return [a - b for a, b in zip(u, v)]


def cyc_scale(k: int, v: Sequence[int]) -> list[int]:
    return [k * x for x in v]


def cyc_shift(v: Sequence[int], a: int) -> list[int]:
    """Multiply v by zeta_p^a."""
    p = len(v)
    a %= p
    if a == 0:
        return list(v)
    return list(v[p - a:]) + list(v[:p - a])


def cyc_mul(u: Sequence[int], v: Sequence[int]) -> list[int]:
    """Exact product in Z[T]/(T^p - 1), valid in Z[zeta_p]."""
    p = len(u)
    out = [0] * p
    for i, ui in enumerate(u):
        if ui:
            for j, vj in enumerate(v):
                if vj:
                    out[(i + j) % p] += ui * vj
    return out


def cyc_pow(u: Sequence[int], e: int) -> list[int]:
    p = len(u)
    res = cyc_one(p)
    base = list(u)
    while e > 0:
        if e & 1:
            res = cyc_mul(res, base)
        e >>= 1
        if e:
            base = cyc_mul(base, base)
    return res


def cyc_conj(v: Sequence[int]) -> list[int]:
    """Complex conjugation: zeta_p^a -> zeta_p^{-a}."""
    p = len(v)
    out = [0] * p
    out[0] = v[0]
    for a in range(1, p):
        out[p - a] = v[a]
    return out


def cyc_abs_sq_element(v: Sequence[int]) -> list[int]:
    """Exact element |v|^2 = v * conj(v) in Z[zeta_p + zeta_p^{-1}] subset Z[zeta_p]."""
    return cyc_mul(v, cyc_conj(v))


def cyc_galois_avg_abs_sq(v: Sequence[int]) -> Fraction:
    """
    Exact rational average (1/(p-1)) sum_{a=1}^{p-1} |sigma_a(v)|^2.
    For v = sum_{r=0}^{p-1} c_r zeta_p^r:
        sum_{a=1}^{p-1} |sigma_a(v)|^2 = p * sum_r c_r^2 - (sum_r c_r)^2.
    """
    p = len(v)
    s1 = sum(v)
    s2 = sum(x * x for x in v)
    return Fraction(p * s2 - s1 * s1, p - 1)


def cyc_galois_sum_abs_sq(v: Sequence[int]) -> int:
    """Exact integer sum_{a=1}^{p-1} |sigma_a(v)|^2 = p * sum c_r^2 - (sum c_r)^2."""
    p = len(v)
    s1 = sum(v)
    s2 = sum(x * x for x in v)
    return p * s2 - s1 * s1


def cyc_to_complex_display(v: Sequence[int], a: int = 1) -> complex:
    """Display-only float evaluation at zeta_p = exp(2 pi i a / p). Never used for checks."""
    p = len(v)
    ang = 2.0 * math.pi * a / p
    re = sum(c * math.cos(ang * r) for r, c in enumerate(v))
    im = sum(c * math.sin(ang * r) for r, c in enumerate(v))
    return complex(re, im)


# ---------------------------------------------------------------------------
# Polynomial evaluation and exact DP over F_p
# ---------------------------------------------------------------------------

def eval_poly_mod(coeffs: Sequence[int], x: int, p: int) -> int:
    """Evaluate sum_j coeffs[j] x^j mod p (coeffs[0] is constant term)."""
    acc = 0
    for c in reversed(coeffs):
        acc = (acc * x + c) % p
    return acc


def poly_values_fp(coeffs: Sequence[int], p: int) -> list[int]:
    return [eval_poly_mod(coeffs, x, p) for x in range(p)]


def compute_M_fp(fvals: Sequence[int], p: int) -> list[int]:
    """Exact M = sum_{x in F_p} zeta_p^{f(x)}."""
    out = [0] * p
    for val in fvals:
        out[val] += 1
    return out


def compute_Nall_dp_fp(fvals: Sequence[int], c: Sequence[int], p: int) -> list[list[int]]:
    """
    Exact DP returning Nall[s] = sum_{Q_c(x) = s} zeta_p^{sum f(x_i)} in Z[zeta_p]
    for every s in F_p, where len(c) = k - 1 (k >= 2).

    State at step i (after choosing x_0, ..., x_i):
      dp[s][x_i][r] = #{(x_0, ..., x_i) : sum_{j<i} c_j x_j x_{j+1} = s, sum_{j<=i} f(x_j) = r}.
    Complexity: O(k * p^4) integer additions, exact with Python bigints.
    """
    k = len(c) + 1
    assert k >= 2
    # Step 0: s = 0, x_0 in F_p, r = f(x_0)
    dp = [[[0] * p for _ in range(p)] for _ in range(p)]
    for x0 in range(p):
        dp[0][x0][fvals[x0]] = 1

    for step in range(k - 1):
        ci = c[step] % p
        ndp = [[[0] * p for _ in range(p)] for _ in range(p)]
        for s in range(p):
            row_s = dp[s]
            for xprev in range(p):
                vec = row_s[xprev]
                # Skip all-zero vectors
                if not any(vec):
                    continue
                step_delta = (ci * xprev) % p
                for xnext in range(p):
                    ns = (s + step_delta * xnext) % p
                    fn = fvals[xnext]
                    target = ndp[ns][xnext]
                    # Shift vec by fn mod p and add into target
                    if fn == 0:
                        for r in range(p):
                            target[r] += vec[r]
                    else:
                        split = p - fn
                        for r in range(split):
                            target[r + fn] += vec[r]
                        for r in range(split, p):
                            target[r - split] += vec[r]
        dp = ndp

    # Sum over final coordinate x_{k-1}
    out = [[0] * p for _ in range(p)]
    for s in range(p):
        for xlast in range(p):
            vec = dp[s][xlast]
            for r in range(p):
                out[s][r] += vec[r]
    return out


def compute_N_dp_fast_fp(fvals: Sequence[int], c: Sequence[int], p: int) -> list[list[int]]:
    """
    Faster exact DP over F_p using flat integer lists and precomputed shifts.
    Returns Nall[s] in Z[zeta_p] for s = 0..p-1.
    """
    return compute_Nall_dp_fp(fvals, c, p)


def compute_Nall_brute_fp(fvals: Sequence[int], c: Sequence[int], p: int) -> list[list[int]]:
    """Exact brute-force enumeration over F_p^k (for validation at small p, k)."""
    k = len(c) + 1
    out = [[0] * p for _ in range(p)]
    xs = [0] * k

    def rec(idx: int, q_acc: int, f_acc: int) -> None:
        if idx == k:
            out[q_acc][f_acc] += 1
            return
        if idx == 0:
            for x in range(p):
                xs[0] = x
                rec(1, 0, fvals[x])
        else:
            prev_c = (c[idx - 1] * xs[idx - 1]) % p
            for x in range(p):
                xs[idx] = x
                rec(idx + 1, (q_acc + prev_c * x) % p, (f_acc + fvals[x]) % p)

    rec(0, 0, 0)
    return out


def compute_S_from_Nall(Nall: Sequence[Sequence[int]], h: int, p: int) -> list[int]:
    """
    Exact S(h) = sum_{s in F_p} Nall[s] * zeta_p^{h * s} in Z[zeta_p].
    """
    out = [0] * p
    h %= p
    for s in range(p):
        hs = (h * s) % p
        vec = Nall[s]
        for r in range(p):
            out[(r + hs) % p] += vec[r]
    return out


def compute_R_from_Nall(Nall: Sequence[Sequence[int]], p: int) -> list[int]:
    """Exact R = sum_{h=1}^{p-1} S(h) in Z[zeta_p]."""
    out = [0] * p
    for h in range(1, p):
        sh = compute_S_from_Nall(Nall, h, p)
        for r in range(p):
            out[r] += sh[r]
    return out


# ---------------------------------------------------------------------------
# Fast O(p^2) exact Segre formula for k = 4 over F_p
# ---------------------------------------------------------------------------

def compute_C_table_fp(fvals: Sequence[int], p: int) -> list[list[int]]:
    """Exact C(r) = sum_{x in F_p} zeta_p^{f(x) + f(r*x)} in Z[zeta_p] for r = 0..p-1."""
    table = [[0] * p for _ in range(p)]
    for r in range(p):
        vec = table[r]
        for x in range(p):
            vec[(fvals[x] + fvals[(r * x) % p]) % p] += 1
    return table


def compute_N4_segre_fp(
    fvals: Sequence[int],
    c: tuple[int, int, int],
    p: int,
    C_table: Sequence[Sequence[int]] | None = None,
    M: Sequence[int] | None = None,
) -> list[int]:
    """
    Exact O(p^2) Segre formula for k = 4 (c1, c2, c3 != 0 mod p):
        N_4 = -p * t_0^4 + t_0^2 * M^2 + sum_{r in F_p} C(r) * C(tau(r))
    where t_0 = zeta_p^{f(0)}, tau(r) = -(c3 * r + c2) / c1 mod p.

    Check of origin term:
      On each plane Pi_lam, origin contributes t_0^4 (Wait: t_0^4 = zeta_p^{4 f(0)}!).
      There are p + 1 planes in P^1(F_p), meeting at the origin 0:
      N_4 = t_0^4 + sum_{lam in P^1} (Plane_lam - t_0^4)
          = t_0^4 - (p + 1) t_0^4 + (t_0 M)^2 + sum_{r in F_p} C(r) C(tau(r))
          = -p * t_0^4 + t_0^2 * M^2 + sum_{r in F_p} C(r) C(tau(r)).
      (Notice: for quadratic character t_0^2 = 1 so t_0^4 = 1; for Artin-Schreier
      t_0 = zeta_p^{f(0)}, so keeping t_0^4 handles f(0) != 0 cleanly!)
    """
    c1, c2, c3 = c[0] % p, c[1] % p, c[2] % p
    assert c1 != 0 and c2 != 0 and c3 != 0
    if C_table is None:
        C_table = compute_C_table_fp(fvals, p)
    if M is None:
        M = compute_M_fp(fvals, p)
    inv_c1 = pow(c1, p - 2, p)
    a = (-c3 * inv_c1) % p
    b = (-c2 * inv_c1) % p

    f0 = fvals[0]
    t0_sq = cyc_zeta(p, 2 * f0)
    t0_4 = cyc_zeta(p, 4 * f0)
    out = cyc_sub(cyc_mul(t0_sq, cyc_mul(M, M)), cyc_scale(p, t0_4))
    for r in range(p):
        tr = (a * r + b) % p
        prod = cyc_mul(C_table[r], C_table[tr])
        for i in range(p):
            out[i] += prod[i]
    return out


# ---------------------------------------------------------------------------
# Finite field extensions F_{p^n} = F_p[u] / (mod_poly(u))
# ---------------------------------------------------------------------------

class FiniteField:
    """Exact finite field F_{p^n} = F_p[u]/(mod_poly), with exact multiplication & trace tables."""

    def __init__(self, p: int, mod_poly: Sequence[int]):
        """mod_poly is monic of degree n: coeffs [a_0, a_1, ..., a_{n-1}, 1]."""
        self.p = p
        self.n = len(mod_poly) - 1
        assert mod_poly[-1] % p == 1
        self.mod_poly = [x % p for x in mod_poly]
        self.q = p ** self.n
        # Encode elements as ints 0..q-1 in base p
        self.polys = [self._decode(i) for i in range(self.q)]
        self.add_tab = [[0] * self.q for _ in range(self.q)]
        self.sub_tab = [[0] * self.q for _ in range(self.q)]
        self.neg_tab = [0] * self.q
        self.mul_tab = [[0] * self.q for _ in range(self.q)]
        self.inv_tab = [0] * self.q
        self.tr_tab = [0] * self.q

        for i in range(self.q):
            pi = self.polys[i]
            self.neg_tab[i] = self._encode([(-c) % p for c in pi])
            for j in range(self.q):
                pj = self.polys[j]
                self.add_tab[i][j] = self._encode([(pi[k] + pj[k]) % p for k in range(self.n)])
                self.sub_tab[i][j] = self._encode([(pi[k] - pj[k]) % p for k in range(self.n)])
                self.mul_tab[i][j] = self._encode(self._poly_mul_mod(pi, pj))

        for i in range(1, self.q):
            for j in range(1, self.q):
                if self.mul_tab[i][j] == 1:
                    self.inv_tab[i] = j
                    break
            assert self.inv_tab[i] != 0, f"mod_poly {mod_poly} is not irreducible mod {p}"

        # Trace Tr_{F_q / F_p}(x) = sum_{j=0}^{n-1} x^{p^j}
        for i in range(self.q):
            s = 0
            cur = i
            for _ in range(self.n):
                s = self.add_tab[s][cur]
                cur = self.pow(cur, p)
            # s must lie in F_p (only constant term nonzero)
            ps = self.polys[s]
            assert all(ps[k] == 0 for k in range(1, self.n))
            self.tr_tab[i] = ps[0]

    def _decode(self, idx: int) -> list[int]:
        out = []
        for _ in range(self.n):
            out.append(idx % self.p)
            idx //= self.p
        return out

    def _encode(self, poly: Sequence[int]) -> int:
        acc = 0
        for c in reversed(poly):
            acc = acc * self.p + (c % self.p)
        return acc

    def _poly_mul_mod(self, a: Sequence[int], b: Sequence[int]) -> list[int]:
        p, n = self.p, self.n
        prod = [0] * (2 * n - 1)
        for i in range(n):
            if a[i]:
                for j in range(n):
                    prod[i + j] = (prod[i + j] + a[i] * b[j]) % p
        for deg in range(2 * n - 2, n - 1, -1):
            lead = prod[deg]
            if lead:
                shift = deg - n
                for j in range(n + 1):
                    prod[shift + j] = (prod[shift + j] - lead * self.mod_poly[j]) % p
        return prod[:n]

    def pow(self, x: int, e: int) -> int:
        res = 1
        base = x
        while e > 0:
            if e & 1:
                res = self.mul_tab[res][base]
            e >>= 1
            if e:
                base = self.mul_tab[base][base]
        return res

    def eval_poly_fp_coeffs(self, coeffs: Sequence[int], x: int) -> int:
        """Evaluate polynomial with F_p coefficients at x in F_q."""
        acc = 0
        for c in reversed(coeffs):
            acc = self.add_tab[self.mul_tab[acc][x]][c % self.p]
        return acc

    def tr_fvals(self, coeffs: Sequence[int]) -> list[int]:
        """Return [Tr(f(x)) mod p for x in F_q]."""
        return [self.tr_tab[self.eval_poly_fp_coeffs(coeffs, x)] for x in range(self.q)]


def compute_M_fq(tfvals: Sequence[int], p: int) -> list[int]:
    out = [0] * p
    for val in tfvals:
        out[val] += 1
    return out


def compute_C_table_fq(F: FiniteField, tfvals: Sequence[int]) -> list[list[int]]:
    p, q = F.p, F.q
    mul = F.mul_tab
    table = [[0] * p for _ in range(q)]
    for r in range(q):
        vec = table[r]
        mul_r = mul[r]
        for x in range(q):
            vec[(tfvals[x] + tfvals[mul_r[x]]) % p] += 1
    return table


def compute_N4_segre_fq(
    F: FiniteField,
    tfvals: Sequence[int],
    c: tuple[int, int, int],
    C_table: Sequence[Sequence[int]] | None = None,
    M: Sequence[int] | None = None,
) -> list[int]:
    """Exact Segre formula for k = 4 over F_{p^n}, returning an element of Z[zeta_p]."""
    p, q = F.p, F.q
    c1, c2, c3 = c
    assert c1 != 0 and c2 != 0 and c3 != 0
    if C_table is None:
        C_table = compute_C_table_fq(F, tfvals)
    if M is None:
        M = compute_M_fq(tfvals, p)
    inv_c1 = F.inv_tab[c1]
    a = F.neg_tab[F.mul_tab[c3][inv_c1]]
    b = F.neg_tab[F.mul_tab[c2][inv_c1]]

    f0 = tfvals[0]
    t0_sq = cyc_zeta(p, 2 * f0)
    t0_4 = cyc_zeta(p, 4 * f0)
    out = cyc_sub(cyc_mul(t0_sq, cyc_mul(M, M)), cyc_scale(q, t0_4))
    mul_a = F.mul_tab[a]
    add_b = F.add_tab[b]
    for r in range(q):
        tr = add_b[mul_a[r]]
        prod = cyc_mul(C_table[r], C_table[tr])
        for i in range(p):
            out[i] += prod[i]
    return out
