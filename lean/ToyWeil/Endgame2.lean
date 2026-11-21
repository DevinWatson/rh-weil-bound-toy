import ToyWeil.PowerSum

namespace ToyWeil

/-- G2 (three families): `a` and `e` enter with a plus sign, `b` with a minus sign;
if the `b` bases are at most `ρ` then so are the `a` bases. -/
theorem no_cancellation_signed3 {A E B : Type*} [Fintype A] [Fintype E] [Fintype B]
    (a : A → ℂ) (e : E → ℂ) (b : B → ℂ) (C ρ : ℝ) (hρ : 0 ≤ ρ)
    (h : ∀ n : ℕ, 1 ≤ n → ‖(∑ i, a i ^ n) + (∑ i, e i ^ n) - ∑ j, b j ^ n‖ ≤ C * ρ ^ n)
    (hb : ∀ j, ‖b j‖ ≤ ρ) :
    ∀ i, ‖a i‖ ≤ ρ := by
  classical
  intro i0
  let V : Finset ℂ := Finset.univ.image a ∪ Finset.univ.image e ∪ Finset.univ.image b
  have haV : ∀ i, a i ∈ V := fun i => by
    simp only [V, Finset.mem_union, Finset.mem_image, Finset.mem_univ, true_and]
    exact Or.inl (Or.inl ⟨i, rfl⟩)
  have heV : ∀ i, e i ∈ V := fun i => by
    simp only [V, Finset.mem_union, Finset.mem_image, Finset.mem_univ, true_and]
    exact Or.inl (Or.inr ⟨i, rfl⟩)
  have hbV : ∀ j, b j ∈ V := fun j => by
    simp only [V, Finset.mem_union, Finset.mem_image, Finset.mem_univ, true_and]
    exact Or.inr ⟨j, rfl⟩
  let coeff : ℂ → ℂ := fun v =>
    ((Finset.univ.filter (fun i => a i = v)).card : ℂ) +
    ((Finset.univ.filter (fun i => e i = v)).card : ℂ) -
    ((Finset.univ.filter (fun j => b j = v)).card : ℂ)
  let W : Finset ℂ := V.filter (fun v => coeff v ≠ 0)
  have key := no_hidden_growth' (fun v : W => v.1) Subtype.val_injective
    (fun v => coeff v.1) (fun v => (Finset.mem_filter.1 v.2).2) C ρ hρ (by
      intro n hn
      have h1 := h n hn
      rw [sum_pow_group a V haV n, sum_pow_group e V heV n, sum_pow_group b V hbV n,
        ← Finset.sum_add_distrib, ← Finset.sum_sub_distrib] at h1
      rw [Finset.sum_coe_sort W (fun v => coeff v * v ^ n)]
      have h2 : ∑ v ∈ W, coeff v * v ^ n = ∑ v ∈ V, coeff v * v ^ n :=
        Finset.sum_filter_of_ne (fun v _ hne => left_ne_zero_of_mul hne)
      rw [h2]
      convert h1 using 2
      apply Finset.sum_congr rfl
      intro v _
      simp only [coeff]; ring)
  by_cases hc : coeff (a i0) ≠ 0
  · simpa using key ⟨a i0, Finset.mem_filter.2 ⟨haV i0, hc⟩⟩
  · push_neg at hc
    have hApos : 0 < (Finset.univ.filter (fun i => a i = a i0)).card :=
      Finset.card_pos.2 ⟨i0, by simp⟩
    have hnat : (Finset.univ.filter (fun i => a i = a i0)).card +
        (Finset.univ.filter (fun i => e i = a i0)).card =
        (Finset.univ.filter (fun j => b j = a i0)).card := by
      have : (((Finset.univ.filter (fun i => a i = a i0)).card +
        (Finset.univ.filter (fun i => e i = a i0)).card : ℕ) : ℂ) =
        (((Finset.univ.filter (fun j => b j = a i0)).card : ℕ) : ℂ) := by
        push_cast
        simp only [coeff] at hc
        linear_combination hc
      exact_mod_cast this
    have hBpos : 0 < (Finset.univ.filter (fun j => b j = a i0)).card := by omega
    obtain ⟨j, hj⟩ := Finset.card_pos.1 hBpos
    have hj' : b j = a i0 := (Finset.mem_filter.1 hj).2
    rw [← hj']
    exact hb j

/-- G1 (signed no-cancellation, two families). -/
theorem no_cancellation_signed {A B : Type*} [Fintype A] [Fintype B]
    (a : A → ℂ) (b : B → ℂ) (C ρ : ℝ) (hρ : 0 ≤ ρ)
    (h : ∀ n : ℕ, 1 ≤ n → ‖(∑ i, a i ^ n) - ∑ j, b j ^ n‖ ≤ C * ρ ^ n)
    (hb : ∀ j, ‖b j‖ ≤ ρ) :
    ∀ i, ‖a i‖ ≤ ρ := by
  refine no_cancellation_signed3 a (Empty.elim : Empty → ℂ) b C ρ hρ ?_ hb
  intro n hn
  simpa using h n hn

/-- G3 (endgame from fibres). -/
theorem endgame_fibres {d : ℕ} (α : Fin d → ℂ) (q : ℝ) (hq : 1 < q)
    (H : ∀ k : ℕ, 2 ≤ k → ∃ (E : Type) (B : Type) (_ : Fintype E) (_ : Fintype B)
      (e : E → ℂ) (b : B → ℂ) (C : ℝ),
      (∀ n : ℕ, 1 ≤ n →
        ‖(∑ I : Fin k → Fin d, (∏ j, α (I j)) ^ n) + (∑ i, e i ^ n) - ∑ j, b j ^ n‖ ≤
          C * (q ^ (((k : ℝ) + 3) / 2)) ^ n) ∧
      (∀ j, ‖b j‖ ≤ q ^ (((k : ℝ) + 3) / 2))) :
    ∀ i, ‖α i‖ ≤ Real.sqrt q := by
  intro i
  have hq0 : 0 ≤ q := by linarith
  have hy : 0 ≤ Real.sqrt q := Real.sqrt_nonneg _
  apply le_of_pow_succ_le hy (norm_nonneg _) (K := (Real.sqrt q) ^ 4)
  intro N hN
  obtain ⟨E, B, _, _, e, b, C, hC, hb⟩ := H (N + 1) (by omega)
  have step := no_cancellation_signed3 (fun I : Fin (N + 1) → Fin d => ∏ j, α (I j)) e b C
    (q ^ (((((N + 1 : ℕ)) : ℝ) + 3) / 2)) (by positivity) hC hb (fun _ => i)
  simp only [Finset.prod_const, Finset.card_univ, Fintype.card_fin, norm_pow] at step
  have e' : q ^ (((((N + 1 : ℕ)) : ℝ) + 3) / 2) = (Real.sqrt q) ^ (N + 1 + 3) := by
    rw [Real.sqrt_eq_rpow, ← Real.rpow_natCast, ← Real.rpow_mul hq0]
    congr 1; push_cast; ring
  rw [e'] at step
  calc ‖α i‖ ^ (N + 1) ≤ (Real.sqrt q) ^ (N + 1 + 3) := step
    _ = (Real.sqrt q) ^ 4 * (Real.sqrt q) ^ N := by rw [← pow_add]; congr 1; omega

#print axioms no_cancellation_signed3
#print axioms no_cancellation_signed
#print axioms endgame_fibres

end ToyWeil
