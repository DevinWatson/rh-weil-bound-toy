# Proof draft: |alpha| <= sqrt(q) for y^2 = f(x), by the Fourier route, assembled from the round-3 reports

Written 2026-11-20 by the assembly agent from reports A, B, C, D, E, F (round 3) and the round-one/round-two material.
Everything here is about character sums over finite fields, where the bound is Weil's theorem (1948). Nothing here says anything about the Riemann Hypothesis for the integers.
Labels: PROVED (argument given), CITED (statement named, OPENED or NOT OPENED per report D unless another report is named), CHECKED (exact computation or Lean, file named), OPEN, HINT. Weights, purity, the Weil bound and the Weil conjectures are used in no proof below; they appear only in lines marked [interpretation only].
This is a draft written from the reports. I re-derived nothing from primary sources. It is not a verified proof and the words "this proves" are not used: see section 0.

## 0. Status at the top

What the first-phase reports found about Claims A and B of the brief:

- Claim A (reduction): REDUCTION_HOLDS_WITH_CHANGES (report A). Three changes. (i) The wrong-parity group is a quotient coker(d_2) of H^2_c(G_m,R^k), not equal to it (equal when R^{k+1} = 0, which is our case under Claim B). (ii) Hypotheses must be explicit: L geometrically nontrivial (the conclusion is false for the trivial sheaf at k >= 4, test 3.1 of A), all c_i nonzero, (P_k^c) at the geometric generic point. (iii) "alpha of largest modulus" is not needed.
- Claim B (fibre statement): no error found (report B), with two repairs: the set R of root ratios must contain 1, and irreducibility of P_{i+1} needs surjectivity of pi_1(V - Z) -> pi_1(V) and transitivity of middle extension. The hypothesis of Claim B is sufficient, not necessary. Report C proved the vanishing H^{k+1}_c = 0 for k = 2, 3 for all nonzero c_i, h != 0, including c_1 = -c_2 where Claim B's hypothesis fails.
- Report D found no published proof of the route (absence of hits only) and notes that the sources contain no weight-free theorem evaluating the fibre sum of Claim A except the elementary Parseval bound used here.
- No referee outside the author of B has gone through the induction for k >= 4. The exact tests (E, B, C) use f = x - 1 (d = 1, H = 0) for k >= 3 and d = 3 only for k = 2. So the induction at d >= 3, k >= 3 is checked by nothing except its own author and by consistency of dimension counts.

Disagreements between reports, not smoothed over (details in section 5): A leaves (P_3^c) at c_1 = -c_2 undecided, C proves it; B and C disagree on whether KL/Deligne-Laumon sources were opened (section 5); D says the induction hypothesis on tameness is "not verified beyond one step" while B says it is proved from Laumon 2.3.x/2.4.3/2.5.3.1.

## 1. Theorem and scope

Setting. p odd, q a power of p, F_q, l != p, psi_0 a nontrivial additive character of F_p, chi the quadratic character. f in F_q[x] squarefree of odd degree d >= 3. Z = roots of f in F-bar. L = L_chi(f) on U_0 = A^1 - Z, j: U_0 -> A^1, H = H^1_c(A^1_{F-bar}, j_!L), dim H = d - 1, Frobenius eigenvalues alpha_1..alpha_{d-1} (in Q-bar_l), so that sum over x in F_{q^n} of chi_n(f(x)) = -sum alpha_i^n. For every embedding iota: Q-bar_l -> C these are the reciprocal roots of the L-function of y^2 = f(x).

Theorem (Weil 1948, claimed route). For every iota and every i: |iota(alpha_i)| = sqrt q.

Exact scope the reports support. The upper bound |alpha_i| <= sqrt q is the content of steps S1-S10; the lower bound (equality) is S11 and is not checked by any report. The theorem as stated is CONDITIONAL on every CITED statement of lists 1 and 2 being used correctly, and on the induction S5, which only its author has examined. Status of the whole: OPEN-but-no-known-gap, not "proved". Narrower statements that the reports support more firmly:
- k = 2 and k = 3: fibre vanishing H^{k+1}_c = 0 for all c_i != 0, h != 0 (report C, PROVED by hand modulo a short list of cited facts), with exact checks (C, E).
- k = 4: round two (main session check) settled the quadric statement for generic coefficients, giving |alpha| <= q^(7/8) without weights. This is independent of S5.
- For every k, the statement is reduced (A, B) to the induction S5.

