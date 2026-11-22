# A2. Dependency and weight audit of Laumon 1987, chapters 1 and 2

Agent A2, round four. Written 2026-11-21 (UTC, `date -u` 22:54 at start, 23:05 at end).
Subject: G. Laumon, "Transformation de Fourier, constantes d'equations fonctionnelles et conjecture de Weil",
Publ. Math. IHES 65 (1987), 131-210. This is about character sums over finite fields. Nothing here says anything
about the Riemann Hypothesis for the integers.

Conventions of this report
- "j.p." = journal page; the PDF page is j.p. - 129. Every statement of Laumon is paraphrased in my own words; no
  passage is copied, no image is copied (two crops were made transiently in the scratchpad for reading at higher
  resolution and deleted at once).
- Labels: PROVED (argument given here), CITED (statement number, page, and where read), CHECKED (exact arithmetic,
  script named), OPEN, HINT. "READ (img)" = read on the page image by me. "READ (dump)" = read in a local text
  dump of round two (`../round2/compute/LIT/`), which is OCR for KL.txt, BBD.txt, LAU.txt and extracted PDF text
  for SGA4h.txt; named each time it is relied on.
- I read the page images myself for PDF pages 3-7, 10-25, 26-40, 49, 74, 75, 80, 81 (every statement and proof of
  chapters 1 and 2 that the induction can touch, except the items listed in section 7). I did not read 2.6, 2.7
  (PDF 41-48), chapter 3 beyond its first page and its last page, or chapter 4 beyond 4.1.
- Floating point is not used anywhere. The only computation is `compute/A2/check_bookkeeping.py` (exact
  `Fraction` arithmetic, output `compute/A2/check_bookkeeping_out.txt`).

## 0. Summary of answers (details below)

1. **Weights, purity, Weil II.** In every proof of chapters 1 and 2 that I read on the images, and in the outside
   proofs I could open (Katz-Laumon 2.4.1-2.4.4 in the KL dump, BBD chapter 4 in the BBD dump, Sommes trig. 4.3
   and 4.20 in the SGA 4 1/2 dump), no weight, no purity in the sense of Deligne, and no Weil bound is used.
   The word "pur" in chapters 1-3 means "purely of relative dimension r" or "purely of slope lambda" (PDF pages 18,
   23, 25, 30) or Langlands' "purely local" (PDF 56). Weil II appears only as the reference [De 4] for the
   formalism of l-adic sheaves (section 1 of that paper) in sections 0 and 1.1 and in a notation remark in 2.1.1
   (PDF 5, 6, 7, 22). Weights first appear in the introduction (PDF 3-4, announcing chapter 4) and in the text at
   chapter 4, definition 4.1.2 (j.p. 204, PDF 75). Exceptions to "read": Gabber-Katz (not opened), Deligne-Laumon
   semicontinuity (not opened), SGA 7 XIII 2.1.7.1 and SGA 4 1/2 Th. finitude 2.16 (cited statements only; see
   table). **PROVED/CITED for what I read; NOT a statement about what I did not open.**
