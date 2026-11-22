# A3. Exact tests aimed at breaking the induction (S5)

Started 2026-11-21 (UTC clock via `date -u`). Report is extended as work proceeds.

## Summary (finished 2026-11-21 about 23:55 UTC)
Exact (integer, Z[omega]) iterated additive Fourier transforms on F_{q^n} for q = 3, 4, 16 (p = 2, 3; quadratic and cubic characters; d = 1, 2, 3), with the stalk L-series of every Q_i = FT(P_i) at every point of F_q computed by exact Newton identities.
Result: in all 4471 determined data points where hypothesis (G) of S5 holds (generic ranks, drop locations, drop sizes, fibre dimensions D_k), the prediction of the invariant (I_i) agrees exactly; no counterexample.
Reach: d=1 up to Q_5 (partly Q_6), d=2 up to Q_3, d=3 up to Q_2 (limited by field size and by ranks 1,2,3,5,8,13 / 1,2,5,12,29 / 1,3,10,33). Controls with (G) failing or f(0)=0 fail as they should (test has teeth).
Limit: a net (Euler characteristic) test; it does not see cancellation between degrees k and k+1, so it does not prove the vanishing of S5 step 7. Nothing in this report is a proof of the induction.
Labels: engine and results CHECKED (scripts and outputs named); the local sheaf facts behind the prediction are CITED from the draft (not re-read by me, that is A1/A2); weight observations are HINT (floating point).

## 1. What was tested and how (method)

All sums are exact. Engine: `compute/A3/zfour.c` (and `zfour2.c`, same plus polynomial f), compiled with gcc, integer arithmetic only:
elements of Z[omega] (omega a primitive cube root of unity) are stored as a + b*omega with a, b in __int128; the additive Fourier
transform on F_p^N uses only additions, subtractions and multiplication by omega (a coordinate shuffle); the field F_{p^N} = F_p[X]/(m) with m
primitive is built from integer tables. The engine aborts if any coordinate exceeds 2^118 (it never did; the proven bound
|Ghat_i| <= |F|^{(i+1)/2} from the Parseval estimate S1 is far below 2^118 for every run). Floating point appears nowhere in the
engine or in the Newton-identity step (Python Fractions in Q(omega)).

Objects (my own notation, same as S4 of the draft): over F_{q^n}, t(y) = chi_n(f(y)), G_1 = t,
Ghat_i(y) = sum_x G_i(x) psi(Tr(b_i x y)) with b_i = h c_i, G_{i+1}(y) = t(y) Ghat_i(y).
Then Ghat_i(w) for w in F_q (embedded in F_{q^n}) is the trace of Frob_w^n on the stalk of Q_i = FT_{b_i}(P_i) at w, up to the
sign (-1)^i, and Ghat_k(0) = S_h(F_{q^n}) is the fibre sum of S4.

Test of one data set: for fixed (case, h, c, i, w) take p_n = (-1)^i Ghat_i(w) for n = 1..N and compute, exactly,
the series L(T) = exp(-sum p_n T^n / n) up to T^N by the Newton identities (division by j in Q(omega), integrality checked).
If the stalk of Q_i at w is a single-degree cohomology group of dimension D, then prod(1 - gamma T) is a polynomial
of degree D in T with coefficients in Z[omega]. Observed: index of the last nonzero coefficient up to T^N. "AGREE" means
D < N and the last nonzero coefficient is exactly T^D (so N - D coefficients vanish, a nontrivial check of rationality and degree);
"UNDET" means D >= N, nothing can be said.
A caveat to state at once: this checks the Euler characteristic (net count) of the stalk and the rationality; it cannot see
cancellation between H^j and H^{j+1} with equal eigenvalues, so it does not directly prove vanishing in the wrong degree.

Engine validation (CHECKED): `validate.py`, `validate_w.py` compare the engine with an independent, naive Python implementation
of the definition (own field arithmetic, own trace; for k = 3 the plain sum over all x in F^k): 0 mismatches in every comparison
(outputs `validate_out.txt`, `validate_w_out.txt`), for q = 3 (quadratic chi) and q = 4 (cubic chi), n = 1, 2, 3, including stalk
values at w != 0.

## 2. The prediction from the invariant (I_i) of S5, re-derived by me

