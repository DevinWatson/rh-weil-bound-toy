# K4C: exact computation for k = 4 (round two)

Started 2026-11-20 18:21:52Z, finished 2026-11-20 about 18:35Z. Scope: character sums over finite fields only; nothing here concerns the Riemann Hypothesis for the integers. All CHECKED figures are exact integer or rational arithmetic (scripts and outputs in `round2/compute/K4C/`). Floats appear only in lines marked "for reading only". Weights, purity and the Weil bound are used NOWHERE as a step of a proof; where I use them to interpret data I say "(interpretation, uses Weil)".

Notation: p prime, t(x) = chi(f(x)), M = sum t, t0 = t(0), rho = number of roots of f in F_p, C(r) = sum_x t(x) t(r x), tau(r) = a r + b with a = -c3/c1, b = -c2/c1, E(a,b) = sum_r C(r) C(a r + b), S = sum_r C(r).

## Summary

| Item | Result | Label |
|---|---|---|
| E1 | N_4 = -q + t0^2 M^2 + E(a,b) agrees with the direct count in 592 of 592 cases (p in 5,7,11,13; all c in (F_p^*)^3 with c1=1; f = x^3+x+1 and x^3-x+3) | CHECKED |
| E2 | On the line a+b=1 (equivalently c1+c2+c3=0) E = (p-rho)^2 + (rest); this line is the only structured part of the large-E set that survives at larger p. Off the line, 85% of the large values are explained by a "spike term" or by a = -1; b = 0 is a separate, strongly enriched class that is NOT a path quadric | PROVED (line identity), CHECKED (data), conjectures stated with hit rates |
| E3 | The four pieces of E are tabulated for 43 primes p <= 199, three f, four c. S_aa (the genus d-1 traces) carries essentially all of E; the three cross/character pieces are smaller by a factor of about 10 to 1000 in p^2 units; at c1+c2+c3=0 every E is positive and S_aa is positive for every prime | CHECKED |
| E4 | sum_r C(r) = M^2 - t0 M + q t0^2, derived and checked for 315 (f,p) pairs, failures 0 | PROVED, CHECKED |
| E5 | N_4 over F_9, F_81, F_729 for three cubics over F_3 and eight c; the all-ones values 195, 6147, 520851 for x^3+x+1 are reproduced; for c1+c2+c3 != 0 the values are far below q^2 in F_729 | CHECKED |

## E1. The formula for N_4

CHECKED: `compute/K4C/e1.py`, output `e1_out.txt`. For p in {5, 7, 11, 13}, f in {x^3+x+1, x^3-x+3} (squarefree mod p and f(0) != 0 in all eight cases; discriminants -31 and -239), every c = (1, c2, c3) with c2, c3 in F_p^*: N_4 is computed by brute force over all p^4 points of the quadric Q_c = c1 x1 x2 + c2 x2 x3 + c3 x3 x4 = 0 and compared with -p + t0^2 M^2 + sum_r C(r) C(-c3 r - c2). The affine map was also checked symbolically in the script against the stated form -(c3/c1)(r + c2/c3) with explicit modular inverses. 16 + 16 + 36 + 36 + 100 + 100 + 144 + 144 = 592 cases, 0 mismatches. (Here t0^2 = 1 in every case, so the term t0^2 M^2 is M^2.)

## E2. Map of the bad set of E(a,b)

Scripts: `e2.py` (raw lists, `e2_out.txt`), `e2b.py` (raw and centred, `e2b_out.txt`), `e2c.py`/`e2d.py` (predicate enrichment, `e2c_out.txt`, `e2d_out.txt`, console copies `e2c_console.txt`, `e2d_console.txt`), `e2e.py` (spike term, `e2e_out.txt`), `e2f.py` (palindromic c, `e2f_out.txt`). Exact integers/Fractions throughout.

Test families for each p: f = (x-1)(x-2)(x-4); f = (x-1)(x-3)(x-9) (a second three-root cubic, kept as a probe for root-ratio structure; skipped if not squarefree mod p); the lexicographically first irreducible cubic x^3 + a x^2 + b x + c with c != 0 (never has a root, hence f(0) != 0); the quintic x^5 + x + c with smallest c making it squarefree. All have f(0) != 0. Prime sets: the requested 11, 13, 17, 19, 23, 29, 31 (all 28 or fewer (p,f) pairs) and, as an extension to see the trend, 37..101.

