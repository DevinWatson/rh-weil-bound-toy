# E: exact L-functions of the fibre sums (Claim B tests)

Started 2026-11-20 15:01Z, finished about 15:30Z. This is about character sums over finite fields, where the bound is Weil's theorem of 1948. Nothing here concerns the Riemann Hypothesis for the integers.

All code and data: `./round3/compute/NUM/` (`ffl.py` engine, `validate.py` / `validate_out.txt`, `cond.py`, `predicted.py`, `run.py` with `configs1/2/3.py` and `results1/2/3.jsonl`, `analyze.py` with `analysis1/2/3.txt`, `compare.py` / `predicted_vs_observed.txt`).

## 0. Summary

- CHECKED. For every case where the L-series terminated inside the reachable range, L(T) = exp((-1)^(k+1) sum S_h(n) T^n / n) is an exact polynomial in Z[omega][T] with constant term 1, and its degree equals the Euler-characteristic number D_k computed by the stationary-phase bookkeeping of Claim B (my own bookkeeping, `predicted.py`, and independently the formulas of reports B and C). Cases: f = x-1 for k = 2, 3, 4 (D = 2, 2, 5; at q = 3 and q = 9), f = x^3-x+1 at k = 2 (D = 10 = d^2+1, three exact zero coefficients beyond).
- CHECKED. The hypothesis of Claim B is NOT necessary for polynomiality in the cases tested: with f = x-1 and c_1 = -c_2 (k = 3), c = (1,1,-1) and (1,-1,1) (k = 4), all c_i = 1 (k = 5, 6), L(T) is still an exact polynomial, of degree 1, 4, 3, 6, 11, respectively. These degrees are also what the same bookkeeping predicts when points coincide (Z meets Sigma_i, so the lost drops are subtracted). No ratio was found anywhere.
- CHECKED/limit. For d = 3 the degrees D_3 = 32, D_4 = 109 are far beyond the reachable n (14). Those cases show only that the series has not terminated in 13 to 14 terms. Nothing is claimed for them. Likewise f = x-1 at k = 5 (predicted D = 7, equal to the reachable n at q = 9) and k = 6, 7.
- Important caveat (OPEN, not decidable by this data): a polynomial L only says that numerator minus denominator has no leftover. It does not prove H^(k+1) = 0, because a class in degree k+1 could cancel an equal eigenvalue in degree k. What the data supports: the degree equals the Euler-characteristic prediction in each case; cancellation would require exact coincidences of Frobenius eigenvalues across different degrees.
- HINT (floating roots, and I used purity-type language only to read the data): in every terminated case all reciprocal roots have |beta| <= q^(k/2), below the q^((k+1)/2) that Claim A uses.

## 1. Method (what was computed)

Setting: p = 3, base field F_q with q = 3^e (e = 1, 2), fibre over F_Q, Q = q^n. t(y) = chi_Q(f(y)), psi(x) = omega^(Tr_(F_Q/F_3) x), omega = exp(2 pi i / 3). g_1 = t, g_(j+1)(y) = t(y) sum_x g_j(x) psi(h c_j x y), S_h(n) = sum_y g_k(y).

- Field F_(3^m), m = e n, from a primitive polynomial found by search; log/exp tables built by block doubling with matrix multiplication; trace table from conjugate sums (checked to land in F_3). Elements of F_q inside F_(q^n): gamma = a fixed root of a fixed primitive polynomial of degree e (so the embedding is consistent across n); c_i = gamma^(cexp_i), h = gamma^(hexp). For q = 3, gamma = -1.
- The transform x -> sum_x g(x) psi(a x y): psi(a x y) = omega^(x^T B_a y) with B_a the matrix of the trace form of a; a fast 3-point DFT on each of the m digit axes, then a permutation u(y) = B_a y. Cost about Q m.
- Exact arithmetic: values in Z[omega] as pairs (A, B) = A + B omega of int64. Each DFT stage multiplies the largest coordinate by at most 5; before every stage the program checks max coordinate < 2^63/5 and aborts (OverflowError) otherwise, so no silent wrap-around inside the transform. Final sums are done exactly with Python integers (high and low 32-bit halves). I found and fixed one weakness during the run: my first version summed with int64 and an S_h near or above 9.2e18 (k = 6, n = 7, true value about 3e20) would have wrapped silently. Those records were deleted and recomputed with the exact sum; k = 6 results in `results2.jsonl` and `results3.jsonl` are post-fix (n = 14 k = 6 values above 1e20 are visible there).
- L-series: n L_n = sum_(j=1..n) a_j L_(n-j), a_j = (-1)^(k+1) S_j, exact in Q(omega) with Fractions. Polynomial test: trailing exact zeros. Exact Hankel rank (Gaussian elimination in Q(omega)) of the matrix (S_(i+j-1)) as a second, independent check: Hankel rank = number of distinct reciprocal roots with nonzero net multiplicity.
- Predicted degree: my own bookkeeping `predicted.py`: P_1 rank 1 with drops 1 at each root; FT_b(P) has rank equal to the sum of drops, singular at -a/b for each nonzero frequency a at infinity (drop = dimension of that piece) and at 0 with drop r - W; P_(i+1) has full drop at Z (stalk 0) plus the singular points of FT; dim H^1_c(A^1,P) = sum of drops + W - r. In the coincidence case (Z meets the singular set) the drop at the coinciding point is overwritten by the full rank, which is the Euler characteristic with stalk 0 at Z. I consider this predicted number as bookkeeping of the claimed picture, not as an independent proof.

