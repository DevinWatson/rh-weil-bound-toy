# C1: hostile referee report on LEMMA_R.md

Referee: C1 (Sonnet 5.5). Date 2026-11-21. Scope: character sums and l-adic sheaves on the affine line only; nothing here concerns the Riemann
Hypothesis for the integers. Laumon IHES 65 pages read on the images: p012-p014 (1.2.1 to 1.2.2.5), p018 (1.3.2), p020 (1.4.2.1), p021 (1.4.3.2),
p023-p027 (2.1.2 to 2.2.1.2), p029-p030 (2.3.1.1 with proof, 2.3.1.2, 2.3.1.3). Journal page = PDF page + 129. Statements below are in my words.
Labels: PROVED / CITED / CHECKED / OPEN / HINT. Defect classes: FATAL / REPAIRABLE / COSMETIC.

## Verdict

Lemma R holds as written. I found no FATAL and no REPAIRABLE defect; ten COSMETIC points (section 5), three of which should be fixed in the text
before anyone else reads it. Every use of a cited statement matches the page, with one provenance remark on R4. The mathematical content of Steps 0 and 1
is Laumon's own proof of 2.3.1.1 (i),(ii),(iii) and 2.3.1.2 (p158-159) restated in sheaf ranks; the new content is Steps 2 and 3, which I re-derived
line by line and could not break.

## 1. Inputs R1 to R5 against the page images

R1 (2.2.1, j.p.155). CITED, p026. Definitions r(F), r_x(F) = dim of the stalk, s_x(F) = Swan of the local monodromy, a_x = r + s_x - r_x; extended to
complexes by additivity; for K perverse, a_x(K) <= r(K) - r_x(K) <= 0 (2.2.1.1). Sign for K = G[1], G a sheaf: r, r_x, a_x of K are the NEGATIVES of
those of G, while s_x(K) = -s_x(G). So for K = (j_*M)[1]: r(K) = -r, r_x(K) = -dim M^(I_x), a_x(K) = -(r - dim M^(I_x) + Sw_x(M)). Matches LEMMA_R
exactly (PROVED by additivity; also consistent with a_x(K) <= 0).

R2 (2.2.1.2, j.p.156). CITED, p027. For X projective and K in D^b_c: chi(X, K) = chi(X) r(K) - sum deg(x) a_x(K), chi(X) = C(2-2g). Matches. It is
for every K in D^b_c, not only perverse, so applying it to a sheaf G (extension by zero of j_*M tensor L) is legitimate. Proof (Raynaud, SGA 5 X) not
read (OPEN, as the lemma says).

