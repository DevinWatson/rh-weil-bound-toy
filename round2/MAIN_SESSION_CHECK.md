# Main session check of round two (Claude Fable 5.2, 2026-11-20 19:55 UTC)

`ROUND2.md` was written by the synthesis agent from nine reports. Workflow `wf_626e889b-06a`: ten agents on
`claude-sonnet-5-5` at medium effort, 86 minutes, 2.22 million subagent tokens, no failures. This file says what
I checked myself. Everything is about character sums over finite fields, where the bound is Weil's theorem. It
says nothing about the Riemann Hypothesis for the integers.

## Checked by me

| Item | How | Result |
|---|---|---|
| `lean/ToyWeil/Identity.lean` | Recompiled with `tools/lean_check.sh`; text search for `sorry`, `axiom`, `native_decide` | Exit 0. Six theorems, each `[propext, Classical.choice, Quot.sound]`. The unconditional inequality `‖q N − M^k‖ ≤ (q−1) q √q^(k−1)` is now a Lean theorem for the path quadric. |
| The k = 4 theorem (report K4T, Theorem D), case of f with no multiplicative symmetry | Read the proof step by step and redid each step | I could follow all of it and found no gap. Steps: (1) the quadric is a family of planes over the projective line, which gives H^5 = H^6 = 0 and H^4 = (a plane term) + (coinvariants of V ⊗ τ*V); (2) V is tame everywhere, by computing the Euler characteristic of the total space two ways; (3) a map between tame sheaves on the line with disjoint finite singular sets factors through constant quotients, because the affine line has no tame covers; (4) V has no constant quotient, by restricting classes to the diagonal and using the duality pairing. None of the four uses weights. |
| New bad set predicted by the theory | Own code, exact integers (`compute/main-session-check/round2_check_out.txt`) | For f = x^3 − a with cube roots of unity in F_p, the theory predicts two planes in the plain all-ones quadric and one when the coefficients sum to zero. I get N_4/p^2 between 1.5 and 2.0 for (1,1,1), between 0.8 and 1.1 for (1,1,−2), and near 0 for (1,2,3), at eight primes up to 97. |
| No failure on the remaining exceptional lines | Same script | For f = (x−1)(x−2)(x−4) and coefficients on three of the lines where the theorem does not apply, N_4/p^2 stays within 0.19 of zero at five primes, the same as for generic coefficients, against 0.85 to 0.95 when the coefficients sum to zero. |

## Not checked by me

- The cited theorems (Künneth, the Euler characteristic formula, duality on curves, the fundamental group
  statements). Report LIT opened some of them; I opened none.
- The cases of Theorem D where f has a multiplicative symmetry (the character count), and the referee's large
  tables at p = 509 and 1009.
- Report GEN's reduction for general k and report FS's analysis at infinity.

## What round two establishes, in my reading

1. **k = 4 is settled for generic coefficients, without weights.** For f squarefree of odd degree, f(0) ≠ 0, not of
   the form x^d − a, and coefficients off at most (d^2 − d + 2)^2 − 1 explicit lines, the cohomology of the quadric
   is concentrated in degree 3. With round one this gives |α| ≤ q^(7/8) for every Frobenius eigenvalue of
   y^2 = f(x), by a route that uses no weights. That is far weaker than Weil's bound; its interest is that the
   route works at all.
2. **The sign statement is false on an explicit set and that set is now understood**: planes
   {x_4 = ρ x_2, x_1 = ρ' x_3} with ρ, ρ' multiplicative symmetries of the roots and c_2 + c_3 ρ + c_1 ρ' = 0.
3. **My reduction of round one was mostly right and partly wrong** (report RED): the cohomology of the quadric lives
   in degrees k−1, k, k+1 only, and only degree k has the wrong sign; but my description of that group left out a
   differential and a second term, and needs the extra input that the fibre over h has cohomology in one degree
   for all but finitely many h.

## A lead, not a result

Report GEN observes that the sign statement may not be needed at all. Call (P_k) the statement that for all but
finitely many h the k-variable sum with phase h·Q has cohomology in degree k only. Then:

- any wrong-sign class of the quadric is q times an eigenvalue on a constant quotient of the family over h;
- such an eigenvalue occurs in every fibre, and in a fibre with cohomology in one degree the Parseval bound
  controls every eigenvalue;
- so a class that cancels α^k satisfies the same bound that non-cancellation would have given, and
  |α| ≤ q^(1/2 + 3/(2k)) holds either way.

I went through this argument and could not fault it. It makes the bad coefficient sets harmless and reduces the
whole route to (P_k) for infinitely many k. No referee agent has checked it.

For (P_k) itself I see a possible proof, not checked by anyone: the fibre sum is the cohomology of the sheaf P_k
obtained by k−1 rounds of "Fourier transform, then multiply by the character sheaf". The Fourier transform
preserves irreducible perverse sheaves. If each P_i is irreducible of generic rank at least 2, the degree k+1
group, which is the constant quotient of P_k, vanishes. Irreducibility is preserved by the multiplication step as
long as the singular points of the transformed sheaf avoid the roots of f, and those singular points are fixed
multiples of h times roots, so this holds for all but finitely many h, provided f(0) ≠ 0. Every tool in this
sketch (Fourier inversion, exactness, location of singularities by stationary phase) is in Laumon's 1987 paper
and, according to report LIT, proved there without weights.

If (P_k) is proved this way, the route becomes a complete proof of Weil's bound for y^2 = f(x) that uses no
weights. That is a statement about a possible proof. It has not been written down or refereed.
