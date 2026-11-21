# Round two: write-up

Scope. Character sums over finite fields, where the bound is a theorem of Weil (1948). The question is only whether the route of the note is a valid proof and what it needs. Nothing here concerns the Riemann Hypothesis for the integers. Labels: PROVED (full argument in a report), CITED, CHECKED (exact integer or rational arithmetic, script and output named), OPEN, HINT. No PROVED statement below uses weights, purity or the Weil bound; where weights are used to read data the report says so. Report names: K4T (k = 4 theory), REF2 (hostile referee), K4C and NUM (computation), RED (reduction check), FS (forget supports), GEN (general k), LIT (primary sources). All in `round2/reports/`. Notation as in TOY_CASE.md.

## 1. What changed since round one

1. k = 4 now has a weight-free theorem outside an explicit finite set of lines in c-space (K4T Theorem D, re-derived by REF2). Round one only had the failure at c_1+c_2+c_3 = 0.
2. That failure set is larger than round one thought when f has a multiplicative symmetry (K4T Theorem B, confirmed by REF2's data).
3. For general k the cohomology lives in degrees k-1, k, k+1 only, and only degree k has the wrong sign. GEN claims the route needs only one input, (P_k), instead of (S_k); nobody has refereed that.
4. The forget-supports criterion became exact (FS) but does not decide anything; LIT opened primary sources for the Fourier-transform inputs and found no weights in them.
5. Lean now proves q N = M^k + R and the bound including the factor q-1 (section 5).

## 2. The case k = 4

**Exact theorem now claimed (K4T Theorem D, REF2 section 0).** Let q be odd, f in F_q[x] squarefree of odd degree d >= 3, f(0) != 0, f not of the form x^d - a. Let Z be the roots of f, mu = {rho : rho Z = Z}, S = {0} together with all ratios z'/z (z, z' in Z). Let c = (c_1,c_2,c_3) have nonzero entries with c_2 + c_3 s + c_1 s' != 0 for all s, s' in S. Then H^j_c(Y,K) = 0 for every j != 3, so (S_4) holds. For mu = {1}, dim H^3_c = 4d^3 - 3d^2 + 4d - 1 (92 at d = 3, 444 at d = 5).

**Exceptional set.**
- Proved to fail: X1, meaning a pair rho, rho' in mu with c_2 + c_3 rho + c_1 rho' = 0 (a plane lies in Y, class of eigenvalue q^2 up to a root of unity). It contains X0: c_1+c_2+c_3 = 0. For f = x^3 - a it is nine lines.
- Open: f = x^d - a (dim of V_pi at most 1; decided only through a HINT); X4 minus X1, the other lines with c_2 + c_3 s + c_1 s' = 0 (at most (d^2-d+2)^2 - 1 = 63 lines at d = 3).

**Proof in outline.**
1. Y minus the origin fibres over the projective line by planes; N_4 = -q + t_0^2 M^2 + sum_r C(r) C(tau(r)). PROVED (K4T; REF2 derived it independently). CHECKED: 48 cases (K4T), 592 (K4C), 236 (REF2), 1148 (NUM), 0 mismatches.
2. Leray: H^5_c = H^6_c = 0; H^4_c has pieces E^{0,4} and coker(d_2 : E^{0,3} -> E^{2,2}), with E^{2,2} = (V tensor tau^*V) coinvariants (-1). PROVED (K4T, re-derived by REF2). Uses Kunneth, proper base change, Poincare duality, cited from memory.
3. V is tame at every point including infinity, by comparing two Euler characteristics of the total space. PROVED, using Grothendieck-Ogg-Shafarevich (CITED, from memory). CHECKED symbolically (total Swan 0).
4. Lemma: for tame sheaves with disjoint finite singular sets, Hom_pi(A,B) = Hom(A_pi, B^pi), because the tame fundamental group of the affine line is trivial. PROVED; SGA 1 XIII 2.12 was opened by LIT. The step "kernel of pi_1(U) -> pi_1(X) is the normal closure of inertia" (SGA 1 V 8.2) is CITED from memory. Correction to the brief: disjointness is needed only at finite points.
5. V_pi = 0 when mu = {1}: PROVED (K4T, re-derived by REF2). For mu of order m with 1 < m < d: PROVED by REF2's elementary Euler-characteristic count (K4T had cited Deligne-Lusztig, not needed). For x^d - a: OPEN.
6. Theorem B (planes) and Theorem D follow. PROVED.
7. X4 minus X1: K4T reduces it to two statements, (Irr) W irreducible and (Loc0) monodromy at r = 0 has eigenvalue -1. REF2 checked the logic. Both inputs are OPEN, HINT level.

