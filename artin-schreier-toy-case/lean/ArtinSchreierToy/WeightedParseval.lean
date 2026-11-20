import Mathlib.Algebra.Group.AddChar
import Mathlib.Analysis.Complex.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Algebra.BigOperators.Ring.Finset

/-!
# Weighted Path-Quadric Orthogonality, Iterated Parseval, and Identity

Extends `ToyWeil.Parseval` and `ToyWeil.Identity` from the plain all-ones path quadric
to an arbitrary nonzero-weighted path quadric
`Q_c(x) = ∑ i : Fin n, c i * x i.castSucc * x i.succ`
over any finite field `F` with a nontrivial additive character `psi : AddChar F ℂ`.

This fixes the unweighted limitation of `toy-case/lean/ToyWeil/` (where `c = (1, 1, 1)`
fails `(S_4)` in characteristic `3` for Kummer and in characteristic `7` for Artin–Schreier
at `d = 3`).
-/

open Finset

namespace ArtinSchreierToy

section Basic

variable {F : Type*} [Field F] [Fintype F] (psi : AddChar F ℂ)

/-- Orthogonality of a nontrivial additive character on a finite field. -/
theorem sum_psi_mul [DecidableEq F] (hψ : psi ≠ 0) (a : F) :
    ∑ h : F, psi (h * a) = if a = 0 then (Fintype.card F : ℂ) else 0 := by
  split_ifs with ha
  · simp [ha]
  · have : ∑ h : F, psi (h * a) = ∑ y : F, psi y :=
      Fintype.sum_equiv (Equiv.mulRight₀ a ha) _ _ (fun _ => rfl)
    rw [this, AddChar.sum_eq_ite]
    simp [hψ]

/-- Orthogonality summed over `h : F` gives `q` times the sum over `{Qf x = 0}`. -/
theorem orthogonality (hψ : psi ≠ 0) {X : Type*} [Fintype X] [DecidableEq F]
    (g : X → ℂ) (Qf : X → F) :
    ∑ h : F, ∑ x : X, g x * psi (h * Qf x)
      = (Fintype.card F : ℂ) * ∑ x ∈ Finset.univ.filter (fun x => Qf x = 0), g x := by
  rw [Finset.sum_comm]
  simp_rw [← Finset.mul_sum, sum_psi_mul psi hψ]
  rw [Finset.sum_filter, Finset.mul_sum]
  refine Finset.sum_congr rfl fun x _ => ?_
  split_ifs <;> simp [mul_comm]

