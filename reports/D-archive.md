# D-archive: what the Lean archive contains that corresponds to footnote 3

Agent D (archive reader), 2026-11-20. Read-only: only `declgrep.py` and `tgrep.py` were used; nothing was extracted, built or run. Everything below is reading of text. A name is a label chosen by the archive's authors; where a statement is guessed from names it says so. Labels: PROVED / CITED / CHECKED / OPEN / HINT. No build was done, so CHECKED below means only "read in the file text", never "compiles". Nothing here says anything about the Riemann Hypothesis for the integers or about whether the archive's proofs are correct.

## Short answer

1. The toy argument of footnote 3 (path quadric, weights t(x_1)...t(x_k), iterated Parseval, sign of middle cohomology, comparison with M^k) is NOT formalised anywhere I could find. I found no name or statement for a path quadric, an iterated Parseval, a Frobenius-eigenvalue or Weil-number statement for a variety over a finite field, a point-count identity for a variety, Lang-Weil, Hasse-Weil, a Weil bound for character sums or curves, or Katz-style bounds. (Coverage caveat at the end.)
2. The one file in the neighbourhood is the elementary `FiniteFieldQuadraticFormPointCount.lean`: for ONE nondegenerate quadratic form in an even number 2M of variables over a finite field of odd characteristic, |#{Q(x)=s} - q^(2M-1)| <= q^M. It is the UNWEIGHTED, Gauss-sum-cancellation analogue of the "sum over h first" step. No weights t(x_i), no sign, no cohomology, no Parseval iterated k times. A grep of `CompanionTheory/` shows it is cited only by `LocalQuadraticDensityNearOne.lean` (a local-density lemma on the Siegel-Weil side).
3. `Development/WeilBound` is confirmed to be Weil representation / Siegel-Weil / theta lifts / Casselman-Wallach / p-adic Hodge material, not the Weil bound for curves. `Formalism/FrobeniusOrbits` and `Formalism/FrobeniusContraction` are not about Frobenius eigenvalues of varieties either.
4. The archive's own route to its five final statements, as visible from `VWin`, `VVle` and `OpenLiteratureStatements`, goes through Galois cohomology and Selmer/Sha lengths in CM and cyclotomic fields, Euler systems, theta lifts and automorphy of Galois representations. Nothing visible mentions an identity `qN = M^k + R`. So the archive neither contains nor visibly relies on the toy argument. This is a reading of names and a few definitions (HINT).

## Question 1: is the toy argument formalised?

### 1a. `FiniteFieldQuadraticFormPointCount.lean` (full file read)
Module `CompanionTheory.SpectralGeometry.LocalGlobalProofs.AdelicAnalysis.FiniteFieldQuadraticFormPointCount` (166 lines), namespace `GlobalTheory.CompanionTheory.SW.QuadricCount`.

