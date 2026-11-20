# Footnote 3 of the Remark: the "sign-only" route to the Weil bound

Scope. The Weil bound for y^2 = f(x) over a finite field is a theorem (Weil 1948). The question here is only whether the route sketched in footnote 3 of the four-page "Remark" is a valid proof of it, what that route needs, and whether it is already known. Nothing below says anything about the Riemann Hypothesis for the integers. Labels: PROVED (full argument given), CITED (standard theorem), CHECKED (exact integer arithmetic, with script and output file), OPEN, HINT (heuristic or search summary).

Verdict in one paragraph. Every step of the route is PROVED or CITED except one. That one is a sign statement about the cohomology of a quadric (called (S_k) or its weaker form (W*) below). It is not proved for any k >= 4, it is false for some explicit simple choices of the quadric, and every known way of proving it that we could think of uses weights (Weil-type purity), which would make the route circular. So the sketch is not a proof as it stands. It is a reduction of the Weil bound to an unproved vanishing statement.

Provenance. This account was assembled from the reports in `reports/`, the data in `compute/` and the Lean files in `lean/ToyWeil/`. The proofs in reports A, H and I (cohomological arguments) were not re-derived by the writer. The Lean files and the figures in section 4 were opened and read directly.

## 1. Statement

Let q be odd, f a squarefree polynomial over F_q of odd degree d >= 3, chi the quadratic character, t(x) = chi(f(x)), M = sum over x of t(x), r the number of roots of f in F_q. Let psi be a nontrivial additive character and Q_c(x) = c_1 x_1 x_2 + ... + c_{k-1} x_{k-1} x_k (the "path" quadric; the footnote's plain version has all c_i = 1). Put

    S(h) = sum over x_1..x_k of t(x_1)...t(x_k) psi(h Q(x)),
    N = sum of t(x_1)...t(x_k) over the zeros of Q.

Claim of the route: if the argument works for all k and all extensions F_{q^n}, then every Frobenius eigenvalue alpha of the curve satisfies |alpha| <= sqrt(q).

## 2. The argument in six steps

1. Identity. Summing over h first gives q N = M^k + R, with R = sum over h != 0 of S(h) and S(0) = M^k. PROVED (reports A, H). Lean: `orthogonality` (section 5). The same holds over every F_{q^n} with psi composed with the trace and chi with the norm.
2. Iterated Parseval. For h != 0, k-1 applications of the unitary-up-to-sqrt(q) Fourier step give |S(h)| <= (q - r) q^((k-1)/2), hence |R| <= (q-1)(q-r) q^((k-1)/2) < q^((k+3)/2) with a constant independent of n. PROVED (A, H). Lean: `parseval_step`, `iterated_bound`, `iterated_bound_rpow`, `Ssum_eq_path_sum`; the final multiplication by the q-1 values of h is not in Lean. (The footnote says "k times"; the argument uses k-1. The statement is unchanged.) By hand check: q=3, f = x^3-x+1, k=3 gives R = 18, bound 18, N = 15 (report H).
3. Eigenvalue expansion. The zeta function of the curve is rational (CITED: F. K. Schmidt 1931; Weil 1948) so M_n = -sum alpha_i^n over F_{q^n}, and M_n^k = (-1)^k sum over k-fold products of the alpha's, to the n-th power. This second form follows from the first (PROVED). The Grothendieck-Lefschetz trace formula and Kunneth (SGA 5, SGA 4 XVII) give q N_n as a signed sum of n-th powers of eigenvalues of H^*_c(Y, K) (CITED; Y = {Q = 0}, K = restriction of the k-fold external power of the extension by zero of the Kummer sheaf). Statement numbers are from memory and were not rechecked.
4. THE SIGN INPUT. Assume H^j_c(Y, K) = 0 for all j != k-1 (statement (S_k)). Then q N_n = (-1)^(k-1) times a sum of n-th powers, so R = (-1)^(k-1)(sum over E + sum over products) has every coefficient of one sign, and the coefficient of alpha_max^k in R is nonzero. OPEN for every k >= 4; see section 3. Only the weaker (W*) is needed.
5. No cancellation, exponent. If the coefficient of alpha_max^k in R_n is nonzero and |R_n| <= C B^n, then |alpha_max|^k <= B (a pole of the generating function cannot lie inside the disc of convergence). With B = q^((k+3)/2): |alpha_max| <= q^(1/2 + 3/(2k)). PROVED, and in Lean (`no_hidden_growth`, `no_cancellation`, `endgame`). This is the trivial bound at k = 3, q^(7/8) at k = 4, q^(3/4) at k = 6.
6. Limit k to infinity. If step 4 holds for infinitely many k with the same f and q, then |alpha| <= sqrt(q). PROVED given the input. Two caveats (section 3): at fixed q, genericity of c fails once k is of order log q, so c must be taken in F_{q^m} with m growing with k (PROVED in outline, report H); and for the infinite family one needs the input for infinitely many k, not just one.

Not treated: the second half of footnote 3 (Gabber's hypersurface, the Gauss-sum cover, the "complete graph"). It makes no checkable claim, and no agent attempted it. It says where the quadric came from, and the argument above does not use it.

## 3. The one input that carries the argument

Exact statement (report H):

(W*) For the fixed f over F_q (after translating x so that f(0) != 0, and allowing the quadric coefficients c in F_{q^m}, m = m(k)), for infinitely many even k there is a c such that in the unique expansion q^n N_n(c) - M_n^k = sum over gamma of r_gamma gamma^n, the coefficient r_gamma* of gamma* = alpha_*^k (alpha_* of maximal modulus) is nonzero.

Sufficient cohomological form (S_k): H^j_c(Y_c, K) = 0 for every j != k-1.

Referee verdict (H): CONDITIONAL_ON. The route proves the Weil bound exactly when (W*) is proved. The footnote's phrase "Bertini gives a definite sign from middle cohomology" is the claim (S_k); it does not follow from Bertini or from Artin vanishing. The pointwise sign of the integer N_n is not the claim: it is false at k = 2 (q=3, f = x^3-x+1 gives N = 5), and B and C found N_k of both signs, which is irrelevant for the same reason.

What agent I established:
- PROVED (all k, f, c): H^j_c(Y,K) = 0 for j < k-1, by Artin vanishing for the perverse sheaf K[k-1] on the affine hypersurface Y. The upper half is the content and is not formal.
- PROVED: (S_2) for every c. (S_3) when f(0) != 0 and f(x)f(-lambda x) is not a square (dimension 3d^2-3d+1); it fails when c_1 = -c_2.
- PROVED for k = 4: H^5_c = H^6_c = 0. And (S_4) FAILS whenever c_1+c_2+c_3 = 0, because the plane {x_1 = x_3, x_2 = x_4} lies in Y and contributes a class of eigenvalue q^2. This includes the plain path quadric c = (1,1,1) in characteristic 3.
- OPEN: H^4_c for c_1+c_2+c_3 != 0 (reduces to a monodromy statement about an explicit family of hyperelliptic curves); every k >= 5.

Where the agents disagree.
- Lower half. H says Artin vanishing needs non-characteristic restriction of Y to the root strata; I says it does not (K is one sheaf in one degree on an affine hypersurface). H's own tests show non-characteristic restriction fails in several cases (section 4). Not resolved here; I's argument is the shorter and does not use the condition, but it has not been checked independently.
- Failure at p = 3. H saw N_4 near +q^2 for x^3+x+1 and x^3-x over F_{3^n} and guessed a symmetry effect (HINT). I proves the cause: c = (1,1,1) has c_1+c_2+c_3 = 3 = 0. The two explanations are not exclusive; I's is a proof (unchecked by us), H's is a guess.
- Euler characteristic at k = 4. I derives -92 (d = 3) assuming Swan conductor 0 at singular points, and it matches A's hand count; H could not confirm it by point counts (section 4). Status: derived under an unproved assumption.
- Odd k. H shows the plain quadric fails non-characteristic restriction for every odd k >= 3; I proves (S_3) for generic c regardless. No contradiction, since I does not use that condition.

Circularity (HINT, from H and A). Steps 1, 2, 3, 5 use no weights. The input is where weights hide: known proofs of such concentration and no-coinvariant statements go through irreducibility or big monodromy, proved by purity or Weil II. A purity proof of (S_k) would contain the toy theorem. No weight-free proof of (S_k) for k >= 4 was found, and the footnote gives none. Also, the Rankin-type resemblance (positivity of a square, then weights) is a warning sign.

## 4. What exact computation showed

All figures below are exact integers or rationals and were copied from the named files (paths relative to `compute/`). None says anything about (S_k) for general k: at k = 4 the expected number of exponentials is about 92, and only a few values of n are reachable.

| Figure | File |
|---|---|
| Fast N_k routine equals brute force in 192 cases (p in 3,5,7,11; k = 1..4); equals pure-Python-integer DP in 24 more | `B/t1_output.txt` |
| Closed forms N_2 = 2 t0 M - t0^2 and N_3 = t0 M^2 + (M - t0) C hold for 315 (p, f) pairs, p <= 199; failures: 0 | `B/t2_output.txt` |
| Independent extension-field code (q <= 729): 128 comparisons with brute force, mismatches: 0 | `C/u3_validation.txt` |
| Same closed forms and spectral checks over F_{p^n}: TOTAL failures 0 | `C/u4_out.txt` |
| Agent C's table agrees with agent B's: 47 of 47 rows, mismatch 0 | `C/compare_B_out.txt` |
| Observed |S_h|^2 / p^k stays below 31.7369 (x^3-x, k=4, p=101, interval arithmetic, 348 cases); the proved bound is about p^(k+1) | `B/t4_summary.txt` |
| Largest N^2/p^3 at k=4 over 582 rows: 2096704/29791 (x^3+2x+5, p=31, N=1448) | `B/t3_summary.txt` |
| Odd f = x^3-x, k=5: N^2/p^4 reaches 85598097701776/43617904801 (p=457), while generic f stays much smaller (e.g. x^3+x+1: 56968619761/705911761 at p=163, still a different order from the odd f) | `B/t3_summary.txt` |
| Same curve, translated so f(0) != 0: at p=229, k=5, N = -1244068 for x^3-x against -28899 for its translate by 2; k=3: -6780 against -987 | `H/h2_out.txt` |
| Odd cubic x^3-x at p=5, k=3: N_3 = 4, 132, -2684, 8708 for n = 1..4 (coefficients of mixed sign, positivity fails) | `C/u4_out.txt` |
| Tangency (failure of non-characteristic restriction), plain quadric c = 1 and root sum zero: 6 tangent strata of 255 at k=4, 12 of 4095 at k=6; with random c: 0 | `H/h5_out.txt` |
| Same test, generic roots, k = 3 and k = 5, d = 3: 6 and 30 tangent strata for c = 1 (odd k fails); k = 4, 6: 0 | `H/h3_out.txt` |
| k = 4, p = 53: mean N_4/p^2 over eight f is 0.946 for c = (1,1,51) (c_1+c_2+c_3 = 0 mod p), 0.181 for c = (1,1,1), -0.037 for c = (1,2,3) | `I/i_k4_out.txt` |
| p = 3, f = x^3+x+1: N_4 = 195, 553, 6147, 43681, 520851 for n = 2..6 | `C/u3_validation.txt` |
| Euler characteristic at k=4: the point-count fit is not consistent with an integer-coefficient cubic; the fit's P(1) = -3318, against the claimed -92 | `H/h1_k4_out.txt` |

Reading. The data are consistent with the identity and the size of the Parseval bound (steps 1 and 2); with the closed forms at k = 2, 3; and with I's prediction that a persistent q^2 term appears when c_1+c_2+c_3 = 0. The f(0) = 0 anomaly (odd f) is a property of how the roots sit relative to the cone vertex, not of the curve. The Euler-characteristic check at k = 4 could not be completed from data. The values -5 and 19 for k = 2, 3 are stated in report H but are not in a saved output file; treat them as report-only.

## 5. What is formalised in Lean

Files: `lean/ToyWeil/Parseval.lean`, `lean/ToyWeil/PowerSum.lean`. Logs in `lean/logs/` show warnings only (unused variables, a deprecated `push_neg`) and no errors. Neither file contains `sorry`, an `axiom` declaration or `native_decide` (reports F and G; the writer read both files). Both compile with the supplied script (reports F and G give exit 0; the exit code itself is not recorded in the logs).

Context for Parseval.lean: `variable {F : Type*} [Field F] [Fintype F] [DecidableEq F] (psi : AddChar F ℂ)`, inside `namespace ToyWeil`. Statements, copied exactly:

    theorem orthogonality (hψ : psi ≠ 0) {X : Type*} [Fintype X] (g : X → ℂ) (Qf : X → F) :
        ∑ h : F, ∑ x : X, g x * psi (h * Qf x)
          = (Fintype.card F : ℂ) * ∑ x ∈ Finset.univ.filter (fun x => Qf x = 0), g x

    theorem parseval_step (hψ : psi ≠ 0) (u : F → ℂ) {h : F} (hh : h ≠ 0) :
        ∑ y : F, ‖∑ x, u x * psi (h * x * y)‖ ^ 2
          = (Fintype.card F : ℝ) * ∑ x, ‖u x‖ ^ 2

    theorem iterated_bound (hψ : psi ≠ 0) (t : F → ℂ) {h : F} (hh : h ≠ 0) (B : ℝ)
        (hB : ∀ x, ‖t x‖ ≤ B) (n : ℕ) :
        ‖Ssum psi t h (n + 2)‖
          ≤ Real.sqrt (Fintype.card F) ^ (n + 1) * B ^ n * ∑ x, ‖t x‖ ^ 2

    theorem iterated_bound_rpow (hψ : psi ≠ 0) (t : F → ℂ) {h : F} (hh : h ≠ 0) (B : ℝ)
        (hB : ∀ x, ‖t x‖ ≤ B) (k : ℕ) (hk : 2 ≤ k) :
        ‖Ssum psi t h k‖
          ≤ (Fintype.card F : ℝ) ^ (((k : ℝ) - 1) / 2) * B ^ (k - 2) * ∑ x, ‖t x‖ ^ 2

    def pathQuadric {k : ℕ} (x : Fin (k + 1) → F) : F := ∑ i : Fin k, x i.castSucc * x i.succ

    theorem Ssum_eq_path_sum (hψ : psi ≠ 0) (t : F → ℂ) (h : F) (n : ℕ) :
        Ssum psi t h (n + 1)
          = ∑ x : Fin (n + 1) → F, (∏ i, t (x i)) * psi (h * pathQuadric x)

(`Ssum` is the iterated recursion defined in the file; `Ssum_eq_path_sum` ties it to the path-quadric sum.) Here F is any finite field, not just a prime field.

PowerSum.lean (inside `namespace ToyWeil`):

    theorem no_hidden_growth {m : ℕ} (γ : Fin m → ℂ) (hγ : Function.Injective γ)
        (c : Fin m → ℂ) (hc : ∀ j, c j ≠ 0) (C ρ : ℝ) (hρ : 0 ≤ ρ)
        (h : ∀ n : ℕ, 1 ≤ n → ‖∑ j, c j * γ j ^ n‖ ≤ C * ρ ^ n) :
        ∀ j, ‖γ j‖ ≤ ρ

    theorem no_cancellation {A B : Type*} [Fintype A] [Fintype B] (a : A → ℂ) (b : B → ℂ)
        (C ρ : ℝ) (hρ : 0 ≤ ρ)
        (h : ∀ n : ℕ, 1 ≤ n → ‖(∑ i, a i ^ n) + ∑ j, b j ^ n‖ ≤ C * ρ ^ n) :
        ∀ i, ‖a i‖ ≤ ρ

    theorem endgame {d : ℕ} (α : Fin d → ℂ) (q : ℝ) (hq : 1 < q)
        (H : ∀ k : ℕ, 2 ≤ k → ∃ (B : Type) (_ : Fintype B) (b : B → ℂ) (C : ℝ),
          ∀ n : ℕ, 1 ≤ n →
            ‖(∑ I : Fin k → Fin d, (∏ j, α (I j)) ^ n) + ∑ j, b j ^ n‖ ≤
              C * (q ^ (((k : ℝ) + 3) / 2)) ^ n) :
        ∀ i, ‖α i‖ ≤ Real.sqrt q

Axiom lines from the logs. In `lean/logs/ToyWeil.Parseval.log`, for `iterated_bound_rpow`, `pathQuadric_snoc`, `gseq_path`, `Ssum_eq_path_sum`, `sum_psi_mul`, `orthogonality`, `parseval_step` and `iterated_bound`, each reads:

    'ToyWeil.<name>' depends on axioms: [propext, Classical.choice, Quot.sound]

In `lean/logs/ToyWeil.PowerSum.log`, for `le_of_pow_succ_le`, `no_hidden_growth`, `no_hidden_growth'`, `no_cancellation` and `endgame`, the same line. These are the standard Lean axioms.

What `endgame` says, and does not say. Its hypothesis H already contains the sign: the k-fold products of the alpha's and an arbitrary other family b enter with the same sign, with the bound q^((k+3)/2) per power, for every k >= 2. From H it concludes |alpha| <= sqrt(q). Whether H holds for the curve is exactly the unproved input of section 3.

Not formalised: the trace formula and Kunneth, the cohomological sign input, the passage to extension fields, the multiplication by the q-1 values of h, the extension of c to F_{q^m}, and anything about the Weil bound itself. No file exists for any of these.

## 6. Known or new

Not decided. The literature search (report E) found no source containing the footnote 3 argument (sum over h, path quadric, sign of middle cohomology against M^k, iterated Parseval), no MathOverflow, blog, Zulip or arXiv discussion of it, and news coverage of the Remark does not mention it. Absence in a few searches is not evidence of novelty. Almost all claims in E rest on search summaries; primary texts (SGA 4, BBD, Weil I and II, Stepanov, Bombieri, Katz) were not opened, and the Remark's PDF was unreadable through the fetch tool. HINT-level only.

Nearest relatives, and how they differ (all HINT):
- Rankin squaring in Deligne's Weil I and Katz's Weil II lectures: uses positivity of a Hermitian square and tensor powers; footnote 3 claims opposite signs of two eigenvalue families. Katz lectures: https://www.math.arizona.edu/~swc/notes/files/00KatzN.pdf ; Katz on smooth hypersurfaces: https://arxiv.org/pdf/math.NT/0504316
- Fouvry-Kowalski-Michel, "A study in sums of products": https://arxiv.org/abs/1405.2293 (takes Deligne's theorem as input).
- Stepanov 1971 and Bombieri: auxiliary polynomial with high multiplicity, no cohomology: https://geodesic.mathdoc.fr/item/IM2_1971_5_2_a3 ; Kopparty's notes: https://sites.math.rutgers.edu/~sk1233/courses/finitefields-F13/weil.pdf
- Artin vanishing and perverse weak Lefschetz (CITED as SGA 4 XIV 3.1 and BBD 4.1.1; the two sources' t-exactness wordings differ in snippets, check BBD): https://arxiv.org/pdf/0901.0660

The Remark calls its argument "a descendant of Stepanov's"; E sees no technical descent. The note's mentions of OpenAI results ("Siegel", triangle group, "Stepanov without multiplicity") were not identified. Quanta's report on the quasi-Riemann 7/8 claim: https://quantamagazine.org/ai-proved-the-quasi-riemann-hypothesis-what-happens-now-20261019 (summary only).

## 7. What the Lean archive of the claimed proof contains about this

Agent D read the archive only through the provided search scripts; nothing was extracted, built or run. Result (CHECKED as file text; coverage limited to name searches):
- The path-quadric argument is not formalised anywhere found. No Weil bound for sums or curves, Lang-Weil, Hasse-Weil, Frobenius-eigenvalue purity for varieties, Stepanov method or iterated Parseval was found.
- Nearest file: `FiniteFieldQuadraticFormPointCount.lean`. It proves, for one nondegenerate quadratic form in 2M variables over odd F_q, |#{Q = s} - q^(2M-1)| <= q^M, using the sum-over-h identity and an exact Gauss-sum modulus q^M. It has no weights t(x_i), no sign and no cohomology. It is the unweighted classical count.
- The folder `Development/WeilBound` is Weil representation, Siegel-Weil, theta-lift and Hodge-Tate material, not the Weil bound. `Formalism/FrobeniusOrbits` and `FrobeniusContraction` concern number-field Galois groups and window combinatorics.
- The two Parseval items found (`parsevalSep_identity`, `parsevalSep_bound`) are a single Plancherel step on Z/N, not k-1 iterations.
- The archive's own route (from `VWin`, `VVle`, `OpenLiteratureStatements`) is Galois cohomology and automorphy of Galois representations; it does not visibly use qN = M^k + R (HINT, from names and a few definitions).

Therefore the archive gives no formal check of footnote 3, and no evidence either way. Whether some unnamed lemma implements it, and whether any archive proof compiles, is OPEN.

## 8. Open items, in order of importance

1. (W*)/(S_k) for any k >= 4: no proof, and no weight-free route known. For k = 4 the remaining case is H^4_c when c_1+c_2+c_3 != 0 (a monodromy statement on an explicit family); for k >= 5 nothing is known. This decides whether the route is a proof.
2. Circularity: whether any proof of (S_k) can avoid weights, or whether it necessarily contains the toy theorem.
3. Explicit failures to account for: c_1 = -c_2 at k = 3 (any f), c_1+c_2+c_3 = 0 at k = 4, the matching hyperplanes for even k (survival into H^k_c unproved beyond k = 4), and f with symmetries (odd f). The plain all-ones quadric is in the bad set at k = 4 whenever 3 = 0 in F_q.
4. Uniformity in k at fixed q: choosing c in F_{q^m} with m growing, and showing good c exist for every even k; checked only for k <= 6 with random rational roots.
5. Non-characteristic restriction at infinity; and the disagreement between H and I about whether the lower-half Artin step needs it.
6. Euler characteristic -92 at k = 4: depends on an unproved Swan-conductor assumption; a data check failed to confirm it.
7. Primary-source check of every CITED statement number (SGA 4, SGA 5, BBD, Kunneth, Artin vanishing); E and the derivations quote several from memory.
8. Literature status of the route (known or new): primary texts not opened.
9. Second half of footnote 3 (Gabber hypersurface, Gauss-sum cover): not treated.
10. Lean: the sum over h != 0 multiplication and the link from step 3 to the Lean `endgame` hypothesis are not formalised.

Nothing in this account is evidence about the Riemann Hypothesis for the integers. Finite computations cannot show that an argument valid for all primes is valid.

---

## 9. Main session check (Claude Fable 5.2, 2026-11-20 18:05 UTC)

Sections 1 to 8 were written by the synthesis agent. This section is the orchestrating session's own check.

Re-run by me:
- Both Lean files recompiled with `tools/lean_check.sh`: exit 0, and the thirteen `#print axioms` lines read
  `[propext, Classical.choice, Quot.sound]`. A text search finds no `sorry`, `axiom`, `native_decide` or `unsafe`.
  The recursion `gseq` and the definition `pathQuadric` are what section 5 says they are.
- An exact spot check written without reading the agents' code (`compute/main-session-check/spotcheck.py`,
  output `spotcheck_out.txt`, 0 failures): my routine against brute force (5 cases); the closed forms for N_2 and
  N_3 (60 cases); N_4 = 1448 for x^3+2x+5 at p = 31; 78 rows of `B/n4_table.tsv` recomputed with 0 mismatches; the
  five characteristic-3 values 195, 553, 6147, 43681, 520851; the plane {x_1 = x_3, x_2 = x_4} carrying (p-r)^2;
  and the count q^3 + q^2 - q for the trivial weight.
- Every figure in the table of section 4 was found in the file named beside it.

On the disagreement about the lower half: I checked agent I's argument and it holds without any genericity.
K[k-1] is a single sheaf placed in degree -(k-1) on a variety of dimension k-1, so it satisfies the support
condition; the restriction of a perverse sheaf to a divisor with affine complement, shifted by -1, satisfies the
cosupport condition; Artin vanishing then gives H^j_c = 0 for j < k-1. Agent H's extra condition is not needed.

A sharper form of the open input, derived by me and NOT checked by anyone else (treat as OPEN):
- Summing over h in the affine line and splitting off h = 0 gives, using only the lower half, an exact sequence
  0 -> (k-fold tensor power of H^1_c of the line) -> H^(k+1)_c of the exponential sum over h != 0 -> H^(k-1)_c(Y,K)(-1) -> 0.
  So the k-fold products of the eigenvalues always sit in the middle cohomology of the sum R.
- For fixed h != 0 the k-variable sum is the cohomology of the line with coefficients in a perverse sheaf built by
  k-1 rounds of "Fourier transform, then multiply by the character sheaf" (the sheaf form of iterated Parseval).
  That cohomology lives in two degrees only. Consequently H^j_c(Y,K) can be nonzero only for j = k-1, k and k+1.
- The wrong-parity group H^k_c(Y,K) is then the group of coinvariants, in the h direction, of the local system
  h -> (middle cohomology of the sum at h), up to a Tate twist. The sign input is a statement about constant
  quotients of that one local system. The plane found by agent I at c_1+c_2+c_3 = 0 is such a constant quotient.
  The Fourier transform and its exactness need no weights, so this formulation may avoid the circularity that
  section 3 worries about. That is a suggestion, not a result.

Two cautions on sections 3 and 8. First, "false for some c" does not refute the route, since the route may choose
c; it refutes the footnote's plain all-ones quadric in characteristic 3 at k = 4. Second, when some power of an
eigenvalue is a power of q (supersingular curves), a wrong-parity class with eigenvalue a power of q could cancel
alpha^k for infinitely many k, so that case needs its own argument. Not checked.