R3 (2.1.2.4 to 2.1.2.8, 2.1.3, 2.1.4, j.p.152-154). CITED, p023-p025.
- Break decomposition is canonical, a decomposition of I-modules (p152, after 2.1.2.3); projectors exact; r and s additive (p153). OK.
- 2.1.2.7 (p153): (i) s(V tensor L) = r(V_[0,1[) + s(V_1 tensor L) + s(V_]1,inf[); (ii) s(V_1 tensor L) <= r(V_1), with equality iff (V_1 tensor L)^(I^(1-eps)) = 0
  for some eps in [0, 1/r(V_1)[. The proof states, for a simple P-module W of slope lambda: W tensor L is simple of slope Sup(1, lambda) if lambda != 1 and of slope
  mu <= 1 if lambda = 1. And, in the equality case, s(V_1 tensor L) = r(V_1) iff every simple P-constituent W has s(W tensor L) = r(W), i.e. slope 1. So LEMMA_R's
  "equality iff V_1 tensor L has no part of slope < 1" is what the proof gives; the printed (ii) states it through the invariants. OK.
- 2.1.2.8 (p154): L_psi(1/pi) has Swan conductor 1 for any uniformizer pi, so L_psi(a x), a != 0, in the coordinate x = 1/pi with pi = 1/(a x), has Swan 1. OK.
  Dual: 2.1.3 gives (L_psi(1/pi))^dual = L_{psi^-1}(1/pi). Not used by the lemma.
- 2.1.4 (p154): tame iff P acts trivially iff pure of slope 0 iff s = 0. OK.
The word "simple module" in R3 must mean simple P-module (COSMETIC C1).

R4 (stalk of F(K) at s' is RGamma_c(A, K tensor L_psi(x s'))[1]). The first displayed line of the proof of 2.3.1.1 (p158) is only the rank (Euler
characteristic) statement r_s'(K') = -chi_c(A tensor k-bar, K tensor L(x.s')). The complex-level statement is the definition of F (1.2.1.1, p141) plus proper
base change (C-2); it is not "the first line" on the page. COSMETIC C2, and see 2.0 below: the lemma only needs the Euler characteristic version.

R5. CITED. 1.2.2.1 (p141): F'(F(K)) is a_*K(-r), where F' is the Fourier-Deligne transform of the dual bundle associated to THE SAME psi, and a: E -> E'' is
the isomorphism e -> -<e, >. Here r = 1 and a_* = a^* for the involution x -> -x, so F'F(K) = a^*K(-1). 1.2.2.3 (p143): F is an equivalence with quasi-inverse
a^*F'( )(r). 1.3.2.3 and 1.3.2.4 (p147): F is an equivalence on perverse sheaves and preserves simple objects. 1.4.2.1 (ii) (p149): F exchanges T3 and T3', and
F(j_*F[1]) = j'_*F'[1] with F' irreducible lisse on the maximal open of lissity U'. Type T3 is: F irreducible lisse on a dense open U, no subquotient of F|U (over k-bar)
isomorphic to L(x.a')|U. The main session says it did not read 1.2.2.1; I read it: the form quoted in LEMMA_R (same psi, a, twist (-1)) is exactly the page.
On the page the pushforward in T3 and in 1.4.3.1 (j_! -> j_* -> Rj_* are isomorphisms for K_chi, chi nontrivial) is the ordinary j_*; on a curve the middle extension
of a lisse sheaf is the ordinary j_*, BBD 2.1.11 (not opened; OPEN-standard).

## 2. Steps 0 to 3, redone

2.0. Euler characteristic suffices. Both applications of (E) can be done with Laumon's rank statement r_s'(K') = -chi_c(...) (p158) and the facts that the
stalk of j'_*N[1] has Euler characteristic -dim N^(I) and the stalk of a^*P(-1) has Euler characteristic -dim M^(I_(-sigma)). The claim "the stalk sits in one degree" is true
(a middle extension on a curve is a sheaf in degree -1 after the shift) but not needed, and H^0_c = H^2_c = 0 need not be invoked. COSMETIC C2.

Step 0. PROVED (given R2, R4). Extension by zero G of j_*M tensor L_psi(x s') to P^1. chi(P^1, G) = chi_c(A, j_*M tensor L). R2 in sheaf form: chi(P^1,G) = 2 r(G) - sum deg(x) a_x(G).
Finite points: a_s(G) = r + Sw_s(M) - dim M^(I_s) = art_s(M) at s in S (L_psi lisse on A, so the twist changes neither the invariants nor the Swan conductor);
a = 0 at lisse points. At infinity: the stalk of the extension by zero is 0, so a_inf(G) = r + Sw_inf(M tensor L_psi(x s')). Hence chi = 2r - sum art_s - r - Sw_inf = r - sum art_s - Sw_inf, and
dim of the stalk of F(P) at s' = -chi = sum art_s + Sw_inf - r. This is (E); I checked every sign, and it agrees with Laumon's own displayed formula in the proof of 2.3.1.1 (p159, first line):
r_s'(K') = -r(K) + sum deg(x) a_x(K) - s(F_inf tensor L(x.s')), read with K = j_*M[1] (r(K) = -r, a_x(K) = -art_x, s(F tensor L) = Sw): -dim N^(I_s') = r - sum art - Sw. Same equation.

Step 1. PROVED. (H2) gives M tensor L_psi(x s') = sum over a of L_psi((a+s')x) tensor W_a. A block with a + s' != 0 is L_psi of Swan 1 tensor a tame module: every P-constituent has slope exactly 1, so
Swan = n_a (needs only 2.1.2.8 and the definition of s; 2.1.2.7 is not even needed). The block with a + s' = 0 is tame: Swan 0. So Sw_inf = r - n_(-s') (sum of n_a = r). With (H1): art_s = m(s).
(E) gives dim N^(I_s') = sum m(s) - n_(-s'). Generic s' gives (1) (rank N = sum m). Then the drop at w is n_a exactly at w = -a, which is (2). Cross-check with Laumon: 2.3.1.1 (ii), (iii) and 2.3.1.2 (p158-159) say the same: drop r(F_1) - s(F_1 tensor L(x s')) at s' != 0' (here n_(-s')) and r(F_[0,1[) - s(F_[0,1[) at 0' (here n_0).
(1) forces S nonempty (if S = {} then dim N^(I_s') = -n_(-s') < 0 for s' = -a): the hypotheses (H1), (H2), type T3 are inconsistent with S = {} but that is a consequence, not a gap (C9).

Step 2. PROVED. F'(F(P)) = a^*P(-1) (1.2.2.1, p141), and the rank statement for F' (same argument as Step 0 on the dual line, same psi, symmetric pairing, twist L_psi(x' sigma)) gives (E'). LHS = dim of the stalk of j_*(a^*M) at sigma = dim M^(I_(-sigma)) = r - m(-sigma). Tate twist and a^* do not change any dimension (k algebraically closed, no Frobenius used). Sum over w: art_w(N) = n_a + Sw_w(N) at w = -a (by (2)), 0 elsewhere (N lisse there, Sw = 0); sum of n_a = r. Slope parts of V' = N at infinity': for sigma != 0, R3 (i) gives Sw(V' tensor L) = r(V'_<1) + Sw(V'_1 tensor L) + Sw(V'_>1); V'_<1 tensor L has all slopes exactly 1 (P-constituents of slope lambda < 1 go to slope Sup(1,lambda) = 1), V'_>1 tensor L keeps slopes (Sup(1, lambda) = lambda). Finiteness claim: a P-simple W of slope 1 with W tensor L_sigma of slope < 1 gives, for tau != sigma, W tensor L_tau = (W tensor L_sigma) tensor L_(tau-sigma) of slope Sup(1, mu) = 1 (each P-constituent of W tensor L_sigma has slope mu < 1, simple by R3). There are finitely many isomorphism classes of P-simple constituents of V'_1, so for all but finitely many sigma, V'_1 tensor L_sigma has all slopes 1, Sw = r(V'_1), and m(-sigma) = 0. For such sigma: r = sum n_a + sum Sw_w + r(V'_<1) + r(V'_1) + Sw(V'_>1) - rank N = r + sum Sw_w + (Sw(V'_>1) - r(V'_>1)).
Both extra terms are >= 0; Sw(V'_>1) = sum lambda r(V_lambda) > r(V'_>1) for lambda > 1 unless V'_>1 = 0 (strict). So Sw_w(N) = 0 for every finite w, V'_>1 = 0. This is (3). Tate twist and a^*: harmless (PROVED).
No part of the finite-point conclusion uses irreducibility or type T3 beyond getting F(P) = j'_*N[1] (R5).

Step 3. PROVED. Subtract: for sigma != 0, m(-sigma) = r(V'_1) - Sw(V'_1 tensor L_sigma) (V'_<1 contributes r(V'_<1) both sides, V'_>1 = 0); for sigma = 0, L trivial, Sw(V') = Sw(V'_<1) + r(V'_1) (slope exactly 1), so m(0) = r(V'_<1) - Sw(V'_<1). Both match Laumon's printed (ii)' and (iii)' (p158) up to the sign of the twist (section 4).
Well-definedness of V'_(1,sigma): V'_1 tensor L_sigma has slopes <= 1 (R3 (ii)), hence a canonical decomposition as I-modules (p152) into a slope < 1 part and a slope 1 part. Tensoring back with L_(-sigma) is an I-module isomorphism, so V'_1 = A_sigma (+) B_sigma canonically as I-modules, A_sigma tensor L_sigma of slopes < 1 (A_sigma has slope exactly 1 because Sup(1, mu) = 1), B_sigma tensor L_sigma of slope 1. So A_sigma = V'_(1,sigma) is a direct summand, not merely a submodule. Then Sw(V'_1 tensor L) = Sw(A tensor L) + r(B), so m(-sigma) = r(A_sigma) - Sw(A_sigma tensor L_sigma) <= r(A_sigma), equality iff A_sigma tensor L_sigma is tame (2.1.4). OK.
Distinct sigma, tau: no common simple constituent (as P-modules, hence as I-modules): a P-simple U in both would give U tensor L_sigma, U tensor L_tau of slope < 1 each, but U tensor L_tau = (U tensor L_sigma) tensor L_(tau-sigma) has slope 1. Directness of the sum: needs the extra sentence that a nonzero submodule of A_sigma intersect A_tau would contain a simple submodule, which would be a common constituent; by induction on the number of summands the constituents of A_1 + ... + A_j (a quotient of the direct sum) are among those of the A_i, disjoint from those of A_(j+1). This also covers non-semisimple tame parts: nothing in Step 3 uses semisimplicity. Gap of one line (C3), no mathematical problem.
Chain: sum_s m(s) = m(0) + sum_{sigma != 0} m(-sigma) <= r(V'_<1) + sum r(A_sigma) <= r(V'_<1) + r(V'_1) = rank N, since V'_>1 = 0; (1) says the ends agree, so equality throughout: V'_1 = (+) A_sigma, A_sigma tensor L_sigma tame of rank m(-sigma), V'_<1 tame of rank m(0). With s = -sigma: A_sigma = L_psi(s x') tensor (tame of rank m(s)); this is (4).
Cases sigma = 0 and 0 in S or 0 in Freq: sigma = 0 is handled separately (V'_<1), and the frequency 0 of N at infinity' sits in V'_<1 (rank m(0)), the frequency 0 of M at infinity gives the singular point 0 of N (n_0 >= 1) and drop at 0'. No collision of roles: the two zeros enter (E') at different places. Non-semisimple W_a or V'_1: not used. The sign: see section 4.

## 3. The inductive consequences (item 7) and hidden hypotheses (item 8)

3.1 What Theorem 1 of PROOF_V2 takes from Lemmas A and B, and whether Lemma R delivers it.
- Rank N = sum m(s): (1). Location of singular set of Q_i: exactly -Freq/b, i.e. Sigma_i = rho_i S_(i-1) after the scaling by b = h c_i (Lemma T(b), PROVED, a change of variable): (2).
- Drop sizes n_a = m_(i-1)(s) (a = h c_(i-1) s): (2) with (4) of the previous stage; the blocks at infinity of M_(i+1) = L tensor N are the blocks of N tensored with the tame rank one L_inf: (4). Distinct s give distinct frequencies (b != 0).
- Tameness of M_(i+1) at S_(i+1): at a root (L tame, N lisse by (G)) and at points of Sigma_i (L lisse, N tame by (3)). Needed (H1). Lemma B's extra claims (I_w trivial on N^I; wild inertia through a finite p-group; Maschke) are no longer needed.
- Type T3 and irreducibility of Q_i: R5, not Lemma A. Irreducibility of M_(i+1): C-7 plus rank one tensor.
- The rank recursion: at a root z, M_(i+1) = L tensor N with scalar -1 on a module of rank rank N: m(z) = rank N = r_i... (indexing as PROOF_V2). Sum over Sigma_i of the drops is sum of n_a over the previous blocks = r_(i-1). So r_(i+1) = d r_i + r_(i-1). CHECKED below (3.3).
- Preservation of "M not lisse at any point of S": at a root, inertia acts by -1 on a module of positive rank, no invariants, not lisse; at w in Sigma_i, N has a drop n_a >= 1 and L is lisse. PROVED, for the exact set S_(i+1) = Z union Sigma_i (the roots are not in Sigma_i by (G)). S_(i+1) is the exact non-lisse set.
- Not delivered, not needed: characters of the tame parts (the lemma does not track them; the induction never uses them: the only character used is the scalar -1 of L at the roots). Lemma A's "summand at (inf, inf') has rank 0" is replaced by the equality case of Step 3.
Nothing Lemmas A and B gave and the induction uses is missing. The preconditions (G_k) are used exactly where PROOF_V2 uses them (Z disjoint from Sigma_i).

3.2 Hidden hypotheses.
- k algebraically closed: used (deg x = 1, no Frobenius, sigma in k). PROOF_V2 S5 is stated over k-bar. Over a finite field the lemma would need geometric versions. Not a defect.
- Coefficients: Q_l-bar throughout, as in Laumon. The l-adic/Q_l-bar formalism is cited (C-2), not opened by anyone. OPEN-standard.
- Irreducibility and T3 are used ONLY to obtain F(P) = j'_*N[1] with N lisse on a dense open (R5); Steps 0-3 do not use irreducibility of M or N.
- (H2) as a direct sum: Steps 0-1 use only additivity of Swan on exact sequences, so a filtration with the stated graded pieces would do for the hypothesis; Step 2 and 3 use only the slope decomposition of N at infinity'. (4) delivers a direct sum, and for the induction that is what is needed (M_(i+1) at infinity is L_inf tensor a direct sum). Not a defect (C7).
- Tame modules may be non-semisimple (unipotent monodromy): the lemma is correct for them; "tame" means P acts trivially (2.1.4).
- p: only that psi and L_psi exist and 2.1.2.8 holds (any p); p odd is used in the induction (chi != 1 at the roots).

3.3 Exact computation (CHECKED). Script ./round4/compute/C1/check_lemmaR_bookkeeping.py, output
.../compute/C1/check_lemmaR_bookkeeping_out.txt. One process, pure integers. It re-predicts the stalk dimensions of Q_i = F_(h c_i)(P_i) from statements (1), (2), (4) of the lemma and the
rules of the Consequence section ONLY (ranks, singular set rho_i S_(i-1), drop sizes, m at roots = rank Q_i, (G) asserted at every stage used), and compares with the COMPUTED column of the main-session engine
(a direct evaluation of the character sums, validated against double sums by its author, 0 mismatches on 189 values) in `toy-case/compute/main-session-check/round4_check_out.txt`, cases 1 (q = 3, f = x - 1, Q_1 to Q_4, h = 1, 2) and 2 (q = 3, f = x^3 - x + 1, Q_1, Q_2): 36 values compared, 0 mismatches; predicted ranks of Q_i: 1, 2, 3, 5 (d = 1) and 3, 10 (d = 3), the recursion r_(i+1) = d r_i + r_(i-1). A mutant with the sign of rho_2 flipped is rejected (mismatches at Q_2, y = 1, 2). Limits: F_3 points only; d = 1 up to Q_4, d = 3 up to Q_2; stalk Euler characteristics only; the test pins the composite of (2) and (4) (singular point at -(b s)), not each sign separately; it cannot see non-semisimplicity or wild behaviour. It re-uses the main session's engine output, it is not an independent evaluation of the sums.

3.4 Classical examples, by reasoning.
- P = j_*K_chi[1] on G_m (chi nontrivial, tame at 0 and infinity). S = {0}, r = 1, Freq = {0}, n_0 = 1, m(0) = 1. Lemma: rank N = 1; N singular exactly at 0' with drop 1; N tame at infinity' with a rank 1 block of frequency 0. Laumon 1.4.3.2 (iii) (p150, read): F(j_*K_chi[1]) = j'_*K_(chi^-1)(x')[1] tensor G(chi, psi), G of dimension 1 (1.4.3.2 (i)), a Kummer sheaf, tame, singular at 0' only. Agreement. PROVED.
- P = j_*(K_chi tensor L_psi(w x))[1] (translate by the kernel identity, F(K tensor L_psi(w x))(x') = F(K)(x' + w)): Freq = {w}, n_w = 1, S = {0}. Lemma: N singular exactly at -w, rank 1, drop 1, tame, block at infinity' of frequency 0. True answer: translate of K_(chi^-1)(x') by -w: singular at -w. Agreement. PROVED.
- P = j_*K_chi(x - s)[1], s != 0: S = {s}, Freq = {0}. Lemma (4): N at infinity' = L_psi(s x') tensor (tame of rank 1). True answer (change of variable in the kernel): F(K(x - s)) = L_psi(s x') tensor F(K): frequency +s. Agreement; this pins the sign of (4) by itself. PROVED.
- Skyscraper at s: F = L_psi(s x')[1] (1.4.2.1 (i), p149 formula with kernel L(s.x)), F' of that = skyscraper at -s (1.2.2.1): sign consistent with section 4.
- A Kloosterman sheaf is outside (H2) (slopes 1/n): the lemma says nothing about it, correctly.

## 4. The sign of the frequencies

PROVED: the lemma is right to avoid the printed (ii)'. The printed (ii)' (p158) reads: r_s(K) = r(K) + r((F'_inf')_1) - s((F'_inf')_1 tensor L(s.x')_inf'), with s the point of A. Laumon says (ii)', (iii)', (i)' follow from (ii), (iii), (i) by involutivity "(1.3.2.3)". But 1.2.2.1, 1.2.2.3 give K = a^*F'(F(K))(1), i.e. r_s(K) = r_(-s)(F'(K')), and (ii) applied to F' at the point -s carries the twist L(-s x'), not L(s x'). With the translation example above (frequency +s of N, drop of the stalk of K at s) the printed sign is inconsistent for s != 0 in characteristic != 2. So the printed (ii)' has a sign slip (or an unstated change of convention); I do not know which, OPEN at the source; harmless for the statements that are invariant under s -> -s and harmless for Lemma R, which derives the sign from 1.2.2.1. The cited exact computation (round4_check, case 1: singular point at rho_2 z = 2, not -rho_2 z = 1) pins the composite only (3.3), the individual signs of (2) and (4) are pinned by the three examples of 3.4. LEMMA_R's paragraph is correct and sufficient; it should add that the printed (ii)' has the opposite sign (COSMETIC C6).

## 5. Defects (all COSMETIC; none FATAL or REPAIRABLE)

- C1. R3: "simple module" must read "simple P-module", and "constituent" in Steps 2 and 3 means P-simple constituent (the statements of 2.1.2.7 are about P-modules; an I-constituent has a P-semisimple restriction, so nothing changes).
- C2. R4 as stated is stronger than the page: the first displayed line in the proof of 2.3.1.1 is the Euler characteristic form. The lemma only needs the Euler characteristic form; delete "sits in one degree" and the implicit H^0_c = H^2_c = 0.
- C3. Step 3: add one sentence for the directness of the sum for non-semisimple modules (no common simple constituent implies pairwise and iterated intersection zero).
- C4. R5 remark "involutivity 1.2.2.1 read by A2, not by me": it is on p141 and says F'F(K) = a_*K(-r) with the same psi; the quasi-inverse is 1.2.2.3 (p143) and 1.3.2.3 (p147). a_* = a^* for x -> -x.
- C5. R2 is for any K in D^b_c, not only perverse; make this explicit since Step 0 applies it to a sheaf G (the sign conversion in R1 is for complexes K = G[1]).
- C6. The sign section should note that the printed (ii)' of 2.3.1.1 has the opposite sign to what 1.2.2.1 gives (4).
- C7. (H2) could be weakened to "M at infinity has a filtration with graded pieces L_psi(a x) tensor W_a (W_a tame of rank n_a)"; the lemma then outputs a direct sum for N.
- C8. "j_*" in R5 and T3 is the ordinary pushforward = the middle extension on a curve (BBD 2.1.11, not opened); the page uses j_* in 1.4.2.1 and 1.4.3.1.
- C9. The lemma implies S is nonempty (the sum of the m(s) = rank N >= 1); say so, it explains why no lisse M on the whole line with slopes <= 1 exists beyond rank-one Artin-Schreier ones, consistent with T3.
- C10. "None of their proofs uses weights or purity": true for the pages I read (statements and proofs on p141-143, 147, 149-150, 152-156, 158-159). Not read: the proof of R2, the proofs in BBD 4.1.1, 4.1.2, 4.2.5, 4.3.1 (used by 1.3.2.3, 1.4.2.1), Serre/Katz for 2.1.2.6.

## 6. What I could not check

- The proof of Grothendieck-Ogg-Shafarevich (Raynaud, SGA 5 X): not read. All of the rank formulas depend on it.
- BBD 4.1.1, 4.1.2, 4.2.5, 4.3.1 and the proof of 1.3.1.1; Katz-Laumon 2.1.3; 1.2.2.1's use of 1.1.3.2, 1.1.3.4 (only the statement of 1.2.2.1 and the shape of its proof on p142-143 were read).
- Break decomposition existence (2.1.2.1 to 2.1.2.6, Hasse-Arf, Serre) was used from the page statements, not from the cited books.
- The Q_l-bar and l-adic formalism (proper base change, projection formula, C-2): standard, not opened.
- The identification of the stalk of the middle extension (BBD 2.1.11).
- 1.2.3.2 (translation): I used the elementary change of variables in the kernel instead; not read on the page again.
- The exact computation covers only F_3 points, small ranks, Euler characteristics, and reuses the main session's engine output.
- I did not test any statement with p >= 5, characters of order > 2, or ranks above 10.
- No Lean was run; none of the lemma is in Lean.

## 7. Short answer

Holds as written (ten cosmetic edits recommended). Steps 0 and 1 reproduce Laumon's own proof of 2.3.1.1/2.3.1.2; Steps 2 and 3 (involutivity plus counting) are correct; the induction gets everything Lemmas A and B gave. Remaining weight on unread proofs: GOS (Raynaud), BBD, and the Q_l-bar formalism.
