# G: Lean formalisation of the endgame (PowerSum.lean)

File: ./lean/ToyWeil/PowerSum.lean
Compiled with lean_check.sh ToyWeil.PowerSum: exit 0, "LEANCHECK OK", 18 s. Only warning: `push_neg` is deprecated (cosmetic). No sorry, no axiom declaration, no native_decide.

All three targets S1, S2, S3 are PROVED (kernel-checked, Lean 4.34.1 + Mathlib). Log: toy-case/lean/logs/ToyWeil.PowerSum.log

## Final statements (copied from the file)

S1 (Fin m version, exactly as requested):
    theorem no_hidden_growth {m : N} (g : Fin m -> C) (hg : Function.Injective g)
        (c : Fin m -> C) (hc : forall j, c j != 0) (C rho : R) (hrho : 0 <= rho)
        (h : forall n : N, 1 <= n -> ||sum j, c j * g j ^ n|| <= C * rho ^ n) :
        forall j, ||g j|| <= rho
(In the file the symbols are gamma, rho, norm bars and `∑ j, c j * γ j ^ n`.) Also proved for any finite index type: `no_hidden_growth'`.
Route: window of exponents N+1+i, i < m; w = s *v V^-1 with V the Vandermonde matrix (det nonzero by Matrix.det_vandermonde_ne_zero_iff); the inverse is independent of N, so ||c_j|| ||g_j||^(N+1) <= K rho^N with K = |C| R^m sum_i ||V^-1 i j||, R = max 1 rho; then helper `le_of_pow_succ_le` (x^(N+1) <= K rho^N for all N >= 1 implies x <= rho; unbounded geometric growth if x > rho).

S2:
    theorem no_cancellation {A B : Type*} [Fintype A] [Fintype B] (a : A -> C) (b : B -> C)
        (C rho : R) (hrho : 0 <= rho)
        (h : forall n, 1 <= n -> ||(sum i, a i ^ n) + sum j, b j ^ n|| <= C * rho ^ n) :
        forall i, ||a i|| <= rho
Route: group equal values (Finset.sum_fiberwise_of_maps_to), multiplicity = positive natural number, apply S1' to the distinct values. Zero values are harmless.

S3:
    theorem endgame {d : N} (alpha : Fin d -> C) (q : R) (hq : 1 < q)
        (H : forall k, 2 <= k -> exists (B : Type) (_ : Fintype B) (b : B -> C) (C : R),
          forall n, 1 <= n ->
            ||(sum I : Fin k -> Fin d, (prod j, alpha (I j)) ^ n) + sum j, b j ^ n||
              <= C * (q ^ (((k:R) + 3) / 2)) ^ n) :
        forall i, ||alpha i|| <= Real.sqrt q
Note: B is quantified in `Type` (universe 0), a harmless restriction for finite types that is how it is written in the file. Route: S2 gives ||prod alpha(I j)|| <= q^((k+3)/2) for each I; take I constant i, so ||alpha i||^k <= sqrt(q)^(k+3); the helper lemma yields ||alpha i|| <= sqrt q.

## #print axioms (copied from the log)
'ToyWeil.le_of_pow_succ_le' depends on axioms: [propext, Classical.choice, Quot.sound]
'ToyWeil.no_hidden_growth' depends on axioms: [propext, Classical.choice, Quot.sound]
'ToyWeil.no_hidden_growth'' depends on axioms: [propext, Classical.choice, Quot.sound]
'ToyWeil.no_cancellation' depends on axioms: [propext, Classical.choice, Quot.sound]
'ToyWeil.endgame' depends on axioms: [propext, Classical.choice, Quot.sound]

## Targets not reached
None. Caveat: these statements formalise only the analytic endgame; they say nothing about whether the hypotheses of S3 (the bound with exponent (k+3)/2 for every k) can be established from the footnote, and nothing about the Riemann Hypothesis for the integers.
