# Main session check of round three (Claude Fable 5.2, 2026-11-20 20:50 UTC)

`ROUND3.md` and `PROOF_DRAFT.md` were written by agents. Workflow `wf_4ee702f3-5d9`: ten agents on
`claude-sonnet-5-5` at medium effort, 41 minutes, 1.99 million subagent tokens, no failures. This file says what
I checked myself. Everything is about character sums over finite fields, where the bound is Weil's theorem of
1948. It says nothing about the Riemann Hypothesis for the integers.

## Where the route stands

A complete proof draft now exists (`PROOF_DRAFT.md`, steps S0 to S12) of |alpha| = sqrt(q) for the Frobenius
eigenvalues attached to y^2 = f(x), f squarefree of odd degree at least 3, q odd, along the route of footnote 3,
using no weights. It is a draft checked by agents and by me, not by a specialist, and one step rests on a source
that nobody has read from clean pages.

- **Reduction (Claim A): holds, with two corrections** (referee agent A; re-derived by referee H; I had derived the
  same argument before the round). The wrong-parity group is a quotient of the constant quotient, not equal to
  it; and the sheaf must be geometrically nontrivial (for the trivial sheaf the fibre statement holds and the
  conclusion is false, which the agent checked on exact data).
- **Fibre statement (Claim B): no error found.** Agent B wrote the induction with an explicit invariant; agent C
  proved k = 2 and k = 3 by hand for every choice of coefficients; referee I checked each cited statement of
  Laumon against the text dump and calls the step proved modulo the citations; referee H re-derived everything
  except the local structure of the transform at infinity and its tameness, and calls that one step unverified.
- **The condition on the coefficients** does not involve h. It is: no product rho_i rho_(i-2) ... of the ratios
  rho_i = -c_(i-1)/c_i is a ratio of two roots of f. It can be met over a finite extension for every k. The plain
  all-ones quadric fails it from k = 5 on. The condition is sufficient, not necessary.
- **Dimension formula:** r_1 = 1, r_2 = d, r_(i+1) = d r_i + r_(i-1), and the fibre cohomology has dimension
  r_(k+1), minus 1 when k is odd (d^2+1, d^3+2d-1, d^4+3d^2+1 for k = 2, 3, 4).

## Checked by me

| Item | How | Result |
|---|---|---|
| `lean/ToyWeil/Endgame2.lean` | Recompiled; text search for `sorry`, `axiom`, `native_decide` | Exit 0; three theorems, standard axioms. The signed three-family lemma is exactly the dichotomy of the reduction. Total now 22 theorems in four files. |
| Number of eigenvalues of the fibre sum | Own code, exact arithmetic in Z[omega] over F_3 to F_729 (`compute/main-session-check/round3_check_out.txt`) | f = x - 1: the sums satisfy a recurrence of order exactly 2 for k = 2, exactly 2 for k = 3 with c = (1,1), and exactly 1 for k = 3 with c = (1,-1) where the hypothesis fails. All three as predicted. |
| The reduction | Derived independently before the round; compared with agent A's corrected theorem | Agree. I had "equal to" where "a quotient of" is right; harmless. |
| The induction's use of the local Fourier transform | Compared with what I know of the theory (Laumon; Katz, Exponential Sums and Differential Equations, section 7.4): the transform at infinity is the sum over the finite singular points s of L_psi(b s y) tensor (tame); the finite singular points of the transform are minus the frequencies at infinity divided by b, and 0 when there is a tame part; tame goes to tame | Consistent with the induction as written. This is from memory, not from an opened source. |

## Not checked by me

- Laumon's statements on clean pages. The agents read an OCR text with garbled formulas. The file
  `compute/D/laumon13.pdf` that an agent saved is a different paper (a talk by Katz), so no page images of
  Laumon 1987 are on disk.
- The other cited theorems (trace formula, Künneth, base change, Artin vanishing in both forms, duality on
  curves, the Euler characteristic formula, simple perverse sheaves as middle extensions).
- Agent E's and referee I's larger exact tests (degree 10 for the cubic at k = 2; degree 7 at k = 5 over F_5).

## Loose ends

1. Read Laumon 1.3.2.3, 1.3.2.4, 1.4.2.1, 2.3.1 to 2.3.3, 2.4.3 and 2.5.3.1 on the pages, and confirm that the
   proofs of chapters 1 and 2 use no weights.
2. No exact test reaches degree at least 3 with k at least 3 (the predicted dimension is 32).
3. The Lean theorem `endgame_fibres` assumes one field for all k; the route uses a larger field for larger k. The
   per-k step is formal; the passage to the limit is on paper.
4. Novelty is undecided. The sources agent places the route in the "method of families" of Rankin, Laumon and
   Katz and found no published instance; three relevant sources were not opened. Absence of hits is not evidence.
5. A specialist has not read it.
