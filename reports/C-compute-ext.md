# C: independent implementation and extension fields (agent C)

Date 2026-11-20. Code and outputs in `remark-review-20261120/toy-case/compute/C/`. Everything labelled CHECKED comes from exact
integer arithmetic (numpy integer tables and Python ints; no floating point anywhere; the decimals printed beside exact fractions
are exact integer long division, display only). Nothing here says anything about the Riemann Hypothesis for the integers.
The Weil bound itself is a theorem (Weil 1948); this report tests only the footnote-3 route.

Files: `ff.py` (fields, N_k), `u2.py`/`u2_out.tsv`, `u3.py`/`u3_validation.txt`/`N_table.tsv`, `u4.py`/`u4_out.txt`, `u5.py`/`u5_out.tsv`,
`u6.py`/`crosscheck.tsv`, `compare_B.py`/`compare_B_out.txt`, `scan_N4_to_499.tsv`, `scale.py`/`scale_out.txt`, `special.py`/`special_out.txt`.

## Bottom line

1. The field code and the sums are correct (U1-U3): 128 independent comparisons, 0 mismatches; the trace recurrence holds for every n.
2. k = 2 and k = 3: N is an explicit polynomial in M, t(0) and C. In the generic case every coefficient of (-1)^(k-1) N in terms of n-th powers is
   positive (PROVED by algebra, CHECKED for every n). This sign comes from the product structure of these small cases, not from any cohomological
   input. It FAILS for the odd cubic f = x^3 - x (t(0) = 0): N_3 = M*C has coefficients of both signs.
3. k = 4 (the first case where the route has content): the sign needed is not visible in the data: N_4 takes both signs over primes (a single value
   proves nothing about coefficients), and for p = 3 its dominant term is +q^2, the wrong sign (HINT level). Its size is at least q^(3/2) on the data and is mostly carried by the single fibre c = 1 of an exact convolution
   identity (CHECKED), which is a non-generic locus. For primes up to 499 the mean of N_4^2/p^3 stays bounded, about 3 to 9, no growth like p.
4. U6: 47 of 47 values agree with agent B's table (plus 42 more from my larger scan); no mismatch.
5. Status of the footnote-3 route from this agent's data: the sign claim for k >= 4 is OPEN at best and contradicted for p = 3, k = 4 by the data
   as described (HINT level: 6 values of n, one prime).

## U1. Fields (CHECKED)

`ff.py`: F_{p^n} as base-p digit vectors, a primitive polynomial found by exhaustive search (x must have exact order q-1), exp/log tables, then
full addition, negation, multiplication and inverse tables (int32). chi(y) = +1 if log y is even, -1 if odd, 0 at 0. F_p embeds as codes 0..p-1.
t = chi(f(.)) for f with coefficients in F_p. Fields built: 3^n (n <= 6), 5^n (n <= 4), 7^n (n <= 3).

## U2. M_n and the trace recurrence (CHECKED: u2.py, u2_out.tsv)

For f = x^3+x+1 and f = x^3-x (discriminants -31 and 4, so good at p = 3, 5, 7), M_n = sum over F_{p^n} of t. With y^2 = f(x) an elliptic curve and
alpha + conj(alpha) = -M_1, alpha*conj(alpha) = p, M_n = -(alpha^n + conj(alpha)^n) = -s_n, and s_n = s_1 s_{n-1} - p s_{n-2}, s_0 = 2, s_1 = -M_1. Hence
**M_n = -M_1 M_{n-1} - p M_{n-2}, M_0 = -2.**
Checked for all 26 (p, f, n) with p^n <= 729: 0 failures; also exact Hasse-Weil M_n^2 <= 4 p^n for all; M_1 re-derived table-free by Euler's criterion.
Examples: p = 5, x^3+x+1: M_1..M_4 = 3, 1, -18, 49. p = 3, n = 6: M = 54 (both cubics; note x^3 - x vanishes identically on F_3 so M_1 = 0).
CITED: Hasse (1933-36), Weil (1948): for a smooth projective genus-1 curve over F_p, #C(F_{p^n}) = p^n + 1 - alpha^n - conj(alpha)^n, |alpha| = sqrt p.

## U3. N_k by solving for a variable (CHECKED: u3.py, u3_validation.txt, N_table.tsv)

Method (not a dynamic programme): Q = x_2 (c_1 x_1 + c_2 x_3) + c_3 x_3 x_4 + ... . For x_2 != 0 solve x_1 = -(c_2 x_2 x_3 + ... + c_{k-1} x_{k-1} x_k)/(c_1 x_2) and
sum over x_2 != 0, x_3..x_k; for x_2 = 0, x_1 is free and the rest is t(0) * M * N_{k-2}(c_3, ...). Vectorised over x_3..x_k.
Validation: fast vs brute force over F_q^k vs a table-free brute force with plain mod-p arithmetic and Euler's criterion (prime q), for q in {3,5,7,9},
both cubics, k = 2..5 where q^k <= 70000, with c = all ones and three random nonzero c vectors each: **128 comparisons, 0 mismatches.**
Table N_2..N_5 (c = all ones) for all fields above (N_5 only where q <= 125) is in `N_table.tsv`. Example: p=3, f=x^3+x+1, n=6: N_4 = 520851.