### E2.1 Mean term: the raw list is dominated by S^2/p at small p

The brief's criterion |E|/p^2 > 1/2 in `e2.py` flags between 12 and 506 of p(p-1) pairs at p <= 31 (see `e2_out.txt`; for instance all 506 pairs for the quintic at p = 23). The reason is a trivial one. PROVED: since tau is a bijection of F_p, E(a,b) = S^2/p + E_c(a,b), where E_c(a,b) = sum_r (C(r) - S/p)(C(tau r) - S/p), and S = M^2 - t0 M + p t0^2 (E4). For M of size 2 sqrt(p) or more at small p, S^2/p is not small compared with p^2/2; in the quintic p = 23 case it exceeds it. This is a small-p effect (interpretation, uses Weil: S^2/p is about p when |M| <~ sqrt(p) and the quantity (S^2/p)/p^2 then tends to 0 like 1/p). So I report both raw and centred figures; the centred criterion is |E_c| > p^2/2 (tested exactly as 2|p E - S^2| > p^3).

### E2.2 The line a + b = 1 (the c1 + c2 + c3 = 0 locus)

PROVED: with c1 = 1, c2 + c3 = -1 gives tau(1) = -c3 - c2 = 1, i.e. a + b = 1. Conversely a + b = 1 means tau(1) = 1, i.e. c1 + c2 + c3 = 0 for general c1 (a + b = -(c2 + c3)/c1). On this line E(a,b) = C(1)^2 + sum_{r != 1} C(r) C(tau r), and C(1) = sum_x t(x)^2 = p - rho exactly. So the line contributes a term (p - rho)^2, of exact size p^2(1 - O(1/p)), to E. (This is the "plane x1 = x3, x2 = x4" of round one seen on the r-line: at r = 1 the fibre V(1) has the constant class.)

CHECKED, raw criterion at p in {11..31}, 28 (p,f) pairs: all p - 1 pairs of the line are flagged in 26 of the 28; the two exceptions are f = (x-1)(x-3)(x-9) at p = 13 (7 of 12; here f = x^3 - 1 mod 13 has the cube roots of unity as roots, a symmetric case) and at p = 17 (12 of 16). CHECKED, centred criterion at p in {37..101}, 60 (p,f) pairs: the whole line is flagged in 57 of 60. I do not know the 3 exceptions' cause (HINT: |rest| of order 2 sqrt(p) p cancels (p - rho)^2 only when p is moderate; not examined).

### E2.3 Off the line: what is left

Over p in {31..101}, all four f, b != 0 and a + b != 1: 282,208 pairs, of which 2,969 (1.05%) are flagged by the centred criterion. Two further structures, tested exactly:

(i) b = 0 (PROVED: b = 0 means c2 = 0). Then Q_c = c1 x1 x2 + c3 x3 x4 and the path graph is disconnected; this is not a path quadric and is not part of the family in question (it also has a different diagnosis: E(a,0) = sum_r C(r) C(a r) is a multiplicative correlation of C with itself). CHECKED: among the 4,000 pairs with b = 0 and a + b != 1, 990 (24.75%) are flagged against 1.38% over all pairs outside the line (`e2c_console.txt`, lift 17.9); with a = -1, b = 0: 28 of 64. I exclude b = 0 below.

(ii) The spike term. CHECKED/PROVED: C(1) = p - rho is the only value of size p; C(r) for r != 1 satisfies |C(r)| <= (2g) sqrt(p) + 1 with g = d - 1 (interpretation, uses Weil). Off the line E(a,b) = (p - rho) (C(tau(1)) + C(tau^{-1}(1))) + (terms with r outside {1, tau^{-1} 1}); here tau^{-1}(1) = (1 - b)/a, and the two spike terms are distinct since a + b != 1. Define Sp(a,b) = (p - rho)(C(a+b) + C((1-b)/a)). Conjecture D (stated, hit rate): for b != 0 off the line, "|E_c| > p^2/2" implies "4|Sp| > p^2 or a = -1". Data (`e2e_out.txt`): 2,969 flagged; 2,506 have 4|Sp| > p^2; 247 have a = -1; the union explains 2,533 = 85.3%. Precision is low: of 30,921 pairs with 4|Sp| > p^2 only 2,506 (8.1%) are flagged. The sum of E^2 over these pairs is 443,031,150,028 and the sum of (E - Sp)^2 is 150,430,069,404 (ratio 0.34, floats for reading only): the spike term removes about two thirds of the sum of squares. About 400 flagged pairs (15%) are unexplained.

