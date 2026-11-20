# F: Lean formalisation of the elementary core (Parseval route)

File: toy-case/lean/ToyWeil/Parseval.lean. Compiled with lean_check.sh ToyWeil.Parseval: exit 0, no errors, no sorry, no axiom, no native_decide (grep-checked). Log: toy-case/lean/logs/ToyWeil.Parseval.log. Only linter warnings (unused section variable, deprecated push_neg).

Setting: F is any finite field (`[Field F] [Fintype F] [DecidableEq F]`), `psi : AddChar F ℂ` nontrivial, hypothesis `hψ : psi ≠ 0` (AddChar zero is the trivial character). All targets P1-P4 reached; nothing left out.

## Statements (copied from the file)  -- all CHECKED by the Lean kernel (PROVED in Lean)
P1:
theorem orthogonality (hψ : psi ≠ 0) {X : Type*} [Fintype X] (g : X → ℂ) (Qf : X → F) :
    ∑ h : F, ∑ x : X, g x * psi (h * Qf x)
      = (Fintype.card F : ℂ) * ∑ x ∈ Finset.univ.filter (fun x => Qf x = 0), g x
(with lemma sum_psi_mul: ∑ h, psi (h*a) = if a = 0 then card F else 0)

P2:
theorem parseval_step (hψ : psi ≠ 0) (u : F → ℂ) {h : F} (hh : h ≠ 0) :
    ∑ y : F, ‖∑ x, u x * psi (h * x * y)‖ ^ 2 = (Fintype.card F : ℝ) * ∑ x, ‖u x‖ ^ 2

P3: definitions
def gseq (t : F → ℂ) (h : F) : ℕ → F → ℂ   -- gseq 1 = t, gseq (j+2) y = t y * ∑ x, gseq (j+1) x * psi (h*x*y); index 0 is a dummy (= t)
def Ssum (t) (h) (k : ℕ) : ℂ := ∑ y, gseq psi t h k y
theorem iterated_bound (hψ) (t) {h} (hh : h ≠ 0) (B : ℝ) (hB : ∀ x, ‖t x‖ ≤ B) (n : ℕ) :
    ‖Ssum psi t h (n + 2)‖ ≤ Real.sqrt (Fintype.card F) ^ (n + 1) * B ^ n * ∑ x, ‖t x‖ ^ 2
theorem iterated_bound_rpow (hψ) (t) {h} (hh : h ≠ 0) (B : ℝ) (hB) (k : ℕ) (hk : 2 ≤ k) :
    ‖Ssum psi t h k‖ ≤ (Fintype.card F : ℝ) ^ (((k : ℝ) - 1) / 2) * B ^ (k - 2) * ∑ x, ‖t x‖ ^ 2
Also gseq_sq_bound: ∑ y ‖gseq (j+1) y‖² ≤ (B² q)^j ∑‖t x‖² (the iterated Parseval step).
Proof shape: Cauchy-Schwarz on S k = ∑ t y * V y, then Parseval once on V, then the induction above.

P4 (general k = n+1, not only k = 2,3,4):
def pathQuadric {k} (x : Fin (k+1) → F) : F := ∑ i : Fin k, x i.castSucc * x i.succ
theorem Ssum_eq_path_sum (hψ) (t) (h : F) (n : ℕ) :
    Ssum psi t h (n + 1) = ∑ x : Fin (n + 1) → F, (∏ i, t (x i)) * psi (h * pathQuadric x)
(h arbitrary here, including 0.) Supporting: pathQuadric_snoc, gseq_path.

## #print axioms (from the log)
sum_psi_mul, orthogonality, parseval_step, iterated_bound, iterated_bound_rpow, pathQuadric_snoc, gseq_path, Ssum_eq_path_sum: each "depends on axioms: [propext, Classical.choice, Quot.sound]".

## What this does and does not say
- PROVED (Lean): the orthogonality identity, one Parseval step, the bound |S_k| <= q^((k-1)/2) B^(k-2) ||t||_2^2 for every h != 0 and k >= 2, and the identification of S_k with the path-quadric sum. Together with P1 (summing over h of the path-quadric sum gives q * sum over the quadric's zeros of prod t, the h=0 term being M^k) this is the elementary part of footnote 3: R, the sum over h != 0, is bounded by q^((k-1)/2) * B^(k-2) * ||t||^2 times (q-1) terms... that last multiplication by q-1 is not formalised.
- NOT covered here: the sign/cohomology claim (middle cohomology, Bertini, Katz), the passage to extension fields, and the "k -> infinity" step. Those remain OPEN/CITED in the other reports. Nothing here concerns RH over the integers.
- Observation (HINT, not formalised): with B = O(1) and ||t||^2 = q the bound is q^((k+1)/2), the trivial size of S_k is q^k.. so the bound is nontrivial only against M^k-type main terms; assessing that is for the other reports.
