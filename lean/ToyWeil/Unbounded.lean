import ToyWeil.Endgame2

/-!
Part A7 (2), round four: the endgame with a field degree `s(k)` depending on `k`, for an
unbounded set of `k`; and the signed dichotomy with the field allowed to depend on `k`.
Own proofs.  `ρ = (q^s)^((k+3)/2) = q^(s (k+3) / 2)`.
-/

namespace ToyWeil

/-- Exact `s`-th root: `x^(s k) ≤ r^(s (k+3))` with `s ≥ 1`, `x, r ≥ 0` gives `x^k ≤ r^(k+3)`. -/
theorem pow_root_step {x r : ℝ} (hx : 0 ≤ x) (hr : 0 ≤ r) {s k : ℕ} (hs : 1 ≤ s)
    (h : x ^ (s * k) ≤ r ^ (s * (k + 3))) : x ^ k ≤ r ^ (k + 3) := by
  have h1 : (x ^ k) ^ s ≤ (r ^ (k + 3)) ^ s := by
    rw [← pow_mul, ← pow_mul, mul_comm k s, mul_comm (k + 3) s]; exact h
  exact (pow_le_pow_iff_left₀ (by positivity) (by positivity) (by omega)).1 h1

/-- Limit in `k`: if `x^k ≤ r^(k+3)` for an unbounded set of `k`, then `x ≤ r`. -/
theorem le_of_pow_le_unbounded {x r : ℝ} (hx : 0 ≤ x) (hr : 0 ≤ r)
    (H : ∀ K : ℕ, ∃ k : ℕ, K ≤ k ∧ x ^ k ≤ r ^ (k + 3)) : x ≤ r := by
  by_contra hlt
  push_neg at hlt
  have hxpos : 0 < x := lt_of_le_of_lt hr hlt
  rcases hr.eq_or_lt with h0 | hpos
  · obtain ⟨k, hk, hk2⟩ := H 1
    rw [← h0] at hk2
    have : (0 : ℝ) ^ (k + 3) = 0 := by simp
    rw [this] at hk2
    have : 0 < x ^ k := by positivity
    linarith
  · have hrat : 1 < x / r := by rw [lt_div_iff₀ hpos]; linarith
    obtain ⟨N0, hN0⟩ := pow_unbounded_of_one_lt (r ^ 3) hrat
    obtain ⟨k, hk, hk2⟩ := H N0
    have hmono : (x / r) ^ N0 ≤ (x / r) ^ k := pow_le_pow_right₀ hrat.le hk
    have hxk : x ^ k = (x / r) ^ k * r ^ k := by rw [← mul_pow]; field_simp
    have hrk : 0 < r ^ k := pow_pos hpos _
    have : (x / r) ^ k * r ^ k ≤ r ^ 3 * r ^ k := by
      rw [← hxk]; calc x ^ k ≤ r ^ (k + 3) := hk2
        _ = r ^ 3 * r ^ k := by rw [pow_add]; ring
    have := le_of_mul_le_mul_right this hrk
    linarith

/-- Single eigenvalue form: `‖α‖^(s k) ≤ q^(s (k+3)/2)` for an unbounded set of `k`, each with its
own `s ≥ 1`, gives `‖α‖ ≤ sqrt q`. -/
theorem endgame_unbounded (α : ℂ) (q : ℝ) (hq : 1 < q)
    (H : ∀ K : ℕ, ∃ k : ℕ, K ≤ k ∧ ∃ s : ℕ, 1 ≤ s ∧
      ‖α‖ ^ (s * k) ≤ q ^ ((s : ℝ) * ((k : ℝ) + 3) / 2)) :
    ‖α‖ ≤ Real.sqrt q := by
  have hq0 : 0 ≤ q := by linarith
  refine le_of_pow_le_unbounded (norm_nonneg _) (Real.sqrt_nonneg _) fun K => ?_
  obtain ⟨k, hk, s, hs, h⟩ := H K
  refine ⟨k, hk, pow_root_step (norm_nonneg _) (Real.sqrt_nonneg _) hs ?_⟩
  have e : q ^ ((s : ℝ) * ((k : ℝ) + 3) / 2) = (Real.sqrt q) ^ (s * (k + 3)) := by
    rw [Real.sqrt_eq_rpow, ← Real.rpow_natCast, ← Real.rpow_mul hq0]
    congr 1; push_cast; ring
  rwa [e] at h