(iii) a = -1, i.e. c1 = c3 ("palindromic" c, tau an involution; Q_c is invariant under the reversal (x1,x2,x3,x4) -> (x4,x3,x2,x1)). Enrichment: with b != 0 and off the line, a = -1: 247 of 4,000 flagged (6.2%, lift 5.9) against 1.05% overall (`e2d_console.txt`). The involution doubles the terms C(r)C(b-r) in pairs, which increases the variance by about a factor 2; this is a heuristic reading (HINT). I also tested whether palindromic c have a systematically positive mean E/p^2 (`e2f_out.txt`, 64 (p,f) pairs, p in 31..101): mean of the class means a = -1: +0.049, a = 1: +0.032, other: +0.047 (floats for reading only); a = -1 above "other" in 31 of 64. No systematic signal: not a bad set.

### E2.4 Other candidate descriptions, with hit rates (CHECKED, enrichment over b != 0, off the line, p = 31..101, 282,208 pairs, base flag rate 1.05%; `e2d_console.txt`)

| Description | pairs | flagged | rate | lift |
|---|---|---|---|---|
| a = 1 (translation) | 4,064 | 58 | 1.43% | 1.4 |
| a = -1 | 4,000 | 247 | 6.17% | 5.9 |
| tau(1) = -1 | 4,000 | 90 | 2.25% | 2.1 |
| tau(-1) = 1 | 4,000 | 90 | 2.25% | 2.1 |
| a a ratio e_j/e_i of roots (3-root and quintic f) | 11,368 | 72 | 0.63% | 0.6 |
| b a ratio of roots | 11,368 | 86 | 0.76% | 0.7 |
| tau(1) a ratio of roots | 11,368 | 70 | 0.62% | 0.6 |
| tau maps some ratio to a ratio | 45,820 | 344 | 0.75% | 0.7 |

So conditions involving ratios of roots are NOT enriched (lift below 1). The "ratios of roots" conjecture does not hold in this form: the ratios r = e_j/e_i make f(x)f(rx) singular but the fibre sum there is only of size sqrt(p), not p (the only fibre where f(x) f(r x) is a perfect square, so that C(r) has size p, is r = 1). This is why the line a+b=1 (through r = 1) is the one structured part.

### E2.5 Conjectures (not facts)

- C1. For c1 + c2 + c3 = 0 (a + b = 1), E(a,b)/p^2 -> 1 as p -> infinity, uniformly in f. Hit rate: the exact term (p - rho)^2 is proved; the remainder is sqrt(p)-scale in the data (flagged on the whole line in 57 of 60 (p,f) at p >= 37 and in 26 of 28 at p <= 31). Mean E/p^2 over p > 100 in E3: 0.997, 0.973, 0.987 for the three f (c = (1,1,-2)).
- C2. For b != 0 and a + b != 1, E(a,b)/p^2 is O(p^(-1/2)) except for the spike pairs and a = -1; hit rate 85% for flagged pairs (E2.3 (ii) and (iii)). The mean square of E_c/p^2 outside the line times p is between about 0.5 and 2.9 for the (p,f) sampled (`e2c_out.txt`); I did not fit a limit.
- C3. b = 0 (c2 = 0) is a separate degenerate family; it is not in the path-quadric family.
- NOT confirmed: a b-relation beyond a + b = 1; root-ratio conditions.

## E3. The four pieces of E over p <= 199