## 2. Conventions and bookkeeping

- t(x) = chi(f(x)) over any finite extension; |t| <= 1.
- Q = q^s a power of q; psi = psi_0 o Tr on F_Q; c = (c_1..c_{k-1}) in (F_Q^*)^{k-1}; Q_c(x) = sum_{i<k} c_i x_i x_{i+1}; h in F_Q.
- S_h(F_{Q^n}) = sum over x in F_{Q^n}^k of t(x_1)..t(x_k) psi_n(h Q_c(x)); R_n = sum over h in F_{Q^n}^* of S_h; N_n = number-weighted sum of t(x_1)..t(x_k) over Y = {Q_c = 0}; M_n = sum of t over F_{Q^n}.
- Over F_Q, H has eigenvalues alpha_i^s.
- Exponent bookkeeping, all relative to the base field F_Q: fibre sums are bounded by Q^{n(k+1)/2}; R_n by Q^{n(k+3)/2}; a wrong-parity eigenvalue is Q times beta with |beta| <= Q^{(k+1)/2}, so at most Q^{(k+3)/2}.
- Transfer of identities in Q-bar_l to C by iota: trace identities hold in Q(zeta_p) inside Q-bar_l; iota restricted to Q(zeta_p) gives a complex character psi_C, and the elementary bound S1 holds for every nontrivial complex character, so the same estimate holds for every iota. PROVED (bookkeeping).

## 3. The proof in steps

### S0. Reductions (f(0) != 0, extension of scalars)
Statement: it suffices to prove |alpha_i|^{s} <= q^{s/2}-type bounds after replacing F_q by F_{q^s} and f(x) by f(x + a) with a in F_{q^s}, f(a) != 0.
Argument: f has at most d roots, so a exists once q^s > d; translation x -> x + a is an isomorphism of A^1 carrying L_chi(f) to L_chi(f(x+a)), so H and its Frobenius eigenvalues over F_{q^s} (alpha_i^s) are unchanged. dim H = d - 1 is by the Euler-Poincare formula (rank 1, d points of inertia -1, tame at infinity, H^0_c = H^2_c = 0 since L is nontrivial rank one with nontrivial inertia). Status: PROVED (elementary); the dimension formula uses Grothendieck-Ogg-Shafarevich (CITED, NOT OPENED by any report; report C also uses it). Checked in: A (hypotheses), B (section 1 setting), C (F1).

### S1. The elementary identity and the fibre bound
Statement: q N = M^k + R with R = sum_{h != 0} S_h, and for h != 0, all c_i != 0, over every finite field F: |S_h| <= |F|^{(k-1)/2} sum |t|^2 <= |F|^{(k+1)/2}.
Argument: orthogonality for psi, then k - 1 Cauchy-Schwarz/Parseval steps along the path quadric. Status: CHECKED in Lean, ToyWeil/Identity.lean and ToyWeil/Parseval.lean (theorems identity, identity_bound_one, iterated_bound, Ssum_eq_path_sum). The main session recompiled Identity.lean in round two (exit 0, standard axioms). I have no record that Parseval.lean was recompiled by the main session. Elementary; no weights.

### S2. Power-sum lemma
Statement: if a finite sum of n-th powers with nonzero coefficients (distinct bases) is O(rho^n) as n -> infinity, then every base has modulus <= rho. Signed three-family version: for finite families a, e, b with sum a^n + sum e^n - sum b^n = O(rho^n) and |b_j| <= rho for all j, every |a_i| <= rho. Status: CHECKED in Lean, PowerSum.lean (no_hidden_growth, no_cancellation) and Endgame2.lean (no_cancellation_signed3, no_cancellation_signed); report F: compiled clean, axioms propext, Classical.choice, Quot.sound only, no sorry. The main session has not recompiled Endgame2.lean.

