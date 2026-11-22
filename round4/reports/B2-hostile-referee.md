# B2 hostile referee report on PROOF_V2.md (round four)

Referee: agent B2. Subject: character sums over finite fields (Weil 1948 for y^2 = f(x)). Nothing here concerns the Riemann
Hypothesis for the integers. Started 2026-11-22 00:01 UTC (date -u). Labels: PROVED, CITED (where read), CHECKED (exact
arithmetic, script named), OPEN, HINT. Error classes: FATAL (the proof as written fails and no local repair is known),
REPAIRABLE (a gap or misstatement with a repair I can state), COSMETIC (wording, bookkeeping, no effect).

## 0. Verdict in one paragraph

Label for the whole: COMPLETE ON PAPER MODULO NAMED CITATIONS, with no fatal error found. One misstatement is repairable
(the register presents Laumon 2.4.2.1 as covering every finite point; the page covers only the three base points, so the
passage to s != 0 and s' != 0' needs a translation argument that PROOF_V2 only names). Everything else I found is cosmetic.
The proof has NOT been shown wrong anywhere I looked, and it is NOT yet a fully read proof: about a dozen cited statements
(listed in section 6) were not opened by anyone, including me. The step that carries the weight is S5; I checked the page
statements it uses, re-did its rank and Euler-characteristic bookkeeping independently, and found that its conclusion
reduces to a short robust statement (section 3, S5 (a)). The exact tests cannot see the thing S5 claims (cancellation between
degrees) and do not reach d = 3 with k >= 3.

## 1. What I actually did

1. Read PROOF_V2.md end to end.
2. Opened these page images of Laumon 1987 (PDF page number; journal page = PDF + 129) and read the statements: 006, 007
   (conventions 0.5 to 0.9, 1.1), 015, 016 (1.2.2.6 to 1.2.3.5, translation 1.2.3.2), 018 (1.3.2.1 to 1.3.2.4),
   019, 020 (1.4.1, 1.4.2, T1 to T3, 1.4.2.1), 021 (1.4.3.1, 1.4.3.2), 022 (2.1.1), 024, 025 (2.1.2.6, 2.1.2.7, 2.1.4, 2.1.5),
   029, 030 (2.3.1.1, 2.3.1.2, 2.3.1.3, 2.3.2), 031 (2.3.2.1, 2.3.2.3), 032 (2.3.3.1, 2.3.3.3), 033, 034 (2.4.1, 2.4.2.1,
   2.4.2.2, 2.4.2.3, 2.4.3), 036, 037, 038 (2.5.1 to 2.5.3.2, 2.5.4, 2.5.5 start). Not opened: 2.2.1.x, 2.2.2.x (pp. 155-157),
   1.3.1.x (p. 146), 1.2.2.1 (p. 141-142), the second half of 2.4.3, 2.5.5 onward, chapters 3 and 4.
3. Wrote `compute/B2/euler_check.py` (exact integers) re-deriving, from the invariant J(i) alone, the Euler characteristic
   of j_* M_k on the line and comparing with the claimed dimension r_{k+1} - [k odd]. Output `compute/B2/euler_check_out.txt`:
   112 of 112 cases agree (d = 1,2,3,4,5,6,7,9; k = 1..14). This checks the internal coherence of J; it does not check the
   sheaf theory.
4. Opened the Lean logs and statements of `Weighted.lean`, `Unbounded.lean` (did not recompile; the logs are later than the sources).
5. Argued each step adversarially (cases below). Nothing was run on the GPU or on the Lean archive of the Remark.

## 2. Page checks of the Laumon register (section 3.1 of PROOF_V2)