Script `e3.py`, per-prime integers in `e3_rows.tsv`, summary in `e3_summary.txt`. Exact definition of a(r) (needs no weights, only a point count): for r != 0, a(r) := -C(r) - chi(r). For r not equal 1 and not a ratio of roots, the curve y^2 = f(x) f(r x) of degree 2d (squarefree) has genus d - 1, p + C(r) affine points and 1 + chi(r) points at infinity (leading coefficient r^d, chi(r^d) = chi(r) for odd d), so #points = p + 1 - a(r), i.e. a(r) is the Frobenius trace of that curve. For the other r the same formula defines a(r). The splitting is C(r) = -a(r) - chi(r) for r != 0 and C(0) = t0 M. Pieces, over r with r != 0 and tau(r) != 0: S_aa = sum a(r) a(tau r), S_ach = sum a(r) chi(tau r), S_cha = sum chi(r) a(tau r), S_chch = sum chi(r) chi(tau r); the fifth term B collects r = 0 and tau(r) = 0. The identity S_aa + S_ach + S_cha + S_chch + B = E is asserted in the script for every row (43 primes x 3 f x 4 c, 0 failures). Note that S_chch = sum_r chi(r) chi(-c3 r - c2) = chi(-c3) sum_r chi(r^2 + (c2/c3) r) = -chi(-c3) exactly (the excluded terms r = 0 and tau(r) = 0 vanish; the quadratic has nonzero discriminant since c2 != 0), so |S_chch| = 1; this agrees with the tabulated maximum 1/25 = 0.04 (p = 5).

c = (1,1,1), (1,2,3), (1,3,5) and the bad case (1,1,-2) = (1,1,p-2), c1+c2+c3 = 0. Counts of primes (positive / negative), mean of piece/p^2 over p > 100 (floats for reading only):

| f, c | E | S_aa | S_ach | S_cha | S_chch | B |
|---|---|---|---|---|---|---|
| x^3+x+1, (1,1,1) (43 primes) | 26/17, +0.057 | 25/17 (1 zero), +0.056 | 25/17, +0.001 | 25/17, +0.001 | 22/21, 0.000 | 16/25, -0.001 |
| x^3+x+1, (1,2,3) | 30/13, +0.032 | 30/13, +0.025 | 26/17, +0.006 | 21/22, +0.001 | 23/20, 0.000 | 20/21, +0.001 |
| x^3+x+1, (1,3,5) (42) | 24/18, -0.005 | 26/16, -0.008 | 24/18, +0.004 | 26/16, +0.001 | 23/19, 0.000 | 16/21, -0.003 |
| x^3+x+1, (1,1,-2) | 43/0, +0.997 | 43/0, +1.015 | 4/39, -0.007 | 4/38, -0.010 | 24/19, 0.000 | 21/18, -0.001 |
| x^3-x+3, (1,1,1) (44) | 29/15, +0.101 | 26/16, +0.094 | 22/21, +0.002 | 22/21, +0.002 | 23/21, 0.000 | 26/16, +0.003 |
| x^3-x+3, (1,2,3) | 31/13, +0.077 | 29/15, +0.078 | 23/21, 0.000 | 27/17, +0.001 | 23/21, 0.000 | 20/20, -0.001 |
| x^3-x+3, (1,3,5) (43) | 31/12, +0.043 | 30/13, +0.045 | 24/19, 0.000 | 23/20, 0.000 | 24/19, 0.000 | 18/23, -0.002 |
| x^3-x+3, (1,1,-2) | 44/0, +0.973 | 44/0, +0.987 | 9/35, -0.007 | 8/35, -0.007 | 24/20, 0.000 | 24/17, -0.001 |
| x^5+x+1, (1,1,1) (42) | 24/18, +0.062 | 24/17, +0.061 | 20/22, +0.001 | 20/22, +0.001 | 21/21, 0.000 | 16/21, -0.002 |
| x^5+x+1, (1,2,3) | 22/20, +0.036 | 23/18, +0.038 | 23/18, +0.001 | 20/22, -0.001 | 22/20, 0.000 | 18/19, -0.002 |
| x^5+x+1, (1,3,5) (41) | 25/16, -0.013 | 26/15, -0.017 | 23/17, +0.001 | 25/15, +0.002 | 24/17, 0.000 | 21/16, +0.002 |
| x^5+x+1, (1,1,-2) | 42/0, +0.987 | 42/0, +1.003 | 3/39, -0.010 | 5/37, -0.007 | 24/18, 0.000 | 12/23, 0.000 |

(Pairs of counts omit exact zeros; the sums are not always equal to the number of primes for that reason.)

