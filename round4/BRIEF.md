# Round four: from a proof draft to a complete proof on paper

Read first: `../round3/PROOF_DRAFT.md` (steps S0 to S12 and its three lists), `../round3/MAIN_SESSION_CHECK.md`,
and `../round3/BRIEF.md` for the setting, Claim A and Claim B. Earlier material: `../TOY_CASE.md`,
`../round2/ROUND2.md`.

This is about character sums over finite fields. The bound in question is Weil's theorem of 1948. Nothing here
says anything about the Riemann Hypothesis for the integers.

## What changed since round three

Laumon's 1987 paper is now on disk as clean page images, and the main session has read the statements the draft
cites on those pages.

- Page images: `<workspace>/remark-review-20261120/laumon-1987/png/pNNN.png`, NNN = PDF page
  (001 to 081). **Journal page = PDF page + 129.** Open them with the Read tool; they are legible.
- The main session's reading, in its own words, with page numbers:
  `<workspace>/remark-review-20261120/laumon-1987/LAUMON_NOTES.md`. It covers 1.3.1.1 to 1.3.2.4,
  the types T1 to T3, 1.4.2.1, 2.2.2.1, 2.2.2.2, 2.3.1.1 to 2.3.1.3, 2.3.2.1, 2.3.2.3, 2.3.3.1, 2.4.2.1 to 2.4.3
  and 2.5.3.1 with its proof. Treat it as one more reader's notes: check it against the images, do not assume it.
- To find a statement, use the text layer (rough OCR, good enough for searching numbers):
  `python <workspace>/remark-review-20261120/laumon-1987/tools/pages.py find "<scratch>/laumon-1987-20261121/laumon-1987-pmihes-65.pdf" "2\.1\.2\.7"`
  prints the PDF pages that contain the pattern. Then read the image of that page. Never quote the OCR text as
  the source: read the image.
- The paper is copyrighted. In your report, state results in your own words with statement number and journal
  page. Do not copy passages of the paper into any file. Do not copy the images anywhere.

## The goal of the round

A proof in which every step is either PROVED in full or CITED with the statement read at its source, and in
which the induction of S5 has been re-derived by someone other than its author. The draft's own list of what
stands between it and that is its "List 2". Each agent below owns part of that list.

The outcome is allowed to be "the proof does not close, and here is where". A hole reported is a good result. A
hole papered over is the worst result.

## Rules for every agent

- Label every claim PROVED (full argument given), CITED (author, title, year, statement number, page, and where
  you read it: page image, web page with its address, or local file), CHECKED (exact arithmetic or Lean; script
  and output file named), OPEN or HINT.
- No proof may use weights, purity, the Weil bound or the Weil conjectures. When you cite a theorem, say whether
  its own proof uses them, and how you know.
- Floating point may suggest, never certify. Anything reported as checked is exact integer or exact algebraic
  arithmetic.
- Do not download files. You may read web pages (for example pages of the Stacks Project). The local text dumps
  of round two (`../round2/compute/LIT/`: SGA1.txt, SGA4h.txt, BBD.txt, KL.txt, TRAVL.txt and others) may be used
  for searching; they are OCR and must be named as such when relied on.
- Write only under `round4/` (the Lean agent also in `../lean/ToyWeil/`). Your report goes in `round4/reports/`,
  your scripts and outputs in `round4/compute/<your letter>/`. Write the report file as you go, not at the end.
- Machine load: one compute process at a time per agent, at most 2 threads, started at below-normal priority.
  Do not start shells in a loop. Lean is compiled only through
  `wsl.exe -d Ubuntu -- bash ./tools/lean_check.sh ToyWeil.<Module>`
  (called from PowerShell), one module at a time; it takes a lock, so wait for it.
- Never extract, build or run the Lean archive of the claimed proof of the Riemann Hypothesis.
- Read the clock with `date -u` if you stamp a time.
- Your final answer is a short structured summary; the substance is in your report file.

## The parts

**A1. The Fourier induction, re-derived (S5).** Do not open `../round3/reports/B-*.md` or section S5 of the draft
until your own derivation is written. From Laumon's pages, with P_1 = j_!L[1] and
P_(i+1) = (j_!L) tensor FT_(h c_i)(P_i), state and prove an explicit induction invariant: P_i is a simple perverse
sheaf of type T3; its finite singular set; its local monodromy at each singular point; its structure at infinity
as a sum of blocks L_psi(a x) tensor (tame) with the set of a; its generic rank. Give exact scalings and signs
(the transform with parameter b = h c_i, the frequencies, the points of the next singular set). State the
condition on c under which the step goes through, and prove that P_(i+1) is again of type T3 (irreducible, the
extension by zero equals the middle extension at every point, not an Artin-Schreier sheaf). Then derive the
conclusion: for those c and every h != 0 the cohomology of the line with coefficients in P_k sits in one degree.
For every statement of Laumon you use, check on the page that its hypotheses hold here. Only then compare with
the draft and with round three's report B, and list every difference, however small.

