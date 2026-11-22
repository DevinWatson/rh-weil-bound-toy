import ToyWeil.Parseval

/-!
Part A7 (1), round four: the identity `q N = M^k + R` and the fibre bound for the path quadric
`Q_c(x) = c_0 x_0 x_1 + c_1 x_1 x_2 + ... + c_{k-2} x_{k-2} x_{k-1}` with arbitrary coefficients
`c : ℕ → F`, nonzero for the indices that occur.  Own proofs (adapted from `Parseval.lean` and
`Identity.lean` of this tree, not copied from the companion study).
-/

open Finset

namespace ToyWeil

variable {F : Type*} [Field F] [Fintype F] [DecidableEq F] (psi : AddChar F ℂ)

/-- Weighted path quadric on `Fin (k+1) → F`: `∑_{i<k} c i * x_i * x_{i+1}`. -/
def pathQuadricW (c : ℕ → F) {k : ℕ} (x : Fin (k + 1) → F) : F :=
  ∑ i : Fin k, c i * x i.castSucc * x i.succ

theorem pathQuadricW_snoc (c : ℕ → F) {n : ℕ} (x : Fin (n + 1) → F) (y : F) :
    pathQuadricW c (Fin.snoc (α := fun _ => F) x y : Fin (n + 2) → F)
      = pathQuadricW c x + c n * x (Fin.last n) * y := by
  unfold pathQuadricW
  rw [Fin.sum_univ_castSucc]
  simp only [Fin.snoc_castSucc, Fin.snoc_last, Fin.succ_castSucc, Fin.succ_last,
    Fin.coe_castSucc, Fin.val_last]

/-- Iterated sequence with coefficients: `g_{j+2} y = t y * ∑ x, g_{j+1} x * psi (h * c j * x * y)`. -/
def gseqW (c : ℕ → F) (t : F → ℂ) (h : F) : ℕ → F → ℂ
  | 0 => t
  | 1 => t
  | (j + 2) => fun y => t y * ∑ x, gseqW c t h (j + 1) x * psi (h * c j * x * y)

def SsumW (c : ℕ → F) (t : F → ℂ) (h : F) (k : ℕ) : ℂ := ∑ y, gseqW psi c t h k y

theorem gseqW_succ (c : ℕ → F) (t : F → ℂ) (h : F) (j : ℕ) (y : F) :
    gseqW psi c t h (j + 2) y = t y * ∑ x, gseqW psi c t h (j + 1) x * psi (h * c j * x * y) := rfl

theorem gseqW_one (c : ℕ → F) (t : F → ℂ) (h : F) : gseqW psi c t h 1 = t := rfl

theorem gseqW_sq_bound (hψ : psi ≠ 0) (c : ℕ → F) (t : F → ℂ) {h : F} (hh : h ≠ 0) (B : ℝ)
    (hB : ∀ x, ‖t x‖ ≤ B) (j : ℕ) (hc : ∀ i, i < j → c i ≠ 0) :
    ∑ y, ‖gseqW psi c t h (j + 1) y‖ ^ 2 ≤ (B ^ 2 * Fintype.card F) ^ j * ∑ x, ‖t x‖ ^ 2 := by
  induction j with
  | zero => simp [gseqW_one]
  | succ j ih =>
    have hcj : c j ≠ 0 := hc j (Nat.lt_succ_self j)
    have ih' := ih (fun i hi => hc i (Nat.lt_succ_of_lt hi))
    have hstep : ∑ y, ‖gseqW psi c t h (j + 1 + 1) y‖ ^ 2
        ≤ B ^ 2 * ∑ y, ‖∑ x, gseqW psi c t h (j + 1) x * psi (h * c j * x * y)‖ ^ 2 := by
      rw [Finset.mul_sum]
      refine Finset.sum_le_sum fun y _ => ?_
      rw [gseqW_succ, norm_mul, mul_pow]
      exact mul_le_mul_of_nonneg_right (pow_le_pow_left₀ (norm_nonneg _) (hB y) 2)
        (sq_nonneg _)
    rw [parseval_step psi hψ _ (mul_ne_zero hh hcj)] at hstep
    calc _ ≤ _ := hstep
      _ = (B ^ 2 * Fintype.card F) * ∑ y, ‖gseqW psi c t h (j + 1) y‖ ^ 2 := by ring
      _ ≤ (B ^ 2 * Fintype.card F) * ((B ^ 2 * Fintype.card F) ^ j * ∑ x, ‖t x‖ ^ 2) := by
        gcongr
      _ = _ := by ring

