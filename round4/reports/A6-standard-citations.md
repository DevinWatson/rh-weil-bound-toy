# A6. The standard theorems, opened (round four)

Written 2026-11-21 (UTC) by agent A6. Scope: items 1 to 6, 8 and 9 of List 1 of `round3/PROOF_DRAFT.md`.
Everything here is about character sums over finite fields (Weil 1948). Nothing says anything about the Riemann Hypothesis for the integers.
Evidence log (greps and line numbers): `round4/compute/A6/evidence.txt`.

## 0. How to read this report; what "OPENED" means here (read first)

Sources used and their quality, stated plainly:

- **SGA 4 1/2 (Deligne et al.)**: the local file `round2/compute/LIT/SGA4h.txt` is the whole volume with a clean LaTeX-type text layer (not garbled OCR). Statements were read in that text. Printed page numbers are those of the volume ("CHAPITRE n ... page"). Not read from page images; the text layer is good enough that I rely on it.
- **SGA 1 (arXiv retyped version)**: `round2/compute/LIT/SGA1.txt`, clean text. Read.
- **Katz-Laumon 1985 (`KL.txt`)**: OCR of the Numdam scan; symbols garbled (script letters, hats), but statement numbers and prose are legible. Statements were read; the symbols were reconstructed from context. Labelled "OPENED (OCR)".
- **BBD (`BBD.txt`)**: rough OCR, and the dump holds two OCR layers of every page. Statements 4.0, 4.1.1, 4.1.2, 4.2.5, 4.2.7, 4.2.8, 4.3.1 to 4.3.4, 4.4.1 to 4.4.5 were read; they are legible enough to read their content. "OPENED (OCR)".
- **Stacks Project**: read through the web-fetch tool, which returns a **summary** of a tag page made by a small model, not the verbatim page. Statements and tag numbers below that I took from it are labelled "OPENED (web, summarised)". I did not get any tag page verbatim. Where I only saw a search-result snippet, and not the page, I say "NOT OPENED (search snippet only)". The numbers of lemma and tag should be confirmed against the live pages before anyone writes them in a final text.
- I did not download any file. I opened no page image of Laumon (not my part).

Labels: PROVED / CITED / CHECKED / OPEN / HINT as in the brief. OPENED / NOT OPENED as in the draft.

## 1. Summary table

| # | Draft's item | Statement read at | Marked | Weights in its proof? |
|---|---|---|---|---|
| 1 | Grothendieck trace formula | SGA 4 1/2, "Rapport", Thm 3.2 (p. 38), Q_l-sheaves; reduction 3.7, 3.8, 4, 5.2, 5.3 (pp. 40, 45-46). Also Stacks 64.2 (03SJ), 64.14 (03TW), 64.16 (03UF) | **OPENED** (statement and the shape of the proof; proof not read through) | No. Proof goes through the fixed-point formula of Weil for curves (Rapport 5.3) and Z/l^n-coefficients. HINT-level for the inner proofs (see 2.1). |
| 2a | Kunneth | Stacks 59.97 (0F13), Lemma 59.97.2 (0F14), 59.97.9 (0F1P) | **OPENED (web, summarised)**, for RGamma only, Z/n coefficients; the compact-support version for Q_l is **NOT OPENED** at a source | No. Proof: projection formula, proper base change, Leray (Stacks). |
| 2b | Proper base change | Stacks 59.91.11 (095T) via search; Rf_! version Lemma 63.9.4 (0F7L) | **OPENED (web, summarised)** for 63.9.4; 095T snippet only | No |
| 2c | Projection formula | Stacks 63.10 (0G28), Lemma 63.10.7 (0GL5) | **OPENED (web, summarised)** | No |
| 2d | Excision (j_! sequence, triangle for Rf_!) | Stacks 59.70.8 (095L) | **OPENED (web, summarised)**; the Rf_! triangle (63.10.5) is **NOT OPENED** (search snippet only) | No |
| 2e | Leray | Stacks 59.54.2 (03QC); composition Rg_! Rf_! = R(gf)_!, Lemma 63.9.2 (0F7J) | **OPENED (web, summarised)**; Rapport 1.4 also read (Frobenius on the Leray sequence) | No |
| 3 | Artin vanishing | BBD 4.1.1, 4.1.2 (p. 102-103), Artin SGA 4 XIV 3.1 quoted there; Stacks 59.95.6 (0F0V), 59.95.8 (0F0X) | **OPENED (OCR)** BBD; **OPENED (web, summarised)** Stacks, torsion form only | No. BBD says 4.1.1 only restates SGA 4 XIV 3.1. |
| 4 | Duality on curves | SGA 4 1/2 "Dualite" Thm 1.3 (p. 75), Thm 2.2 (pp. 76-77); "Sommes trig." 3.3 (p. 93) | **OPENED** (Z/n coefficients; Q_l form by limit, stated in Sommes trig. 3.3) | No. Proof: Artin's argument with the trace H^2(X, mu_n) = Z/n. |
| 5 | Grothendieck-Ogg-Shafarevich | SGA 4 1/2 "Sommes trig." 3.2.1 (pp. 92-93), citing Raynaud, Bourbaki 286 | **OPENED** (statement); the proof (Raynaud, SGA 5 X) **NOT OPENED** | Not in the statement. Proof not read: HINT that it uses none. |
| 6 | BBD chapter 4 | 4.0, 4.1.1, 4.1.2, 4.2.5, 4.2.8, 4.3.1 with proof, 4.4.1-4.4.5 | **OPENED (OCR)** | No (chapter 5 of BBD is the weight chapter; the proofs read use only Artin vanishing, purity for smooth pairs, formal gluing). 4.4 is only half of what the draft says (see 3.6). |
| 8 | Katz-Laumon 2.1.3, 2.1.5 | KL pp. 154-155 (statements), 155-159 (proofs) | **OPENED (OCR)**. This settles the discrepancy of draft list 1 item 8 (B says opened, D says not): they are opened now. | No (2.1.3: appendix 2.4, Artin-Schreier cover, projection formula, smooth base change; 2.1.5 (i)(ii): proper base change, duality; (iii) uses KL 1.1.9(v), 1.2.2(v), not read). Weights appear only in KL 2.2.1, which the draft does not use. |
| 9 | SGA 1 V 8.2 | SGA 1 V 8, Prop. 8.2 (pp. 143-144) | **OPENED** | No (proof: SGA 1 I.10.1 only) |

