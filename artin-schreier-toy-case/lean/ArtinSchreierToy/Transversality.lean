import ArtinSchreierToy.WeightedParseval
import Mathlib.Data.Fin.VecNotation

/-!
# Algebraic Transversality Theorems for the Artin–Schreier Path-Quadric Toy Case

Machine-checked algebraic core of the transversality analysis between the projective
path quadric `Q_c(X) = ∑_{i=0}^{k-2} c_i X_i X_{i+1} = 0` and the Fermat hypersurface
`F_d(X) = ∑_{i=0}^{k-1} X_i^d = 0` in `P^{k-1}` over any field `F`:

1. `sum_mul_pathGrad` & `alternating_sum_mul_pathGrad`: Euler identity
   `∑ X_i (∇Q_c)_i = 2 Q_c(X)` and alternating cancellation
   `∑ (-1)^i X_i (∇Q_c)_i = 0` for all `k`, `c`, `X`.
2. `base_locus_transversal` & `base_locus_no_tangency`: for every even `k = 2(m+1)` and
   every `c` with `c_i ≠ 0`, at every nonzero point `X` of the base locus
   `{X_i X_{i+1} = 0}`, the gradients `∇Q_c(X)` and `∇F_d(X)` are linearly independent.
3. `k4_bad_lines` & `k4_bad_plane`: exact characterization of the `k = 4` bad locus
   `B_{4,d}` as the `d^2` lines `c_0 + ζ_1 c_1 + ζ_1 ζ_2 c_2 = 0` (`ζ_1^d = ζ_2^d = -1`).
4. `euler_char_identity`: exact algebraic identity for the closed-form Betti number
   `dim H^{k-1}_c(Y, K) = 2 ∑_{j=1}^{k-1} (d - 1)^j + 1`.
-/

open Finset

namespace ArtinSchreierToy

section GradientIdentities

variable {F : Type*} [Field F]

/-- The `i`-th partial derivative `∂Q_c / ∂X_i` of the weighted path quadric
`Q_c(X) = ∑_{j=0}^{n-1} c_j X_j X_{j+1}`. -/
def pathGrad {n : ℕ} (c : Fin n → F) (X : Fin (n + 1) → F) (i : Fin (n + 1)) : F :=
  (if h : 0 < i.val then c ⟨i.val - 1, by omega⟩ * X ⟨i.val - 1, by omega⟩ else 0) +
  (if h : i.val < n then c ⟨i.val, h⟩ * X ⟨i.val + 1, by omega⟩ else 0)

/-- Split the sum over `Fin (n + 1)` of the left-neighbor term of `pathGrad`. -/
private lemma sum_left_neighbor {n : ℕ} (w : Fin (n + 1) → F) (c : Fin n → F)
    (X : Fin (n + 1) → F) :
    ∑ i : Fin (n + 1), w i *
      (if h : 0 < i.val then c ⟨i.val - 1, by omega⟩ * X ⟨i.val - 1, by omega⟩ else 0)
    = ∑ j : Fin n, w j.succ * (c j * X j.castSucc) := by
  rw [Fin.sum_univ_succ]
  simp only [Fin.val_zero, lt_self_iff_false, ↓reduceDIte, mul_zero, zero_add]
  refine Finset.sum_congr rfl fun j _ => ?_
  split_ifs with h
  · rfl
  · exact absurd (Nat.succ_pos j.val) h

/-- Split the sum over `Fin (n + 1)` of the right-neighbor term of `pathGrad`. -/
private lemma sum_right_neighbor {n : ℕ} (w : Fin (n + 1) → F) (c : Fin n → F)
    (X : Fin (n + 1) → F) :
    ∑ i : Fin (n + 1), w i *
      (if h : i.val < n then c ⟨i.val, h⟩ * X ⟨i.val + 1, by omega⟩ else 0)
    = ∑ j : Fin n, w j.castSucc * (c j * X j.succ) := by
  rw [Fin.sum_univ_castSucc]
  simp only [Fin.val_last, lt_self_iff_false, ↓reduceDIte, mul_zero, add_zero]
  refine Finset.sum_congr rfl fun j _ => ?_
  split_ifs with h
  · rfl
  · exact absurd j.isLt h

