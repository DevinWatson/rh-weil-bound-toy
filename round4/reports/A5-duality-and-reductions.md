# A5. The lower bound (S11) and the reductions (S0), round four

Scope: character sums over finite fields (Weil 1948). Nothing here concerns the Riemann Hypothesis for the integers.
Labels: PROVED, CITED (source, and whether I READ it), CHECKED (script and output file), OPEN, HINT.
Scripts and outputs: `round4/compute/A5/` (`lfun.py`, `run_sym.py`, `run_more.py`, `out_sym_odd.txt`, `out_more.txt`). All arithmetic is exact integers (tables for F_q, resultants over F_q, Fractions); no floating point anywhere.
No weights, purity, Weil bound or Weil conjectures are used anywhere below. Where I say "the cited theorem's proof does not use weights" I give the reason and mark how far I verified it.

## 0. Summary of results

- S11 (lower bound by duality): the argument of the draft is correct in outline. I wrote it in full (section 2) with the two local computations the draft skipped (the roots, and Rj_* = j_!). It rests on one standard theorem, Poincare duality for a smooth curve with a lisse sheaf, plus the Grothendieck trace formula and a local computation of inertia cohomology. **None of the cited statements was OPENED by me at a readable source** (my one attempt, Milne's Lectures on Etale Cohomology, returned only the table of contents entry "24 Poincare Duality"; the Stacks Project has no etale duality-for-curves page that my search could find). So S11 is PROVED modulo CITED-NOT-OPENED statements. I found no error in it.
- S0 (reductions): written in full (section 3), PROVED, with the exact statement the later steps need. The draft's one-line statement "it suffices to prove |alpha_i|^s <= q^{s/2}-type bounds" is imprecise (cosmetic); the order of choices (Q first, then a, then c) must be stated, because the set of root ratios of S3 depends on a (repairable gap in exposition, no mathematical error).
- Exact checks (section 4): 33 random cases (q in {3,5,7,9,11,13,25}, d in {3,5,7}) of the L-polynomial computed from F_q[x] arithmetic alone: palindromic symmetry a_{2g-i} = q^{g-i} a_i holds in all 33, and the coefficients of degree >= d vanish. Cross-checks: agreement with direct point counting over F_{p^n}, n <= 6 (5 cases), base change F_3 -> F_9 and translation (3 cases, 22 translations), and an even-degree control where the symmetry of the full (d-1)-dimensional H fails exactly as the theory predicts (one unpaired eigenvalue +-1).
- A byproduct (PROVED, elementary, section 1.3): the Dirichlet series D(u) = sum over monic g of chi(Res(g,f)) u^deg g is a polynomial of degree <= d-1 and equals prod(1 - alpha_i u). This gives an independent, weight-free, cohomology-free proof that H has "dimension at most d-1", and a way to compute everything exactly.

## 1. Setting, definitions, and the identification of the alpha_i

Setting: p odd, q = p^e, f in F_q[x] squarefree of odd degree d >= 3, Z = roots in F-bar (d distinct), U_0 = A^1 - Z, chi the quadratic character of F_q.

### 1.1 The sheaf L (definition that makes base change and translation formal)
Let C0 = {(x,y): y^2 = f(x), f(x) != 0} -> U_0, (x,y) -> x. It is a finite etale double cover defined over F_q. pi_* Q_l = Q_l + L, where L is the rank one sheaf given by the sign character of the Z/2-torsor. PROVED consequences:
(a) L is a character of pi_1(U_0) with values in {+1,-1}, so L tensor L = Q_l (as Frobenius-sheaves over F_q), hence L = L^vee over F_q.
(b) The trace of geometric Frobenius at x in U_0(F_{q^n}) is chi_n(f(x)) (number of y with y^2 = f(x), minus 1), chi_n the quadratic character of F_{q^n}.
(c) L is geometrically nontrivial: the cover is geometrically connected because f is not a square in F-bar(x) (squarefree, nonconstant).
(d) Local monodromy. At a root z, f = u (x - z) with u a unit, so y^2 = u (x-z) is totally ramified of degree 2: inertia I_z acts on L through the order-two character, i.e. a generator sigma of tame inertia acts as -1. Tame because 2 != p. At infinity, with t = 1/x, f = t^{-d} (unit), valuation -d odd (d odd), so again totally ramified of degree 2 and I_inf acts by the order-two character (this is exactly where d odd is used). All of this is PROVED (local algebra).
Base change: the same definition over F_Q (Q = q^s) gives L_{chi_Q}(f), with chi_Q = chi o Norm. Pullback under an automorphism of A^1 commutes with forming the cover.

### 1.2 H and its Frobenius eigenvalues
j: U_0 -> A^1, H = H^1_c(A^1_{F-bar}, j_!L). Facts:
- H^0_c = 0 (PROVED: a section of j_!L with finite support restricts to a section of the lisse rank-one sheaf L on connected U_0 vanishing on a dense open set, hence zero; the stalk at Z is 0).
- H^2_c = 0 (CITED: H^2_c(U_0,L) = (coinvariants of pi_1^geom on L)(-1) by Poincare duality / top-degree compactly supported cohomology; L geometrically nontrivial of rank 1, so coinvariants vanish. Source not opened.)
- Dimension: Grothendieck-Ogg-Shafarevich: chi_c(U_0, L) = rank * chi_c(U_0) - sum of Swan conductors = (2 - (d+1)) - 0, Swan = 0 because L is tame (p odd, order 2). So dim H = d - 1. CITED (Raynaud / SGA 5 X, NOT OPENED). Independent corroboration: section 1.3 shows that the degree of the L-polynomial is at most d - 1, and the data in section 4 shows it equal to d - 1 in all cases tested.
- Trace formula (CITED, SGA 4 1/2 [Rapport] / [Fonctions L], NOT OPENED by me; A6 owns it): for every n, sum over x in F_{q^n} of chi_n(f(x)) = sum (-1)^i Tr(F^n | H^i_c) = - Tr(F^n | H). (Stalk trace at a root is 0, consistent with chi(0) = 0.) Hence sum_x chi_n(f(x)) = - sum alpha_i^n. Frobenius is an automorphism, so every alpha_i != 0.

### 1.3 The Dirichlet series D(u): an elementary identification (PROVED)
For monic g in F_q[x] set chi_f(g) = chi(Res(g,f)) where Res(g,f) = prod over roots theta of g (with multiplicity) of f(theta) (in F_q). Multiplicative in g (resultant is). For g = P irreducible of degree m, Res(P,f) = Norm_{F_{q^m}/F_q}(f(theta)), and chi_{q^m} = chi o Norm, so chi_f(P) = chi_m(f(theta_P)): the Frobenius trace of L at the closed point P (for f(theta) != 0), and 0 if P | f.
D(u) = sum over monic g of chi_f(g) u^{deg g} = prod over primes P of (1 - chi_f(P) u^{deg P})^{-1} (formal Euler product, multiplicativity).
Taking log: log D = sum_P sum_m chi_f(P)^m u^{m deg P}/m. And sum_{x in F_{q^n}} chi_n(f(x)) = sum over P with deg P | n of deg P * chi_f(P)^{n/deg P} (each closed point of degree m | n has m rational points over F_{q^n}, all with the same value chi_n(f(x)) = chi_m(f(theta))^{n/m}). Hence log D = sum_n (u^n/n) S_n, with S_n = sum_{x in F_{q^n}} chi_n(f(x)). By 1.2, D(u) = exp(-sum alpha_i^n u^n / n) = prod (1 - alpha_i u). PROVED (given the trace formula for the last identification).
Polynomiality, elementary: Res(g,f) = (-1)^{md} lc(f)^m * prod_{z in Z} g(z) for g monic of degree m. prod_z g(z) = Norm_{A/F_q}(g mod f) for A = F_q[x]/(f) = prod F_{q^{d_i}} (f squarefree). For m >= d the residue map from monic polynomials of degree m onto A is q^{m-d}-to-one and onto, so sum_{deg g = m} chi_f(g) = chi((-1)^{md} lc^m) q^{m-d} * sum_{r in A} chi(Norm r), and sum_{r in A} chi(Norm r) = prod_i (sum over F_{q^{d_i}} of the quadratic character) = 0. So the coefficients of D vanish for m >= d: D is a polynomial of degree <= d - 1. PROVED. (Checked exactly in section 4: coefficients of u^d, u^{d+1} are 0 in all cases.)

## 2. S11: the multiset {alpha_i} is stable under alpha -> q/alpha, hence |alpha| = sqrt q

**Theorem S11.** Under the setting above, the multiset {alpha_1,...,alpha_{d-1}} (Frobenius eigenvalues on H, with multiplicity) equals the multiset {q/alpha_1,...,q/alpha_{d-1}}. Consequently if for some embedding iota: Q-bar_l -> C one has |iota(alpha_i)| <= sqrt q for all i, then |iota(alpha_i)| = sqrt q for all i.

Proof.
Step 1 (local cohomology, PROVED). Let K = fraction field of the strict henselisation at a closed point b of P^1, I = Gal(K^sep/K), P the wild inertia (pro-p). For a Q_l-sheaf M on a punctured neighbourhood, with l != p, H^i(I, M) = H^i(I/P, M) (P pro-p, so H^i(P, -) = 0 for i > 0 on Q_l-vector spaces with continuous action; Hochschild-Serre) and I/P is procyclic (generated topologically by sigma, I/P = prod_{l' != p} Z_{l'}(1)); so H^0 = ker(sigma - 1), H^1 = coker(sigma - 1)(-1), H^i = 0 for i >= 2. By 1.1(d), sigma acts as -1 on L at every b in Z and at infinity. So RGamma(I_b, L) = 0 for b in Z union {infinity}. (The statement that the stalk of Rj_*L at a closed point is RGamma(I_b, L) is CITED, SGA 4 1/2 [Arcata] / SGA 4 VIII; NOT OPENED.)
Step 2 (PROVED from Step 1). On A^1, the stalk of Rj_*L at z in Z is RGamma(I_z,L) = 0, so Rj_*L = j_!L (as complexes). Let k: A^1 -> P^1. The cone of k_!(j_!L) -> Rk_*(j_!L) is supported at infinity with stalk RGamma(I_inf, L) = 0 (the stalk of j_!L at infinity-neighbourhood is L, and the local cohomology is that of inertia at infinity). Hence the forget-supports maps
 H^i_c(A^1, j_!L) = H^i_c(U_0, L) -> H^i(U_0, L) = H^i(A^1, Rj_*L)
are isomorphisms for all i, Frobenius equivariant. In particular phi: H = H^1_c -> H^1(U_0,L) is an isomorphism.
Step 3 (duality; CITED). Poincare duality on the smooth connected curve U_0 (over F-bar) with the lisse sheaf L: the cup product followed by the trace map gives a perfect pairing
 H^1_c(U_0,L) x H^1(U_0, L^vee) -> H^2_c(U_0, Q_l) = Q_l(-1),
compatible with the action of Frobenius over F_q (geometric Frobenius acts on Q_l(-1) by multiplication by q). Source: SGA 4 XVIII (Deligne, Dualite), the curve case 3.2.5 as I recall it; Milne, Etale Cohomology (1980) VI 11.1; Milne, Lectures on Etale Cohomology, section 24 (I saw only its title in the table of contents). **NOT OPENED** at the statement level. Weights: the proof is the formalism of Verdier duality (trace map, dualizing complex), l-adic limit; no weights appear (HINT: standard; I did not read the proofs).
Step 4 (the pairing on H). Using L = L^vee (1.1(a)) and phi from Step 2, B(x,y) = < x, phi(y) > is a perfect bilinear form on the (d-1)-dimensional space H with B(Fx, Fy) = q B(x,y). Then B(Fx, y) = q B(x, F^{-1} y), so the adjoint of F with respect to B is q F^{-1}. A map and its adjoint have the same characteristic polynomial (adjoint = transpose in suitable bases), so charpoly(F) = charpoly(q F^{-1}), i.e. the multisets {alpha_i} and {q/alpha_i} coincide. PROVED from Step 3.
Step 5 (the inequality, PROVED). Fix iota with |iota(alpha_j)| <= sqrt q for all j. For each i, q/alpha_i = alpha_j for some j (Step 4), so q/|iota(alpha_i)| = |iota(alpha_j)| <= sqrt q, i.e. |iota(alpha_i)| >= sqrt q. With the hypothesis, = sqrt q. (iota fixes q in Z.) QED.

Where the theorem uses oddness of d: only in Step 1 at infinity (sigma acts as -1 there). In the even case (leading coefficient a square) L is unramified at infinity, H^0(I_inf, L) = L_inf != 0 and H^1_c -> H^1 has a kernel/cokernel of rank 1 carrying one eigenvalue epsilon = +-1: see the control in section 4.3.

Alternative route (HINT/CITED, not used): the symmetry is the functional equation of the zeta function of the hyperelliptic curve y^2 = f(x) (one rational point at infinity, genus (d-1)/2), classically obtained from Riemann-Roch (F. K. Schmidt 1931; Rosen, Number Theory in Function Fields, Thm 5.9 as I recall; Stichtenoth, Algebraic Function Fields and Codes, Thm 5.1.15 as I recall) or for hyperelliptic curves from Gauss sums (Artin 1924). The identification of the L-polynomial of the curve with D(u) is the Euler product computation of section 1.3 (affine point count: #C(F_{q^n}) = q^n + 1 + S_n). None of these sources was read; this route is listed only as a second possible citation. Its proof uses no weights (Riemann-Roch), which predates Weil.

Status: S11 PROVED modulo (T) trace formula, (GOS) dimension formula, (PD) Poincare duality, (RJ) stalk of Rj_* = inertia cohomology. All four CITED, NOT OPENED by me.

## 3. S0 in full: the reductions

**Lemma S0.** Let (q, f) be as in the setting, s >= 1, Q = q^s, with Q > d. Then there exists a in F_Q with f(a) != 0. For every such a put f_a(x) = f(x + a) in F_Q[x]. Then:
1. f_a is squarefree of odd degree d over F_Q, with the same leading coefficient, f_a(0) != 0, and root set Z_a = Z - a.
2. With H_a = H^1_c(A^1_{F-bar}, j_!L_{chi_Q}(f_a)), the geometric Frobenius over F_Q acting on H_a has eigenvalues alpha_1^s, ..., alpha_{d-1}^s (with multiplicity), where alpha_i are the eigenvalues of Frobenius over F_q on H.
3. Hence any inequality proved for the eigenvalues of Frobenius over F_Q on H_a of the form |beta|^k <= Q^{(k+3)/2} gives |alpha_i|^{sk} <= q^{s(k+3)/2}, i.e. |alpha_i| <= q^{(k+3)/(2k)} = q^{1/2 + 3/(2k)}.

Proof.
Existence of a: f has at most d roots and F_Q has Q > d elements (PROVED).
1. Translation by a in F_Q is an F_Q-automorphism tau of A^1, tau^*(f)(x) = f(x+a) (PROVED). Squarefreeness, degree and leading coefficient are unchanged; roots are z - a; f_a(0) = f(a) != 0.
2. (i) Base change. H is by definition H^1_c(A^1_{F-bar}, j_!L) with Gal(F-bar/F_q) acting through the F_q-structure of (A^1, j_!L). The subgroup Gal(F-bar/F_Q) is the closed subgroup generated by Frob_q^s, and the F_Q-structure of (A^1, j_!L) is the base change of the F_q-structure (by 1.1 the cover defining L is defined over F_q, and its base change to F_Q is the cover defining L_{chi_Q}(f), whose trace function at x in F_{Q^n} is chi_{Q^n}(f(x)) = chi_{q^{sn}}(f(x))). So the geometric Frobenius over F_Q is F^s, and its eigenvalues on H are alpha_i^s with multiplicity (triangularise F). PROVED (definitions).
(ii) Translation. tau^* of the double cover y^2 = f(x) is the double cover y^2 = f(x+a), so tau^* L_{chi_Q}(f) = L_{chi_Q}(f_a) and tau^* j_! = j_{a!} tau^*, because tau^{-1}(Z) = Z_a. Since tau is an automorphism defined over F_Q, tau^*: H^1_c(A^1, j_!L) -> H^1_c(A^1, j_{a!} L(f_a)) is an isomorphism commuting with the F_Q-Frobenius (PROVED). So H_a = H as F_Q-Frobenius modules.
3. The s-th root of a real inequality is exact. PROVED.

Remarks needed by the later steps (cosmetic but the draft omitted them):
- Order of choices for each k: choose Q = q^s with Q > d and Q - 1 > (k^2/2 + k) d^2 (this is the S3 requirement; it already implies Q > d for k >= 2), then choose a in F_Q with f(a) != 0, then replace f by f_a, then choose c in (F_Q^*)^{k-1} by S3 for the root set Z_a. The set of root ratios R_ratio = {z'/z} of S3 is that of Z_a, which depends on a. This order has no circularity; the draft's wording ("replacing F_q by F_{q^s} and f(x) by f(x+a)") has the right content but never states the order.
- The conclusion does not depend on a: alpha_i^s is intrinsic to f over F_q. Different k use different (s_k, a_k), and the bound is on the same alpha_i. PROVED.
- Where f(0) != 0 is used downstream (S3, S5): 0 must not be a root, since Sigma_1 = {0} and the singular point 0 of the odd-index transforms must avoid Z. A translation is the cheapest way to arrange it, and an F_q-translation may be impossible: f = x^3 - x over F_3 vanishes on every element of F_3, so one needs F_9. CHECKED in section 4.2 (that f, its F_9 translations).
- p odd is preserved by extension; chi_Q is the quadratic character of F_Q.
- Dimension count of S0 (dim H = d - 1, H^0_c = H^2_c = 0): see 1.2; GOS CITED NOT OPENED.

## 4. Exact checks (CHECKED)

All scripts exact integer; below `D` denotes D(u) = sum_g chi(Res(g,f)) u^{deg g}, computed by brute force over all monic g of degree <= d+1 over F_q (q = prime power: field tables built by trial-division irreducible polynomials).

### 4.1 Symmetry of the L-polynomial (`run_sym.py`, output `out_sym_odd.txt`)
For random squarefree f with f(0) != 0 (3 per case, 1 for the largest cases): odd d in {3,5,7}, q in {3,5,7,9,11,13,25}; g = (d-1)/2. Tested: (i) coefficients of u^d and u^{d+1} are 0, (ii) a_{2g-i} = q^{g-i} a_i for i = 0..g (this includes a_{2g} = q^g). Result: **33 of 33 cases pass** ("ALL OK" at the end of `out_sym_odd.txt`). Example: q = 7, d = 5, f = 2+3x+6x^2+5x^4+5x^5: D = 1 - 3u + 14u^2 - 21u^3 + 49u^4 (21 = 7*3, 49 = 7^2). Note a first run of this script had a coding error (it tested i > g with negative exponents and reported three q = 7, d = 5 failures); the corrected test is the one in the output file. The failure was in my test, not in the symmetry.
Scope: this tests the functional equation for polynomials in F_q[x] with q up to 25 and d up to 7. It does not prove it and does not test eigenvalue statements beyond the symmetry.

### 4.2 Cross-checks (`run_more.py`, `out_more.txt`)
- Identification D(u) = prod(1 - alpha_i u) = exp(sum S_n u^n/n), where S_n is computed independently by counting y with y^2 = f(x) over F_{p^n} (field F_p[x]/m): 5 cases (p, d) = (3,3), (3,5), (5,3), (7,3), (5,5), n up to 6, 4, 4, 4, 4 resp. All S_n equal -p_n from D. (Also confirms the trace-formula consequence of 1.2 on these cases, and that D is polynomial of degree d-1 reproducing power sums beyond n = d-1.)
- S0 base change and translation, q = 3, Q = 9: f = x^3 - x (all of F_3 are roots), f = x^3 + x + 1, one squarefree degree-5 polynomial. Exactly: D_3(u) D_3(-u) = D_9(u^2) (this is prod (1 - alpha_i^2 u^2)) in all 3 cases; and D_9(f_a) = D_9(f) for every a in F_9 with f(a) != 0 (6, 6 and 8 translations). The first f has no F_3-point with f != 0, so the extension is really needed there.
- Even-degree control (d = 4, 6; q = 3, 5, 7; 10 cases): D has degree d - 1 (coefficients beyond vanish) and factors exactly as (1 - epsilon u) times a polynomial symmetric under alpha -> q/alpha of degree d - 2, epsilon = +-1 (both signs occur). So the full (d-1)-dimensional multiset is not stable under alpha -> q/alpha for even d: one eigenvalue +-1 has partner +-q absent. This matches the prediction of Step 1 at infinity and confirms that the oddness of d is a real hypothesis of S11. HINT-level corroboration only (an example of the mechanism, not a proof).

## 5. Referee remarks on the draft's S11 and S0

1. S11, repairable gap (exposition): the draft compares H^1_c(j_!L) with H^1(A^1, j_*L) and checks only the inertia at infinity. It also needs RGamma(I_z, L) = 0 at every root z (true because sigma acts as -1) so that Rj_*L = j_*L = j_!L and the dual sheaf is the one used. Supplied in Steps 1-2. Not an error in the statement.
2. S11: the draft writes "H^1(I_inf, L) = 0 (coinvariants zero)" but must also use H^0(I_inf, L) = 0 and the vanishing of H^i for i >= 2 (inertia has cohomological dimension 1 for l != p). Cosmetic; in Step 1.
3. S11: the draft's use of L = L^vee should be the arithmetic statement (a character of pi_1(U_0) over F_q with values +-1), not only a geometric isomorphism: otherwise the pairing is twisted by a character of Gal(F-bar/F_q) and the Frobenius eigenvalue statement changes. Supplied in 1.1(a). Cosmetic.
4. S0: the sentence "it suffices to prove |alpha_i|^s <= q^{s/2}-type bounds" is not the statement used later (the later statement is |alpha_i|^{sk} <= q^{s(k+3)/2}); cosmetic. The missing order of choices (Q, then a, then c) is a repairable exposition gap, section 3.
5. S0/S10: the translation changes the root ratios R_ratio of S3, so S3's counting must be applied to Z_a. Same item as 4.
6. No fatal error found in S0 or S11. The one genuinely external input of S11 is Poincare duality for lisse sheaves on curves, together with the trace formula and the GOS formula; I did not read their statements at a source.

## 6. What is still open for this part
- Open the four cited statements (T, GOS, PD, RJ) at readable sources; A6 owns this for T, GOS and the duality statement. I attempted Milne's notes and the Stacks Project and could not read the statement.
- The functional-equation route (section 2, last paragraph) is only named. A self-contained proof via Gauss sums or Riemann-Roch would remove the need for l-adic duality here; I did not write it.
- The degree statement "dim H = d - 1 exactly" rests on GOS (cited); section 1.3 proves only "<= d - 1", and section 4 shows equality in the tested cases.
