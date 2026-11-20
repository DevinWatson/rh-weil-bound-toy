"""
T2: Exhaustive exact map of the k = 4 Artin-Schreier bad locus B_{4,d} over F_p.

Predicted bad lines in P^2_c (from infinity transversality of {Q_c=0} and {sum X_i^d=0}):
    L(zeta_1, zeta_2) : c_1 + zeta_1 * c_2 + zeta_1 * zeta_2 * c_3 = 0,
where zeta_1^d = -1 and zeta_2^d = -1 in F_bar_p.
Over F_p (normalised c_1 = 1), we also check:
  - the universal line c_1 - c_2 + c_3 = 0 (zeta_1 = zeta_2 = -1, exists for every odd d);
  - all F_p-rational bad lines L(zeta_1, zeta_2) with zeta_1, zeta_2 in F_p, zeta_i^d = -1;
  - the special prime p = 7 where c = (1, 1, 1) lies on L(5, 3) for d = 3!

Every check uses exact Fraction arithmetic on the Galois average
    AvgSq(c) = (1/(p-1)) sum_{a=1}^{p-1} |N_4(c; psi_a)|^2.
Under (S_4), AvgSq(c) / p^3 is bounded (by (dim H^3_c)^2 = 29^2 = 841 for d=3),
while a plane in Y carrying a constant sheaf (eigenvalue q^2) makes AvgSq(c) / p^4 -> 1
(or m^2 if m planes collide). Floats appear ONLY in formatted display columns.
"""

from fractions import Fraction
from pathlib import Path
from as_core import (
    compute_C_table_fp,
    compute_M_fp,
    compute_N4_segre_fp,
    cyc_galois_avg_abs_sq,
    poly_values_fp,
)


def fp_bad_lines(d: int, p: int) -> set[tuple[int, int]]:
    """Return set of (c2, c3) in (F_p^*)^2 lying on some F_p-rational line 1 + z1*c2 + z1*z2*c3 = 0 with z1^d = z2^d = -1."""
    zroots = [z for z in range(1, p) if pow(z, d, p) == p - 1]
    bad: set[tuple[int, int]] = set()
    for z1 in zroots:
        for z2 in zroots:
            z12 = (z1 * z2) % p
            inv_z12 = pow(z12, p - 2, p)
            for c2 in range(1, p):
                c3 = (-(1 + z1 * c2) * inv_z12) % p
                if c3 != 0:
                    bad.add((c2, c3))
    return bad


def fp_line_multiplicity(c2: int, c3: int, d: int, p: int) -> int:
    """Number of pairs (z1, z2) in F_p^2 with z1^d = z2^d = -1 and 1 + z1*c2 + z1*z2*c3 = 0."""
    zroots = [z for z in range(1, p) if pow(z, d, p) == p - 1]
    cnt = 0
    for z1 in zroots:
        for z2 in zroots:
            if (1 + z1 * c2 + z1 * z2 * c3) % p == 0:
                cnt += 1
    return cnt