**Referee verdict (REF2): PROVED_FOR_GENERIC_C.** No weights, no unproved irreducibility used in the theorem, nothing wrong found in the main chain. REF2 found four repairable defects (D1 to D4). Foundation theorem numbers were not opened by REF2. This gives only the exponent q^(7/8) at k = 4 and says nothing for k >= 5; the route needs the input for infinitely many k.

**Disagreement.** K4T says a nonzero E^{2,2} class would have size about q and be invisible in data. REF2 (D1) argues it would have size q^2 if W is irreducible, so as visible as X0. Both are weight readings of data, not proof steps. No data failure was found on X4 minus X1 either way. I do not pick a side: REF2 gives a derivation, K4T gives none, but it rests on (Irr).

## 3. General k and the forget-supports criterion

**Proved (given CITED weight-free inputs).**
- H^j_c(Y,K) = 0 for j < k-1 (all agree).
- H^j_c(Y,K) = 0 for j >= k+2, via the fibration over h and k-1 Fourier transforms (RED claims 1 to 4; GEN Theorem G). Inputs: BBD 4.1, Laumon 1.3, Kunneth.
- H^{k-1} and H^{k+1} enter with the same sign; only H^k is wrong parity (RED, GEN). So (S_k) can be weakened to H^k_c = 0.
- FS Theorem A: (S_k) holds iff B^m = 0 for all m >= k (boundary groups) and H^{k-1}(Y,K) -> B^{k-1} is onto. An exact reformulation, not a reduction. The "isomorphism in all degrees" version is never true here. Boundary divisors D_ab for non-adjacent a, b are the ones with nonzero stalk; strata of codimension 2 or more are undetermined.
- GEN: for k >= 6 no coordinate-matching linear subspace of dimension k/2 lies in Y for any c (PROVED, CHECKED to k = 12). The k = 4 plane mechanism does not recur.

**Where reports disagree.**
- Lower half. FS says the main session's one-line argument is not valid on its own and uses a lci argument. RED and REF2 say it is valid with the direct support count and the triangle j_! j^* P -> P -> i_* i^* P. Same conclusion everywhere. Reason for leaning to RED and REF2: they derive both conditions explicitly. The check against BBD 4.1.9 was not done (LIT did not open it).
- What the fibre over h needs. RED: "R^{k+1} punctual" is needed in addition to a coinvariant statement, and the main session's "coinvariants of one local system" omits a differential d_2 and a term H^1_c(G_m, R^{k+1}). GEN: (P_k), meaning R^{k+1} punctual, is by itself sufficient (Proposition X), without (S_k) or (W*). Both agree (P_k) is OPEN for k >= 3. GEN says Proposition X is unchecked.
- GEN's stationary-phase bookkeeping (period 4, trivial character only for i = 3 mod 4) would give (P_k) for all even k and a weight-free proof of Weil for y^2 = f(x). GEN labels it HINT, high risk. FS and LIT read the literature as saying such concentration usually needs weights (FKM's proof uses them, LIT); GEN's route would avoid that. Unrefereed; Laumon chapters 2 and 3 were not opened. No side taken.
- FS could not reproduce the k = 4 failure from boundary data (the sheaf on the diagonal is constant for every c). REF2: not a contradiction, K4T decides H^4_c by another fibration.
- GEN's c-average identity and the supersingular-type cancellation caveat (main session) are handled only through (P_k).

## 4. The bad set: theory against computed maps

Paths relative to `round2/compute/`. Decimals are for reading; counts are exact integers.

