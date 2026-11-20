import Mathlib.LinearAlgebra.Vandermonde
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.Complex.Basic

/-!
# Subsequence and Extension-Field No-Cancellation Endgame

Fixes two structural limitations of `toy-case/lean/ToyWeil/PowerSum.lean`:
1. `endgame` there requires a bound for *all* `k ≥ 2`, whereas the geometric sign
   argument (both for Kummer and for Artin–Schreier) applies only along *infinitely many*
   `k` (specifically even `k = 2r`).
2. `endgame` there requires fixed base-field coefficients (`m = 1`, all `n ≥ 1`), whereas
   at fixed `q` the bad locus of `c` can cover all of `(F_q^*)^{k-1}` (already seen at
   `k = 4, d = 3, p = 7` and `k = 4, d = 5, p = 11`!), forcing `c` to be chosen in an
   extension field `F_{q^m}` with `m = m(k) ≥ 1`.

`endgame_subseq_ext` handles both an arbitrary unbounded subsequence of `k` and an
arbitrary `k`-dependent extension degree `m = m(k) ≥ 1`, and `weil_bound_of_subseq_ext`
deduces the Weil bound `‖-∑ α_i^n‖ ≤ d * (Real.sqrt q)^n`.
-/

open Matrix

namespace ArtinSchreierToy