Total: 8 items opened at least in statement; two pieces remain NOT OPENED at a source (Kunneth with compact supports for Q_l; Rf_! excision triangle); the proof of GOS is not opened.

## 2. Item by item: statement, hypotheses, check of each use

### 2.1 Trace formula (item 1)

**Statement (CITED, read).** SGA 4 1/2, Rapport, Thm 3.2 (printed p. 38): X_0 separated of finite type over F_q, F_0 a constructible Q_l-sheaf (l not p). For every n, sum over x in X(F_{q^n}) of Tr(F^{n*}, F_x) = sum_i (-1)^i Tr(F^{n*}, H^i_c(X, F)). Thm 3.1 is the L-function form. F^* is the geometric Frobenius correspondence (Rapport 1.2, 1.8.1: F^* is inverse to the arithmetic Frobenius phi on H^i_c). "Sommes trig." 3.2 treats E_lambda-sheaves, so eigenvalues live in a finite extension of Q_l (and in Qbar_l after extension).
Stacks 64.2 states only the torsion version for dimension 1 and says it is "slightly wrong as stated" (web, summarised); 64.16.1 (03UG) states the correct torsion version for dim <= 1 with D_ctf(X, Lambda) coefficients. Stacks does not state the Q_l-version in any dimension: it says the general case follows by dévissage. So the usable source for the draft is the Rapport, not Stacks.

**How it is proved (read in outline only).** Rapport 3.7: with the Q_l-formalism (Leray, base change for R^q f_!), reduce to X_0 a smooth curve and F_0 lisse. 3.8 and 4-5: reduce to Z/l^n-coefficients (Lemma 5.2) and then to Weil's theorem on a smooth projective curve (Thm 5.3: number of fixed points of an endomorphism with isolated fixed points = alternating sum of traces on H^i(X, Q_l); the text on p. 46 attributes it to Weil ([Wei48] n. 43, 66, 68), refers to Lang [Lan83] VI 3 with VII 2 th 3 for a proof, and adds that it also follows from the cycle class). Weil's fixed-point theorem is in Weil's book (Varietes abeliennes et courbes algebriques, 1948), the same book that proves the Riemann hypothesis for curves; but it is a different statement (an intersection number identity) and appears before the Riemann hypothesis part of that book. Stacks 64.14.4 (03U1) reproduces it and (web, summarised) says the argument works with intersection numbers on C x C and the trace on the Jacobian, and that "positivity of Rosati" is listed in a table but not used in the calculation. I could not confirm that last point from a verbatim page.
Weights: grep of the Rapport text (lines 2454-3548 of SGA4h.txt) finds no occurrence of poids, pureté, conjecture de Weil, Weil II, hypothèse de Riemann (evidence.txt). The word "pureté" or weights first appear in the volume in "Sommes trig." 1.17 and "Cycle". So the statement and the proof route read are weight-free. Not read: the proofs in Rapport 5-8 line by line, and Weil's/Lang's proof of 5.3; for these "no weights" rests on the grep, on Rapport's stated route, and on the fact that 5.3 is an identity of integers (HINT).

**Uses in the draft and hypothesis check.**
- S0/S2 (sum over F_{q^n} of chi(f(x)) = -sum alpha_i^n): X_0 = A^1 over F_q, F_0 = j_!L (a constructible, not lisse, Q_l-sheaf: allowed), H^0_c = H^2_c = 0, stalk trace of j_!L at x is chi(f(x)) (zero at a root). OK. Convention: trace of geometric Frobenius at x on L_chi(f) is chi(f(x)); sign conventions for L_psi (psi or its inverse) do not matter for the identity q N = M^k + R, because R is symmetric under h -> -h. Minor, no error.
- S7(c) (R_n as an alternating sum of traces on H^{k+1}_c, H^{k+2}_c of G_m x A^k): X_0 = G_m x A^k over F_Q, F = pullback of the external product of j_!L, tensor L_psi(h Q_c): a Q_l-sheaf (not a complex), constructible. The coefficient field must contain Q(zeta_p) and the values of chi: it is a finite extension E_lambda of Q_l, which is what the Rapport and "Sommes trig." use. OK. The sums over F_{Q^n} are over points of the base field F_Q extended to F_{Q^n}: the formula is used for each n. OK.
- S8 (fibre sums over F_{Q^{mn}} at a closed point h_0 of degree m): X_0 = A^k over F_{Q^m}, F_{h_0}; needs that (R^b pr_! F)_{h_0-bar} = H^b_c(A^k, F_{h_0}) = the stalk, that is base change for R pr_! (item 2b). OK.
- Nothing in the draft uses the trace formula for a complex or in a way outside Rapport 3.2. OK.