Reading. CHECKED: (a) for every c with c1+c2+c3 != 0 the sign of E, of S_aa and of N_4 is mixed over p (between 24 and 31 positive out of 41 to 44), with positive mean of about 0.03 to 0.10 in p^2 units for c = (1,1,1), (1,2,3) and about 0 for (1,3,5); the data do not show a definite sign of N_4 for generic c (no claim is made that N_4 has a sign: the sign statement concerns the cohomology, not N_4 at one q); (b) S_aa is what matters: |S_ach|, |S_cha| are at most 0.24 p^2 at the single worst prime (p = 5, small) and about 0.001 on average; |S_chch| <= 0.04 p^2, B is similar; (c) for c1+c2+c3 = 0 all 43, 44, 42 primes give E > 0 and S_aa > 0, and both cross terms are negative at most primes (34 to 39 of 42..44), with magnitude about 0.01 p^2, i.e. consistent with the spike (p - rho + 1)^2 inside S_aa from the term a(1) a(tau 1) = a(1)^2, plus a small negative cross piece from the a(1) chi(1) products. The spike is where the positive constant class (eigenvalue q^2 in round one) lives.

## E4. Sum over r of C(r)

PROVED (elementary, no weights). sum_r C(r) = sum_r sum_x t(x) t(r x) = sum_x t(x) sum_r t(r x). For x != 0 the map r -> r x permutes F_p so the inner sum is M. For x = 0 the inner sum is p t0. Hence

    S = sum_{r in F_p} C(r) = (M - t0) M + p t0^2 = M^2 - t0 M + q t0^2   (q = p),

and because C(0) = t0 M, sum_{r != 0} C(r) = M^2 - 2 t0 M + q t0^2 = (M - t0)^2 + (q - 1) t0^2. For f(0) != 0 (t0^2 = 1) these read M^2 - t0 M + q and M^2 - 2 t0 M + q. The same derivation works over F_q for any odd q (sum over r in F_q).

CHECKED: `e4.py`, output `e4_out.txt`: for all primes 3 <= p <= 199 (45 primes) and seven polynomials (x^3+x+1, x^3-x+3, x^5+x+1, x^3-x [f(0)=0], x^3+2x+5, (x-1)(x-2)(x-4), x^7+3x+2; non-squarefree reductions are included because the identity is about t only) the three forms agree exactly: 315 checks, 0 failures. Consequence used in E2: tau is a bijection, so sum_r C(tau r) = S as well and E_c = E - S^2/p.

## E5. Extension fields in characteristic 3