**A2. Dependency and weight audit of Laumon chapters 1 and 2.** For each statement the induction needs (the list
in `LAUMON_NOTES.md`, plus 1.2.2.1, 1.2.3.x, 2.1.x on slopes, 2.1.2.7, 2.1.4, 2.2.1.x, 2.5.1, 2.5.2), read its
PROOF on the page images and record what it rests on: earlier statements of the paper, and outside sources
(Katz-Laumon 1985, BBD, SGA 7 XIII, SGA 4 1/2, Gabber-Katz). Produce the dependency table. Answer precisely:
(1) does any proof in the chain use weights, purity or Weil II; (2) does the tame case, which is all the toy
needs, avoid the Gabber-Katz theorem 2.2.2.2 and the wild part of section 2.5; (3) which readings of round three
(made from garbled OCR: the slope maps, the inequality in the semicontinuity statement, LAU.txt lines 1126-1131,
1176-1179, 1285-1324, 1360-1375) were wrong. Also say where chapters 1, 2, 3 and 4 begin and where weights first
appear.

**A3. Exact tests aimed at breaking the induction.** The round-three tests reach degree d = 1 for k >= 3 and
d = 3 only for k = 2. Test what the induction predicts beyond that, with exact arithmetic: generic ranks
r_1 = 1, r_2 = d, r_(i+1) = d r_i + r_(i-1) of the iterated transforms, the location of the singular points of
each transform (the rank of the stalk drops exactly at the predicted points and by the predicted amount), and
fibre dimensions where reachable. Sums over F_(q^n) of this shape can be computed by repeated additive Fourier
transforms on F_(q^n), which costs about n q^n per step, so n near 10 to 14 is reachable for q = 3 or 4. The
induction does not seem to use that the character is quadratic, only that it is nontrivial, tame, and nontrivial
at infinity (chi^d != 1); if you agree after reading S5, a cubic character over F_4 or F_7 gives d = 2 at larger
i. Look for a counterexample: a case where the hypothesis on c holds and the prediction fails. Report every case
run, including the ones that agree.

**A4. The global side, re-derived (S4, S7, S8, S9, S10).** From first principles and with explicit hypotheses:
the identification of the fibre cohomology with the cohomology of the line with coefficients in P_k; the Leray
argument over the h-line; the fibre bound on a constant quotient; the dichotomy; the passage to F_q with a field
that grows with k, and the limit in k. Compare with round three's report A afterwards. Check small cases exactly
where you can.

**A5. The lower bound and the reductions (S11, S0).** Prove that the eigenvalues are permuted by
alpha -> q/alpha, so that |alpha| <= sqrt(q) for all of them gives equality, without weights: by duality on the
curve or by the functional equation of the L-function of the character chi(f) of F_q[x]. Say exactly which
standard theorem is used and where you read it. Check exactly on examples that the L-polynomial has the symmetry.
Also write out S0 (translation to make f(0) != 0, extension of scalars) in full.

**A6. The standard theorems, opened.** For items 1 to 6, 8 and 9 of the draft's List 1 (trace formula; Künneth,
proper base change, projection formula, excision, Leray; Artin vanishing; duality on curves;
Grothendieck-Ogg-Shafarevich; BBD chapter 4 statements; Katz-Laumon 2.1.3 and 2.1.5; SGA 1 V 8.2): find the
statement at a source you can read (Stacks Project tag pages are readable web pages; the arXiv text of SGA 1 is
the local dump), record the exact reference and hypotheses, and check each USE of it in the draft (name the step)
against those hypotheses. Mark each OPENED (where) or NOT OPENED. Say for each whether its proof involves weights
and how you know.

**A7. Lean (S1, S10).** In `../lean/ToyWeil/`: (1) the identity q N = M^k + R and the fibre bound for the
quadric with arbitrary nonzero coefficients c_i, if the existing files state them only for the plain quadric;
(2) the endgame as S10 needs it: for an unbounded set of k, a field degree s(k) >= 1 and the inequality
|alpha|^(s k) <= q^(s (k+3)/2), conclude |alpha| <= sqrt(q); and the signed dichotomy in the form used by S9
with the field allowed to depend on k. Standard axioms only, no `sorry`, print the axioms of every theorem.
The companion study's files `WeightedParseval.lean` and `ExtensionEndgame.lean` (in the public repository,
folder `artin-schreier-toy-case/lean/ArtinSchreierToy/`; a local clone may not exist) solve a similar problem;
write your own proofs.

**B1. Assembly (after A1 to A7).** Write `round4/PROOF_V2.md`: the whole proof, every step labelled, every
citation with where it was read, the reports' disagreements stated and not smoothed, and a list of what is still
not PROVED or CITED-and-read. Statements of cited theorems in your own words.

**B2. Hostile referee (after B1).** Read `PROOF_V2.md` end to end with the page images at hand and try to break
it. Verdict per step; errors classed fatal, repairable or cosmetic; and the label you would put on the whole.
