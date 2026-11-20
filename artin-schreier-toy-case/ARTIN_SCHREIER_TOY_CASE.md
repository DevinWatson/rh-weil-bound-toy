# The Artin–Schreier Sign-Only Toy Case: Closing Footnote 3 Weight-Free for All Even $k \ge 4$

**Scope.** The Weil bound $|\sum _ {x \in \mathbb{F} _ q} \psi(f(x))| \le (d - 1)\sqrt{q}$ for polynomial exponential sums ($p \nmid d$) is a classical theorem (Weil 1948). This study constructs a **companion toy case** to the Kummer/hyperelliptic study in [../TOY_CASE.md](../TOY_CASE.md): replacing the tame quadratic Kummer sheaf $t(x) = \chi(f(x))$ with the **wildly ramified Artin–Schreier sheaf $t(x) = \psi(f(x))$** ($\deg f = d \ge 3$, $p \nmid 2d$). Nothing here says anything about the Riemann Hypothesis for the integers.

**Labels.** `PROVED` (complete proof given), `CITED` (standard theorem with primary source verified), `CHECKED` (exact integer / $\mathbb{Z}[\zeta _ p]$ / `Fraction` / Lean 4 verification, with file and output named), `OPEN`, `HINT`. **No proof below uses weights, purity, Weil I, or Weil II.** Weight language appears only when interpreting finite numerical data and is explicitly marked `(weights, interpretation only)`.

---

## 0. Headline Result and Comparison with the Kummer Toy Case

Why did footnote 3's sign-only route $q N = M ^ k + R$ stall at $k = 4$ ($q ^ {7/8}$) in the Kummer/hyperelliptic case ([../TOY_CASE.md](../TOY_CASE.md) and its Round 2 follow-up)?

As the Round 2 forget-supports analysis (`FS-forget-supports.md`, see [REVIEW_OF_TOY_CASE.md](REVIEW_OF_TOY_CASE.md)) showed, the Kummer sheaf $\mathcal{L} _ \chi(f)$ is **tame** at infinity with monodromy $-1$. On the closure of $Y = \{Q _ c = 0\}$ in $(\mathbb{P} ^ 1) ^ k$, pairs of non-adjacent coordinates at infinity form boundary divisors $D _ {ab}$ around which the monodromy $(-1)(-1) = +1$ cancels, so $K$ extends across infinity, **forget-supports fails**, and $H ^ k _ c(Y, K) = 0$ becomes an open global monodromy problem for all $k \ge 5$.

When we replace $\mathcal{L} _ \chi(f)$ by the **Artin–Schreier sheaf $\mathcal{L} _ \psi(f)$** ($d = \deg f \ge 3$, $p \nmid 2d$):
- On the **projective** quadric cone $\overline{Y} = \{Q _ c(X) = 0\} \subset \mathbb{P} ^ k$ ($k = 2m \ge 4$ even), $\overline{Y}$ is smooth along the boundary $\partial = \{Q _ c = 0\} \subset \mathbb{P} ^ {k-1}$.
- The degree-$d$ leading form $G _ d(X) = a _ d \sum _ {i=1} ^ k X _ i ^ d$ strictly dominates the degree-2 quadric $Q _ c$.
- Whenever $\partial$ intersects the Fermat hypersurface $\{G _ d = 0\} \subset \mathbb{P} ^ {k-1}$ **transversally**, the sheaf $K = \mathcal{L} _ \psi(\sum f(x _ i)) | _ Y$ is **clean at infinity** ($j _ ! K \cong R j _ * K$ on $\overline{Y}$), by a 4-line reduction to **Katz–Laumon Theorem 2.1.3 / Appendix 2.4** (verified weight-free in primary source `KL.txt`!).
- Therefore forget-supports $H ^ j _ c(Y, K) \cong H ^ j(Y, K)$ is an **isomorphism in all degrees**, and Artin vanishing on both sides (BBD 4.1.1 & 4.1.2, weight-free) proves **concentration $(S _ k)$: $H ^ j _ c(Y, K) = 0$ for all $j \ne k - 1$** for **every even $k \ge 4$**!
- Elementary algebra proves that the non-transversal locus $\mathcal{B} _ {k, d} \subset \mathbb{P} ^ {k-2} _ c$ has dimension $\le k - 3 < k - 2$ (and at $k = 4$ equals **precisely** the $d ^ 2$ lines $c _ 1 + \zeta _ 1 c _ 2 + \zeta _ 1 \zeta _ 2 c _ 3 = 0$ with $\zeta _ 1 ^ d = \zeta _ 2 ^ d = -1$).
- Passing to a finite extension $\mathbb{F} _ {q ^ m}$ containing a transversal $c \notin \mathcal{B} _ {k, d}$, weighted iterated Parseval and the subsequence extension-field endgame (both **formally verified in Lean 4**) yield $|\alpha _ i| \le q ^ {1/2 + 3/(2k)}$ for every even $k \ge 4$, hence **$|\alpha _ i| \le \sqrt{q}$** and **$|\sum _ {x \in \mathbb{F} _ q} \psi(f(x))| \le (d - 1)\sqrt{q}$**, **completely weight-free**.

