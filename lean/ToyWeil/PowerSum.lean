import Mathlib.LinearAlgebra.Vandermonde
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.Complex.Basic

open Matrix

namespace ToyWeil

/-- If `x ^ (N+1) ≤ K * ρ ^ N` for all `N ≥ 1` then `x ≤ ρ` (`x, ρ ≥ 0`). -/
theorem le_of_pow_succ_le {x ρ K : ℝ} (hρ : 0 ≤ ρ) (hx : 0 ≤ x)
    (h : ∀ N : ℕ, 1 ≤ N → x ^ (N + 1) ≤ K * ρ ^ N) : x ≤ ρ := by
  by_contra hlt
  push_neg at hlt
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

/-- S1 (no hidden growth), indexed by `Fin m`. -/
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
  obtain ⟨R, hR⟩ : ∃ R : ℝ, R = max 1 ρ := ⟨_, rfl⟩
  have hR1 : 1 ≤ R := hR ▸ le_max_left _ _
  have hRρ : ρ ≤ R := hR ▸ le_max_right _ _
  obtain ⟨K, hK⟩ : ∃ K : ℝ, K = |C| * R ^ m * ∑ i, ‖(Matrix.vandermonde γ)⁻¹ i j‖ := ⟨_, rfl⟩
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
        _ = ‖∑ i : Fin m, (∑ j, c j * γ j ^ (N + 1 + (i : ℕ))) * (Matrix.vandermonde γ)⁻¹ i j‖ := by
          rw [hwj]
        _ ≤ ∑ i : Fin m, ‖(∑ j, c j * γ j ^ (N + 1 + (i : ℕ))) * (Matrix.vandermonde γ)⁻¹ i j‖ :=
          norm_sum_le _ _
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
    have hsum : ∑ i : Fin m, (|C| * R ^ m * ρ ^ N) * ‖(Matrix.vandermonde γ)⁻¹ i j‖ = K * ρ ^ N := by
      rw [← Finset.mul_sum, hK]; ring
    linarith
  have hcpos : 0 < ‖c j‖ := norm_pos_iff.2 (hc j)
  apply le_of_pow_succ_le hρ (norm_nonneg _) (K := K / ‖c j‖)
  intro N _
  rw [div_mul_eq_mul_div, le_div_iff₀ hcpos]
  calc ‖γ j‖ ^ (N + 1) * ‖c j‖ = ‖c j‖ * ‖γ j‖ ^ (N + 1) := mul_comm _ _
    _ ≤ K * ρ ^ N := key N

/-- S1 for an arbitrary finite index type. -/
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

lemma sum_pow_group {A : Type*} [Fintype A] (g : A → ℂ) (V : Finset ℂ) (hV : ∀ i, g i ∈ V)
    (n : ℕ) :
    ∑ i, g i ^ n = ∑ v ∈ V, ((Finset.univ.filter (fun i => g i = v)).card : ℂ) * v ^ n := by
  classical
  rw [← Finset.sum_fiberwise_of_maps_to (s := Finset.univ) (t := V) (g := g) (fun i _ => hV i)]
  apply Finset.sum_congr rfl
  intro v _
  rw [Finset.sum_congr rfl (g := fun _ => v ^ n) (fun i hi => by rw [(Finset.mem_filter.1 hi).2])]
  simp [Finset.sum_const, nsmul_eq_mul]

/-- S2 (no cancellation between two families entering with the same sign). -/
theorem no_cancellation {A B : Type*} [Fintype A] [Fintype B] (a : A → ℂ) (b : B → ℂ)
    (C ρ : ℝ) (hρ : 0 ≤ ρ)
    (h : ∀ n : ℕ, 1 ≤ n → ‖(∑ i, a i ^ n) + ∑ j, b j ^ n‖ ≤ C * ρ ^ n) :
    ∀ i, ‖a i‖ ≤ ρ := by
  classical
  intro i0
  let V : Finset ℂ := Finset.univ.image a ∪ Finset.univ.image b
  have haV : ∀ i, a i ∈ V := fun i => Finset.mem_union_left _ (Finset.mem_image_of_mem _ (Finset.mem_univ _))
  have hbV : ∀ j, b j ∈ V := fun j => Finset.mem_union_right _ (Finset.mem_image_of_mem _ (Finset.mem_univ _))
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

/-- S3 (endgame). -/
theorem endgame {d : ℕ} (α : Fin d → ℂ) (q : ℝ) (hq : 1 < q)
    (H : ∀ k : ℕ, 2 ≤ k → ∃ (B : Type) (_ : Fintype B) (b : B → ℂ) (C : ℝ),
      ∀ n : ℕ, 1 ≤ n →
        ‖(∑ I : Fin k → Fin d, (∏ j, α (I j)) ^ n) + ∑ j, b j ^ n‖ ≤
          C * (q ^ (((k : ℝ) + 3) / 2)) ^ n) :
    ∀ i, ‖α i‖ ≤ Real.sqrt q := by
  intro i
  have hq0 : 0 ≤ q := by linarith
  have hy : 0 ≤ Real.sqrt q := Real.sqrt_nonneg _
  apply le_of_pow_succ_le hy (norm_nonneg _) (K := (Real.sqrt q) ^ 4)
  intro N hN
  obtain ⟨B, _, b, C, hC⟩ := H (N + 1) (by omega)
  have step := no_cancellation (fun I : Fin (N + 1) → Fin d => ∏ j, α (I j)) b C
    (q ^ (((((N + 1 : ℕ)) : ℝ) + 3) / 2)) (by positivity) hC (fun _ => i)
  simp only [Finset.prod_const, Finset.card_univ, Fintype.card_fin, norm_pow] at step
  have e : q ^ (((((N + 1 : ℕ)) : ℝ) + 3) / 2) = (Real.sqrt q) ^ (N + 1 + 3) := by
    rw [Real.sqrt_eq_rpow, ← Real.rpow_natCast, ← Real.rpow_mul hq0]
    congr 1; push_cast; ring
  rw [e] at step
  calc ‖α i‖ ^ (N + 1) ≤ (Real.sqrt q) ^ (N + 1 + 3) := step
    _ = (Real.sqrt q) ^ 4 * (Real.sqrt q) ^ N := by rw [← pow_add]; congr 1; omega

#print axioms le_of_pow_succ_le
#print axioms no_hidden_growth
#print axioms no_hidden_growth'
#print axioms no_cancellation
#print axioms endgame

end ToyWeil