## U4. k = 2, 3 and the sign pattern (PROVED + CHECKED: u4.py, u4_out.txt)

Notation: t0 = t(0) = eps^n with eps = chi_p(f(0)) (f(0) in F_p); C_n = sum_x t(x) t(-x); c = all ones.

* **k = 2 (PROVED):** x_1 x_2 = 0 means x_1 = 0 or x_2 = 0, so N_2 = 2 t0 M - t0^2. With M = -s_n(alpha):
  -N_2 = 2 eps^n (alpha^n + conj(alpha)^n) + (eps^2)^n. Every coefficient (2, 2, 1) is positive when eps != 0. For x^3-x, t0 = 0 and N_2 = 0.
* **k = 3 (PROVED):** Q = x_2 (x_1 + x_3). x_2 = 0 gives t0 M^2. x_2 != 0 gives x_1 = -x_3 and sum_{x_2 != 0} t(x_2) * C = (M - t0) C. So
  **N_3 = t0 M^2 + (M - t0) C.** (General c: C becomes D(-c_2/c_1) with D(c) = sum t(x) t(cx).)
* C through two genus-1 curves (generic f, PROVED + CITED): with f = x^3 + a x + b, f(x) f(-x) = G(x^2), G(u) = b^2 - u (u+a)^2. Then
  C_n = sum_u chi(G(u)) + sum_u chi(u G(u)) = -s_n(E1) - s_n(E2) - lambda^n, lambda = chi_p(-1), where E1: y^2 = G(u) (cubic) and E2: y^2 = u G(u)
  (quartic, genus 1; two points at infinity iff the leading coefficient -1 is a square, giving the lambda^n term). CITED as for U2.
  Hence for eps != 0 and G, uG squarefree:
  N_3 = eps^n s_n(alpha)^2 + s_n(alpha) (S_n + lambda^n) + eps^n (S_n + lambda^n), S_n = s_n(E1) + s_n(E2).
  Expanding the products of power sums (s(alpha)^2 = alpha^2n + conj^2n + 2p^n, s(a)s(b) = sum over the four products, and so on), **every coefficient is a
  positive integer**: (-1)^(k-1) N_3 = N_3 is a positive combination of n-th powers of fixed complex numbers (eps*alpha^2, eps*p, alpha*gamma, lambda*alpha, eps*gamma, ...).
  M^3 = -s_n(alpha)^3 has the opposite sign (negative coefficients); for k = 2, N_2 has negative and M^2 positive coefficients. So in k = 2, 3 the two families have
  opposite signs, as the note says. CHECKED for every n available, p in {3,5,7}, f = x^3+x+1 (all of: t0 = eps^n; N_2; N_3 formula; C formula; spectral form of N_3): 0 failures.
* **Where it fails (CHECKED):** f = x^3 - x is odd, so t(-x) = chi(-1) t(x), t0 = 0 and C_n = lambda^n (q - 3) exactly (verified for every n). Then N_3 = M*C =
  -(alpha^n + conj(alpha)^n) (lambda^n p^n - 3 lambda^n): the coefficient of (lambda p alpha)^n is -1 and of (lambda alpha)^n is +3 (mixed signs). E.g. p=5: N_3 = 4, 132, -2684, 8708 for n = 1..4.
  So even at k = 3 the "definite sign" depends on f(0) != 0 and on f(x) f(-x) being generic; it is not a property of the construction.
* The positivity for k = 2, 3 follows from the factorisation of the sums, not from Bertini or middle cohomology. It says nothing about k >= 4.

## U5. k = 4 (CHECKED: u5.py, u5_out.tsv)

Reading of the question: n is the extension degree, field size Q = p^n, so N_n^2 / q^(3n) means N^2 / Q^3 and N^2 / Q^4. Selected exact data (full table with exact fractions in `u5_out.tsv`):

| p | f | n | N_4 | N^2/Q^3 | N^2/Q^4 |
|---|---|---|-----|---------|---------|
| 3 | x^3+x+1 | 2..6 | 195, 553, 6147, 43681, 520851 | 52.16, 15.54, 71.10, 132.97, 700.24 | 5.80, 0.575, 0.878, 0.547, 0.960 |
| 3 | x^3-x | 2..6 | 132, 384, 5796, 59520, 466500 | 23.90, 7.49, 63.21, 246.89, 561.72 | 2.66, 0.277, 0.780, 1.016, 0.771 |
| 5 | x^3+x+1 | 1..4 | 21, 257, 1722, 174593 | 3.53, 4.23, 1.52, 124.86 | 0.706, 0.169, 0.012, 0.200 |
| 5 | x^3-x | 1..4 | 0, 256, 9504, -42336 | 0, 4.19, 46.25, 7.34 | 0, 0.168, 0.370, 0.012 |
| 7 | x^3+x+1 | 1..3 | 53, 129, 24878 | 8.19, 0.141, 15.34 | 1.170, 0.003, 0.045 |
| 7 | x^3-x | 1..3 | 28, 1056, 21724 | 2.29, 9.48, 11.69 | 0.327, 0.193, 0.034 |