### S3. Choice of c and the explicit genericity conditions
Fix k >= 2 and let Q = q^s. Roots: Z in F-bar, f(0) != 0. R_ratio = {z'/z : z, z' in Z} (contains 1, |R_ratio| <= d^2). rho_i = -c_{i-1}/c_i for 2 <= i <= k-1. Sets (report B, section 3.3):
Sigma_1 = {0}, Sigma_2 = rho_2 Z, Sigma_i = rho_i (Z union Sigma_{i-2}), closed form Sigma_i = {rho_i rho_{i-2} ... rho_{i-2m} z : z in Z, 0 <= m <= floor(i/2) - 1} union ({0} if i is odd).
Condition (G_k): Z disjoint from Sigma_i for 2 <= i <= k-1. Equivalent: for every product pi = rho_i rho_{i-2}...rho_{i-2m} that occurs, pi not in R_ratio. Lists of conditions (B): k=2 none; k=3 rho_2; k=4 rho_2, rho_3; k=5 rho_2, rho_3, rho_4, rho_4 rho_2; k=6 rho_2..rho_5, rho_4 rho_2, rho_5 rho_3. The conditions do not involve h.
Existence of c in F_Q. Each excluded condition is "monomial in the c_i equals a given constant r in R_ratio", and the monomial has a nonzero exponent vector (the product alternates distinct c_i, with a sign). For fixed values of all other coordinates it fixes one coordinate, so it excludes at most (Q-1)^{k-2} points of (F_Q^*)^{k-1}. The number of conditions is at most (k^2/2 + k) d^2. So c exists as soon as Q - 1 > (k^2/2 + k) d^2. Status: PROVED (my elementary counting, assembler; not in any report; unrefereed). The set Sigma_i itself: PROVED by B from the induction (S5), CITED inputs. Note: for the all-ones quadric (c_i = 1) condition (G_k) fails for every k >= 5 (rho_4 rho_2 = 1 in R_ratio); hence c in general position is required, and Q grows with k.

### S4. Fibre cohomology as cohomology on the line
Statement: for h != 0, with G_1 = j_!L, G_{i+1} = j_!L tensor Rpr'_!(pr^*G_i tensor L_psi(h c_i x x')), P_i = G_i[i]: P_1 = j_!L[1], P_{i+1} = (j_!L) tensor FT_{h c_i}(P_i), and H^m_c(A^k, F_h) = H^{m-k}_c(A^1, P_k). Status: PROVED modulo CITED (Fubini/Kunneth, projection formula, proper base change; SGA 4; NOT OPENED by A, B, C). Checked in: B step 0, RED (round two), C (k = 2, 3 by hand). Dimension check D_k = r_{k+1} - eps_k, r_1 = 1, r_2 = d, r_{i+1} = d r_i + r_{i-1} tested by exact Hankel ranks (compute/B/hankel.py, compute/NUM) at d = 1 (k = 2, 3, 4) and d = 3 (k = 2: 10). CHECKED, but only for d = 1 and k <= 4, d = 3 and k = 2.

