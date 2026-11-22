# A1. The Fourier induction (S5), re-derived

Agent A1, round four. Written before opening section S5 of `../round3/PROOF_DRAFT.md` and before opening
`../round3/reports/B-*.md`. Parts 1 to 6 are my own derivation; part 7 is the comparison, written after.
This is about character sums over finite fields (Weil 1948 setting). Nothing here concerns the Riemann
Hypothesis for the integers.

Labels: PROVED (argument given here), CITED (statement number and journal page of Laumon 1987, read on the page
image; journal page = PDF page + 129), CHECKED (exact arithmetic, script named), OPEN, HINT.
Laumon's paper is cited in my own words, no passage is copied.

Started 2026-11-21 23:00 UTC.

## 0. What I read, and what I did not

Read on the page images by me: PDF pages 18 (journal 147), 19, 20 (149), 24 (153), 26 (155), 27 (156), 28 (157),
29 (158), 30 (159), 31 (160), 32 (161), 33 (162), 34 (163), 35 (164), 36 (165), 37 (166). I did not read the
Kummer statements 1.2.3.1 and 1.4.3.2 (used inside the proof of 2.5.3.1, hence inside the tame local transforms), nor 1.2.2.1/1.2.2.3
(involutivity), nor anything of 2.5.4 onward (the wild case). Not opened: `LAU.txt` and every other OCR dump.
Compute: `compute/A1/bookkeeping.py`, output `compute/A1/bookkeeping_output.txt` (exact rational arithmetic).

## 1. Setting and conventions (my fixing)

* k = algebraically closed field of characteristic p odd (everything geometric; Laumon allows `Spec(k)` or
  `Spec(k-bar)`, 1.4.1, p. 148). l != p. psi: F_p -> Qbar_l^* nontrivial. L_psi(a x) is the Artin-Schreier sheaf
  on A^1, pulled back by x -> a x.
* chi: a nontrivial tame character (for the toy, quadratic). f squarefree of degree d >= 1 (I will not need d odd
  or d >= 3 in this part), Z the set of its d roots in k, 0 not in Z (f(0) != 0). L = chi(f) lisse of rank 1 on
  A - Z, tame (p odd), with local character chi at each z in Z (w.r.t. the uniformiser x - z) and some tame
  character at infinity. j_!L = j_*L because the monodromy at z is nontrivial.
* Fourier transform F = F_psi (Laumon 1.4.1.1, p. 148): F(K) = R pr'_!(pr^*K tensor L(x x'))[1], kernel L_psi(x x').
  For b in k^*: F_b(K) := R pr'_!(pr^*K tensor L(b x x'))[1] = [b]^* F(K), [b](w) = b w (base change for R pr'_! along the
  automorphism (x, x') -> (x, b x') of the plane; PROVED, immediate). It is the transform that appears in P_(i+1).
* P_1 = j_!L[1], P_(i+1) = (j_!L) tensor F_(b_i)(P_i), b_i = h c_i, with h != 0 and all c_i != 0.
  Shift convention as in the brief (F contains the [1]); the shifts are checked by A4, not here.
* rho_i := -c_(i-1)/c_i (2 <= i <= k-1).
* Convention warning (Laumon 2.2.1, p. 155): for a perverse K = F[1] with F a sheaf the integers r(K), r_x(K), s_x(K),
  a_x(K) are Euler characteristics, hence negative: r(K) = -rank F, r_x(K) = -(dimension of the stalk of
  H^(-1)K at x), a_x(K) = -(r(F) + Sw_x(F) - dim stalk). Lemma 2.2.1.1 says a_x(K) <= r(K) - r_x(K) <= 0.
  Below I write everything in terms of ranks of sheaves.
  For a lisse sheaf M on U = A - S with K = j_*M[1] and s in S set
  m(s) := r(M) - dim M^(I_s) (the rank of the part of M on which I_s acts nontrivially), a_s(K) = -(m(s) + Sw_s(M)).

## 2. The Laumon inputs, with hypotheses checked on the page

Each item: statement in my words, journal page, what has to hold here, and whether it does.

* **L1 (1.3.2.3, 1.3.2.4, p. 147).** F is an exact equivalence Perv(A) -> Perv(A') (quasi-inverse a^*F'(-)(1)), so it sends
  simple perverse sheaves to simple perverse sheaves. Hypothesis: K perverse on the line over `Spec(k)`. Holds. The proof on the
  page uses BBD 4.2.5, 4.1.1, 4.1.2 and 1.3.1.1, no weights.