theorem sq_norm_sum (u : F → ℂ) (a : F) (y : F) :
    (((‖∑ x, u x * psi (a * x * y)‖ : ℝ) : ℂ)) ^ 2
      = ∑ x, ∑ x', u x * (starRingEnd ℂ) (u x') * psi (y * (a * (x - x'))) := by
  rw [← Complex.mul_conj', map_sum, Finset.sum_mul_sum]
  refine Finset.sum_congr rfl fun x _ => Finset.sum_congr rfl fun x' _ => ?_
  rw [(starRingEnd ℂ).map_mul, ← AddChar.map_neg_eq_conj]
  have harg : psi (y * (a * (x - x'))) = psi (a * x * y) * psi (-(a * x' * y)) := by
    rw [← AddChar.map_add_eq_mul]; congr 1; ring
  rw [harg]; ring

/-- Single Parseval step with arbitrary nonzero scaling `a ≠ 0`. -/
theorem parseval_step (hψ : psi ≠ 0) (u : F → ℂ) {a : F} (ha : a ≠ 0) :
    ∑ y : F, ‖∑ x, u x * psi (a * x * y)‖ ^ 2
      = (Fintype.card F : ℝ) * ∑ x, ‖u x‖ ^ 2 := by
  classical
  apply Complex.ofReal_injective
  push_cast
  simp_rw [sq_norm_sum psi]
  have h1 : ∑ y : F, ∑ x, ∑ x', u x * (starRingEnd ℂ) (u x') * psi (y * (a * (x - x')))
      = ∑ x, ∑ x', u x * (starRingEnd ℂ) (u x') * ∑ y : F, psi (y * (a * (x - x'))) := by
    rw [Finset.sum_comm]
    refine Finset.sum_congr rfl fun x _ => ?_
    rw [Finset.sum_comm]
    refine Finset.sum_congr rfl fun x' _ => ?_
    rw [Finset.mul_sum]
  rw [h1, Finset.mul_sum]
  refine Finset.sum_congr rfl fun x _ => ?_
  simp_rw [sum_psi_mul psi hψ, mul_eq_zero, ha, false_or, sub_eq_zero]
  simp [Complex.mul_conj', mul_comm]

end Basic

section WeightedPath

variable {F : Type*} [Field F] [Fintype F]

/-- Weighted path quadric `Q_c(x) = ∑ i : Fin n, c i * x i.castSucc * x i.succ`
on `k = n + 1` variables. -/
def weightedPathQuadric {n : ℕ} (c : Fin n → F) (x : Fin (n + 1) → F) : F :=
  ∑ i : Fin n, c i * x i.castSucc * x i.succ

omit [Fintype F] in
theorem weightedPathQuadric_snoc {n : ℕ} (c : Fin (n + 1) → F)
    (x : Fin (n + 1) → F) (y : F) :
    weightedPathQuadric c (Fin.snoc (α := fun _ => F) x y : Fin (n + 2) → F)
      = weightedPathQuadric (Fin.init c) x + c (Fin.last n) * x (Fin.last n) * y := by
  unfold weightedPathQuadric
  rw [Fin.sum_univ_castSucc]
  simp only [Fin.init, Fin.snoc_castSucc, Fin.snoc_last, Fin.succ_castSucc, Fin.succ_last]

/-- Iterated Fourier–multiplication sequence for a weighted path `c : Fin n → F`. -/
def weightedGseq (psi : AddChar F ℂ) (t : F → ℂ) (h : F) :
    ∀ {n : ℕ}, (Fin n → F) → F → ℂ
  | 0, _, y => t y
  | n + 1, c, y =>
      t y * ∑ x : F, weightedGseq psi t h (Fin.init c) x * psi (h * c (Fin.last n) * x * y)

/-- `weightedSsum psi t h c = ∑ y, weightedGseq psi t h c y`. -/
def weightedSsum (psi : AddChar F ℂ) (t : F → ℂ) (h : F) {n : ℕ} (c : Fin n → F) : ℂ :=
  ∑ y : F, weightedGseq psi t h c y

theorem weightedGseq_sq_bound (psi : AddChar F ℂ) (hψ : psi ≠ 0) (t : F → ℂ)
    {h : F} (hh : h ≠ 0) (B : ℝ) (hB : ∀ x, ‖t x‖ ≤ B) :
    ∀ {n : ℕ} (c : Fin n → F), (∀ i, c i ≠ 0) →
      ∑ y : F, ‖weightedGseq psi t h c y‖ ^ 2
        ≤ (B ^ 2 * Fintype.card F) ^ n * ∑ x : F, ‖t x‖ ^ 2
  | 0, _, _ => by simp [weightedGseq]
  | n + 1, c, hc => by
      have ih := weightedGseq_sq_bound psi hψ t hh B hB (Fin.init c) (fun i => hc i.castSucc)
      have ha : h * c (Fin.last n) ≠ 0 := mul_ne_zero hh (hc (Fin.last n))
      have hstep : ∑ y : F, ‖weightedGseq psi t h c y‖ ^ 2
          ≤ B ^ 2 * ∑ y : F, ‖∑ x : F, weightedGseq psi t h (Fin.init c) x *
              psi ((h * c (Fin.last n)) * x * y)‖ ^ 2 := by
        rw [Finset.mul_sum]
        refine Finset.sum_le_sum fun y _ => ?_
        simp only [weightedGseq, norm_mul, mul_pow]
        exact mul_le_mul_of_nonneg_right (pow_le_pow_left₀ (norm_nonneg _) (hB y) 2) (sq_nonneg _)
      rw [parseval_step psi hψ _ ha] at hstep
      calc _ ≤ _ := hstep
        _ = (B ^ 2 * Fintype.card F) * ∑ y : F, ‖weightedGseq psi t h (Fin.init c) y‖ ^ 2 := by
              ring
        _ ≤ (B ^ 2 * Fintype.card F) *
              ((B ^ 2 * Fintype.card F) ^ n * ∑ x : F, ‖t x‖ ^ 2) := by
              gcongr
        _ = (B ^ 2 * Fintype.card F) ^ (n + 1) * ∑ x : F, ‖t x‖ ^ 2 := by ring

/-- Weighted iterated Parseval bound for `k = n + 2` variables (`n + 1` nonzero weights). -/
theorem weighted_iterated_bound (psi : AddChar F ℂ) (hψ : psi ≠ 0) (t : F → ℂ)
    {h : F} (hh : h ≠ 0) (B : ℝ) (hB : ∀ x, ‖t x‖ ≤ B) {n : ℕ}
    (c : Fin (n + 1) → F) (hc : ∀ i, c i ≠ 0) :
    ‖weightedSsum psi t h c‖
      ≤ Real.sqrt (Fintype.card F) ^ (n + 1) * B ^ n * ∑ x : F, ‖t x‖ ^ 2 := by
  have hB0 : 0 ≤ B := le_trans (norm_nonneg _) (hB 0)
  set T : ℝ := ∑ x : F, ‖t x‖ ^ 2
  have hT0 : 0 ≤ T := Finset.sum_nonneg fun _ _ => sq_nonneg _
  set q : ℝ := (Fintype.card F : ℝ)
  have hq0 : 0 ≤ q := Nat.cast_nonneg _
  have ha : h * c (Fin.last n) ≠ 0 := mul_ne_zero hh (hc (Fin.last n))
  set V : F → ℂ := fun y =>
    ∑ x : F, weightedGseq psi t h (Fin.init c) x * psi ((h * c (Fin.last n)) * x * y) with hV
  have h1 : ‖weightedSsum psi t h c‖ ≤ ∑ y : F, ‖t y‖ * ‖V y‖ := by
    unfold weightedSsum
    refine (norm_sum_le _ _).trans (le_of_eq ?_)
    refine Finset.sum_congr rfl fun y _ => ?_
    simp only [weightedGseq, norm_mul, hV]
  have h2 : (∑ y : F, ‖t y‖ * ‖V y‖) ^ 2 ≤ T * ∑ y : F, ‖V y‖ ^ 2 :=
    Finset.sum_mul_sq_le_sq_mul_sq _ _ _
  have h3 : ∑ y : F, ‖V y‖ ^ 2 ≤ q * ((B ^ 2 * q) ^ n * T) := by
    have hp := parseval_step psi hψ (weightedGseq psi t h (Fin.init c)) ha
    have h4 := weightedGseq_sq_bound psi hψ t hh B hB (Fin.init c) (fun i => hc i.castSucc)
    simp only [hV]
    rw [hp]
    gcongr
  set R : ℝ := Real.sqrt q ^ (n + 1) * B ^ n * T
  have hR0 : 0 ≤ R := by positivity
  have hs : Real.sqrt q ^ 2 = q := Real.sq_sqrt hq0
  have hR2 : R ^ 2 = T * (q * ((B ^ 2 * q) ^ n * T)) := by
    have : R ^ 2 = (Real.sqrt q ^ 2) ^ (n + 1) * (B ^ 2) ^ n * T ^ 2 := by
      simp only [R]; ring
    rw [this, hs]; ring
  by_contra hlt
  push Not at hlt
  have h5 : R ^ 2 < ‖weightedSsum psi t h c‖ ^ 2 := pow_lt_pow_left₀ hlt hR0 two_ne_zero
  have h6 : ‖weightedSsum psi t h c‖ ^ 2 ≤ (∑ y : F, ‖t y‖ * ‖V y‖) ^ 2 :=
    pow_le_pow_left₀ (norm_nonneg _) h1 2
  have h7 : T * ∑ y : F, ‖V y‖ ^ 2 ≤ T * (q * ((B ^ 2 * q) ^ n * T)) :=
    mul_le_mul_of_nonneg_left h3 hT0
  rw [hR2] at h5
  linarith

/-- Weighted iterated Parseval bound in real-power form for any `n ≥ 1` (`k = n + 1 ≥ 2`). -/
theorem weighted_iterated_bound_rpow (psi : AddChar F ℂ) (hψ : psi ≠ 0) (t : F → ℂ)
    {h : F} (hh : h ≠ 0) (B : ℝ) (hB : ∀ x, ‖t x‖ ≤ B) {n : ℕ} (hn : 1 ≤ n)
    (c : Fin n → F) (hc : ∀ i, c i ≠ 0) :
    ‖weightedSsum psi t h c‖
      ≤ (Fintype.card F : ℝ) ^ ((n : ℝ) / 2) * B ^ (n - 1) * ∑ x : F, ‖t x‖ ^ 2 := by
  obtain ⟨m, rfl⟩ : ∃ m, n = m + 1 := ⟨n - 1, by omega⟩
  have h1 := weighted_iterated_bound psi hψ t hh B hB c hc
  have hq0 : (0 : ℝ) ≤ Fintype.card F := Nat.cast_nonneg _
  have h2 : Real.sqrt (Fintype.card F) ^ (m + 1)
      = (Fintype.card F : ℝ) ^ (((m + 1 : ℕ) : ℝ) / 2) := by
    rw [Real.sqrt_eq_rpow, ← Real.rpow_natCast, ← Real.rpow_mul hq0]
    congr 1; ring
  rw [h2] at h1
  simpa using h1

theorem weightedGseq_path (psi : AddChar F ℂ) (t : F → ℂ) (h : F) :
    ∀ {n : ℕ} (c : Fin n → F) (y : F),
      weightedGseq psi t h c y
        = t y * ∑ x : Fin n → F, (∏ i, t (x i)) *
            psi (h * weightedPathQuadric c (Fin.snoc (α := fun _ => F) x y : Fin (n + 1) → F))
  | 0, c, y => by simp [weightedGseq, weightedPathQuadric]
  | n + 1, c, y => by
      simp only [weightedGseq]
      congr 1
      rw [← (Fin.snocEquiv fun _ : Fin (n + 1) => F).sum_comp, Fintype.sum_prod_type]
      refine Finset.sum_congr rfl fun z _ => ?_
      rw [weightedGseq_path psi t h (Fin.init c) z, mul_assoc, Finset.sum_mul, Finset.mul_sum]
      refine Finset.sum_congr rfl fun x _ => ?_
      have e : (Fin.snocEquiv fun _ : Fin (n + 1) => F) (z, x) = Fin.snoc x z := rfl
      rw [e, Fin.prod_univ_castSucc, weightedPathQuadric_snoc]
      simp only [Fin.snoc_castSucc, Fin.snoc_last]
      rw [mul_add, AddChar.map_add_eq_mul]
      have e2 : h * (c (Fin.last n) * z * y) = h * c (Fin.last n) * z * y := by ring
      rw [e2]; ring

/-- Expansion of `weightedSsum` as the full `k`-variable weighted path-quadric exponential sum. -/
theorem weightedSsum_eq_path_sum (psi : AddChar F ℂ) (t : F → ℂ) (h : F)
    {n : ℕ} (c : Fin n → F) :
    weightedSsum psi t h c
      = ∑ x : Fin (n + 1) → F, (∏ i, t (x i)) * psi (h * weightedPathQuadric c x) := by
  unfold weightedSsum
  rw [← (Fin.snocEquiv fun _ : Fin (n + 1) => F).sum_comp, Fintype.sum_prod_type]
  refine Finset.sum_congr rfl fun y _ => ?_
  rw [weightedGseq_path psi t h c y, Finset.mul_sum]
  refine Finset.sum_congr rfl fun x _ => ?_
  have e : (Fin.snocEquiv fun _ : Fin (n + 1) => F) (y, x) = Fin.snoc x y := rfl
  rw [e, Fin.prod_univ_castSucc]
  simp only [Fin.snoc_castSucc, Fin.snoc_last]
  ring

/-- The `h = 0` mode equals `M^{n+1}`. -/
theorem weightedSsum_zero (psi : AddChar F ℂ) (t : F → ℂ) {n : ℕ} (c : Fin n → F) :
    weightedSsum psi t 0 c = (∑ x : F, t x) ^ (n + 1) := by
  rw [weightedSsum_eq_path_sum, Fintype.sum_pow]
  simp

/-- Weighted sum of `∏ t (x i)` over the zero locus `Q_c(x) = 0`. -/
noncomputable def weightedNcount [DecidableEq F] (t : F → ℂ) {n : ℕ} (c : Fin n → F) : ℂ :=
  ∑ x ∈ Finset.univ.filter (fun x : Fin (n + 1) → F => weightedPathQuadric c x = 0),
    ∏ i, t (x i)

/-- Sum of `weightedSsum` over nonzero `h ∈ Fˣ`. -/
noncomputable def weightedRsum [DecidableEq F] (psi : AddChar F ℂ) (t : F → ℂ)
    {n : ℕ} (c : Fin n → F) : ℂ :=
  ∑ h ∈ (Finset.univ : Finset F).erase 0, weightedSsum psi t h c

/-- Exact weighted identity `q * N_c = M^k + R_c` (`k = n + 1`). -/
theorem weighted_identity [DecidableEq F] (psi : AddChar F ℂ) (hψ : psi ≠ 0) (t : F → ℂ)
    {n : ℕ} (c : Fin n → F) :
    (Fintype.card F : ℂ) * weightedNcount t c
      = (∑ x : F, t x) ^ (n + 1) + weightedRsum psi t c := by
  have h1 := orthogonality psi hψ (X := Fin (n + 1) → F)
    (fun x => ∏ i, t (x i)) (weightedPathQuadric c)
  have h2 : ∀ h : F, ∑ x : Fin (n + 1) → F, (∏ i, t (x i)) * psi (h * weightedPathQuadric c x)
      = weightedSsum psi t h c := fun h => (weightedSsum_eq_path_sum psi t h c).symm
  simp_rw [h2] at h1
  unfold weightedNcount weightedRsum
  rw [← h1, ← Finset.add_sum_erase _ _ (Finset.mem_univ (0 : F)), weightedSsum_zero]

/-- Sharp weighted Parseval bound for `‖t‖ ≤ 1`:
`‖q * N_c - M^k‖ ≤ (q - 1) * q * sqrt(q)^(k - 1)` for `k = n + 1 ≥ 2`. -/
theorem weighted_identity_bound_one [DecidableEq F] (psi : AddChar F ℂ) (hψ : psi ≠ 0)
    (t : F → ℂ) (hB : ∀ x, ‖t x‖ ≤ 1) {n : ℕ} (hn : 1 ≤ n)
    (c : Fin n → F) (hc : ∀ i, c i ≠ 0) :
    ‖(Fintype.card F : ℂ) * weightedNcount t c - (∑ x : F, t x) ^ (n + 1)‖
      ≤ ((Fintype.card F : ℝ) - 1) * (Fintype.card F : ℝ) *
        Real.sqrt (Fintype.card F) ^ n := by
  rw [weighted_identity psi hψ t c, add_sub_cancel_left]
  unfold weightedRsum
  have hcard : (((Finset.univ : Finset F).erase 0).card : ℝ) = (Fintype.card F : ℝ) - 1 := by
    rw [Finset.card_erase_of_mem (Finset.mem_univ _), Finset.card_univ,
      Nat.cast_sub Fintype.card_pos, Nat.cast_one]
  have hsum : ∑ x : F, ‖t x‖ ^ 2 ≤ (Fintype.card F : ℝ) := by
    have : ∑ x : F, ‖t x‖ ^ 2 ≤ ∑ _x : F, (1 : ℝ) :=
      Finset.sum_le_sum fun x _ => by
        have := pow_le_pow_left₀ (norm_nonneg _) (hB x) 2
        simpa using this
    simpa using this
  have hq0 : (0 : ℝ) ≤ Fintype.card F := Nat.cast_nonneg _
  have hsqrt : (Fintype.card F : ℝ) ^ ((n : ℝ) / 2) = Real.sqrt (Fintype.card F) ^ n := by
    rw [Real.sqrt_eq_rpow, ← Real.rpow_natCast, ← Real.rpow_mul hq0]
    congr 1; ring
  have hstep : ‖∑ h ∈ (Finset.univ : Finset F).erase 0, weightedSsum psi t h c‖
      ≤ ((Fintype.card F : ℝ) - 1) *
          (Real.sqrt (Fintype.card F) ^ n * (Fintype.card F : ℝ)) := by
    refine (norm_sum_le _ _).trans ?_
    rw [← hcard, ← nsmul_eq_mul]
    refine Finset.sum_le_card_nsmul _ _ _ fun h hh => ?_
    have hh0 : h ≠ 0 := Finset.ne_of_mem_erase hh
    have hb := weighted_iterated_bound_rpow psi hψ t hh0 1 hB hn c hc
    rw [one_pow, mul_one, hsqrt] at hb
    exact hb.trans (mul_le_mul_of_nonneg_left hsum (by positivity))
  exact hstep.trans (le_of_eq (by ring))

/-- Clean exponent bound `‖q * N_c - M^k‖ ≤ q^((k + 3) / 2)` (`k = n + 1 ≥ 2`) for any
nonzero weights `c : Fin n → F` and any `t` with `‖t‖ ≤ 1` (including `t(x) = psi(f(x))`). -/
theorem weighted_identity_bound_weak [DecidableEq F] (psi : AddChar F ℂ) (hψ : psi ≠ 0)
    (t : F → ℂ) (hB : ∀ x, ‖t x‖ ≤ 1) {n : ℕ} (hn : 1 ≤ n)
    (c : Fin n → F) (hc : ∀ i, c i ≠ 0) :
    ‖(Fintype.card F : ℂ) * weightedNcount t c - (∑ x : F, t x) ^ (n + 1)‖
      ≤ (Fintype.card F : ℝ) ^ ((((n + 1 : ℕ) : ℝ) + 3) / 2) := by
  refine (weighted_identity_bound_one psi hψ t hB hn c hc).trans ?_
  have hq0 : (0 : ℝ) ≤ Fintype.card F := Nat.cast_nonneg _
  have hqpos : (0 : ℝ) < Fintype.card F := by exact_mod_cast Fintype.card_pos
  have hpow : (Fintype.card F : ℝ) ^ ((((n + 1 : ℕ) : ℝ) + 3) / 2)
      = (Fintype.card F : ℝ) * (Fintype.card F : ℝ) * Real.sqrt (Fintype.card F) ^ n := by
    rw [Real.sqrt_eq_rpow, ← Real.rpow_natCast, ← Real.rpow_mul hq0]
    have heq : (Fintype.card F : ℝ) * (Fintype.card F : ℝ) = (Fintype.card F : ℝ) ^ (2 : ℝ) := by
      rw [Real.rpow_two, sq]
    rw [heq, ← Real.rpow_add hqpos]
    congr 1; push_cast; ring
  rw [hpow]
  have hnn : 0 ≤ (Fintype.card F : ℝ) * Real.sqrt (Fintype.card F) ^ n := by positivity
  nlinarith

end WeightedPath

end ArtinSchreierToy

open ArtinSchreierToy in #print axioms orthogonality
open ArtinSchreierToy in #print axioms parseval_step
open ArtinSchreierToy in #print axioms weighted_iterated_bound
open ArtinSchreierToy in #print axioms weighted_iterated_bound_rpow
open ArtinSchreierToy in #print axioms weightedSsum_eq_path_sum
open ArtinSchreierToy in #print axioms weighted_identity
open ArtinSchreierToy in #print axioms weighted_identity_bound_one
open ArtinSchreierToy in #print axioms weighted_identity_bound_weak