**One gap in the draft's List 1:** item 1 says "CITED (SGA 4 1/2, Rapport, Fonctions L)" and weights "not used in the formula (HINT)". Now: OPENED; weights: none in the text (grep).

### 2.2 Kunneth, base change, projection formula, excision, Leray (item 2)

**What is available at readable sources.** Stacks proves everything with torsion coefficients (Lambda a ring, Z/n with n invertible in the field, or torsion cohomology sheaves). The passage to Q_l goes through Rapport 2.9-2.11 (the Q_l-formalism of SGA 5 V, VI: "R^q f_! of a Z_l-sheaf is a Z_l-sheaf", p. 38, read) and BBD 2.2.18 (read in OCR: D^b_c(X, Q_l) as the Q_l-extension of the Z_l-version; the t-structure passes to the limit), and in the Qbar_l form Weil II 1.1 / Ekedahl (NOT OPENED). The draft's sheaves are Q_l (or E_lambda) objects. So every use below is: torsion statement OPENED, passage to Q_l CITED at the Rapport/BBD (opened in outline), the Qbar_l case via extension of scalars.

**(a) Kunneth.** Stacks Lemma 59.97.2 (0F14): k separably closed, X proper over k, Y quasi-compact and quasi-separated: RGamma of the external product = RGamma(X, E) tensor^L RGamma(Y, K), for E, K bounded below with torsion cohomology, or with Z/n coefficients and Y of finite type. Lemma 59.97.9 (0F1P): X, Y of finite type over k separably closed, n invertible in k, Z/n coefficients: Kunneth holds with no properness. Stacks adds a comment that the isomorphism is not shown to agree with the cup-product map. Both statements are for RGamma (ordinary cohomology), not for R f_!; I did not find a Stacks statement for R f_! of an external product (search found none; web, summarised). 
*Use S7(a):* H^*_c(A^k, (j_!L)^{boxtimes k}) = H^{tensor k} and the claim T = H^{tensor k}, degree k only. Here j_!L extends by zero to P^1 (proper); H_c(A^1, j_!L) = H(P^1, bar-j_!L); and (P^1)^k is proper. So Stacks 59.97.2 with proper X = P^1 and Y = (P^1)^{k-1} gives the compactly supported statement for Z/l^n-coefficients; the Q_l limit and the Frobenius equivariance (needed for "T-part of R_n = -M_n^k", S7(a)) are not in Stacks. Frobenius equivariance comes from naturality: Rapport 1.3 (read, p. 35: the Frobenius correspondence is functorial for f_0). I mark: Kunneth for the product of copies of j_!L CITED (Stacks 0F14 for torsion, OPENED web); Q_l limit and Frobenius compatibility CITED (Rapport 1.3, 2.11; opened), not checked line by line. Hypotheses OK: base field alg. closed, l invertible, finite type.
Also needed, but not named in the draft: BBD 4.2.7-4.2.8, external product commutes with the usual operations and is t-exact for Q_l (a field) coefficients (read in OCR; the text there stresses that the perversity function has to be the linear one). Used for "K_ext[k] perverse" in S7(a). The draft's List 1 does not list 4.2.7/4.2.8. Use OK: coefficients Q_l (a field), schemes of finite type over a field alg. closed; tensoring with the lisse rank-one sheaf L_psi(hQ_c) preserves perversity (stalk conditions).

