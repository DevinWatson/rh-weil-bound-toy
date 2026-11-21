import ToyWeil.Parseval

open Finset

namespace ToyWeil

variable {F : Type*} [Field F] [Fintype F] [DecidableEq F] (psi : AddChar F ℂ)

/-- I1: the term `h = 0` is `M^k`. -/
theorem Ssum_zero (hψ : psi ≠ 0) (t : F → ℂ) (n : ℕ) :
    Ssum psi t 0 (n + 1) = (∑ x, t x) ^ (n + 1) := by
  rw [Ssum_eq_path_sum psi hψ, Fintype.sum_pow]
  simp

/-- The sum of `∏ t (x i)` over the zero set of the path quadric. -/
noncomputable def Ncount (t : F → ℂ) (n : ℕ) : ℂ :=
  ∑ x ∈ Finset.univ.filter (fun x : Fin (n + 1) → F => pathQuadric x = 0), ∏ i, t (x i)

/-- The sum over `h ≠ 0`. -/
noncomputable def Rsum (t : F → ℂ) (n : ℕ) : ℂ :=
  ∑ h ∈ (Finset.univ : Finset F).erase 0, Ssum psi t h (n + 1)

/-- I2: `q N = M^k + R`. -/
theorem identity (hψ : psi ≠ 0) (t : F → ℂ) (n : ℕ) :
    (Fintype.card F : ℂ) * Ncount t n = (∑ x, t x) ^ (n + 1) + Rsum psi t n := by
  have h1 := orthogonality psi hψ (X := Fin (n + 1) → F) (fun x => ∏ i, t (x i)) pathQuadric
  have h2 : ∀ h : F, ∑ x : Fin (n + 1) → F, (∏ i, t (x i)) * psi (h * pathQuadric x)
      = Ssum psi t h (n + 1) := fun h => (Ssum_eq_path_sum psi hψ t h n).symm
  simp_rw [h2] at h1
  unfold Ncount Rsum
  rw [← h1, ← Finset.add_sum_erase _ _ (Finset.mem_univ (0 : F)), Ssum_zero psi hψ]

/-- I3: the bound, with the sum of squares form. -/
theorem identity_bound (hψ : psi ≠ 0) (t : F → ℂ) (B : ℝ) (hB : ∀ x, ‖t x‖ ≤ B)
    (n : ℕ) (hn : 1 ≤ n) :
    ‖(Fintype.card F : ℂ) * Ncount t n - (∑ x, t x) ^ (n + 1)‖
      ≤ ((Fintype.card F : ℝ) - 1) *
        ((Fintype.card F : ℝ) ^ ((n : ℝ) / 2) * B ^ (n - 1) * ∑ x, ‖t x‖ ^ 2) := by
  rw [identity psi hψ t n, add_sub_cancel_left]
  unfold Rsum
  refine (norm_sum_le _ _).trans ?_
  have hcard : (((Finset.univ : Finset F).erase 0).card : ℝ) = (Fintype.card F : ℝ) - 1 := by
    rw [Finset.card_erase_of_mem (Finset.mem_univ _), Finset.card_univ,
      Nat.cast_sub Fintype.card_pos, Nat.cast_one]
  rw [← hcard, ← nsmul_eq_mul]
  refine Finset.sum_le_card_nsmul _ _ _ fun h hh => ?_
  have hh0 : h ≠ 0 := Finset.ne_of_mem_erase hh
  have := iterated_bound_rpow psi hψ t hh0 B hB (n + 1) (by omega)
  have e : (((n + 1 : ℕ) : ℝ) - 1) / 2 = (n : ℝ) / 2 := by push_cast; ring
  rw [e] at this
  simpa using this

