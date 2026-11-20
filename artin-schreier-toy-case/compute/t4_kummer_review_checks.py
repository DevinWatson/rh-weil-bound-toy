"""
T4: Exact integer verification of the two new mathematical findings from our review
of the Kummer toy-case study:

1. Closing K4T's open exception (X2) (f(x) = x^d - a, a != 0, d odd, p nmid 2d):
   On the (mu_d x mu_d)-quotient T'' = A^2_{(w, s)} with sheaf L_{chi((w-a)(sw-a))}:
     - sum_{w in F_p} chi((w-a)(sw-a)) = -chi(s)   for all s != 0, 1;
     - sum_{w in F_p} chi((w-a)(-a))   = 0         at s = 0;
     - sum_{w in F_p} chi((w-a)^2)     = p - 1     at s = 1;
     - sum_{s != 1} sum_w chi((w-a)(sw-a)) = +1    (no p-term => H^3_c(T'' - T''_1) = 0);
     - sum_{s in F_p} sum_w chi((w-a)(sw-a)) = p   (exact trace of H^2_c(T'') = Q_l(-1)).
   And on the full space T = A^2_{(x, r)} with f(x) = x^d - a:
     - sum_{x, s in F_p} chi((x^d-a)(s x^d-a)) = p,
     - sum_{x in F_p, s != 1} chi((x^d-a)(s x^d-a)) = #{x in F_p : x^d = a} (no p-term!).

2. Resolving K4C's unexplained coincidence (iv) (K4C-k4-computation.md, lines 123 & 141):
   For f in F_3[x] and c in (F_9^*)^3 with i^2 = -1:
     (1, 1, i) -> reverse -> (i, 1, 1)
     (1, 1, i) -> scale by (-i) -> (-i, -i, 1) -> Frobenius (x -> x^3) -> (i, i, 1) -> reverse -> (1, i, i).
   We check these exact identities in F_9 = F_3[u]/(u^2 + 1) and verify N_4(1,1,i) = N_4(1,i,i) = N_4(i,1,1)
   for all three cubics over F_9 and F_81 via exact quadratic-character Segre evaluation.
"""

from pathlib import Path
from as_core import FiniteField


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def quad_char_fq(F: FiniteField) -> list[int]:
    """Exact quadratic character chi on F_q (q odd): 0 at 0, +1 on squares, -1 on nonsquares."""
    q = F.q
    assert q % 2 == 1
    out = [0] * q
    exp = (q - 1) // 2
    for x in range(1, q):
        r = F.pow(x, exp)
        if r == 1:
            out[x] = 1
        elif r == F.neg_tab[1]:
            out[x] = -1
        else:
            raise AssertionError("Unexpected quadratic character value")
    return out


def kummer_N4_segre_fq(F: FiniteField, fcoeffs: list[int], c: tuple[int, int, int]) -> int:
    """Exact integer N_4 for the Kummer sheaf chi(f(x)) over F_q via Segre formula."""
    q = F.q
    chi = quad_char_fq(F)
    t = [chi[F.eval_poly_fp_coeffs(fcoeffs, x)] for x in range(q)]
    M = sum(t)
    t0 = t[0]
    C = [0] * q
    mul = F.mul_tab
    for r in range(q):
        mul_r = mul[r]
        C[r] = sum(t[x] * t[mul_r[x]] for x in range(q))
    c1, c2, c3 = c
    inv_c1 = F.inv_tab[c1]
    a = F.neg_tab[mul[c3][inv_c1]]
    b = F.neg_tab[mul[c2][inv_c1]]
    add_b = F.add_tab[b]
    mul_a = mul[a]
    return -q + (t0 * t0) * M * M + sum(C[r] * C[add_b[mul_a[r]]] for r in range(q))


