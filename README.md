# A toy "sign-only" route to the Weil bound

This repository contains **two companion studies** of the path-quadric "sign-only" route ($q N = M ^ k + R$) sketched in footnote 3 of the note "Remark" (https://alpo.ge/remark.pdf, November 2026). The note is not reproduced here. Nothing in this repository says anything about the Riemann Hypothesis for the integers; both studies concern classical finite-field character/exponential sums where Weil (1948) is already a theorem.

---

## 1. Kummer / Hyperelliptic Version (`y^2 = f(x)`, root directory)

**Status: a correct reduction, not a proof (stalls past $k = 4$).** Studies $t(x) = \chi(f(x))$ for odd squarefree degree $d \ge 3$ over odd $\mathbb{F} _ q$.

- Proved: the identity $q N = M ^ k + R$, the bound on $R$ from $k - 1$ Parseval steps, and "no cancellation implies $|\alpha| \le q ^ {1/2 + 3/(2k)}$".
- Open: the cohomological vanishing input $(S _ k)$ for $k \ge 4$ in Round 1 (and for $k \ge 5$ after Round 2's weight-free $k = 4$ proof, which reaches $q ^ {7/8}$). Tame monodromy $-1$ at infinity cancels in pairs $(-1)(-1) = +1$ along non-adjacent boundary divisors $D _ {ab} \subset (\mathbb{P} ^ 1) ^ k$, so forget-supports fails.
- False for some quadrics: at $k = 4$ whenever $c _ 1 + c _ 2 + c _ 3 = 0$, which includes the plain all-ones quadric in characteristic 3.

Start with [TOY_CASE.md](TOY_CASE.md).

## 2. Artin–Schreier Companion Version (`t(x) = psi(f(x))`, `artin-schreier-toy-case/`)

**Status: closes weight-free for all even $k \ge 4$, yielding the full Weil bound $|\sum _ {x \in \mathbb{F} _ q} \psi(f(x))| \le (d - 1)\sqrt{q}$ ($d \ge 3$, $p \nmid 2d$).**

Replacing the tame Kummer sheaf $\mathcal{L} _ \chi(f)$ with the wildly ramified Artin–Schreier sheaf $\mathcal{L} _ \psi(f)$ restores **cleanness at infinity** ($j _ ! K \cong R j _ * K$) on the projective quadric cone $\overline{Y} \subset \mathbb{P} ^ k$ whenever $\{Q _ c = 0\}$ intersects $\{X _ 1 ^ d + \dots + X _ k ^ d = 0\}$ transversally in $\mathbb{P} ^ {k-1}$:

- **Weight-free $(S _ k)$ for all even $k \ge 4$:** proven via Katz–Laumon (1985) Appendix 2.4 (`Thm 2.4.1`, weight-free) + BBD Artin vanishing (`4.1.1–4.1.2`, weight-free), with an elementary proof that the non-transversal locus $\mathcal{B} _ {k, d} \subset \mathbb{P} ^ {k-2} _ c$ has dimension $\le k - 3 < k - 2$ (and equals exactly the $d ^ 2$ lines $c _ 1 + \zeta _ 1 c _ 2 + \zeta _ 1 \zeta _ 2 c _ 3 = 0$, $\zeta _ i ^ d = -1$, at $k = 4$).
- **Closed-form middle Betti number for all even $k \ge 2$:** $\dim H ^ {k-1} _ c(Y, K) = 2 \sum _ {j=1} ^ {k-1} (d - 1) ^ j + 1$ ($5, 29, 125, \dots$ for $d = 3$).
- **Upgraded Lean 4.34.1 formalization (23 theorems, zero warnings, standard axioms only):** generalizes `ToyWeil` to arbitrary nonzero weights $c _ i \ne 0$, arbitrary unbounded subsequences of $k$, and $k$-dependent extension fields $\mathbb{F} _ {q ^ m}$ (necessary already at $k = 4, d = 3, p = 7$, where all 36 points of $(\mathbb{F} _ 7 ^ *) ^ 2$ lie on $\mathcal{B} _ {4, 3}$), plus machine-checked algebraic transversality proofs.
- **Forensic review of the Kummer study** ([artin-schreier-toy-case/REVIEW_OF_TOY_CASE.md](artin-schreier-toy-case/REVIEW_OF_TOY_CASE.md)): includes an unconditional weight-free closure of Round 2 `K4T`'s open exception `(X2)` ($f(x) = x ^ d - a$) and an exact symmetry-group explanation of `K4C`'s coincidence `(iv)`.

Start with [artin-schreier-toy-case/ARTIN_SCHREIER_TOY_CASE.md](artin-schreier-toy-case/ARTIN_SCHREIER_TOY_CASE.md).

![A Weight-Free Sign-Only Proof of the Weil Bound](artin-schreier-toy-case/artin_schreier_proof_infographic.png)

*Proof overview poster ([4K PNG](artin-schreier-toy-case/artin_schreier_proof_infographic.png) · [scalable vector SVG](artin-schreier-toy-case/artin_schreier_proof_infographic.svg)).*

---

## Contents

| Path | What |
|---|---|
| [TOY_CASE.md](TOY_CASE.md) | Kummer write-up, with every step labelled `PROVED`, `CITED`, `CHECKED`, `OPEN` or `HINT` |
| [reports/](reports/) | Underlying Kummer reports (derivation, two computations, referee, vanishing analysis, literature, archive read) |
| [compute/](compute/) | Kummer scripts and exact outputs; `compute/main-session-check/` is an independent spot check |
| [lean/ToyWeil/](lean/ToyWeil/) | `Parseval.lean`, `PowerSum.lean`: 13 theorems, Lean 4.34.1 with Mathlib, axioms `propext`, `Classical.choice`, `Quot.sound` |
| [tools/](tools/) | Helper scripts for the Kummer study; some refer to a local copy of the Lean archive of the note, which is not included |
| [artin-schreier-toy-case/ARTIN_SCHREIER_TOY_CASE.md](artin-schreier-toy-case/ARTIN_SCHREIER_TOY_CASE.md) | Artin–Schreier companion write-up proving the Weil bound weight-free for all even $k \ge 4$ |
| [artin-schreier-toy-case/artin_schreier_proof_infographic.png](artin-schreier-toy-case/artin_schreier_proof_infographic.png) | Proof overview infographic poster (4K PNG; vector source in [artin_schreier_proof_infographic.svg](artin-schreier-toy-case/artin_schreier_proof_infographic.svg)) |
| [artin-schreier-toy-case/REVIEW_OF_TOY_CASE.md](artin-schreier-toy-case/REVIEW_OF_TOY_CASE.md) | Forensic review of the Kummer study, closing exception `(X2)` and resolving coincidence `(iv)` |
| [artin-schreier-toy-case/compute/](artin-schreier-toy-case/compute/) | Exact cyclotomic-ring $\mathbb{Z}[\zeta _ p]$ DP/Segre scripts and verified outputs (`t1`–`t4`, 0 failures) |
| [artin-schreier-toy-case/lean/ArtinSchreierToy/](artin-schreier-toy-case/lean/ArtinSchreierToy/) | `WeightedParseval.lean`, `ExtensionEndgame.lean`, `Transversality.lean`: 23 theorems, Lean 4.34.1 with Mathlib, axioms `propext`, `Classical.choice`, `Quot.sound` |
| [artin-schreier-toy-case/tools/lean_check.sh](artin-schreier-toy-case/tools/lean_check.sh) | Portable Lean 4 build/check script for `ArtinSchreierToy` |

## Caveats

- Both versions were produced by AI agents (the Kummer study by Claude; the review and Artin–Schreier companion study by Antigravity / Gemini) and have not been refereed by a mathematician.
- In the Kummer Round 1 study, the literature search worked from search summaries, so "known or new" is undecided and cited statement numbers need checking against primary texts. In the Artin–Schreier study, the weight-free status of BBD 4.1.1–4.1.2 and Katz–Laumon Appendix 2.4 (`Thm 2.4.1`, `2.4.4`) was checked against the primary papers, while the `l`-adic cohomology steps remain paper proofs (not formalized in Lean).
- Scripts were written for one machine; paths have been made relative and may need adjusting (e.g. `MATHLIB_DIR` for `lean_check.sh`).
- No licence has been chosen yet.