/-- I3, closed form: `‖q N - M^(n+1)‖ ≤ (q - 1) q^(n/2 + 1) B^(n+1)`. -/
theorem identity_bound_closed (hψ : psi ≠ 0) (t : F → ℂ) (B : ℝ) (hB : ∀ x, ‖t x‖ ≤ B)
    (n : ℕ) (hn : 1 ≤ n) :
    ‖(Fintype.card F : ℂ) * Ncount t n - (∑ x, t x) ^ (n + 1)‖
      ≤ ((Fintype.card F : ℝ) - 1) *
        ((Fintype.card F : ℝ) ^ ((n : ℝ) / 2 + 1) * B ^ (n + 1)) := by
  refine (identity_bound psi hψ t B hB n hn).trans ?_
  have hq0 : (0 : ℝ) ≤ Fintype.card F := Nat.cast_nonneg _
  have hq1 : (1 : ℝ) ≤ Fintype.card F := by exact_mod_cast Fintype.card_pos
  have hB0 : 0 ≤ B := le_trans (norm_nonneg _) (hB 0)
  have hsum : ∑ x, ‖t x‖ ^ 2 ≤ (Fintype.card F : ℝ) * B ^ 2 := by
    have : ∑ x, ‖t x‖ ^ 2 ≤ ∑ _x : F, B ^ 2 :=
      Finset.sum_le_sum fun x _ => pow_le_pow_left₀ (norm_nonneg _) (hB x) 2
    simpa using this
  have e : (Fintype.card F : ℝ) ^ ((n : ℝ) / 2 + 1)
      = (Fintype.card F : ℝ) ^ ((n : ℝ) / 2) * Fintype.card F := by
    rw [Real.rpow_add_one]
    intro h; rw [h] at hq1; norm_num at hq1
  have e2 : B ^ (n + 1) = B ^ (n - 1) * B ^ 2 := by
    rw [← pow_add]; congr 1; omega
  have hq2 : 0 ≤ (Fintype.card F : ℝ) - 1 := by linarith
  refine mul_le_mul_of_nonneg_left ?_ hq2
  rw [e, e2]
  calc _ ≤ (Fintype.card F : ℝ) ^ ((n : ℝ) / 2) * B ^ (n - 1) * ((Fintype.card F : ℝ) * B ^ 2) := by
        gcongr
    _ = _ := by ring

/-- I4: for `‖t‖ ≤ 1`, `‖q N - M^k‖ ≤ (q - 1) q sqrt(q)^(k-1)`, `k = n + 1`. -/
theorem identity_bound_one (hψ : psi ≠ 0) (t : F → ℂ) (hB : ∀ x, ‖t x‖ ≤ 1)
    (n : ℕ) (hn : 1 ≤ n) :
    ‖(Fintype.card F : ℂ) * Ncount t n - (∑ x, t x) ^ (n + 1)‖
      ≤ ((Fintype.card F : ℝ) - 1) * (Fintype.card F : ℝ) *
        Real.sqrt (Fintype.card F) ^ n := by
  refine (identity_bound_closed psi hψ t 1 hB n hn).trans ?_
  have hq0 : (0 : ℝ) ≤ Fintype.card F := Nat.cast_nonneg _
  have hq1 : (1 : ℝ) ≤ Fintype.card F := by exact_mod_cast Fintype.card_pos
  have e : (Fintype.card F : ℝ) ^ ((n : ℝ) / 2 + 1)
      = Real.sqrt (Fintype.card F) ^ n * Fintype.card F := by
    rw [Real.rpow_add_one (by intro h; rw [h] at hq1; norm_num at hq1),
      Real.sqrt_eq_rpow, ← Real.rpow_natCast, ← Real.rpow_mul hq0]
    congr 2; ring
  rw [e, one_pow, mul_one, ← mul_assoc]
  apply le_of_eq; ring

/-- I4, weaker form: `‖q N - M^k‖ ≤ q^((k+3)/2)` with `k = n + 1`. -/
theorem identity_bound_weak (hψ : psi ≠ 0) (t : F → ℂ) (hB : ∀ x, ‖t x‖ ≤ 1)
    (n : ℕ) (hn : 1 ≤ n) :
    ‖(Fintype.card F : ℂ) * Ncount t n - (∑ x, t x) ^ (n + 1)‖
      ≤ (Fintype.card F : ℝ) ^ ((((n + 1 : ℕ) : ℝ) + 3) / 2) := by
  refine (identity_bound_closed psi hψ t 1 hB n hn).trans ?_
  have hq1 : (1 : ℝ) ≤ Fintype.card F := by exact_mod_cast Fintype.card_pos
  have e : (Fintype.card F : ℝ) ^ ((((n + 1 : ℕ) : ℝ) + 3) / 2)
      = (Fintype.card F : ℝ) ^ ((n : ℝ) / 2 + 1) * Fintype.card F := by
    rw [← Real.rpow_add_one (by intro h; rw [h] at hq1; norm_num at hq1)]
    congr 1; push_cast; ring
  rw [e, one_pow, mul_one]
  have hp : 0 ≤ (Fintype.card F : ℝ) ^ ((n : ℝ) / 2 + 1) := by positivity
  nlinarith

end ToyWeil

open ToyWeil in
#print axioms Ssum_zero
open ToyWeil in
#print axioms identity
open ToyWeil in
#print axioms identity_bound
open ToyWeil in
#print axioms identity_bound_closed
open ToyWeil in
#print axioms identity_bound_one
open ToyWeil in
#print axioms identity_bound_weak