def main() -> None:
    lines: list[str] = []
    lines.append("# T2: Exhaustive k = 4 Artin-Schreier bad-locus scan (exact cyclotomic averages)\n")

    # Part A: Spotlight on p = 7, d = 3, f = x^3 where c = (1, 1, 1) lies on the bad line L(5, 3)!
    p = 7
    fvals = poly_values_fp([0, 0, 0, 1], p)
    C_tab = compute_C_table_fp(fvals, p)
    M = compute_M_fp(fvals, p)
    n4_111 = compute_N4_segre_fp(fvals, (1, 1, 1), p, C_tab, M)
    avg_111 = cyc_galois_avg_abs_sq(n4_111)
    mult_111 = fp_line_multiplicity(1, 1, 3, 7)
    lines.append("## Part A: Spotlight p = 7, f(x) = x^3, plain quadric c = (1, 1, 1)")
    lines.append(f"  Bad-line multiplicity of c=(1,1,1) mod 7: {mult_111}  (unique pair (z1,z2)=(5,3): 1 + 5 + 15 = 21 = 0 mod 7)")
    lines.append(f"  Exact N_4(1,1,1) in Z[zeta_7] (raw counts): {n4_111}")
    lines.append(f"  Exact Galois avg |N_4|^2 = {avg_111}  (= {float(avg_111 / p**4):.4f} * p^4, display float)")
    # Compare with a guaranteed off-bad-locus c mod 7 (if any exists in (F_7^*)^2)
    bad7 = fp_bad_lines(3, 7)
    good7 = [(c2, c3) for c2 in range(1, 7) for c3 in range(1, 7) if (c2, c3) not in bad7]
    lines.append(f"  Number of good (1, c2, c3) in (F_7^*)^2 outside all 9 bad lines: {len(good7)} of 36")
    if good7:
        g2, g3 = good7[0]
        n4_g = compute_N4_segre_fp(fvals, (1, g2, g3), p, C_tab, M)
        avg_g = cyc_galois_avg_abs_sq(n4_g)
        lines.append(f"  Good control c=(1,{g2},{g3}) mod 7 (mult=0): avg |N_4|^2 = {avg_g} (= {float(avg_g / p**3):.4f} * p^3, display float)\n")
    else:
        lines.append("  No F_7-rational good c exists in (F_7^*)^2 (9 lines cover all 36 points; extension F_{49} required!)\n")

    # Part B: Exhaustive scan over ALL (c2, c3) in (F_p^*)^2
    lines.append("## Part B: Exhaustive scan of all (p-1)^2 vectors c = (1, c2, c3) in (F_p^*)^2")
    lines.append("Columns: poly, p, #all, #on_univ (c1-c2+c3=0), #on_Fp_bad, max_off/p^3, mean_off/p^3, mean_univ/p^4, mean_bad_other/p^4 (display floats; exact fractions checked)\n")

    configs = [
        ("x^3", [0, 0, 0, 1], 3, [5, 7, 11, 13, 17, 19, 23, 29, 31]),
        ("x^3+x", [0, 1, 0, 1], 3, [5, 7, 11, 13, 17, 19, 23, 29, 31]),
        ("x^3+x^2+x", [0, 1, 1, 1], 3, [5, 7, 11, 13, 17, 19, 23, 29, 31]),
        ("x^5+x", [0, 1, 0, 0, 0, 1], 5, [7, 11, 13, 17, 19, 23]),
    ]

    for name, coeffs, d, primes in configs:
        for p in primes:
            if p % d == 0:
                continue
            fvals = poly_values_fp(coeffs, p)
            C_tab = compute_C_table_fp(fvals, p)
            M = compute_M_fp(fvals, p)
            bad_set = fp_bad_lines(d, p)

            off_vals: list[Fraction] = []
            univ_vals: list[Fraction] = []
            other_bad_vals: list[Fraction] = []

            for c2 in range(1, p):
                for c3 in range(1, p):
                    n4 = compute_N4_segre_fp(fvals, (1, c2, c3), p, C_tab, M)
                    av = cyc_galois_avg_abs_sq(n4)
                    if (1 - c2 + c3) % p == 0:
                        univ_vals.append(av)
                    elif (c2, c3) in bad_set:
                        other_bad_vals.append(av)
                    else:
                        off_vals.append(av)

            max_off = max(off_vals) if off_vals else Fraction(0)
            mean_off = sum(off_vals, Fraction(0)) / len(off_vals) if off_vals else Fraction(0)
            mean_univ = sum(univ_vals, Fraction(0)) / len(univ_vals) if univ_vals else Fraction(0)
            mean_other = (
                sum(other_bad_vals, Fraction(0)) / len(other_bad_vals)
                if other_bad_vals
                else Fraction(0)
            )

            p3 = Fraction(p ** 3, 1)
            p4 = Fraction(p ** 4, 1)
            other_str = f"{float(mean_other / p4):.4f}" if other_bad_vals else "   n/a"
            lines.append(
                f"  {name:10s} p={p:2d}  all={(p-1)**2:3d}  univ={len(univ_vals):2d}  "
                f"bad_Fp={len(bad_set):3d}  max_off/p^3={float(max_off/p3):7.3f}  "
                f"mean_off/p^3={float(mean_off/p3):6.3f}  mean_univ/p^4={float(mean_univ/p4):7.4f}  "
                f"mean_other_bad/p^4={other_str}"
            )
        lines.append("")

    # Part C: Exact check at larger primes (p = 37..101) for fixed c = (1,2,3) (generic) vs c = (1,2,1) (c1-c2+c3=0)
    lines.append("## Part C: Fixed c comparison across p = 37..101 (f = x^3+x and x^3+x^2+x)")
    primes_big = [37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    for name, coeffs in [("x^3+x", [0, 1, 0, 1]), ("x^3+x^2+x", [0, 1, 1, 1])]:
        ratios_good_p3: list[Fraction] = []
        ratios_bad_p4: list[Fraction] = []
        for p in primes_big:
            fvals = poly_values_fp(coeffs, p)
            C_tab = compute_C_table_fp(fvals, p)
            M = compute_M_fp(fvals, p)
            # Pick a guaranteed off-bad-locus c (1, 2, 3) if not in bad_set, else (1, 2, 4)
            bad_set = fp_bad_lines(3, p)
            c_good = (1, 2, 3) if (2, 3) not in bad_set else (1, 2, 4)
            assert (c_good[1], c_good[2]) not in bad_set
            av_good = cyc_galois_avg_abs_sq(compute_N4_segre_fp(fvals, c_good, p, C_tab, M))
            av_bad = cyc_galois_avg_abs_sq(compute_N4_segre_fp(fvals, (1, 2, 1), p, C_tab, M))
            ratios_good_p3.append(av_good / Fraction(p ** 3, 1))
            ratios_bad_p4.append(av_bad / Fraction(p ** 4, 1))
        mean_good = sum(ratios_good_p3, Fraction(0)) / len(ratios_good_p3)
        max_good = max(ratios_good_p3)
        mean_bad = sum(ratios_bad_p4, Fraction(0)) / len(ratios_bad_p4)
        min_bad = min(ratios_bad_p4)
        max_bad = max(ratios_bad_p4)
        lines.append(
            f"  {name:10s} (15 primes 37..101): "
            f"good c: mean(|N4|^2/p^3)={float(mean_good):.3f}, max={float(max_good):.3f} | "
            f"bad c=(1,2,1): mean(|N4|^2/p^4)={float(mean_bad):.4f}, range=[{float(min_bad):.4f}, {float(max_bad):.4f}]"
        )

    out_text = "\n".join(lines) + "\n"
    print(out_text)
    out_path = Path(__file__).resolve().parent / "t2_k4_bad_locus_out.txt"
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(out_text)


if __name__ == "__main__":
    main()