## 2. Validation (CHECKED, `validate.py`, `validate_out.txt`)

- Field sanity at m = 1, 2, 3, 4, 6: trace additive, distributivity, power Q-1 = 1, Frobenius additive, trace equals the sum of conjugates.
- Fast transform against the direct double sum sum_x g(x) omega^(Tr(a x y)) for Q = 3, 9, 27, 81 (random integer g, several a): equal for every y, in Z[omega] exactly.
- chi_Q(f(y)) against z^((Q-1)/2) computed independently.
- S_h against the brute k-fold sum over all x in F_Q^k for: F_3 f = x-1 (k = 2, 3), F_3 f = x^3-x+1 (k = 2), F_9 f = x-1 (k = 3, 4), F_9 f = x^3-x+1 (k = 2), F_27 f = x-1 (k = 2, 3), F_27 f = x^3-x+1 (k = 2): all nine agree exactly. Not covered: brute-force at k >= 5 (the transform is the same code for any k).
- Limit of the validation: the brute force and the fast path share the field tables. The field-axiom checks above are what covers a table error.

## 3. Part 2: general position (CHECKED)

Hypothesis of Claim B checked by `cond.py` in a field containing the roots and the c_i (output `cond_out.txt`, `gen_configs_out.txt`). Degrees terminate inside range only for small degrees.

| f | q | k | c (gamma exponents) | hypothesis | n reached | exact degree D | predicted | note |
|---|---|---|---|---|---|---|---|---|
| x-1 | 3 | 2 | (0) | n/a | 13 | 2 | 2 | L = 1 + (1-w)T - 9w T^2 |
| x-1 | 3 | 3 | (0,0), h = 1 and h = -1 | holds | 13 | 2, 2 | 2 | same degree for both h |
| x-1 | 3 | 4 | (0,0,0) (c_1+c_2+c_3 = 0 in F_3) | holds | 13 | 5 | 5 | L_5 = 59049 w, 8 trailing zeros |
| x-1 | 9 | 3 | (3,2), two h | holds | 7 | 2, 2 | 2 | 5 trailing zeros |
| x-1 | 9 | 4 | (3,4,1), two h | holds | 7 | 5, 5 | 5 | 2 trailing zeros |
| x-1 | 9 | 5 | (3,0,2,1), two h | holds | 7 | not terminated (L_7 != 0) | 7 | needs n = 8 (m = 16, not run) |
| x-1 | 9 | 6 | (2,7,5,5,0), two h | holds | 7 | not terminated | 13 | out of reach |
| x^3-x+1 | 3 | 2 | (0), h = 1 and h = -1 | holds | 13 | 10, 10 | 10 = d^2+1 | 3 trailing zeros; L_10 = -3^10; D = 10 confirms the brief's expected value |
| x^3-x+1 | 3 | 3 | (0,0) | holds | 13 | not terminated | 32 | out of reach |
| x^3-x+1 | 3 | 4 | (0,0,0) | holds | 13 | not terminated | 109 | out of reach |

Notes. (1) For f = x-1 the case k = 5 at q = 3 has no admissible c (all ratios are +-1); that is why q = 9 was used. (2) k = 4 with c = (1,1,1) in char 3 has c_1 + c_2 + c_3 = 0, the sign-statement failure of round two, yet its fibre is concentrated as in Claim B with the generic dimension 5; this is an example where Claim B's hypothesis holds on a set where the round-two sign statement fails, matching remark (b) of the brief. (3) For f = x^3-x+1 the maximum reachable n is 14 for q = 3 (field 3^14, 4.8 million points); the degrees 32 and 109 need n above 32.

## 4. Part 3: bad coefficients (CHECKED where terminated)