I derived the prediction independently of the draft's section S5 text beyond its invariant (I_i); it coincides with it.
Notation: Z = roots of f, rho_i = -c_{i-1}/c_i (i >= 2), S_i(P) := finite singular set of P_i (including Z and Sigma_{i-1}), e_i(s) := dimension of
vanishing cycles of P_i at s (= r_i - dim M_i^{I_s}), Sigma_i := Sing(Q_i) with drop_i(w) := r_{i+1} - dim(stalk of Q_i at w).
Local facts used (all CITED from the draft's reading of Laumon 2.3.x, GOS; not re-read by me, this is A1/A2's job):
(i) generic rank of FT(P) = sum_s e(s) when the behaviour at infinity of P_i is tame+blocks of slope exactly 1 (Swan_infty(M (x) Lpsi(ay)) = rank M for generic a);
(ii) the stalk of FT_b(P) at w drops by the dimension of the block L_psi(a y) (x) T^a at infinity of P with w = -a/b;
(iii) the blocks at infinity of Q_{i-1} are indexed by the finite singular points s of P_{i-1}, with frequency h c_{i-1} s and multiplicity e_{i-1}(s),
and tensoring with L (tame at infinity, rank one) does not change the frequencies.
Recursion (S_0 := {0 : 1}, "virtual" singular point whose block is the tame L itself at infinity of P_1):
 Sigma_i = rho_i * S_{i-1} with multiplicities, r_i = sum e_{i-1}, S_i = {z: r_i for z in Z} + Sigma_{i-1}.
Hence r_{i+1} = d r_i + r_{i-1} (r_0 = 0, r_1 = 1), Sing(Q_i) = rho_i (Z u Sing(Q_{i-2})) as in the draft, 0 in Sing(Q_i) iff i odd with drop 1,
D_k = r_{k+1} - [k odd]. Checked by hand against the draft for i <= 4 (closed form of Sigma_i, list of conditions (G_k)): identical.
The code `a3lib.predict` / `predict_gen` implements this recursion, merging multiplicities if two images coincide.
The hypothesis flag "(G) valid for Q_i" = Z does not meet Sigma_j for 1 <= j <= i-1 (this is what step 4 of S5 needs to pass from Q_{i-1} to P_i, ..., Q_i).

## 3. Results (CHECKED; all files in `compute/A3/`)

Files: `raw_<family>_n<N>.json` raw engine output (exact integers a, b with Ghat = a + b omega); `analysis_<family>_n<N>.txt` one line per data point;
`summary_all.txt` totals; `run_<family>_n<N>.log` run logs; `validate*.py`, `validate*_out.txt` engine validation; `closed_form_check.py` (+ `_out`).
Terminology: a "data point" is (configuration, stage i, point w in F_q u {0}) with its exact L-series up to T^N; "valid" means hypothesis (G) of S5 holds up to Q_i
(Z disjoint from Sigma_1..Sigma_{i-1}), decided by the code from the recursion of section 2; AGREE = D < N and the last nonzero coefficient is T^D
(so N - D coefficients vanish); UNDET = D >= N. Data points inside one family share stages (configurations with a common c-prefix), so they are not independent;
the number of distinct (field, f, h, c-vector) configurations is in the third column.

| family | field, chi, f | configs | N | valid AGREE | valid UNDET | valid DISAGREE | invalid (control): agree / undet / disagree |
|---|---|---|---|---|---|---|---|
| p3d1 | q=3, quadratic, f = x-1 (d=1), c in {+-1}^K, K=4,5,6, h = +-1 | 56 | 13 | 465 | 0 | 0 | 13 / 0 / 338 |
| p2d1 | q=4, cubic, f = x-1 (d=1), K=3,4,5 | 56 | 12 | 760 | 0 | 0 | 6 / 0 / 174 |
| p2d1h | same, the 12 valid K=5 vectors with h = xi, xi^2 | 24 | 12 | 480 | 0 | 0 | 0 |
| p2d1K6 | same, all 12 valid K=6 vectors (Q_6 is reached) | 12 | 12 | 264 | 24 | 0 | 0 |
| p2d2irr | q=4, cubic, f = x^2+x+xi irreducible (d=2), K=3,4 | 36 | 12 | 312 | 120 | 0 | 0 / 96 / 12 |
| p2d2irrdeep | same, 3 valid vectors, K=3 | 3 | 13 | 36 | 0 | 0 | 0 |
| p3d3irr | q=3, quadratic, f = x^3-x+1 irreducible (d=3), K=2,3 | 12 | 14 | 72 | 12 | 0 | 0 / 12 / 0 |
| p2q16 | q=16, cubic, f = x-1, 20 random valid K=5 and 10 random valid K=6 vectors in (F_16^*)^K, all 16 points w in F_16 | 30 | 6 | 1950 | 610 | 0 | 0 |
| p2d3chi1 | q=4, cubic, f = x^3-1 (d=3, chi^d = 1: unramified at infinity), K=2,3 | 12 | 12 | 96 | 0 | 0 | 0 / 36 / 0 |
| p3zero | q=3, quadratic, f = x (f(0)=0, violates S0) | 12 | 14 | 36 (stage 1 only) | 0 | 0 | 0 / 0 / 96 |
| total | | | | 4471 | 766 | 0 | 19 / 144 / 620 |