| item | claim in register | what the page says (my words) | verdict |
|---|---|---|---|
| L1 (1.3.2.3, 1.3.2.4, j.p.147) | F is an exact equivalence on perverse sheaves, simple to simple | matches; proof uses BBD 4.2.5, 4.1.1, 4.1.2, 1.3.1.1; no weights on the page | OK |
| L2 (1.4.2.1, j.p.149) | T3 exchanged with T3', F(j_*F[1]) = j'_*F'[1] | matches. T3 is defined with F irreducible and no constituent L(x.a') of F on U over k-bar. Note 1.4.1: Laumon works on Spec k "or Spec k-bar" | OK |
| L3 (2.3.1.1, j.p.158) | rank formulas, sign convention | page confirms formulas (i), (ii), (iii) in Euler-characteristic form. Translating to sheaf ranks I get exactly A1's reading: drop at s' != 0' equals r(F_1) - Sw(F_1 tensor L(x.s')); drop at 0' equals r(F_[0,1[) - Sw(F_[0,1[). Cross-check: s' = 0', F = L tame gives drop 1, stalk d-1, which is dim H^1_c(A, j_!L) | OK |
| L4 (2.1.2.7, j.p.153) | Sw(V tensor L) = r(V_[0,1[) + Sw(V_1 tensor L) + Sw(V_]1,inf[); Sw(V_1 tensor L) <= r(V_1) | matches; (ii) states equality iff (V_1 tensor L)^{I^(1-eps)} = 0 for some eps in [0, 1/r(V_1)[ (register's "no part of slope < 1" is equivalent here) | OK |
| L5 (2.3.1.2, j.p.159) | criterion for lissity | matches (a) s' != 0', (b) s' = 0' | OK |
| L6 (2.3.2.1, 2.3.2.3, j.p.160) | vanishing cycles at (infinity, s') | 2.3.2.1 (iii) is stated for every closed point s' of A' and every perverse K; 2.3.2.3 gives the ranks. Proof cites Th. finitude 2.16 and SGA 7 XIII 2.1.7.1 | OK as statement |
| L7 (2.3.3.1, j.p.161) | generic stalk at infinity' as sum over finite singular points plus (infinity, infinity') | matches; (iii) is an isomorphism of G_infinity'-modules, induced modules from the decomposition groups | OK |
| L8 (2.4.2.1, j.p.162) | "vanishing cycles at (s, infinity') are F^(0,infinity')(V)" | the page states three cases only: (i) the origin 0 of A with pi |-> x and pi' |-> 1/x' ; (ii) (infinity, 0') ; (iii) (infinity, infinity'). It is a lemma about germs at the ORIGIN of each line, with hypothesis pi^*K = V_![1] (extension by zero) | MISSTATED IN REGISTER, REPAIRABLE (E1) |
| L9 (2.5.3.1, proof j.p.166-167) | tame local transforms; no Gabber-Katz | statement and proof read: uses 1.2.3.1, 1.4.3.2 (iii), 2.3.2.1, 2.3.3.1, 2.4.2.1, 1.3.1.2, Lemma 2.5.3.2 (SGA 7 XIII 2.1.7.1); no 2.2.2.2. Gabber-Katz (2.2.2.2) is used at 2.5.4 (page 038), as A2 says. 2.5.3.1 (ii) is for Kummer modules V_chi with chi nontrivial, G(chi,psi) as an unramified twist | OK. Round-three B on 2.5.3 is wrong, A2 right |
| L10 (1.2.3.2, j.p.145) | translation: F(tau_e* K) = F(K) tensor L(<e,>) | matches; this is the global translation behind Lemma T(a). 1.2.2.9: formation of F commutes with every base change | OK |
| 1.4.3.2 (j.p.150) | Gauss sum module dim 1 in degree 1; F(j_*K_chi[1]) = j'_*K_{chi^-1}[1] tensor G(chi,psi) | matches (iii) | OK |
| conventions (0.6), (0.7), p.135 | formalism of D^b_c(X, Qbar_l) | Laumon says the t-structure on D^b_c(X, Qbar_l) needs a result of Gabber and Ekedahl UNPUBLISHED in 1987, and adds hypothesis (*) on k (automatic for k finite or algebraically closed); he uses "freely" theorems proved for finite Lambda-modules | the register's "Q_l formalism not opened" is a real but standard citation gap (section 6) |

Reading note: the statement numbers and journal pages in the register are right in every case I opened. I found no weight or
purity (in Deligne's sense) argument on any page I opened.

## 3. Verdict per step

"mod C-n" refers to the citation register of PROOF_V2.

### S0 (reductions). PROVED mod C-5, C-9. Exposition only.
Attacked: roots outside F_Q, f(0) = 0, translation by an element of F_Q, degree and squarefreeness after translation, the order
of choices. Fine: Q = q^s > d gives a in F_Q with f(a) != 0; x -> x + a is an F_Q-automorphism of A^1 carrying L_chi(f) to L_chi(f_a);
squarefreeness and degree are preserved; c is chosen after a (S3 depends on the roots of f_a). Small p: nothing uses p > d.
COSMETIC: "H^0_c = 0 by a direct argument" is a one-liner (U_0 is not proper); "H^2_c = 0" uses L geometrically nontrivial, true because
L is ramified at a root.

### S1 (identity and fibre bound). PROVED and CHECKED in Lean (Weighted.lean).
Re-derived: |F| N = M^k + R is orthogonality of psi; |S_h| <= ||t||^2 |F|^{(k-1)/2} <= |F|^{(k+1)/2} by k-1 operator-norm steps of norm |F|^{1/2}
(B_i B_i^* = |F| Id needs h c_i != 0, which is hypothesised) and D = diag(t) of norm <= 1. `identity_bound_oneW` has hypotheses psi != 0, |t| <= 1,
n >= 1, c_i != 0 for i < n and concludes |q N - M^(n+1)| <= (q-1) q sqrt(q)^n, the bound on R with k = n+1. Faithful. Not in Lean: psi o Tr nontrivial on
F_{Q^n} (true: trace is surjective). No error; characteristic free.

### S2 (power-sum lemma). PROVED, Lean. One COSMETIC point (E3).
Repair (b) for the embedding ("eigenvalues are algebraic over Q(zeta_p) by rationality") is valid only for eigenvalues of nonzero net multiplicity in the
L-function. In S9 the beta_0 with a = 0 and the eigenvalues beta of C are not seen by the L-function; their algebraicity follows from the fibre eigenvalues
(S8: beta^m is a fibre eigenvalue). The choice-free version works but the sentence should say so; repair (a) (fix iota on all of Qbar_l) covers everything.

### S3 (choice of c). PROVED; counting re-checked.
Closed form re-derived by hand: Sigma_2 = rho_2 Z, Sigma_3 = rho_3 Z u {0}, Sigma_4 = rho_4 Z u rho_4 rho_2 Z, Sigma_5 = rho_5 Z u rho_5 rho_3 Z u {0}. Each excluded
condition is a Laurent monomial in the c's with the largest index appearing once with exponent -1, so it removes at most (Q-1)^{k-2} tuples. Number of conditions
is the sum over i = 2..k-1 of floor(i/2) times |R_ratio| <= d^2, about (k^2/4) d^2. For k = 2 there is no condition beyond f(0) != 0. Roots outside F_Q: only
R_ratio intersected with F_Q^* matters, so d^2 still bounds it. No error.

### S4 (fibre = cohomology on the line). PROVED mod C-2.
Shift check G_{i+1} = j_!L tensor Rpr_!(pr^*G_i tensor L(h c_i x x')), P_i = G_i[i] gives P_{i+1} = (j_!L) tensor FT_{hc_i}(P_i) with FT_b = [b]^*F; I verified
FT_b = [b]^*F directly from the kernel. Base change and projection formula are used for separated finite-type morphisms; torsion coefficients are read, the
Qbar_l passage is an open item (section 6). No error.

### S5 (Fourier induction). PROVED mod L1 to L10, C-6, C-7, with repairable points E1, E4. Not re-derived by me from scratch; checked against the pages.
What I did: checked every page statement the induction uses (section 2), re-ran the bookkeeping independently (section 1, item 3), and went through each
step with a hostile eye.

(a) The conclusion of Theorem 2 is robust. If P_k is a simple perverse sheaf of type T3, then P_k = j_*M[1] with M irreducible lisse and not L(x.a')-like, and
H^m_c(A, P_k) for m != 0 vanishes by the elementary argument of Theorem 2 (no sections of j_*M with finite support; H^2_c(U,M) is dual to H^0(U, M^dual)(1) = 0
because M is irreducible and ramified at the roots, so it has no trivial constituent). So all the weight is on "P_k is simple of type T3". That needs
(i) Q_i = F(P_i) simple of type T3' (L1, L2: automatic from P_i simple of type T3); (ii) the location Sigma_i of the singular points of Q_i, so that Z is missed
(this is where (G) enters); (iii) j_!L tensor Q_i has no skyscraper at the roots (inertia -1 times a lisse stalk has no invariants) and is of type T3 (ramified at
every root, L(a'x) is lisse on A^1). I confirm (i) and (iii). Item (ii) is Lemma B together with the frequencies of Lemma A.

(b) Lemma A (structure of F(P) at infinity'): re-derived. 0 -> i_*(M^I) -> j_!M[1] -> j_*M[1] -> 0 is exact in the perverse category (the cone of
j_!M[1] -> j_*M[1] is i_*M^I[1]), so the skyscraper is a SUB; F is exact (L1); the generic stalk at infinity' is exact on perverse sheaves (H^0 of a perverse
sheaf is punctual); F(skyscraper of dim m at s) = L(sx')^m (L2). For j_!M[1] the hypothesis V_![1] of Laumon 2.4.2.1 holds literally at each finite singular point
and at infinity (K is the extension by zero from A). Ranks: generic rank of F(j_!M[1]) is |S| r by 2.3.1.1 (i) (a_s = -(r + Sw) = -r for tame V_![1]; slopes at infinity
<= 1 so the slope > 1 correction is 0); 2.3.3.1 (iii) and L9 give |S| r from the finite points (tame goes to tame of the same rank; for non-semisimple tame V by
exactness), hence the (infinity, infinity') summand has rank 0. The skyscraper sub sits block by block (distinct s give blocks L(sx') tensor tame with no
common constituent), so the quotient at s is L(sx') tensor (tame of rank r - dim M^{I_s}). Correct as written. Laumon's own proof of 2.4.3 (iii) b uses the
Gabber-Katz canonical extension (2.5.4, page 038); A1's rank count avoids it and I find it sound, since it applies the global rank count to the sheaf at hand,
not to a canonical extension of its germ.

(c) Lemma B (location and tameness at the finite singular points of N): re-derived. The rank of R^{-1}Phi at s' is r(V_1) - Sw(V_1 tensor L(x s')) (2.3.2.3): n_a if
s' = -a with a != 0, n_0 at s' = 0', 0 otherwise. The sequence 0 -> N^I -> N -> R^{-1}Phi -> 0 holds because the stalk of the middle extension j'_*N[1] has no H^0. So N is lisse
exactly off {-a}, and N/N^I has rank n_a there. Tameness: identify R^{-1}Phi at s' with F^(infinity,0')(V tensor L(s'x)) (E1); V tensor L(s'x) = W_a (tame) + slope-1 part; the
slope-1 part contributes rank 0 because the total rank is n_a and F^(infinity,0')(W_a) already has rank n_a (L9). So I_{s'} acts on N/N^I tamely and trivially on N^I; wild inertia P
acts on N through a finite p-group (l != p) with trivial action on a sub and the quotient, hence trivially (a finite group of unipotent matrices in characteristic 0 is trivial). Correct.

(d) Induction bookkeeping: frequencies A_i = h c_{i-1} S_{i-1}; singular points -a/(h c_i) = rho_i s with rho_i = -c_{i-1}/c_i, h cancels; r_{i+1} = d r_i + r_{i-1}. Re-checked by hand
and by `euler_check.py`. A further consistency point: for d = 1 and f(0) = 0 (condition f(0) != 0 violated) the fibre sum at k = 2 is g chi(hc)(Q^n - 1), which has a
NEGATIVE coefficient, so single-degree fails there, as it must; the hypothesis (G) is not decorative.

(e) Irreducibility of M_{i+1}: restriction of the irreducible N_i from A - Sigma_i to the smaller open is irreducible (surjectivity of pi_1: SGA 1 V 8.2 and the one-line corollary),
tensoring with a rank-one character preserves irreducibility. Correct. "Irreducible" means absolutely irreducible; the setting is geometric (k-bar), which Laumon 1.4.1 and (0.7) allow.

(f) Small characteristic (p = 3, p | d): nothing in S5 uses p > d or p > k. The danger would be wild ramification at the finite points of the transforms; Lemma B excludes it. L is tame
(order 2, p odd). Artin-Schreier sheaves L(ax), a in F-bar, have Swan 1 for a != 0 in every characteristic. No issue found.

(g) Constituents of local monodromy: tame simple I-modules are characters (2.1.4) and here lie in {1, chi}, chi^2 = 1, so G(chi,psi) versus G(chi^-1,psi) does not matter; and Laumon's statement
is for all tame modules (exactness), so no constituent bookkeeping is needed. COSMETIC (E2).

Repairable points in S5:
- E1 (translation to finite points s != 0 and s' != 0'). The register's L8 says vanishing cycles at (s, infinity') are F^(0,infinity')(V). The page covers only the origins. Two cases:
  * (infinity, s'), used in Lemma B: 2.3.2.1 (iii) and 2.3.2.3 are stated for every s'. To identify the module with a local transform at 0' one uses the global translation
    (L10, Lemma T(a): F(K tensor L(wx)) = tau_w^* F(K), kernel identity): vanishing cycles of F(K) at s' equal those of F(K tensor L(s'x)) at 0', and K tensor L(s'x) near infinity is again
    V_![1] with V replaced by V tensor L(s'x). Only the global translation (read on page 016) and 2.4.2.1 (ii) at the origin are used. Lemma T(c) is NOT needed on this side.
  * (s, infinity'), used in Lemma A: the kernel identity (x+s)x' = xx' + sx' gives sigma_s^* Ker(K) = Ker(tau_s^* K) tensor pr'^* L(sx'); nearby cycles along pr' commute with tensoring by a sheaf
    pulled back from the base trait (Psi(G tensor f^*B) = Psi(G) tensor B_eta), so the (s, infinity') vanishing cycles of K are L(sx') tensor the (0, infinity') vanishing cycles of tau_s^* K. This
    is the content of Lemma T(c): a formal compatibility (SGA 7 XIII 2.1.7 and relatives), NOT OPENED. REPAIRABLE. I do not believe it can fail.
- E4. Lemma A uses L9 for non-semisimple tame modules and the exactness of local transforms (2.4.3 (i) a, (ii) a; 2.5.1 says they follow from 2.4.2.2). Say so. Cosmetic.

### S6 (all h != 0). PROVED mod S5. Correct: the stalk of R^b at every geometric h != 0 vanishes for b != k, so R^b = 0 for b != k on all of G_m.

### S7 (global side). PROVED mod C-1 to C-5.
Re-derived: Rpr_! L(hQ_c) = i_{Y*} Q_l(-1)[-2] (C-10: stalk vanishes where Q_c(x) != 0); K[k] perverse (C-4); A^k - Y = D(Q_c) is affine; Artin vanishing in the perverse form
(BBD 4.1.2; maps to a point from affine schemes are affine) gives H^j_c(A^k, K) = 0 = H^j_c(A^k - Y, K) for j < k, so H^j_c(Y, K_Y) = 0 for j < k-1; excision gives
H^m_c(G_m x A^k, F) = 0 for m <= k and T injects into H^{k+1}_c. The Leray sequence over G_m degenerates (a single R^k). Correct. Requires c_i != 0 (Q_c nonzero) and L geometrically
nontrivial (H in degree 1). CHECKED (A4) only at the level of identities, as stated.

### S8 (fibre bound on the constant quotient). PROVED given S1, S2, S6. Correct.
The closed point h_0 of the dense open of lissity of R^k exists; h_0 != 0 and c_i != 0 in extensions; S1 holds over F_{Q^{mn}}. Frob_{h_0} acts on the constant quotient C as
Frob_Q^m; V_{h_0} -> C is Frobenius equivariant. The fibre sum is (-1)^k Tr(Frob^n | V_{h_0}) by single degree, with positive multiplicities, so S2 applies without cancellation.
No circularity: S8 uses S1 (elementary) and S5 (geometric), no weight statement.

### S9 (dichotomy). PROVED; Lean for the abstract lemma. Correct.
a_lambda = (-1)^{k+1}(m_{k+1} - m_{k+2}). If a(beta_0) != 0, S2 applies. If a(beta_0) = 0 then m_{k+2}(beta_0) = m_{k+1}(beta_0) >= 1, beta_0 = Q beta with beta an eigenvalue on C,
and S8 gives |beta_0| <= Q^{(k+3)/2}. I checked the Lean lemma `no_cancellation_signed3` as used: net coefficient zero forces a b-eigenvalue equal to the a-eigenvalue, and the b's are bounded by
hypothesis; correct. The Lean hypothesis has +1 on H^{k+1}_c and -1 on H^{k+2}_c, which is (-1)^{k+1} R_n; the bound is insensitive to the global sign. The identification of R_n with
the signed eigenvalue sum is NOT in Lean (a hypothesis), as A7 says.

### S10 (limit in k). PROVED, Lean. Correct; the s-th root is taken on positive reals.

### S11 (lower bound by duality). PROVED mod C-1, C-5, C-9, C-12. Correct as written.
Attacked: inertia -1 at every root and at infinity for odd d, so RGamma(I, L) = 0 and Rj_*L = j_!L; arithmetic self-duality (character valued in +-1); pairing H x H -> Q_l(-1) with Frobenius
acting by q; adjoint of F is q F^{-1}, same characteristic polynomial. dim H = d - 1 is even for odd d. For even d the control of A5 shows an unpaired eigenvalue, so d odd is used correctly.
Only C-12 (stalk of Rj_* as inertia cohomology) is unread, and it is standard.

### S12 (conclusion). Follows from S0 to S11. Not circular: S1, S2, S8, S9, S10 use no bound on the alpha_i; the one place where a "single degree" input replaces weights is S8, and it is geometric.

## 4. Errors, classed

FATAL: none found.

REPAIRABLE:
- E1. Local-transform lemma at finite points other than the origin: register L8 overstated; repairs in S5 above. Standing item: Lemma T(c) (SGA 7 XIII) for the (s, infinity') side only. (PROOF_V2 lists it
  as C-15 and D-5; my corrections are that L8 itself is not stated on the page for s != 0 and that the (infinity, s') side does not need T(c).)
- E5. PROOF_V2 section 3.1, first paragraph, says A2 "read the proofs of every item below on the images" and found no weight argument. L6, L7, L9 rest on SGA 7 XIII 2.1.7.1 and Th. finitude, not opened by
  anybody. The weight statement holds for the text of Laumon read, not for those inputs. Section 8 item 10 admits it, but the paragraph in 3.1 overstates. Reword.

COSMETIC:
- E2. L9 covers all tame modules by exactness; no constituent bookkeeping is needed.
- E3. S2 repair (b): algebraicity of the beta's of C comes from the fibre eigenvalues, not from the L-function.
- E4. State the use of exactness for non-semisimple tame modules in Lemma A.
- E6. Register (L2): "irreducible" in Laumon's definition is for the sheaf over k, the constituent condition is over k-bar; with k = k-bar they agree.
- E7. D-1 (Gabber-Katz is not used in 2.5.3.1) is confirmed on pages 037 and 038.

## 5. Test coverage (what the exact computations cannot see)

- The induction is tested only through net (Euler characteristic) counts, 4471 data points (A3). A net count cannot see cancellation between H^k and H^{k+1} of a fibre: it would be
  satisfied also if P_k had an extra skyscraper sub and quotient of equal rank. The vanishing is a theorem of the induction, not a measurement.
- d = 3 is reached only for k = 2; d = 1, 2 deeper. There is no data point with d >= 3 and k >= 3, the only regime in which the final argument is applied. The failure controls ((G) violated)
  disagree with the predictions, so the tests are not vacuous.
- My own check (section 1, item 3) shows J is internally consistent up to k = 14 for d up to 9.

## 6. What I could not check, and what nobody has checked

NOT OPENED by me (and by nobody, per PROOF_V2 section 8): proof of Grothendieck-Ogg-Shafarevich (Raynaud); inner proofs of the trace formula (Rapport 5 to 8, Weil's fixed-point theorem);
SGA 7 XIII 1.4.2.2, 2.1.1, 2.1.7.1; SGA 4 XVII 5.2.6, 5.2.9, 5.4.3; Theoreme de finitude 2.16 in the form Laumon uses; BBD 2.1.11, 4.3.1 (OCR only, by others); SGA 1 V 8.2 (text layer only);
the Qbar_l formalism (Ekedahl, Weil II 1.1; Laumon himself says it was unpublished in 1987); compact-support Kunneth over Qbar_l with Frobenius equivariance; Laumon pages not in my list in
section 1 (2.2.1.x, 2.2.2.x, 1.2.2.1, 1.3.1.x). The claim "no weights" is a statement about the pages named in section 1 only. I did not recompile the Lean files; I read their statements and
logs. I did not run any exact computation of the fibre cohomology beyond the Euler-characteristic bookkeeping.

On circularity: I find no use of the bound being proved. The nearest candidate is the trace formula, whose proof in the Rapport goes through Weil's fixed-point theorem (an intersection-number
identity, not the Riemann hypothesis for curves); for the rank-one sheaf on the line it can be replaced by the zeta function of the hyperelliptic curve (Schmidt, Riemann-Roch), but for the
higher-dimensional sums of S7 and S8 there is no replacement short of the general trace formula.

## 7. Label for the whole

"Complete on paper modulo named citations; no gap known to the referee; one misstated lemma (L8 away from the origin) repairable by a formal translation argument; the unopened citations of
section 6 remain; S5 depends on Laumon 1987 as a black box whose proofs were opened only for the statements in section 2." It is not a proof of anything about the Riemann Hypothesis for the
integers, and it is a route to Weil's 1948 bound whose novelty is not established.