| f | k | c | hypothesis | n | L(T) | degree | predicted (with coincidence) |
|---|---|---|---|---|---|---|---|
| x-1 | 3 | (1,-1) | fails (rho_2 = 1) | 14 | 1 + 3T, exact polynomial | 1 | 1 |
| x-1 | 4 | (1,1,-1) | fails (rho_3 = 1) | 14 | polynomial | 4 | 4 |
| x-1 | 4 | (1,-1,1) | fails (rho_2, rho_3 hits) | 14 | polynomial | 3 | 3 |
| x-1 | 5 | (1,1,1,1), two h | fails (rho_4 rho_2 = 1) | 14 | polynomial, 8 trailing zeros | 6 | 6 |
| x-1 | 6 | (1,1,1,1,1) | fails | 14 | polynomial, 3 trailing zeros | 11 | 11 |
| x-1 | 7 | all ones | fails | 12 only (int64 margin exceeded at n = 13) | not terminated | not decided | 15 |
| x^3-x+1 | 3 | (1,-1) | fails | 14 | not terminated | not decided | 29 (= 32 - 3, matches report C's m = d) |
| x^3-x+1 | 4 | (1,1,-1), (1,-1,1) | fails | 14 | not terminated | not decided | 100, 91 |
| x^3-x+1 | 5, 6 | all ones | fails | 14 | not terminated | not decided | 356, 1171 |

Answers to the question asked. In every case tested where the answer is determinable (f = x-1), L(T) is a polynomial even though the hypothesis of Claim B fails: no ratio, no pole. The degree drops compared with the generic value, exactly as the Euler-characteristic bookkeeping with coincidences predicts. The k = 3 case can be done by hand: with t = chi(x-1), S = g^2 chi(c_1 c_2) sum_(x != 0) chi(x-1) psi(h (c_1+c_2) x), g the quadratic Gauss sum; for c_1 + c_2 = 0 only the constant term -chi(-1) remains (one eigenvalue g^2-size), for c_1 + c_2 != 0 an extra term psi(s) chi(s) g appears (two eigenvalues): degrees 1 and 2, which is what was computed (PROVED by this hand computation, using only the evaluation of the Gauss sum modulus implicitly for interpretation, not for the degree count). The 'no ratio found' statement does not mean H^(k+1) = 0 (section 0 caveat).

No Pade/Hankel ratio search was needed, because the cases where the series terminated are polynomials; for the non-terminated cases the Hankel test with N = 13 or 14 terms could only detect recurrences of order up to 6 or 7 and all reported full rank: nothing detected, nothing excluded.

## 5. Part 4: comparison with reports B and C (read at the end; both existed)

- Report B: D_k = r_(k+1) - eps_k, giving D_2 = d^2+1, D_3 = d^3+2d-1, D_4 = d^4+3d^2+1, D_5 = d^5+4d^3+3d-1, D_6 = d^6+5d^4+6d^2+1. Agreement with my independently coded bookkeeping and with the data: d = 1 gives 2, 2, 5, 7, 13: data 2, 2, 5 (terminated), my predicted 7, 13 (not reachable); d = 3 gives 10 (data, exact), 32, 109, 359 (my predicted values for generic c: 32, 109, 359; not reachable). Agreement on all comparable numbers. Report B's Hankel ranks 2, 2, 5 and "1 and 6" for k = 3 with rho_2 = 1 and k = 5 all ones are reproduced here, and I add exact polynomial degrees (not only ranks), more terms (13 or 14 against 13) and q = 9 data.
- Report C: D_3 = d^3+2d-1-m with m the number of coincidences. My predicted 29 for f = x^3-x+1, c = (1,-1) equals 32 - 3 (m = d = 3); at d = 1, m = 1 the exact degree is 1 ( = 2 - 1). Agreement.
- Mismatch: none found.

## 6. Part 5: reciprocal roots (HINT, floating)

From the exact coefficients, reciprocal roots by numpy, only in terminated cases: largest |beta| as q^(w/2), w = 2 log|beta| / log q.

- x-1, k = 2: both w = 2 (|beta| = q). x^3-x+1, k = 2: all 10 roots w = 2. (Pure of weight k.)
- x-1, k = 3: w = 3 and w = 2. k = 3 with c_1 = -c_2: w = 2.
- x-1, k = 4: all 5 roots w = 4 (generic and sum-zero); bad cases 4, 3 roots all w = 4.
- k = 5 (all ones, bad): w up to 5, down to 4. k = 6 (all ones): w up to 6, down to 5. k = 5 generic at q = 9: all 7 roots w = 5, but this series has not been shown to terminate, so this is only consistent with a degree-7 polynomial.
- Largest modulus overall is q^(k/2), below the q^((k+1)/2) used in Claim A. Weight language here is interpretation of data, not used in any proof.

## 7. What was covered and what was not

Covered: p = 3; q = 3 (n up to 14 for k <= 6, n up to 12 for k = 7) and q = 9 (n up to 7); f = x-1 and f = x^3-x+1 (irreducible cubic, roots in F_27); h = 1, -1 (q = 3) and h = 1, gamma^3 (q = 9); k = 2 to 7. Exact transform validated against direct sums (Q <= 81) and brute k-fold sums (k <= 4, Q <= 27).

Not covered: any f of degree 3 beyond k = 2 (degree too large), any case that needs n > 14; q = 27 (not run, only n <= 4 reachable, useless for degrees); f = x-1 at k = 5 with n = 8 (field 3^16, memory beyond my cap); odd roots of ratio type R' for d = 3 (needs c in F_27 and more terms); all p other than 3; no check of vanishing of H^j for j != k separately from the L-function; no test of Claim A itself.

Statement-level verdict on Claim B from this data: no counterexample found. The structural prediction (degree = Euler characteristic of the claimed irreducible picture, including the coincidence shifts) holds in every terminated case, with exact integers. This supports the picture, it does not prove it, and for d >= 3 beyond k = 2 it is untested.
