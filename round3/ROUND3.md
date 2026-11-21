# Round three: write-up

Scope. Character sums over finite fields, where the bound is a theorem of Weil (1948). Nothing here says anything about the Riemann Hypothesis for the integers. Labels: PROVED (argument in a report), CITED (OPENED or NOT OPENED), CHECKED (exact computation or Lean, file named), OPEN, HINT. Reports are in `round3/reports/` (A reduction referee, B Fourier induction, C small cases, D sources and novelty, E exact L-functions, F Lean, H general referee, I Fourier referee); the assembled draft is `round3/PROOF_DRAFT.md`. I opened all of those files, `Endgame2.lean`, its log, `compute/NUM/predicted_vs_observed.txt` and `round2/ROUND2.md`. I recompiled and re-ran nothing. Notation as in BRIEF.md.

## 1. Verdict in five lines

1. The route is not yet a complete proof, even modulo cited theorems. It is a proof of a conditional statement.
2. The statement: for q odd and f squarefree of odd degree d >= 3 over F_q, if the fibre statement (Claim B) holds for infinitely many k, then |alpha_i| <= sqrt q for every embedding of Q-bar_l in C. Equality then follows from a duality step (draft S11) that only referee H has checked.
3. No false step was found by any of the three referees (A, H, I). Referee I calls the Fourier step proved modulo cited statements; referee H calls the whole draft GAPS. They disagree, and I do not pick a side.
4. The disagreement is one item: the local structure of the transformed sheaves (draft S5 step 3, tameness and the singular sets), which rests on Laumon 1987 as read from a garbled text layer. Nobody has read page images.
5. Nothing is claimed beyond that. The draft itself calls its result conditional.

## 2. Claim A: the theorem as refereed

Referee A (verdict REDUCTION_HOLDS_WITH_CHANGES), re-derived from the brief before reading the earlier reports; referee H re-derived the same steps independently and found them correct.

Theorem A' (PROVED modulo CITED, NOT OPENED by A: Laumon 1.3.2.3, BBD 4.1.1 and 4.1.2, SGA 4 Kunneth, trace formula, Poincare duality on curves). Let q be odd, F_Q a finite extension, f in F_q[x] not a constant times a square, k >= 2, c in (F_Q^*)^(k-1). Assume H^(k+1)_c(A^k, F_h) = 0 at the geometric generic point of the h-line (P_k^c). Then |alpha_i|^k <= q^((k+3)/2) for every i and every embedding.

Changes to the brief's Claim A:
- The wrong-parity group is a quotient of H^2_c(G_m, R^k) = C(-1), namely the cokernel of d_2, not equal to it. Harmless: the argument only needs "quotient". Under Claim B, R^(k+1) = 0 and it is equal.
- Hypotheses made explicit: L geometrically nontrivial; all c_i nonzero; vanishing needed at every h != 0 for the fibre degrees (automatic); (P_k^c) at the generic point only (one closed point is not enough).
- "alpha of largest modulus" is unnecessary.
- The hypothesis "L nontrivial" is essential. CHECKED (compute/A/check_A.py, check_A_out.txt): for the trivial sheaf, k even >= 4, (P_k^c) holds yet the conclusion is false.
- Disagreement settled: A left (P_3^c) at c_1 = -c_2 undecided; C proved H^4_c = 0 there by hand (not contradictory, the wrong-parity terms sit in H^2_c(G_m, R^3)).

## 3. Claim B: the theorem as refereed

Theorem B' (B's induction, refereed by I and H). Let p be odd, f squarefree, f(0) != 0, c_i != 0, h != 0, and rho_i = -c_(i-1)/c_i. Put Sigma_1 = {0}, Sigma_2 = rho_2 Z, Sigma_i = rho_i (Z union Sigma_(i-2)). If Z is disjoint from Sigma_i for 2 <= i <= k-1 (condition G_k), then H^j_c(A^k, F_h) = 0 for j != k.