No counterexample: in all 4471 determined data points where (G) holds, the prediction of section 2 is exact, and no valid point contradicts it.

Dimensions checked in the valid range, by stage (these are the stalk dimensions of Q_i and, for w = 0, the fibre dimension D_k of S4):
- d=1 (generic ranks r_2.. = 1,2,3,5,8,13): Q_1: 0,1; Q_2: 1,2; Q_3: 2,3; Q_4: 3,4,5; Q_5: 5,7,8; Q_6: 8 and 11 determined (12 and 13 undetermined at N=12).
  So D_k = r_{k+1} - [k odd] is confirmed for k = 1,...,5 at q = 4, k = 1,...,4 at q = 3, and k = 1..4 at q = 16 over all 16 points.
- d=2 (r = 1,2,5,12,29): Q_1: 1,2; Q_2: 5; Q_3: 11 (at w = 0, D_3 = 12 - 1) and 12 (generic; at N = 13 one coefficient vanishes); Q_4 (rank 29) undetermined.
- d=3 (r = 1,3,10,33): Q_1: 2,3; Q_2: 10 (N = 14: four vanishing coefficients); Q_3 (rank 33, 32 at w = 0) undetermined, as is every claim with D >= N.
- chi^d = 1 at infinity (q=4, d=3, f = x^3 - 1, chi cubic, so L is unramified at infinity): Q_1 and Q_2 agree (dims 2,3 and 9,10); the nontriviality of chi^d at infinity is not needed for these ranks.
In every determined case the L-polynomial had coefficients in Z[omega] (integrality was tested for each polynomial; one failure would have shown).

Where the singular points are: in the d=1 families every point of F_q (q = 3, 4, 16) was tested at every stage; the drops occurred exactly at the points
rho_i (S_{i-1} as in section 2) and with the predicted size, including merged points (two preimages with the same image) and the point 0 for odd i.
For d = 2 and 3 with irreducible f the roots are not in the base field, so only the points of F_q were probed (the singular points rho_i z lie in F_{q^d}); for these the generic rank at all the points of F_q not in Sigma_i is confirmed.
The singular points off F_q for d >= 2 are therefore not directly tested (the 16-point test is for d = 1 only).

Controls (hypothesis fails), to show that the test has teeth:
- (G) fails: q=3, c all equal at K=5 (rho_4 rho_2 = 1, an element of R), q=3 c=(1,1,-1,1) (rho_3 = 1), many q=4 vectors with a repeated consecutive c or rho_4 rho_2 = 1. The naive prediction then fails in most data points
  (observed degree usually lower by one or two): 620 of 639 determined control points. 19 control points agree anyway ("sufficient, not necessary").
  This confirms numerically the draft's remark that the all-ones quadric fails (G_k) for k >= 5.
- f(0) = 0 (f = x, quadratic chi, q=3): the prediction fails at once from stage 2 (the L-series of the stalk of Q_2 at w=0 is not a polynomial of degree 1 up to T^14), as the draft's S0 requires f(0) != 0 and the translation of S0 is needed.
- For q=4 with d=2 and both roots rational in F_4 (Z = {1, xi}), R = F_4^* contains every ratio rho, so (G_3) can never hold; this is why d=2 was run with f irreducible over F_4 (Z in F_16, with ratios of order 5, never in F_4^*).

HINT (floating point, not used anywhere in the claims): `hint_weights.py`, `hint_weights_out.txt`. The reciprocal roots gamma of the exact polynomials above have |gamma| = q^{i/2} (pure part) or q^{(i-1)/2} (a lower weight piece, occurring only where the stalk has a drop, i.e. at singular points, and for odd k at w = 0), never more than q^{i/2}, in all valid determined cases.
So the elementary bound |S| <= |F|^{(k+1)/2} used in S8 has slack of a factor sqrt|F| over what the data show, and for odd k the fibre cohomology at w = 0 is not pure (it contains weight k-1 eigenvalues). The draft does not claim purity, so there is no conflict, but any later argument that assumed the fibre sums for odd k to be pure of weight k would be wrong (HINT, depends on weights).

