# Round four: the main session's check

2026-11-22 (UTC). Subject: character sums over finite fields. The bound is Weil's theorem of 1948 for the curves
y^2 = f(x). Nothing here says anything about the Riemann Hypothesis for the integers.

## Label for the whole

**A proof on paper with no known gap, reduced to named standard theorems; not refereed by a mathematician; not a
theorem.** What changed against round three: the central step (S5) was re-derived twice from clean pages of
Laumon's paper, the hostile referee found no fatal error, and the main session found a shorter proof of the
induction step (`LEMMA_R.md`, refereed by one agent: holds as written) that removes the one lemma nobody had read
at a source. The Lean files cover the
elementary half only. No part of the cohomological half is machine-checked, and it cannot be with today's Mathlib.

## What the main session did itself

### 1. Lean, recompiled (CHECKED)

`tools/lean_check.sh` on Parseval, PowerSum, Identity, Endgame2, Weighted, Unbounded, in that order, Lean 4.34.1,
one process: all six exit 0. The logs in `../lean/logs/` contain 34 lines "depends on axioms: [propext,
Classical.choice, Quot.sound]" (Parseval 8, PowerSum 5, Identity 6, Endgame2 3, Weighted 7, Unbounded 5), no other
axiom line, no `sorry`, no error. That is 22 theorems from rounds one to three plus 12 new ones. I read the
statements of the new ones:

- `identityW`: |F| N = M^(n+1) + R for the path quadric with arbitrary coefficients, N defined directly as the
  weighted sum over the zero set. `identity_bound_oneW`: | |F| N - M^(n+1) | <= (|F| - 1) |F| sqrt(|F|)^n for
  n >= 1, |t| <= 1, nonzero coefficients. These are S1 for every quadric the proof uses.
- `endgame_fibres_var`: if for unboundedly many k there are a degree s >= 1, finite families e, b and a constant C
  with the signed power-sum bound at radius q^(s(k+3)/2) and all |b_j| below that radius, then every
  |alpha_i| <= sqrt q. This is S9 and S10 with the field depending on k, which the round-three files did not have.

The Lean theorems take the identification of R_n with a signed sum of Frobenius eigenvalues as a hypothesis. That
identification is the cohomological half.

### 2. Exact tests, recomputed with separate code (CHECKED)

`../compute/main-session-check/round4_check.py`, output `round4_check_out.txt`. Own field arithmetic for F_(3^n)
and F_(4^n), own transforms (int64 with wraparound, made exact by the Lean-checked bound of S1, tested as an integer
inequality), own prediction code, Newton's identities in exact fractions. Engines agree with direct double sums in
189 of 189 values. No floating point.

- Hypothesis-valid cases: **105 of 105 determined stalk dimensions agree** with the prediction of S5, none
  undetermined, none disagreeing, all L-series integral. Reach: q = 3, quadratic character, d = 1 to Q_4
  (n <= 12) and d = 3 (irreducible cubic) to Q_2, where rank 10 is seen at n = 13; q = 4, cubic character, d = 1 to
  Q_5 (ranks 1, 2, 3, 5, 8; n <= 11, stage five to n = 10). The stalk at y = 0 is the fibre cohomology itself:
  dimensions r_(k+1) - [k odd] in every case reached. Anchor: for f = x^3 - x + 1 over F_3 the stalk of Q_1 at 0
  has e_2 = 3 = q, as the functional equation requires.
- Where the families overlap, my numbers equal A3's (for example the plain quadric at q = 3, d = 1: dimensions
  5, 4, 3 for Q_4 and 6, 6, 4 for Q_5 at the three points). Two independent engines.

**A correction to A3's reading of its controls.** A3 reports that when hypothesis (G) fails the prediction fails in
620 of 639 points, and takes that as proof that the test "has teeth". With the rank formulas applied properly
(the sheaf at a root is an extension by zero, so a singular point that lands on a root is absorbed), the same
numbers are predicted exactly: 17 of my 19 control points agree, one is undetermined, and the one that disagrees
is f(0) = 0, where the series at y = 0 does not terminate (two cohomology degrees: a real failure). So:

- the net counts follow the Euler-Poincare formula whether or not (G) holds; they test the bookkeeping of S5
  (sets, signs, scalings, ranks), not the hypothesis;
- the evidence for "one degree" in these tests is that the series at y = 0 is a polynomial of the predicted
  degree; a failure with eigenvalues that do not cancel would show as a series that does not stop, as in the
  f(0) = 0 control;
- (G) is sufficient, not necessary: the plain quadric at k = 5 fails (G) and its fibre series is still a polynomial.

None of this is a proof of the vanishing. There is still no data point with d >= 3 and k >= 3.

### 3. The central step against the pages

Re-read by me on the images for this check: journal pp. 153 to 156 (2.1.2.6 to 2.2.1.2), 158 to 159 (2.3.1.1
with proof, 2.3.1.2, 2.3.1.3), 162 (2.4.1 to 2.4.2.1). Together with the pages read before the round (146 to 149,
157 to 166) this covers every statement of Laumon that `PROOF_V2.md` S5 or `LEMMA_R.md` uses, except 1.2.2.1
(involutivity), which A2 read.

Findings:

1. The agents' three corrections to my own notes are right (sign convention of r, r_x, a_x for a shifted sheaf;
   "tame of the same rank" is false when there are invariants; 2.4.2.1 is stated at the origins only). The notes
   file is corrected.
