"""
T3: Extension-field tests (F_{5^n}, n=1..4 and F_{7^n}, n=1..2), k=6 exact DP check,
and exact Euler-characteristic / Betti-number verification for the Artin-Schreier toy case.

All mathematical checks use exact integers / Fractions / Z[zeta_p]; floats appear only in
display columns explicitly marked as display-only.
"""

from fractions import Fraction
from pathlib import Path
from as_core import (
    FiniteField,
    compute_C_table_fp,
    compute_M_fp,
    compute_M_fq,
    compute_N4_segre_fp,
    compute_N4_segre_fq,
    compute_Nall_dp_fp,
    compute_R_from_Nall,
    cyc_add,
    cyc_eq,
    cyc_galois_avg_abs_sq,
    cyc_pow,
    cyc_scale,
    poly_values_fp,
)


def check_k4_transversal_over_fbar(c: tuple[int, int, int], d: int, p: int) -> tuple[bool, int]:
    """
    Exact algebraic check (via resultant / splitting field F_{p^2} for d=3) of whether
    c = (c1, c2, c3) in (F_p^*)^3 lies on any of the d^2 lines c1 + z1 c2 + z1 z2 c3 = 0
    with z1^d = z2^d = -1 in F_bar_p.
    Implemented for d = 3 (where z^3 = -1 splits completely in F_{p^2} for every p != 3).
    Returns (is_transversal, num_bad_pairs_in_Fbar).
    """
    assert d == 3 and p != 3
    # Build F_{p^2} via an irreducible quadratic x^2 - nr = 0
    nr = next(a for a in range(2, p) if pow(a, (p - 1) // 2, p) == p - 1)
    F2 = FiniteField(p, [(-nr) % p, 0, 1])
    zroots = [z for z in range(1, F2.q) if F2.pow(z, 3) == F2.neg_tab[1]]
    assert len(zroots) == 3
    c1, c2, c3 = c[0] % p, c[1] % p, c[2] % p
    hits = 0
    for z1 in zroots:
        for z2 in zroots:
            z12 = F2.mul_tab[z1][z2]
            val = F2.add_tab[c1][F2.add_tab[F2.mul_tab[z1][c2]][F2.mul_tab[z12][c3]]]
            if val == 0:
                hits += 1
    return (hits == 0, hits)


def main() -> None:
    lines: list[str] = []
    failures = 0

    def check(cond: bool, msg: str) -> None:
        nonlocal failures
        if not cond:
            failures += 1
            lines.append(f"FAIL: {msg}")

    lines.append("# T3: Extension fields, k = 6 exact DP, and Betti-number / Milnor checks\n")

    # ------------------------------------------------------------------
    # 1. Exact check over F_{5^n}, n = 1, 2, 3, 4 (q = 5, 25, 125, 625)
    # ------------------------------------------------------------------
    lines.append("## 1. Extension-field growth over F_{5^n} (n = 1..4, q = 5..625), k = 4, d = 3")
    # Irreducible polynomials over F_5:
    # n=1: u
    # n=2: u^2 + 2  (disc = -8 = 2 mod 5, non-square)
    # n=3: u^3 + 3u + 2  (check no roots mod 5: 0->2, 1->1, 2->1, 3->3, 4->3)
    # n=4: u^4 + u^2 + 2 (let FiniteField assert invertibility of every nonzero element!)
    ext_specs_5 = [
        (1, [0, 1]),
        (2, [2, 0, 1]),
        (3, [2, 3, 0, 1]),
        (4, [2, 0, 1, 0, 1]),
    ]
    # Verify c=(1,1,1) is transversal over F_bar_5 and c=(1,2,1) is on the bad line c1-c2+c3=0!
    ok_111, hits_111 = check_k4_transversal_over_fbar((1, 1, 1), 3, 5)
    ok_121, hits_121 = check_k4_transversal_over_fbar((1, 2, 1), 3, 5)
    check(ok_111 and hits_111 == 0, "c=(1,1,1) should be transversal over F_bar_5")
    check((not ok_121) and hits_121 == 1, "c=(1,2,1) should hit 1 bad line over F_bar_5")
    lines.append(f"  Transversality check over F_bar_5: c=(1,1,1) hits={hits_111} (GOOD), c=(1,2,1) hits={hits_121} (BAD: c1-c2+c3=0)\n")

    polys_5 = [
        ("x^3", [0, 0, 0, 1]),
        ("x^3+x", [0, 1, 0, 1]),
        ("x^3+x^2+x", [0, 1, 1, 1]),
    ]
    fields_5 = [FiniteField(5, mp) for _, mp in ext_specs_5]
    for pname, coeffs in polys_5:
        lines.append(f"  f(x) = {pname}:")
        for F in fields_5:
            q = F.q
            tf = F.tr_fvals(coeffs)
            M = compute_M_fq(tf, 5)
            # We only need C_tab once per (F, f)
            from as_core import compute_C_table_fq
            C_tab = compute_C_table_fq(F, tf)
            n4_good = compute_N4_segre_fq(F, tf, (1, 1, 1), C_tab, M)
            n4_bad = compute_N4_segre_fq(F, tf, (1, 2, 1), C_tab, M)
            av_good = cyc_galois_avg_abs_sq(n4_good)
            av_bad = cyc_galois_avg_abs_sq(n4_bad)
            # Exact check: on good c, avg |N4|^2 / q^3 <= 29^2 = 841 (Weil bound for dim H^3_c = 29)
            check(av_good <= Fraction(841 * q ** 3, 1), f"F_{q} {pname} good c exceeds 29^2 q^3")
            lines.append(
                f"    q={q:3d} (n={F.n}): "
                f"GOOD c=(1,1,1) avg|N4|^2/q^3 = {float(av_good / Fraction(q**3)):8.4f} (avg/q^4={float(av_good / Fraction(q**4)):.5f}) | "
                f"BAD c=(1,2,1) avg|N4|^2/q^4 = {float(av_bad / Fraction(q**4)):8.4f}"
            )
        lines.append("")

    # ------------------------------------------------------------------
    # 2. Extension-field check over F_7 and F_{49} for the p=7 bad c=(1,1,1) vs good c in F_{49}
    # ------------------------------------------------------------------
    lines.append("## 2. Characteristic 7: c=(1,1,1) (BAD mod 7, pair (5,3)) vs good c in F_{49} (d=3)")
    ok7_111, hits7_111 = check_k4_transversal_over_fbar((1, 1, 1), 3, 7)
    check((not ok7_111) and hits7_111 == 1, "c=(1,1,1) should hit 1 bad line mod 7: (z1,z2)=(5,3)")
    F49 = FiniteField(7, [1, 0, 1])  # u^2 + 1 irreducible mod 7 (7 = 3 mod 4)
    # Find a good c = (1, c2, c3) in F_{49}^* avoiding all 9 bad lines!
    zroots7 = [3, 5, 6]  # all cube roots of -1 already live in F_7!
    c_good49 = None
    for c2 in range(7, 49):  # non-F_7 element
        for c3 in range(1, 49):
            ok = True
            for z1 in zroots7:
                for z2 in zroots7:
                    val = F49.add_tab[1][F49.add_tab[F49.mul_tab[z1][c2]][F49.mul_tab[(z1 * z2) % 7][c3]]]
                    if val == 0:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                c_good49 = (1, c2, c3)
                break
        if c_good49 is not None:
            break
    assert c_good49 is not None
    lines.append(f"  Found transversal c in (F_49^*)^3: c = {c_good49} (poly reps: {[F49.polys[x] for x in c_good49]})")
    for pname, coeffs in [("x^3", [0, 0, 0, 1]), ("x^3+x", [0, 1, 0, 1])]:
        tf49 = F49.tr_fvals(coeffs)
        M49 = compute_M_fq(tf49, 7)
        C49 = compute_C_table_fq(F49, tf49)
        av_bad = cyc_galois_avg_abs_sq(compute_N4_segre_fq(F49, tf49, (1, 1, 1), C49, M49))
        av_good = cyc_galois_avg_abs_sq(compute_N4_segre_fq(F49, tf49, c_good49, C49, M49))
        check(av_good <= Fraction(841 * 49 ** 3, 1), f"F_49 {pname} good c exceeds 29^2 q^3")
        lines.append(
            f"  F_49, f={pname:6s}: BAD c=(1,1,1) avg|N4|^2/q^4 = {float(av_bad / Fraction(49**4)):.4f} | "
            f"GOOD c={c_good49} avg|N4|^2/q^3 = {float(av_good / Fraction(49**3)):.4f} (avg/q^4={float(av_good / Fraction(49**4)):.5f})"
        )
    lines.append("")

    # ------------------------------------------------------------------
    # 3. Exact k = 6 DP checks over F_5 and F_7
    # ------------------------------------------------------------------
    lines.append("## 3. Exact k = 6 path-quadric DP checks over F_5 and F_7 (d = 3)")
    # At k = 6, check exact identity p*N_6 = M^6 + R_6, exact Parseval bound,
    # and compare transversal c vs an explicit tangency-bad c in B_{6,3}!
    # Construct an explicit tangency-bad c for k=6, d=3 over F_5:
    # Need X_1^3 + X_3^3 + X_5^3 = 0 and X_2^3 + X_4^3 + X_6^3 = 0 mod 5, all X_i != 0.
    # Cubes mod 5: 1^3=1, 2^3=3, 3^3=2, 4^3=4.
    # Pick X_odd = (1, 1, 2) -> cubes (1, 1, 3), sum = 5 = 0 mod 5!
    # Pick X_even = (1, 2, 1) -> cubes (1, 3, 1), sum = 5 = 0 mod 5!
    # So X = (1, 1, 1, 2, 2, 1) mod 5!
    # Alternating partial sums u_j = (-1)^{j-1} sum_{r=1}^j (-1)^{r-1} X_r^3:
    # u_1 = X_1^3 = 1
    # u_2 = X_2^3 - u_1 = 1 - 1 = 0 -> oops, gives c_2 = 0! Let's pick X_even = (2, 1, 1) -> cubes (3, 1, 1):
    # u_1 = 1, u_2 = 3 - 1 = 2, u_3 = 1 - 2 = 4, u_4 = 1 - 4 = 2, u_5 = 3 - 2 = 1 (= X_6^3 = 1!). All u_j != 0!
    X_bad6 = (1, 2, 1, 1, 2, 1)
    p = 5
    u_bad6 = [1, 2, 4, 2, 1]
    c_bad6 = tuple((u_bad6[j] * pow((X_bad6[j] * X_bad6[j + 1]) % p, p - 2, p)) % p for j in range(5))
    # Verify grad Q_c(X) == (X_i^2) and Q_c(X) == 0 and sum X_i^3 == 0 mod 5!
    assert sum(pow(x, 3, p) for x in X_bad6) % p == 0
    assert sum(c_bad6[j] * X_bad6[j] * X_bad6[j + 1] for j in range(5)) % p == 0
    grad_Q = [
        (c_bad6[0] * X_bad6[1]) % p,
        (c_bad6[0] * X_bad6[0] + c_bad6[1] * X_bad6[2]) % p,
        (c_bad6[1] * X_bad6[1] + c_bad6[2] * X_bad6[3]) % p,
        (c_bad6[2] * X_bad6[2] + c_bad6[3] * X_bad6[4]) % p,
        (c_bad6[3] * X_bad6[3] + c_bad6[4] * X_bad6[5]) % p,
        (c_bad6[4] * X_bad6[4]) % p,
    ]
    assert grad_Q == [pow(x, 2, p) for x in X_bad6]
    lines.append(f"  Explicit tangency-bad c in B_{{6,3}}(F_5): c_bad6 = {c_bad6}, tangent at X = {X_bad6}")

    for pname, coeffs in [("x^3", [0, 0, 0, 1]), ("x^3+x", [0, 1, 0, 1]), ("x^3+x^2+x", [0, 1, 1, 1])]:
        fvals = poly_values_fp(coeffs, 5)
        M = compute_M_fp(fvals, 5)
        m6 = cyc_pow(M, 6)
        for label, c6 in [("plain (1,1,1,1,1)", (1, 1, 1, 1, 1)), ("c_good (1,2,3,4,1)", (1, 2, 3, 4, 1)), ("c_bad6", c_bad6)]:
            nall = compute_Nall_dp_fp(fvals, c6, 5)
            R6 = compute_R_from_Nall(nall, 5)
            check(cyc_eq(cyc_scale(5, nall[0]), cyc_add(m6, R6)), f"k=6 pN!=M^6+R {pname} {label}")
            avg_R6 = cyc_galois_avg_abs_sq(R6)
            check(avg_R6 <= Fraction(4 ** 2 * 5 ** 7, 1), f"k=6 Parseval bound {pname} {label}")
            avg_N6 = cyc_galois_avg_abs_sq(nall[0])
            lines.append(
                f"  F_5, f={pname:9s}, {label:18s}: "
                f"avg|N_6|^2/5^5 = {float(avg_N6 / Fraction(5**5)):8.3f}, "
                f"avg|R_6|^2/5^7 = {float(avg_R6 / Fraction(5**7)):8.3f} (bound 16.000)"
            )
    lines.append("")

    # ------------------------------------------------------------------
    # 4. Exact Milnor-fibre & Betti-number identity check (k = 4, d = 3: dim H^3_c = 29)
    # ------------------------------------------------------------------
    lines.append("## 4. Exact Milnor-fibre identity & Betti number dim H^3_c(Y, K) = 29 (k = 4, d = 3)")
    # For homogeneous f(x) = x^3, N_4(c) = #Y_0(F_p) + sum_{t=1}^{p-1} #Y_t(F_p) * zeta_p^t
    # where Y_t = {Q_c(x) = 0, x_1^3+x_2^3+x_3^3+x_4^3 = t}.
    # Also check: #Y_0(F_p) = 1 + (p - 1) * #Z(F_p), where Z = {Q_c = 0, sum X_i^3 = 0} in P^3
    # is a smooth curve of genus g = (d - 1)^2 = 4 whenever c is transversal!
    # And check the closed-form Betti number formula against direct residue expansion of Chern classes!
    for p in (5, 11, 13):
        c_test = (1, 1, 1)
        ok_t, hits_t = check_k4_transversal_over_fbar(c_test, 3, p)
        check(ok_t and hits_t == 0, f"c=(1,1,1) should be transversal mod {p}")
        fvals = poly_values_fp([0, 0, 0, 1], p)
        n4 = compute_N4_segre_fp(fvals, c_test, p)
        # Recompute #Y_0(F_p) directly from Z(F_p) in P^3!
        # Wait: n4 from Segre is only equal in Z[zeta_p] (shifted by constant), whereas DP gives exact #Y_t!
        dp4 = compute_Nall_dp_fp(fvals, c_test, p)[0]
        check(cyc_eq(dp4, n4), f"Milnor check DP!=Segre p={p}")
        y0_count = dp4[0]
        # Count points of Z(F_p) in P^3 by dividing (y0_count - 1) by (p - 1)
        check((y0_count - 1) % (p - 1) == 0, f"Y_0 affine cone divisibility p={p}")
        z_pts = (y0_count - 1) // (p - 1)
        # Weil bound on smooth genus-4 curve Z: |#Z(F_p) - (p + 1)| <= 2 * 4 * sqrt(p) = 8 sqrt(p)
        diff = z_pts - (p + 1)
        check(diff * diff <= 64 * p, f"Genus-4 curve Z bound violated at p={p}: #Z={z_pts}")
        # Check sum_{t=0}^{p-1} #Y_t(F_p) == #Y(F_p) == p^3 + p^2 - p (hyperbolic quadric cone in A^4!)
        total_Y = sum(dp4)
        check(total_Y == p ** 3 + p ** 2 - p, f"#Y(F_p) != p^3+p^2-p at p={p}")
        lines.append(
            f"  p={p:2d}, c=(1,1,1) (transversal): #Y={total_Y} (exact p^3+p^2-p), "
            f"#Y_0={y0_count}, #Z(F_p)={z_pts} (p+1={p+1}, |#Z-(p+1)|={abs(diff)} <= 8*sqrt(p))"
        )

    # Exact algebraic check of Betti number formula via exact rational Chern-class series for k=2,4,6,8,10, d=2..6
    lines.append("\n  Exact Chern-class verification of chi_c(Y, K) = -(2*sum_{j=1}^{k-1} (d-1)^j + 1):")
    for d in (3, 4, 5):
        u = d - 1
        row = []
        for m in range(1, 6):
            k = 2 * m
            # Compute [t^{2m-3}] of 2(u+1) / ((1-t)^2 (1+t) (1+ut)) via exact integer series!
            # Series of 1/(1-t)^2 is (j+1) t^j
            # Multiply by 1/(1+t) -> (-1)^j, then by 1/(1+ut) -> (-u)^j
            deg = 2 * m - 3
            if deg < 0:
                chi_Z = 0
            else:
                # convolve a[j] = j+1 with b[j] = (-1)^j then c[j] = (-u)^j
                s1 = [sum((i + 1) * ((-1) ** (j - i)) for i in range(j + 1)) for j in range(deg + 1)]
                s2 = [sum(s1[i] * ((-u) ** (j - i)) for i in range(j + 1)) for j in range(deg + 1)]
                chi_Z = 2 * (u + 1) * s2[deg]
            chi_Yinf = 2 * m
            chi_c = 1 - d * (chi_Yinf - chi_Z)
            closed = -(2 * sum(u ** j for j in range(1, k)) + 1)
            check(chi_c == closed, f"Betti formula mismatch d={d} k={k}: {chi_c} vs {closed}")
            row.append(f"k={k}:{-chi_c}")
        lines.append(f"    d={d}: " + ", ".join(row))

    lines.append(f"\nTOTAL FAILURES: {failures}")
    out_text = "\n".join(lines) + "\n"
    print(out_text)
    out_path = Path(__file__).resolve().parent / "t3_ext_and_betti_out.txt"
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(out_text)
    assert failures == 0


if __name__ == "__main__":
    main()