def main() -> None:
    lines: list[str] = []
    failures = 0

    def check(cond: bool, msg: str) -> None:
        nonlocal failures
        if not cond:
            failures += 1
            lines.append(f"FAIL: {msg}")

    lines.append("# T4: Exact checks of our two new findings from reviewing toy-case\n")

    # Part 1: K4T exception (X2) quotient identities
    primes = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    cases_x2 = 0
    for d in (3, 5):
        for p in primes:
            if p % d == 0:
                continue
            for a in (1, 2, p - 1):
                # Quotient T'' = A^2_{(w, s)}
                total_w = 0
                off1_w = 0
                for s in range(p):
                    sw = sum(legendre((w - a) * (s * w - a), p) for w in range(p))
                    if s == 0:
                        check(sw == 0, f"T'' s=0 p={p} a={a}: got {sw}")
                    elif s == 1:
                        check(sw == p - 1, f"T'' s=1 p={p} a={a}: got {sw}")
                    else:
                        check(sw == -legendre(s, p), f"T'' s={s} p={p} a={a}: got {sw}")
                        off1_w += sw
                    total_w += sw
                check(off1_w == 1, f"T'' off1 sum p={p} a={a}: got {off1_w}")
                check(total_w == p, f"T'' total sum p={p} a={a}: got {total_w}")

                # Intermediate quotient T' = T / ({1} x mu_d) = A^2_{(x, s)}
                xd = [pow(x, d, p) for x in range(p)]
                r0 = sum(1 for v in xd if v == a)
                total_x = 0
                off1_x = 0
                for s in range(p):
                    sx = sum(legendre((v - a) * (s * v - a), p) for v in xd)
                    total_x += sx
                    if s != 1:
                        off1_x += sx
                check(total_x == p, f"T' total sum p={p} d={d} a={a}: got {total_x}")
                check(off1_x == r0, f"T' off1 sum p={p} d={d} a={a}: got {off1_x} != r0={r0}")
                cases_x2 += 1

    lines.append(f"1. K4T exception (X2) (f(x)=x^d-a) quotient identities (d=3,5; p<=97): {cases_x2} cases, failures={failures}")

    # Part 2: K4C coincidence (iv) symmetry-group check over F_9 and F_81
    F9 = FiniteField(3, [1, 0, 1])  # u^2 + 1 = 0, so i = u (encoded as 3)
    i9 = 3
    assert F9.mul_tab[i9][i9] == F9.neg_tab[1]
    neg_i9 = F9.neg_tab[i9]

    # Check the algebraic orbit in F_9^3:
    c_a = (1, 1, i9)
    # 1) reverse -> (i, 1, 1)
    c_rev = (c_a[2], c_a[1], c_a[0])
    check(c_rev == (i9, 1, 1), "reverse check")
    # 2) scale by -i -> (-i, -i, 1), Frobenius x -> x^3 -> (i, i, 1), reverse -> (1, i, i)
    c_scaled = tuple(F9.mul_tab[neg_i9][x] for x in c_a)
    check(c_scaled == (neg_i9, neg_i9, 1), f"scale check got {c_scaled}")
    c_frob = tuple(F9.pow(x, 3) for x in c_scaled)
    check(c_frob == (i9, i9, 1), f"frob check got {c_frob}")
    c_frob_rev = (c_frob[2], c_frob[1], c_frob[0])
    check(c_frob_rev == (1, i9, i9), f"frob+rev check got {c_frob_rev}")

    # Verify N_4 equality over F_9 and F_81 for the three K4C cubics over F_3:
    # x^3+x+1, x^3-x+1, x^3+x^2+2
    # F_81 = F_3[v]/(v^4 + 2v^3 + 2) (check irreducible & find i with i^2 = -1)
    F81 = FiniteField(3, [2, 0, 0, 2, 1])
    i81 = next(x for x in range(1, 81) if F81.mul_tab[x][x] == F81.neg_tab[1])
    cubics = [
        ("x^3+x+1", [1, 1, 0, 1]),
        ("x^3-x+1", [1, 2, 0, 1]),
        ("x^3+x^2+2", [2, 0, 1, 1]),
    ]
    lines.append("\n2. K4C coincidence (iv) exact symmetry check (F_9 and F_81):")
    for fname, coeffs in cubics:
        vals9 = [kummer_N4_segre_fq(F9, coeffs, c) for c in ((1, 1, i9), (1, i9, i9), (i9, 1, 1))]
        vals81 = [kummer_N4_segre_fq(F81, coeffs, c) for c in ((1, 1, i81), (1, i81, i81), (i81, 1, 1))]
        check(vals9[0] == vals9[1] == vals9[2], f"F9 mismatch {fname}: {vals9}")
        check(vals81[0] == vals81[1] == vals81[2], f"F81 mismatch {fname}: {vals81}")
        lines.append(f"  {fname:10s}: F_9 N_4 = {vals9[0]:4d} (all 3 equal) | F_81 N_4 = {vals81[0]:5d} (all 3 equal)")

    lines.append(f"\nTOTAL FAILURES: {failures}")
    out_text = "\n".join(lines) + "\n"
    print(out_text)
    out_path = Path(__file__).resolve().parent / "t4_kummer_review_checks_out.txt"
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(out_text)
    assert failures == 0


if __name__ == "__main__":
    main()