Genericity conditions (R = root ratios z'/z, including 1): k=3: rho_2 not in R. k=4: rho_2, rho_3. k=5: rho_2, rho_3, rho_4, rho_4 rho_2. k=6 adds rho_5, rho_5 rho_3. They do not involve h (h cancels). The all-ones quadric fails from k = 5. Referee I derived the singular sets independently (proper base change plus Grothendieck-Ogg-Shafarevich) and got the same sets with equality. A script (compute/I/sigma_check.py) agrees for k <= 6; I notes it codes the same rule, so it checks arithmetic, not theory.

Repairs to B: R must contain 1; irreducibility needs surjectivity of pi_1(V - Z) -> pi_1(V) (I replaced SGA 1 V 8.2 by a three-line argument); B's unresolved sign note on the vanishing-cycle module E_s was resolved by I (the sequence runs 0 -> i_*W -> j_!M[1] -> P -> 0). The criterion at a root where Q_i is singular: j_!N is the middle extension iff the tame generator has no eigenvalue -1 on M'^(P_z). The hypothesis is sufficient, not necessary (d = 1, q = 3, k = 3, c = (1,-1): cohomology in degree 3 only, dimension 1).

Dimension formulas (B, re-derived by I's second implementation for d = 1, 2, 3, 5, 7 and k <= 8): r_1 = 1, r_2 = d, r_(i+1) = d r_i + r_(i-1), D_k = r_(k+1) - [k odd]. So D_2 = d^2+1, D_3 = d^3+2d-1, D_4 = d^4+3d^2+1, D_5 = d^5+4d^3+3d-1, D_6 = d^6+5d^4+6d^2+1; d = 3 gives 2, 10, 32, 109, 359, 1189. In the coincidence case C gives D_3 = d^3+2d-1-m.

Existence of c: PROVED twice (draft's counting, refereed by H; I's explicit choice c_j = g^(2^j) in F_Q, Q = q^(m ell), ell prime > 2^k, CHECKED in big-integer arithmetic for five (q,m,k)). The field grows with k.

The two verdicts.
- Referee I: FOURIER_STEP_PROVED_MODULO_CITED. Used Laumon 1.2.2.1, 1.3.1.1, 1.3.2.3, 1.3.2.4, 1.4.2.1(ii), 2.2.1.1, 2.3.1.1, 2.3.3.1, 2.4.2.1, 2.4.3, 2.5.3.1 within their hypotheses, as read from OCR. Several formulas (2.3.1.2, 2.4.3) are garbled; I reconstructed the rank and drop formulas independently, and exact data agree.
- Referee H: GAPS. Rederived the combinatorics and recursion; could not rederive the form of Q_i at infinity or its tameness at finite singular points, used "tame goes to tame" from memory (HINT). Notes the final vanishing needs only that P_k is simple and not constant. Also says "singular" must be defined as M' ramified.
- D says the tameness induction is "not verified beyond one step"; B and I say it follows from Laumon 2.3 to 2.5. Only B (and then I) have gone through it. H also notes the theorem needs the induction for infinitely many k, not all k.
- Scope found by H: any odd q; d odd is not used in S5 to S10 (so the upper bound would hold for even d, which is true); CHECKED x^2-1, x^2+1 over F_3, k=2, degree 5 = d^2+1 (compute/H/analysis_even.txt).

## 4. Exact tests (report E)

Fibre sums computed exactly in Z[omega], p = 3; L(T) built exactly; "poly" means the series terminated (trailing exact zeros). Files are in `round3/compute/NUM/`; the row list is `predicted_vs_observed.txt`, and the cases in `results1.jsonl`, `results2.jsonl`, `results3.jsonl`.

| case (f, q, k, c) | hypothesis | predicted degree | observed degree | file |
|---|---|---|---|---|
| x-1, 3, k=2 | n/a | 2 | 2 (poly) | predicted_vs_observed.txt, f1_k2_e1 |
| x-1, 3, k=3, (1,1) | holds | 2 | 2 | f1_k3_e1 |
| x-1, 3, k=4, (1,1,1) | holds | 5 | 5 | f1_k4_e1_sum0 |
| x-1, 9, k=3 and k=4 | holds | 2; 5 | 2; 5 | f1_k3_e2gen, f1_k4_e2gen |
| x^3-x+1, 3, k=2 | holds | 10 | 10 | f3_k2_e1 |
| x-1, 3, k=3, (1,-1) | fails | 1 | 1 | f1_k3_bad |
| x-1, 3, k=4, (1,1,-1); (1,-1,1) | fails | 4; 3 | 4; 3 | f1_k4_bad_a, f1_k4_bad_b |
| x-1, 3, k=5, all ones; k=6 all ones | fails | 6; 11 | 6; 11 | f1_k5_ones, f1_k6_ones |
| x-1, 9, k=5 | holds | 7 | not terminated (n = 7) | f1_k5_e2gen |
| x^3-x+1, 3, k=3 and k=4 | holds | 32; 109 | not terminated (n = 13) | f3_k3_e1, f3_k4_e1_sum0 |

The "predicted" degree is E's own bookkeeping (`predicted.py`), not an independent proof; it agrees with B's and C's formulas. No mismatch. Caveats E states and I repeat: a polynomial L does not exclude a degree k+1 class cancelling an equal eigenvalue in degree k; d = 3 beyond k = 2 is untested by anyone.

Referee I added (CHECKED mod P, P1 = 400000091, P2 = 300000031, f = x - a over F_5, n <= 9; `compute/I/analysis_P1.txt`, `analysis_P2_a2.txt`): 15 configurations, k = 2 to 5, all match, including the first terminated k = 5 case with (G_k) holding (degree 7, L_8 = L_9 = 0) and the drop to 6 when rho_4 rho_2 = 1. This is mod P, so zeros are evidence, nonzero coefficients would have been refutations. Referee H's `compute/H/central.py`: 78 cases of the Parseval bound R^2 <= (p-1)^2 p^(k+1), no violation; k = 2 closed form exact in 26 of 26.

## 5. Lean

New file `lean/ToyWeil/Endgame2.lean` (report F), statements copied from the file:

    theorem no_cancellation_signed3 {A E B : Type*} [Fintype A] [Fintype E] [Fintype B]
        (a : A → ℂ) (e : E → ℂ) (b : B → ℂ) (C ρ : ℝ) (hρ : 0 ≤ ρ)
        (h : ∀ n : ℕ, 1 ≤ n → ‖(∑ i, a i ^ n) + (∑ i, e i ^ n) - ∑ j, b j ^ n‖ ≤ C * ρ ^ n)
        (hb : ∀ j, ‖b j‖ ≤ ρ) :
        ∀ i, ‖a i‖ ≤ ρ

    theorem no_cancellation_signed {A B : Type*} [Fintype A] [Fintype B]
        (a : A → ℂ) (b : B → ℂ) (C ρ : ℝ) (hρ : 0 ≤ ρ)
        (h : ∀ n : ℕ, 1 ≤ n → ‖(∑ i, a i ^ n) - ∑ j, b j ^ n‖ ≤ C * ρ ^ n)
        (hb : ∀ j, ‖b j‖ ≤ ρ) :
        ∀ i, ‖a i‖ ≤ ρ

    theorem endgame_fibres {d : ℕ} (α : Fin d → ℂ) (q : ℝ) (hq : 1 < q)
        (H : ∀ k : ℕ, 2 ≤ k → ∃ (E : Type) (B : Type) (_ : Fintype E) (_ : Fintype B)
          (e : E → ℂ) (b : B → ℂ) (C : ℝ),
          (∀ n : ℕ, 1 ≤ n →
            ‖(∑ I : Fin k → Fin d, (∏ j, α (I j)) ^ n) + (∑ i, e i ^ n) - ∑ j, b j ^ n‖ ≤
              C * (q ^ (((k : ℝ) + 3) / 2)) ^ n) ∧
          (∀ j, ‖b j‖ ≤ q ^ (((k : ℝ) + 3) / 2))) :
        ∀ i, ‖α i‖ ≤ Real.sqrt q

Log `lean/logs/ToyWeil.Endgame2.log`: one deprecation warning for `push_neg`, then

    'ToyWeil.no_cancellation_signed3' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ToyWeil.no_cancellation_signed' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ToyWeil.endgame_fibres' depends on axioms: [propext, Classical.choice, Quot.sound]

The log records no exit code; F says the check script returned 0. I did not recompile, nor did referee H or the main session in this round. Limits: `endgame_fibres` assumes one fixed field and one hypothesis H for every k, while the route uses a growing field F_(q^(s_k)); H calls this immaterial (the per-k step has no constants and the rest is real analysis), but the s-th root and the limit are not in Lean. Lean covers no cohomological statement and does not say that H holds.

## 6. Sources

Opened (OCR text layers, symbols garbled, no page images): Laumon 1987 (B, D, I; numbers listed in section 3), BBD chapter 4 (B), Katz-Laumon 1985 (B says opened; D says 2.1.5 seen only as quoted; I read the Katz-Laumon 2.1.3 statement through Laumon 1.3.1.1 and not its proof; treat as unresolved), Laumon's Swan-conductor paper, Asterisque 82-83, Theoreme 2.1.1 (D; C lists it NOT OPENED; B's induction does not use it), Katz's four lectures, Venkatesh's note, Kopparty's notes (D).

NOT OPENED by anyone: Grothendieck-Ogg-Shafarevich, SGA 4 formalism (Kunneth, projection formula, proper base change, Artin vanishing, Leray), trace formula, Poincare duality on curves, SGA 1 V 8.2 (replaced by I's elementary argument), Gabber-Katz (inside Laumon 2.5.3), BBD 1.4.25, Kiehl-Weissauer, Brylinski, Katz Asterisque 79.

Weights: D's grep of the OCR of Laumon finds no weight argument in chapters 1 to 3; weights first enter at Definition 4.1.2. That is a word search of an OCR, not a reading of proofs. For BBD chapter 4, the trace formula, GOS and Katz-Laumon 2.1.3 the weight-freeness is memory (HINT; H says so). Where hidden circularity would sit: a weight-free evaluation of the fibre sum; the only size inputs in the draft are the Parseval bound (Lean) and the power-sum lemma (Lean).

## 7. Novelty (report D, with its uncertainty)

D read Laumon chapter 4, Katz's four lectures and two sets of notes. Findings: Laumon applies the Fourier transform once and uses Deligne's reality criterion and a product formula; neither "Plancherel" nor "Parseval" appears in the dump. Katz uses Rankin positivity on tensor powers and one fourth-moment orthogonality computation. The route (k-fold iterated transform, fibre vanishing, Parseval on fibres, limit in k) is a variant of the Kloosterman-Rankin-Laumon-Katz "method of families", not a special case of either. Five generic searches found no published proof of the route; that is only an absence of hits. The brief's attribution of a Plancherel argument to Kiehl-Weissauer is unverified (the book was behind a login). B and A both say the skeleton is the standard Katz-Laumon apparatus. Uncertainty: Kiehl-Weissauer, Katz Asterisque 79 and Brylinski are unopened, so a rediscovery cannot be excluded.

## 8. What remains, in order

1. Read the page images of Laumon 2.3.1.2, 2.3.3.1, 2.4.3 and 2.5.3.1 (and the 1.4.2.1 reading) and check that the slope-1 part at infinity is a sum of L_psi(a y) tensor tame, that the local transforms send tame to tame, and that no slope above 1 appears. This is the one item on which H and I differ.
2. Open the cited statements nobody opened (GOS, SGA 4 formalism, BBD 4.3.1 beyond OCR, Katz-Laumon 2.1.3 with proof, Gabber-Katz) and check by reading, not grep, that none uses weights.
3. A test of fibre vanishing at d >= 3 with k >= 3 (D_3 = 32 needs about 64 terms; out of reach so far), and one that separates degree k from degree k+1.
4. Recompile Parseval.lean and Endgame2.lean in the main session; decide whether to formalise the limit with a growing field.
5. Edit the draft: state k >= 2 in S1; define "singular" as M' ramified; put in the middle-extension criterion, I's three-line pi_1 argument and the k = 5 test; replace "OPEN-but-no-known-gap" by "conditional on S5 step 3 and the list of cited statements"; note S5 to S10 do not use d odd.
6. Have the duality step S11 refereed again (H found it correct; Poincare duality is cited).
7. Settle novelty by opening Kiehl-Weissauer, Katz Asterisque 79 and Brylinski.
8. The coincidence case (Z meets a singular set) is outside the theorem and not needed; E and I give data, no proof.
