"""
T1: Exact validation of the Artin-Schreier path-quadric engine in Z[zeta_p].
All checks are exact integer / cyclotomic-ring / Fraction comparisons (zero floats).
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
    compute_Nall_brute_fp,
    compute_Nall_dp_fp,
    compute_R_from_Nall,
    compute_S_from_Nall,
    cyc_add,
    cyc_eq,
    cyc_galois_avg_abs_sq,
    cyc_mul,
    cyc_pow,
    cyc_scale,
    cyc_sub,
    cyc_zeta,
    poly_values_fp,
)


def main() -> None:
    lines: list[str] = []
    failures = 0

    def check(cond: bool, msg: str) -> None:
        nonlocal failures
        if not cond:
            failures += 1
            lines.append(f"FAIL: {msg}")

    # 1. DP vs brute force + exact identity p*N_k = M^k + R_k + exact Galois-avg Parseval
    polys = [
        ("x^3", [0, 0, 0, 1]),
        ("x^3+x", [0, 1, 0, 1]),
        ("x^3+x^2+2x+1", [1, 2, 1, 1]),
        ("x^5+x+3", [3, 1, 0, 0, 0, 1]),
    ]
    dp_cases = 0
    for p in (5, 7):
        for name, coeffs in polys:
            fvals = poly_values_fp(coeffs, p)
            M = compute_M_fp(fvals, p)
            c_lists = [
                (1,),
                (2,),
                (1, 1),
                (1, 2),
                (1, p - 1),
                (1, 1, 1),
                (1, 2, 3),
                (1, 2, 1),
                (1, 1, p - 2),
            ]
            for c in c_lists:
                k = len(c) + 1
                dp = compute_Nall_dp_fp(fvals, c, p)
                br = compute_Nall_brute_fp(fvals, c, p)
                for s in range(p):
                    check(dp[s] == br[s], f"DP!=brute p={p} {name} c={c} s={s}")
                # Check sum_s Nall[s] == M^k in Z[zeta_p]
                s0 = compute_S_from_Nall(dp, 0, p)
                mk = cyc_pow(M, k)
                check(cyc_eq(s0, mk), f"S(0)!=M^k p={p} {name} c={c}")
                # Check p * N_k == M^k + R_k in Z[zeta_p]
                R = compute_R_from_Nall(dp, p)
                lhs = cyc_scale(p, dp[0])
                rhs = cyc_add(mk, R)
                check(cyc_eq(lhs, rhs), f"pN!=M^k+R p={p} {name} c={c}")
                # Exact Parseval check on Galois average: avg |S(h)|^2 <= p^{k+1}
                for h in range(1, p):
                    sh = compute_S_from_Nall(dp, h, p)
                    avg_sq = cyc_galois_avg_abs_sq(sh)
                    check(avg_sq <= Fraction(p ** (k + 1), 1), f"Parseval avg p={p} {name} c={c} h={h}")
                # Exact Parseval bound on R: avg |R|^2 <= (p-1)^2 * p^{k+1}
                avg_R_sq = cyc_galois_avg_abs_sq(R)
                check(avg_R_sq <= Fraction((p - 1) ** 2 * p ** (k + 1), 1), f"R bound p={p} {name} c={c}")
                dp_cases += 1

    lines.append(f"1. DP vs brute + exact identity pN=M^k+R + Parseval avg: {dp_cases} cases, failures={failures}")

    # 2. Exact closed forms for k=2, k=3, and Segre k=4 over F_p
    cf_cases = 0
    for p in (5, 7, 11):
        for name, coeffs in polys:
            fvals = poly_values_fp(coeffs, p)
            M = compute_M_fp(fvals, p)
            t0 = cyc_zeta(p, fvals[0])
            t0_sq = cyc_zeta(p, 2 * fvals[0])
            C_tab = compute_C_table_fp(fvals, p)

            # k = 2
            for c1 in (1, 2, p - 1):
                dp2 = compute_Nall_dp_fp(fvals, (c1,), p)[0]
                cf2 = cyc_sub(cyc_scale(2, cyc_mul(t0, M)), t0_sq)
                check(cyc_eq(dp2, cf2), f"N2 closed form p={p} {name} c1={c1}")
                cf_cases += 1

            # k = 3: N_3 = t0 * M^2 + (M - t0) * C(-c1/c2)
            for c1, c2 in ((1, 1), (1, 2), (1, p - 1), (2, 3)):
                dp3 = compute_Nall_dp_fp(fvals, (c1, c2), p)[0]
                lam = (-c1 * pow(c2, p - 2, p)) % p
                cf3 = cyc_add(
                    cyc_mul(t0, cyc_mul(M, M)),
                    cyc_mul(cyc_sub(M, t0), C_tab[lam]),
                )
                check(cyc_eq(dp3, cf3), f"N3 closed form p={p} {name} c={(c1, c2)}")
                cf_cases += 1

            # k = 4: Segre formula vs DP
            for c in ((1, 1, 1), (1, 2, 1), (1, 2, 3), (1, 1, p - 2), (2, 3, 4 % p or 1)):
                dp4 = compute_Nall_dp_fp(fvals, c, p)[0]
                sg4 = compute_N4_segre_fp(fvals, c, p, C_tab, M)
                check(cyc_eq(dp4, sg4), f"N4 Segre!=DP p={p} {name} c={c}")
                cf_cases += 1

    lines.append(f"2. Closed forms N2, N3, and Segre N4 vs DP (p=5,7,11): {cf_cases} cases, failures={failures}")

    # 3. Validate FiniteField extension Segre N_4 against direct brute force over F_9 (d=5, 3 nmid 5)
    # F_9 = F_3[u] / (u^2 + 1)
    F9 = FiniteField(3, [1, 0, 1])
    ext_cases = 0
    for name, coeffs in [("x^5", [0, 0, 0, 0, 0, 1]), ("x^5+x+1", [1, 1, 0, 0, 0, 1])]:
        tf = F9.tr_fvals(coeffs)
        for c in ((1, 1, 1), (1, 2, 1), (1, 3, 4), (1, 3, 7)):
            # Direct brute force over F_9^4 (6561 points)
            brute = [0] * 3
            c1, c2, c3 = c
            mul = F9.mul_tab
            add = F9.add_tab
            for x1 in range(9):
                t1 = tf[x1]
                for x2 in range(9):
                    q12 = mul[c1][mul[x1][x2]]
                    t12 = t1 + tf[x2]
                    for x3 in range(9):
                        q123 = add[q12][mul[c2][mul[x2][x3]]]
                        t123 = t12 + tf[x3]
                        c3x3 = mul[c3][x3]
                        for x4 in range(9):
                            if add[q123][mul[c3x3][x4]] == 0:
                                brute[(t123 + tf[x4]) % 3] += 1
            sg = compute_N4_segre_fq(F9, tf, c)
            check(cyc_eq(brute, sg), f"F9 Segre!=brute {name} c={c}")
            ext_cases += 1

    lines.append(f"3. FiniteField F_9 Segre N4 vs brute force (d=5): {ext_cases} cases, failures={failures}")
    lines.append(f"TOTAL FAILURES: {failures}")

    out_text = "\n".join(lines) + "\n"
    print(out_text)
    out_path = Path(__file__).resolve().parent / "t1_validate_out.txt"
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(out_text)
    assert failures == 0


if __name__ == "__main__":
    main()