/-- The signed dichotomy of S9 for a fixed `k` and a field `F_Q`, `Q = q^s` (so `ρ = Q^((k+3)/2)`
is any real).  Here `a` are the eigenvalues of the tensor-power part `T` of `H^{k+1}_c` over `F_Q`,
`e` the other eigenvalues of `H^{k+1}_c`, `b` those of `H^{k+2}_c` (wrong parity). -/
theorem dichotomy_field_dep {A E B : Type*} [Fintype A] [Fintype E] [Fintype B]
    (a : A → ℂ) (e : E → ℂ) (b : B → ℂ) (q : ℝ) (s k : ℕ) (C : ℝ) (hq : 1 < q)
    (h : ∀ n : ℕ, 1 ≤ n → ‖(∑ i, a i ^ n) + (∑ i, e i ^ n) - ∑ j, b j ^ n‖ ≤
      C * ((q ^ s) ^ (((k : ℝ) + 3) / 2)) ^ n)
    (hb : ∀ j, ‖b j‖ ≤ (q ^ s) ^ (((k : ℝ) + 3) / 2)) :
    ∀ i, ‖a i‖ ≤ (q ^ s) ^ (((k : ℝ) + 3) / 2) := by
  have : 0 ≤ (q ^ s) ^ (((k : ℝ) + 3) / 2) :=
    Real.rpow_nonneg (pow_nonneg (by linarith) _) _
  exact no_cancellation_signed3 a e b C _ this h hb

/-- The endgame with the field degree depending on `k`, for an unbounded set of `k`
(`α i` the Frobenius eigenvalues over `F_q`; over `F_{q^s}` the tensor power has eigenvalues
`∏ j, (α (I j))^s`). -/
theorem endgame_fibres_var {d : ℕ} (α : Fin d → ℂ) (q : ℝ) (hq : 1 < q)
    (H : ∀ K : ℕ, ∃ k : ℕ, K ≤ k ∧ ∃ s : ℕ, 1 ≤ s ∧ ∃ (E : Type) (B : Type)
      (_ : Fintype E) (_ : Fintype B) (e : E → ℂ) (b : B → ℂ) (C : ℝ),
      (∀ n : ℕ, 1 ≤ n →
        ‖(∑ I : Fin k → Fin d, (∏ j, α (I j) ^ s) ^ n) + (∑ i, e i ^ n) - ∑ j, b j ^ n‖ ≤
          C * (q ^ ((s : ℝ) * ((k : ℝ) + 3) / 2)) ^ n) ∧
      (∀ j, ‖b j‖ ≤ q ^ ((s : ℝ) * ((k : ℝ) + 3) / 2))) :
    ∀ i, ‖α i‖ ≤ Real.sqrt q := by
  intro i
  have hq0 : 0 ≤ q := by linarith
  refine le_of_pow_le_unbounded (norm_nonneg _) (Real.sqrt_nonneg _) fun K => ?_
  obtain ⟨k, hk, s, hs, E, B, _, _, e, b, C, hC, hb⟩ := H K
  refine ⟨k, hk, pow_root_step (norm_nonneg _) (Real.sqrt_nonneg _) hs ?_⟩
  have step := no_cancellation_signed3 (fun I : Fin k → Fin d => ∏ j, α (I j) ^ s) e b C
    (q ^ ((s : ℝ) * ((k : ℝ) + 3) / 2)) (Real.rpow_nonneg hq0 _) hC hb (fun _ => i)
  simp only [Finset.prod_const, Finset.card_univ, Fintype.card_fin, norm_pow] at step
  have e' : q ^ ((s : ℝ) * ((k : ℝ) + 3) / 2) = (Real.sqrt q) ^ (s * (k + 3)) := by
    rw [Real.sqrt_eq_rpow, ← Real.rpow_natCast, ← Real.rpow_mul hq0]
    congr 1; push_cast; ring
  rw [e'] at step
  rw [← pow_mul] at step
  exact step

#print axioms pow_root_step
#print axioms le_of_pow_le_unbounded
#print axioms endgame_unbounded
#print axioms dichotomy_field_dep
#print axioms endgame_fibres_var

end ToyWeil