- `sum_char_dot`: for a nontrivial additive character psi and w != 0, sum over y of psi(y . w) = 0.
- `gauss_mul_conj`: for symmetric B with det B != 0, t != 0, 2 != 0: G * conj(G) = q^(card iota), G = sum_x psi(t * quadForm B x). (The proof, as read, is the standard square-and-sum-over-the-dual-variable trick.)
- `norm_gauss`: ||G|| = q^M when card iota = 2M.
- `count_mul_card`, the "sum over h first" identity, exact statement:

      theorem count_mul_card (ψ : AddChar k ℂ) (hψ : ψ ≠ 1) (B : Matrix ι ι k) (s : k) :
          (Nat.card {x : ι → k // quadForm B x = s} : ℂ) * (Fintype.card k : ℂ) =
            ∑ t : k, ψ (-(t * s)) * ∑ x, ψ (t * quadForm B x)

  In ordinary terms: q times the number of solutions of Q(x)=s equals a sum over the dual variable t (the footnote's h) of twisted Gauss sums; the t = 0 term is q^(card iota). This matches the first two bullets of the FOOTNOTE.md reading, in the unweighted case only.
- `quadric_count_even`, exact statement:

      theorem quadric_count_even : ∀ (k : Type) [Field k] [Fintype k], ringChar k ≠ 2 → ∀ (ι : Type) [Fintype ι] [DecidableEq ι] (M : ℕ), Fintype.card ι = 2 * M → 1 ≤ M → ∀ (B : Matrix ι ι k), B.IsSymm → B.det ≠ 0 → ∀ s : k, |(Nat.card {x : ι → k // (2 : k)⁻¹ * (x ⬝ᵥ (B *ᵥ x)) = s} : ℝ) - (Fintype.card k : ℝ) ^ (2 * M - 1)| ≤ (Fintype.card k : ℝ) ^ M

  Ordinary terms: a nondegenerate quadric in 2M variables over F_q, q odd, has q^(2M-1) +- q^M points, for every value s. Re-exported as `GlobalTheory.T.finite_field_quadratic_form_point_count`.
- What it is NOT: no weights t(x_1)...t(x_k); no sign statement; no cohomology; no extension fields F_{q^n}; and no use of the path form x_1x_2+...+x_{k-1}x_k (it takes any invertible symmetric B). Whether the path form has invertible B for even k is not stated in the file; I did not check it (OPEN, standard fact believed). The content is textbook (CITED as known mathematics: Lidl and Niederreiter, Finite Fields, the theorems on the number of solutions of a quadratic form), not new.

### 1b. Name searches for the other ingredients
Regex searches over the 1,057,805 declaration names, plus narrow folder greps:

- Gauss sums: `gaussSum`, `gauss_fin`, `gauss_hermitian`, `norm_gaussSumAt_sq`, `gaussSumAt_normSq`, `GlobalTheory.T.heckeLocalGaussSum_norm_sq_eq_absNorm_pow` (Hecke Gauss sums over number-field residue rings, norm squared equals absolute norm power; by name), `gauss_dvd`. None is a Weil bound.
- `quad_sum_char_pi`, `quad_char_skew`, `quad_count` in `Development.AbelianVarietyTheory.Proofs.FlagMeasures.CardHermitianQuadricAffineSubspaceResidueRing` (exported as `GlobalTheory.T.card_hermitianQuadric_affineSubspace_residueRing`): counts on a Hermitian quadric over a residue ring. Not read; guess: Gauss-sum counting, unweighted.
- Point counts, Weil numbers, Lang-Weil, zeta function of a variety, Lefschetz: no match. `weilNumber`-like hits are Chern-Weil numbers (unrelated). `localZeta` hits are local zeta integrals of the doubling method. `TraceFormula` hits are Hecke/trace formulas on automorphic side.
- `hasseNormPrinciple*`: Hasse norm theorem, unrelated to Hasse-Weil.
- Bertini: `bertini_simple_zeros_generic_sections`, `bertini_strata_cotangent` etc. (algebraic-geometry/commutative-algebra Bertini, by name). Nothing links Bertini to a sign of middle cohomology of a quadric over a finite field.
- Stepanov / multiplicity: all hits are representation-theoretic multiplicity (multiplicity one, multiplicity spaces). No auxiliary-polynomial vanishing multiplicity. `GlobalTheory.T.riemann_inequality_cofinal_functionField` appears (by name a Riemann-Roch-type inequality, not RH).
- Katz: only `KatzMessingTheorem` (p-adic Hodge), `KatzEtDualOfIso`, `KatzQuasiIntegralCriterion`. Gabber: no hit.
- Frobenius: `frobeniusTorus_*`, `FrobeniusOrbit*`, `FrobeniusOnTorsion`, `FrobeniusActsOnTypeAtValuation`, `ExistsMaxUnramifiedFrobeniusTame`: Frobenius as Galois or torus element, not eigenvalues on cohomology.

### 1c. The folders named in the task
- `Development/WeilBound/...` declaration counts by sub-folder (top): RepresentationTheoryGL.ArchimedeanBaseChange 6597, CoreStatements.AutomorphicKernels 6457, RepresentationTheoryGL.SiegelWeilProof 5140, CoreStatements.PadicHodgeComparison 4805, CoreStatements.PublishedTheorems 2759, RepresentationTheoryGL.UnitaryDualProof 2482, CoreStatements.HodgeTatePoints 2393, then ThetaLifts.* and others. PublishedTheorems sub-folders include CasselmanWallach.*, ClozelPurity, CuspidalMultiplicityOne, GlobalEulerCharacteristic, FiniteGLInvariants. CONFIRMED: Weil representation, Siegel-Weil, theta lifts, Hodge-Tate, Casselman-Wallach; not the Weil bound for curves. The name is a label. Two names not read: `CasselmanWallach.ZetaClassicalZeroFreeRegion`, `CasselmanWallach.EtaleCohomologyNegativeVanishingDegreeZero`.
- `GroundTheory/FunctionField`: modules PlaceDefs, Repartition, Divisor, WeilDifferential, PlaceSum, PlaceBridge, PlaceAbove, ExistsBoundDegSubFinrankL, DivisorDegree, ValuationAevalSubCoeffZeroLe, Approximation (10 to 44 declarations each). By names: places, divisors, repartitions (adeles), Weil differentials, Riemann-Roch-type dimension bounds. No zeta, no point counts, no RH. Not read in full.
- `Formalism/FrobeniusOrbits/Statement.lean` (read in part): `HostHyp q d := q.Prime ∧ d.Prime ∧ q % 8 = 3 ∧ d % 16 = 7 ∧ jacobiSym (-(d : ℤ)) q = 1`, groups `GG e := G0 × HGrp e` with `HGrp e := (ZMod (2 ^ (e + 2)))ˣ ⧸ zpowers (-1)`, subfields of cyclotomic-type fields, CM types. Galois groups of 2-adic towers; same shape as `WinPair` below. Not Frobenius eigenvalues over a finite field.
- `Formalism/FrobeniusContraction/StatementTop.lean` (read in part): `sg`, `InWin`, `FarWin`, `Low`, `Cl`, `SgBound`, `LemmaS`, `LemmaD`: floors of series in ell, windows of integer multisets, a lemma about modules over a local ring (Wach-module-like combinatorics). Not Frobenius eigenvalues of varieties.
- `Development/AbelianVarietyTheory/Proofs/CharacterTheory`: finite-field-flavoured character theory of tori and GL over F_q; see Q2.

## Question 2: integer-side and footnote-ingredient analogues

Honest summary: I found NO statement of the shape "weighted count = main term + remainder" on the integer side, no iterated Parseval, no sign or positivity statement on middle cohomology, and no Stepanov-style multiplicity step. Below are the neighbours (twelve items). Items 1-6, 9 and 10, 11 are quoted exactly from files I read; items 7, 8, 12 say so where only names or definitions were read.

1. `quadric_count_even` (module of 1a; also `GlobalTheory.T.finite_field_quadratic_form_point_count`). Statement quoted in 1a. A nondegenerate even-dimensional quadric over odd F_q has q^(2M-1) +- q^M points. Closest thing to "count = main + remainder"; unweighted.
2. `count_mul_card` (same module). Quoted in 1a. q times the solution count equals a sum over the dual variable of twisted Gauss sums: the footnote's "sum over h first", unweighted.
3. `norm_gauss` (same module), exact:

       theorem norm_gauss (ψ : AddChar k ℂ) (hψ : ψ ≠ 1) (h2 : (2 : k) ≠ 0) {B : Matrix ι ι k} (hB : B.IsSymm) (hdet : B.det ≠ 0) {M : ℕ} (hM : Fintype.card ι = 2 * M) {t : k} (ht : t ≠ 0) : ‖∑ x, ψ (t * quadForm B x)‖ = (Fintype.card k : ℝ) ^ M

   The quadratic Gauss sum in 2M variables has absolute value exactly q^M: the "Gauss sum cancellation" that footnote 3 says it replaces by iterated Parseval. With no weights it is exact.
4. `parsevalSep_bound` (module `Development.AbelianVarietyTheory.Proofs.CharacterTheory.ParsevalBoundIntegerVectorSmallFourierSupport`; exported as `GlobalTheory.T.parseval_bound_integerVector_smallFourierSupport`), exact:

       theorem parsevalSep_bound : ∀ (n N : ℕ) (ω : ℂ) (c : ℕ → ℤ) (S : Finset ℕ), 0 < n → 0 < N → IsPrimitiveRoot ω N → ∑ k ∈ Finset.range N, c k ^ 2 = 2 * n → |∑ k ∈ Finset.range N, c k| ≤ (n : ℤ) - 1 → (∀ j : ℕ, 0 < j → j < N → j ∉ S → ∑ k ∈ Finset.range N, (c k : ℂ) * ω ^ (j * k) = 0) → 2 * n * N ≤ (n - 1) ^ 2 + 4 * n ^ 2 * S.card

   For an integer vector on Z/N with sum of squares 2n and sum at most n-1 in absolute value, whose Fourier transform vanishes off S, N is at most (n-1)^2/(2n) + 2n|S|. The proof (read) is one Plancherel step plus a trivial bound: one Parseval, on a cyclic group, not k-1 iterations, and no quadric. Its use is unclear (guess from the folder name: a lemma about characters of GL over F_q). It is the only "Parseval bound with explicit constants" I found.
5. `frobeniusTorus_character_orthogonality` (module `...CharacterTheory.FrobeniusTorusCharacterOrthogonalityStatement`), exact:

       theorem _root_.GlobalTheory.T.frobeniusTorus_character_orthogonality : ∀ (F : Type) [Field F] [Finite F] (θ : AlgebraicClosure F →* ℂ), (∀ x y : AlgebraicClosure F, x ≠ 0 → y ≠ 0 → θ x = θ y → x = y) → ∀ n : ℕ, 0 < n → (∃ ζ : AlgebraicClosure F, IsPrimitiveRoot ζ (Nat.card F ^ n - 1) ∧ IsPrimitiveRoot (θ ζ) (Nat.card F ^ n - 1)) ∧ ∀ k l : ℕ, ∑ᶠ α ∈ {α : AlgebraicClosure F | α ^ (Nat.card F ^ n - 1) = 1}, θ α ^ k * star (θ α ^ l) = if k ≡ l [MOD Nat.card F ^ n - 1] then ((Nat.card F ^ n - 1 : ℕ) : ℂ) else 0

   Orthogonality of the characters alpha -> theta(alpha)^k on the (q^n - 1)-th roots of unity in the algebraic closure of F: the multiplicative-character orthogonality needed to "pass to all extension fields". Not a statement about a variety.
6. `frobeniusTorus_minpoly_degree_rootPowerSum` (same folder), exact:

       theorem _root_.GlobalTheory.T.frobeniusTorus_minpoly_degree_rootPowerSum : ∀ (F : Type) [Field F] [Finite F] (θ : AlgebraicClosure F →* ℂ) (n : ℕ), 0 < n → ∀ α ∈ {α : AlgebraicClosure F | α ^ (Nat.card F ^ n - 1) = 1}, (minpoly F α).natDegree ∣ n ∧ (minpoly F α).coeff 0 ≠ 0 ∧ ∀ k : ℕ, rootSum θ k (minpoly F α ^ (n / (minpoly F α).natDegree)) = ∑ i ∈ Finset.range n, θ (α ^ Nat.card F ^ i) ^ k

   A power sum over the roots of minpoly^(n/d) equals the sum over the Frobenius orbit of alpha^k: a "sum of k-th powers over Frobenius conjugates" identity (finite-group character theory of GL_n(F_q); a companion `GlobalTheory.T.innerProduct_rootPowerSum_eq_of_frobenius_modEq` is in the same folder). The algebra the footnote's "sum of n-th powers of Frobenius eigenvalues" would sit on, but no variety appears.
7. `UpperTheory.Top.VVle`, `VWinAt`, `VWin` (module `Development.AutomorphicArithmetic.CharacterBoxes.ExistsPageN`), exact:

       def VVle (E : Type) [Field E] [NumberField E] (t : ℕ) (B : ℝ) : Prop :=
         ∀ (Ω : Type) [Field Ω] [Algebra E Ω] [IsAlgClosure E Ω] (ld : ∀ (p : ℕ) [Fact p.Prime], Formalism.GaloisCohomology.LData E Ω p),
           (∀ (p : ℕ) [Fact p.Prime] (e : ℕ), 0 < e → e < t → Formalism.GaloisCohomology.shaLen (ld p) (e : ℤ) ≠ ⊤) ∧
           ∀ S : Finset Nat.Primes,
             ∑ l ∈ S, Real.log (l : ℕ) *
               ∑ e ∈ Finset.Ico 1 t, ((@Formalism.GaloisCohomology.shaLen E Ω _ _ _ _ _ l ⟨l.2⟩ (@ld l ⟨l.2⟩) (e : ℤ)).toNat : ℝ) ≤ B

       def VWin : Prop := ∀ ψ : PChar, VWinAt ψ 401

   (`VWinAt` is a long statement about primes q, d in a window: q % 8 = 3, d % 16 = 7, q | d + 1, with scale Y and `VAt ψ eps Ct q d (e x) x` for all x in [Y, Y^2].) In ordinary terms: the archive's top hypothesis `VWin` is a bound, uniform over all l-adic Galois cohomology data, on a log-weighted sum of Sha lengths for fields cut out by a character psi in a 2-adic tower. This is the quantity the RH chain is built on; it is Galois-cohomological, not the toy sign argument. (`UpperTheory.EveryCharacter` is defined at `...CharacterBoxes.EveryCharacter`, line 13.)
8. `UpperTheory.LiteratureTheorems.OpenLiteratureStatements` (module `...ThetaPairLifts.ThirdPlaceSeries.EveryCharacterOfLiteratureOfVWin`, line 215), exact:

       structure UpperTheory.LiteratureTheorems.OpenLiteratureStatements : Prop where
         caraianiLocalGlobalDual : _root_.UpperTheory.One.M.Row
         localLanglandsExists : _root_.UpperTheory.Zero.LLC.RecTExists
         galoisRepOfPolarizedPairLit : _root_.UpperTheory.One.M.Row

   Local-global compatibility and local Langlands inputs; the theorems under it are `deligne_ribet_of_literature`, `partial_zeta_functional_equation_of_literature`, `global_artin_reciprocity_of_literature` and so on. None is a Weil bound. The "automorphy" here is of Galois representations over number fields, not the footnote's "holo/automorphy over a function field".
9. `GlobalTheory.Published.ClozelPurity` (module `Development.AbelianVarietyTheory.PublishedTheorems.GaloisGeometry₂.ClozelPurity`), exact:

       def ClozelPurity : Prop :=
         ∀ (E : Type) [Field E] [NumberField E] [IsTotallyComplex E] (a : ℕ), 1 ≤ a → ∀ π : CuspSub E a,
           (∀ τ, ∀ z ∈ (CG.mk π).infChar τ, ∃ n : ℤ, z = (n : ℂ) + ((a : ℂ) - 1) / 2) →
           ∃ w₀ : ℤ, ∀ τ : E →+* ℂ,
             (CG.mk π).infChar ((starRingEnd ℂ).comp τ) = ((CG.mk π).infChar τ).map fun z => (w₀ : ℂ) - z

   Clozel's purity lemma: a regular algebraic cuspidal representation of GL_a over a totally complex field has complex-conjugation-symmetric infinitesimal characters with a common weight w0. A "purity of weights" statement, but about archimedean characters, not absolute values of Frobenius eigenvalues. It is a `def : Prop` (a target), restated in `Development.WeilBound.CoreStatements.PublishedTheorems.ClozelPurity.Bridge` as theorem `clozelPurity`.
10. `parsevalSep_identity` (module of item 4), exact:

        theorem parsevalSep_identity (N : ℕ) (ω : ℂ) (hN : 0 < N) (hω : IsPrimitiveRoot ω N) (c : ℕ → ℤ) : ∑ j ∈ Finset.range N, ‖∑ k ∈ Finset.range N, (c k : ℂ) * ω ^ (j * k)‖ ^ 2 = (N : ℝ) * ((∑ k ∈ Finset.range N, c k ^ 2 : ℤ) : ℝ)

    Discrete Plancherel on Z/N for an integer vector. The Parseval step footnote 3 would apply k-1 times; here it appears once.
11. `sum_char_dot` (module of item 1), exact:

        theorem sum_char_dot (ψ : AddChar k ℂ) (hψ : ψ ≠ 1) {w : ι → k} (hw : w ≠ 0) : ∑ y : ι → k, ψ (y ⬝ᵥ w) = 0

    Additive-character orthogonality, which makes "sum over h first" work.
12. (names only, not read) `quad_count` and relatives in `...FlagMeasures.CardHermitianQuadricAffineSubspaceResidueRing`; `gauss_hermitian` in `...DivisorProofs.GaussSumNondegenerateFiniteHermitianModule` (line 458). Guess from names: Hermitian analogues of items 1-3, unweighted.

No item matches "sign of the cohomology". Names with the word sign or purity in other places (`card_eigenvalues_sign_add`, `LieAlgebraEigenDecompositionCMSignature`, `sixth_weight_purity`) were not read; I expect real-analysis eigenvalue signs and CM signature, a guess only.

## Question 3: anything that contradicts or sharpens the reading in FOOTNOTE.md

(a) Supports and sharpens, in the unweighted case: the archive proves that summing over the dual variable first gives q times the count, that the zero mode is q^(card iota), and that the Gauss sum has modulus exactly q^M. There the remainder is bounded by (q-1) q^M, a trivial sum of moduli, with no Parseval iteration. So the footnote's phrase "Gauss sum cancellation replaced by iterated Parseval" is a real departure from this elementary method, and the archive gives no formal version of the replacement.

(b) A gap the reading should state: FOOTNOTE.md bullet 1 takes weights t(x) = chi(f(x)); the archive's theorem has no weights. With weights, the sum over the zeros of the quadric of the product of t-values is not a point count. Its identification with a trace of Frobenius on a single cohomology degree (needed for the "sign" bullet 5) is exactly the part absent from the archive. OPEN.

(c) No contradiction with bullets 2-4 of the reading. Bullet 5 (definite sign from middle cohomology, opposite to the sign on the M^k side) has no counterpart anywhere I looked, in formal or informal form (the archive has few comments).

(d) The route actually taken by the claimed proof, from the definitions of `VWin`, `VVle`, `OpenLiteratureStatements`, is Galois cohomology (Sha lengths), Euler systems and automorphy of Galois representations over number fields. It does not visibly use `qN = M^k + R`. This is consistent with the Remark calling the toy setting an inspiration, but it means the archive provides no formal check of footnote 3 and no evidence either way on whether the footnote's sketch is a valid proof. (HINT, from names and a few definitions.)

(e) Misleading names, as warned: `Development/WeilBound` (Weil representation), `Formalism/FrobeniusOrbits` and `FrobeniusContraction` (number-field Galois groups; p-adic window combinatorics), `Bertini` (commutative algebra), `Katz*` (Katz-Messing), `multiplicity` (representation theory).

## How far the search went

- declgrep name searches (case-insensitive): weilNumber, langWeil, pointCount/point_count/card_points/numPoints/rationalPoints, zetaFunction/localZeta, lefschetz/traceFormula, hypersurface, bertini, parseval, vwin, quadric, purity, gaussSum, eigen/frob/sqrt/card combinations, module matches for WeilBound, katz, gabber, stepanov, and exports under `GlobalTheory.T.*` containing weil, frobenius, pointcount, character_sum, parseval, stepanov, hasse, zeta_function, katz, bertini, gabber.
- Several patterns are loose (for example "pointcount" also matches many `rationalPoints` lemmas), and a relevant statement could hide under a name I did not guess (for example a point-count lemma with an opaque name, or a path-quadric lemma named by letters). A reliable negative would need a search by statement shape on a built environment, which was not done.
- Files read in full: the quadric file, its Statement file, the Parseval file, `ExistsPageN.lean`, `ClozelPurity.lean`, and the four `CharacterTheory` Statement files. Read in part: `FrobeniusOrbits/Statement.lean`, `FrobeniusContraction/StatementTop.lean`, `EveryCharacterOfLiteratureOfVWin.lean`. Everything else is names. Not searched: the bodies of the 186 `LiteratureTheorems`, `HodgeTatePoints`, `PadicHodgeComparison`.

## Labelled findings

- CHECKED (file text only; nothing compiled): `quadric_count_even` states |N - q^(2M-1)| <= q^M for one nondegenerate even-dimensional quadric over odd F_q; `count_mul_card` is the sum-over-dual-variable identity; `norm_gauss` is ||G|| = q^M; `parsevalSep_identity` and `parsevalSep_bound` are one-step Plancherel statements on Z/N.
- CHECKED (name searches, coverage caveat above): no statement matching Weil number, Lang-Weil, Hasse-Weil, zeta of a variety, Frobenius-eigenvalue absolute value, Stepanov method, path quadric or iterated Parseval.
- CHECKED (folder listing and names): `Development/WeilBound` is Weil-representation, Siegel-Weil, theta-lift, Hodge-Tate and Casselman-Wallach material.
- OPEN: whether an unnamed lemma implements the weighted version of footnote 3; whether the path form's matrix is invertible for even k (standard, unchecked); the correctness of any archive proof (nothing built).
- HINT: the archive's route to its five theorems is Galois-cohomological and automorphic and does not visibly use footnote 3.