### S5. The Fourier induction (Claim B): fibre cohomology is concentrated in degree k
Statement (Theorem B'). Assume p odd, f squarefree, f(0) != 0, (G_k), c_i != 0, h != 0. Then H^j_c(A^k_{F-bar}, F_h) = 0 for j != k.
Invariant (I_i), i = 1..k-1: (1) P_i = j_{!*}(M_i[1]) with M_i irreducible lisse on A^1 - S_i; (2) Z contained in S_i, inertia -1 at each root; (3) M_i tame at S_i; (4) at infinity M_i = T^0 + sum_a L_psi(a y) tensor T^a with T tame; (5) the frequencies A_i = h c_{i-1}(S_{i-1} - {0}); T^0 != 0 iff 0 in S_{i-1}.
Steps (report B section 1):
1. P_1 = j_*L[1] is simple (BBD 4.3.1(ii)); tame. PROVED modulo CITED.
2. Q_i = FT(P_i) is simple perverse (Laumon 1.3.2.3, 1.3.2.4, OPENED, OCR); P_i is not punctual and not of the L_psi(ax)-type (it ramifies at the roots), so it is of type (T3); FT exchanges (T3) and (T3') (Laumon 1.4.2.1(ii), OPENED): Q_i = j_{!*}(M'[1]), M' irreducible lisse.
3. Singular set and local structure of Q_i: generic rank sum over S of a_s(P); stalk drop at w != 0 equals dim T^a if w = -a/b; Sing(Q_i) - {0} = rho_i(S_{i-1} - {0}); 0 is singular iff T^0 != 0, i.e. iff i odd. The monodromy at infinity of Q_i is sum over s in S_i of L_psi(h c_i s y) tensor E_s with E_s tame; Q_i tame at finite singular points. Sources: Laumon 2.3.1.1-2, 2.3.2.1, 2.3.3.1 (a PROPOSITION, not a theorem), 2.4.3, 2.5.3.1 (OPENED, OCR, symbols garbled) and Grothendieck-Ogg-Shafarevich with proper base change (rederived by B). The assembly of the E_s from these statements is B's own (D: not verified beyond one step).
4. If Z does not meet Sing(Q_i): at each root Q_i is lisse and inertia acts on L tensor M' by -1 (no invariants, no coinvariants), so j_! = Rj_* = j_{!*} and P_{i+1} = j_{!*}((L tensor M')|_{V-Z}[1]).
5. pi_1(V - Z) -> pi_1(V) is surjective (SGA 1 V 8.2, NOT OPENED), so M_{i+1} is irreducible and P_{i+1} is simple (BBD 4.3.1(ii)).
6. L_infty tame, so (4) and (5) hold for i+1.
7. Conclusion: P_k = j_{!*}(M_k[1]), M_k irreducible with inertia -1 at the roots, hence no coinvariants. Artin vanishing: H^{<0}_c(A^1, P_k) = 0; H^1_c(P_k) = H^2_c(j_*M_k) = (coinvariants of M_k)(-1) = 0; H^{>=2}_c = 0. Together with S4: H^m_c(A^k, F_h) = 0 for m != k, every h != 0.
Status: PROVED modulo CITED (B); the singular-set step 3 and the induction hypothesis propagation are the part that no one else has gone through; the sheaf-level facts used in steps 4-7 are elementary once step 3 is accepted. Do the cited theorems use weights? See list 1. Small cases independent of S5: k = 2 (C section 1: lisse on G_m of Q_1 by Deligne-Laumon or FT preserving irreducibility, CITED NOT OPENED by C), k = 3 (C section 2: H^4_c = 0 by the coinvariant lemma F2 for every c_1, c_2 != 0 and h != 0). 
The hypothesis (G_k) is sufficient, not necessary (B, C): e.g. d = 1, q = 3, k = 3, c = (1,-1) has rho_2 = 1 but still has cohomology only in degree 3 (dimension 1, not D_3 = 2).

### S6. (P_k^c) holds
By S5, R^{k+1} = 0 on all of G_m (not only generically). So (P_k^c) holds and the fibre cohomology of every h != 0 is in degree k. Status: follows from S5; PROVED modulo CITED.