/-- If `x ^ (N + 1) ≤ K * ρ ^ N` for all `N ≥ 1` then `x ≤ ρ` (`x, ρ ≥ 0`). -/
theorem le_of_pow_succ_le {x ρ K : ℝ} (hρ : 0 ≤ ρ) (hx : 0 ≤ x)
    (h : ∀ N : ℕ, 1 ≤ N → x ^ (N + 1) ≤ K * ρ ^ N) : x ≤ ρ := by
  by_contra hlt
  push Not at hlt
  have hxpos : 0 < x := lt_of_le_of_lt hρ hlt
  rcases hρ.eq_or_lt with h0 | hpos
  · have h1 := h 1 le_rfl
    rw [← h0] at h1
    have h2 : x ^ (1 + 1) ≤ 0 := by simpa using h1
    have h3 : 0 < x ^ (1 + 1) := by positivity
    linarith
  · have hr : 1 < x / ρ := by rw [lt_div_iff₀ hpos]; linarith
    obtain ⟨N0, hN0⟩ := pow_unbounded_of_one_lt (K / x) hr
    have hN := h (N0 + 1) (by omega)
    have hxN : x ^ (N0 + 1) = (x / ρ) ^ (N0 + 1) * ρ ^ (N0 + 1) := by
      rw [← mul_pow]; field_simp
    have hmono : (x / ρ) ^ N0 ≤ (x / ρ) ^ (N0 + 1) :=
      pow_le_pow_right₀ hr.le (by omega)
    have hρp : 0 < ρ ^ (N0 + 1) := pow_pos hpos _
    have h2 : K < x * (x / ρ) ^ (N0 + 1) := by
      calc K = x * (K / x) := by field_simp
        _ < x * (x / ρ) ^ N0 := mul_lt_mul_of_pos_left hN0 hxpos
        _ ≤ x * (x / ρ) ^ (N0 + 1) := mul_le_mul_of_nonneg_left hmono hx
    have h3 := mul_lt_mul_of_pos_right h2 hρp
    have h4 : x ^ (N0 + 1 + 1) = x * (x / ρ) ^ (N0 + 1) * ρ ^ (N0 + 1) := by
      rw [pow_succ' x (N0 + 1), hxN]; ring
    linarith

/-- No hidden growth for an exponential sum with distinct bases and nonzero coefficients. -/
theorem no_hidden_growth {m : ℕ} (γ : Fin m → ℂ) (hγ : Function.Injective γ)
    (c : Fin m → ℂ) (hc : ∀ j, c j ≠ 0) (C ρ : ℝ) (hρ : 0 ≤ ρ)
    (h : ∀ n : ℕ, 1 ≤ n → ‖∑ j, c j * γ j ^ n‖ ≤ C * ρ ^ n) :
    ∀ j, ‖γ j‖ ≤ ρ := by
  classical
  have hdet : IsUnit (Matrix.vandermonde γ).det :=
    (isUnit_iff_ne_zero).2 ((Matrix.det_vandermonde_ne_zero_iff).2 hγ)
  have hAB : Matrix.vandermonde γ * (Matrix.vandermonde γ)⁻¹ = 1 :=
    Matrix.mul_nonsing_inv _ hdet
  intro j
  set R : ℝ := max 1 ρ
  have hR1 : 1 ≤ R := le_max_left _ _
  have hRρ : ρ ≤ R := le_max_right _ _
  set K : ℝ := |C| * R ^ m * ∑ i, ‖(Matrix.vandermonde γ)⁻¹ i j‖
  have key : ∀ N : ℕ, ‖c j‖ * ‖γ j‖ ^ (N + 1) ≤ K * ρ ^ N := by
    intro N
    have hs : (fun i : Fin m => ∑ j, c j * γ j ^ (N + 1 + (i : ℕ))) =
        (fun j => c j * γ j ^ (N + 1)) ᵥ* Matrix.vandermonde γ := by
      funext i
      simp only [Matrix.vecMul, dotProduct, Matrix.vandermonde_apply]
      apply Finset.sum_congr rfl
      intro j _
      rw [pow_add]; ring
    have hw : (fun j => c j * γ j ^ (N + 1)) =
        (fun i : Fin m => ∑ j, c j * γ j ^ (N + 1 + (i : ℕ))) ᵥ* (Matrix.vandermonde γ)⁻¹ := by
      rw [hs, Matrix.vecMul_vecMul, hAB, Matrix.vecMul_one]
    have hwj : c j * γ j ^ (N + 1) =
        ∑ i : Fin m, (∑ j, c j * γ j ^ (N + 1 + (i : ℕ))) * (Matrix.vandermonde γ)⁻¹ i j := by
      have := congrFun hw j
      simpa [Matrix.vecMul, dotProduct] using this
    have hbound : ‖c j‖ * ‖γ j‖ ^ (N + 1) ≤
        ∑ i : Fin m, (|C| * R ^ m * ρ ^ N) * ‖(Matrix.vandermonde γ)⁻¹ i j‖ := by
      calc ‖c j‖ * ‖γ j‖ ^ (N + 1) = ‖c j * γ j ^ (N + 1)‖ := by rw [norm_mul, norm_pow]
        _ = ‖∑ i : Fin m, (∑ j, c j * γ j ^ (N + 1 + (i : ℕ))) *
              (Matrix.vandermonde γ)⁻¹ i j‖ := by rw [hwj]
        _ ≤ ∑ i : Fin m, ‖(∑ j, c j * γ j ^ (N + 1 + (i : ℕ))) *
              (Matrix.vandermonde γ)⁻¹ i j‖ := norm_sum_le _ _
        _ ≤ _ := by
          apply Finset.sum_le_sum
          intro i _
          rw [norm_mul]
          apply mul_le_mul_of_nonneg_right _ (norm_nonneg _)
          have hi := i.isLt
          have h1 := h (N + 1 + (i : ℕ)) (by omega)
          have h2 : C * ρ ^ (N + 1 + (i : ℕ)) ≤ |C| * ρ ^ (N + 1 + (i : ℕ)) :=
            mul_le_mul_of_nonneg_right (le_abs_self C) (pow_nonneg hρ _)
          have h3 : ρ ^ (N + 1 + (i : ℕ)) ≤ R ^ m * ρ ^ N := by
            have e : ρ ^ (N + 1 + (i : ℕ)) = ρ ^ (1 + (i : ℕ)) * ρ ^ N := by
              rw [← pow_add]; congr 1; omega
            rw [e]
            apply mul_le_mul_of_nonneg_right _ (pow_nonneg hρ _)
            calc ρ ^ (1 + (i : ℕ)) ≤ R ^ (1 + (i : ℕ)) := pow_le_pow_left₀ hρ hRρ _
              _ ≤ R ^ m := pow_le_pow_right₀ hR1 (by omega)
          calc ‖∑ j, c j * γ j ^ (N + 1 + (i : ℕ))‖ ≤ C * ρ ^ (N + 1 + (i : ℕ)) := h1
            _ ≤ |C| * ρ ^ (N + 1 + (i : ℕ)) := h2
            _ ≤ |C| * (R ^ m * ρ ^ N) := mul_le_mul_of_nonneg_left h3 (abs_nonneg C)
            _ = |C| * R ^ m * ρ ^ N := by ring
    have hsum : ∑ i : Fin m, (|C| * R ^ m * ρ ^ N) * ‖(Matrix.vandermonde γ)⁻¹ i j‖
        = K * ρ ^ N := by
      rw [← Finset.mul_sum]; ring
    linarith
  have hcpos : 0 < ‖c j‖ := norm_pos_iff.2 (hc j)
  apply le_of_pow_succ_le hρ (norm_nonneg _) (K := K / ‖c j‖)
  intro N _
  rw [div_mul_eq_mul_div, le_div_iff₀ hcpos]
  calc ‖γ j‖ ^ (N + 1) * ‖c j‖ = ‖c j‖ * ‖γ j‖ ^ (N + 1) := mul_comm _ _
    _ ≤ K * ρ ^ N := key N

theorem no_hidden_growth' {ι : Type*} [Fintype ι] (γ : ι → ℂ) (hγ : Function.Injective γ)
    (c : ι → ℂ) (hc : ∀ j, c j ≠ 0) (C ρ : ℝ) (hρ : 0 ≤ ρ)
    (h : ∀ n : ℕ, 1 ≤ n → ‖∑ j, c j * γ j ^ n‖ ≤ C * ρ ^ n) :
    ∀ j, ‖γ j‖ ≤ ρ := by
  intro j
  let e := Fintype.equivFin ι
  have := no_hidden_growth (fun k => γ (e.symm k)) (hγ.comp e.symm.injective)
    (fun k => c (e.symm k)) (fun k => hc _) C ρ hρ (by
      intro n hn
      have := h n hn
      rwa [← Equiv.sum_comp e.symm (fun j => c j * γ j ^ n)] at this) (e j)
  simpa using this

private lemma sum_pow_group {A : Type*} [Fintype A] (g : A → ℂ) (V : Finset ℂ) (hV : ∀ i, g i ∈ V)
    (n : ℕ) :
    ∑ i, g i ^ n = ∑ v ∈ V, ((Finset.univ.filter (fun i => g i = v)).card : ℂ) * v ^ n := by
  classical
  rw [← Finset.sum_fiberwise_of_maps_to (s := Finset.univ) (t := V) (g := g) (fun i _ => hV i)]
  apply Finset.sum_congr rfl
  intro v _
  rw [Finset.sum_congr rfl (g := fun _ => v ^ n) (fun i hi => by rw [(Finset.mem_filter.1 hi).2])]
  simp [Finset.sum_const, nsmul_eq_mul]

/-- No cancellation between two finite families of complex exponentials entering with the same sign. -/
theorem no_cancellation {A B : Type*} [Fintype A] [Fintype B] (a : A → ℂ) (b : B → ℂ)
    (C ρ : ℝ) (hρ : 0 ≤ ρ)
    (h : ∀ n : ℕ, 1 ≤ n → ‖(∑ i, a i ^ n) + ∑ j, b j ^ n‖ ≤ C * ρ ^ n) :
    ∀ i, ‖a i‖ ≤ ρ := by
  classical
  intro i0
  let V : Finset ℂ := Finset.univ.image a ∪ Finset.univ.image b
  have haV : ∀ i, a i ∈ V := fun i =>
    Finset.mem_union_left _ (Finset.mem_image_of_mem _ (Finset.mem_univ _))
  have hbV : ∀ j, b j ∈ V := fun j =>
    Finset.mem_union_right _ (Finset.mem_image_of_mem _ (Finset.mem_univ _))
  let cnt : ℂ → ℕ := fun v => (Finset.univ.filter (fun i => a i = v)).card +
    (Finset.univ.filter (fun j => b j = v)).card
  have hcnt : ∀ v : V, ((cnt v.1 : ℕ) : ℂ) ≠ 0 := by
    intro v
    have hv := v.2
    rw [Nat.cast_ne_zero]
    rcases Finset.mem_union.1 hv with hv | hv
    · obtain ⟨i, _, hi⟩ := Finset.mem_image.1 hv
      have : 0 < (Finset.univ.filter (fun i => a i = v.1)).card :=
        Finset.card_pos.2 ⟨i, by simp [hi]⟩
      simp only [cnt]; omega
    · obtain ⟨j, _, hj⟩ := Finset.mem_image.1 hv
      have : 0 < (Finset.univ.filter (fun j => b j = v.1)).card :=
        Finset.card_pos.2 ⟨j, by simp [hj]⟩
      simp only [cnt]; omega
  have key := no_hidden_growth' (fun v : V => v.1) Subtype.val_injective
    (fun v => ((cnt v.1 : ℕ) : ℂ)) hcnt C ρ hρ (by
      intro n hn
      have := h n hn
      rw [sum_pow_group a V haV n, sum_pow_group b V hbV n, ← Finset.sum_add_distrib] at this
      rw [Finset.sum_coe_sort V (fun v => ((cnt v : ℕ) : ℂ) * v ^ n)]
      convert this using 2
      apply Finset.sum_congr rfl
      intro v _
      simp only [cnt]; push_cast; ring)
  simpa using key ⟨a i0, haV i0⟩

/-- Subsequence tensor-power limit: if `x ^ k ≤ q ^ ((k + 3) / 2)` for arbitrarily large `k`,
then `x ≤ sqrt q`. Works along any unbounded subsequence (e.g. even `k = 2r`). -/
theorem le_sqrt_of_subseq_rpow {x q : ℝ} (hq : 1 < q)
    (h : ∀ K : ℕ, ∃ k ≥ K, 1 ≤ k ∧ x ^ k ≤ q ^ (((k : ℝ) + 3) / 2)) :
    x ≤ Real.sqrt q := by
  have hq0 : 0 ≤ q := by linarith
  have hspos : 0 < Real.sqrt q := Real.sqrt_pos.2 (by linarith)
  by_contra hlt
  push Not at hlt
  have hr : 1 < x / Real.sqrt q := by rw [lt_div_iff₀ hspos]; linarith
  obtain ⟨K, hK⟩ := pow_unbounded_of_one_lt ((Real.sqrt q) ^ 3) hr
  obtain ⟨k, hkK, _, hxk⟩ := h K
  have hmono : (x / Real.sqrt q) ^ K ≤ (x / Real.sqrt q) ^ k :=
    pow_le_pow_right₀ hr.le hkK
  have hstrict : (Real.sqrt q) ^ 3 < (x / Real.sqrt q) ^ k := lt_of_lt_of_le hK hmono
  have hsp : 0 < (Real.sqrt q) ^ k := pow_pos hspos k
  have hmul := mul_lt_mul_of_pos_right hstrict hsp
  have hcancel : (x / Real.sqrt q) ^ k * (Real.sqrt q) ^ k = x ^ k := by
    rw [← mul_pow]; field_simp
  have hpow : q ^ (((k : ℝ) + 3) / 2) = (Real.sqrt q) ^ 3 * (Real.sqrt q) ^ k := by
    rw [Real.sqrt_eq_rpow, ← Real.rpow_natCast, ← Real.rpow_natCast,
      ← Real.rpow_mul hq0, ← Real.rpow_mul hq0, ← Real.rpow_add (by linarith)]
    congr 1; ring
  rw [hcancel] at hmul
  rw [hpow] at hxk
  linarith

/-- Subsequence + extension-field endgame: if for arbitrarily large `k ≥ 2`, there exists an
extension degree `m ≥ 1` and an auxiliary family `b` entering with the same sign as the
`k`-fold products of `α_i^m` with `q^m`-Parseval bound `C * ((q^m)^((k+3)/2))^n`, then
`‖α_i‖ ≤ sqrt q` for every `i`. -/
theorem endgame_subseq_ext {d : ℕ} (α : Fin d → ℂ) (q : ℝ) (hq : 1 < q)
    (H : ∀ K : ℕ, ∃ k ≥ K, 2 ≤ k ∧ ∃ m : ℕ, 1 ≤ m ∧
      ∃ (B : Type) (_ : Fintype B) (b : B → ℂ) (C : ℝ),
        ∀ n : ℕ, 1 ≤ n →
          ‖(∑ I : Fin k → Fin d, ((∏ j, α (I j)) ^ m) ^ n) + ∑ j, b j ^ n‖ ≤
            C * ((q ^ m) ^ (((k : ℝ) + 3) / 2)) ^ n) :
    ∀ i, ‖α i‖ ≤ Real.sqrt q := by
  have hq0 : 0 ≤ q := by linarith
  intro i
  apply le_sqrt_of_subseq_rpow hq
  intro K
  obtain ⟨k, hkK, hk2, m, hm1, B, _, b, C, hC⟩ := H K
  refine ⟨k, hkK, by omega, ?_⟩
  have hρ : 0 ≤ (q ^ m) ^ (((k : ℝ) + 3) / 2) := by positivity
  have step := no_cancellation (fun I : Fin k → Fin d => (∏ j, α (I j)) ^ m) b C
    ((q ^ m) ^ (((k : ℝ) + 3) / 2)) hρ hC (fun _ => i)
  simp only [Finset.prod_const, Finset.card_univ, Fintype.card_fin, norm_pow] at step
  have hrhs : (q ^ m) ^ (((k : ℝ) + 3) / 2) = (q ^ (((k : ℝ) + 3) / 2)) ^ m := by
    rw [← Real.rpow_natCast q m, ← Real.rpow_mul hq0, ← Real.rpow_natCast,
      ← Real.rpow_mul hq0]
    congr 1; ring
  rw [hrhs] at step
  exact le_of_pow_le_pow_left₀ (by omega) (by positivity) step

/-- Specialization of `endgame_subseq_ext` to even `k = 2r` (`r ≥ 2`), matching the
Artin–Schreier path-quadric theorem directly. -/
theorem endgame_even_ext {d : ℕ} (α : Fin d → ℂ) (q : ℝ) (hq : 1 < q)
    (H : ∀ r : ℕ, 2 ≤ r → ∃ m : ℕ, 1 ≤ m ∧
      ∃ (B : Type) (_ : Fintype B) (b : B → ℂ) (C : ℝ),
        ∀ n : ℕ, 1 ≤ n →
          ‖(∑ I : Fin (2 * r) → Fin d, ((∏ j, α (I j)) ^ m) ^ n) + ∑ j, b j ^ n‖ ≤
            C * ((q ^ m) ^ ((((2 * r : ℕ) : ℝ) + 3) / 2)) ^ n) :
    ∀ i, ‖α i‖ ≤ Real.sqrt q := by
  apply endgame_subseq_ext α q hq
  intro K
  obtain ⟨m, hm1, B, hFB, b, C, hC⟩ := H (max K 2) (le_max_right _ _)
  exact ⟨2 * max K 2, by omega, by omega, m, hm1, B, hFB, b, C, hC⟩

/-- Direct Weil bound `‖- ∑ i, α i ^ n‖ ≤ d * (sqrt q) ^ n` from `endgame_even_ext`. -/
theorem weil_bound_of_even_ext {d : ℕ} (α : Fin d → ℂ) (q : ℝ) (hq : 1 < q)
    (H : ∀ r : ℕ, 2 ≤ r → ∃ m : ℕ, 1 ≤ m ∧
      ∃ (B : Type) (_ : Fintype B) (b : B → ℂ) (C : ℝ),
        ∀ n : ℕ, 1 ≤ n →
          ‖(∑ I : Fin (2 * r) → Fin d, ((∏ j, α (I j)) ^ m) ^ n) + ∑ j, b j ^ n‖ ≤
            C * ((q ^ m) ^ ((((2 * r : ℕ) : ℝ) + 3) / 2)) ^ n)
    (n : ℕ) :
    ‖- ∑ i : Fin d, α i ^ n‖ ≤ (d : ℝ) * (Real.sqrt q) ^ n := by
  have hα := endgame_even_ext α q hq H
  rw [norm_neg]
  calc ‖∑ i : Fin d, α i ^ n‖
      ≤ ∑ i : Fin d, ‖α i ^ n‖ := norm_sum_le _ _
    _ = ∑ i : Fin d, ‖α i‖ ^ n := by simp_rw [norm_pow]
    _ ≤ ∑ _i : Fin d, (Real.sqrt q) ^ n :=
        Finset.sum_le_sum fun i _ => pow_le_pow_left₀ (norm_nonneg _) (hα i) n
    _ = (d : ℝ) * (Real.sqrt q) ^ n := by simp

end ArtinSchreierToy

open ArtinSchreierToy in #print axioms le_of_pow_succ_le
open ArtinSchreierToy in #print axioms no_hidden_growth
open ArtinSchreierToy in #print axioms no_cancellation
open ArtinSchreierToy in #print axioms le_sqrt_of_subseq_rpow
open ArtinSchreierToy in #print axioms endgame_subseq_ext
open ArtinSchreierToy in #print axioms endgame_even_ext
open ArtinSchreierToy in #print axioms weil_bound_of_even_ext