Script `e5.py` (uses agent C's validated `ff.py`, itself checked against brute force in round one and by the main session), output `e5_out.txt` (72 lines). Fields F_{3^n}, n = 2, 4, 6. c has entries in F_9: 1, -1 and i with i^2 = -1 (a square root of -1 found in each field; -i gives the same N_4 because t is Frobenius invariant for f over F_3). Three cubics over F_3: x^3+x+1 (it has the root 1 mod 3 and is squarefree), x^3-x+1 (irreducible), x^3+x^2+2.

All-ones control, c = (1,1,1) (here c1+c2+c3 = 3 = 0): N_4 = 195 (F_9), 6147 (F_81), 520851 (F_729) for x^3+x+1: reproduced exactly. For x^3-x+1: 33, 4257, 587595; for x^3+x^2+2: 193, 6241, 519883.

Table of N_4 (F_9 / F_81 / F_729); "sum" = c1+c2+c3 (nonzero or 0):

| c | sum | x^3+x+1 | x^3-x+1 | x^3+x^2+2 |
|---|---|---|---|---|
| (1,1,1) | 0 | 195 / 6147 / 520851 | 33 / 4257 / 587595 | 193 / 6241 / 519883 |
| (1,1,-1) | nonzero | 195 / 1059 / -47373 | 33 / 417 / -22011 | 193 / -287 / 34117 |
| (1,1,i) | nonzero | 193 / 769 / -21551 | 1 / 1057 / 26446 | 97 / 97 / 15694 |
| (1,i,i) | nonzero | 193 / 769 / -21551 | 1 / 1057 / 26446 | 97 / 97 / 15694 |
| (i,1,1) | nonzero | 193 / 769 / -21551 | 1 / 1057 / 26446 | 97 / 97 / 15694 |
| (1,i,1) | nonzero | 195 / 5091 / 43347 | 33 / 1281 / -53376 | 65 / 3137 / -59968 |
| (i,i,i) | 0 | 195 / 6147 / 520851 | 33 / 4257 / 587595 | 193 / 6241 / 519883 |
| (1,i,-1-i) | 0 | 199 / 7143 / 478039 | 97 / 6369 / 504175 | 129 / 6241 / 501279 |

Reading (CHECKED data; the size comparisons use q^2 = 81, 6561, 531441, floats for reading only): at q = 729 the five nonzero-sum c have |N_4|/q^2 between 0.03 and 0.11 for all three f, with mixed signs (e.g. -0.089, -0.041, +0.082 for x^3+x+1), while all three sum-zero c per cubic ((1,1,1), (i,i,i), (1,i,-1-i)) have N_4/q^2 between 0.90 and 1.11. At q = 81 the nonzero-sum c still give 0.01 to 0.78 times q^2 and at q = 9 almost all values are of size q^2, i.e. these fields are too small to see the separation, and values at the palindromic c = (1,i,1) (a = -1) are the largest nonzero-sum ones at q = 81 (5091, 1281, 3137), but at q = 729 they are not (43347, -53376, -59968), and the prime-field data (E2.3) show no systematic palindromic effect. Also: c = (1,1,i), (1,i,i) and (i,1,1) always give the same N_4 (observed in all 9 cases (3 f x 3 fields)): HINT, not examined (the three c are related by rescaling variables x_i -> lambda_i x_i? that rescaling multiplies t(x_i) by chi(f(lambda_i x_i)/f(x_i)) only when f is homogeneous, so it is not a symmetry; I did not find the reason). Over F_3 with c in F_3 and sum nonzero (the row (1,1,-1)) the values are small at q = 729 as well.

The sum-zero rows reproduce the round-one prediction: the plane x1 = x3, x2 = x4 is in Y when c1+c2+c3 = 0 and gives a q^2 term. The N_4/q^2 values 0.90 to 1.11 are of the size predicted by the single class (p - rho)^2 / p^2 plus a smaller remainder. At p = 3 these c include the all-ones quadric, as noted in round one.

## What this says for the open statement

(All HINT, from the data above; no proof, and none of the figures is a proof.)

1. Formula E1 holds exactly for the c-family tested, so the reduction of N_4 to sum_r C(r) C(tau r) is confirmed independently of the earlier derivation.
2. The bad c at k = 4 are visible as the single line a + b = 1, where E contains the exact square (p - rho)^2 because r = 1 is a fixed point of tau and C(1) has size p. No second structured family (root ratios, a = 1) shows in the data. This is consistent with the claim that the only forced H^4_c class comes from r = 1, but it does not rule out classes of lower weight (the data cannot see them at these p).
3. E4 gives the mean of C: S/p = (M^2 - t0 M)/p + 1 (for f(0) != 0). The constant 1 is the "x = 0" contribution; the rest is of order M^2/p, small once p is large. In the E2 data this mean term (S^2/p in E) is negligible for p >= 100 and matters only at small p. Whether this has any bearing on constant quotients of V(r) is OPEN (I did not test it).
4. E5: in characteristic 3 over F_729 the all-ones quadric is in the bad set (1+1+1 = 0) and nonzero-sum c show no q^2 term, again consistent with round one, but with only three fields and no extrapolation possible.

Nothing here says anything about any zeta function over the integers, or proves (S_4) or (W*): fixed finite computations cannot establish a statement for all q.

## Files

- `compute/K4C/core.py`, `e1.py`, `e2.py`, `e2b.py`, `e2c.py`, `e2d.py`, `e2e.py`, `e2f.py`, `e3.py`, `e4.py`, `e5.py` and outputs `e1_out.txt`, `e2_out.txt`, `e2b_out.txt`, `e2c_out.txt`, `e2c_console.txt`, `e2d_console.txt`, `e2d_out.txt`, `e2e_out.txt`, `e2f_out.txt`, `e3_rows.tsv`, `e3_summary.txt`, `e4_out.txt`, `e5_out.txt`.
- Honest gaps: (i) the three line exceptions at p >= 37 in E2.2 and the 15% unexplained flagged pairs of E2.3 are not explained; (ii) the "Conjecture D" threshold p^2/4 was chosen after looking at the data (not a pre-registered test); (iii) the identification of a(r) with the trace of the genus d-1 curve is for squarefree fibres only, other fibres only define a(r) by the formula; (iv) the coincidence c = (1,1,i), (1,i,i), (i,1,1) in E5 is unexplained.