/-- Euler identity: `∑_i X_i * (∂Q_c / ∂X_i) = 2 * Q_c(X)`. -/
theorem sum_mul_pathGrad {n : ℕ} (c : Fin n → F) (X : Fin (n + 1) → F) :
    ∑ i : Fin (n + 1), X i * pathGrad c X i = 2 * weightedPathQuadric c X := by
  simp only [pathGrad, mul_add, Finset.sum_add_distrib]
  rw [sum_left_neighbor X c X, sum_right_neighbor X c X, ← Finset.sum_add_distrib]
  unfold weightedPathQuadric
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl fun j _ => by ring

/-- Alternating cancellation identity: `∑_i (-1)^i * X_i * (∂Q_c / ∂X_i) = 0`. -/
theorem alternating_sum_mul_pathGrad {n : ℕ} (c : Fin n → F) (X : Fin (n + 1) → F) :
    ∑ i : Fin (n + 1), (-1 : F) ^ i.val * (X i * pathGrad c X i) = 0 := by
  have hrew : ∀ i : Fin (n + 1),
      (-1 : F) ^ i.val * (X i * pathGrad c X i)
        = ((-1 : F) ^ i.val * X i) * pathGrad c X i := fun _ => by ring
  simp_rw [hrew, pathGrad, mul_add, Finset.sum_add_distrib]
  rw [sum_left_neighbor (fun i => (-1 : F) ^ i.val * X i) c X,
      sum_right_neighbor (fun i => (-1 : F) ^ i.val * X i) c X,
      ← Finset.sum_add_distrib]
  refine Finset.sum_eq_zero fun j _ => ?_
  simp only [Fin.val_succ, Fin.val_castSucc, pow_succ]
  ring

/-- Consequences of tangency `∇Q_c(X) = λ • (X_i^{d-1})`:
both `2 Q_c(X) = λ ∑ X_i^d` and `λ ∑ (-1)^i X_i^d = 0`. -/
theorem tangency_identities {n d : ℕ} (hd : 1 ≤ d) (c : Fin n → F)
    (X : Fin (n + 1) → F) (lam : F)
    (htan : ∀ i : Fin (n + 1), pathGrad c X i = lam * X i ^ (d - 1)) :
    2 * weightedPathQuadric c X = lam * ∑ i : Fin (n + 1), X i ^ d ∧
    lam * ∑ i : Fin (n + 1), (-1 : F) ^ i.val * X i ^ d = 0 := by
  have hpow : ∀ i : Fin (n + 1), X i * (lam * X i ^ (d - 1)) = lam * X i ^ d := by
    intro i
    calc X i * (lam * X i ^ (d - 1)) = lam * (X i ^ 1 * X i ^ (d - 1)) := by ring
      _ = lam * X i ^ (1 + (d - 1)) := by rw [← pow_add]
      _ = lam * X i ^ d := by congr 2; omega
  constructor
  · rw [← sum_mul_pathGrad]
    simp_rw [htan, hpow, ← Finset.mul_sum]
  · have h0 := alternating_sum_mul_pathGrad c X
    simp_rw [htan, hpow] at h0
    have h1 : ∑ i : Fin (n + 1), (-1 : F) ^ i.val * (lam * X i ^ d)
        = lam * ∑ i : Fin (n + 1), (-1 : F) ^ i.val * X i ^ d := by
      rw [Finset.mul_sum]
      refine Finset.sum_congr rfl fun i _ => by ring
    rwa [← h1]

end GradientIdentities

section BaseLocusTransversality

variable {F : Type*} [Field F]

