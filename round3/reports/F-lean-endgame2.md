# F: Lean endgame 2 (Claim A, signed and three-family no-cancellation)

All three targets reached. File: toy-case/lean/ToyWeil/Endgame2.lean. Compiled with lean_check.sh (ToyWeil.PowerSum then ToyWeil.Endgame2), exit 0. Only a push_neg deprecation warning. No sorry, no axiom, no native_decide. No weights, purity or Weil bound used anywhere (pure linear algebra: Vandermonde argument from PowerSum).

## Statements (copied from the file)

CHECKED (Lean kernel):
```
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
```
G1 = no_cancellation_signed (derived from G2 with E = Empty), G2 = no_cancellation_signed3, G3 = endgame_fibres.

## Axioms (from toy-case/lean/logs/ToyWeil.Endgame2.log)
```
'ToyWeil.no_cancellation_signed3' depends on axioms: [propext, Classical.choice, Quot.sound]
'ToyWeil.no_cancellation_signed' depends on axioms: [propext, Classical.choice, Quot.sound]
'ToyWeil.endgame_fibres' depends on axioms: [propext, Classical.choice, Quot.sound]
```

## Proof idea (PROVED, full Lean proof)
Group the three families by value over V = union of images. Net coefficient of v is (#a=v)+(#e=v)-(#b=v) as a complex number. Restrict to values with nonzero net coefficient, apply no_hidden_growth' (injective bases, nonzero coefficients): those bases have norm <= rho. For a i0 with zero net coefficient, #b=a i0 equals #a + #e >= 1 (cast injectivity), so a i0 = b j for some j and ||b j|| <= rho. G3 repeats the proof of `endgame` with k = N+1, using the bound on b (hypothesis) for the minus-sign family.

## Scope note
G3 assumes the fibre-statement hypothesis H for every k >= 2 (this is Claim A's output: the middle family e carries wrong-parity eigenvalues, b the cancelling ones with modulus bound). It says nothing about whether H holds: that is Claim B and the cohomological part of Claim A, untouched here. Nothing here concerns the Riemann Hypothesis for the integers.

## Not reached
None.