**(b) Proper base change and base change for R f_!.** Stacks 59.91.11 (095T), the proper base change theorem (search result; the page itself NOT OPENED). Lemma 63.9.4 (0F7L): for a cartesian square with f separated of finite type and all schemes quasi-compact and quasi-separated, g^{-1} R f_! = R f'_! g'^{-1}, no condition on g (web, summarised; the proof cites proper base change for bounded below torsion complexes or torsion Lambda). Its proof uses Lemma 63.8.1: g_! R f'_* K -> R f_* g'_! K is an isomorphism for proper f, f' and g, g' separated quasi-finite, when K is bounded below with torsion cohomology or Lambda is torsion. 
*Uses:* S4 (Rpr'_!(pr^*G_i tensor L_psi) as a family; fibre of R^b pr_{h!} F over h_0 = H^b_c(A^k, F_{h_0})); S7(a) (stalk computation of Rpr_! L_psi(hQ)); S8 (fibre at the closed point h_0). Hypotheses: finite-type separated morphisms of noetherian schemes: OK. Coefficients: torsion, then Z_l limit as in Rapport 2.11 and the stated "essential result" (VI 2.2): OK.
The one place where a stalk computation is done and a sheaf-level identification is made is S7(a): R pr_{A^k !} (L_psi(hQ_c)) = i_{Y *} Q_l[-2](-1). My re-derivation: the stalk at x in A^k is H_c(A^1, L_psi(h Q_c(x))) = 0 if Q_c(x) != 0 (by Sommes trig. 2.7*: H^*_c(G_a, L_psi) = 0, see 2.7 below) and = Q_l(-1)[-2] if Q_c(x) = 0; hence R pr_! L is supported on Y, so equals i_* i^* R pr_! L, and i^* R pr_! L = R pr_{Y!} (Q_l) = Q_l[-2](-1) by base change along i (0F7L). Hypotheses OK. PROVED modulo the cited statements. Note: the vanishing H^*_c(G_a, L_psi) = 0 is an input the draft's List 1 does not list. See 2.7.

**(c) Projection formula.** Stacks Lemma 63.10.7 (0GL5), in Section 63.10 (tag 0G28): R f_! E tensor^L K = R f_!(E tensor^L f^{-1} K), f separated of finite type between quasi-compact quasi-separated schemes, Lambda torsion (web, summarised: proved from j_! projection formula and the proper projection formula 59.96.6). Uses: S4 (P_{i+1} = (j_!L) tensor FT(P_i)); KL 2.1.3 uses it too. Coefficients: torsion, Q_l by limit. OK.

**(d) Excision.** Stacks 59.70.8 (095L): for X, closed Z with open complement U, any abelian sheaf F: 0 -> j_! j^{-1}F -> F -> i_* i^{-1}F -> 0 exact (web, summarised, no extra hypothesis). The corresponding distinguished triangle for R f_! (Stacks 63.10.5) was seen only in a search snippet: NOT OPENED; it follows from the sequence, because R f_! is a triangulated functor. Uses: S7(a) (G_m x A^k in A^1 x A^k, complement {0} x A^k) and S0 (j_!). Hypotheses: none beyond finite type for the H_c. OK.

**(e) Leray.** Stacks 59.54.2 (03QC): spectral sequence H^p(Y, R^q f_* F) => H^{p+q}(X, F), any morphism (web, summarised). For compact supports the draft needs H^p_c(Y, R^q f_! F) => H^{p+q}_c(X, F); this comes from the composition R g_! R f_! = R(gf)_! (Stacks 63.9.2, 0F7J; web, summarised) and the canonical truncation; Rapport 1.4 (read, p. 35) states exactly the compact-support Leray sequence with Frobenius action. In the draft S7(b) the Leray sequence is used in the degenerate case: R^b = 0 for b != k, so R pr_{h!} F = R^k[-k] and H^{k+a}_c(G_m x A^k, F) = H^a_c(G_m, R^k) holds without any spectral sequence: only the composition 63.9.2. Fine. Hypotheses OK. One detail that the draft takes for granted: H^2_c(G_m, R^k) equals H^2_c(U, V), V = R^k|_U lisse, because R^k and j_!V (or j_*V) differ by punctual sheaves, which contribute only to H^0_c, H^1_c. True (extra stalks at finitely many points add H^0 only; the sequence 0 -> j_!V -> R^k -> punctual -> 0 gives H^2_c(j_!V) = H^2_c(R^k) because H^1, H^2 of a punctual sheaf vanish). And H^2_c(U, V) = V_{pi_1^{geo}}(-1): see 2.4.

### 2.3 Artin vanishing (item 3)

**Statement (CITED, read).** BBD Thm 4.1.1 (printed p. 102, OCR): for f affine, R f_*: D^b_c(X, Q_l) -> D^b_c(Y, Q_l) is right t-exact for the self-dual perversity (D^{<= 0} to D^{<= 0}); BBD says it restates SGA 4 XIV 3.1 (M. Artin). Cor. 4.1.2 (p. 103), by Verdier duality: R f_! is left t-exact (D^{>= 0} to D^{>= 0}). Hypotheses of 4.0: schemes separated of finite type over k, k finite or algebraically closed, Q_l coefficients (the text says it also works with E_lambda, Z/l^n).
Stacks (web, summarised): 59.95.6 (0F0V): X affine of finite type over a field K: cd(X) <= dim X + cd(K); 59.95.8 (0F0X): for an affine morphism f of finite-type K-schemes and a torsion sheaf supported on points of transcendence degree <= a, R^q f_* F is supported on points of transcendence degree <= a - q. Both torsion, no weights or Frobenius in the proofs (the summaries list transcendence degree, strict henselisation, colimits, Lemma 59.95.7).

**Uses and hypothesis check.**
- S5 step 7, "H^{<0}_c(A^1, P_k) = 0": P_k perverse on A^1 over F-bar, A^1 -> pt affine, apply BBD 4.1.2. OK (coefficient field Q_l or E_lambda: OK; for Qbar_l by extension of scalars).
- S7(a), "H^j_c(Y, K) = 0 for j < k-1 (Y has affine complement in A^k, K_ext[k] perverse, Artin)": my re-derivation. Let P = K_ext[k] on A^k, perverse (BBD 4.2.8 for the external product of the perverse sheaves j_!L[1]; j_!L[1] is perverse because j: U_0 -> A^1 is an affine open immersion; tensoring with L_psi(hQ_c) restricted to h fixed preserves perversity). U = A^k - Y is affine (complement of the hypersurface Q_c = 0 in affine space). Then H^j_c(A^k, P) = 0 and H^j_c(U, P|_U) = 0 for j < 0 by BBD 4.1.2 applied to A^k -> pt and U -> pt (both affine). The triangle H_c(U) -> H_c(A^k) -> H_c(Y) -> gives H^j_c(Y, P|_Y) = 0 for j < -1, that is H^{j+k}_c(Y, K) = 0 for j + k < k - 1. This matches the draft. PROVED modulo BBD 4.1.2, 4.2.8 and excision. Here h is held fixed, so P lives on A^k.
  Remaining hypothesis in this step that the draft does not state: Q_c has to be a nonzero polynomial (all c_i nonzero: yes).
- Stacks 0F0V gives the same statement for H^i (not H^i_c) with torsion coefficients; the draft needs the H_c form for perverse sheaves, which is BBD 4.1.2. Fine.

**Weights:** none; BBD 4.1.1 is a restatement of Artin (SGA 4 XIV 3.1, 1963-64; weight theory did not exist).

### 2.4 Duality on curves (item 4)

**Statement (CITED, read).** SGA 4 1/2 "Dualite": Thm 1.3 (p. 75): S regular of dimension 1, j: U -> S dense open, F locally constant constructible Z/n-module on U: D(j_*F) = j_* D(F), i.e. Hom(j_*F, Z/n) = j_*F^vee and Ext^i(j_*F, Z/n) = 0, i > 0 (n invertible). Thm 2.2 and 2.1 (pp. 76-77, Artin's proof): X smooth projective curve over alg. closed k; for K in D^b_c(X, Z/n) the trace pairing RGamma(X, K) x RGamma(X, DK) -> Z/n is perfect, where DK = RHom(K, Z/n(1)[2]); the case K = j_!Z/n is "Poincare duality between cohomology and compactly supported cohomology of an open". "Sommes trig." 3.3 (p. 93): for X-bar projective smooth connected curve over alg. closed k, j: X -> X-bar, F a lisse E_lambda-sheaf on X: H^i(X-bar, j_*F) and H^{2-i}(X-bar, j_*(F^vee(1))) are dual.
Proof inputs read: trace H^2(X, mu_n) = Z/n, local biduality 1.3 (inertia computation), Artin's covering trick. No weights. (grep of lines 5318-5700: no hit.)

**Uses and checks.**
- S0 (H^2_c(U_0, L) = 0): needs "H^2_c(U, F) = coinvariants of pi_1^{geo} on F, twisted by (-1)" for F lisse on the smooth connected curve U. This is the duality H^2_c(U, F) dual to H^0(U, F^vee(1)), with pairing perfect for lisse F on an open curve: Dualite 2.1 states it for K = j_!Z/n, and Thm 2.2 for general constructible K on the projective curve; the passage to lisse F on U uses j_! F, a constructible sheaf on X. OK. For L of rank one with nontrivial monodromy, no invariants and no coinvariants. OK.
- S5 step 7 (H^1_c(P_k) = H^2_c(j_*M_k) = coinvariants(-1) = 0): as above, plus: for a curve, j_{!*}(M[1]) = (j_* M)[1] (BBD 2.1.11 plus Dualite 1.3). I did not open BBD 2.1.11; this is a standard fact. OK, but flagged: the draft states it without citing.
- S7(b): H^2_c(G_m, R^k) = C(-1) with C the coinvariants: same duality; H^3_c = 0 and H^i_c = 0 for i not in {0,1,2}: "Sommes trig." 3.2 (p. 92) states the vanishing outside {0,1,2}. OK.
- S11 (assembler's duality argument): pairing H^1_c(A^1, j_!L) x H^1(A^1, j_*L^vee(1)) -> Q_l(-1). Dualite 1.3 + 2.1 give it with j_* on the compactification and with j_!, for the open curve as stated above. The next step "H^1_c -> H^1 is an isomorphism because L^{I_infty} = 0 = H^1(I_infty, L)" uses the exact sequences 0 -> j_!L -> j_*L -> (L^{I})_infty -> 0 on P^1, and Dualite 1.3 for D(j_*L). OK as a plan; this is A5's step, not checked here beyond hypotheses: self-duality of L (chi^2 = 1) holds for any l != p including l = 2; d odd gives L ramified at infinity (quadratic), tame since p odd. OK.
- Coefficient hypothesis: Dualite is for Z/n with n invertible; Q_l by limit as stated in Sommes trig. 3.3 for E_lambda-sheaves. Fine.

### 2.5 Grothendieck-Ogg-Shafarevich (item 5)

**Statement (CITED, read).** SGA 4 1/2 "Sommes trig." 3.2.1 (pp. 92-93): X-bar smooth projective connected curve of genus g over algebraically closed k, X open dense with complement a finite set S, F a lisse E_lambda-sheaf on X: chi_c(F) = rank(F) * chi(X) - sum over s in S of Sw_s(F), with chi(X) = 2 - 2g - #S. Source named there: [Ray65] = Raynaud, Seminaire Bourbaki 286. The text also says (3.2) that H^i_c vanish for i not in {0,1,2}. Raynaud's paper and SGA 5 X: NOT OPENED. Stacks: no GOS formula found (search found none).

**Uses and hypothesis check.**
- S0, dim H = d - 1: U_0 = A^1 - Z, X-bar = P^1, g = 0, S = Z + {infinity} so #S = d + 1, chi(U_0) = 1 - d. L: lisse of rank 1 on U_0, tame everywhere: the character chi has order 2, p odd, so wild inertia (a pro-p group) acts trivially, so all Swan conductors are 0. So chi_c(L) = 1 - d. With H^0_c = 0 (L has no invariants) and H^2_c = 0 (no coinvariants: monodromy is nontrivial), dim H^1_c = d - 1. OK. The draft's H = H^1_c(A^1, j_!L) = H^1_c(U_0, L) by composition. OK.
- S7(a)/L_psi: H^*_c(A^1, L_psi(ax)) = 0 (a != 0): GOS gives chi_c = 1*1 - Sw_infty = 0 (Sw = 1 for L_psi at infinity: this is the value, read in "Sommes trig." in other places; I did not look for the line); with H^0_c = H^2_c = 0 this also proves the vanishing. The draft instead gets it from the translation-homotopy argument (Sommes trig. 2.7*, see 2.7), independent of GOS. Either works.
- S5 step 3 (B's ranks and Swan conductors of Fourier transforms) uses GOS in the same form (lisse F on an open dense subset of the line over alg. closed field): hypotheses OK as long as the sheaf is lisse on the open set; the local terms Sw_s are computed from the structure of the sheaf, which is A1/A2's part.
- Coefficients: E_lambda (finite extension of Q_l); the draft's Qbar_l objects are defined over some finite E_lambda: OK.
**Weights:** the statement contains none. The proof (Raynaud; classical route: Riemann-Hurwitz for a finite Galois cover trivialising the mod l^n sheaf, Brauer characters and the integrality of Artin's Swan representation) is not opened, so "weight-free" is a HINT, supported by the date (1965) and by the fact that "Sommes trig." places GOS in 3.2 before it states the use of weights (3.4: "Weil proved ..."). Note "Sommes trig." 3.4 says that for sheaves trivialised on a finite cover (L_chi(f) is of this kind) Weil proved |eigenvalue| = q^{i/2} on H^i(X-bar, j_*F): the Riemann hypothesis for the very sums the draft is about. This is not used anywhere in the draft; I mention it so nobody reads the citation of 3.2 as an input from 3.4.

### 2.6 BBD chapter 4 (item 6)

Read (OCR; hypotheses of 4.0: separated finite-type schemes over a field k with k finite or alg. closed; coefficients Q_l, or E_lambda, Z_l, Z/l^n):

- **4.1.1 and 4.1.2:** see 2.3.
- **4.2.5 (p. ~108):** f smooth of relative dimension d with connected geometric fibres: f^*[d] is fully faithful from perverse sheaves on Y to perverse sheaves on X. The draft lists it in List 1 but I find no step S0-S12 that uses it by name; probably intended for pr^*[1] in the construction of FT. If used: hypotheses (smooth, connected fibres) hold for pr: A^1 x A^1 -> A^1. I mark: use not identified.
- **4.2.7, 4.2.8:** external product commutes with R f_*, R f_!, f^*, f^!, and is t-exact for the self-dual perversity (field coefficients; the proof uses the linearity of the perversity). Needed for "K_ext[k] perverse" (S7(a)); not in the draft's List 1 (add it).
- **4.3.1 (p. 112):** (i) the category of perverse sheaves is artinian and noetherian; (ii) if j: V -> X is the inclusion of an irreducible subvariety, smooth over k (reduced smooth), and L is an irreducible lisse Q_l-sheaf on V, then j_{!*}(L[dim V]) is a simple perverse sheaf, and every simple perverse sheaf is of this form. Proof read (4.3.2-4.3.4): uses cohomological purity for a smooth pair (the theorem de purete cohomologique of SGA 4 XVI, not weights), irreducibility of monodromy not changing on a dense open of a normal X, and formal properties 1.4.2.5 of j_{!*}. No weights. Hypothesis note: in 4.3.1 "irreducible" refers to Q_l (or the E_lambda used); the draft works with Qbar_l and eigenvalues in Qbar_l. The invariant (I_i) must read "irreducible over Qbar_l", that is absolutely irreducible over some finite E_lambda; BBD 2.2.18 treats E_lambda by extension of scalars, and an absolutely irreducible sheaf stays irreducible after any finite extension, so the use is fine. I flag it because irreducible-over-E_lambda alone would not give a tensor product M tensor L with L of rank 1 irreducible over a bigger field: with rank one L it would still work, but the statement of the invariant should say Qbar_l. (This is for A1/B2 to settle.)
  Uses: S5 step 1 (P_1 = j_*L[1] simple): V = U_0, L irreducible (rank 1), j_! = j_* = j_{!*} at the roots because L has no inertia invariants there. OK. S5 steps 4-5 (P_{i+1} = j_{!*}(M_{i+1}[1]) simple): V = V' - Z (open in A^1), M_{i+1} irreducible lisse. OK, given irreducibility (2.9).
- **4.4.1 to 4.4.5 (pp. 114-117):** Here is a **mismatch with the draft**. The draft (List 1 item 6) says BBD 4.4 gives the "Artin-Gabber t-exactness of Psi, Phi". What 4.4.2 actually proves (OCR, p. 114) is only an upper estimate for the nearby-cycle functor psi: it sends D^{<= 0} to D^{<= 0} for the self-dual perversity (the section is titled "Cycles evanescents (estimations superieures)"). BBD say that t-exactness would follow if one also knew, "vrai, mais non prouve dans ces notes", that psi commutes with duality. So BBD 4.4 does not state full t-exactness. Full t-exactness of Psi and Phi is outside the BBD text (Illusie, Gabber). Whether the induction needs the full statement is a question for A1/A2 (Laumon's local theory); the proof of the partial statement read (4.4.5) uses Artin vanishing-type dimension counts, no weights.
- **Weights in BBD:** weights enter from chapter 5 (La perversite autoduale: poids) on, as the table of contents of the dump shows; chapter 4's last sections (4.4, 4.5) are preparation for the purity theorem 5.3.4 (BBD says so at the start of 4.4) but the statements above do not use it.

### 2.7 Items used but not in the draft's List 1 (inputs to add)

1. **H^*_c(G_a, L_psi) = 0** ("Sommes trig." Thm 2.7*, p. 92, with Lemma 2.8; read, clean text): for G_0 a connected commutative algebraic group over F_q and chi a nontrivial character of G_0(F_q), H^*_c(G, F(chi)) = 0. Proof: Lang torsor, translation by rational points acts on H_c by the identity (homotopy argument, Lemma 2.8) and by multiplication by chi(g)^{-1}. No weights. Used in S7(a) through the computation of R pr_! L_psi(hQ_c). OPENED.
2. **BBD 4.2.8** (external product t-exact): above.
3. **BBD 2.2.18, Rapport 2.9-2.11 and Weil II 1.1** (Q_l and Qbar_l formalism): the first two read, the third NOT OPENED.
4. **Middle extension on a curve is j_*:** j_{!*}(M[1]) = (j_*M)[1], BBD 2.1.11 (NOT OPENED) with "Dualite" 1.3 (read).
5. **Definition and properties of L_psi and L_chi(f)** (Lang torsor, trace of Frobenius): "Sommes trig." 1.x, 2.x; not opened here beyond 2.7*.

## 3. Findings: errors, gaps and mismatches in the draft's use of the standard theorems

None of the cited standard theorems is wrong as stated in the draft, and I found no use whose hypotheses fail. Findings, from the most to the least relevant:

1. **BBD 4.4 is only half of what List 1 item 6 says** (2.6): it is an upper estimate for psi, not t-exactness of Psi and Phi. Class: repairable; the draft's own steps S0-S12 do not use psi or phi directly; a reader of Laumon's chapter 2 must check whether the full statement is needed.
2. **Stacks gives only torsion coefficients** (all of 2.2, 2.3): the Q_l and Qbar_l statements rest on SGA 5 V-VI (Jouanolou), Ekedahl and Weil II 1.1, none opened. The draft's List 1 says "SGA 4 XVII, XVIII ... weight-free (HINT)". The honest label for the Q_l versions: CITED, passage to the limit NOT OPENED; the ones opened here are the torsion versions and Rapport 2.9-2.11. Class: cosmetic as to truth (this is the standard formalism), but the draft's label "OPENED" would be an overstatement for them.
3. **Compact-support Kunneth for Q_l** (2.2a): not stated in any source I could read. For the uses in the draft it follows from the proper-factor Kunneth (Stacks 0F14), since A^1 = P^1 minus a point and j_!L extends by zero. Frobenius equivariance of the Kunneth isomorphism is not in Stacks (Stacks even notes that compatibility with the cup product is not written out); it follows from naturality (Rapport 1.3). Class: repairable, the draft should say this.
4. **SGA 1 V 8.2 is cited for the wrong form of the statement** (2.9 below): 8.2 is about the generic point of S; the draft uses it for an open dense V - Z in V. One line repairs it. Class: cosmetic.
5. **Unlisted inputs** (2.7): H^*_c(G_a, L_psi) = 0, BBD 4.2.8, and the coefficient formalism. Class: cosmetic as to truth.
6. **Trace formula, Stacks vs SGA 4 1/2:** Stacks' own statement 64.2 is "slightly wrong as stated" per its own text (web, summarised) and its proof of 64.16.1 is said to have "INSERT REFERENCE" placeholders and a list of gaps (64.21). The draft should cite the Rapport (Thm 3.2), not Stacks, for the Q_l version. Class: cosmetic.
7. **The trace formula rests on Weil's 1948 fixed-point theorem for curves** (Rapport 5.3). Not a weight statement, and not the Riemann hypothesis for curves; but a reader who forbids "Weil's theorem of 1948" in any form should know that the input comes from the same book. Class: scope note, not an error.
8. **BBD 4.3.1 is stated with coefficients Q_l (or E_lambda)** and "irreducible" must be read over Qbar_l (2.6). Class: repairable wording in the invariant (I_i).

No error found that breaks a step.

## 4. SGA 1 V 8.2, item 9, in detail

**Statement (read, SGA 1 V p. 143-144, clean text).** Prop. 8.2: S a connected, locally noetherian, normal prescheme, K = k(s) its function field, Omega an algebraically closed extension of K giving geometric points a' of Spec K and a of S: then pi_1(Spec K, a') -> pi_1(S, a) is surjective; its kernel corresponds to the extensions of K unramified over S. The first assertion is that the inverse image over Spec K of a connected finite etale cover of S is connected, equivalently integral, which is SGA 1 I.10.1.
**The draft's use (S5 step 5):** pi_1(V - Z) -> pi_1(V) surjective, V - Z dense open in the connected smooth curve V. The composite pi_1(Spec K) -> pi_1(V - Z) -> pi_1(V) is surjective by 8.2 (V is connected, normal, noetherian; V - Z is connected, also normal, with the same function field and the same generic point), so the second map is surjective. Hypotheses hold: V smooth (normal), connected, noetherian. PROVED from 8.2 in one line. Consequence used: an irreducible lisse sheaf M' on V stays irreducible on V - Z, because the image of the representation is unchanged. For a continuous l-adic representation "irreducible" depends only on the image subgroup: fine.
**Weights:** none; the proof of 8.2 is the one-line reduction to I.10.1 (connected etale cover of a normal scheme is integral). I read the whole proof.

## 5. Weights: per-item answers, and how I know

- Trace formula: no weights in the text read (grep, evidence.txt); proof route Weil's fixed-point theorem. HINT for the unread inner proofs.
- Kunneth, base change, projection formula, excision, Leray: the Stacks proofs (as summarised) use no weights or Frobenius (Stacks lists are formal or about torsion sheaves); none of the statements involves Frobenius. HINT, since pages were summarised.
- Artin vanishing: BBD says 4.1.1 reformulates SGA 4 XIV 3.1 (1963-64). Weight-free (CITED statement of the source).
- Duality on curves: proof read (Dualite 1-2): no weights (grep).
- GOS: statement none; proof not read; HINT.
- BBD chapter 4: statements read; proofs of 4.1, 4.3 read: no weights. Chapter 5 is where weights begin. 4.4 prepares 5.3.4 but its statement is a one-sided estimate.
- KL 2.1.3, 2.1.5: proofs read (2.1.3 in the appendix; 2.1.5 (i), (ii)): no weights. KL's use of Deligne's weight theorem begins at 2.2.1 (and in 2.3.1 (ii): sheaves "ponctuellement purs de poids"), which the draft does not cite; 2.1.5 (iii) uses 1.1.9 (v) and 1.2.2 (v), not read. In "Sommes trig." weights first appear at 1.17 (line 6350 of SGA4h.txt), outside the passages cited here.
- SGA 1 V 8.2: no weights.

## 6. Where each cited statement was read (for PROOF_V2)

| Statement | Source | Location | Quality |
|---|---|---|---|
| Trace formula for Q_l-sheaves | SGA 4 1/2, Rapport Thm 3.2 | p. 38 | text layer, clean |
| Frobenius correspondence, functoriality, Leray with Frobenius | Rapport 1.2-1.4, 1.8 | pp. 34-36 | clean |
| Q_l-sheaves, H_c of Q_l-sheaves | Rapport 2.9-2.11 | p. 38 | clean |
| Weil's fixed point theorem on a curve | Rapport 5.3 | p. 45-46 | clean |
| H^*_c(G_a, L_psi) = 0 | Sommes trig. 2.7*, 2.8 | p. 92 | clean |
| GOS | Sommes trig. 3.2.1 | pp. 92-93 | clean |
| Poincare duality, open curve | Sommes trig. 3.3; Dualite 2.1, 2.2 | pp. 93; 76-77 | clean |
| D j_* = j_* D | Dualite 1.3 | p. 75 | clean |
| Artin vanishing for perverse sheaves | BBD 4.1.1, 4.1.2 | pp. 102-103 | OCR |
| External product t-exact | BBD 4.2.8 | section 4.2 | OCR |
| Simple perverse sheaves | BBD 4.3.1 (with 4.3.2-4.3.4) | pp. 112-113 | OCR |
| Nearby cycles upper estimate | BBD 4.4.2 | p. 114 | OCR |
| Forget supports for FT; FT base change, duality, perversity | KL 2.1.3, 2.1.5; proofs in 2.4 | pp. 154-159 | OCR |
| pi_1 surjectivity | SGA 1 V 8.2 | pp. 143-144 | clean |
| Kunneth (RGamma), Leray, excision, projection formula, base change for Rf_! | Stacks 0F14, 0F1P, 03QC, 095L, 0GL5, 0F7L, 0F7J | | web, summarised |

Printed page numbers are from the page headers of the text layers; the BBD and KL numbers come from OCR page footers and could be off by one.

## 7. Not done / open

- Raynaud's proof of GOS and Weil's/Lang's proof of the fixed-point theorem were not opened: weight-freeness of their proofs is a HINT.
- The Stacks tag pages were not read verbatim; the numbers of tags and lemmas must be confirmed against the live pages. Stacks 63.10.5 (open-closed triangle for Rf_!) and 59.91.11 (proper base change) were not opened (snippets).
- Compact-support Kunneth for Q_l, and Weil II 1.1 / Ekedahl for Qbar_l: not opened.
- BBD 2.1.11 (IC on curves) and the proofs of KL 1.1.9 (v), 1.2.2 (v): not opened.
- No page image was opened (BBD has no images on disk; the SGA 4 1/2 text layer is clean; KL text OCR is legible; Laumon is A1/A2's).
- I did not re-derive the induction S5 or the global side S4, S7-S10 (A1 and A4 do); I only checked the hypotheses of the standard theorems at the points where S4, S5, S7, S8, S11 use them.