2. **Tame case and Gabber-Katz.** Section 2.5.3 (tame modules) and its proposition 2.5.3.1 do NOT use Gabber-Katz;
   I read the proof (j.p. 166-167). Gabber-Katz (2.2.2.2) is used in 2.5.4, 2.5.5, 2.5.6 (j.p. 167-169) and
   presumably 2.7. Round three's report B says "2.5.3 uses Gabber-Katz": that is a misreading. BUT the toy's
   modules are not all tame: P_i at infinity contains slope-1 blocks L_psi(a x) tensor (tame). The vanishing of
   F^(inf,inf') on such blocks is theorem 2.4.3 (iii)b, whose printed proof (2.5.4) uses Gabber-Katz. I give
   (section 4) a replacement for the toy's blocks that uses only 2.2.2.1 and a dimension count, plus a second
   argument by a rank count. Both are mine, unrefereed: label PROVED-by-A2, to be checked by B2.
3. **Round-three misreadings.** (a) The slope maps s/(1+s), s/(1-s), s/(s-1) are RIGHT (page 163-164 formulas
   r' = r+s, r-s, s-r with s' = s; CHECKED). (b) Round three D wrote that F^(inf,0') vanishes on slopes in ]1,inf[;
   the page says [1,inf[ (confirmed on a 200 dpi crop). (c) B says 2.5.3 uses Gabber-Katz: wrong. (d) B's L8 drops the term
   H^0(K'_s') of the exact sequence of 2.3.2 (the page has a four-term sequence); harmless for T3 sheaves. (e) D's
   rendering of F^(inf,0')(V_chi) as "Kummer module of chi^-1 tensor G(chi,psi)" is not what 2.5.3.1(ii) prints (it
   prints V'_chi tensor G(chi^-1, psi)). (f) The semicontinuity inequality read as ">=" is wrong in direction: see
   section 5.3. (g) A gap that nobody listed: 2.4.2.1 is stated for K with pi^*K = V_!(1) (extension by zero), while
   the sheaves of the induction are middle extensions; see section 4.2.

## 1. Where the chapters begin, where weights first appear

| part | j.p. | PDF page | note |
|---|---|---|---|
| Introduction | 131-134 | 2-5 (top) | mentions Deligne's theorem on weights (j.p. 132, PDF 3) and the purity criterion (j.p. 133, PDF 4) as ingredients of chapter 4 |
| 0. Notations | 134-136 | 5-7 | (0.6): D^b_c(X, Qbar_l) is defined by Deligne [De 4] (1.1.2); t-structures need Gabber/Ekedahl, unpublished at the time, avoided by (*) (k finite or alg. closed suffices) |
| 1. La transformation de Fourier-Deligne | begins j.p. 136 (bottom) | 7 | 1.1 j.p. 136-140; 1.2 j.p. 141-146 (PDF 12-17); 1.3 j.p. 146-147; 1.4 j.p. 148-150 |
| 2. Transformations de Fourier locales | begins j.p. 150 (bottom) | 21 | 2.1 j.p. 150-155; 2.2 j.p. 155-157; 2.3 j.p. 157-161 (PDF 28-32); 2.4 j.p. 161-164 (PDF 32-35); 2.5 j.p. 165-169 (PDF 36-40); 2.6 j.p. 170 on (PDF 41); 2.7 j.p. 174 on (PDF 45) |
| 3. Formules du produit | begins j.p. 178 (middle) | 49 | |
| 4. Another proof of Deligne's main theorem | begins j.p. 203 (bottom) | 74 | weights: def. 4.1.2 (iota-pure, iota-weights) j.p. 204 (PDF 75); Deligne's theorem 4.1.3 recalled; purity criterion 4.2.1 |
| Bibliography | 209-210 | 80-81 | [De 4] = La conjecture de Weil II, Publ. IHES 52; [Ka 2] = Katz, Extensions of representations of fundamental groups, Ann. Inst. Fourier (to appear in 1987); [Ka-La] = Katz-Laumon, Publ. IHES 62; [Lau 3] = Laumon, Semi-continuite du conducteur de Swan, Asterisque 82-83 |

Text-layer search (OCR, a search not a reading): "poids" occurs on PDF 3 (introduction) and 75-79 (chapter 4)
only; "pur" on PDF 4, 18, 23, 25, 30, 56 (all "purement ...", see above) and 75-79. `[De 4]` occurs on PDF 5-7, 22
(formalism, read), 70 (section 3.6, not read), 74-76, 80.

## 2. Sign convention that the draft must respect (found while reading, not on any list)

For a perverse sheaf K, Laumon's r(K), r_x(K), s_x(K), a_x(K) are the numbers of the COMPLEX, so for K = F[1] with
F a sheaf they are the NEGATIVES of the sheaf quantities (rank, stalk rank, Swan, total drop). Evidence: 2.2.1.1
(j.p. 155) states a_x(K) <= r(K) - r_x(K) <= 0 for perverse K; and 2.3.1.1(i) (j.p. 158) reads r(K') = sum
deg(s) a_s(K) + [term from slopes > 1], which is <= 0 for K' = F'[1]. Translating to sheaf quantities (rank rho of
F', drop-plus-Swan A_s of F at s): rho = sum_s deg(s) A_s + (s - r)(slopes > 1 part), and the stalk of F' at s' != 0'
drops from rho by r(V_1) - s(V_1 tensor L(x.s')) (the formula (ii) with both sides negated), where V_1 is the
slope-1 part of F at infinity. The main-session notes copy the formulas without this remark; the draft uses positive
ranks (r_1 = 1, r_2 = d) so it is on the sheaf convention, which is consistent as long as the translation is made.
Not an error, a trap. I checked the signs on the whole chain in section 4.3.

## 3. The dependency table

Columns: "rests on" = earlier statements of the paper used in the proof as printed; "outside" = other sources;
"W?" = whether weights, purity or Weil II enter (as read); "toy" = used by the induction S5 / by S4 (Y = needed,
N = not needed, M = needed only in the tame/blocks form). Journal page, then (PDF page).

### 3.1 Chapter 0 and 1

| statement | j.p. (PDF) | what it says (my words) | rests on | outside | W? | toy |
|---|---|---|---|---|---|---|
| 0.5-0.9 formalism | 134-136 (5-7) | D^b_c(X, Qbar_l), functors, trace function, Frobenius | definitions | [De 4] 1.1.x (formalism only), [SGA 4] XIV, XVII, [SGA 4 1/2] Th. finitude, SGA 7 XIII, Rapport (trace formula), BBD 2.2, 4.3.1 | no | Y |
| 0.6 | 135 (6) | t-structure on D^b_c needs a hypothesis (*); automatic for k finite or alg. closed | -- | Gabber, Ekedahl (unpublished then) | no | Y (we use k finite or alg. closed) |
| 1.1.3.x Lang torsors, L_chi, K_chi, 1.1.3.4 | 139-140 (10-11) | rank-one sheaves from a character of a connected group's rational points; cohomology vanishes if chi nontrivial | Lang's isogeny | [De 5]? (as cited) | no | Y (for L_psi, K_chi) |
| 1.2.1.1, 1.2.1.2 | 141 (12) | definition of F_psi; trace function = (-1)^r times classical transform | 1.1.1.1, 1.1.1.4, 1.1.3.3 | Grothendieck trace formula | no | N for the proof (only definition used) |
| **1.2.2.1** involutivity F'F(K) = a_*K(-r) | 141-142 (12-13) | F twice is the pullback by x -> -x with a Tate twist | 1.1.3.2 (additivity of L_psi), 1.2.2.2 | SGA 4 XVII 5.2.6 (proper base change), 5.2.9 (projection formula); SGA 5 VII 1.1(ii) | no (proof on page) | Y |
| 1.2.2.2 | 142-143 (13-14) | F of a pullback from the base is the delta at the zero section | proper base change, projection formula, vanishing of R pr'_! L_psi off the zero section (1.1.3.1, 1.1.3.4) | SGA 5 VII 1.1(ii) | no | Y |
| 1.2.2.3 | 143 (14) | F is an equivalence of triangulated categories with quasi-inverse a^*F'(-)(r) | 1.2.2.1 | -- | no | Y |
| 1.2.2.4 | 143 (14) | F commutes with linear maps (f -> transpose) | adjunction of f, f', proper base change, projection formula | SGA 4 XVII | no | M (used for 1.2.3.x) |
| 1.2.2.5-1.2.2.9 | 143-144 (14-15) | pushforward to the base, convolution, Plancherel, base change | 1.2.2.4, Kunneth | SGA 4 XVII 5.4.3 | no | N (1.2.2.7 feeds 1.2.3.2) |
| 1.2.3.1 | 144 (15) | F of constant sheaf on a subbundle | 1.2.2.4, 1.2.2.2 | -- | no | Y (used in 2.5.3.1, 1.4.3.2, for delta and constant sheaf) |
| 1.2.3.2 | 145 (16) | translation by e multiplies F(K) by L(<e, >) | 1.2.2.7 (convolution) | -- | no | Y (translation of singular points) |
| 1.2.3.3-1.2.3.5 | 145-146 (16-17) | quadratic form, group action, base change | 1.2.2.4, Kunneth, proper base change | -- | no | M (1.2.3.4 used in 1.4.3.2(iii)) |
| **1.3.1.1** forget supports iso | 146 (17) | F_! = F_* | stated as [Ka-La] 2.1.3 | Katz-Laumon 2.1.3 / 2.4.1-2.4.4 | no (KL proof READ in the KL dump, OCR, pp. 12-17 of the dump: Artin-Schreier cover, projection formula, base change by a smooth map and a radiciel factorisation, SGA 4 XII 5.1, XVI 1.2; no weights) | Y |
| 1.3.1.2 / 1.3.1.3 | 146 (17) | pr_1: D_1 x A_2 -> D_1 universally strongly acyclic rel. (alpha x 1)_! L(x1 x2); RPsi = RPhi = 0 | [Ka-La] 2.4.4 | -- | no | Y (2.3.3.1, 2.5.3.1) |
| 1.3.2.1, 1.3.2.2 | 147 (18) | F commutes with duality (psi -> psi^-1, Tate twist) | duality theorems, pr smooth, 1.3.1.1; for L = Qbar_l [Ka-La] 2.1.5(ii) | -- | no | M (A5 duality, not S5) |
| **1.3.2.3** F is t-exact; Perv equivalence | 147 (18) | F sends perverse to perverse, equivalence of abelian categories | pr^*[r] t-exact (BBD 4.2.5), pr'_! left t-exact for pr' affine (BBD 4.1.2), pr'_* right t-exact (BBD 4.1.1), 1.3.1.1, 1.2.2.3 | BBD 4.1.1, 4.1.2, 4.2.5 (BBD dump, chapter 4: no weights; "pureté" there is cohomological purity of smooth pairs) | no | Y |
| **1.3.2.4** | 147 (18) | simple perverse -> simple perverse | 1.3.2.3 | -- | no | Y |
| 1.4.1-1.4.2 types T1, T2, T3 | 148-149 (19-20) | simple perverse sheaves on A are punctual, Artin-Schreier-type, or j_{!*}F[1] with no geometric constituent L(x.a') | BBD 4.3.1(ii) (needs L irreducible lisse on an irreducible smooth V over k) | BBD 4.3.1 | no | Y |
| **1.4.2.1** (i) T1<->T2', T2<->T1' ; (ii) T3<->T3' | 149 (20) | FT of a type-T3 sheaf is j'_{!*}F'[1] with F' irreducible lisse on U' | 1.3.2.4, (i), 1.2.2.1 | -- | no | Y |
| 1.4.3, 1.4.3.1 | 149-150 (20-21) | Kummer sheaves K_chi (x), j_! = j_* = Rj_* for chi nontrivial | -- | Sommes trig. (4.20) (SGA4h dump, Prop. 4.20(iii): R a_! = R a_* when all characters nontrivial; READ) | no | Y |
| **1.4.3.2** | 150 (21) | G(chi,psi) = H^1_c(G_m, K_chi tensor L_psi) has dimension 1, in degree 1 only; Frobenius acts by the Gauss sum; F_psi(j_*K_chi(x)[1]) = j'_*K_{chi^-1}(x')[1] tensor G | (i),(ii): Sommes trig. 4.3; (iii): 1.4.2.1(ii), 1.2.3.4, Kunneth, 1.1.3.7 | Sommes trig. Prop. 4.3 (dump: proof uses Euler-Poincare with Swan 0 at 0, 1 at infinity, and vanishing of H^0_c, H^2_c for a ramified rank-one sheaf; no weights; the "|tau|=1" remark 4.4 is not used) | no | Y (initial data of 2.5.3.1, only the dimension and the unramified-twist form; no absolute value) |

### 3.2 Chapter 2, sections 2.1 and 2.2 (local theory and curves)

| statement | j.p. (PDF) | what it says | rests on | outside | W? | toy |
|---|---|---|---|---|---|---|
| 2.1.1-2.1.2.1 | 151-152 (22-23) | henselian trait, G, I, P, upper numbering I^(lambda); G-modules | definitions | [Se 1] IV, [De 4] (0.6) notation | no | Y |
| 2.1.2.2, 2.1.2.3 | 152 (23) | P acts through a finite quotient; every P-module is semisimple; slope lambda of a simple P-module; decomposition V = sum V_lambda; Swan s(V) = sum lambda r(V_lambda) | l != p, pro-p group | [Se-Ta] p. 515, [Se 1] IV 3 | no | Y (semisimplicity used in my tameness argument 4.4) |
| 2.1.2.6 Hasse-Arf form | 153 (24) | slopes rational; lambda r(V_lambda) integer; s(V) integer | -- | [Se 1] IV 3, [Ka 3] pp. 211-215 | no | Y (rank/Swan integrality, used in the converse of 2.1.2.7(ii)) |
| **2.1.2.7** | 153-154 (24-25) | L rank one, Swan 1: (i) s(V tensor L) = r(V_[0,1[) + s(V_1 tensor L) + s(V_]1,inf[); (ii) s(V_1 tensor L) <= r(V_1), equality iff (V_1 tensor L)^{I^(1-eps)} = 0 for some eps in [0, 1/r(V_1)[ | simple P-module W of slope lambda: W tensor L is simple of slope sup(1,lambda) if lambda != 1, of slope <= 1 if lambda = 1; 2.1.2.6 | -- | no (proof on the page, short) | Y |
| 2.1.2.8 | 154 (25) | L_psi(1/pi) rank one Swan 1 | -- | [Se 1] IV 2 ex. 5 | no | Y |
| 2.1.4 | 154 (25) | tame = P trivial = slope 0 = Swan 0; simple tame modules have rank 1 (characters of Zhat'(1)) | I/P procyclic | -- | no | Y |
| 2.1.5 | 154 (25) | geometrically constant = unramified; equivalent conditions | -- | -- | no | N |
| **2.2.1.1** | 155 (26) | K perverse: a_x(K) <= r(K) - r_x(K) <= 0; equivalent: H^0(K)_x = 0 and H^-1(K) lisse at x; a_x = 0; r_x = r | BBD (4.0) | BBD 4.0 | no | Y |
| **2.2.1.2** GOS | 156 (27) | chi(X, K) = chi(X) r(K) - sum deg(x) a_x(K) on a projective curve | -- | [Ra], SGA 5 X 7 | no (HINT: standard; I have not opened it) | Y |
| **2.2.2.1** | 157 (28) | tame quotients of pi_1 of the punctured disc at infinity and of G_m are identified | Kummer covering v^N = u | -- | no | Y |
| **2.2.2.2** Gabber-Katz | 157 (28) | existence of a canonical extension of any local representation to a lisse sheaf on G_m tame at the other end | stated; proof in [Ka 2] (1.4) | Katz, Ann. Inst. Fourier 1986 | UNKNOWN (not opened) | see section 4: avoidable for the toy's blocks |

### 3.3 Chapter 2, sections 2.3 to 2.5

| statement | j.p. (PDF) | what it says | rests on | outside | W? | toy |
|---|---|---|---|---|---|---|
| **2.3.1.1** (i)-(iii), primed versions | 158-159 (29-30) | generic rank of K', its stalk rank at s' != 0', at 0' | proper base change r_s'(K') = -chi_c(A, K tensor L(x.s')), GOS 2.2.1.2, 2.1.2.7(i), and for (i): 2.1.2.8 so that (V_1 tensor L(x.a'))^{I^(1)} = 0 for almost all a'; (i)',(ii)',(iii)' by involutivity 1.3.2.3 | SGA 4 XVII 5.2.6 | no | Y |
| **2.3.1.2** | 159 (30) | U' depends only on the slope-[0,1] part; criterion for s' != 0' and 0' | 2.2.1.1, 2.3.1.1 | -- | no | Y |
| **2.3.1.3** | 159 (30) | (i) F_inf nonzero, slopes < 1 => U' = A' - {0'}, r(K') = sum deg(s) a_s(K); (ii) slopes > 1 => U' = A' | 2.3.1.1, 2.3.1.2 | -- | no | Y (the case "slopes in {0,1}" is neither (i) nor (ii); the toy uses 2.3.1.1(i)-(iii) and 2.3.1.2 directly) |
| 2.3.2 triangle, 4-term sequence | 159-160 (30-31) | 0 -> H^-1(K'_s') -> F'_{eta s'} -> R^-1 Phi -> H^0(K'_s') -> 0 | SGA 7 XIII 1.4.2.2; K' perverse | SGA 7 XIII | no | Y |
| **2.3.2.1** | 160 (31) | vanishing cycles of K' at s' come from (inf, s'); concentrated in degree -1 | Th. finitude 2.16 (L(x.x') lisse on A x A'_(s')), SGA 7 XIII 2.1.7.1 | SGA 4 1/2 Th. finitude, SGA 7 XIII | no | Y |
| 2.3.2.2, 2.3.2.4 remarks | 160 (31) | (2.3.2.1)(ii) is an instance of Artin-Gabber t-exactness (BBD 4.4); 2.3.2.3 is an instance of Swan semicontinuity [Lau 3] 5.1.1 via 2.1.2.7(i) | -- | BBD 4.4, [Lau 3] | no | N (remarks only; section 5.3) |
| **2.3.2.3** | 160 (31) | rank of R^-1 Phi at (inf, s'): r(V_1) - s(V_1 tensor L(x.s')) for s' != 0'; r(V_[0,1[) - s(V_[0,1[) for s' = 0' | 2.3.2.1, 2.3.1.1 | -- | no | Y |
| **2.3.3.1** (a Proposition) | 161 (32) | at infinity': vanishing cycles vanish over U x eta_inf'; sit in degree -1; F'_{eta inf'} = sum over s in S of induced stalks at (s, inf') plus the stalk at (inf, inf') | 1.3.1.2 (with A_1 = A', A_2 = A), SGA 7 XIII 2.1.7.1 | SGA 7 XIII | no | Y |
| 2.3.3.2, 2.3.3.3 | 161 (32) | ranks of the pieces: a_s(K) at s in S, r(F_]1,inf[) - s(F_]1,inf[) at (inf, inf'); only SUGGESTED here, proved in 2.4.3 (i)b for s = 0 and (iii)b | -- | -- | no | Y (the rank a_s is used; proved only via 2.4.3 (tame case: 2.5.3)) |
| 2.4.1 | 162 (33) | traits T, T', kernels L(pi/pi'), L(pi'/pi), L(1/pi pi') | -- | -- | no | Y |
| **2.4.2.1** | 162 (33) | local-to-global comparison of vanishing cycles in the three cases (finite, inf'), (inf, finite), (inf, inf'); hypothesis: pi^*K ~ V_!(1) | definitions ("immediate") | -- | no | Y, but see section 4.2 (hypothesis) |
| **2.4.2.2** | 163 (34) | local vanishing cycles live at the closed point, in degree 1 | printed proof: 2.2.2.1, 2.4.2.1, 2.3.2.1(i)(ii), 2.3.3.1(i)(ii) | -- | no | Y |
| 2.4.2.3 | 163 (34) | definition of F^(0,inf'), F^(inf,0'), F^(inf,inf') | 2.4.2.2 | -- | no | Y |
| **2.4.3** (i)-(iii) | 163-164 (34-35) | exactness; rank/Swan formulas; equivalences; duality | proof deferred to 2.5 | -- | no | see 2.5 |
| 2.5.1, 2.5.2 | 165 (36) | exactness from 2.4.2.2; reduction to simple V; commutation with base change; reduction to k alg. closed | 2.4.2.2, definitions | -- | no | Y |
| 2.5.3 reduction | 165 (36) | for tame V it suffices to prove 2.5.3.1 | 2.5.1, 2.5.2, 2.1.4 | -- | no | Y |
| **2.5.3.1** | 165-167 (36-38) | trivial module: (0,inf')-> trivial, (inf,0')-> trivial(-1), (inf,inf')-> 0; Kummer chi != 1: (0,inf')(V_chi) = V'_chi tensor G(chi,psi), (inf,0')(V_chi) = V'_chi tensor G(chi^-1,psi), (inf,inf') = 0 | proof (j.p. 166-167): F of Qbar_l, of the delta at 0, of j_*K_chi (1.2.3.1, 1.4.3.2(iii)); 2.3.2.1, 2.3.3.1, 2.4.2.1; for (inf,inf')=0 a blow-up chart h(x~,x~') = (x~ x~', x~'), 1.3.1.2, and Lemma 2.5.3.2 | SGA 7 XIII 2.1.7.1 (inside Lemma 2.5.3.2), Th. finitude 2.16 | no; **no Gabber-Katz** | Y |
| 2.5.3.2 | 167 (38) | vanishing cycles at an isolated point of the non-acyclicity locus are a direct summand | SGA 7 XIII 2.1.7.1 | SGA 7 XIII | no | Y |
| 2.5.4 | 167 (38) | (inf,0')(V) = 0 for V in G_[1,inf[; (inf,inf')(V) = 0 for V in G_[0,1] | **2.2.2.2** (canonical extension F, tame at 0, pi^*F = V); 2.3.2.3(ii), 2.4.2.1(ii); 2.3.1.1(i), 2.3.3.1(iii), 2.4.2.1, 2.5.3 and a dimension count | Gabber-Katz | UNKNOWN for Gabber-Katz | the second vanishing is needed by the toy for slope-1 blocks; see section 4 |
| 2.5.5, 2.5.6, 2.5.7 | 167-169 (38-40) | the rank/Swan formulas for general V, the quasi-inverses, duality | 2.2.2.2 (canonical extension), 2.3.1.3, 2.3.3.1(iii), 2.4.2.1, 2.5.3, GOS, involutivity | Gabber-Katz | UNKNOWN | N for tame; M for the blocks only through 2.4.3(iii)b |

## 4. What the induction actually needs, and what each need rests on

I derive the list from the structure of the induction (P_{i+1} = (j_!L) tensor FT(P_i); P_i simple perverse of type
T3, lisse on A - S_i, tame at S_i, at infinity a sum T^0 + sum_a L_psi(a x) tensor T^a with T^a tame; rank,
singular set and frequencies of FT(P_i) read from Laumon). A1 re-derives the induction; I only audit what each step
of that derivation would cite.

(N1) FT preserves perverse and simple objects, types T3 <-> T3': 1.3.2.3, 1.3.2.4, 1.4.2.1(ii) (BBD 4.1.1, 4.1.2,
4.2.5, 4.3.1; [Ka-La] 2.1.3). No weights. READ (img) all of it; BBD and KL statements READ (dump, OCR).
(N2) Generic rank of FT(K), stalk drops, location of the singular points of FT(K): 2.3.1.1, 2.3.1.2 (GOS, 2.1.2.7,
2.1.2.8, proper base change). No weights. READ (img). Needs: for the blocks, with b the transform parameter and
V_1 = sum_a L_psi(a x) tensor T^a, T^a tame: the twist V_1 tensor L_psi(b x') is the sum of L_psi((a + b x') x)
tensor T^a, each of slope exactly 1 unless a + b x' = 0, where it is T^a (tame, slope 0): by 2.1.2.7's proof
(simple W of slope 0 tensor L is simple of slope 1). So the drop at s' = -a/b is dim T^a, and at s' = 0' it is the
rank of the slope-<1 part; both are consistent with 2.3.1.1(ii),(iii) and 2.3.1.2. PROVED (given 2.3.1.1).
(N3) Structure of FT(K) at infinity': 2.3.3.1(iii) with the (s,inf') pieces identified by 2.4.2.1(i), translation
(1.2.3.2) and 2.5.3.1 (tame), and the (inf,inf') piece = 0. The only point with a dependency question is the last
(section 4.1). The identification of the (s,inf') pieces needs a repair for middle extensions (section 4.2).
(N4) Tameness of FT(K) at its finite singular points: 2.3.2.1(iii), 2.3.2.3, 2.4.2.1(ii), 2.4.3 (ii)(b) (tame case =
2.5.3.1) give that R^-1 Phi at (inf, s') is tame; passing from the vanishing-cycle module to the local monodromy of
F' needs an argument not in Laumon (section 4.4).
(N5) Rank recursion rho_i = d rho_{i-1} + rho_{i-2}: section 4.3 (derived from 2.3.1.1 and involutivity).

### 4.1 The vanishing of F^(inf,inf') on the toy's slope-1 blocks, without Gabber-Katz

The statement needed: for V a finite sum of modules L_psi(a x) tensor T (T tame, a != 0) and tame modules, the local
transform F^(inf,inf')(V) is 0. Laumon's 2.4.3(iii)b states this for all V in G_[0,1]; its proof 2.5.4 uses 2.2.2.2.

Argument A (explicit canonical extension). PROVED by A2, unrefereed.
- Work over k alg. closed (2.5.2 reduces the local statements to that case; the induction is geometric).
- For V = L_psi(a x) tensor T with T tame: let F_T be the lisse tame sheaf on G_m with local monodromy T at infinity
  and tame at 0; it exists because the tame fundamental group of G_m and of the punctured disc at infinity
  coincide (2.2.2.1, j.p. 157, READ (img): Kummer coverings), and a tame I-module is a representation of the quotient
  Zhat'(1) (2.1.4), continuous with a finite P-quotient (2.1.2.2). Then F = L_psi(a x) tensor F_T is lisse on G_m,
  of slopes <= 1 at infinity, tame at 0, and pi^*F = V.
- Repeat the argument of 2.5.4 for K = j_! F[1], j: A - {0} -> A: r(FT(K)) = a_0(K) (2.3.1.1(i), no slope > 1)
  = r(F|eta_0) = rank, and FT(K)|eta_inf' = (stalk at (0, inf'), rank r(F|eta_0) by 2.5.3.1) + (stalk at (inf,
  inf')) by 2.3.3.1(iii), 2.4.2.1; hence the (inf, inf') stalk has rank 0 (dimension count as printed in 2.5.4).
  Additivity (2.4.3(iii)a, exactness, from 2.4.2.2) extends it to sums of such V.
- Dependencies: 2.2.2.1, 2.3.1.1, 2.3.3.1, 2.4.2.1, 2.5.3.1. No Gabber-Katz.
Caveat: step "FT(K)|eta_inf' at the point (0,inf') has rank r(F|eta_0)" uses 2.5.3.1 at the tame point 0.

Argument B (global rank count). PROVED by A2, unrefereed. By 2.3.1.1(i) the rank of F' is
sum_s deg(s) a_s(K) (no slope > 1 part), and by 2.3.3.1(iii) F'|eta_inf' is the sum of the induced (s,inf') pieces
and the (inf,inf') piece. If the (s,inf') piece has rank a_s(K) (Remark 2.3.3.3, proved for s = 0 through 2.4.3(i)b,
i.e. 2.5.3.1 in the tame case, and for s != 0 by translation 1.2.3.2), then the (inf,inf') piece has rank 0. This
uses the ranks a_s(K) at the finite singular points s, which in the toy are tame, so only 2.5.3.1; it does not use
2.5.4. Labels: both A and B are my arguments, not statements of the paper.

### 4.2 A gap in applying 2.4.2.1 to middle extensions (not on any earlier list)

2.4.2.1(i) (j.p. 162, READ img) assumes an isomorphism pi^*K ~ V_!(1) with V_! the extension by zero. The induction's
sheaves are P = j_{!*}F[1] of type T3. At a finite singular point s with invariants V^I != 0 (V = F|eta_s) the stalk
of j_{!*}F[1] at s is V^I in degree -1, so P is not V_![1] near s: there is an exact sequence of perverse sheaves
0 -> i_*V^I -> V_![1] -> P -> 0 near s. Consequently the (s,inf') piece of FT(P) is NOT F^(0,inf')(V) but its quotient
F^(0,inf')(V)/F^(0,inf')(V^I) = F^(0,inf')(V/V^I) (exactness, 2.4.3(i)a; F^(0,inf') of a trivial module is trivial by
2.5.3.1(i)), of rank r(V/V^I) + s(V) = -a_s(P) in Laumon's sign convention. This matches the formula 2.3.1.1(i) (it
involves a_s, not r(V)+s(V)), so Laumon's global statements are right; only the identification of the local piece
with F^(0,inf')(V) is wrong when V^I != 0. For the toy: at the roots Z the inertia acts on F by -1, so V^I = 0 and no
repair is needed; at a finite singular point w of a transform Q_i (where M' = F_{Q_i} has invariants of dimension
rho - drop), the repair is needed, the quotient is still tame, and the frequency block is L_psi(b_{i+1} w y) tensor
(tame module of rank a_w(Q_i)). PROVED by A2 modulo the exactness statements cited. Label for B2: repairable, not fatal.

### 4.3 The rank recursion from 2.3.1.1 and involutivity (cross-check of S4's dimension count)

Notation (sheaf convention, k alg. closed): rho_i = rank of Q_i = FT(P_i), rank of P_{i+1} = rho_i, rho_0 = rank P_1 =
1. Invariant: slopes of P_i at infinity are in {0,1}; Z disjoint from Sing(Q_{i-1}) (condition G_k).
- 2.3.1.1(i) with no slope > 1 part: rho_i = sum over S_i of deg(s) a_s(P_i).
- At z in Z: inertia acts by -1 on every constituent, so V^I = 0, tame, a_z = rank of P_i = rho_{i-1}: d rho_{i-1}.
- At w in Sing(Q_{i-1}): P_i = (j_!L) tensor Q_{i-1} locally at w, and L is lisse at w, so a_w(P_i) = a_w(Q_{i-1}).
- sum over w in Sing(Q_{i-1}) of a_w(Q_{i-1}) is the generic rank of FT(Q_{i-1}) = the generic rank of P_{i-1} up to the
  rescaling and sign of 1.2.2.1 (involutivity) = rho_{i-2}, again by 2.3.1.1(i) applied to Q_{i-1} whose slopes at
  infinity are <= 1.
Hence rho_i = d rho_{i-1} + rho_{i-2} (rho_{-1} := 0). PROVED (A2), modulo the invariant. CHECKED: the dictionary of
frequencies and ranks of section 4 (S_i, A_i, ranks, Z disjoint from Sing(Q_i)) implemented in exact rationals for
d = 1, 2, 3, 4, 5, 7, k up to 9, three random seeds each: the recursion holds, the involutivity identity
sum of a_w = rank P_{i-1} holds at every step, 0 is in Sing(Q_i) iff i is odd (this last is checked indirectly:
it is built into the dictionary; see the script header). The check is bookkeeping consistency, not a proof of the
cited statements. Output: `compute/A2/check_bookkeeping_out.txt`. This agrees with the draft's r_{i+1} = d r_i + r_{i-1}
(S4) and with report B.

### 4.4 Tameness of Q_i at finite singular points: the step from vanishing cycles to local monodromy

Laumon gives R^-1 Phi at (inf, s'), identified with the local monodromy-quotient of K' = FT(K) at s' (2.3.2.1(iii)),
as a tame module (2.4.3(ii)(b) in the tame case: 2.5.3.1). What the induction needs is that F' itself, the local
monodromy of the T3 sheaf Q_i at s', is tame. PROVED by A2 (not in Laumon, not in any round-three report):
K' = j'_{!*}F'[1] is of type T3', so H^0(K'_s') = 0 and the exact sequence of 2.3.2 reads 0 -> F'^{I} -> F' ->
R^-1 Phi -> 0. P acts semisimply on F' (2.1.2.3); F'^I is contained in F'^P. Write F' = F'^P (+) W with W the sum of
the P-isotypic parts for nontrivial characters of P-quotients; W meets F'^I trivially, so W injects into R^-1 Phi,
on which P acts trivially, hence W = 0 and F' is tame. Dependencies: 2.1.2.2, 2.1.2.3, 2.3.2, 1.4.2.1(ii) (type
T3'). Round three's B-report states the conclusion "Q_i tame at its finite singular points" and attributes it to
2.3.2.1/2.4.3; the short argument above is what makes the attribution valid. Label: PROVED, unrefereed.

### 4.5 Answer to question (2), stated carefully

- Tame modules at points of A (finite points, like the roots Z): the full chain 2.3.1.1, 2.3.2.1, 2.3.3.1,
  2.4.2.1, 2.5.3.1 avoids Gabber-Katz and everything wild in 2.5 (2.5.4-2.5.7). READ (img), with one exception
  below.
- The exception: 2.4.2.2, whose statement is for every V in G, cites 2.2.2.1 (not 2.2.2.2) in its printed proof
  (confirmed on a 230 dpi crop). A global K with prescribed local module V at infinity is needed to apply 2.4.2.1; for
  wild V only Gabber-Katz provides it. The printed citation is therefore insufficient for wild V as it stands, but
  the printed proof is fine for tame V (2.2.2.1 provides the sheaf). This is a remark about the paper, not about
  the toy; I did not try to settle it.
- Wild-looking but explicit modules (the blocks): see section 4.1, the replacement for 2.5.4.
- Not read: 2.6, 2.7 (they use the canonical extension, 2.7.1.1, j.p. 178); they do not enter the chain above.

## 5. Round three's readings, checked against the page images

### 5.1 The slope maps (round three D item 6; B)
Page 163-164 (2.4.3): (i)b r(F^(0,inf')(V)) = r(V) + s(V), s(F(V)) = s(V), image in slopes [0,1[; (ii)b on
V in G_[0,1[: r = r(V) - s(V), s = s(V); (iii)b on V in G_]1,inf[: r = s(V) - r(V), s = s(V), image in ]1,inf[.
Slope = s/r gives lambda -> lambda/(1+lambda), lambda -> lambda/(1-lambda), lambda -> lambda/(lambda-1). RIGHT.
CHECKED (exact): composite identities (quasi-inverses of 2.4.3 (i)c, (ii)c, (iii)c) hold on 9,321 rational pairs
(r,s); the vanishing ranges are forced by signs of r-s. Script `compute/A2/check_bookkeeping.py`, part 1.

### 5.2 Vanishing ranges
(ii)b: F^(inf,0')(V) = 0 for V in G_[1,inf[ (closed at 1), page 163 bottom, read on a 200 dpi crop. Round three D
item 6 wrote "]1,inf[" (zero on slopes in ]1,inf[ and an equivalence on slopes in [0,1[): the closed bracket at
1 matters for the toy because a slope-exactly-1 block L_psi(a x) tensor T must be killed by F^(inf,0') (it is
related to the finite point -a, not to 0'). (iii)b: F^(inf,inf')(V) = 0 for V in G_[0,1] (closed on both sides),
confirmed on a 200 dpi crop. (iii)c: equivalence G_]1,inf[ -> G'_]1,inf[. D's item 6 is right for (i) and (iii).

### 5.3 The inequality in the semicontinuity statement (LAU.txt, [Lau 3] 2.1.1)
Round three D read, from OCR with the sign garbled, "phi(s) >= phi(t) for s in the closure of {t}" and the draft's
list 1 item 10 repeats the reading ">=". Laumon's own formulas show the direction on the page images: 2.3.2.3 (j.p.
160) gives the rank of R^-1 Phi at (inf, s') as r(V_1) - s(V_1 tensor L(x.s')), which is >= 0 by 2.1.2.7(ii)
(s(V_1 tensor L) <= r(V_1), j.p. 153). So along the family of the transform, Swan of the twist at the SPECIAL
parameter s' is <= its value at the generic parameter. In Deligne's function phi(s) = sum_y [Sw_y + rank], which
counts the Swan conductors, this is phi(special) <= phi(generic) (the section Y = {inf} x A' does not collide with
the finite sections), i.e. lower semicontinuity in the usual sense. A reading "phi(special) >= phi(generic)" would be
contradicted by the Fourier family itself (Swan drops from rank to 0 when a + s' = 0). So the OCR reading ">=" was
wrong in the direction in which the family drops; the sign of the symbol in [Lau 3] 2.1.1 itself I have NOT seen
(that paper is not on disk as images and I did not download it). Label: OPEN at the source; the direction used by
the induction is PROVED from 2.1.2.7(ii) and 2.3.2.3. B's route avoids semicontinuity (its section 2.1 says so),
so nothing in S5 depends on this.

### 5.4 The four OCR passages named in the brief (LAU.txt)
- Lines 1126-1131 (the sequence of 2.3.2): the page has a four-term exact sequence 0 -> H^-1(K'_s') -> F'_{eta s'} ->
  R^-1 Phi -> H^0(K'_s') -> 0, which reduces to a three-term one only because K' is perverse and the other
  cohomology vanishes; B's table L8 prints the three-term version "for K perverse" and drops the H^0 term (true for
  T3 sheaves). Minor; reading otherwise right.
- Lines 1176-1179 (2.3.3.1(iii)): right as B and D read it (induced stalks at (s,inf'), s in S, plus the (inf,inf')
  stalk); the subscript G_{s x k inf'} on the induction is the Galois group of the product point; for k alg. closed
  there is no index.
- Lines 1285-1324 (2.4.3): right as to ranks and slope maps; wrong on "(ii) zero on ]1,inf[" (section 5.2).
- Lines 1360-1375 (2.5.3.1): right as to (i), (iii); (ii)'s second line is V'_chi tensor G(chi^-1,psi), not
  "Kummer module of chi^-1 tensor G(chi,psi)" (D). For the toy the character enters only through tameness and its
  order, so this is bookkeeping.
- B-report L10: "2.5.3 uses Gabber-Katz 2.2.2.2": wrong, see section 4.5.

## 6. Outside sources: what each is and whether it was opened

| source | used for | opened? | weights? |
|---|---|---|---|
| [De 4] = Weil II, section 1.1 (formalism) | definition of D^b_c(X, Qbar_l), trace function | NOT opened; only the way Laumon cites it (j.p. 134-136, 151) | formalism only (HINT, background) |
| [Ka-La] 2.1.3, 2.4.4 | 1.3.1.1, 1.3.1.2 | proof READ in KL dump (OCR), pages 12-17 of the dump (appendix 2.4) | no weights in the proof as read |
| BBD 4.0-4.4 | t-structure, 4.1.1, 4.1.2, 4.2.5, 4.3.1, 4.4 | READ in BBD dump (OCR, lines about 11619-13500; chapter 5 on weights starts at about line 14659). The only "purete" in chapter 4 is cohomological purity for smooth pairs (4.3.2 proof, line about 13325) | no weights |
| SGA 4 1/2 Sommes trig. 4.3, 4.20 | 1.4.3.1, 1.4.3.2 | READ in SGA4h dump (extracted text, clean) | no (Euler-Poincare + vanishing) |
| SGA 4 1/2 Th. finitude 2.16, 3.11 | acyclicity, inertia | the dump has Cor. 2.16 (S spectrum of a field: universally locally acyclic) and 3.1-3.2 (constructibility of RPsi); whether Laumon's "(2.16)" is that statement or the smooth case I did not settle | no weights |
| SGA 7 XIII 1.4.2.2, 2.1.1, 2.1.7.1 | triangle, RPhi, base change RPsi o Rf_* = Rf_* o RPsi for f proper | NOT opened | no weights (HINT, standard) |
| SGA 5 X 7, [Ra] (GOS) | 2.2.1.2 | NOT opened | no weights (HINT) |
| Serre Local Fields IV, [Se-Ta], [Ka 3] | 2.1.2.x | NOT opened | no |
| [Ka 2] Gabber-Katz | 2.2.2.2 | NOT opened | UNKNOWN |
| [Lau 3] Deligne-Laumon | remarks 2.3.2.4 only | NOT opened by me (round three D opened it as OCR) | not used by the chain |

## 7. What I did not do or could not settle

- Gabber-Katz (Katz, Ann. Inst. Fourier 1986) and Deligne-Laumon (Asterisque 82-83): not opened by me; no
  statement about their proofs and weights is made.
- SGA 7 XIII 2.1.7.1, SGA 4 XVII 5.2.6, 5.2.9, 5.4.3, SGA 5 X 7 / Raynaud: only cited-by-Laumon statements; A6's job.
- 2.6 and 2.7 of Laumon (PDF 41-48) and chapters 3-4 beyond what is stated above: not read; "no weights in chapters
  1-3" in the text-layer search is a search of OCR, and I verified it by reading only chapters 0-2.
- BBD, KL, SGA4h dumps are round-two dumps; KL.txt and BBD.txt are OCR with errors; I read the relevant paragraphs
  but did not compare them against page images of those papers.
- That the induction is correct is not shown here (A1's part). My sections 4.1-4.4 are small steps the induction
  needs and that are not literally in Laumon; each is labelled PROVED by A2 and needs a second reader.

## 8. Files

- Report: `./round4/reports/A2-laumon-dependency-audit.md`
- Script and output: `.../round4/compute/A2/check_bookkeeping.py`, `.../round4/compute/A2/check_bookkeeping_out.txt`