Answer: **N_4 is of size q^(3n/2) or larger in nearly every row** (N^2/Q^3 is at least 1.5 in 22 of the 26 rows; the four exceptions are 0.04 at p=3, n=1, two rows with N_4 = 0 at n=1, and 0.14 at p=7, n=2; maximum 700 at p=3, n=6, and 124.86 at p=5, n=4), and for p = 3 it is of size Q^2
(N^2/Q^4 about 0.55 to 1.0). It is never smaller than the middle-weight size with a constant near 1 in a way that would suggest cancellation below q^(3/2).
Extra exact identity (PROVED by the substitution y = x_2 + x_4, so that Q = x_1 x_2 + x_3 y, then cases x_2, y zero or not; CHECKED on all 26 rows, 0 failures):
N_4 = sum_{c != 0} D(c) (D(-1-c) - t0^2) + t0^2 M (M - t0) + t0 M (C - t0^2) + t0^2 M^2, with D(c) = sum_x t(x) t(cx) = point count of a genus-2 curve
y^2 = f(x) f(cx) (degenerate at c = 1, where D(1) = q - #zeros of f, about q).
Consequence (PROVED for the main term, HINT for the rest): in characteristic 3 the values c and -1-c coincide at c = 1, so N_4 contains (q-z)(q-z-t0^2) = q^2 + O(q) with sign +. That explains N_4 ~ +q^2 for p = 3.
For p >= 5 the same fibre gives D(1) D(-2) of size q * sqrt q. (`special.py`: for 22 to 25 primes per band the c = 1, -2 terms carry most of the mean square, e.g. band 351-500: mean N^2/p^3 = 5.17,
of which the special terms alone give 4.81.) HINT: much of N_4's size comes from a non-generic fibre, not from the middle cohomology of a generic fibre.
Sign (CHECKED data, HINT interpretation): over primes up to 499, N_4 > 0 for 59 of 93 (x^3+x+1) and 46 of 94 (x^3-x, 3 zeros); N_4 < 0 for 34 and 45. A single n gives no coefficient test, but
for p = 3, N_4 > 0 for all six n and N_4/q^2 is 0.94, 0.74, 0.98 for n = 4, 5, 6: a dominant term near +p^(2n). The pattern "(-1)^(k-1) N = -N_4 positive combination" would require that term to be negative. OPEN
whether other p show the same; p = 3 is the one where the data are clean (6 values only, so HINT).
Primes (U6 extension, `scan_N4_to_499.tsv`, `scale_out.txt`): mean N_4^2/p^3 per band of primes: x^3+x+1: 2.59 (3-30), 3.86, 4.18, 9.15, 5.17 (351-500); x^3-x: 6.33, 3.00, 4.39, 7.07, 5.56.
Maximum 42.25. Mean N^2/p^4 falls from 0.28 to 0.012. So over primes |N_4| is of order p^(3/2) with rms constant about 2 to 3: not smaller than q^(3/2), not growing to q^2. The k = 5 table (`u5_out.tsv`, last block) is similar (N_5^2/Q^4 from 0 to 411).

## U6. Cross-check over prime fields (CHECKED: crosscheck.tsv, compare_B.py)

`crosscheck.tsv` (columns f, p, M, N_4) written first from my own code: f = x^3+x+1 at all odd primes up to 97 except 31 (disc -31), f = x^3-x at all odd primes up to 97: 47 rows.
Then compared with `compute/B/n4_table.tsv`: **47 of 47 agree, 0 mismatches** (`compare_B_out.txt`). My larger scan to p = 499 overlaps B's table on 42 further rows (primes 101-199): 0 mismatches.
B's file also has f = x^3+2x+5 and x^5+x+1, x^5-5x+3, which I did not compute.

## Labels summary

* PROVED: N_2, N_3 closed forms; positivity of all coefficients of (-1)^(k-1) N_k for k = 2, 3 in the generic case (modulo the CITED point counts); failure for odd f (x^3 - x); the k = 4 convolution identity and the +q^2 term in characteristic 3.
* CITED: Hasse 1933/36 and Weil 1948 (genus-1 point counts via Frobenius eigenvalues).
* CHECKED: all identities and tables above, with scripts and files named.
* HINT/OPEN: that N_4 has the wrong sign in general; interpretation of the special fibre as the source of N_4's size; k >= 5; whether the route can give a proof at all (not decided here).
* Not tested: other quadric coefficient vectors for the sign question (only c = all ones in the tables; random c only for validating the algorithm), cubics other than two, fields beyond the sizes stated.