2. The referee's item E1 is right: `PROOF_V2.md` uses the local-global comparison at finite points other than
   the origin, which needs a translation compatibility (register C-15) that nobody read.
3. **That dependency can be removed.** `LEMMA_R.md` proves the four facts the induction needs (rank, place and size
   of the drops, tameness at finite points, the blocks at infinity) from the Euler-Poincare formula applied in
   both directions of the transform, with Swan conductors under an Artin-Schreier twist. It uses Laumon up to
   2.3.1.1 only. It does not use vanishing cycles, the local transforms, Lemma T(c), SGA 7 XIII, Th. finitude or
   Gabber-Katz. A1's "rank count" and A2's "Argument B" are the same idea used for one term; Lemma R uses it for
   everything.
4. The conclusion of S5 needs only "P_k is a simple perverse sheaf of type T3": then the cohomology of the line
   with coefficients in P_k sits in one degree by two elementary facts (no sections with finite support; H^2_c is
   the coinvariants, which vanish for an irreducible non-constant sheaf). I checked this reduction; B2 found the
   same.

**Referee of Lemma R** (`reports/C1-lemma-R-referee.md`; one agent, Sonnet 5.5 medium, asked to break it against
the pages). Verdict: **holds as written; no fatal and no repairable defect; ten cosmetic points**, all entered in
`LEMMA_R.md`. The agent read the cited pages including the involutivity theorem 1.2.2.1 (journal p. 141), redid
every step with the special cases (the point 0, the frequency 0, non-semisimple tame modules), confirmed that
the induction gets everything Lemmas A and B gave, and checked the lemma against three classical examples
(Kummer sheaf, its translate, its Artin-Schreier twist), which fix the sign of the frequencies. It also found
that the printed primed formula (ii)' of 2.3.1.1 has the opposite sign to what 1.2.2.1 gives; the lemma does not
use it. Its exact check (36 values) re-uses my engine's output, so it tests the lemma's bookkeeping, not the sums
again. So the central step now has: two independent derivations by the route through local transforms (A1, A2),
one hostile reading of that route (B2), and a second, shorter route (Lemma R) with its own hostile reading (C1).

### 4. The global half and the lower bound

Read in `PROOF_V2.md` (S4, S6 to S11) and re-derived by me at the level of the exact sequences: the excision
sequence 0 -> T -> H^(k+1)_c -> H^(k-1)_c(Y)(-1) -> 0 (needs H^(k-2)_c(Y) = 0, which is Artin vanishing for the
perverse sheaf K[k] on A^k and on the affine complement of Y); H^(k+2)_c = C(-1); the fibre bound on C through one
closed point; the dichotomy; the s-th root and the limit. I agree with A4 and B2. The repair of the embedding
(S2 needs the eigenvalues themselves in C) is right and needed.

S11 (the lower bound) is A5's argument: the pairing on H with values in Q_l(-1) makes the eigenvalues stable
under alpha -> q/alpha. It needs odd d; A5's even-d control shows the hypothesis is real.

## Errors found in the round, classed

- Fatal: none found by anyone.
- Repairable, repaired: the translation step E1 and C-15 (removed by Lemma R); the draft's S11 (roots, higher
  inertia cohomology, arithmetic self-duality: A5); the embedding in S2 (A4); the order of choices Q, a, c in S0
  and S3 (A5); the Lean coverage (A7).
- Wrong readings from round three's OCR, none affecting the toy: 2.5.3 does not use Gabber-Katz; the local
  transform from infinity to 0' vanishes on slopes >= 1, not > 1; the direction of the semicontinuity inequality.
- Wrong in my notes: three items, corrected (above).
- Wrong in a round-four report: A3's reading of its controls (above). `PROOF_V2.md` section 3.1 overstates what
  was read about weights (B2's E5); `PROOF_V2.md` Lemmas A and B are superseded by Lemma R, not wrong.

## What the proof still rests on that nobody here has read at its source

1. The proof of the Grothendieck-Ogg-Shafarevich formula (Raynaud; SGA 5 X). Statement read. It is now the main
   tool of S5.
2. The inner proofs of the trace formula (SGA 4 1/2, Rapport, sections 5 to 8), which go through the fixed-point
   formula for curves of Weil's 1948 book. That formula is an intersection-number identity, not the bound being
   proved; nobody here read its proof.
3. The formalism for Q_l-bar coefficients (base change, projection formula, Kunneth with compact supports,
   duality): statements seen for torsion coefficients or in summary only.
4. BBD chapter 4 (4.1.1, 4.1.2, 4.2.5, 4.2.8, 4.3.1) and Katz-Laumon 2.1.3: read from OCR dumps, not page images.
5. Inside Laumon: the break decomposition and Hasse-Arf (2.1.1 to 2.1.2.6, citing Serre and Katz); 1.2.2.1 read
   by A2 only.
6. Whether the route is new. Weil's bound has had weight-free proofs since Stepanov and Bombieri, and Katz (2015)
   and Zhang (arXiv 2601.20187, 2026) give sheaf-theoretic routes to the general statement; none found uses the
   Fourier transform with a product over a quadric. Not established either way.

## What would turn this into a theorem

A mathematician who knows l-adic sheaves reading `PROOF_V2.md` with `LEMMA_R.md` (a few hours), or a formal proof,
which needs etale cohomology with l-adic coefficients, the six operations and perverse sheaves in Lean. Neither
exists here.
