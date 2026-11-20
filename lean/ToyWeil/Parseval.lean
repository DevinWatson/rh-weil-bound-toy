import Mathlib.Algebra.Group.AddChar
import Mathlib.Analysis.Complex.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Algebra.BigOperators.Ring.Finset

open Finset

namespace ToyWeil

variable {F : Type*} [Field F] [Fintype F] [DecidableEq F] (psi : AddChar F ℂ)

/-- Orthogonality of a nontrivial additive character on a finite field. -/
theorem sum_psi_mul (hψ : psi ≠ 0) (a : F) :
    ∑ h : F, psi (h * a) = if a = 0 then (Fintype.card F : ℂ) else 0 := by
  classical
  split_ifs with ha
  · simp [ha]
  · have : ∑ h : F, psi (h * a) = ∑ y : F, psi y :=
      Fintype.sum_equiv (Equiv.mulRight₀ a ha) _ _ (fun h => rfl)
    rw [this, AddChar.sum_eq_ite]
    simp [hψ]

/-- P1 (orthogonality). -/
theorem orthogonality (hψ : psi ≠ 0) {X : Type*} [Fintype X] (g : X → ℂ) (Qf : X → F) :
    ∑ h : F, ∑ x : X, g x * psi (h * Qf x)
      = (Fintype.card F : ℂ) * ∑ x ∈ Finset.univ.filter (fun x => Qf x = 0), g x := by
  classical
  rw [Finset.sum_comm]
  simp_rw [← Finset.mul_sum, sum_psi_mul psi hψ]
  rw [Finset.sum_filter, Finset.mul_sum]
  refine Finset.sum_congr rfl fun x _ => ?_
  split_ifs <;> simp [mul_comm]

