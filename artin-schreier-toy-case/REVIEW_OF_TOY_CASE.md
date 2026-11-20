# Forensic Review of the Kummer `toy-case` Study

**Scope.** This document reviews the Round 1 study in this repository ([../TOY_CASE.md](../TOY_CASE.md), [../reports/](../reports/), [../compute/](../compute/), [../lean/ToyWeil/](../lean/ToyWeil/)) together with its local Round 2 follow-up (`round2/reports/*`, `Identity.lean`, not yet pushed to this repository) investigating footnote 3 of `alpo.ge/remark.pdf` (the sign-only $q N = M ^ k + R$ path-quadric route to the Weil bound for hyperelliptic curves $y ^ 2 = f(x)$ over $\mathbb{F} _ q$). Nothing here concerns the Riemann Hypothesis for the integers. Nothing in the original Kummer study was modified.

**Labels.** `PROVED` (complete proof given), `CITED` (standard theorem with source), `CHECKED` (exact integer/rational arithmetic, script and output named), `OPEN`, `HINT`. No proof below uses weights, purity, or the Weil bound.

---

## 1. Executive Verdict

The Kummer `toy-case` investigation is unusually rigorous, self-critical, and well-engineered. Its core conclusion is **correct**:

- For the **Kummer / hyperelliptic** setting ($t(x) = \chi(f(x))$, odd squarefree degree $d \ge 3$, odd $q$), every elementary step of footnote 3 ($q N = M ^ k + R$, iterated Parseval $|R| \le q ^ {(k+3)/2}$, power-sum no-cancellation endgame) is valid (`PROVED`, partly formalized in Lean 4).
- The entire mathematical content sits in the single upper-cohomology vanishing statement $(S _ k')$: $H ^ k _ c(Y _ c, K) = 0$ (sharpened from $(S _ k)$ in the Round 2 report `RED-reduction-check.md`, since $H ^ {k+1} _ c$ carries the same Frobenius trace sign $(-1) ^ {k-1}$ as $H ^ {k-1} _ c$).
- Round 2 achieved one genuine weight-free breakthrough: `K4T-k4-theory.md` proved $(S _ 4)$ **without weights** outside an explicit finite union of coincidence lines `X4` (plus an open exception `X2`, $f(x) = x ^ d - a$, which we **close unconditionally below**). That yields $|\alpha _ i| \le q ^ {7/8}$ unconditionally and weight-free via footnote 3's route.
- For **$k \ge 5$, $(S _ k')$ and $(W ^ *)$ remain completely `OPEN`** for $t(x) = \chi(f(x))$. Because the Kummer sheaf is tame at infinity with monodromy $-1$, non-adjacent boundary divisors $D _ {ab} = \{x _ a = x _ b = \infty\} \subset (\mathbb{P} ^ 1) ^ k$ have trivial monodromy $(-1)(-1) = +1$ (Round 2 `FS-forget-supports.md`), so $K$ is **not clean at infinity** and the forget-supports criterion fails. Thus the Kummer toy case stalls at $k = 4$ ($q ^ {7/8}$) and does not reach the Weil bound $q ^ {1/2}$.

---

## 2. File-by-File Verification Summary

| Component | Files Reviewed | Audit Verdict |
|---|---|---|
| Round 1 synthesis | [../TOY_CASE.md](../TOY_CASE.md) | Accurate and honest. Section 9's one-line perversity shortcut for $i ^ * [-1]$ was rightly tightened by Round 2 `FS` Lemma 1, and its fibration claim was rightly refined by Round 2 `RED`. |
| Round 1 theory & referee | [../reports/A-derivation.md](../reports/A-derivation.md), [../reports/H-referee.md](../reports/H-referee.md), [../reports/I-vanishing.md](../reports/I-vanishing.md) | Solid. `I`'s Proposition 1 (lower-half Artin vanishing without non-characteristic hypothesis) and Theorem 4 ($c _ 1 + c _ 2 + c _ 3 = 0$ failure plane) are verified. |
| Round 2 fibration check (`RED`) | Local `round2/reports/RED-reduction-check.md` | Solid. Key genuine improvement: $H ^ {k+1} _ c$ has the same sign as $H ^ {k-1} _ c$, reducing $(S _ k)$ to $(S _ k')$: $H ^ k _ c(Y, K) = 0$. Correctly flags $R ^ {k+1}$ punctuality and $d _ 2$ as open inputs. |
| Round 2 forget-supports (`FS`) | Local `round2/reports/FS-forget-supports.md` | Solid and refreshingly frank about failure on Kummer. Theorem A is exact; Section 2 correctly locates the obstruction at the non-adjacent boundary divisors $D _ {ab}$. |
| Round 2 $k = 4$ theory (`K4T`) | Local `round2/reports/K4T-k4-theory.md` | **Crown jewel of the Kummer study**, checked step by step. Tameness proof via total-space Euler characteristic (Section 3) is watertight once lisseness of $V$ off $S$ is cited (see Section 3.4 below). Exception `(X2)` ($f = x ^ d - a$) is **closed unconditionally** in Section 3.1 below. |
| Round 2 $k = 4$ compute (`K4C`) | Local `round2/reports/K4C-k4-computation.md` | Exact arithmetic throughout; E1–E5 verified. Its unexplained coincidence `(iv)` ($c = (1,1,i), (1,i,i), (i,1,1)$) is **resolved** in Section 3.2 below. |
| Round 2 general-$k$ compute (`NUM`) | Local `round2/reports/NUM-moments-and-bad-sets.md` | Exact DP up to $k = 6$, good identification of Family B as a sum of squares. At review time, M3/M4 computations were still active in `compute/NUM/` and Section 3 had not yet been appended. |
| Round 2 primary literature (`LIT`) | Local `round2/reports/LIT-primary-sources.md` | High value. Directly verified weight-freeness of BBD 4.1.1–4.1.2, Laumon 1.3.1.1/1.3.2.3, Katz–Laumon 2.1.3 & Appendix 2.4, and SGA 1 XIII 2.12. Rightly caught that "Sommes trig. Thm 8.4" quoted in `FS` does not exist in the opened edition. |
| Lean 4 formalization | [../lean/ToyWeil/Parseval.lean](../lean/ToyWeil/Parseval.lean), [../lean/ToyWeil/PowerSum.lean](../lean/ToyWeil/PowerSum.lean) (and Round 2 `Identity.lean`) | Compiles cleanly with zero `sorry` and standard axioms `[propext, Classical.choice, Quot.sound]`, **but has two structural specification gaps** relative to footnote 3 (Section 3.3 below). |

---

## 3. New Mathematical Findings and Resolutions from This Review

### 3.1 Unconditional Weight-Free Closure of `K4T`'s Open Exception `(X2)` ($f(x) = x ^ d - a$) — `PROVED` & `CHECKED`

In Round 2 `K4T-k4-theory.md` (Section 5.3(iii)), Theorem C proved $V _ \pi = 0$ for every squarefree odd-degree $f$ with $f(0) \ne 0$ **except** $f(x) = x ^ d - a$ ($a \ne 0$, $\mu = \mu _ d$), where it only obtained $\dim V _ \pi \le 1$ and left $V _ \pi = 0$ as an open exception `(X2)` with an unproved local-exponent hint.

**Theorem (Closure of `(X2)`, `PROVED`, weight-free).** Let $q$ be odd and $f(x) = x ^ d - a \in \mathbb{F} _ q[x]$ be squarefree with $d \ge 3$ odd and $a \ne 0$ (hence $p \nmid d$). Then $V _ \pi = 0$. Consequently, `K4T`'s Theorem C holds with **no exception `(X2)`**, and Theorem D ($(S _ 4)$ off `X4`) holds for $f(x) = x ^ d - a$ as well.

**Proof.** By `K4T` Section 5.1, $V _ \pi(-1) \cong \mathrm{coker}(\Phi)$, where

```math
\Phi : H ^ 2 _ c(T, K _ T) \longrightarrow W := \bigoplus _ {\rho \in \mu _ d} H ^ 2 _ c(T _ \rho, K _ T | _ {T _ \rho}) \cong \overline{\mathbb{Q}} _ \ell(-1)[\mu _ d]
```

is the restriction map on $T = \mathbb{A} ^ 2 _ {(x, r)}$ with $K _ T = j _ ! \mathcal{L} _ {\chi(f(x) f(rx))}$ and $T _ \rho = \{r = \rho\}$.

1. **Group action.** Because $p \nmid d$, the finite group $G = \mu _ d \times \mu _ d$ has order $d ^ 2$ prime to $p$ and acts on $T$ by $(\zeta, \rho) \cdot (x, r) = (\zeta x, \rho r)$, preserving $f(x) f(rx) = (x ^ d - a)(r ^ d x ^ d - a)$ identically. Hence $G$ acts on $K _ T$, and $\Phi$ is $G$-equivariant.
2. **Nontrivial $\{1\} \times \mu _ d$-isotypic part.** By `K4T` Sections 5.2–5.3, on $U' = \{x \ne 0\} \subset T$, the $\{1\} \times \mu _ d$-action on $H ^ 2 _ c(U', K _ T) = H ^ 1 _ c(\mathbb{G} _ m, F) \otimes H$ acts via $\mathrm{id} \otimes \sigma _ \rho$ on $H = H ^ 1 _ c(\mathbb{A} ^ 1, F)$. Since $\varepsilon(\rho) = 1$ (as $(\rho x) ^ d - a = x ^ d - a$ fixes the stalk $F _ 0$ identically), the Lefschetz trace in `K4T` 5.3(ii) gives multiplicity $1$ for every nontrivial character of $\mu _ d$ and multiplicity $0$ for the trivial character. Thus $\Phi(H ^ 2 _ c(U', K _ T))$ has dimension $d - 1$ inside the $(d - 1)$-dimensional hyperplane $W _ {\ne 1} = \{(v _ \rho) : \sum _ \rho v _ \rho = 0\}$, hence equals $W _ {\ne 1}$.
3. **Reduction to $G$-invariants.** On each fibre $T _ \rho = \mathbb{A} ^ 1 _ x$ with $K _ T | _ {T _ \rho} = j' _ ! \overline{\mathbb{Q}} _ \ell$, scaling $x \mapsto \zeta x$ lies in the connected group $\mathbb{G} _ m$ and therefore acts trivially on $H ^ 2 _ c(T _ \rho, j' _ ! \overline{\mathbb{Q}} _ \ell) = \overline{\mathbb{Q}} _ \ell(-1)$. Hence $\mu _ d \times \{1\}$ acts trivially on $W$, so $W ^ G = W ^ {\{1\} \times \mu _ d}$ is the remaining 1-dimensional diagonal summand. Surjectivity of $\Phi$ is therefore equivalent to surjectivity of $\Phi ^ G : H ^ 2 _ c(T, K _ T) ^ G \to W ^ G$.
4. **Quotient identification.** Let $\pi : T \to \bar{\bar{T}} := \mathbb{A} ^ 2 _ {(w, s)}$, $(x, r) \mapsto (x ^ d, r ^ d)$, and $K _ {\bar{\bar{T}}} := j _ ! \mathcal{L} _ {\chi((w - a)(s w - a))}$. Then $K _ T = \pi ^ * K _ {\bar{\bar{T}}}$ everywhere on $T$ (including along $x = 0$ and $r = 0$, where $(w - a)(sw - a) \ne 0$). Since $\pi$ is finite and $(\pi _ * \overline{\mathbb{Q}} _ \ell) ^ G = \overline{\mathbb{Q}} _ \ell$ everywhere, the projection formula gives $(\pi _ * K _ T) ^ G \cong K _ {\bar{\bar{T}}}$. Thus $\Phi ^ G$ identifies canonically with the restriction map

```math
\bar{\bar{\Phi}} : H ^ 2 _ c(\bar{\bar{T}}, K _ {\bar{\bar{T}}}) \longrightarrow H ^ 2 _ c(\bar{\bar{T}} _ 1, K _ {\bar{\bar{T}}} | _ {\bar{\bar{T}} _ 1}), \qquad \bar{\bar{T}} _ 1 = \{s = 1\}.
```

5. **Vanishing of $\mathrm{coker}(\bar{\bar{\Phi}})$.** By excision for $\bar{\bar{T}} _ 1 \subset \bar{\bar{T}}$, $\mathrm{coker}(\bar{\bar{\Phi}})$ injects into $H ^ 3 _ c(\bar{\bar{T}} \setminus \bar{\bar{T}} _ 1, K _ {\bar{\bar{T}}})$. Consider $\bar{\bar{p}} : \bar{\bar{T}} \setminus \bar{\bar{T}} _ 1 \to \mathbb{A} ^ 1 _ s \setminus \{1\}$:
   - At $s = 0$: the fibre carries $j _ ! \mathcal{L} _ {\chi(-a(w - a))}$ on $\mathbb{A} ^ 1 _ w$, ramified at $w = a$ and $\infty$ ($\chi _ c = 1 - 1 = 0$, $H ^ 0 _ c = H ^ 2 _ c = 0$), so $H ^ * _ c = 0$ in all degrees.
   - Over $s \in \mathbb{A} ^ 1 _ s \setminus \{0, 1\}$: the affine-linear substitution $w = a \bigl(1 + \frac{1 - s}{s} u\bigr)$ gives the exact algebraic identity

```math
(w - a)(s w - a) = \left(\frac{a(1 - s)}{s}\right) ^ 2 \cdot s \cdot u(u - 1).
```

   Since $\bigl(\frac{a(1 - s)}{s}\bigr) ^ 2$ is a square unit on $\mathbb{A} ^ 1 _ s \setminus \{0, 1\}$, we have an isomorphism of sheaves $K _ {\bar{\bar{T}}} | _ {\mathbb{A} ^ 1 _ w \times (\mathbb{A} ^ 1 _ s \setminus \{0, 1\})} \cong \mathcal{L} _ {\chi(s)} \boxtimes j _ ! \mathcal{L} _ {\chi(u(u - 1))}$. Therefore $R ^ 0 = R ^ 2 = 0$ and $R ^ 1 \bar{\bar{p}} _ ! K _ {\bar{\bar{T}}} | _ {\mathbb{A} ^ 1 _ s \setminus \{0, 1\}} \cong \mathcal{L} _ {\chi(s)}$ (rank 1, nontrivial monodromy $-1$ at $0$ and $\infty$).
   - Hence $H ^ 3 _ c(\bar{\bar{T}} \setminus \bar{\bar{T}} _ 1, K _ {\bar{\bar{T}}}) \cong H ^ 2 _ c(\mathbb{A} ^ 1 _ s \setminus \{0, 1\}, \mathcal{L} _ {\chi(s)}) = 0$.

Therefore $\bar{\bar{\Phi}}$ is surjective, $\Phi$ is surjective, and $V _ \pi = 0$. **QED.**

**Exact Arithmetic Check (`CHECKED`):** [compute/t4_kummer_review_checks.py](compute/t4_kummer_review_checks.py) ([compute/t4_kummer_review_checks_out.txt](compute/t4_kummer_review_checks_out.txt)) verifies every trace identity of $\bar{\bar{T}}$ and $\bar{T}$ across 135 `(d, p, a)` triples ($d \in \{3, 5\}$, $p \le 97$, 0 failures).

---

### 3.2 Resolution of `K4C`'s Unexplained Coincidence `(iv)` — `PROVED` & `CHECKED`

In Round 2 `K4C-k4-computation.md` (lines 123 and 141), `K4C` observed that for all three cubics over $\mathbb{F} _ 3$ and all three fields $\mathbb{F} _ 9, \mathbb{F} _ {81}, \mathbb{F} _ {729}$, the three vectors $c = (1, 1, i)$, $(1, i, i)$, and $(i, 1, 1)$ ($i ^ 2 = -1$) produced identical values of $N _ 4$, and flagged this as unexplained.

**Explanation (`PROVED`).** For any $f \in \mathbb{F} _ p[x]$ and any $q = p ^ n$, $N _ k(c)$ is invariant under three exact symmetries of $c \in (\mathbb{F} _ q ^ *) ^ {k-1}$:
1. **Path reversal** $(x _ 1, \dots, x _ k) \mapsto (x _ k, \dots, x _ 1)$, sending $(c _ 1, \dots, c _ {k-1}) \mapsto (c _ {k-1}, \dots, c _ 1)$;
2. **Projective scaling** $c \mapsto \lambda c$ ($\lambda \in \mathbb{F} _ q ^ *$), leaving $\{Q _ c = 0\}$ unchanged;
3. **Frobenius** $x _ j \mapsto x _ j ^ p$, which satisfies $t(x ^ p) = t(x)$ (since $f \in \mathbb{F} _ p[x]$ and $\mathrm{Norm}(x ^ p) = \mathrm{Norm}(x)$) and sends $c \mapsto c ^ p$.

In characteristic 3 with $i ^ 2 = -1$ (so $i ^ 3 = -i$ and $(-i) ^ 3 = i$):

```math
(1, 1, i) \stackrel{\mathrm{rev}}{\to} (i, 1, 1),
```
```math
(1, 1, i) \stackrel{\times (-i)}{\to} (-i, -i, 1) \stackrel{\mathrm{Frob}}{\to} (i, i, 1) \stackrel{\mathrm{rev}}{\to} (1, i, i).
```

(In fact, for any field $q = p ^ n$ and $f \in \mathbb{F} _ p[x]$, the entire orbit under $\langle \text{scaling}, \text{reversal}, \text{Frob} _ p \rangle$ shares the exact same $N _ k$.)

**Exact Arithmetic Check (`CHECKED`):** [compute/t4_kummer_review_checks.py](compute/t4_kummer_review_checks.py) verifies the orbit algebra and reproduces `K4C`'s exact values over $\mathbb{F} _ 9$ (`193, 1, 97`) and $\mathbb{F} _ {81}$ (`769, 1057, 97`) with 0 failures.

---

### 3.3 Two Structural Gaps in `lean/ToyWeil/`

The Lean 4.34.1 files in [../lean/ToyWeil/](../lean/ToyWeil/) are cleanly proved with standard axioms only, but their **statements** do not match what footnote 3 actually requires:

1. **Unweighted quadric only.** [../lean/ToyWeil/Parseval.lean](../lean/ToyWeil/Parseval.lean) (and Round 2 `Identity.lean`) formalize only the plain all-ones quadric `pathQuadric x = ∑ i, x i.castSucc * x i.succ`. Yet [../reports/I-vanishing.md](../reports/I-vanishing.md) itself proved (`Theorem 4`) that $c = (1, 1, 1)$ **fails** $(S _ 4)$ in characteristic 3 (and fails non-characteristic restriction for depressed cubics). The formalization must carry arbitrary nonzero weights $c : \mathrm{Fin}\, n \to F$.
2. **All-$k$, base-field ($m = 1$) endgame only.** [../lean/ToyWeil/PowerSum.lean](../lean/ToyWeil/PowerSum.lean) states `endgame` with hypothesis `∀ k : ℕ, 2 ≤ k → ...` over all `n ≥ 1` with the *same* base $q$. Yet:
   - only **infinitely many** $k$ (specifically even $k = 2r$) are available ([../reports/H-referee.md](../reports/H-referee.md), Section 1.9);
   - at fixed $q$, the bad set of $c$ covers all of $(\mathbb{F} _ q ^ *) ^ {k-1}$ once $k$ grows (and in our Artin–Schreier toy case already at $k = 4, d = 3, p = 7$!), so $c$ must be chosen in a finite extension $\mathbb{F} _ {q ^ m}$ with $m = m(k) \ge 1$, giving a bound over $\mathbb{F} _ {q ^ {m n}}$ (equivalently replacing $\alpha _ i$ by $\alpha _ i ^ m$ and $q$ by $q ^ m$).

Both gaps are closed in our companion Lean 4 formalization: [lean/ArtinSchreierToy/WeightedParseval.lean](lean/ArtinSchreierToy/WeightedParseval.lean) and [lean/ArtinSchreierToy/ExtensionEndgame.lean](lean/ArtinSchreierToy/ExtensionEndgame.lean).

---

### 3.4 Minor Citations and Pivot to the Artin–Schreier Toy Case

1. **Lisseness of $V = R ^ 1 p _ ! K _ T$ off $S$ in `K4T`.** Sections 2 and 3 of `K4T-k4-theory.md` use that $V$ is lisse on $\mathbb{A} ^ 1 _ r \setminus S$ ($S = \{0\} \cup R'$) without citing the reason. The reason is standard and weight-free: over $\mathbb{A} ^ 1 _ r \setminus S$, the divisor $\{\infty\} \cup \{f(x) = 0\} \cup \{f(rx) = 0\} \subset \mathbb{P} ^ 1 _ x \times (\mathbb{A} ^ 1 _ r \setminus S)$ is a disjoint union of $2d + 1$ finite étale sections along which $\mathcal{L} _ {\chi(f(x)f(rx))}$ is tamely ramified ($p$ odd), so tame specialization (SGA 7 XIII / SGA 4½ *Th. finitude*) makes $R ^ 1 p _ ! K _ T$ lisse off $S$.
2. **Why the Kummer toy case stalls — and the pivot to our own toy case.** Comparing `FS` and `LIT` pinpoints the exact structural barrier: for $t(x) = \chi(f(x))$, the sheaf is *tame* at infinity, so pairs of $-1$ monodromies cancel on $D _ {ab} \subset (\mathbb{P} ^ 1) ^ k$ and prevent cleanness at infinity. Replacing the tame Kummer sheaf $\mathcal{L} _ \chi(f)$ with the **wildly ramified Artin–Schreier sheaf $\mathcal{L} _ \psi(f)$** ($d \ge 3, p \nmid 2d$) restores cleanness at infinity on $\overline{Y} \subset \mathbb{P} ^ k$ and makes footnote 3's sign-only route **close unconditionally and weight-free for all even $k \ge 4$** — see [ARTIN_SCHREIER_TOY_CASE.md](ARTIN_SCHREIER_TOY_CASE.md).