/-- On the base locus `{X_i X_{i+1} = 0}` of the path quadric for any even `k = 2 * (m + 1)`
and any nonzero weights `c_i ≠ 0`, every nonzero point `X` has a coordinate `j` where
`X j = 0` and `(∇Q_c(X))_j ≠ 0`. -/
theorem base_locus_transversal {m : ℕ} (c : Fin (2 * m + 1) → F) (hc : ∀ i, c i ≠ 0)
    (X : Fin (2 * m + 2) → F)
    (hbase : ∀ i : Fin (2 * m + 1), X i.castSucc * X i.succ = 0)
    (hX : ∃ i : Fin (2 * m + 2), X i ≠ 0) :
    ∃ j : Fin (2 * m + 2), X j = 0 ∧ pathGrad c X j ≠ 0 := by
  by_contra hall
  push Not at hall
  -- hall : ∀ j, X j = 0 → pathGrad c X j = 0
  by_cases h0 : X ⟨0, by omega⟩ = 0
  · -- If X_0 = 0, strong induction forces all X_i = 0, contradicting hX.
    have hall0 : ∀ t : ℕ, (ht : t < 2 * m + 2) → X ⟨t, ht⟩ = 0 := by
      intro t
      induction t using Nat.strongRecOn with
      | ind t ih =>
          intro ht
          cases t with
          | zero => exact h0
          | succ s =>
              have hprev : X ⟨s, by omega⟩ = 0 := ih s (by omega) (by omega)
              have hg : pathGrad c X ⟨s, by omega⟩ = 0 := hall ⟨s, by omega⟩ hprev
              unfold pathGrad at hg
              have hlt : s < 2 * m + 1 := by omega
              simp only [hlt, ↓reduceDIte] at hg
              have hleft :
                  (if h : 0 < s then c ⟨s - 1, by omega⟩ * X ⟨s - 1, by omega⟩ else 0) = 0 := by
                split_ifs with hp
                · have hp0 : X ⟨s - 1, by omega⟩ = 0 := ih (s - 1) (by omega) (by omega)
                  rw [hp0, mul_zero]
                · rfl
              rw [hleft, zero_add] at hg
              rcases mul_eq_zero.mp hg with hc0 | hx0
              · exact absurd hc0 (hc ⟨s, hlt⟩)
              · exact hx0
    obtain ⟨i, hi⟩ := hX
    exact hi (hall0 i.val i.isLt)
  · -- If X_0 ≠ 0, induction on r ≤ m shows X_{2r} ≠ 0 and X_{2r+1} = 0.
    have hpair : ∀ r : ℕ, (hr : r ≤ m) →
        X ⟨2 * r, by omega⟩ ≠ 0 ∧ X ⟨2 * r + 1, by omega⟩ = 0 := by
      intro r
      induction r with
      | zero =>
          intro _
          refine ⟨h0, ?_⟩
          have hb := hbase ⟨0, by omega⟩
          rcases mul_eq_zero.mp hb with h_0 | h_1
          · exact absurd h_0 h0
          · exact h_1
      | succ r ih =>
          intro hr
          obtain ⟨h2r, h2r1⟩ := ih (by omega)
          have hg := hall ⟨2 * r + 1, by omega⟩ h2r1
          unfold pathGrad at hg
          have hpos : 0 < 2 * r + 1 := by omega
          have hlt : 2 * r + 1 < 2 * m + 1 := by omega
          simp only [hpos, hlt, ↓reduceDIte] at hg
          have h2r2 : X ⟨2 * (r + 1), by omega⟩ ≠ 0 := by
            intro hzero
            have hz' : X ⟨2 * r + 1 + 1, by omega⟩ = 0 := by
              convert hzero using 2
            rw [hz', mul_zero, add_zero] at hg
            rcases mul_eq_zero.mp hg with hc0 | hx0
            · exact absurd hc0 (hc ⟨2 * r + 1 - 1, by omega⟩)
            · exact h2r (by convert hx0 using 2; exact Fin.ext (by dsimp))
          refine ⟨h2r2, ?_⟩
          have hb := hbase ⟨2 * (r + 1), by omega⟩
          rcases mul_eq_zero.mp hb with h_a | h_b
          · exact absurd h_a h2r2
          · convert h_b using 2; exact Fin.ext (by simp)
    -- At r = m, the last coordinate j = 2m + 1 has X_j = 0 yet pathGrad = c_{2m} X_{2m} ≠ 0!
    obtain ⟨h2m, h2m1⟩ := hpair m le_rfl
    have hg := hall ⟨2 * m + 1, by omega⟩ h2m1
    unfold pathGrad at hg
    have hpos : 0 < 2 * m + 1 := by omega
    have hnlt : ¬ (2 * m + 1 < 2 * m + 1) := lt_irrefl _
    simp only [hpos, hnlt, ↓reduceDIte, add_zero] at hg
    rcases mul_eq_zero.mp hg with hc0 | hx0
    · exact absurd hc0 (hc ⟨2 * m + 1 - 1, by omega⟩)
    · exact h2m (by convert hx0 using 2; exact Fin.ext (by dsimp))

/-- Immediate corollary: for every even `k = 2(m+1)`, every `d ≥ 2`, and every nonzero `c`,
`{Q_c = 0}` is never tangent to `{∑ X_i^d = 0}` at any point of the base locus `B`. -/
theorem base_locus_no_tangency {m d : ℕ} (hd : 2 ≤ d)
    (c : Fin (2 * m + 1) → F) (hc : ∀ i, c i ≠ 0)
    (X : Fin (2 * m + 2) → F)
    (hbase : ∀ i : Fin (2 * m + 1), X i.castSucc * X i.succ = 0)
    (hX : ∃ i : Fin (2 * m + 2), X i ≠ 0)
    (lam : F) :
    ¬ (∀ i : Fin (2 * m + 2), pathGrad c X i = lam * X i ^ (d - 1)) := by
  intro htan
  obtain ⟨j, hXj, hgj⟩ := base_locus_transversal c hc X hbase hX
  have hj := htan j
  rw [hXj, zero_pow (by omega : d - 1 ≠ 0), mul_zero] at hj
  exact hgj hj

end BaseLocusTransversality

section CaseK4

variable {F : Type*} [Field F]

/-- Exact characterization of the `k = 4` bad locus `B_{4, d}`:
if `2 ≠ 0` in `F`, `d ≥ 2`, `c_0, c_1, c_2 ≠ 0`, `X ≠ 0`, `∑ X_i^d = 0`, and
`∇Q_c(X) = (X_i^{d-1})`, then all four coordinates `X_i` are nonzero, the ratios
`ζ_1 = X_2 / X_0` and `ζ_2 = X_3 / X_1` satisfy `ζ_1^d = -1` and `ζ_2^d = -1`, and `c`
lies on the line `c_0 + ζ_1 c_1 + ζ_1 ζ_2 c_2 = 0`. -/
theorem k4_bad_lines {d : ℕ} (hd : 2 ≤ d) (h2 : (2 : F) ≠ 0)
    (c : Fin 3 → F) (hc : ∀ i, c i ≠ 0)
    (X : Fin 4 → F) (hX : ∃ i : Fin 4, X i ≠ 0)
    (hF : ∑ i : Fin 4, X i ^ d = 0)
    (htan : ∀ i : Fin 4, pathGrad c X i = X i ^ (d - 1)) :
    (X 0 ≠ 0 ∧ X 1 ≠ 0 ∧ X 2 ≠ 0 ∧ X 3 ≠ 0) ∧
    (X 2 / X 0) ^ d = -1 ∧ (X 3 / X 1) ^ d = -1 ∧
    c 0 + (X 2 / X 0) * c 1 + (X 2 / X 0) * (X 3 / X 1) * c 2 = 0 := by
  have hd0 : d - 1 ≠ 0 := by omega
  have heq0 : c 0 * X 1 = X 0 ^ (d - 1) := by simpa [pathGrad] using htan 0
  have heq1 : c 0 * X 0 + c 1 * X 2 = X 1 ^ (d - 1) := by simpa [pathGrad] using htan 1
  have heq2 : c 1 * X 1 + c 2 * X 3 = X 2 ^ (d - 1) := by simpa [pathGrad] using htan 2
  have heq3 : c 2 * X 2 = X 3 ^ (d - 1) := by simpa [pathGrad] using htan 3
  have hc0 : c 0 ≠ 0 := hc 0
  have hc1 : c 1 ≠ 0 := hc 1
  have hc2 : c 2 ≠ 0 := hc 2
  have hX0 : X 0 ≠ 0 := by
    intro hx0
    rw [hx0, zero_pow hd0] at heq0
    have hx1 : X 1 = 0 := (mul_eq_zero.mp heq0).resolve_left hc0
    rw [hx0, hx1, mul_zero, zero_add, zero_pow hd0] at heq1
    have hx2 : X 2 = 0 := (mul_eq_zero.mp heq1).resolve_left hc1
    rw [hx1, hx2, mul_zero, zero_add, zero_pow hd0] at heq2
    have hx3 : X 3 = 0 := (mul_eq_zero.mp heq2).resolve_left hc2
    obtain ⟨i, hi⟩ := hX
    fin_cases i <;> contradiction
  have hX1 : X 1 ≠ 0 := by
    intro hx1
    rw [hx1, mul_zero] at heq0
    exact pow_ne_zero (d - 1) hX0 heq0.symm
  have hX3 : X 3 ≠ 0 := by
    intro hx3
    rw [hx3, zero_pow hd0] at heq3
    have hx2 : X 2 = 0 := (mul_eq_zero.mp heq3).resolve_left hc2
    rw [hx2, hx3, mul_zero, add_zero, zero_pow hd0] at heq2
    have hx1 : X 1 = 0 := (mul_eq_zero.mp heq2).resolve_left hc1
    exact hX1 hx1
  have hX2 : X 2 ≠ 0 := by
    intro hx2
    rw [hx2, mul_zero] at heq3
    exact pow_ne_zero (d - 1) hX3 heq3.symm
  -- Apply tangency_identities with lam = 1
  have ⟨hQ2, halt⟩ := tangency_identities (by omega : 1 ≤ d) c X 1 (fun i => by simpa using htan i)
  rw [one_mul, hF] at hQ2
  have hQ0 : weightedPathQuadric c X = 0 := (mul_eq_zero.mp hQ2).resolve_left h2
  rw [one_mul] at halt
  -- Expand F_d = 0 and alternating sum = 0 on Fin 4
  rw [Fin.sum_univ_four] at hF halt
  simp only [Fin.val_zero, Fin.val_one, Fin.val_two, pow_zero, pow_one, one_mul] at halt
  have h3val : (3 : Fin 4).val = 3 := rfl
  rw [h3val] at halt
  have hodd : X 0 ^ d + X 2 ^ d = 0 := by
    have hsum : 2 * (X 0 ^ d + X 2 ^ d) = 0 := by
      have hm1_2 : (-1 : F) ^ (2 : ℕ) = 1 := by norm_num
      have hm1_3 : (-1 : F) ^ (3 : ℕ) = -1 := by norm_num
      rw [hm1_2, hm1_3] at halt
      linear_combination hF + halt
    exact (mul_eq_zero.mp hsum).resolve_left h2
  have heven : X 1 ^ d + X 3 ^ d = 0 := by
    linear_combination hF - hodd
  have hζ1 : (X 2 / X 0) ^ d = -1 := by
    rw [div_pow, div_eq_iff (pow_ne_zero d hX0)]
    linear_combination hodd
  have hζ2 : (X 3 / X 1) ^ d = -1 := by
    rw [div_pow, div_eq_iff (pow_ne_zero d hX1)]
    linear_combination heven
  have hline : c 0 + (X 2 / X 0) * c 1 + (X 2 / X 0) * (X 3 / X 1) * c 2 = 0 := by
    unfold weightedPathQuadric at hQ0
    rw [Fin.sum_univ_three] at hQ0
    have hQexp : c 0 * X 0 * X 1 + c 1 * X 1 * X 2 + c 2 * X 2 * X 3 = 0 := hQ0
    have hprod : (X 0 * X 1) * (c 0 + (X 2 / X 0) * c 1 + (X 2 / X 0) * (X 3 / X 1) * c 2) = 0 := by
      field_simp [hX0, hX1]
      linear_combination hQexp
    exact (mul_eq_zero.mp hprod).resolve_left (mul_ne_zero hX0 hX1)
  exact ⟨⟨hX0, hX1, hX2, hX3⟩, hζ1, hζ2, hline⟩

/-- Converse plane construction at `k = 4`: whenever `c_0 + ζ_1 c_1 + ζ_1 ζ_2 c_2 = 0` with
`ζ_1^d = ζ_2^d = -1`, the 2-plane `(u, v, ζ_1 u, ζ_2 v)` lies in `{Q_c = 0} ∩ {∑ X_i^d = 0}`. -/
theorem k4_bad_plane {d : ℕ} (c : Fin 3 → F) (ζ₁ ζ₂ : F)
    (h1 : ζ₁ ^ d = -1) (h2 : ζ₂ ^ d = -1)
    (hline : c 0 + ζ₁ * c 1 + ζ₁ * ζ₂ * c 2 = 0) (u v : F) :
    let X : Fin 4 → F := ![u, v, ζ₁ * u, ζ₂ * v]
    weightedPathQuadric c X = 0 ∧ ∑ i : Fin 4, X i ^ d = 0 := by
  dsimp only
  constructor
  · unfold weightedPathQuadric
    rw [Fin.sum_univ_three]
    simp only [Fin.castSucc_zero, Fin.succ_zero_eq_one, Fin.castSucc_one,
      Matrix.cons_val_zero, Matrix.cons_val_one]
    calc c 0 * u * v + c 1 * v * (ζ₁ * u) + c 2 * (ζ₁ * u) * (ζ₂ * v)
        = (u * v) * (c 0 + ζ₁ * c 1 + ζ₁ * ζ₂ * c 2) := by ring
      _ = 0 := by rw [hline, mul_zero]
  · rw [Fin.sum_univ_four]
    simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val, mul_pow, h1, h2]
    ring