/-- Fibre bound for `k = n + 2`, coefficients `c 0, ..., c n` nonzero. -/
theorem iterated_boundW (hψ : psi ≠ 0) (c : ℕ → F) (t : F → ℂ) {h : F} (hh : h ≠ 0) (B : ℝ)
    (hB : ∀ x, ‖t x‖ ≤ B) (n : ℕ) (hc : ∀ i, i < n + 1 → c i ≠ 0) :
    ‖SsumW psi c t h (n + 2)‖
      ≤ Real.sqrt (Fintype.card F) ^ (n + 1) * B ^ n * ∑ x, ‖t x‖ ^ 2 := by
  have hB0 : 0 ≤ B := le_trans (norm_nonneg _) (hB 0)
  set T : ℝ := ∑ x, ‖t x‖ ^ 2 with hT
  have hT0 : 0 ≤ T := Finset.sum_nonneg fun _ _ => sq_nonneg _
  set q : ℝ := (Fintype.card F : ℝ) with hq
  have hq0 : 0 ≤ q := Nat.cast_nonneg _
  have hcn : c n ≠ 0 := hc n (Nat.lt_succ_self n)
  set V : F → ℂ := fun y => ∑ x, gseqW psi c t h (n + 1) x * psi (h * c n * x * y) with hV
  have h1 : ‖SsumW psi c t h (n + 2)‖ ≤ ∑ y, ‖t y‖ * ‖V y‖ := by
    unfold SsumW
    refine (norm_sum_le _ _).trans (le_of_eq ?_)
    refine Finset.sum_congr rfl fun y _ => ?_
    rw [gseqW_succ, norm_mul]
  have h2 : (∑ y, ‖t y‖ * ‖V y‖) ^ 2 ≤ (∑ y, ‖t y‖ ^ 2) * ∑ y, ‖V y‖ ^ 2 :=
    Finset.sum_mul_sq_le_sq_mul_sq _ _ _
  have h3 : ∑ y, ‖V y‖ ^ 2 ≤ q * ((B ^ 2 * q) ^ n * T) := by
    have := parseval_step psi hψ (gseqW psi c t h (n + 1)) (mul_ne_zero hh hcn)
    have h4 := gseqW_sq_bound psi hψ c t hh B hB n (fun i hi => hc i (Nat.lt_succ_of_lt hi))
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
  have h5 : R ^ 2 < ‖SsumW psi c t h (n + 2)‖ ^ 2 := pow_lt_pow_left₀ hlt hR0 two_ne_zero
  have h6 : ‖SsumW psi c t h (n + 2)‖ ^ 2 ≤ (∑ y, ‖t y‖ * ‖V y‖) ^ 2 :=
    pow_le_pow_left₀ (norm_nonneg _) h1 2
  have h7 : T * ∑ y, ‖V y‖ ^ 2 ≤ T * (q * ((B ^ 2 * q) ^ n * T)) :=
    mul_le_mul_of_nonneg_left h3 hT0
  rw [hR2] at h5
  linarith

theorem gseqW_path (hψ : psi ≠ 0) (c : ℕ → F) (t : F → ℂ) (h : F) (n : ℕ) (y : F) :
    gseqW psi c t h (n + 1) y
      = t y * ∑ x : Fin n → F, (∏ i, t (x i)) *
          psi (h * pathQuadricW c (Fin.snoc (α := fun _ => F) x y : Fin (n + 1) → F)) := by
  induction n generalizing y with
  | zero => simp [gseqW_one, pathQuadricW]
  | succ n ih =>
    rw [gseqW_succ]
    congr 1
    rw [← (Fin.snocEquiv fun _ : Fin (n + 1) => F).sum_comp, Fintype.sum_prod_type]
    refine Finset.sum_congr rfl fun z _ => ?_
    rw [ih z, mul_assoc, Finset.sum_mul, Finset.mul_sum]
    refine Finset.sum_congr rfl fun x _ => ?_
    have e : (Fin.snocEquiv fun _ : Fin (n + 1) => F) (z, x) = Fin.snoc x z := rfl
    rw [e, Fin.prod_univ_castSucc, pathQuadricW_snoc]
    simp only [Fin.snoc_castSucc, Fin.snoc_last]
    rw [mul_add, AddChar.map_add_eq_mul]
    have e2 : h * (c n * z * y) = h * c n * z * y := by ring
    rw [e2]; ring

theorem SsumW_eq_path_sum (hψ : psi ≠ 0) (c : ℕ → F) (t : F → ℂ) (h : F) (n : ℕ) :
    SsumW psi c t h (n + 1)
      = ∑ x : Fin (n + 1) → F, (∏ i, t (x i)) * psi (h * pathQuadricW c x) := by
  unfold SsumW
  rw [← (Fin.snocEquiv fun _ : Fin (n + 1) => F).sum_comp, Fintype.sum_prod_type]
  refine Finset.sum_congr rfl fun y _ => ?_
  rw [gseqW_path psi hψ c t h n y, Finset.mul_sum]
  refine Finset.sum_congr rfl fun x _ => ?_
  have e : (Fin.snocEquiv fun _ : Fin (n + 1) => F) (y, x) = Fin.snoc x y := rfl
  rw [e, Fin.prod_univ_castSucc]
  simp only [Fin.snoc_castSucc, Fin.snoc_last]
  ring

theorem SsumW_zero (hψ : psi ≠ 0) (c : ℕ → F) (t : F → ℂ) (n : ℕ) :
    SsumW psi c t 0 (n + 1) = (∑ x, t x) ^ (n + 1) := by
  rw [SsumW_eq_path_sum psi hψ, Fintype.sum_pow]
  simp