* **L2 (1.4.2.1, p. 149).** Simple perverse sheaves on A are of type T1, T2 or T3 (BBD 4.3.1 (ii), quoted); F exchanges T3 and T3'. For K = j_*F[1]
  of type T3 there is a maximal open U' of lissity and an irreducible lisse F' on U' with F(K) = j'_*F'[1], again of type T3'.
  T3 means: F irreducible lisse on a dense open U, and no subquotient of F|U (over k-bar) is isomorphic to L(x.a')|U for any a'.
  Also the first formula of 1.4.2.1 (i): F(i_*F) = (pr_A')_*(L(s.x) tensor pr_s^*F)[1], so the transform of a skyscraper
  of dimension m at s is L_psi(s x')^m in degree -1.
  Hypothesis for use: P_i is of type T3. This is part of the induction (part 4).
* **L3 (2.3.1.1, pp. 158-159).** Rank formulas. In my rank language (signs fixed as in part 1), for K = j_*F[1] of type T3 and K' = F(K) = j'_*F'[1]:
  (i) r(F') = sum over s in S of deg(s) (m(s) + Sw_s(F)) + (Sw - rank) of the part of F_(infinity) of slopes > 1;
  (ii) for s' != 0': stalk rank of K' at s' = r(F') - ( r(F_1) - Sw(F_1 tensor L(x.s')) ), F_1 the slope-1 part of F at infinity;
  (iii) stalk rank at 0' = r(F') - ( r(F_[0,1[) - Sw(F_[0,1[) ).
  The proof (p. 159): proper base change gives the stalk rank as an Euler characteristic of A with coefficients in K tensor L(x.s'); then
  Grothendieck-Ogg-Shafarevich (2.2.1.2, p. 156) and 2.1.2.7 (p. 153). No weights. Hypothesis: K perverse, nothing else. Holds.
  **Sign remark.** In Laumon's printed form (ii) reads r_s'(K') = r(K') + r(F_1) - s(F_1 tensor L). With r(K') = -rank this IS
  "stalk rank = generic rank minus (r(F_1) - s)", a drop. Read as ranks with plus signs (as the notes' paraphrase does) it would say the stalk is larger than the
  generic fibre, which is impossible for K' = j'_*F'[1]. I checked it on the example K = L_psi(ax)[1], K' = skyscraper at -a.
* **L4 (2.1.2.7, p. 153).** For a rank-one I-module L of Swan conductor 1 and any I-module V: Sw(V tensor L) = r(V_[0,1[) + Sw(V_1 tensor L) + Sw(V_]1,infinity[),
  and Sw(V_1 tensor L) <= r(V_1) with equality iff V_1 tensor L has no part of slope < 1. Used with L = L_psi(a x) at infinity, a != 0 (slope 1; 2.1.2.8, quoted on p. 159; not read by me).
* **L5 (2.3.1.2, p. 159).** U' depends only on F_(infinity),[0,1]. A point s' != 0' lies in U' iff (F_1 tensor L(x.s')) has no part of slope < 1; the point 0' lies in U' iff F_(infinity),[0,1[ = 0.
  The proof is "immediate from 2.2.1.1 and 2.3.1.1" (p. 159); I re-checked the equivalence using L3 (ii), (iii) and L4: s' in U' iff stalk rank = generic rank
  iff Sw(F_1 tensor L(x.s')) = r(F_1) iff no slope < 1 in F_1 tensor L(x.s'). Holds.
* **L6 (2.3.2.1, 2.3.2.3 and the exact sequence on p. 160).** For s' in S' the module of vanishing cycles R^(-1)Phi_(s') (K') sits in 0 -> H^(-1)(K'_(s')) -> F'_(eta s') -> R^(-1)Phi -> H^0(K'_(s')) -> 0.
  For K' = j'_*F'[1] this says R^(-1)Phi = F'/F'^(I_s'), of rank m'(s'). It is isomorphic to R^(-1)Phi of the kernel sheaf at the point (infinity, s'), and its rank equals
  r(F_1) - Sw(F_1 tensor L(x.s')) if s' != 0', and r(F_[0,1[) - Sw(F_[0,1[) if s' = 0'. Hypothesis: K perverse. Holds.
* **L7 (2.3.3.1, p. 161).** For K perverse: vanishing cycles at (s, infinity') for s in S and at (infinity, infinity') are in degree -1 only, are zero on U x eta_(infinity'), and
  F'_(infinity') is the direct sum over s in S of the induced modules of R^(-1)Phi at (s, infinity'), plus R^(-1)Phi at (infinity, infinity'). The proof (p. 161) uses 1.3.1.2 and SGA 7 XIII 2.1.7.1. Holds.
  Over k = k-bar the induced modules are the modules themselves.
* **L8 (2.4.2.1, 2.4.2.2, 2.4.2.3, p. 162-163).** If near a point the perverse sheaf is V_![1] for an I-module V (V_! = extension by zero), the vanishing cycles at (s, infinity') are the local transform
  F^(0,infinity')(V) (point s = 0, kernel L(pi/pi') with pi = x, pi' = 1/x'), those at (infinity, 0') are F^(infinity,0')(V) (pi = 1/x, pi' = x', kernel L(pi'/pi)).
  Hypothesis: the perverse sheaf is V_![1] on the henselian trait. Holds for j_!M[1] at each point of S and for K~ near infinity (lisse there).
  **It does NOT hold literally for j_*M[1] at a point with invariants, and it is stated only for the point 0 (resp. infinity).**
  Both are handled in part 3 (Lemma A, steps 1 and 2).
* **L9 (2.4.3 (i) b), (ii) b), p. 163-164, proved in 2.5 pp. 165-166).** Tame case only. For a tame I-module V at a finite point: F^(0,infinity') is exact, rank r(V) + s(V) = r(V), Swan s(V) = 0, so the image is tame.
  For a tame I-module V at infinity: F^(infinity,0') is exact, rank r(V) - s(V) = r(V), Swan 0. The wild statements (vanishing on slopes >= 1 of F^(infinity,0'), of F^(infinity,infinity') on slopes <= 1)
  I do not use (they are proved in the part of 2.5 I did not read); the rank comparison in Lemma A, B replaces them. The tame cases follow from 2.5.3.1 (p. 165; proof pp. 165-166): trivial -> trivial, nontrivial Kummer chi -> rank one Kummer
  with the same chi (with respect to the uniformisers pi = x - s, pi' = 1/x' resp. pi = 1/x, pi' = x'), twisted by an unramified Gauss sum.
  In the proof on p. 166 I read the use of FT(j_*K_chi(x)) = j'_*K_(chi^-1)(x') tensor G(chi, psi) (cited from 1.4.3.2 (iii), not read) and 2.3.2.1, 2.3.3.1, 2.4.2.1, 1.3.1.2, Th. finitude 2.16.
* **L10 (2.2.1.2, p. 156).** Grothendieck-Ogg-Shafarevich for projective X. Used inside L3 and in the final Euler characteristic computation (part 5).

## 3. Two local lemmas (my own statements and proofs)

Standing notation. P = j_*M[1] is a simple perverse sheaf of type T3 on the line over k, j: U = A - S -> A, S finite, M lisse irreducible of rank r on U.
Assume:
 (H1) M is tame at every s in S (wild inertia acts trivially);
 (H2) M_(infinity) as I_infinity-module is a sum of blocks L_psi(a x) tensor W_a, a in a finite set A(M) of k, with W_a tame of rank n_a >= 1
      (so every slope is 0 or 1: slope 0 for a = 0, slope 1 for a != 0).
For s in S put m(s) = r - dim M^(I_s) >= 1 (>= 1 because s in S means I_s acts nontrivially).

### Lemma T (translation, scaling). PROVED
(a) F(K tensor L_psi(w x))(v) = F(K)(v + w) for K perverse and w in k: the kernel satisfies L(x (v + w)) = L(x v) tensor L(w x). So F(K tensor L(w x)) = tau_w^* F(K), tau_w(v) = v + w. In particular the local structure of F(K) at the point w
 equals that of F(K tensor L(w x)) at 0'.
(b) F_b(K) = [b]^*F(K), b != 0. Singular points scale by b^(-1), a block L_psi(s x') at infinity' becomes L_psi(b s x'), tame data are unchanged (b is a unit, so the identification of tame inertia is unchanged).
(c) F(tau_s^* K) = L_psi(-s x') tensor F(K) (change of variable y = x - s in R pr'_!). Together with the fact that R Psi relative to pr' depends only on the generic fibre D x eta_(infinity'), so that R Psi (G tensor pr'^*E) = R Psi (G) tensor E for E lisse on eta_(infinity'),
 this identifies the summand of F'_(infinity') belonging to the finite point s in L7 with L_psi(s x') tensor (summand of F(tau_s^*K) belonging to 0). Laumon uses RPsi = RPhi here (p. 161, last lines of the proof of 2.3.3.1). **This is the one place where I rely on a compatibility Laumon does not state on the pages I read for s != 0; I consider it standard (SGA 7 XIII, compatibility of nearby cycles with twisting by a sheaf coming from the base), NOT opened.**

### Lemma A (structure of F(P) at infinity'). 
Under (H1), (H2): F(P) = j'_*N[1] with N irreducible lisse of type T3' and
 (A1) rank N = sum over s in S of m(s);
 (A2) N_(infinity') = direct sum over s in S of L_psi(s x') tensor Wh_s, with Wh_s tame of rank m(s); (all slopes <= 1, the block of frequency s = 0 is tame.)
Proof. T3' and N irreducible: L2. (A1): L3 (i); the part of F_infinity with slope > 1 is zero by (H2), so rank N = sum_s (m(s) + Sw_s(M)) = sum_s m(s) by (H1).
(A2). Step 1 (j_! instead of j_*). Put K_! = j_!M[1]. Triangle j_!M[1] -> j_*M[1] -> i_*(M^I)[1] with M^I = (M^(I_s))_s in S, all three terms perverse, so 0 -> i_*(M^I) -> K_! -> P -> 0 is exact in Perv(A) (BBD 1.3.6).
 Apply F (exact, L1), then pass to the generic stalk of H^(-1) at eta_(infinity') (exact on perverse sheaves because H^0 is punctual): 0 -> (+)_s L_psi(s x')^(m_0(s)) -> F(K_!)_(infinity') -> N_(infinity') -> 0, m_0(s) = dim M^(I_s), by L2 for the skyscraper.
Step 2 (the summands of F(K_!)). L7 for K_! writes F(K_!)_(infinity') as a sum of the modules R^(-1)Phi at (s, infinity') and (infinity, infinity'). By L8 + Lemma T(c), the summand at s is L_psi(s x') tensor F^(0,infinity')(M_(eta s)), where M_(eta s) is the I_s-module M
 (K_! is V_![1] near s with V = M_(eta s)). By L9 (tame), it is tame of rank r. Its Swan conductor is 0.
Step 3 (the summand at (infinity, infinity') is zero). From step 1, rank F(K_!)_(infinity') = rank N + sum_s m_0(s). From step 2 and L7 it also equals sum_s r + rank of the (infinity, infinity') summand.
 By (A1), rank N = sum_s m(s) = sum_s (r - m_0(s)). Comparing: the rank of the (infinity, infinity') summand is 0, hence the summand is 0. (This replaces the wild theorem 2.4.3 (iii) b), which I do not use.)
Step 4. The submodule (+)_s L_psi(s x')^(m_0(s)) sits inside (+)_s L_psi(s x') tensor Theta_s, Theta_s := F^(0,infinity')(M_(eta s)) tame of rank r. Distinct s give modules with no common Jordan-Hoelder constituent
 (a constituent of L_psi(s x') tensor Theta_s has slope 1 and "frequency" s if s != 0, slope 0 if s = 0; L_psi((s - t)x') tensor tame is irreducible only if of slope 1 for s != t), so every submodule is the direct sum of its intersections with the summands.
 Hence N_(infinity') = (+)_s L_psi(s x') tensor (Theta_s / Triv_s) with Triv_s of rank m_0(s) the image of the skyscraper's module (trivial because the skyscraper contributes L_psi(s x')^m_0 itself). Put Wh_s = Theta_s/Triv_s: tame (quotient of tame), rank r - m_0(s) = m(s). QED.

Remark: Wh_s can contain trivial constituents of the I_infinity'-module, and can be non-semisimple (Jordan blocks); nothing below needs its characters.

### Lemma B (singular points and local monodromy of F(P)). 
Under (H1), (H2): 
 (B1) the set of points where N is not lisse is Sing = { -a : a in A(M) } (so 0' lies in Sing iff A(M) contains 0, i.e. iff M_infinity has a nonzero tame part);
 (B2) at w = -a in Sing, N is tame (I_w-action through the tame quotient) and rank (N / N^(I_w)) = n_a.
Proof. (B1) is L5 with F_1 = (+)_(a != 0) L_psi(a x) tensor W_a: F_1 tensor L(x.s') = (+) L_psi((a + s')x) tensor W_a has a slope-0 part iff a + s' = 0 for some a != 0; and 0' in Sing iff F_[0,1[ = W_0 != 0.
(B2). By L6, N/N^I = R^(-1)Phi_(w)(F(P)) has rank n_a (L6 with Sw(F_1 tensor L) = r(F_1) - n_a if w != 0'; for w = 0' rank r(F_[0,1[) - 0 = n_0). By Lemma T(a) this module is R^(-1)Phi_(0')(F(P tensor L(w x))), then by L6 the vanishing cycles at (infinity, 0') of the twisted sheaf,
 and by L8 (infinity near K~ = P tensor L(w x), lisse there, so K~ = V_![1] near infinity with V = M_(infinity) tensor L_psi(w x) = (+)_(a' != a) L_psi((a'-a)... sign: a' + w) tensor W_(a') (+) W_a) it equals F^(infinity,0')(V). F^(infinity,0') is additive. The summand F^(infinity,0')(W_a) is tame of rank n_a (L9) and the total has rank n_a (L6), so
 the summand F^(infinity,0')((+)_(a'+w != 0) L_psi((a'+w)x) tensor W_a') has rank 0: it is 0 (ranks of modules are >= 0). So N/N^(I_w) = F^(infinity,0')(W_a), tame. N^(I_w) has trivial action of I_w; thus the wild inertia P_w acts trivially on N^I and on N/N^I.
 An l-adic representation of a pro-p group factors through a finite p-group, and a finite p-group representation in characteristic 0 is semisimple (Maschke): so P_w acts trivially on N, i.e. N is tame at w. QED.

## 4. The induction invariant, the condition on c, and the proof that P_(i+1) is of type T3

Define finite sets and functions by recursion (all in k).
 S_1 = Z; Sigma_1 = {0}; for i >= 2: Sigma_i = rho_i S_(i-1); S_(i+1) = Z u Sigma_i. (S_2 = Z u {0}.)
 Block ranks: m_1 = 1 on Z. Mu_1 (0) = 1 (the rank of the tame part of L at infinity). For i >= 2: Mu_i(rho_i s) = m_(i-1)(s) (summed over coincident points); m_(i+1)(z) = r_(i+1) for z in Z, m_(i+1)(w) = Mu_i(w) for w in Sigma_i.
 Ranks: r_1 = 1, r_(i+1) = sum over s in S_i of m_i(s).
 Closed form for Sigma_i (CHECKED against the recursion for i <= 8, `bookkeeping_output.txt`): with pi(i, m) = rho_i rho_(i-2) ... rho_m for m = i, i-2, ..., >= 2,
 Sigma_i = { pi(i,m) z : z in Z, m = i, i-2, ..., >= 2 } u ( {0} if i odd ).
 So 0 in S_i iff i is even; the sets are rational functions of the ratios c_(j-1)/c_j and of Z only. h does not occur.

**Condition C_k on (f, c).** Z and Sigma_i are disjoint for 1 <= i <= k - 1. Explicitly (0 not in Z by f(0) != 0): for every 2 <= i <= k-1, every m in {i, i-2, ...} with m >= 2, and all z, z' in Z:
 z' != rho_i rho_(i-2) ... rho_m z. Equivalently rho_i rho_(i-2) ... rho_m is not in R' := {z'/z} (R' contains 1 as z = z' is allowed).
 It does not involve h. It is a finite union of proper hypersurface conditions on (c_1, ..., c_(k-1)) in the torus (each says a Laurent monomial in the ratios equals one of the finitely many elements of R').
 Consistency checks (CHECKED, script): plain quadric c_i = 1 gives all rho_i = -1 and Sigma_4 contains Z (rho_4 rho_2 = 1): first failure at i = 4. c_1 = -c_2 gives rho_2 = 1 and Sigma_2 = Z: failure at i = 2 (k = 3). For c = (1,1,-2) the conditions i <= 3 hold for generic Z.

**Theorem 1 (the induction).** Let k_ = k-bar of odd characteristic, h != 0, c_i != 0 and C_k hold. Then for every 1 <= i <= k the following J(i) holds (it does not depend on h):
 (J1) P_i = j_*M_i[1], M_i lisse irreducible on U_i = A - S_i, rank r_i, with S_i as above (a disjoint union Z u Sigma_(i-1)), and P_i is a simple perverse sheaf of type T3. In particular extension by zero equals middle extension at every point of S_i.
 (J2) M_i is tame at every point of S_i; at z in Z it is (a scalar character: chi-twist of a trivial local system) of rank r_i, so m_i(z) = r_i; at w in Sigma_(i-1) the rank of M_i/M_i^(I_w) is Mu_(i-1)(w) = m_i(w) >= 1.
 (J3) M_i|I_infinity = (+) over a in A_i of L_psi(a x) tensor W_a with W_a tame, where A_1 = {0}, W_0 = L|I_infinity, and for i >= 2: A_i = { b_(i-1) s : s in S_(i-1) }, rank W_(b_(i-1) s) = m_(i-1)(s). (All slopes in {0,1}.)
 (J4) r_(i+1) = sum over S_i of m_i = d r_i + r_(i-1) (r_0 := 0), so r_1 = 1, r_2 = d, r_3 = d^2 + 1, r_4 = d^3 + 2d.
Proof by induction.
 i = 1. P_1 = j_!L[1] = j_*L[1], L rank one irreducible, M_1 = L. T3: L|(A - Z) is ramified at every z in Z (nontrivial monodromy) while L_psi(a' x) is lisse on A, so no isomorphism. Simple: j_*(irreducible lisse)[1] is simple (BBD 4.3.1; on a curve j_! * = j_*). (J2): tame at z since p is odd, scalar chi, m_1(z) = 1. (J3): L at infinity is tame, A_1 = {0}, W_0 = L_infinity, rank 1. (H1), (H2) hold.
 i -> i+1 (1 <= i <= k-1). (H1),(H2) hold for P_i by J(i). Put b = b_i = h c_i != 0 and Q_i = F_b(P_i) = [b]^*F(P_i).
 Step 1. By L1, L2, Lemma A and Lemma T(b): Q_i = j'_*N_i[1] is simple of type T3', N_i irreducible lisse on A - Sing(Q_i) of rank sum_(s in S_i) m_i(s) = r_(i+1) (this is the rank of M_(i+1) after the twist),
  N_i at infinity = (+)_(s in S_i) L_psi(b s x) tensor Wh_s (all blocks, Wh_s tame of rank m_i(s)).
 Step 2. By Lemma B and T(b): Sing(Q_i) = { -a / b : a in A_i }. For i = 1, A_1 = {0}: Sing(Q_1) = {0} = Sigma_1. For i >= 2, A_i = b_(i-1) S_(i-1) so -a/b = -(h c_(i-1))/(h c_i) s = rho_i s: Sing(Q_i) = rho_i S_(i-1) = Sigma_i (h cancels). N_i is tame at each point w of Sing(Q_i) and the rank of N_i/N_i^I at w equals the rank of the block of A_i that is killed, i.e. m_(i-1)(s) for w = rho_i s (for i = 1: rank 1 at w = 0).
 Step 3 (P_(i+1) is a middle extension of an irreducible lisse sheaf). P_(i+1) = (j_!L) tensor Q_i. Let U_(i+1) = A - (Z u Sigma_i) and M_(i+1) = (L tensor N_i)|U_(i+1).
  - Irreducible: N_i is irreducible on A - Sigma_i, hence its restriction to the smaller open U_(i+1) is irreducible (pi_1 of the smaller open surjects, removing points from a normal connected curve), and tensoring with a rank one lisse sheaf is an autoequivalence. 
  - P_(i+1) = j_*M_(i+1)[1]: at a point u outside Z u Sigma_i both are L tensor N_i[1]. At w in Sigma_i - Z, L is lisse near w so (j_!L) tensor j'_*N_i[1] = j_*(L tensor N_i)[1] there (tensoring with a lisse sheaf commutes with j_*). At z in Z: **here C_k is used**: z is not in Sigma_i, so Q_i = N_i[1] is lisse near z with I_z acting trivially on N_i, hence (L tensor N_i)|I_z = chi^(r_(i+1)) (scalar chi), which has no invariants because chi != 1. So (j_!L tensor N_i)[1] = j_!(L tensor N_i)[1] = j_*(L tensor N_i)[1] near z.
  - Simple: BBD 4.3.1 (irreducible lisse on U gives a simple middle extension), done.
 Step 4 (T3: not an Artin-Schreier sheaf). M_(i+1) is irreducible, so its only subquotient is itself. It is ramified at every z in Z (character chi, nontrivial), while L_psi(a' x)|U is the restriction of a sheaf lisse on all of A; so M_(i+1) is not isomorphic to any L_psi(a' x)|U (this works for every d >= 1, and Z is nonempty). For d >= 2 one can also say rank r_(i+1) >= 2. 
 Step 5 (J2, J3, J4 for i + 1). Singular set exactly S_(i+1): at z, monodromy chi^(r) nontrivial; at w in Sigma_i, N_i is not lisse (L lisse there), so M_(i+1) is not lisse. Tameness: at z scalar chi; at w tame by Lemma B. J2 holds with m_(i+1)(z) = r_(i+1), m_(i+1)(w) = Mu_i(w).
  At infinity: L|I_infinity is tame (character of order 2, p odd), so M_(i+1)|I_infinity = (+)_(s in S_i) L_psi(b_i s x) tensor (Wh_s tensor L_infinity): A_(i+1) = b_i S_i, ranks m_i(s). That is J3.
  J4: r_(i+2) = sum over S_(i+1) of m_(i+1) = d r_(i+1) + sum over Sigma_i of Mu_i = d r_(i+1) + sum over s in S_(i-1) of m_(i-1)(s) = d r_(i+1) + r_i (for i >= 2; and for i = 1 the sum over Sigma_1 is 1 = r_1). QED.

Coincidences among the points of Sigma_i themselves do not matter: the sets are sets, the functions add. The only coincidence that matters is a point of Sigma_i equal to a root, and that is the condition C_k. (CHECKED for bookkeeping with the script on Z of size 5 and random rational c.)

### Where the character is used
Only: chi != 1 at the roots (so that j_! = j_* when N_i is lisse at z, and L is ramified at z), tameness of chi (p odd), and chi tame at infinity (rank-one tame block). The value of chi^d at infinity is not used: a tame block at infinity of any character, even trivial, gives a block with a = 0. So I expect the induction not to need chi^d != 1 and not to need d odd (see part 8 for the checks I did not run).

## 5. The conclusion: one degree

**Theorem 2.** Under the hypotheses of Theorem 1 (C_k, h != 0, all c_i != 0, k = k-bar), H^m_c(A, P_k) = 0 for m != 0, and the dimension of H^0_c(A, P_k) = H^1_c(A, j_*M_k) is r_(k+1) - [k odd]. Hence the fibre cohomology H^j_c(A^k, F_h), which is H^(j-k)_c(A, P_k), is concentrated in the single degree j = k, for every h != 0.
Proof. P_k = j_*M_k[1], so H^m_c(A, P_k) = H^(m+1)_c(A, j_*M_k).
 m + 1 = 0: H^0_c(A, j_*M_k) = 0. A section of j_*M_k with proper (= finite) support is supported at finitely many points, and j_*M_k has no nonzero section supported at a point (it is the pushforward from the dense open U_k of a lisse sheaf, torsion free). [PROVED, standard.]
 m + 1 = 2: H^2_c(A, j_*M_k) = H^2_c(U_k, M_k) (the quotient j_*M/j_!M is punctual, and H^1_c, H^2_c of a punctual sheaf vanish in degree 2) = dual of H^0(U_k, M_k^dual)(1) (duality on curves). M_k^dual is irreducible, and not trivial: M_k is ramified at the roots (rank >= 1 with chi-monodromy), so it has no nonzero section: it is irreducible of rank r_k >= 1 and has no trivial constituent since it is ramified. So H^2_c = 0. [PROVED modulo the duality theorem on curves, a standard citation, to be opened by A6.]
 m + 1 < 0 or > 2: vanish (cohomological dimension 2 of a curve with the c-condition).
 Dimension: this is a computation. By Euler-Poincare (GOS, L10): chi_c(A, j_*M) = r (1 - |S|) + sum_(s in S) dim M^(I_s) - Sw_infinity(M) (tame at finite points). With M = M_k, S = S_k: = r_k - sum_(s in S_k) m_k(s) - Sw_infinity(M_k) = r_k - r_(k+1) - Sw_infinity, and Sw_infinity(M_k) = sum over a != 0 of rank W_a = r_k - n_0(P_k), n_0(P_k) = [0 in S_(k-1)] m_(k-1)(0) (for k = 1: n_0 = 1). Since 0 in S_(k-1) iff k - 1 is even, i.e. k odd, and m_(k-1)(0) = 1 (the rank-one block from the tame part of L at infinity is transported unchanged), dim H^1_c = r_(k+1) - [k odd].
 CHECKED by hand for k = 1 (d - 1 = dim H^1_c(A, j_!L), the Euler characteristic of A with j_!L: (1 - d) - 0 ... correct: Sw_infinity(L) = 0, chi_c = 1 - d) and k = 2 (d^2 + 1, a direct fibration count with generic rank d over x_2 and stalk rank d - 1 at x_2 = 0 gives the same Euler characteristic -(d^2 + 1)).
 **Predictions for A3 (exact tests):** the sum over F_(q^n) of t(x_1)...t(x_k) psi(h Q_c(x)) is, up to sign, a sum of exactly r_(k+1) - [k odd] n-th powers (when the Frobenius structure and k = F_q-bar with c, h, f defined over F_q, and the hypothesis holds over F-bar_q): k = 2 gives d^2 + 1, k = 3 gives d^3 + 2d - 1, k = 4 gives r_5 = d^4 + 3d^2 + 1 (r_5 = d r_4 + r_3 = d^4 + 2d^2 + d^2 + 1). Not run by me (see part 8).

## 6. Where the proof needs something I did not verify (honest list)

 1. Lemma T(c): compatibility of the summand decomposition of L7 with translation by s != 0 (used in Lemma A step 2). Standard; not opened. If one wanted to avoid it, translate the whole problem so that one point is at 0 and use L7 for each of the finitely many translates, but that is the same compatibility.
 2. L9 is used only in the tame case, via 2.5.3.1; the proof of 2.5.3.1 invokes 1.2.3.1 and 1.4.3.2 (iii) (transform of j_*K_chi), which I did not read; and the Gauss-sum twist is unramified so it does not affect anything above.
 3. L2 relies on BBD 4.3.1 (ii) (classification of simple perverse sheaves on a curve), quoted, not opened by me; A6 owns it.
 4. Duality on curves for H^2_c; Artin vanishing (H^m_c = 0 for m < 0 etc.): standard, A6.
 5. Base change to k = k-bar: the conclusion of Theorem 2 is a statement on dimensions over k-bar and so is insensitive to Frobenius; the descent to F_q (field growing with k) is S9/S10, not mine.
 6. I did NOT check the shift conventions of the identification H^j_c(A^k, F_h) = H^(j-k)_c(A, P_k); this is A4.
 7. The vanishing H^0_c(A, j_*M_k) = 0 and H^2_c: I use that M_k is not constant; this uses ramification at roots, which is part of the invariant, fine.

 8. The surjection pi_1(U_(i+1)) -> pi_1(A - Sigma_i) (removing points from a normal connected curve), used in Step 3: SGA 1 V 8.2, NOT OPENED by me (A6 owns it).
 9. Time: nothing here was run on the Frobenius side. The only computation is the bookkeeping script (indices, scalings, closed form, rank recursion), which cannot detect an error in the sheaf theory. The sign of rho_i was cross-checked by a hand computation of the stalk of Q_2 at w:
    Q_2(w) = sum_(x_1) t(x_1) G^(c_1 x_1 + c_2 w) with G^ = F(j_!L), which is singular exactly when the second factor's singular point 0' (argument zero) meets a root: x_1 = -c_2 w / c_1 = z, w = -(c_1/c_2) z = rho_2 z. (HINT-level, not a proof.)

## 7. Comparison with the draft (S5) and with report B (done AFTER the derivation above was written)

I then read S5, S3, S4, S7 to S9 of `../round3/PROOF_DRAFT.md` (lines 28-140) and all of report B up to its section 9. Result: **my derivation and report B reach the same invariant, the same sets, the same rank recursion, the same dimension formula and the same final step.** The differences, however small:

D1. **Sign and meaning of Laumon's integers (not an error in B, a trap in the notes).** Laumon's r(K), r_x(K), a_x(K) for perverse K = F[1] are Euler characteristics, so negative (2.2.1, p. 155; 2.2.1.1: a_x(K) <= r(K) - r_x(K) <= 0). B, the draft and I all use positive ranks; Laumon's printed 2.3.1.1 (i) "r(K') = sum deg(s) a_s(K) + r(F_]1,inf[) - s(F_]1,inf[)" and (ii), (iii) are correct in his sign convention but become: r(F') = sum m_s + (Sw - rank) of the part with slopes > 1, and stalk rank at s' = r(F') - (r(F_1) - Sw(F_1 tensor L(x.s'))). `LAUMON_NOTES.md` (main session) paraphrases (i) as "plus rank minus Swan of the part with slopes > 1" and (ii) as "r_s'(K') = r(K') + r(slope-1 part) - Swan(...)". Read with positive ranks these two have the wrong sign for the correction terms (for slopes > 1 and for the stalk). Harmless for the toy (no slope > 1; and one reads the stalk formula as a drop), but it is the kind of sign that breaks a rank count if someone reuses it. Same remark for 2.3.3.3 (p. 161), where "r(...)" of a module in degree -1 is minus its rank.
D2. **Notes item 1 ("a tame module at a finite point s contributes at infinity' L(s x') tensor tame of the same rank") is only right for local monodromy without invariants.** For j_*M[1] at a point with invariants the contribution has rank r - dim M^(I_s) = m(s), not r. This matters for the toy exactly at the point 0 in S_i (i even, i >= 2), where M_i has r_i - 1 invariants (for i = 2: d - 1) and the block has rank 1. With "same rank" the recursion would give r_3 = d^2 + d instead of d^2 + 1. B has the right rank (from GOS). My Lemma A step 1 to 4 is the clean proof.
D3. **B's sign inconsistency in section 3.2 is explained.** B wrote that his bookkeeping with 0 -> j_!F -> j_*F -> i_*W -> 0 gave r + m_s + Sw instead of r - m_s + Sw and fell back on the GOS dimension. The sheaf sequence is right but the perverse sequence has the opposite direction: 0 -> i_*W -> j_!F[1] -> j_*F[1] -> 0 (the cone of j_!F[1] -> j_*F[1] is i_*W[1]), so the skyscraper is a sub of j_!M[1] and the module for j_*M[1] is Theta_s / (m_0 copies of L(sx')), rank r - m_0 (Lemma A step 1, 4). Not a gap in B's proof (he used the dimension from GOS) but it is the missing consistency.
D4. **B uses wild statements of 2.4.3 where I use only the tame case.** B 3.2 invokes 2.4.3 (iii) b) (F^(inf,inf') vanishes on slopes <= 1) and 2.4.3 (ii) b) (F^(inf,0') kills slopes >= 1, with Swan s(V)) on modules that contain slope-1 blocks; those general statements are proved in the part of 2.5 (after 2.5.3) that I did not read and that may use more machinery. I replaced both by rank comparisons: (infinity, infinity') summand has rank 0 because the global rank formula 2.3.1.1 (i) leaves no room (Lemma A step 3); the module R^(-1)Phi at w is F^(inf,0') of the twisted module, whose slope >= 1 part has rank 0 because the tame summand already accounts for the total rank given by 2.3.2.3 (Lemma B). Consequence: the toy needs only the tame cases 2.5.3.1, proved on pp. 165-166 (read), plus the rank formulas 2.3.1.1, 2.3.2.3 (proved globally on pp. 158-160 by proper base change and GOS). This answers part of A2's question (2) from the A1 side; A2 must confirm the dependency list of 2.5.3.1 itself.
D5. **Statement of the invariant.** B and the draft separate A_i in k^* from T^0 (slope 0); I keep a = 0 among the frequencies (block L_psi(0 x) tensor W_0 = W_0), which makes Lemmas A, B uniform. Equivalent. B's (2) says "scalar -1" at roots, I write the scalar chi (the same for the quadratic character).
D6. **Type T3.** B proves "P_i is T3" by excluding T1 and T2 and using the trichotomy of Laumon 1.4.2 (BBD 4.3.1 (ii)); I verify Laumon's definition of T3 directly (irreducible, and not isomorphic to an Artin-Schreier sheaf because ramified at roots). Equivalent; B's exclusion "stalk at z is 0 but generic rank >= 1, so not lisse" is cleaner than "ramified at the roots" of the brief, and mine uses the same fact.
D7. **Translation to a finite singular point s != 0 (Lemma T(c)).** Laumon's 2.4.2.1 treats only the point 0 (and infinity); the passage to s != 0 is a twisting by L(s x') which commutes with nearby cycles because RPsi = RPhi here and it only sees the generic fibre. B writes "translation by s: L_psi(x + s, y) = L_psi(x,y) tensor L_psi(s,y)" and moves on; the draft says nothing. I state it as a lemma with a proof sketch and flag the compatibility as not opened (SGA 7 XIII). I consider this the only step of S5 that is not literally on a page of Laumon, and I do not think it can fail.
D8. **The condition (G_k).** The draft's (G_k) is for 2 <= i <= k-1; mine is 1 <= i <= k-1, the case i = 1 (Sigma_1 = {0} not in Z) being f(0) != 0. Same. The closed form and the lists of conditions for k <= 6 agree (B 3.3, 3.4; draft S3); I checked the closed form against the recursion up to i = 8 (script) and that the plain quadric first fails at i = 4 and c_1 = -c_2 at i = 2.
D9. **d odd is not needed (nor chi^d != 1).** Both B (point 5 of section 7) and I find that the induction uses only that L is tame (p odd), chi != 1 at the roots (for j_! = j_* when Q_i is lisse at z), and that L at infinity is tame (so tensoring with it preserves blocks). The brief's A3 asks about chi^d != 1: from the A1 side I see no use of it. This is reasoning, not a test; the draft's S11 (the lower bound) is where d odd enters.
D10. **Step 7 of the draft** ("M_k irreducible with inertia -1 at the roots, hence no coinvariants"): the inertia statement alone does not give no coinvariants; irreducibility and nonconstancy together do. B's version says that. Cosmetic.
D11. **Sufficient, not necessary.** Both B and I note the hypothesis is only sufficient. Exact condition at a point z in Z meeting Sigma_i: P_(i+1) is still a middle extension of an irreducible sheaf iff chi is not a constituent of the local monodromy of N_i at z (B 5(d) says j_! != j_* iff there is a (-1)-eigenvector); but the later steps then require the characters, which the invariant above does not track (so I do not claim anything there).
D12. **No error found in S5 or in B as far as the steps I re-derived go.** What I could not re-derive without something outside the pages I read: Lemma T(c) (D7), the classification BBD 4.3.1 (ii), SGA 1 V 8.2, duality on curves (items 3, 4, 8 of part 6).

## 8. Answers to the brief, in short

* **Invariant.** Theorem 1 (J1) to (J4): simple perverse of type T3, S_i = Z u Sigma_(i-1) (Sigma_1 = {0}, Sigma_i = rho_i S_(i-1)), tame local monodromy (scalar chi at the roots, rank m_i(w) = Mu_(i-1)(w) of nontrivial part at the other points), blocks L_psi(a x) tensor (tame) at infinity with a in {h c_(i-1) s : s in S_(i-1)} (rank m_(i-1)(s)), generic rank r_1 = 1, r_2 = d, r_(i+1) = d r_i + r_(i-1).
* **Scalings and signs.** Transform with parameter b = h c_i: F_b = [b]^*F; block frequency b s at infinity' from the singular point s; singular points at -a / b from the frequency a. With a = h c_(i-1) s the h cancels and the singular point is -(c_(i-1)/c_i) s = rho_i s.
* **Condition on c.** (G_k) = C_k: rho_i rho_(i-2) ... rho_m not in R' = {z'/z} for 2 <= m <= i <= k - 1, m = i mod 2 (and f(0) != 0). Independent of h. Finitely many proper conditions on the torus.
* **P_(i+1) is of type T3.** Theorem 1, steps 3 and 4.
* **Conclusion.** Theorem 2: H^m_c(A, P_k) = 0 for m != 0, of dimension r_(k+1) - [k odd] in degree 0.
* **What this does not prove.** The identification of the fibre cohomology with that of P_k (A4), the global argument (A4), the lower bound (A5) and the standard theorems (A6). The conclusion of Theorem 2 says nothing about zeros of anything; it is a statement about Weil's 1948 bound for y^2 = f(x) over finite fields.

## 9. Files

* `./round4/reports/A1-fourier-induction-rederived.md` (this file)
* `./round4/compute/A1/bookkeeping.py`, `bookkeeping_output.txt`