end CaseK4

section BettiFormula

/-- Exact algebraic identity behind the closed-form Betti number
`dim H^{k-1}_c(Y, K) = 2 ∑_{j=1}^{k-1} (d - 1)^j + 1 = (2 (d - 1)^k - d) / (d - 2)`. -/
theorem euler_char_identity (d k : ℕ) (hk : 1 ≤ k) :
    ((d : ℤ) - 2) * (2 * ∑ j ∈ Finset.Ico 1 k, ((d : ℤ) - 1) ^ j + 1)
      = 2 * ((d : ℤ) - 1) ^ k - (d : ℤ) := by
  obtain ⟨m, rfl⟩ : ∃ m, k = m + 1 := ⟨k - 1, by omega⟩
  clear hk
  induction m with
  | zero =>
      simp; ring
  | succ m ih =>
      rw [Finset.sum_Ico_succ_top (by omega : 1 ≤ m + 1)]
      have hsplit : ((d : ℤ) - 2) *
          (2 * ((∑ j ∈ Finset.Ico 1 (m + 1), ((d : ℤ) - 1) ^ j) + ((d : ℤ) - 1) ^ (m + 1)) + 1)
        = ((d : ℤ) - 2) * (2 * ∑ j ∈ Finset.Ico 1 (m + 1), ((d : ℤ) - 1) ^ j + 1) +
          2 * ((d : ℤ) - 2) * ((d : ℤ) - 1) ^ (m + 1) := by ring
      rw [hsplit, ih]
      rw [pow_succ]
      ring

end BettiFormula

end ArtinSchreierToy

open ArtinSchreierToy in #print axioms sum_mul_pathGrad
open ArtinSchreierToy in #print axioms alternating_sum_mul_pathGrad
open ArtinSchreierToy in #print axioms tangency_identities
open ArtinSchreierToy in #print axioms base_locus_transversal
open ArtinSchreierToy in #print axioms base_locus_no_tangency
open ArtinSchreierToy in #print axioms k4_bad_lines
open ArtinSchreierToy in #print axioms k4_bad_plane
open ArtinSchreierToy in #print axioms euler_char_identity
