# LIT-primary-sources (round 2, literature agent)

Scope: character sums over finite fields (Weil 1948 is a theorem). The question is only whether the route of the note is valid and what it needs. Nothing here says anything about the Riemann Hypothesis for the integers.

Method. The fetch tool could not read scanned PDFs, but it saved each PDF to disk. I extracted the OCR text layers with PyMuPDF (scripts `compute/LIT/probe.py`, `compute/LIT/dump.py`; text dumps in `compute/LIT/`: `BBD.txt`, `LAU.txt`, `KL.txt`, `SGA4h.txt`, `SGA1.txt`, `ETUDE.txt`, `TRAVL.txt`, `FU.txt`, `MELLIN.txt`, `DR.txt`; line numbers below refer to these dumps). The text layers are OCR, so quotations carry OCR noise (I normalised accents). "OPENED" = I read the numbered statement in a text I actually obtained. "NOT OPENED" = only a search summary, or the numbered statement was not found. Weights remark: no argument below uses weights; I only report whether the cited proofs do. CHECKED = a text search (grep) of a dump; it checks the OCR text, not the mathematics.

## Summary table

| # | Wanted | Status |
|---|---|---|
| 1 | Artin vanishing, BBD 4.1.1, 4.1.2 | OPENED (BBD, Asterisque 100, p. 103). SGA 4 XIV 3.1, 3.2 themselves: NOT OPENED; BBD's reformulation and Deligne's pointer to them are OPENED |
| 2 | Laumon 1.2.2.1, 1.3.1.1, 1.3.2.3; Katz-Laumon 2.1.3 | OPENED. No weights in the proofs of these statements (grep) |
| 3 | Concentration for chi(g) psi(F) | Deligne "Sommes trig." Theoreme 8.4: does NOT exist in the edition I opened (section 8 has only 8.1-8.3). Katz Asterisque 79 chap. 4-5: NOT OPENED (over the 10 MB fetch limit). Denef-Loeser, Adolphson-Sperber: NOT OPENED; their statements OPENED as quoted by Fu (arXiv math/0607164) |
| 4 | Tame pi_1 of A^1 | OPENED: SGA 1 XIII Corollaire 2.12 |
| 5 | Picard-Lefschetz, SGA 7 XV 3.4 | NOT OPENED (Deligne's Expose XV). The statement as recalled by Katz in SGA 7 XVIII 6.5 is OPENED |
| 6 | Sums of C(r)C(ar+b); iterated Fourier/Kummer | Nothing found for this exact sum. Related theory OPENED or partly OPENED (Katz "Convolution and Equidistribution", FKM "sums of products", Dettweiler-Reiter) |

---

## 1. Artin vanishing

### 1a. BBD, "Faisceaux pervers", Asterisque 100 (1982), 4.1.1 and 4.1.2 (volume p. 103). OPENED
URL opened: https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/BBD-pervers-2x.pdf (scan with OCR layer; `BBD.txt` lines 11770-11935).
- CITED. BBD 4.1: "Le theoreme suivant reformule le theoreme SGA4 XIV 3.1 de M. Artin. Theoreme 4.1.1. Si f : X -> Y est un morphisme affine, le foncteur Rf_* : D^b_c(X, Q_l) -> D^b_c(Y, Q_l) est t-exact a droite." (Rf_* maps pD^{<=0} into pD^{<=0}.)
- CITED. "Par application de la dualite de Verdier, le theoreme 4.1.1 se dualise en le Corollaire 4.1.2. Sous la meme hypothese, Rf_! est t-exact a gauche." (Rf_! maps pD^{>=0} into pD^{>=0}.)
- CITED. BBD 4.1.4: for X affine over an algebraically closed field, H^i(X,F)=0 for i > dim X (this is SGA 4 XIV 3.2; the text says "4.1.1 fournit le corollaire SGA4 XIV 3.2"). BBD 4.1.5: k algebraically closed, K in pD^{<=0}(X), u: Z -> X quasi-finite with Z affine: H^i(Z,K)=0 for i>0.
- Which vanishes where. For K perverse on an affine X over an algebraically closed field: H^i(X,K) = 0 for i > 0 (ordinary cohomology, positive degrees; 4.1.1, 4.1.5) and H^i_c(X,K) = 0 for i < 0 (compact support, negative degrees; 4.1.2). Applied to K[k-1] on the affine (k-1)-dimensional hypersurface Y this is the lower half of round one, H^j_c(Y,K)=0 for j < k-1. The citation agrees with round one. The upper half (j > k-1) is not given by this theorem.
- Proof of 4.1.1 in BBD: reduces to Z/l^n coefficients and then to Artin's theorem; the text says "C'est ce qu'affirme SGA4 XIV 3.1." No weights.
- BBD 4.1.9 is announced in the text as "L'enonce essentiel est 4.1.9 (non demontre ici)" (line 1690). I did not open the statement of 4.1.9, so the round-one step "restriction of a perverse sheaf to a divisor with affine complement, shifted by -1, satisfies the cosupport condition" is not confirmed here. OPEN as a primary-source check.

### 1b. SGA 4, Expose XIV, Theoreme 3.1 and Corollaire 3.2 (Artin). NOT OPENED directly
I could not obtain the text of SGA 4 tome 3. What I opened:
- BBD 4.1 (above) says 4.1.1 "reformule SGA4 XIV 3.1" and 4.1.4 is "SGA4 XIV 3.2".
- Deligne, SGA 4 1/2, "Th. finitude" 4.6.4 (retypeset edition, https://matematicas.unex.es/~navarro/res/sga/SGA%204%20%26%20HALF%20Cohomologie%20Etale.pdf; `SGA4h.txt` line 1675). CITED: "Theoreme 4.6.4 (dimension cohomologique des schemas affines). Soient X un schema affine de type fini sur un corps separablement clos et F un faisceau de torsion sur X. Alors on a H^q(X, F) = 0 pour q > dim(X). Pour la tres jolie demonstration nous renvoyons a [AGV72], XIV paragraphes 2 et 3." So Artin's theorem is cited, not reproved, there.

## 2. The l-adic Fourier transform

Opened: Laumon, "Transformation de Fourier, constantes d'equations fonctionnelles et conjecture de Weil", Publ. IHES 65 (1987) 131-210 (https://www.numdam.org/item/10.1007/BF02698937.pdf; `LAU.txt`). Katz-Laumon, Publ. IHES 62 (1985) 145-202 (https://web.math.princeton.edu/~nmk/old/TFandmajSE.pdf; `KL.txt`). Katz, "Travaux de Laumon", Sem. Bourbaki 691 (1987-88) (https://web.math.princeton.edu/~nmk/old/travlaumon.pdf; `TRAVL.txt`).

Setting in Laumon chapter 1: E -> S a vector bundle of rank r over a scheme S over a field of characteristic p, psi a nontrivial additive character, F_psi(K) = R pr'_! (pr^* K tensor L_psi(<,>))[r].

- CITED. Laumon Theoreme (1.2.2.1) (involutivity): for F'_psi the transform on the dual bundle E' -> S, "on a un isomorphisme fonctoriel F'_{psi'} o F_psi (K) ~= a^* K (-r) pour K in D^b_c(E, Q_l)" (a = the map e -> -e; the OCR garbles the symbols, the shape F' F K = K(-r) up to the sign map is clear). Proof (volume pp. 141-143): proper base change (SGA 4 XVII 5.2.6), projection formula (XVII 5.2.9), cohomology of A^r (SGA 5 VII 1.1), and Prop. 1.2.2.2. Corollaire 1.2.2.3: F_psi is an equivalence of triangulated categories with quasi-inverse a^* F'(-)(r).
- CITED. Laumon Theoreme (1.3.1.1) ("forget supports"): "Pour tout K in D^b_c(E, Q_l), la fleche d'oubli des supports R pr'_!(pr^* K tensor L_psi) -> R pr'_*(pr^* K tensor L_psi) est un isomorphisme." Laumon: "Cet enonce n'est autre que [Ka-La] (2.1.3)". It is proved in [Ka-La] together with 1.3.1.2 ([Ka-La] 2.4.4: P^1 x A^1 -> P^1 is universally strongly acyclic for j_! L_psi(xy)).
- CITED. Laumon Theoreme (1.3.2.3): "F_psi transforme les Q_l-faisceaux pervers sur E en Q_l-faisceaux pervers sur E'. Le foncteur F_psi : Perv(E) -> Perv(E') est une equivalence de categories abeliennes de quasi-inverse a^* F'(-)(r)." Proof (volume p. 147): pr smooth of relative dimension r, so pr^*(-)[r] is t-exact ([B-B-D] 4.2.5); pr' is affine, so one of pr'_*, pr'_! is t-exact on the left ([B-B-D] 4.1.2 quoted) and the other on the right ([B-B-D] 4.1.1); by 1.3.1.1 the two functors are equal, hence F_psi is t-exact. (The OCR does not reliably show which subscript goes with which; BBD 4.1.1 and 4.1.2 in 1a are the authority.)
- CITED. Laumon 1.3.2.1 and 1.3.2.2: F_psi commutes with Verdier duality up to a Tate twist; a consequence of 1.3.1.1.
- CITED. Katz-Laumon Theoreme (2.1.3): "La fleche naturelle d'oubli des supports F_!psi(-) -> F_*psi(-) est un isomorphisme de foncteurs" (for good F_q-schemes S). Proof in the Appendice (2.4), Theoreme 2.4.1 with torsion coefficients: induction on r to r = 1, E = A^1_S; then the map is shown to be an isomorphism at the point at infinity using translation, the projection formula for j_!, and the Artin-Schreier covering t^p - t = xy with its compactification (finite Galois, totally ramified over infinity x G_m). Also Theoreme 2.4.4 (P^1 x A^1 -> P^1 universally strongly locally acyclic for j_! L_psi). Katz's Bourbaki account calls the statement "Theorem 1 (Verdier)" and says "Verdier's proof, never published", sketched by involutivity plus duality.

Do the proofs use weights? CHECKED by grep on the dumps:
- Laumon chapter 1 (`LAU.txt` lines 244-765): no "poids", no "pur" other than "purement de dimension relative r", no "Weil II". Weights first enter in the introduction (describing chapter 4) and in chapter 4 (lines 2956ff: "i-pur", [De 4], "La conjecture de Weil II").
- Katz-Laumon Appendice (2.4) (`KL.txt` lines 508-668): no "poids", "pur", "Weil", "Frobenius", "Deligne". Weights enter after it (Theoreme 2.2.1 "Si K est pur de poids m ... F(K) est pur de poids m + r", lines 475-477, obtained from Deligne [8] 6.2.3 and 2.1.3).
- So involutivity, forget-supports and perverse exactness are weight-free as stated and proved there; their inputs are SGA 4 base change and projection formula, Artin vanishing (BBD 4.1.1, 4.1.2) and local acyclicity. Not checked: that every sub-result they cite (BBD 4.2.5, SGA 4 XVII 5.2.6, 5.2.9) is weight-free. Not checked: Laumon chapters 2-3. This supports (CITED) the main session's claim that Fourier-transform exactness needs no weights.
- Katz-Laumon's actual bound for exponential sums does use weights (Weil II); I opened only sections 2.1-2.4.

## 3. Concentration theorems for sums of chi(g(x)) psi(F(x))

### 3a. Deligne, "Sommes trigonometriques" (SGA 4 1/2), "Theoreme 8.4": NOT FOUND
The retypeset edition (`SGA4h.txt` lines 5940-8590) has the chapter in sections 1 Principes, 2 Dictionnaire, 3 Sommes a une variable, 4 Sommes de Gauss et sommes de Jacobi, 5 Caracteres de Hecke, 6 Caracteres de Hecke definis par sommes de Jacobi, 7 Sommes de Kloosterman generalisees, 8 Autres applications. Section 8 has only 8.1, 8.2, 8.3 (remarks), so there is no Theoreme 8.4 in this edition. I could not check the original numbering. What is there (CITED):
- 3.5.2: for f a rational function on a smooth projective curve X_0 of genus g over F_q, not of the form g^p - g + const, |S_f| <= (2g - 2 + sum over x with v*_x(f) != 0 of [k(x):F_q](1 + v*_x(f))) q^(1/2). Proof: S_f = -Tr(F, H^1) (3.5.5) since F(psi_f) is nonconstant so only H^1 is nonzero; the dimension of H^1 comes from the Euler-Poincare formula (3.2.1) and the Swan conductor; then "chacune de valeurs absolues complexes q^(1/2)", which is Weil's theorem (3.4). Uses weights.
- 3.8: for P in F_q[X_1..X_n] of degree d not of the form Q^p - Q + const, |sum psi(P)| <= (d+1) q^(n - 1/2), by a Lang-Weil style induction from 3.5.2. Uses weights through 3.5.2.
- 7.4, 7.8: Kloosterman sums; cohomology of the variety {x_1...x_n = a} with the Kloosterman sheaf concentrated in one degree.
No statement of the shape "a multivariable sum of chi(g)psi(F) is concentrated in one degree under a hypothesis on F" is in the sections I read.

### 3b. Katz, "Sommes exponentielles", Asterisque 79 (1980), chapters 4-5: NOT OPENED
The Princeton copy (https://web.math.princeton.edu/~nmk/sommesexp.pdf) and the Numdam copy exceed the fetch limit of 10 MB. The SMF sample (`KSAMPLE.txt`) contains only title and avant-propos. The English translation (arXiv 2308.11611) is withdrawn by its author, and its PDF URL returned 404. No statement to quote. OPEN.

### 3c. Denef-Loeser (Invent. Math. 106 (1991) 275-294), Adolphson-Sperber: NOT OPENED. Statements OPENED through Lei Fu, "Twisted exponential sums", arXiv math/0607164 (`FU.txt`)
Fu: "Our results complete those in [DL], where the case of trivial chi_i is treated."
- Setting. k finite of characteristic p, K_chi the Kummer sheaf of chi: k^{*n} -> Q_l^* on the torus T^n, L_psi the Artin-Schreier sheaf, f a Laurent polynomial, Delta_infty(f) = convex hull of {0} and the support of f; f is non-degenerate w.r.t. Delta_infty(f) if for every face tau not containing 0 the locus d f_tau/dX_1 = ... = d f_tau/dX_n = 0 in T^n is empty.
- CITED. Fu Theorem 0.1: if f is non-degenerate and dim Delta_infty(f) = n, then (i) H^i_c(T^n_kbar, K_chi tensor f^*L_psi) = 0 for i != n; (ii) dim H^n_c = n! vol(Delta_infty(f)); (iii) if 0 is an interior point of Delta_infty(f), H^n_c is pure of weight n. Fu says (i) and (iii) follow from [DL] Theorem 1.3 applied to f(X_1^{q-1}, ..., X_n^{q-1}).
- CITED. Fu Corollary 0.2: |sum over x_i in k^* of chi_1(x_1)...chi_n(x_n) psi(f(x))| <= n! vol(Delta_infty(f)) q^(n/2). The proof uses Deligne [D] 3.3.1 (an upper bound on weights).
- CITED. Fu Corollary 0.3: for F = f(x) + x_{n+1} f_1(x) + ... + x_{n+m} f_m(x), non-degenerate with dim Delta_infty(F) = m+n: |sum chi_1(f_1(x))...chi_m(f_m(x)) psi(f(x))| <= (n+m)! vol(Delta_infty(F)) q^(n/2), chi_i nontrivial (via the Gauss sum G(chi_i, psi)).
- CITED. Fu Remark 0.6: Corollary 0.5 with Theorem 0.1 "is Theorem 4.2 in [AS], except that Adolphson and Sperber prove the theorem for almost all p." Adolphson-Sperber is p-adic (Dwork); not opened. HINT.
- Do the proofs use weights? Fu's (iii) is a purity statement and his Cor. 0.2 uses a weight bound. Denef-Loeser use intersection cohomology on a toroidal compactification and compute weights (the title; HINT, text not read). Fu states his own proof of 0.1 is independent of [DL] (not read).

Relevance to the route (HINT, not proved). By Fu's Gauss-sum trick the route's sum, sum over x of chi(f(x_1))...chi(f(x_k)) psi(h Q_c(x)), is a sum of psi(F) over 2k variables, F = h Q_c(x) + y_1 f(x_1) + ... + y_k f(x_k), over the torus only (all variables nonzero); the route sums over all of F_q^k. The cited theory then gives a bound with a factorial constant in k and uses weights; so (a) it is a different, weight-using route, (b) circular for the toy case, (c) not the uniform-in-k statement (S_k) or (W*). I did not check non-degeneracy of this F. OPEN.

## 4. Tame fundamental group of the affine line

SGA 1 (Grothendieck, Revetements etales et groupe fondamental), Expose XIII (Mme Raynaud), Corollaire 2.12. OPENED in the LaTeX edition https://arxiv.org/pdf/math/0206203v1 (`SGA1.txt` lines 13852-13870).
- CITED. "Corollaire 2.12. Soit X une courbe propre et lisse connexe de genre g sur un corps separablement clos k de caracteristique p >= 0. Soit U l'ouvert obtenu en enlevant a X n points fermes distincts a_1, ..., a_n. Alors le groupe fondamental moderement ramifie pi_1^t(U) peut etre engendre par 2g + n elements x_i, y_i, sigma_j, tel que sigma_j soit un generateur d'un groupe d'inertie correspondant a a_j, et que l'on ait la relation prod_i (x_i y_i x_i^-1 y_i^-1) . prod_j sigma_j = 1 (*)." The statement continues: pi_1^{p'}(U) is the pro-p'-group generated by the x_i, y_i, sigma_j with the single relation (*).
- PROVED from 2.12. g = 0, X = P^1, n = 1: pi_1^t(A^1) is generated by sigma_1 with relation sigma_1 = 1, so it is trivial. For P^1 minus n points: pi_1^t is the quotient of the free pro-p' group on sigma_1..sigma_n by prod sigma_j = 1. Dividing by the normal subgroup generated by sigma_1..sigma_{n-1} (the finite points) kills sigma_n too, so the quotient is trivial. This is the group-theoretic content of suggestion S-c. Caveat (HINT): each sheaf must factor through pi_1^t, i.e. be tame at infinity and at the finite points; wild ramification breaks the argument (the Artin-Schreier cover of A^1 is a quotient of pi_1(A^1), not of pi_1^t).
- Katz (SGA 7 XVIII, proof of 6.1.10) uses "SGA 1 XIII 2.16" for "pi_1^t(D - D cap X) est engendre par les groupes d'inertie en les differents points". I did not locate the text of 2.16 in `SGA1.txt`: NOT OPENED as a numbered statement.

## 5. Picard-Lefschetz in odd characteristic, SGA 7 II, Expose XV (Deligne), Theoreme 3.4: NOT OPENED
No copy of Expose XV was obtained. I opened Katz, SGA 7 Expose XVIII (https://web.math.princeton.edu/~nmk/old/etudecoho.pdf; `ETUDE.txt` lines 2695-2900), which recalls the statement under "Un rappel sur la formule de Picard-Lefschetz (XV 3.4)".
- CITED as recalled by Katz: "Soient S le spectre d'un anneau de valuation henselien strict, eta son point generique, eta-bar un point geometrique au-dessus de eta, s son point ferme. Soit p: X -> S un morphisme propre, avec X un schema regulier connexe de dimension n, tel que p est lisse en dehors d'un point x, point qui se trouve dans la fibre speciale, et qui est une singularite quadratique ordinaire de la fibre speciale. Designons par I le groupe d'inertie de S en s. On sait (XV 3.4) que I agit trivialement sur H^i(X_eta-bar, Q_l) pour i != n-1, et que son action sur H^{n-1}(X_eta-bar, Q_l) est donnee par les formules suivantes." Case n = 2m+1: I acts through a quotient Z/2 (if the characteristic is not 2 there is exactly one such quotient), vanishing cycle delta determined up to sign, nontrivial element acts by x -> x - (-1)^m (x.delta) delta. Case n = 2m+2: I acts through its tame quotient t_l(1) by the transvection x -> x - (-1)^m a (x.delta) delta.
- Katz's introduction to XVIII says the monodromy group of a Lefschetz pencil acts irreducibly on vanishing cohomology except for dim X odd and characteristic 2, using Picard-Lefschetz and SGA 1 XIII 2.16.
- Also opened: Katz SGA 7 XVII (https://web.math.princeton.edu/~nmk/old/pinclef.pdf; `PINCLEF.txt`), existence of Lefschetz pencils; it refers to "la formule de Picard-Lefschetz de Exp. XV".
- Weights: XV predates weights (1973); the statement is about the inertia action. I did not read its proof. HINT.

## 6. Sums of C(r)C(ar+b); the iteration "Fourier transform, multiply by Kummer, repeat"

Exact sum, sum over r of C(r) C(a r + b) with C(r) = sum over x of chi(f(x) f(r x)): I found no source that treats it. Katz, "Convolution and Equidistribution" (Annals of Math Studies 180, 2012; https://web.math.princeton.edu/~nmk/mellin398.pdf; OPENED, 200 pages, `MELLIN.txt`): its introduction treats chi_2(f(x)) sums for f squarefree cubic and the Mellin transform side; grep for "f(rx)" and "sums of products" finds no matching theorem (CHECKED on OCR text only). Absence is not evidence of novelty.

Related theory:
- Fouvry-Kowalski-Michel, "A study in sums of products" (https://ar5iv.labs.arxiv.org/html/1405.2293, first 100k characters OPENED). CITED: Proposition 1.1: if H^2_c(A^1 x Fbar_p, tensor F_i tensor D(G)) = 0 then the sum is at most C sqrt(p); "all estimates will be derived using, ultimately, the following application of the Riemann Hypothesis over finite fields." Theorem 1.5 applies to a "bountiful" sheaf (middle extension, pointwise pure of weight 0, rank >= 2, geometric monodromy SL_r or Sp_r, trivial projective automorphism group); vanishing comes from Tannakian/Goursat arguments on monodromy (Def. 2.1, Thm 2.7, Lemma 2.8). The family y^2 = f(x)(x - z) was not seen in the part read. So the standard way coinvariants are shown to vanish uses weights (the main session's section 3 circularity worry, supported at the level of this paper's own statement).
- Katz, "Rigid local systems" (Annals of Math Studies 139, 1996): NOT OPENED. A table of contents (search summary) lists 2.9 "Middle additive convolution with Kummer sheaves" and 2.10 "Interpretation of middle additive convolution via Fourier Transform". Dettweiler-Reiter, "On the middle convolution", arXiv math/0305311 (`DR.txt`) is over C (local systems on a punctured line); its Theorem 4.4: MC_lambda(F) ~= R^1(pbar_2)_*(j_*(p_1^*F tensor q^*L_lambda)). Not a finite-field statement; CITED only.
- So the iterated Fourier/Kummer construction exists in the literature as middle convolution, but I found no concentration or vanishing statement for the specific iteration of the route. OPEN.

## What this says about the five suggestions (limited to what the sources can say)

- S-a. The lower-half Artin step is CITED correctly (BBD 4.1.2). The forget-supports isomorphism for the Fourier transform is CITED (Laumon 1.3.1.1 = Katz-Laumon 2.1.3) and weight-free by grep. No theorem found gives "H_c -> H is an isomorphism for (Y, K[k-1])" on the quadric Y. OPEN.
- S-c. The tame fundamental group fact is PROVED from SGA 1 XIII 2.12 as above, with the caveat that every sheaf involved must be tame at infinity.
- S-b, S-d, S-e: not tested against any primary source here.
- Circularity map. Weight-free: Laumon ch. 1, Katz-Laumon appendix, BBD 4.1, SGA 1 XIII 2.12. Weight-using: Katz-Laumon bounds, FKM sums of products, Denef-Loeser purity, Fu (iii), SGA 4 1/2 3.5.2 and 3.8.

## Not opened, in one list
SGA 4 XIV 3.1 and 3.2 (the text itself); BBD 4.1.9 and 4.2.5; Katz Asterisque 79 chapters 4-5; Denef-Loeser; Adolphson-Sperber; the original numbering of Deligne's "Sommes trig." (no 8.4 in the retypeset edition); SGA 1 XIII 2.16; SGA 7 XV 3.4 itself; Katz "Rigid local systems" 2.9-2.10; Laumon chapters 2-3 for weights; Katz-Laumon beyond section 2.4.

Written 2026-11-20 UTC.