theorem sq_norm_sum (hψ : psi ≠ 0) (u : F → ℂ) (h : F) (y : F) :
    (((‖∑ x, u x * psi (h * x * y)‖ : ℝ) : ℂ)) ^ 2
      = ∑ x, ∑ x', u x * (starRingEnd ℂ) (u x') * psi (y * (h * (x - x'))) := by
  rw [← Complex.mul_conj', map_sum, Finset.sum_mul_sum]
  refine Finset.sum_congr rfl fun x _ => Finset.sum_congr rfl fun x' _ => ?_
  rw [(starRingEnd ℂ).map_mul, ← AddChar.map_neg_eq_conj]
  have : psi (y * (h * (x - x'))) = psi (h * x * y) * psi (-(h * x' * y)) := by
    rw [← AddChar.map_add_eq_mul]; congr 1; ring
  rw [this]; ring

/-- P2 (one Parseval step). -/
theorem parseval_step (hψ : psi ≠ 0) (u : F → ℂ) {h : F} (hh : h ≠ 0) :
    ∑ y : F, ‖∑ x, u x * psi (h * x * y)‖ ^ 2
      = (Fintype.card F : ℝ) * ∑ x, ‖u x‖ ^ 2 := by
  apply Complex.ofReal_injective
  push_cast
  simp_rw [sq_norm_sum psi hψ]
  have h1 : ∑ y : F, ∑ x, ∑ x', u x * (starRingEnd ℂ) (u x') * psi (y * (h * (x - x')))
      = ∑ x, ∑ x', u x * (starRingEnd ℂ) (u x') * ∑ y : F, psi (y * (h * (x - x'))) := by
    rw [Finset.sum_comm]
    refine Finset.sum_congr rfl fun x _ => ?_
    rw [Finset.sum_comm]
    refine Finset.sum_congr rfl fun x' _ => ?_
    rw [Finset.mul_sum]
  rw [h1, Finset.mul_sum]
  refine Finset.sum_congr rfl fun x _ => ?_
  simp_rw [sum_psi_mul psi hψ, mul_eq_zero, hh, false_or, sub_eq_zero]
  simp [Complex.mul_conj', mul_ite, mul_comm]

/-- The iterated sequence: `gseq 1 = t`, `gseq (j+1) y = t y * ∑ x, gseq j x * psi (h x y)`
(index `0` is a dummy value, equal to `t`). -/
def gseq (t : F → ℂ) (h : F) : ℕ → F → ℂ
  | 0 => t
  | 1 => t
  | (j + 2) => fun y => t y * ∑ x, gseq t h (j + 1) x * psi (h * x * y)

/-- `S k = ∑ y, g_k y`. -/
def Ssum (t : F → ℂ) (h : F) (k : ℕ) : ℂ := ∑ y, gseq psi t h k y

theorem gseq_one (t : F → ℂ) (h : F) : gseq psi t h 1 = t := rfl

theorem gseq_succ (t : F → ℂ) (h : F) (j : ℕ) (y : F) :
    gseq psi t h (j + 2) y = t y * ∑ x, gseq psi t h (j + 1) x * psi (h * x * y) := rfl

theorem gseq_sq_bound (hψ : psi ≠ 0) (t : F → ℂ) {h : F} (hh : h ≠ 0) (B : ℝ)
    (hB : ∀ x, ‖t x‖ ≤ B) (j : ℕ) :
    ∑ y, ‖gseq psi t h (j + 1) y‖ ^ 2 ≤ (B ^ 2 * Fintype.card F) ^ j * ∑ x, ‖t x‖ ^ 2 := by
  induction j with
  | zero => simp [gseq_one]
  | succ j ih =>
    have hstep : ∑ y, ‖gseq psi t h (j + 1 + 1) y‖ ^ 2
        ≤ B ^ 2 * ∑ y, ‖∑ x, gseq psi t h (j + 1) x * psi (h * x * y)‖ ^ 2 := by
      rw [Finset.mul_sum]
      refine Finset.sum_le_sum fun y _ => ?_
      rw [gseq_succ, norm_mul, mul_pow]
      exact mul_le_mul_of_nonneg_right (pow_le_pow_left₀ (norm_nonneg _) (hB y) 2)
        (sq_nonneg _)
    rw [parseval_step psi hψ _ hh] at hstep
    calc _ ≤ _ := hstep
      _ = (B ^ 2 * Fintype.card F) * ∑ y, ‖gseq psi t h (j + 1) y‖ ^ 2 := by ring
      _ ≤ (B ^ 2 * Fintype.card F) * ((B ^ 2 * Fintype.card F) ^ j * ∑ x, ‖t x‖ ^ 2) := by
        gcongr
      _ = _ := by ring

/-- P3 (iterated bound), for `k = n + 2`. -/
theorem iterated_bound (hψ : psi ≠ 0) (t : F → ℂ) {h : F} (hh : h ≠ 0) (B : ℝ)
    (hB : ∀ x, ‖t x‖ ≤ B) (n : ℕ) :
    ‖Ssum psi t h (n + 2)‖
      ≤ Real.sqrt (Fintype.card F) ^ (n + 1) * B ^ n * ∑ x, ‖t x‖ ^ 2 := by
  have hB0 : 0 ≤ B := le_trans (norm_nonneg _) (hB 0)
  set T : ℝ := ∑ x, ‖t x‖ ^ 2 with hT
  have hT0 : 0 ≤ T := Finset.sum_nonneg fun _ _ => sq_nonneg _
  set q : ℝ := (Fintype.card F : ℝ) with hq
  have hq0 : 0 ≤ q := Nat.cast_nonneg _
  set V : F → ℂ := fun y => ∑ x, gseq psi t h (n + 1) x * psi (h * x * y) with hV
  have h1 : ‖Ssum psi t h (n + 2)‖ ≤ ∑ y, ‖t y‖ * ‖V y‖ := by
    unfold Ssum
    refine (norm_sum_le _ _).trans (le_of_eq ?_)
    refine Finset.sum_congr rfl fun y _ => ?_
    rw [gseq_succ, norm_mul]
  have h2 : (∑ y, ‖t y‖ * ‖V y‖) ^ 2 ≤ (∑ y, ‖t y‖ ^ 2) * ∑ y, ‖V y‖ ^ 2 :=
    Finset.sum_mul_sq_le_sq_mul_sq _ _ _
  have h3 : ∑ y, ‖V y‖ ^ 2 ≤ q * ((B ^ 2 * q) ^ n * T) := by
    have := parseval_step psi hψ (gseq psi t h (n + 1)) hh
    have h4 := gseq_sq_bound psi hψ t hh B hB n
    simp only [hV]
    rw [this]
    gcongr
  set R : ℝ := Real.sqrt q ^ (n + 1) * B ^ n * T with hR
  have hR0 : 0 ≤ R := by positivity
  have hs : Real.sqrt q ^ 2 = q := Real.sq_sqrt hq0
  have hR2 : R ^ 2 = T * (q * ((B ^ 2 * q) ^ n * T)) := by
    have : R ^ 2 = (Real.sqrt q ^ 2) ^ (n + 1) * (B ^ 2) ^ n * T ^ 2 := by
      simp only [hR]; ring
    rw [this, hs]; ring
  by_contra hlt
  push_neg at hlt
  have h5 : R ^ 2 < ‖Ssum psi t h (n + 2)‖ ^ 2 := pow_lt_pow_left₀ hlt hR0 two_ne_zero
  have h6 : ‖Ssum psi t h (n + 2)‖ ^ 2 ≤ (∑ y, ‖t y‖ * ‖V y‖) ^ 2 :=
    pow_le_pow_left₀ (norm_nonneg _) h1 2
  have h7 : T * ∑ y, ‖V y‖ ^ 2 ≤ T * (q * ((B ^ 2 * q) ^ n * T)) :=
    mul_le_mul_of_nonneg_left h3 hT0
  rw [hR2] at h5
  linarith

/-- P3 for general `k ≥ 2`, with a real power. -/
theorem iterated_bound_rpow (hψ : psi ≠ 0) (t : F → ℂ) {h : F} (hh : h ≠ 0) (B : ℝ)
    (hB : ∀ x, ‖t x‖ ≤ B) (k : ℕ) (hk : 2 ≤ k) :
    ‖Ssum psi t h k‖
      ≤ (Fintype.card F : ℝ) ^ (((k : ℝ) - 1) / 2) * B ^ (k - 2) * ∑ x, ‖t x‖ ^ 2 := by
  obtain ⟨n, rfl⟩ : ∃ n, k = n + 2 := ⟨k - 2, by omega⟩
  have h1 := iterated_bound psi hψ t hh B hB n
  have hq0 : (0 : ℝ) ≤ Fintype.card F := Nat.cast_nonneg _
  have h2 : Real.sqrt (Fintype.card F) ^ (n + 1)
      = (Fintype.card F : ℝ) ^ ((((n + 2 : ℕ) : ℝ) - 1) / 2) := by
    rw [Real.sqrt_eq_rpow, ← Real.rpow_natCast, ← Real.rpow_mul hq0]
    congr 1; push_cast; ring
  rw [h2] at h1
  simpa using h1

/-- The path quadric `x₀x₁ + x₁x₂ + ⋯ + x_{k-1}x_k` on `Fin (k+1) → F`. -/
def pathQuadric {k : ℕ} (x : Fin (k + 1) → F) : F := ∑ i : Fin k, x i.castSucc * x i.succ

theorem pathQuadric_snoc {n : ℕ} (x : Fin (n + 1) → F) (y : F) :
    pathQuadric (Fin.snoc (α := fun _ => F) x y : Fin (n + 2) → F)
      = pathQuadric x + x (Fin.last n) * y := by
  unfold pathQuadric
  rw [Fin.sum_univ_castSucc]
  simp only [Fin.snoc_castSucc, Fin.snoc_last, Fin.succ_castSucc, Fin.succ_last]

theorem gseq_path (hψ : psi ≠ 0) (t : F → ℂ) (h : F) (n : ℕ) (y : F) :
    gseq psi t h (n + 1) y
      = t y * ∑ x : Fin n → F, (∏ i, t (x i)) *
          psi (h * pathQuadric (Fin.snoc (α := fun _ => F) x y : Fin (n + 1) → F)) := by
  induction n generalizing y with
  | zero => simp [gseq_one, pathQuadric]
  | succ n ih =>
    rw [gseq_succ]
    congr 1
    rw [← (Fin.snocEquiv fun _ : Fin (n + 1) => F).sum_comp, Fintype.sum_prod_type]
    refine Finset.sum_congr rfl fun z _ => ?_
    rw [ih z, mul_assoc, Finset.sum_mul, Finset.mul_sum]
    refine Finset.sum_congr rfl fun x _ => ?_
    have e : (Fin.snocEquiv fun _ : Fin (n + 1) => F) (z, x) = Fin.snoc x z := rfl
    rw [e, Fin.prod_univ_castSucc, pathQuadric_snoc]
    simp only [Fin.snoc_castSucc, Fin.snoc_last]
    rw [mul_add, AddChar.map_add_eq_mul]
    have e2 : h * (z * y) = h * z * y := by ring
    rw [e2]; ring

/-- P4: `S k` as a sum over all `x : Fin k → F` of `∏ t (x i) * psi (h * pathQuadric x)`,
for every `k = n + 1`. -/
theorem Ssum_eq_path_sum (hψ : psi ≠ 0) (t : F → ℂ) (h : F) (n : ℕ) :
    Ssum psi t h (n + 1)
      = ∑ x : Fin (n + 1) → F, (∏ i, t (x i)) * psi (h * pathQuadric x) := by
  unfold Ssum
  rw [← (Fin.snocEquiv fun _ : Fin (n + 1) => F).sum_comp, Fintype.sum_prod_type]
  refine Finset.sum_congr rfl fun y _ => ?_
  rw [gseq_path psi hψ t h n y, Finset.mul_sum]
  refine Finset.sum_congr rfl fun x _ => ?_
  have e : (Fin.snocEquiv fun _ : Fin (n + 1) => F) (y, x) = Fin.snoc x y := rfl
  rw [e, Fin.prod_univ_castSucc]
  simp only [Fin.snoc_castSucc, Fin.snoc_last]
  ring

end ToyWeil

open ToyWeil in
#print axioms iterated_bound_rpow
open ToyWeil in
#print axioms pathQuadric_snoc
open ToyWeil in
#print axioms gseq_path
open ToyWeil in
#print axioms Ssum_eq_path_sum
open ToyWeil in
#print axioms sum_psi_mul
open ToyWeil in
#print axioms orthogonality
open ToyWeil in
#print axioms parseval_step
open ToyWeil in
#print axioms iterated_bound