| Feature | Kummer Toy Case (`toy-case`) | Artin–Schreier Toy Case (`artin-schreier-toy-case`) |
|---|---|---|
| Weight function $t(x)$ | $\chi(f(x))$, odd squarefree $d \ge 3$ | $\psi(f(x))$, $d \ge 3$, $p \nmid 2d$ |
| Ramification at $\infty$ | Tame (monodromy $-1$) | Wild (Swan conductor $d$, prime to $p$) |
| Natural compactification of $Y$ | Closure in $(\mathbb{P} ^ 1) ^ k$ | Projective quadric cone $\overline{Y} \subset \mathbb{P} ^ k$ |
| Clean at infinity ($j _ ! K \cong R j _ * K$)? | **NO** (fails on non-adjacent $D _ {ab}$) | **YES** (for all even $k \ge 4$ off $\mathcal{B} _ {k, d}$) |
| $(S _ k)$ proved weight-free? | $k = 2, 3, 4$ (`K4T` + our closure of `X2`); **$k \ge 5$ OPEN** | **ALL even $k \ge 4$** (`PROVED`) |
| Resulting bound on $|\alpha _ i|$ | Stalls at $q ^ {7/8}$ ($k = 4$) | **Full Weil bound $q ^ {1/2}$** ($k \to \infty$) |
| Exact $k = 4$ bad locus $\mathcal{B} _ {4, d}$ | `X1` ($c _ 2 + c _ 3 \rho + c _ 1 \rho' = 0$) $\subset$ `X4` (63 lines for $d = 3$) | Exactly $d ^ 2$ lines $c _ 1 + \zeta _ 1 c _ 2 + \zeta _ 1 \zeta _ 2 c _ 3 = 0$ ($\zeta _ i ^ d = -1$) |
| Small-field failure of plain $c = (1,1,1)$ | Char 3 ($1 + 1 + 1 = 0$) | Char 7 at $d = 3$ ($1 + 5 + 15 \equiv 0 \pmod 7$; in fact ALL 36 points of $(\mathbb{F} _ 7 ^ *) ^ 2$ lie on $\mathcal{B} _ {4, 3}$, forcing $\mathbb{F} _ {49}$!) |
| Closed-form middle Betti number | $92$ ($k = 4, d = 3$); general $k$ open | $2 \sum _ {j=1} ^ {k-1} (d - 1) ^ j + 1$ for **all even $k \ge 2$** ($5, 29, 125, \dots$ at $d = 3$) |
| Lean 4 formalization | Unweighted `pathQuadric`; all-$k$, $m = 1$ `endgame` | **Weighted** $Q _ c$, **subsequence + extension-field** `endgame_even_ext`, **algebraic transversality** (`base_locus_no_tangency`, `k4_bad_lines`, `k4_bad_plane`, `euler_char_identity`) |

---

## 1. Setting and Target Statement

Let $q = p ^ r$ be a power of an odd prime $p$, let $\psi : \mathbb{F} _ q \to \mathbb{C} ^ *$ be a nontrivial additive character, and let $f(x) = a _ d x ^ d + a _ {d-1} x ^ {d-1} + \dots + a _ 0 \in \mathbb{F} _ q[x]$ have degree $d \ge 3$ with $a _ d \ne 0$ and $p \nmid 2d$. Put

```math
t _ n(x) = \psi(\mathrm{Tr} _ {\mathbb{F} _ {q ^ n} / \mathbb{F} _ q}(f(x))), \qquad M _ n = \sum _ {x \in \mathbb{F} _ {q ^ n}} t _ n(x).
```

- **Rationality (`CITED`: Grothendieck–Lefschetz SGA 5 XV / SGA 4½ Rapport; Grothendieck–Ogg–Shafarevich SGA 5 X; no weights).** Let $\mathcal{L} = \mathcal{L} _ \psi(f)$ be the rank-1 Artin–Schreier sheaf on $\mathbb{A} ^ 1$. It is lisse on $\mathbb{A} ^ 1$, geometrically nontrivial, and wildly ramified at $\infty$ with Swan conductor $d$ (since $p \nmid d$). Hence $H ^ 0 _ c(\mathbb{A} ^ 1, \mathcal{L}) = H ^ 2 _ c(\mathbb{A} ^ 1, \mathcal{L}) = 0$ and $\dim H ^ 1 _ c(\mathbb{A} ^ 1, \mathcal{L}) = -\chi _ c(\mathbb{A} ^ 1, \mathcal{L}) = d - 1$. Writing $\alpha _ 1, \dots, \alpha _ {d-1} \in \mathbb{C}$ for the Frobenius eigenvalues on $H ^ 1 _ c(\mathbb{A} ^ 1 _ {\overline{\mathbb{F}} _ q}, \mathcal{L})$, we have

```math
M _ n = - \sum _ {i = 1} ^ {d - 1} \alpha _ i ^ n \qquad (\forall n \ge 1).
```

- **Target (Weil 1948):** $|\alpha _ i| \le \sqrt{q}$ for every $i$, hence $|M _ n| \le (d - 1) q ^ {n/2}$ for all $n \ge 1$.

For even $k = 2m \ge 4$ and $c = (c _ 1, \dots, c _ {k-1}) \in (\mathbb{F} _ {q ^ m} ^ *) ^ {k-1}$ (over an extension $\mathbb{F} _ {q ^ m}$), set

```math
Q _ c(x) = \sum _ {i = 1} ^ {k - 1} c _ i x _ i x _ {i + 1}, \qquad G(x) = \sum _ {i = 1} ^ k f(x _ i), \qquad Y = \{Q _ c = 0\} \subset \mathbb{A} ^ k, \qquad K = \mathcal{L} _ \psi(G) | _ Y,
```
```math
N _ n(c) = \sum _ {x \in Y(\mathbb{F} _ {q ^ {mn}})} \prod _ {i = 1} ^ k t _ {mn}(x _ i), \qquad S _ n(h) = \sum _ {x \in \mathbb{F} _ {q ^ {mn}} ^ k} \Bigl(\prod _ {i = 1} ^ k t _ {mn}(x _ i)\Bigr) \psi _ {mn}(h Q _ c(x)).
```

---

## 2. Complete Weight-Free Proof of the Weil Bound via $q N _ c = M ^ k + R _ c$

### Step 1. Weighted Identity and Iterated Parseval (`PROVED`, formalized in Lean 4)

Over any finite field $F$ of cardinality $Q = q ^ {mn}$ with nontrivial additive character $\psi$ and arbitrary $c \in (F ^ *) ^ {k-1}$ ($k \ge 2$):

```math
Q \cdot N(c) = M ^ k + R(c), \qquad R(c) = \sum _ {h \in F ^ *} S(h),
```
```math
|R(c)| \le (Q - 1) Q \cdot Q ^ {(k - 1) / 2} \le Q ^ {(k + 3) / 2}.
```

Formalized in [lean/ArtinSchreierToy/WeightedParseval.lean](lean/ArtinSchreierToy/WeightedParseval.lean) (`weighted_identity`, `weighted_identity_bound_one`, `weighted_identity_bound_weak`), using zero `sorry` and standard Lean axioms only.

### Step 2. Perversity and Artin Vanishing on $Y$ (`PROVED`, given `CITED` BBD 4.1.1–4.1.2)

For even $k = 2m \ge 4$ and all $c _ i \ne 0$, $Q _ c$ is nondegenerate ($\det(A _ c) = (-1) ^ m \prod c _ {2j-1} ^ 2 \ne 0$), so $Y = \{Q _ c = 0\} \subset \mathbb{A} ^ k$ is a reduced affine hypersurface of pure dimension $k - 1$ (smooth everywhere except the isolated cone vertex $0 \in Y$). Since $K = i ^ * \mathcal{L} _ \psi(G)$ is a single lisse rank-1 sheaf on $Y$ and the complement $u : \mathbb{A} ^ k \setminus Y \hookrightarrow \mathbb{A} ^ k$ is affine, the localization triangle $i _ * K[k - 1] \to u _ ! u ^ * (\mathcal{L} _ \psi(G)[k]) \to \mathcal{L} _ \psi(G)[k] \to +1$ together with $t$-exactness of $u _ !$ (BBD 4.1.1 & Cor. 4.1.2, weight-free) shows $K[k - 1] \in {} ^ p D ^ {[0, 1]}(Y)$; since $K$ sits in degree $-(k - 1)$ on $\dim Y = k - 1$, it also lies in ${} ^ p D ^ {\le 0}(Y)$, so $K[k - 1]$ is **perverse** on $Y$.

Applying Artin vanishing for perverse sheaves on the affine variety $Y$ (`CITED`: BBD Thm 4.1.1 & Cor. 4.1.2, opened in `BBD.txt`, weight-free):

```math
H ^ j _ c(Y, K) = 0 \quad (\forall j < k - 1), \qquad H ^ j(Y, K) = 0 \quad (\forall j > k - 1).
```

### Step 3. Local Cleanness Lemma for $w / z ^ d$ (`PROVED`, given `CITED` Katz–Laumon 2.4.1)

**Lemma 3.1 (Cleanness of $w / z ^ d$, `PROVED`, weight-free).** Let $p \nmid d$, $j _ z : \{z \ne 0\} \hookrightarrow \mathbb{A} ^ 2 _ {(z, w)}$, and $i _ z : \{z = 0\} \hookrightarrow \mathbb{A} ^ 2 _ {(z, w)}$. Then

```math
i _ z ^ * R j _ {z*} \mathcal{L} _ \psi(w / z ^ d) = 0 \quad \text{on } \{z = 0\}.
```

**Proof.** Let $\phi : \mathbb{A} ^ 2 _ {(z, w)} \to \mathbb{A} ^ 2 _ {(Z, w)}$ be $\phi(z, w) = (z ^ d, w)$. Since $\phi$ is finite and $\phi ^ {-1}(\{Z = 0\}) = \{z = 0\}$ set-theoretically, vanishing of $i _ z ^ * R j _ {z*} \mathcal{F}$ is equivalent to vanishing of $i _ Z ^ * \phi _ * R j _ {z*} \mathcal{F}$. Over $\{Z \ne 0\}$, $\phi ^ \circ$ is a finite étale $\mu _ d$-Galois cover ($p \nmid d$), so the projection formula gives

```math
\phi _ * R j _ {z*} \mathcal{L} _ \psi(w / z ^ d) = R j _ {Z*} \bigl( \phi ^ \circ _ * (\phi ^ \circ) ^ * \mathcal{L} _ \psi(w / Z) \bigr) \cong \bigoplus _ {\chi \in \widehat{\mu _ d}} R j _ {Z*} \bigl( \mathcal{L} _ \psi(w / Z) \otimes \mathcal{L} _ \chi(Z) \bigr).
```

Set $x = 1 / Z$, identifying $\mathbb{A} ^ 2 _ {(Z, w)}$ with the open neighborhood $\{x \ne 0\}$ of $\{\infty\} \times \mathbb{A} ^ 1 _ w$ inside $\mathbb{P} ^ 1 _ x \times \mathbb{A} ^ 1 _ w$, with $j _ \infty : \mathbb{A} ^ 1 _ x \times \mathbb{A} ^ 1 _ w \hookrightarrow \mathbb{P} ^ 1 _ x \times \mathbb{A} ^ 1 _ w$. For each $\chi \in \widehat{\mu _ d}$, define $K _ \chi \in D ^ b _ c(\mathbb{A} ^ 1 _ x, \overline{\mathbb{Q}} _ \ell)$ by $K _ 1 = \overline{\mathbb{Q}} _ \ell$ and $K _ \chi = j _ {0!} \mathcal{L} _ {\chi ^ {-1}}(x)$ for $\chi \ne 1$. Near $x = \infty$, $\mathrm{pr} _ 1 ^ * K _ \chi \otimes \mathcal{L} _ \psi(w x)$ coincides with $\mathcal{L} _ \psi(w / Z) \otimes \mathcal{L} _ \chi(Z)$.

By **Katz–Laumon (1985), Appendix (2.4), Theorem (2.4.1) Step (a)** (`CITED`, *Publ. IHES* 62, pp. 156–159; proved purely via translation, the Artin–Schreier cover $t ^ p - t = x y$, radicial factorization, and smooth base change — **no weights**!), the forget-supports arrow

```math
j _ {\infty !} \bigl( \mathrm{pr} _ 1 ^ * K _ \chi \otimes \mathcal{L} _ \psi(w x) \bigr) \longrightarrow R j _ {\infty *} \bigl( \mathrm{pr} _ 1 ^ * K _ \chi \otimes \mathcal{L} _ \psi(w x) \bigr)
```

is an **isomorphism** on $\mathbb{P} ^ 1 _ x \times \mathbb{A} ^ 1 _ w$ (and in particular its cone $i _ \infty ^ * R j _ {\infty *}(\cdots)$ vanishes identically on $\{\infty\} \times \mathbb{A} ^ 1 _ w$). Summing over $\chi \in \widehat{\mu _ d}$ gives $i _ Z ^ * \phi _ * R j _ {z*} \mathcal{L} _ \psi(w / z ^ d) = 0$, hence $i _ z ^ * R j _ {z*} \mathcal{L} _ \psi(w / z ^ d) = 0$. **QED.**

### Step 4. Cleanness at Infinity and Middle-Degree Concentration $(S _ k)$ (`PROVED`, weight-free)

Let $\overline{Y} = \{Q _ c(X _ 1, \dots, X _ k) = 0\} \subset \mathbb{P} ^ k$ be the projective closure of $Y$ (homogeneous coordinates $[X _ 1 : \dots : X _ k : Z]$), with open immersion $j : Y \hookrightarrow \overline{Y}$ and boundary $\partial = \overline{Y} \cap \{Z = 0\} = \{Q _ c(X) = 0\} \subset \mathbb{P} ^ {k-1}$. Because $k = 2m$ is even and all $c _ i \ne 0$, $\partial$ is a smooth projective quadric of dimension $k - 2$, and $\overline{Y}$ is smooth at every point of $\partial$ (the unique singular point $[0 : \dots : 0 : 1]$ lies in $Y$, disjoint from $\partial$).

**Theorem 4.1 (Forget-supports & $(S _ k)$, `PROVED`, weight-free).** Suppose $\partial = \{Q _ c(X) = 0\} \subset \mathbb{P} ^ {k-1}$ intersects the smooth Fermat hypersurface $F _ d = \{X _ 1 ^ d + \dots + X _ k ^ d = 0\} \subset \mathbb{P} ^ {k-1}$ **transversally**. Then:
1. $j _ ! K \to R j _ * K$ is an isomorphism in $D ^ b _ c(\overline{Y}, \overline{\mathbb{Q}} _ \ell)$;
2. the forget-supports map $H ^ j _ c(Y, K) \to H ^ j(Y, K)$ is an isomorphism for every $j \in \mathbb{Z}$;
3. **concentration $(S _ k)$ holds:** $H ^ j _ c(Y, K) = 0$ for all $j \ne k - 1$.

**Proof.** Rescaling $f$ by $a _ d ^ {-1}$ (absorbed into $\psi$ via $a _ d \ne 0$), write $G(X / Z) = H(X, Z) / Z ^ d$ where $H(X, Z) = \sum _ {i=1} ^ k X _ i ^ d + Z H _ 1(X, Z)$. Check the stalk $(R j _ * K) _ x$ at every point $x \in \partial$ in an affine chart $X _ {i _ 0} = 1$ with $z = Z / X _ {i _ 0}$ and $w = H(X / X _ {i _ 0}, z)$:
- **Case 1 ($x \in \partial \setminus F _ d$):** $w(x) \ne 0$ is a unit. Since $p \nmid d$, in an étale neighborhood of $x$, $w = v ^ d$ for a unit $v$, so putting $t = z / v$ puts $G = 1 / t ^ d$ in smooth local coordinates $(t, u _ 1, \dots, u _ {k-2})$. By smooth base change, $(R j _ * K) _ x$ is the stalk at $t = 0$ of $R j _ {t*} \mathcal{L} _ \psi(1 / t ^ d)$, which vanishes in all degrees ($I _ 0$ acts nontrivially on rank-1 $\mathcal{L} _ \psi(1/t ^ d)$, so both invariants $H ^ 0(I _ 0, -)$ and coinvariants $H ^ 1(I _ 0, -)$ vanish).
- **Case 2 ($x \in \partial \cap F _ d$):** $z(x) = w(x) = 0$. Because $w \equiv F _ d(X / X _ {i _ 0}) \pmod z$, the restriction of $dw | _ x$ to $T _ x \partial = \ker(dz | _ x)$ is nonzero precisely by transversality of $\partial$ and $F _ d$ at $x$. Thus $dz | _ x, dw | _ x$ are linearly independent in $\Omega ^ 1 _ {\overline{Y}, x}$ and extend to a regular system of local parameters $(z, w, u _ 1, \dots, u _ {k-3})$ giving an étale map $\pi : U _ x \to \mathbb{A} ^ 2 _ {(z, w)} \times \mathbb{A} ^ {k-3} _ u$ with $G = \pi ^ *(w / z ^ d)$. By smooth base change (SGA 4 XVI 1.2) and Lemma 3.1, $(R j _ * K) _ x = (R j _ {z*} \mathcal{L} _ \psi(w / z ^ d)) _ {(0, 0)} = 0$.

Thus $i ^ * R j _ * K = 0$ on $\partial$, so $j _ ! K \to R j _ * K$ is an isomorphism. Taking $R \Gamma(\overline{Y}, -)$ on the proper variety $\overline{Y}$ yields $H ^ j _ c(Y, K) = H ^ j(\overline{Y}, j _ ! K) \cong H ^ j(\overline{Y}, R j _ * K) = H ^ j(Y, K)$ for all $j$. Combining with Step 2 ($H ^ j _ c = 0$ for $j < k - 1$ and $H ^ j = 0$ for $j > k - 1$) yields $H ^ j _ c(Y, K) = 0$ for all $j \ne k - 1$. **QED.**

### Step 5. Existence of Transversal $c$ for Every Even $k \ge 4$ (`PROVED`, algebraic core in Lean 4)

**Theorem 5.1 (Properness of the bad locus $\mathcal{B} _ {k, d}$, `PROVED`, weight-free).** Let $p \nmid 2d$, $d \ge 3$, and $k = 2m \ge 4$ even. Let $T = \{[c] \in \mathbb{P} ^ {k-2} : \prod _ {i=1} ^ {k-1} c _ i \ne 0\}$ and let $\mathcal{B} _ {k, d} \subset T$ be the set of $[c]$ for which $\{Q _ c = 0\}$ fails to intersect $F _ d = \{\sum _ {i=1} ^ k X _ i ^ d = 0\}$ transversally in $\mathbb{P} ^ {k-1}$. Then:
1. $\mathcal{B} _ {k, d}$ is a Zariski-closed subset of $T$ of dimension **at most $k - 3 < k - 2 = \dim T$**; hence $T(\overline{\mathbb{F}} _ q) \setminus \mathcal{B} _ {k, d}(\overline{\mathbb{F}} _ q)$ is nonempty, and for every even $k \ge 4$ there exists a finite extension $\mathbb{F} _ {q ^ m}$ ($m = m(k) \ge 1$) and $c \in (\mathbb{F} _ {q ^ m} ^ *) ^ {k-1}$ with $[c] \notin \mathcal{B} _ {k, d}$.
2. **Exact $k = 4$ characterization:** $\mathcal{B} _ {4, d}$ is precisely the union of the $d ^ 2$ lines

```math
c _ 1 + \zeta _ 1 c _ 2 + \zeta _ 1 \zeta _ 2 c _ 3 = 0 \qquad (\zeta _ 1 ^ d = -1, \; \zeta _ 2 ^ d = -1).
```

**Proof.** The incidence locus $\mathcal{I} = \{(X, [c]) \in F _ d \times T : Q _ c(X) = 0, \; \mathrm{rank}[\nabla Q _ c(X) \mid \nabla F _ d(X)] \le 1\}$ is closed in $F _ d \times T$, so since $F _ d$ is proper, $\mathcal{B} _ {k, d} = \mathrm{pr} _ 2(\mathcal{I})$ is Zariski-closed in $T$.

For any $(X, [c]) \in \mathcal{I}$, nondegeneracy of $Q _ c$ gives $\nabla Q _ c(X) \ne 0$, so $\nabla Q _ c(X) = \lambda \nabla F _ d(X)$ with $\lambda \ne 0$. Rescaling $c$ sets $\lambda = 1 / d$ (valid since $p \nmid d$), yielding the system $\nabla Q _ c(X) = (X _ i ^ {d-1}) _ {i=1} ^ k$ in affine coordinates $(X, c) \in (\overline{\mathbb{F}} _ q ^ k \setminus \{0\}) \times (\overline{\mathbb{F}} _ q ^ *) ^ {k-1}$. Notice the weighted $\mathbb{G} _ m$-action $t \cdot (X, c) = (t X, t ^ {d-2} c)$ ($d - 2 \ge 1$) preserves this system, has 1-dimensional orbits (since $X \ne 0$), and maps each orbit to a single projective point $[c] \in T$.

Stratify solutions by the zero set $Z _ 0 = \{j \in \{1, \dots, k\} : X _ j = 0\}$, of size $s = |Z _ 0|$:
- **Base locus excluded (Lean: `base_locus_no_tangency`):** if $X _ i X _ {i+1} = 0$ for all $i$, no solution exists for any $c \in (\overline{\mathbb{F}} _ q ^ *) ^ {k-1}$.
- **Forbidden zero patterns:** if $1 \in Z _ 0$ (or $k \in Z _ 0$), or two adjacent indices lie in $Z _ 0$, or a nonzero coordinate is isolated between zeros, the linear equations $\nabla Q _ c(X) = (X _ i ^ {d-1})$ force a contradiction ($X = 0$). Hence $Z _ 0 \subset \{2, \dots, k - 1\}$ splits $\{1, \dots, k\}$ into $s + 1$ maximal contiguous nonzero blocks $B _ 0, \dots, B _ s$, each of length $L _ a \ge 2$.
- **Block equations:** on each block $B _ a = \{l _ a, \dots, r _ a\}$, multiplying $\nabla Q _ c(X) = (X _ i ^ {d-1})$ by $X _ i$ and putting $u _ i = c _ i X _ i X _ {i+1}$ is equivalent to:
  1. one alternating-sum equation $A _ a(X) := \sum _ {i = l _ a} ^ {r _ a} (-1) ^ {i - l _ a} X _ i ^ d = 0$ (Lean: `alternating_sum_mul_pathGrad` / `tangency_identities`), and
  2. explicit unique formulas $c _ i = \frac{1}{X _ i X _ {i+1}} \sum _ {r = l _ a} ^ i (-1) ^ {i - r} X _ r ^ d$ for the $L _ a - 1$ internal coefficients $c _ i$ ($l _ a \le i < r _ a$).
  At each zero $j \in Z _ 0$, equation $j$ gives $c _ j = -c _ {j-1} X _ {j-1} / X _ {j+1}$, leaving 1 free scalar $c _ {j-1} \in \overline{\mathbb{F}} _ q ^ *$. Summing over all blocks gives $2 Q _ c(X) = F _ d(X)$, so $Q _ c(X) = 0$ is automatic from $F _ d(X) = 0$ ($p \ne 2$).
- **Dimension count:** on $(\overline{\mathbb{F}} _ q ^ *) ^ {k - s}$, the $s + 2$ equations $A _ 0(X) = \dots = A _ s(X) = F _ d(X) = 0$ have Jacobian of full rank $s + 2$ at every point (since $p \nmid 2d$, $L _ a \ge 2$, and $X _ i \ne 0$ on each disjoint block $B _ a$), defining a smooth locus $V _ {Z _ 0}$ of dimension $(k - s) - (s + 2) = k - 2s - 2$. Adding the $s$ free scalars $(c _ {j-1}) _ {j \in Z _ 0}$ gives $\dim W _ {Z _ 0} \le k - s - 2$. Dividing out the 1-dimensional $\mathbb{G} _ m$-orbits $t \cdot (X, c) = (t X, t ^ {d-2} c)$ shows that the image in $T \subset \mathbb{P} ^ {k-2}$ has dimension

```math
\dim \mathrm{im}(W _ {Z _ 0}) \le (k - s - 2) - 1 = k - s - 3 \le k - 3 < k - 2 = \dim T.
```

Taking the finite union over all zero sets $Z _ 0$ gives $\dim \mathcal{B} _ {k, d} \le k - 3 < \dim T$.
- **Exact $k = 4$ case (Lean: `k4_bad_lines` & `k4_bad_plane`):** for $k = 4$, $3s + 2 \le 4$ forces $s = 0$ (all $X _ i \ne 0$), $X _ 1 ^ d + X _ 3 ^ d = X _ 2 ^ d + X _ 4 ^ d = 0$ gives $\zeta _ 1 = X _ 3 / X _ 1$, $\zeta _ 2 = X _ 4 / X _ 2$ with $\zeta _ i ^ d = -1$, and dividing $Q _ c(X) = 0$ by $X _ 1 X _ 2$ yields $c _ 1 + \zeta _ 1 c _ 2 + \zeta _ 1 \zeta _ 2 c _ 3 = 0$. Conversely, on any such line the 2-plane $(u, v, \zeta _ 1 u, \zeta _ 2 v)$ lies in $Y \cap \{F _ d = 0\}$, and its projective line at infinity is tangent to $F _ d$ where $c _ 1 v ^ 3 + c _ 3 \zeta _ 1 ^ 2 \zeta _ 2 u ^ 3 = 0$ (more generally $c _ 1 v ^ d = -c _ 3 \zeta _ 1 ^ {d-1} \zeta _ 2 u ^ d$). **QED.**

### Step 6. Trace Formula, No Cancellation, and Weil Bound (`PROVED`, endgame in Lean 4)

Fix any even $k = 2r \ge 4$. By Step 5, pick $m = m(k) \ge 1$ and $c \in (\mathbb{F} _ {q ^ m} ^ *) ^ {k-1}$ with $[c] \notin \mathcal{B} _ {k, d}$. By Step 4, $H ^ j _ c(Y, K) = 0$ for all $j \ne k - 1$. By the Grothendieck–Lefschetz trace formula and Künneth (no weights):
- $M _ {mn} ^ k = (-1) ^ k \sum _ {I : \mathrm{Fin}\, k \to \mathrm{Fin}(d-1)} \bigl((\prod _ j \alpha _ {I(j)}) ^ m\bigr) ^ n$,
- $q ^ {mn} N _ {mn}(c) = (-1) ^ {k - 1} \sum _ {\beta \in E} \beta ^ n$, where $E$ is the finite multiset of Frobenius eigenvalues of $H ^ {k-1} _ c(Y _ {\overline{\mathbb{F}} _ q}, K)(-1)$ over $\mathbb{F} _ {q ^ m}$.

Hence $R _ {mn}(c) = q ^ {mn} N _ {mn}(c) - M _ {mn} ^ k = (-1) ^ {k - 1} \Bigl(\sum _ I \bigl((\prod _ j \alpha _ {I(j)}) ^ m\bigr) ^ n + \sum _ {\beta \in E} \beta ^ n\Bigr)$ has **all exponentials entering with the same sign $(-1) ^ {k-1}$**. By Step 1 (`weighted_identity_bound_weak`),

```math
\left| \Bigl(\sum _ I \bigl((\prod _ j \alpha _ {I(j)}) ^ m\bigr) ^ n\Bigr) + \sum _ {\beta \in E} \beta ^ n \right| = |R _ {mn}(c)| \le \bigl((q ^ m) ^ {(k + 3) / 2}\bigr) ^ n \qquad (\forall n \ge 1).
```

Applying [lean/ArtinSchreierToy/ExtensionEndgame.lean](lean/ArtinSchreierToy/ExtensionEndgame.lean) (`endgame_even_ext` and `weil_bound_of_even_ext`) over all even $k = 2r$ ($r \ge 2$) gives:

```math
|\alpha _ i| \le \sqrt{q} \quad (\forall i = 1, \dots, d - 1), \qquad |M _ n| = \left| \sum _ {x \in \mathbb{F} _ {q ^ n}} \psi(\mathrm{Tr}(f(x))) \right| \le (d - 1) q ^ {n / 2}. \qquad \text{\textbf{QED.}}
```

---

## 3. Closed-Form Middle Betti Number for All Even $k$ (`PROVED` & `CHECKED`)

**Theorem 3.1 (`PROVED`, weight-free).** For every even $k = 2m \ge 2$, every $f$ of degree $d \ge 3$ with $p \nmid 2d$, and every transversal $c \notin \mathcal{B} _ {k, d}$:

```math
\dim H ^ {k - 1} _ c(Y, K) = (-1) ^ {k - 1} \chi _ c(Y, K) = 2 \sum _ {j = 1} ^ {k - 1} (d - 1) ^ j + 1 = \frac{2 (d - 1) ^ k - d}{d - 2}.
```

In particular, $\dim H ^ {k-1} _ c(Y, K)$ is **independent of all lower-order coefficients of $f$**:
- $d = 3$: $5, 29, 125, 509, 2045, \dots, 2 ^ {k+1} - 3$;
- $d = 5$: $9, 169, 2729, 43689, 699049, \dots$.

**Proof.**
1. *Deformation to $G _ d$.* On $\overline{Y} \times \mathbb{A} ^ 1 _ t$ consider $G _ t(x) = \sum _ {i=1} ^ k t ^ d f(x _ i / t) = a _ d \sum X _ i ^ d + t (\cdots)$. Because its leading form at infinity is constant in $t$ and transversal to $\partial$, Katz–Laumon Theorem 2.4.4 (universal strong local acyclicity along $\partial \times \mathbb{A} ^ 1 _ t$, `KL.txt` line 668, weight-free) implies $R ^ j \mathrm{pr} _ {t!} \mathcal{L} _ \psi(G _ t)$ is lisse on $\mathbb{A} ^ 1 _ t$, so $\chi _ c(Y, \mathcal{L} _ \psi(G)) = \chi _ c(Y, \mathcal{L} _ \psi(G _ d))$.
2. *Milnor-fibre projection $G _ d : Y \to \mathbb{A} ^ 1 _ s$.* Over $s = 0$, $Y _ 0 = \{Q _ c = 0, G _ d = 0\}$ is the affine cone over $Z = \partial \cap \{G _ d = 0\}$, so $\chi _ c(Y _ 0) = 1 + \chi _ c(\mathbb{G} _ m) \chi(Z) = 1$. Over $\mathbb{G} _ m$, the fibre $Y _ s \cong Y _ 1$ is a smooth finite étale $\mu _ d$-cover of $\partial \setminus Z$, tamely ramified along $0, \infty$; by Grothendieck–Ogg–Shafarevich on $\mathbb{G} _ m$, each tame lisse sheaf $\mathcal{E} ^ b = R ^ b G _ {d!} \overline{\mathbb{Q}} _ \ell | _ {\mathbb{G} _ m}$ satisfies $\chi _ c(\mathbb{G} _ m, \mathcal{E} ^ b \otimes \mathcal{L} _ \psi(s)) = -\mathrm{rk}(\mathcal{E} ^ b)$. Hence

```math
\chi _ c(Y, \mathcal{L} _ \psi(G _ d)) = 1 - \chi _ c(Y _ 1) = 1 - d \bigl(\chi(\partial) - \chi(Z)\bigr).
```

3. *Chern-class evaluation.* For the smooth quadric $\partial \subset \mathbb{P} ^ {2m-1}$ and the smooth $(2, d)$ complete intersection $Z = \partial \cap F _ d$, putting $u = d - 1$:
   - $\chi(\partial) = 2m$,
   - $\chi(Z) = 2 d [h ^ {2m-3}] \frac{(1 + h) ^ {2m}}{(1 + 2h)(1 + dh)} = 2(u + 1) [t ^ {2m-3}] \frac{1}{(1 - t) ^ 2 (1 + t)(1 + u t)} = 2m - 2 \frac{u ^ {2m} - 1}{u ^ 2 - 1}$ (via $t = h/(1 + h)$ and partial fractions).
   Substituting gives $\chi _ c(Y, K) = 1 - (u + 1) \cdot 2 \frac{u ^ {2m} - 1}{u ^ 2 - 1} = 1 - 2 \frac{u ^ {2m} - 1}{u - 1} = -\bigl(2 \sum _ {j=1} ^ {2m-1} u ^ j + 1\bigr)$. The algebraic equivalence with $\frac{2(d - 1) ^ k - d}{d - 2}$ is formally verified in Lean (`euler_char_identity`), and the Chern-class expansion is verified in [compute/t3_ext_and_betti.py](compute/t3_ext_and_betti.py) for $d \in \{3, 4, 5\}$, $k \in \{2, 4, 6, 8, 10\}$. **QED.**

*(Independent $k = 4$ cross-check via the Segre fibration: on $T = \mathbb{A} ^ 2 _ {(x, r)}$ with $f(x) + f(rx)$, $\chi _ c(T) = d ^ 2 - d + 1$, giving total drop $\sum (\mathrm{deficit} _ s + \mathrm{Sw} _ s + h ^ 2 _ s) = d ^ 2$ regardless of lower-order terms of $f$ — e.g. $\mathrm{Sw} _ \zeta = d - 1$ for generic $f$ vs $\mathrm{Sw} _ \zeta = 0, h ^ 2 _ \zeta = 1$ for $f = x ^ d$ — and $\chi _ c(Y, K) = -1 + 2(d - 1) ^ 2 - 2(d - 1) d ^ 2 = -(2 d ^ 3 - 4 d ^ 2 + 4 d - 1) = -(2(u ^ 3 + u ^ 2 + u) + 1)$, matching identically!)*

---

## 4. Exact Cyclotomic Computation (`CHECKED`)

All computations use exact arithmetic in $\mathbb{Z}[\zeta _ p] = \mathbb{Z}[T] / (1 + T + \dots + T ^ {p-1})$ and exact `Fraction` averages $\mathrm{AvgSq}(c) = \frac{1}{p - 1} \sum _ {a = 1} ^ {p - 1} |N _ k(c; \psi _ a)| ^ 2$ (zero floating-point certificates; floats appear only in display columns). Scripts live in [compute/](compute/).

| Check | Result (`CHECKED`, 0 failures) | Script & Output |
|---|---|---|
| DP vs brute force + $p N _ k = M ^ k + R _ k$ + Galois-avg Parseval ($k = 2, 3, 4$, $p = 5, 7$, 4 polynomials) | 72 cases, **0 failures** | [compute/t1_validate.py](compute/t1_validate.py), [compute/t1_validate_out.txt](compute/t1_validate_out.txt) |
| Closed forms $N _ 2 = 2 t _ 0 M - t _ 0 ^ 2$, $N _ 3 = t _ 0 M ^ 2 + (M - t _ 0) C(-c _ 1 / c _ 2)$, Segre $N _ 4 = -p t _ 0 ^ 4 + t _ 0 ^ 2 M ^ 2 + \sum C(r) C(\tau(r))$ ($p = 5, 7, 11$) | 144 cases, **0 failures** | [compute/t1_validate_out.txt](compute/t1_validate_out.txt) |
| Extension-field `FiniteField` Segre $N _ 4$ vs brute force over $\mathbb{F} _ 9$ ($d = 5$) | 8 cases, **0 failures** | [compute/t1_validate_out.txt](compute/t1_validate_out.txt) |
| **Spotlight $p = 7, d = 3$**: all 36 points of $(\mathbb{F} _ 7 ^ *) ^ 2$ lie on the 9 bad lines $\mathcal{B} _ {4, 3}$; plain $c = (1, 1, 1)$ hits $(\zeta _ 1, \zeta _ 2) = (5, 3)$ ($1 + 5 + 15 = 21 \equiv 0 \pmod 7$), giving $\mathrm{AvgSq}(1, 1, 1) = 9506 \approx 3.959 \, p ^ 4$ for $f = x ^ 3$. Passing to $\mathbb{F} _ {49} = \mathbb{F} _ 7[u]/(u ^ 2 + 1)$, transversal $c = (1, u, 1)$ drops $\mathrm{AvgSq} / q ^ 4$ from $1.2703$ to $0.0796$ ($3.898 \, q ^ 3$)! | Exact match with Theorem 5.1 & extension necessity | [compute/t2_k4_bad_locus.py](compute/t2_k4_bad_locus.py), [compute/t2_k4_bad_locus_out.txt](compute/t2_k4_bad_locus_out.txt), [compute/t3_ext_and_betti_out.txt](compute/t3_ext_and_betti_out.txt) |
| Exhaustive $k = 4$ scan across $p \in [5, 31]$ + fixed-$c$ scan across 15 primes $p \in [37, 101]$ | For odd $f = x ^ 3 + x$ on $p \in [37, 101]$: good $c$ has mean $\mathrm{AvgSq}/p ^ 3 = 3.081$ (max $4.266$), while bad $c = (1, 2, 1)$ ($c _ 1 - c _ 2 + c _ 3 = 0$) has mean $\mathrm{AvgSq}/p ^ 4 = 1.0190$ ($[0.963, 1.078]$). For $f = x ^ 3$, **all 9** $\mathbb{F} _ p$-bad lines have $\mathrm{AvgSq} \sim p ^ 4$. | [compute/t2_k4_bad_locus_out.txt](compute/t2_k4_bad_locus_out.txt) |
| Extension tower $\mathbb{F} _ {5 ^ n}$ ($n = 1..4$, $q = 5, 25, 125, 625$) for $k = 4, d = 3$ | Transversal $c = (1, 1, 1)$ stays bounded in $q ^ 3$ ($f = x ^ 3 + x$: $\mathrm{AvgSq}/q ^ 3 = 12.30, 8.70, 11.29, 8.45$, $\mathrm{AvgSq}/q ^ 4 \to 0.0135$), while bad $c = (1, 2, 1)$ stays $O(q ^ 4)$ ($2.46, 1.09, 0.49, 0.96$). Every good case satisfies $\mathrm{AvgSq} \le 29 ^ 2 q ^ 3$. | [compute/t3_ext_and_betti.py](compute/t3_ext_and_betti.py), [compute/t3_ext_and_betti_out.txt](compute/t3_ext_and_betti_out.txt) |
| Exact $k = 6$ DP over $\mathbb{F} _ 5$ ($p N _ 6 = M ^ 6 + R _ 6$, explicit tangency-bad $c = (3, 1, 4, 1, 3) \in \mathcal{B} _ {6, 3}(\mathbb{F} _ 5)$ at $X = (1, 2, 1, 1, 2, 1)$) | 9 cases, **0 failures** on identity & Parseval bound $\mathrm{AvgSq}(R _ 6) \le 16 \cdot 5 ^ 7$ | [compute/t3_ext_and_betti_out.txt](compute/t3_ext_and_betti_out.txt) |
| Exact Milnor-fibre `#Y, #Y_0, #Z(F_p)` counts ($p = 5, 11, 13$) & Chern-class Betti verification ($d = 3, 4, 5$, $k = 2..10$) | All 15 $(d, k)$ Betti numbers match $\dim H ^ {k-1} _ c = 2\sum _ {j=1} ^ {k-1}(d-1) ^ j + 1$ exactly; **0 failures** | [compute/t3_ext_and_betti_out.txt](compute/t3_ext_and_betti_out.txt) |

---

## 5. Lean 4.34.1 Formalization (`CHECKED`)

Compiled against Mathlib (Lean 4.34.1) via [tools/lean_check.sh](tools/lean_check.sh). Every module is checked with zero `sorry`, zero custom axioms, and zero `native_decide` (all `#print axioms` lines depend solely on `[propext, Classical.choice, Quot.sound]`).

1. **[lean/ArtinSchreierToy/WeightedParseval.lean](lean/ArtinSchreierToy/WeightedParseval.lean)** ([log](lean/logs/ArtinSchreierToy.WeightedParseval.log)):
   - `weightedPathQuadric c x`, `orthogonality`, `parseval_step` (for arbitrary nonzero scaling `a ≠ 0`),
   - `weighted_iterated_bound`, `weighted_iterated_bound_rpow`, `weightedSsum_eq_path_sum`,
   - `weighted_identity` (`q * N_c = M^{n+1} + R_c`), `weighted_identity_bound_one`, `weighted_identity_bound_weak` (`‖q * N_c - M^k‖ ≤ q^((k+3)/2)` for all nonzero `c : Fin n → F` and `‖t‖ ≤ 1`).
2. **[lean/ArtinSchreierToy/ExtensionEndgame.lean](lean/ArtinSchreierToy/ExtensionEndgame.lean)** ([log](lean/logs/ArtinSchreierToy.ExtensionEndgame.log)):
   - `no_hidden_growth`, `no_cancellation`, `le_sqrt_of_subseq_rpow`,
   - `endgame_subseq_ext` (handles **both** an arbitrary unbounded subsequence of $k$ and an arbitrary $k$-dependent extension degree $m = m(k) \ge 1$),
   - `endgame_even_ext` (specialized to even $k = 2r$),
   - `weil_bound_of_even_ext` (`‖- ∑ i, α i ^ n‖ ≤ d * (Real.sqrt q) ^ n`).
3. **[lean/ArtinSchreierToy/Transversality.lean](lean/ArtinSchreierToy/Transversality.lean)** ([log](lean/logs/ArtinSchreierToy.Transversality.log)):
   - `sum_mul_pathGrad` (`∑ X_i (∇Q_c)_i = 2 Q_c(X)`),
   - `alternating_sum_mul_pathGrad` (`∑ (-1)^i X_i (∇Q_c)_i = 0`),
   - `tangency_identities`,
   - `base_locus_transversal` & `base_locus_no_tangency` (for every even $k = 2(m+1)$, $d \ge 2$, nonzero $c$, and nonzero base-locus point $X$, $\nabla Q _ c(X)$ and $\nabla F _ d(X)$ are linearly independent),
   - `k4_bad_lines` & `k4_bad_plane` (exact characterization of $\mathcal{B} _ {4, d}$ as the $d ^ 2$ lines $c _ 0 + \zeta _ 1 c _ 1 + \zeta _ 1 \zeta _ 2 c _ 2 = 0$ with $\zeta _ i ^ d = -1$),
   - `euler_char_identity` (`(d - 2) * (2 * ∑_{j=1}^{k-1} (d - 1)^j + 1) = 2 * (d - 1)^k - d`).

*(What is NOT formalized in Lean 4: the $\ell$-adic cohomology machinery — Grothendieck–Lefschetz, Künneth, BBD Artin vanishing, and Katz–Laumon Theorem 2.4.1 — and the Zariski-dimension argument of Theorem 5.1 for $k \ge 6$. Those are proved/cited on paper in Section 2, with zero weights or purity anywhere.)*

---

## 6. Paper Inputs and Weight-Free Audit

Every external theorem used in Section 2 is **weight-free**:

| Citation | Exact Statement Used | Weight-Free Status |
|---|---|---|
| SGA 5 XV; SGA 4½ *Rapport* | Grothendieck–Lefschetz trace formula | Weight-free (`CITED`) |
| SGA 4 XVII 5.4.3 | Künneth for compactly supported cohomology | Weight-free (`CITED`) |
| SGA 5 X 7.1 (Raynaud, Bourbaki 286) | Grothendieck–Ogg–Shafarevich on $\mathbb{A} ^ 1$ and $\mathbb{G} _ m$ | Weight-free (`CITED`) |
| SGA 4 XVI 1.2 | Smooth base change | Weight-free (`CITED`) |
| BBD, *Astérisque* 100 (1982), Thm 4.1.1 & Cor. 4.1.2 | Artin vanishing & $t$-exactness of affine $Rf _ *$, $Rf _ !$ | Weight-free (`CITED`, primary text checked) |
| Katz–Laumon, *Publ. IHES* 62 (1985), Thm 2.1.3, Appendix (2.4) Thm 2.4.1 & 2.4.4 (= Laumon, *Publ. IHES* 65 (1987), Thm 1.3.1.1) | Forget supports $j _ {\infty !} \cong R j _ {\infty *}$ for $\mathcal{L} _ \psi(xy)$ and universal strong local acyclicity | Weight-free (`CITED`, primary text checked, pp. 156–160) |

**Not used:** Deligne's Weil I, Weil II, weights, purity, equidistribution, big monodromy, or the Weil bound itself.