Closed form of S3 (CHECKED symbolic, `closed_form_check.py`): the draft's closed form for Sigma_i equals the recursion Sigma_i = rho_i (Z u Sigma_{i-2}), Sigma_1 = {0}, for all i <= 14. The condition lists of S3 (k=5,6) follow.

## 4. What the tests do not show (limits, stated plainly)
1. The tests measure a net count: the exact L-series of the stalk is the net (Euler characteristic) series. A dimension and rationality agreement cannot see cancellation between two adjacent degrees with equal Frobenius eigenvalues. So the vanishing of H^{k+1}_c, the heart of S5 step 7, is supported only indirectly: the net dimension equals the one predicted from the invariant, which assumed a single degree; hidden eigenvalue pairs in degrees k and k+1 would leave the net dimension unchanged. This is the weakness the draft itself attributes to the earlier exact tests (list 3), and it remains.
2. Reach: determined data only where the predicted dimension D < N. For d=1 this gives k <= 5 (q=4), k <= 4 (q=3 and q=16), and Q_6 only at two of its points; for d=2, k <= 3; for d=3, k <= 2. The induction is untested above that, in particular nothing here tests ranks above 12 (N <= 14 because of the size of the field: 3^14, 4^13, 16^6). The ranks of Q_i grow like ((d+sqrt(d^2+4))/2)^i.
3. Only p = 2, 3 and characters of order 2 and 3. Nothing for p >= 5 or order 4 or more.
4. The tests do not test the draft's S3 existence count for c (Q-1 > (k^2/2+k) d^2): for Q = 4 or 16 the count does not apply, yet valid c exist in the tested families (d=1 and d=2 irreducible).
5. Tameness/irreducibility (type T3) of the P_i and the structure at infinity are not visible in dimension counts: only their numerical consequences (ranks and drops) are.

## 5. Findings on the draft (referee)
No error was found in the quantitative predictions of S5 (ranks, drop locations and sizes) in the hypothesis range. Small points:
(a) The invariant (5) of S5, "T^0 != 0 iff 0 in S_{i-1}", is not literally defined for i = 1; the base case needs the convention that T^0 of P_1 is L itself at infinity (my S_0 = {0 : 1}). Cosmetic.
(b) The draft's remark in section 0 that "the induction at d >= 3, k >= 3 is checked by nothing" is now partly out of date: d=2 (k <= 3), d=1 (k <= 5, and Q_6 partly), d=3 only k <= 2. The remaining gap is large ranks (>= 13), which these methods cannot reach with N <= 14.
(c) For d=2 with both roots in F_q^*, q = 4, (G_k) fails for every k >= 3 because R = F_q^*; the S3 counting argument handles this only by passing to a larger Q, so the choice of F_Q depending on k and on the root field is essential, as the draft says. Confirmed by the rational d=2 control (no run needed beyond the algebra).
(d) For odd k the fibre at h != 0 contains eigenvalues of weight k-1 (hint) besides weight k: the fibre cohomology is mixed there. S8 uses only the elementary upper bound, so this is harmless.
(e) f(0) != 0 is necessary for the prediction (control p3zero), so S0 cannot be dropped.
(f) Nothing contradicts D_k = r_{k+1} - [k odd] of S4: confirmed for k <= 5 (d=1), k <= 3 (d=2), k <= 2 (d=3).

## 6. Reproduction
Engine: `gcc -O2 -o zfour3.exe zfour2.c` (zfour.c is the first version without polynomial f; same arithmetic; zfour3 differs from zfour2 only by the optional choice of the generator xi for q=16). Driver: `python run_cases.py <family> <Nmax>` then `python analyze.py <family> <Nmax>`; the primitive polynomials are in `prim_polys.json` (found and verified by Python big-integer arithmetic).
Engine validation: `python validate.py`, `python validate_w.py` (0 mismatches; q=16 was not validated against brute force, only against the rationality of all its L-series).
Process used one thread at below-normal priority; peak memory about 5.3 GB for the n=13, q=4 runs (4^13 elements). Run times, UTC 2026-11-21 23:02 to about 23:55.