/-- Sum of `∏ t (x i)` over the zero set of the weighted path quadric. -/
noncomputable def NcountW (c : ℕ → F) (t : F → ℂ) (n : ℕ) : ℂ :=
  ∑ x ∈ Finset.univ.filter (fun x : Fin (n + 1) → F => pathQuadricW c x = 0), ∏ i, t (x i)

/-- The sum over `h ≠ 0`. -/
noncomputable def RsumW (c : ℕ → F) (t : F → ℂ) (n : ℕ) : ℂ :=
  ∑ h ∈ (Finset.univ : Finset F).erase 0, SsumW psi c t h (n + 1)

/-- The identity `q N = M^k + R` (`k = n + 1`), for arbitrary coefficients `c` (no hypothesis on `c`). -/
theorem identityW (hψ : psi ≠ 0) (c : ℕ → F) (t : F → ℂ) (n : ℕ) :
    (Fintype.card F : ℂ) * NcountW c t n = (∑ x, t x) ^ (n + 1) + RsumW psi c t n := by
  have h1 := orthogonality psi hψ (X := Fin (n + 1) → F) (fun x => ∏ i, t (x i)) (pathQuadricW c)
  have h2 : ∀ h : F, ∑ x : Fin (n + 1) → F, (∏ i, t (x i)) * psi (h * pathQuadricW c x)
      = SsumW psi c t h (n + 1) := fun h => (SsumW_eq_path_sum psi hψ c t h n).symm
  simp_rw [h2] at h1
  unfold NcountW RsumW
  rw [← h1, ← Finset.add_sum_erase _ _ (Finset.mem_univ (0 : F)), SsumW_zero psi hψ]

/-- Fibre bound in the form used by the draft: `k = n + 1 ≥ 2`, `‖t‖ ≤ 1`, nonzero `c 0, ..., c (n-1)`:
`‖q N - M^k‖ ≤ (q - 1) q sqrt(q)^n`. -/
theorem identity_bound_oneW (hψ : psi ≠ 0) (c : ℕ → F) (t : F → ℂ) (hB : ∀ x, ‖t x‖ ≤ 1)
    (n : ℕ) (hn : 1 ≤ n) (hc : ∀ i, i < n → c i ≠ 0) :
    ‖(Fintype.card F : ℂ) * NcountW c t n - (∑ x, t x) ^ (n + 1)‖
      ≤ ((Fintype.card F : ℝ) - 1) * (Fintype.card F : ℝ) * Real.sqrt (Fintype.card F) ^ n := by
  obtain ⟨m, rfl⟩ : ∃ m, n = m + 1 := ⟨n - 1, by omega⟩
  rw [identityW psi hψ c t (m + 1), add_sub_cancel_left]
  unfold RsumW
  refine (norm_sum_le _ _).trans ?_
  have hcard : (((Finset.univ : Finset F).erase 0).card : ℝ) = (Fintype.card F : ℝ) - 1 := by
    rw [Finset.card_erase_of_mem (Finset.mem_univ _), Finset.card_univ,
      Nat.cast_sub Fintype.card_pos, Nat.cast_one]
  have hq1 : (1 : ℝ) ≤ Fintype.card F := by exact_mod_cast Fintype.card_pos
  have hT : ∑ x, ‖t x‖ ^ 2 ≤ (Fintype.card F : ℝ) := by
    have : ∑ x, ‖t x‖ ^ 2 ≤ ∑ _x : F, (1 : ℝ) ^ 2 :=
      Finset.sum_le_sum fun x _ => pow_le_pow_left₀ (norm_nonneg _) (hB x) 2
    simpa using this
  have hbound : ∀ h ∈ (Finset.univ : Finset F).erase 0,
      ‖SsumW psi c t h (m + 1 + 1)‖ ≤ (Fintype.card F : ℝ) * Real.sqrt (Fintype.card F) ^ (m + 1) := by
    intro h hh
    have hh0 : h ≠ 0 := Finset.ne_of_mem_erase hh
    have := iterated_boundW psi hψ c t hh0 1 hB m (fun i hi => hc i (by omega))
    simp only [one_pow, mul_one] at this
    have hs0 : 0 ≤ Real.sqrt (Fintype.card F : ℝ) ^ (m + 1) := by positivity
    calc ‖SsumW psi c t h (m + 1 + 1)‖ ≤ _ := this
      _ ≤ _ := by rw [mul_comm]; gcongr
  have := Finset.sum_le_card_nsmul _ _ _ hbound
  refine this.trans (le_of_eq ?_)
  rw [nsmul_eq_mul, hcard]; ring

end ToyWeil

open ToyWeil in
#print axioms pathQuadricW_snoc
open ToyWeil in
#print axioms gseqW_sq_bound
open ToyWeil in
#print axioms iterated_boundW
open ToyWeil in
#print axioms gseqW_path
open ToyWeil in
#print axioms SsumW_eq_path_sum
open ToyWeil in
#print axioms identityW
open ToyWeil in
#print axioms identity_bound_oneW