| Theory says | Figure | File |
|---|---|---|
| N_4 formula is exact | 592 of 592 match (K4C); 0 mismatches in 236 (REF2) | K4C/e1_out.txt; REF2/x4_test_out.txt |
| X0 gives N_4 near p^2 (mu = {1}) | mean N/p^2 = 0.985, 1.014 (p = 509), 1.001, 0.995 (p = 1009); all 507 and 1007 points with abs(N) > 0.8 p^2 lie on X0 | REF2/x4_test_out.txt |
| X4 minus X1 not a failure in data | mean -0.001 to 0.040 (about 61,000 points at p = 1009), 0 flagged | same |
| X1 with m planes gives N/p^2 near m (f = x^3 - 2, p = 1009) | m = 0: n = 1,007,010, mean -0.000; m = 1: n = 9045, mean 0.998; m = 2: n = 9, mean 1.940. For x^5 - 2, p = 1021: m = 1: 0.994, m = 2: 2.036 | REF2/x1_mult_out.txt |
| X1 lines for x^3 - a | mean N/p^2 from 1.499 (p = 31) to 2.276 (p = 103) on the two-plane choices; chi_c = -92, -444 | K4T/k4t_checks_out.txt |
| Plane term (p - r)^2 leads on c_1+c_2+c_3 = 0 | 146 rows, p up to 397; largest D^2/p^3 = 12.843 (p = 71) | RED/k4_plane_out.txt |
| X0 alone is the exceptional set (NUM's reading) | 2677 of 2694 plane vectors have 2N >= p^2, but the plane covers 2677 of 6578 flagged vectors; 191 are unexplained | NUM/m1c_all_primes.txt |
| Line exceptions | 10 of 60 (p,f) lines have a failing point (REF2); K4C reported 3 of 60 (K4C report; I did not reopen its output) | REF2/line_exc_out.txt |
| No matching plane for k >= 6 | admissible matchings: 1 (k = 4), 0 at k = 6, 8, 10, 12 | GEN/matchings_out.txt |
| k = 6: only family B (c_3 = 0) acts as a plane; it is a sum of squares | N/(p-r)^3 = 1.016, 0.965, 0.905, 0.937 (f1, p = 29, 41, 67, 83) | NUM/m2e_family_ratio.txt |
| (1,1,i), (1,i,i), (i,1,1) coincide | all give N_4 = 193 over F_9 (x^3+x+1); REF2 proves one symmetry orbit | K4C/e5_out.txt |

Reading. For mu = {1} the data show exactly the predicted bad line and nothing else of order p^2. NUM's X0-only set is incomplete when f has a symmetry (K4T, REF2 section 4b). Flagged off-plane vectors are lower-order effects (M^4/p, c_3 = 0, the terms C(1)C(tau 1)), 191 of 6578 unexplained; K4T does not predict them. At k = 6 about 95 percent of the excess-bad vectors at p <= 17 are unexplained (NUM report; I did not reopen those tables); odd k shows no size gap (NUM report).

One thing I found that no report discusses. REF2's `x4_test_out.txt` for x^5 - 2 (p = 1021) lists 400 flagged points outside X4 (425 for x^5 - 32), with abs(N)/p^2 up to 0.97. REF2's text states "none outside X4" for the split cubics, which is right for the cubic lines of that file. A Gaussian guess with the printed std 0.226 and n = 1,005,100 gives about 400 such points (HINT, a float estimate). I read them as tail noise at the larger std of d = 5, but REF2 did not say so.

## 5. Lean

File `lean/ToyWeil/Identity.lean` exists and imports `ToyWeil.Parseval` unedited. The log `lean/logs/ToyWeil.Identity.log` contains only six axiom lines and no error. It does not record an exit code; the LEAN report says the check script returned 0. Statements copied from the file:

    theorem Ssum_zero (hψ : psi ≠ 0) (t : F → ℂ) (n : ℕ) :
        Ssum psi t 0 (n + 1) = (∑ x, t x) ^ (n + 1)

    theorem identity (hψ : psi ≠ 0) (t : F → ℂ) (n : ℕ) :
        (Fintype.card F : ℂ) * Ncount t n = (∑ x, t x) ^ (n + 1) + Rsum psi t n

    theorem identity_bound (hψ : psi ≠ 0) (t : F → ℂ) (B : ℝ) (hB : ∀ x, ‖t x‖ ≤ B)
        (n : ℕ) (hn : 1 ≤ n) :
        ‖(Fintype.card F : ℂ) * Ncount t n - (∑ x, t x) ^ (n + 1)‖
          ≤ ((Fintype.card F : ℝ) - 1) *
            ((Fintype.card F : ℝ) ^ ((n : ℝ) / 2) * B ^ (n - 1) * ∑ x, ‖t x‖ ^ 2)

    theorem identity_bound_one (hψ : psi ≠ 0) (t : F → ℂ) (hB : ∀ x, ‖t x‖ ≤ 1)
        (n : ℕ) (hn : 1 ≤ n) :
        ‖(Fintype.card F : ℂ) * Ncount t n - (∑ x, t x) ^ (n + 1)‖
          ≤ ((Fintype.card F : ℝ) - 1) * (Fintype.card F : ℝ) *
            Real.sqrt (Fintype.card F) ^ n

`identity_bound_closed` and `identity_bound_weak` (bound q^((k+3)/2), non-strict) are also in the file. Axiom lines from the log, each of the six: `'ToyWeil.<name>' depends on axioms: [propext, Classical.choice, Quot.sound]` for Ssum_zero, identity, identity_bound, identity_bound_closed, identity_bound_one, identity_bound_weak. The strict inequality of round one was not attempted. Still not formalised: trace formula, Kunneth, any cohomological input, passage to F_(q^m).

## 6. Primary sources

Opened (LIT, text extracted from the saved PDFs; "no weights" means a text search of the OCR layer, which checks words, not mathematics):
- BBD, Asterisque 100, 4.1.1, 4.1.2, 4.1.4, 4.1.5: https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/BBD-pervers-2x.pdf
- Laumon, Publ. IHES 65 (1987), 1.2.2.1, 1.3.1.1, 1.3.2.3: https://www.numdam.org/item/10.1007/BF02698937.pdf
- Katz-Laumon, Publ. IHES 62 (1985), 2.1.3 and appendix 2.4: https://web.math.princeton.edu/~nmk/old/TFandmajSE.pdf
- SGA 1 XIII Corollaire 2.12: https://arxiv.org/pdf/math/0206203v1
- SGA 4 1/2, Th. finitude 4.6.4; Sommes trig. 3.5.2 and 3.8 (retypeset edition): https://matematicas.unex.es/~navarro/res/sga/SGA%204%20%26%20HALF%20Cohomologie%20Etale.pdf
- Katz in SGA 7 XVIII, recall of XV 3.4: https://web.math.princeton.edu/~nmk/old/etudecoho.pdf
- Partly: Fu, arXiv math/0607164 (Theorem 0.1, Corollaries 0.2, 0.3; Denef-Loeser seen through it); FKM, https://ar5iv.labs.arxiv.org/html/1405.2293 (Prop. 1.1, Thm 1.5); Katz, Convolution and Equidistribution, https://web.math.princeton.edu/~nmk/mellin398.pdf.
- Deligne "Theoreme 8.4" (cited by FS) does not exist in the edition LIT opened (section 8 has 8.1 to 8.3).

Still from memory: SGA 4 XIV 3.1, 3.2 (Artin) and XVII 5.4.3, XII 5.1, XVIII 3.2.5, XVI; GOS (Raynaud, Bourbaki 286; SGA 5 X 7.1); SGA 1 V 8.2 and XIII 2.16; Hartshorne IV 2.4; SGA 7 XV 3.4 and XVIII 6.6; BBD 4.1.9 and 4.2.5; Laumon chapters 2 and 3 (stationary phase, local transforms, used by GEN); Kiehl-Weissauer Ch. III; Katz Asterisque 79; Adolphson-Sperber; Schmidt 1931 and Weil 1948.

## 7. What remains open, in order

1. (P_k) for infinitely many even k, or any substitute for (S_k') and (W*). Decides whether the route is a proof. GEN's plan:
   - Step 1: verify in primary sources that Fourier-transform exactness, local transforms and stationary phase are weight-free (Laumon chapters 1 and 2, BBD 4.1). Low to medium difficulty.
   - Step 2: prove (P_k) for all even k from the recursion, exact local statements for the trivial character and unipotent blocks. Medium difficulty. Fallback: (S_k') or (W*), very high difficulty, no known weight-free tool.
   - Step 3: referee Proposition X line by line. Low difficulty.
   - Step 4: choice of Q = q^m and h; trivial.
   - Step 5: k to infinity; done in Lean (`endgame`).
   - Tests first: T1 exact S_n(h) over F_(3^n), n <= 15, k = 2, checking d^2-d+1 exponentials; T2 the k = 3 prediction; T3 the referee pass.
2. Referee Proposition X (the Frobenius action on a geometrically constant quotient; E_2 versus E_infinity in the virtual count) and GEN's stationary-phase table. Neither has been seen by a second agent.
3. k = 4 residue: f = x^d - a (V_pi); X4 minus X1 (needs (Irr), (Loc0)); d_2 on those loci.
4. Primary-source check of the remaining memory citations in section 6, especially BBD 4.1.9 and weight use in Laumon chapters 2 and 3.
5. FS: stalks of Rj_*K on strata of codimension 2 or more, and onto-ness of H^{k-1}(Y,K) -> B^{k-1}.
6. Data gaps: K4C's three line exceptions against REF2's ten (unreconciled); k = 6 unexplained vectors; odd k.
7. Lean: strict inequality; link from the eigenvalue expansion to the `endgame` hypothesis; extension field c.

Nothing in this document is evidence about the Riemann Hypothesis for the integers.