### S7. The global side (Claim A, corrected)
Statement: with F the sheaf (pullback of the external product of j_!L) tensor L_psi(h Q_c) on G_m x A^k over F_Q (L_psi(h Q_c) with h the G_m coordinate), and R^b = R^b pr_{h!} F:
(a) H^m_c(G_m x A^k, F) = 0 for m <= k; the sequence 0 -> T -> H^{k+1}_c(G_m x A^k, F) -> H^{k-1}_c(Y,K)(-1) -> 0, with T = H^{tensor k}; the T-part of R_n is (-1)^{k+1} Tr(T) = -M_n^k.
Argument: H^m_c(A^1 x A^k, F) = H^{m-2}_c(Y,K)(-1), which vanishes for m <= k since H^j_c(Y,K) = 0 for j < k-1 (Y has affine complement in A^k, K_ext[k] perverse, Artin; E3, re-proved by A); H^*_c({0} x A^k, F) = T sits in degree k only; T injects since H^k_c(A^1 x A^k, F) = 0. Status: PROVED (A, step (a)), modulo CITED Kunneth, Artin, excision sequence.
(b) By S6, R^b = 0 for b != k, so the Leray sequence degenerates: H^{k+a}_c(G_m x A^k, F) = H^a_c(G_m, R^k), a = 0, 1, 2. H^0_c = 0 (since H^k_c(G_m x A^k) = 0); H^{k+1}_c = H^1_c(G_m, R^k) contains T; H^{k+2}_c = H^2_c(G_m, R^k) = C(-1) where C = maximal geometrically constant quotient of V = R^k|_U (U dense open on which R^k is lisse); H^{k+3}_c = 0. (A's general version, when only (P_k^c) at the generic point is known: H^{k+2}_c is the quotient coker(d_2) of C(-1); every wrong-parity eigenvalue has the form Q beta with beta an eigenvalue on C. In our case R^{k+1} = 0 so this is equality.) Status: PROVED (A (b), (c)) modulo CITED Leray, trace formula, Poincare duality on curves, NOT OPENED by A.
(c) R_n = (-1)^{k+1} Tr(Frob^n | H^{k+1}_c) + (-1)^{k+2} Tr(Frob^n | H^{k+2}_c): Grothendieck trace formula over F_{Q^n}. Status: CITED (NOT OPENED); weight-free statement.
Checks: for k = 2, R_n = -sum (alpha_i alpha_j)^n - 2 sum (Q t_0 alpha_i)^n - Q^n, H^3 of rank d^2, H^4 = 0, C = 0 (A 3.2, 32 cases, exact); for k = 3, c_1 != -c_2 all coefficients positive (A 3.3); c_1 = -c_2 has wrong-parity terms -Q^{2n} u, -t_0^n Q^{2n}; k = 4, c_1 + c_2 + c_3 = 0 has a plane class beta = Q^2 (A 3.4). All CHECKED by exact integers (compute: check_A.py, check_A_out.txt). These tests check identities and bookkeeping only. Hypothesis note: S7 needs L geometrically nontrivial (true: ramified at roots).

### S8. Fibre bound on the constant quotient
Statement: every eigenvalue beta of Frobenius on C satisfies |iota(beta)| <= Q^{(k+1)/2}.
Argument (A (d)): choose a closed point h_0 of U of degree m over F_Q. Frob_{h_0} on V_{h_0} = H^k_c(A^k, F_{h_0}) maps onto Frob_Q^m on C, so beta^m is a Frobenius eigenvalue of the fibre. By S6 the fibre cohomology is in degree k, so the fibre sums over F_{Q^{mn}} equal (-1)^k sum_j gamma_j^n with positive multiplicities. By S1, |S| <= Q^{mn(k+1)/2} (h_0 != 0, c_i != 0), so by S2 every |gamma_j| <= Q^{m(k+1)/2}. Hence |beta^m| <= Q^{m(k+1)/2}, i.e. |beta| <= Q^{(k+1)/2}. Status: PROVED (A (d)), given S1, S2, S6. Hypotheses needed: (P_k^c) only at a closed point of the generic locus U; vanishing at a single point would not suffice (A).

### S9. The dichotomy (no sign statement about Y is used)
Statement: for every i, |iota(alpha_i^s)|^k <= Q^{(k+3)/2}.
Argument (A (e) with Lean G2): R_n = sum over distinct bases lambda of a_lambda lambda^n with a_lambda = (-1)^{k+1}(m_{k+1}(lambda) - m_{k+2}(lambda)), m the multiplicity in H^{k+1}_c, H^{k+2}_c. By S1, |R_n| <= (Q^n - 1) Q^{n(k+1)/2} < Q^{n(k+3)/2}. Let beta_0 = alpha_i^{ks}; since T contains the eigenvalue alpha_i^{sk}, m_{k+1}(beta_0) >= 1 by S7(a). If a_{beta_0} != 0, S2 gives |beta_0| <= Q^{(k+3)/2}. If a_{beta_0} = 0, then m_{k+2}(beta_0) >= 1, so beta_0 = Q beta with |beta| <= Q^{(k+1)/2} by S8, hence again |beta_0| <= Q^{(k+3)/2}. In the three-family form (a = T's eigenvalues, e = the rest of H^{k+1}, b = the wrong-parity eigenvalues, with bound |b| <= Q^{(k+3)/2} by S8) this is exactly Lean no_cancellation_signed3, which does not need to know which case occurs. Status: PROVED (A, F).

### S10. Passage to F_q and the limit in k
|iota(alpha_i)|^{ks} <= q^{s(k+3)/2}, so |alpha_i|^k <= q^{(k+3)/2}, i.e. |alpha_i| <= q^{1/2 + 3/(2k)} (the s-th root is exact). This holds for every k >= 2, with a different field F_{q^s} and c for each k. Let k -> infinity: |alpha_i| <= sqrt q. Status: PROVED (elementary calculus). Mismatch to flag: the Lean theorems endgame and endgame_fibres (PowerSum.lean, Endgame2.lean) assume one fixed field and one fixed alpha for all k. Our application uses Q = q^{s_k} with s_k growing, so the Lean endgame theorem does not apply as stated; what is covered in Lean is the per-k step (no_cancellation_signed3), and the s-th root and limit are not in Lean. The exponent bookkeeping is thus CHECKED for the per-k signed cancellation and not for the passage to the limit.

### S11. The lower bound by duality (needed for |alpha| = sqrt q)
Statement: the multiset {alpha_i} is stable under alpha -> q/alpha. Hence, with S10 for all iota, |alpha_i| >= sqrt q.
Argument (assembler's, no report): L is self-dual (chi^2 = 1), so Poincare duality on A^1 gives a perfect pairing H^1_c(A^1, j_!L) x H^1(A^1, j_*L) -> Q_l(-1). Since d is odd, the inertia at infinity acts on L by the nontrivial quadratic character, so L^{I_infty} = 0 and H^1(I_infty, L) = 0 (coinvariants zero), so H^1_c(j_!L) -> H^1(j_*L) is an isomorphism. Hence H x H -> Q_l(-1) is a perfect Frobenius-equivariant pairing; the eigenvalues satisfy alpha <-> q/alpha. For every iota, q/alpha_i is an alpha_j, so |q/alpha_i| <= sqrt q, i.e. |alpha_i| >= sqrt q. Status: CITED (Poincare duality for curves, the exact sequence relating H_c and H with inertia at infinity; NOT OPENED) with my argument; not refereed. [interpretation only: this reproduces the functional equation of the L-function].

### S12. Conclusion
If S0-S11 are accepted, |iota(alpha_i)| = sqrt q for all i and iota, i.e. Weil's bound for y^2 = f(x) with f squarefree of odd degree d >= 3 over F_q, q odd. Until S5 has been checked by someone other than its author, and the CITED NOT OPENED statements have been opened, this is a conditional statement.

## 4. The three lists

### List 1. Every theorem cited, and what is known about weights
(WG = grep result of report D on the OCR of Laumon 1987: no weight argument in chapters 1-3; weights first at 4.1.2.)
1. Grothendieck trace formula (SGA 4 1/2, Rapport, Fonctions L): NOT OPENED. Weights: not used in the formula (HINT, from background, no report checked).
2. Kunneth, proper base change, projection formula, excision, Leray spectral sequence (SGA 4 XVII, XVIII): NOT OPENED by A, B, C. Weight-free (HINT).
3. Artin vanishing for affine varieties (SGA 4 XIV 3.2): NOT OPENED. Weight-free (HINT).
4. Poincare duality for curves (SGA 4 XVIII; Milne): NOT OPENED. Weight-free (HINT).
5. Grothendieck-Ogg-Shafarevich (Raynaud, Bourbaki; SGA 5 X): NOT OPENED. B and C use it for ranks and Swan conductors. Weight-free (HINT, standard; no report checked).
6. BBD (Beilinson-Bernstein-Deligne) 4.1.1, 4.1.2, 4.2.5, 4.3.1(ii), 4.4 (t-exactness, simple objects are IC of irreducible lisse sheaves, Artin-Gabber t-exactness of Psi, Phi): OPENED by B in the dump (OCR, rough). Weights enter BBD only from chapter 5 on (HINT; not grepped by any report). The chapter-4 statements are used without weights here.
7. Laumon 1987 (Publ. IHES 65): 1.2.2.1 (involutivity), 1.3.1.1, 1.3.2.3 (FT is an equivalence of abelian categories Perv -> Perv), 1.3.2.4 (preserves simples), 1.4.2.1 (types T1, T2, T3, FT exchanges T3 and T3'), 2.3.1.1, 2.3.1.2, 2.3.1.3, 2.3.2.1, 2.3.2.3, 2.3.3.1 (a Proposition), 2.4.3, 2.5.3.1: OPENED (B, D; OCR with garbled symbols; the slope maps s/(1+s), s/(1-s), s/(s-1) are read from garbled formulas, HINT). WG: no weight argument in chapters 1-3. Caveat: results that these chapters cite from other papers were not read; B names Gabber-Katz (inside Laumon 2.5.3) as cited, not rechecked.
8. Katz-Laumon 1985 (Publ. IHES 62), 2.1.3 and 2.1.5 (forget-supports isomorphism, FT commutes with duality): B says OPENED in the dump (KL.txt); D says 2.1.5 was seen only as quoted by Laumon and NOT OPENED as a numbered statement. Unresolved discrepancy between the reports; I would treat it as NOT OPENED.
9. SGA 1 V 8.2 (surjectivity of pi_1(V - Z) -> pi_1(V)): NOT OPENED (B). Weight-free (pure fundamental group statement, HINT).
10. Deligne-Laumon semicontinuity of the Swan conductor (Laumon, Asterisque 82-83, 2.1.1): OPENED by D (OCR, inequality sign garbled, read as >=; no weights by grep); C lists it NOT OPENED. Used only in C's alternative route (section 4) and not by B's induction.
11. Katz-Gabber / Gabber-Katz (inside Laumon 2.5.3): NOT OPENED; weights unknown.
12. Round-two material: the main session read the k = 4 theorem (report K4T Theorem D) and recompiled Identity.lean; it opened none of the cited theorems.
13. Kiehl-Weissauer (Ergebnisse 42): NOT OPENED; the brief's "Plancherel" attribution is unverified (D). Katz, Asterisque 79; Brylinski, Asterisque 140-141: NOT OPENED.

### List 2. Steps whose status is not PROVED or CITED-and-OPENED, in order of dependence
1. S5 step 3 (location of Sing(Q_i), the assembly of the E_s, tameness propagation): only B has gone through it; D says it is not verified beyond one step; OCR damage (B lists LAU.txt lines 1126-1131, 1176-1179, 1285-1324, 1360-1375). The whole theorem hangs on it for k >= 5. Needed and would settle it: a referee going through the page images of Laumon 2.3 and 2.4.3, 2.5.3.1.
2. S5 steps 4-5 (irreducibility of P_{i+1}: SGA 1 V 8.2 NOT OPENED; transitivity of middle extension; no hidden skyscraper constituent): PROVED by B under (G_k), CITED NOT OPENED.
3. S5 step 2 as used for all i, with the OCR reading of Laumon 1.4.2.1(ii): OPENED but garbled.
4. S4: the identification H^m_c(A^k, F_h) = H^{m-k}_c(A^1, P_k) and the perversity of each P_i: CITED NOT OPENED (A, B, C).
5. S7 (Leray, trace formula, Poincare duality on curves): CITED NOT OPENED; A's own derivation is the argument.
6. S3 counting (assembler only, unrefereed) and the closed form of Sigma_i (from S5).
7. S11 lower bound by duality: not covered by any report.
8. Weight-freeness of the cited inputs: only grep-level evidence for Laumon chapters 1-3 (OCR); BBD, trace formula, GOS, Gabber-Katz not checked for weights by any report.
9. S10: the limit and the s-th root are not in Lean, and the Lean endgame theorems assume a fixed field (mismatch described in S10).
10. Whether the route circularly uses a weight-type input (D's HINT): the weight-free evaluation of the fibre sum is exactly S8, which uses only Parseval (S1) and the power-sum lemma (S2); no hidden circularity was found, none excluded beyond that.
11. p small relative to d or k: no report examined it; I see no place where p > d or p > k is used (HINT).
12. The k-dependence of the field and of c: PROVED to exist (S3) but the identification of R_n over F_Q for Q growing is trivially fine; the real risk is item 1.

### List 3. What exact computation and Lean cover
- Lean (CHECKED, files in toy-case/lean/ToyWeil/, standard axioms only): the identity qN = M^k + R and the fibre bound for every finite field and every nonzero h (Identity.lean, Parseval.lean); the power-sum lemma and the signed three-family no-cancellation statement (PowerSum.lean, Endgame2.lean G1, G2); G3 endgame_fibres assuming the fibre hypothesis for every k with one fixed field (does not apply as stated; see S10). Not covered in Lean: any cohomological statement (S4-S8), the duality step, the limit with varying field.
- Exact computation (CHECKED): A's identity tests for the trivial sheaf, k = 2, 3, 4 (check_A.py, check_A_out.txt); C's net eigenvalue counts for d = 1 (k = 2, 3), d = 2 (k = 2, 3 with m = 2), d = 3 (k = 2), brute-force match at k = 3 (compute/C/fsum.py, compute/C/out/); B's exact Hankel ranks d = 1, q = 3 (compute/B/fibre_p3.py, hankel.py); E's exact L-series, degrees 2, 2, 5 (f = x - 1, k = 2, 3, 4), 10 (f = x^3 - x + 1, k = 2), and degrees 1, 4, 3, 6, 11 for the bad coefficients, all matching the Euler-characteristic dimension formula (compute/NUM/predicted_vs_observed.txt). They test dimensions and identities; none tests vanishing of H^{k+1} for d >= 3, k >= 3, and a polynomial L does not exclude cancellation of equal eigenvalues between H^k and H^{k+1} (E). Floating-point root moduli (E, B) are HINTs only; in terminated cases all moduli are <= q^{k/2}.

## 5. Where the reports disagree or leave a gap
1. A: "(P_3^c) at c_1 = -c_2 not decided". C: PROVED H^4_c = 0 for every c_1, c_2 != 0, h != 0, via the coinvariant lemma, even when Sigma_2 meets Z. Not contradictory: the wrong-parity terms in A's test 3.3 sit in H^2_c(G_m, R^3) (constant quotient of the generic local system), not in the fibre H^4. I keep both: with C, (P_k^c) at k = 3 holds for all c_i != 0.
2. B: at c_1 = -c_2 (k = 3) the hypothesis fails; fibre cohomology (d = 1) has dimension 1 in degree 3. C and E agree (D_3 = d^3 + 2d - 1 - m).
3. The brief says the wrong-parity group is H^2_c(G_m, R^k) and the dangerous eigenvalues come from the coinvariants of R^k; A shows this is a quotient in general; under (G_k) there is equality (R^{k+1} = 0).
4. Brief's "alpha of largest modulus": unnecessary (A).
5. KL 2.1.3 and Deligne-Laumon 2.1.1 OPENED or NOT OPENED: B and D versus D and C (list 1, items 8 and 10).
6. D: the induction hypothesis on tameness is "not verified beyond one step"; B: derived from 2.3.x, 2.4.3 and 2.5.3.1 plus GOS. I list it as list 2, item 1.

## 6. Novelty paragraph (report D, with its uncertainty)
Report D read Laumon 1987 (chapters 1-4), Katz's four lectures on Weil II, Venkatesh's Fourier-transform note and Kopparty's notes. Chapters 1-3 of Laumon contain no weight argument; weights enter in chapter 4 with Deligne's reality criterion and the L-function product formula; neither Plancherel nor Parseval appears there. The route is a variant of the Kloosterman-Rankin-Laumon-Katz "method of families" (bound one eigenvalue by a k-th power moment of a family; dangerous eigenvalues live in coinvariants of a generic local system; the limit k -> infinity removes the constant). It is not a special case of Laumon chapter 4 (no purity of FT, no weight induction; it iterates FT k - 1 times with twists by a rank-one sheaf and proves fibrewise vanishing) or of Katz's four lectures (the family is the h-line of a fixed squarefree f, there is no monodromy group computation or moment criterion). Elementary relatives (Kloosterman's fourth moment, p^{3/4}; Mordell's bound) do not reach exponent 1/2 by themselves. Five generic searches found no published proof of the route; that is an absence of hits only. Uncertainty: Kiehl-Weissauer, Katz Asterisque 79 and Brylinski were not opened, and D could not verify the brief's attribution of a Plancherel argument to Kiehl-Weissauer. I cannot exclude that the route is a rediscovery. Where a hidden circularity would sit (HINT): in the weight-free evaluation of the fibre sum (S8), exactly where Laumon and Katz use weights or L-function positivity; in this draft that step uses only S1 and S2.
