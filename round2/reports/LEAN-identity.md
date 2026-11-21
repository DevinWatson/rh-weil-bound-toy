# LEAN-identity: the unconditional inequality in Lean 4

Setting: character sums over a finite field F (Weil 1948 is the bound the toy case aims at). Nothing here concerns the Riemann Hypothesis for the integers. No weights, purity or Weil bound are used.

File: ./lean/ToyWeil/Identity.lean (imports ToyWeil.Parseval, unedited).
Log: ./lean/logs/ToyWeil.Identity.log

CHECKED (Lean 4.34.1 + Mathlib, lean_check.sh, exit=0, no errors, no sorry, no native_decide). Targets I1-I4 all reached.

Definitions (copied):
    noncomputable def Ncount (t : F → ℂ) (n : ℕ) : ℂ :=
      ∑ x ∈ Finset.univ.filter (fun x : Fin (n + 1) → F => pathQuadric x = 0), ∏ i, t (x i)
    noncomputable def Rsum (t : F → ℂ) (n : ℕ) : ℂ :=
      ∑ h ∈ (Finset.univ : Finset F).erase 0, Ssum psi t h (n + 1)

Final statements (all with `psi : AddChar F ℂ`, `hψ : psi ≠ 0`, k = n + 1, q = Fintype.card F):

I1. theorem Ssum_zero : Ssum psi t 0 (n + 1) = (∑ x, t x) ^ (n + 1)

I2. theorem identity : (Fintype.card F : ℂ) * Ncount t n = (∑ x, t x) ^ (n + 1) + Rsum psi t n

I3. theorem identity_bound (B) (hB : ∀ x, ‖t x‖ ≤ B) (n) (hn : 1 ≤ n) :
      ‖(Fintype.card F : ℂ) * Ncount t n - (∑ x, t x) ^ (n + 1)‖
        ≤ ((Fintype.card F : ℝ) - 1) * ((Fintype.card F : ℝ) ^ ((n : ℝ) / 2) * B ^ (n - 1) * ∑ x, ‖t x‖ ^ 2)

    theorem identity_bound_closed (same hypotheses) :
      ‖(Fintype.card F : ℂ) * Ncount t n - (∑ x, t x) ^ (n + 1)‖
        ≤ ((Fintype.card F : ℝ) - 1) * ((Fintype.card F : ℝ) ^ ((n : ℝ) / 2 + 1) * B ^ (n + 1))

I4. theorem identity_bound_one (hB : ∀ x, ‖t x‖ ≤ 1) (n) (hn : 1 ≤ n) :
      ‖(Fintype.card F : ℂ) * Ncount t n - (∑ x, t x) ^ (n + 1)‖
        ≤ ((Fintype.card F : ℝ) - 1) * (Fintype.card F : ℝ) * Real.sqrt (Fintype.card F) ^ n
    (that is (q-1) q sqrt(q)^(k-1))

    theorem identity_bound_weak (hB : ∀ x, ‖t x‖ ≤ 1) (n) (hn : 1 ≤ n) :
      ‖(Fintype.card F : ℂ) * Ncount t n - (∑ x, t x) ^ (n + 1)‖
        ≤ (Fintype.card F : ℝ) ^ ((((n + 1 : ℕ) : ℝ) + 3) / 2)
    (that is q^((k+3)/2))

#print axioms lines copied from the log:
    'ToyWeil.Ssum_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ToyWeil.identity' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ToyWeil.identity_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ToyWeil.identity_bound_closed' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ToyWeil.identity_bound_one' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ToyWeil.identity_bound_weak' depends on axioms: [propext, Classical.choice, Quot.sound]

Proof route (PROVED, in the file): I1 from `Ssum_eq_path_sum` and `Fintype.sum_pow` (psi(0)=1); I2 from `orthogonality` with g = ∏ t(x i), Qf = pathQuadric, then splitting off h = 0; I3 from `iterated_bound_rpow` (k = n+1 >= 2) applied to each of the q-1 nonzero h, using sum ‖t‖² ≤ q B² for the closed form; I4 by B = 1 and q-1 ≤ q-type arithmetic (the weak form uses (q-1) q^(n/2+1) ≤ q^(n/2+2)).

Targets not reached: none. The strict bound ‖R‖ < q^((k+3)/2) of round one is replaced here by ≤ (weak inequality); the strict version was not attempted.
