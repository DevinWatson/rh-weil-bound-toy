# A toy "sign-only" route to the Weil bound

A write-up, exact computations and a small Lean 4 formalisation of the argument sketched in footnote 3 of the
note "Remark" (https://alpo.ge/remark.pdf, November 2026). The note is not reproduced here.

**Status: a correct reduction, not a proof.** The Weil bound for y^2 = f(x) over a finite field is a theorem
(Weil, 1948). The question studied here is only whether the route in the footnote proves it. Nothing in this
repository says anything about the Riemann Hypothesis for the integers.

- Proved: the identity qN = M^k + R, the bound on R from k-1 Parseval steps, and "no cancellation implies
  |alpha| <= q^(1/2 + 3/(2k))".
- Open: the one cohomological statement the route rests on, for every k >= 4.
- False for some quadrics: at k = 4 whenever c_1 + c_2 + c_3 = 0, which includes the plain all-ones quadric in
  characteristic 3.

Start with `TOY_CASE.md`.

## Contents

| Path | What |
|---|---|
| `TOY_CASE.md` | The write-up, with every step labelled PROVED, CITED, CHECKED, OPEN or HINT |
| `reports/` | The underlying reports (derivation, two computations, referee, vanishing analysis, literature, archive read) |
| `compute/` | Scripts and exact outputs; `compute/main-session-check/` is an independent spot check |
| `lean/ToyWeil/` | `Parseval.lean`, `PowerSum.lean`: 13 theorems, Lean 4.34.1 with Mathlib, axioms `propext`, `Classical.choice`, `Quot.sound` |
| `tools/` | Helper scripts; some refer to a local copy of the Lean archive of the note, which is not included |

## Caveats

- Produced by AI agents (Claude) and checked by an orchestrating session; not refereed by a mathematician.
- The literature search worked from search summaries, so "known or new" is undecided and cited statement numbers
  need checking against the primary texts.
- Scripts were written for one machine; paths have been made relative and may need adjusting.
- No licence has been chosen yet.
