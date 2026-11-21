# Report C: the smallest cases of Claim B, by hand (round three)

Character sums over finite fields; the bound at stake is Weil's theorem (1948). Nothing here concerns the Riemann
Hypothesis for the integers.

Notation as in BRIEF.md. T(w) = sum_y t(y) psi(w y) is the Fourier transform of t = chi(f); b_i = h c_i with h != 0;
d = deg f, Z = roots (|Z| = d, 0 not in Z), U = G_m minus Z. Let G_1 = R^1 FT(j_!L) as a sheaf (the brief's Q_1 is
G_1[1]). "Cited" results are used only as stated; I opened none of the primary sources in this report (all marked
NOT OPENED); I rely on the dumps' statements only through the brief.

Status: theory written first (this part), computations appended below as they finish.

## 0. Two facts used throughout (both elementary, no weights)

(F1) For every w, H^0_c(A^1, j_!L tensor L_psi(w y)) = 0 and H^2_c = 0, so the stalk of G_1 at w has dimension
-chi_c. PROVED: H^0_c vanishes because a compactly supported section of a lisse sheaf on a connected open of the affine
line vanishes. H^2_c is the coinvariants (twisted by -1) of the rank-one sheaf L tensor L_psi(w y) on A^1 minus Z, whose
inertia at a root acts by the quadratic character, so it is nontrivial: no trivial quotient.

(F2) (coinvariant lemma) If N is a lisse sheaf on A^1 minus a finite set containing Z, and inertia at some z in Z acts on
N with no eigenvalue 1 (for example as -1 times a unipotent), then H^2_c(A^1, j_! N) = N_{pi_1}(-1) = 0, because a
trivial quotient of N would restrict to a trivial quotient of the inertia module. PROVED (two lines).

## 1. k = 2

### 1.1 Q_1 = FT(j_! L)[1]

Stalk at w != 0: by (F1) and the Euler-Poincare formula (EP), chi_c(A^1, j_!L tensor L_psi(w y)) = (1 - d) - Sw_inf, and
Sw_inf(L tensor L_psi(w y)) = 1 because L is tame at infinity (rank one, slope 0) and L_psi(w y) has slope 1 for w != 0.
So dim = d. PROVED (EP is cited: Grothendieck-Ogg-Shafarevich, NOT OPENED, standard, its proof uses no weights).
Stalk at w = 0: H^1_c(A^1, j_!L) has dimension d - 1 (same EP with Sw = 0). PROVED.

Constant dimension d on G_m implies lisse on G_m: two independent justifications.
 (a) Deligne-Laumon (Laumon 1981, Asterisque 82-83, Thm 2.1.1, NOT OPENED): Sw_inf is constant in w on G_m and the
     finite singular points Z do not move, so j_!(L tensor L_psi(w y)) is universally locally acyclic over G_m; hence
     R pi_! is lisse there. CITED.
 (b) Laumon 1987 1.2.2.1, 1.3.2.3 (NOT OPENED): P_1 = j_!L[1] is irreducible perverse (rank one, ramified at the
     roots), so FT(P_1) is irreducible perverse, non-punctual, hence j_{!*} of a lisse sheaf M_1 on a dense open; the
     stalk of H^{-1} of a middle extension is the inertia invariants, which has the full dimension d at every w != 0,
     so there is no singular point in G_m. CITED.

So: generic rank d, lisse on G_m, stalk at 0 of dimension d - 1, singular at 0. Why 0 IS singular: stalk d - 1 < d. The
inertia at 0 acts on the rank-d generic stalk with exactly d - 1 invariants (if Q_1 = j_{!*}; by (b)).
Total Euler characteristic, PROVED elementarily by Fubini: H^*_c(A^2_{y,w}, j_!L(y) tensor L_psi(w y)) is the stalk of j_!L
at y = 0 placed in degree 2 (sum over w of psi(w y) is the delta at y = 0), so rank one in H^2_c. Leray over w gives
chi_c(A^1_w, G_1) = -1 (G_1 in degree one). Since chi_c(A^1, G_1) = chi_c(G_m, M_1) + (d - 1), we get chi_c(G_m, M_1) = -d,
so Sw_0(M_1) + Sw_inf(M_1) = d. PROVED. The splitting Sw_0 = 0, Sw_inf = d (d pieces L_psi(z w) tensor tame, z in Z, rank
one each) is Laumon's stationary phase (Laumon 1987, 2.3.3.1 and 2.5.3.1, NOT OPENED): CITED. The inertia at 0 on the
nontrivial one-dimensional piece is the quadratic character (local Fourier transform (inf, 0') of the tame character
chi_2 of P_1 at infinity: Laumon 2.5.3.1, CITED); for d = 1 this is checked below by an explicit formula.

### 1.2 H^j_c(A^2, F_h)

H^m_c(A^2, F_h) = H^{m-1}_c(A^1, G_2) with G_2 = j_!L tensor G_1(b_1 x) (Fubini over y, then the sheaf in x). Away from
0 and Z, G_2 is lisse of rank d with generic fibre M_2 = L tensor M_1(b_1 x); at z in Z the stalk is zero and the
inertia acts on M_2 by chi_2 times the identity, because M_1(b_1 x) is lisse at b_1 z != 0 (here we use that Q_1 is lisse on
G_m). At 0 the stalk of G_2 has dimension d - 1 (stalk of G_1 at 0; L is lisse at 0 because f(0) != 0).

 * H^3_c(A^2, F_h) = H^2_c(A^1, G_2) = coinvariants of M_2 = 0 by (F2). PROVED, for EVERY c_1 != 0 and h != 0. (The
   difference between G_2 and j_!M_2 is punctual at 0, and H^1_c(punctual) = 0, so H^2_c agree.)
 * H^4_c = H^3_c(curve) = 0, H^1_c = H^0_c(A^1, G_2) = 0 (no punctual sections: G_2 injects into j_* j^* at 0 because
   the stalk of G_1 at 0 injects into the generic stalk, perversity of FT, CITED; also the brief's RED report gives
   cohomology in degrees k, k+1 only).
 * H^2_c(A^2, F_h) = H^1_c(A^1, G_2) of dimension -chi_c(A^1, G_2).

Euler characteristic: U_2 = G_m minus Z, chi(U_2) = -d. Swan at infinity of M_2: M_1(b_1 x) tensor L at infinity is
sum_z L_psi(b_1 z x) tensor tame (stationary phase, CITED), so Sw_inf = d, Sw at 0 and at Z is 0 (tame). So
chi_c(U_2, M_2) = d(-d) - d = -d^2 - d, plus the stalk at 0, d - 1: chi_c(A^1, G_2) = -d^2 - 1.

**dim H^2_c(A^2, F_h) = d^2 + 1** for every c_1 != 0 and h != 0 (modulo the cited Swan splitting; checked for d = 1,
2 below). Cohomology concentrated in degree 2.

## 2. k = 3

### 2.1 The sheaf P_2, the transform FT(P_2), its stalks

P_2 (the brief's) is the perverse sheaf of G_2: middle extension of M_2 on U_2 (stalk d - 1 at 0, zero at Z). Its
finite singular set is Z union {0} (at z: inertia chi_2 times identity, no invariants; at 0: Q_1's inertia). At infinity,
P_2 is sum_{z in Z} L_psi(b_1 z y) tensor (tame, rank one) (CITED stationary phase).

The stalk of Q_2 = FT_{b_2}(P_2) at w is H^1_c(A^1, G_2 tensor L_psi(b_2 w y)) (H^0_c = 0 as above; H^2_c = 0 by (F2),
since L_psi is lisse at roots, for EVERY w including 0). So dim = -chi_c:

 chi_c = d(-d) - Sw_inf(P_2 tensor L_psi(b_2 w y)) + (d - 1).

Frequencies of P_2 at infinity are b_1 z (z in Z, distinct). Twisting by L_psi(b_2 w y) leaves slope 1 unless
b_1 z + b_2 w = 0, i.e. w = -(c_1/c_2) z, in which case that one rank-one piece becomes tame. Hence

 * w not in -(c_1/c_2) Z (including w = 0): Sw_inf = d, stalk dimension d^2 + 1;
 * w = -(c_1/c_2) z (z in Z; distinct z give distinct w): Sw_inf = d - 1, stalk dimension d^2.

So Q_2 has generic rank d^2 + 1, and the stalk drops by exactly one at each point of Sigma_2 = -(c_1/c_2) Z. Q_2 is
NOT lisse there (stalk < generic rank, and a lisse sheaf has constant rank). Everywhere else it is lisse (constant stalk
dimension and constant Swan: Deligne-Laumon again; or: stalk of the sheaf (no punctual part, FT of perverse is
perverse) injects into the inertia invariants of the generic stalk, which has dimension d^2 + 1 = generic rank, so
inertia acts trivially). In particular 0 is NOT a singular point of Q_2 (P_2 has no frequency 0 and no slope < 1 at
infinity), and the singular set does not depend on h. PROVED modulo the cited stationary phase for the list of
frequencies of P_2 (and verified in item 4 below that this input can be replaced by Fourier inversion).

### 2.2 H^j_c(A^3, F_h): the center-variable form (no Q_2 needed)

Sum over x_1 and x_3 separately: S_h = sum_x t(x) T(b_1 x) T(b_2 x). Sheaf-theoretically (Fubini twice, Kunneth for the
two independent sums) H^m_c(A^3, F_h) = H^{m-2}_c(A^1_x, G_3), G_3 = j_!L tensor G_1(b_1 x) tensor G_1(b_2 x). On
U = G_m minus Z, G_3 is lisse with fibre M_3 = L tensor M_1(b_1 x) tensor M_1(b_2 x), rank d^2, inertia at each root z
= chi_2 times identity (both M_1(b_i x) lisse at z since b_i z != 0). The stalk of G_3 at 0 is (d-1)^2 (note: it
is smaller than the invariants of M_3 at 0; G_3 is not a middle extension at 0, which does not matter below).

 * H^4_c(A^3, F_h) = H^2_c(A^1, G_3) = H^2_c(U, M_3) (the difference is punctual at 0) = coinvariants of M_3 = 0 by
   (F2). **PROVED for every c_1, c_2 != 0 and every h != 0.** No hypothesis on the ratio c_1/c_2. Also H^0_c = 0,
   H^1_c = H^0_c = 0, H^5_c = H^6_c = 0 (curve), so the fibre cohomology is concentrated in degree 3 for all c.
 * dim H^3_c(A^3, F_h) = -chi_c(A^1, G_3) = d^3 + 2d - 1 - m, computed in 5 below.

### 2.3 The same through P_3 = j_!L tensor Q_2 (the brief's route)

Q_2 has generic rank d^2 + 1, and (stationary phase, CITED) at infinity it is sum_{z in Z} L_psi(b_2 z w) tensor (tame
of rank d) plus one tame piece (from the point 0 of P_2). The coinvariants of L tensor (generic Q_2) on A^1 minus
(Z union Sigma_2) are again zero, by (F2), as follows.
 * If z in Z is not in Sigma_2 (generic ratio): Q_2 is lisse at z, inertia = chi_2 times identity.
 * If z in Z cap Sigma_2 (i.e. -(c_1/c_2) z' = z for some root z'): Q_2 has stalk d^2 against generic rank d^2 + 1 at z; the
   extra vanishing cycle is rank one, with the tame character of the cancelled piece of P_2 at infinity, which is
   chi_2 (from L at infinity, d odd) times the tame character at infinity of the corresponding piece of Q_1, namely
   chi_2 (local Fourier transform (z', inf') of chi_2, Laumon 2.5.3.1, CITED): trivial. So the local monodromy of Q_2 at
   z is unipotent, inertia on L tensor Q_2 is -1 times unipotent, no eigenvalue 1, and (F2) applies. (For d = 1 this
   is the Bessel sum sum_y chi(y(y-a)) psi(s y) at s = 0, where the stalk is -1: shown below.)
So the brief's hypothesis Z cap Sigma_2 = empty is not needed for the vanishing of H^{k+1} at k = 3; it is needed only for
the specific proof of irreducibility in step 3 of Claim B. Both routes agree: H^4_c = 0.

### 2.4 For which ratios c_1/c_2 does the argument work, what happens for the others?

Let lambda = -c_1/c_2 and m = |Z cap lambda Z| (number of roots z with lambda z in Z).
 * Vanishing of H^4_c (hence the statement P_3^c): works for ALL ratios and all h != 0 (2.2).
 * Generic ratio (m = 0): Q_2 has singular set exactly lambda Z disjoint from Z; P_3 is the middle extension of an
   irreducible lisse sheaf if M_2 is irreducible; dim H^3_c = d^3 + 2d - 1.
 * m > 0 (lambda in R'): Z and Sigma_2 meet in m points. The Swan conductor of the twist drops at the same time
   at m pairs, the Euler characteristic changes by +m (dim H^3_c = d^3 + 2d - 1 - m), and step 3 of Claim B (lisse at roots)
   is not available as stated; the vanishing still holds by 2.2.
 * m = d (lambda Z = Z; this is exactly "f(x) f(lambda x) is a square (lambda = -c_1/c_2, up to the choice of side)" of round one, because for f
   squarefree of odd degree f(x) f(mu x) is a square iff mu Z = Z): dim = d^3 + d - 1. The fibre is still concentrated in
   degree 3. Whatever fails for the QUADRIC in round one at c_1 = -c_2 is therefore not a failure of (P_3^c) in the sense
   of the fibre H^4; it lives in the other terms of the exact sequence (T and H^{k-1}_c(Y, K)), see the computed
   example d = 1 below where the fibre dimension drops from 2 to 1 at c_1 = -c_2 while remaining in degree 3.

## 3. Question 3: the two statements

 * "The finite singular set of Q_2 is -(c_1/c_2) Z, independent of h": TRUE (2.1), as the set of points where Q_2 is not
   lisse, for every c_1, c_2 != 0 and every h != 0. PROVED modulo (i) stationary phase for the frequencies of P_2 at
   infinity (CITED, or replaced by Fourier inversion, item 4), (ii) Deligne-Laumon or perversity for lissity off
   Sigma_2. The jump of the stalk dimension (d^2 + 1 to d^2) is itself exact Euler-Poincare data and shows the points of
   Sigma_2 are singular without using any local Fourier transform. The set can meet Z (then lambda in R'); the claim is a
   statement about Q_2 and is true in that case too.
 * "0 is a singular point of Q_1 but not of Q_2": TRUE. Q_1: stalk d - 1 at 0 against generic rank d. Q_2: stalk d^2 + 1
   at 0 = generic rank, and nothing cancels because P_2 has no frequency 0 and no slope < 1 at infinity. PROVED modulo the
   same citations. (0 reappears as a singular point of Q_3, because 0 is a singular point of P_2.)

## 4. The semicontinuity route (Question 4)

Statement (Deligne conjecture, proved by Laumon 1981, Asterisque 82-83, Thm 2.1.1; NOT OPENED, I state it from
memory of its role): let X -> S be a smooth curve over a normal base, D a closed subscheme finite etale over S, F a lisse
sheaf on X - D. If the Swan conductors of F at the points of D are locally constant on S, then j_! F is universally locally
acyclic relative to S (after the usual compatibility at the boundary).

Application. S = A^1_w, X = P^1_y, D = (Z-type finite singular points of P) union {infinity}, all constant sections. The
sheaf is P tensor L_psi(b w y) (extended by zero at infinity). At finite points of P the twist by L_psi(b w y) is
lisse, so the Swan conductor at those points is the one of P, constant in w. At infinity the Swan conductor is
Sw_inf(P tensor L_psi(b w y)). If it is locally constant at w_0 then j_!(...) is ULA over a neighbourhood of w_0; with
proper base change R pr_! commutes with base change, the cohomology sheaves R^i pr_! are lisse near w_0 (in our case
only R^1 is nonzero, with constant rank by Euler-Poincare). CITED. Conclusion: Sing(Q) is contained in the finite set
J(P)/b of w where w -> Sw_inf(P tensor L_psi(b w y)) is not locally constant. Conversely, if the stalk dimension at w_0 is
below the generic rank (EP plus vanishing of H^0_c, H^2_c as in F1, F2), w_0 is singular. So for these
sheaves the singular set of Q_i is exactly J(P_i)/b_i (PROVED given Deligne-Laumon).

Is this enough, "given only the slopes and frequencies of P_i at infinity"? Yes for the inclusion Sing(Q_i) in Sigma_i, if
the information is stated in the right form. J(P_i) is the set of c for which twisting by L_psi(c y) changes the Swan
conductor at infinity: this is exactly the set of "critical frequencies" of the slope-1 part (the a with V_1 tensor
L_psi(a y) of slope < 1), together with c = 0 when slopes < 1 are present. A tame twist (the factor L in P_i = L tensor Q_{i-1})
does not change J. So Sing(Q_i) in b_i^{-1}(-J(Q_{i-1})). Nothing more than J(Q_{i-1}) is needed: slopes > 1 do not
contribute, and multiplicities do not matter.

Minimal input on P_i at infinity: the finite SET J(Q_{i-1}) of critical frequencies. Can it be obtained without
stationary phase? Yes, from Fourier inversion plus EP, as follows. Q_{i-1} = FT_{b_{i-1}}(P_{i-1}), and
FT(FT(P)) = P(-y)(-1)[-1] (Laumon 1.2.2.1, CITED; its proof is a Fubini/Kunneth computation of H^*_c(A^2, L_psi(w(y + y'))),
no weights). So the stalk of P_{i-1} at s is H^1_c(A^1, Q_{i-1} tensor L_psi(-b_{i-1} s w)) up to the reflection. By EP on
A^1 the finite-point contributions of Q_{i-1} do not depend on the twist, so

 dim (stalk of P_{i-1} at s) = const + Sw_inf(Q_{i-1} tensor L_psi(-b_{i-1} s w)),

provided H^0_c = H^2_c = 0 for these twists (H^0_c: no punctual sections; H^2_c: Q_{i-1} has no quotient L_psi(.), true
if Q_{i-1} is irreducible of rank > 1). Hence J(Q_{i-1}) is contained in {b_{i-1} s : P_{i-1} has stalk dimension different
from its generic rank at s}, i.e. in b_{i-1} Sing(P_{i-1}) when P_{i-1} is a middle extension (stalk = inertia
invariants). With Sing(P_{i-1}) in Z union Sigma_{i-2} (induction; P_i = L tensor Q_{i-1} is singular at most on Z union Sing(Q_{i-1})):

 Sing(Q_i) in { w : b_i w + b_{i-1} s = 0, s in Z union Sigma_{i-2} } = rho_i (Z union Sigma_{i-2}), rho_i = -c_{i-1}/c_i,

with h cancelled. This is exactly Sigma_i of the brief. So the inclusion in step 4 of Claim B follows from three
inputs: Deligne-Laumon (semicontinuity), Fourier inversion (only as the identity of stalk dimensions), and EP. It does
not need the stationary phase decomposition (L_psi(s y) tensor tame for each s), and it does not need to know the tame
parts. What it does need: (a) irreducibility (or at least "no punctual sections, no rank-one L_psi quotient") of the Q_j
at each step, which Claim B has from FT being an equivalence of perverse sheaves (CITED), and (b) that the induction
starts: P_1 = j_!L with Sing = Z, and the case s = 0 (c = 0 enters J if Q has slopes < 1 or frequency 0) is covered
because "slope < 1 present" is the same as "0 is a jump of Sw under twist", i.e. P_{i-1} is singular at 0.

One caution: the inversion identity gives the stalk dimension of P_{i-1} at s for P_{i-1} = FT(Q_{i-2}) viewed with the
twist L; I use P_{i-1} = L tensor Q_{i-2} only through "Sing(P_{i-1}) in Z union Sing(Q_{i-2})". That is where the
roots enter and where the extension by zero of L has stalk zero, so the statement is about the perverse sheaf, not about
Q alone. HINT: the argument is the "global shadow" of stationary phase; it is not an independent proof of the local
structure (the characters of inertia and the ranks of the pieces still need Laumon's local transforms).

## 5. Dimensions of the fibre cohomology (Question 5)

All for h != 0, c_i != 0. Notation lambda = -c_1/c_2, m = |{z in Z : lambda z in Z}| = |Z cap lambda^{-1} Z|.

 * D_2 = dim H^2_c(A^2, F_h) = d^2 + 1 (H^3_c = 0). Independent of c_1 and h. d = 1: D_2 = 2.
 * D_3 = dim H^3_c(A^3, F_h) = d^3 + 2d - 1 - m (H^4_c = 0), with m the number of pairs (z, z') in Z^2 with c_1 z + c_2 z' = 0,
   i.e. the number of cancellations of frequencies at infinity of M_1(b_1 x) tensor M_1(b_2 x). Derivation: rank d^2 on
   U (chi(U) = -d), Sw_inf = d^2 - m (the d^2 pieces L_psi((b_1 z + b_2 z')x) tensor tame, Swan 1 unless b_1 z + b_2 z' = 0),
   stalk (d-1)^2 at 0: chi_c = -d^3 - (d^2 - m) + (d-1)^2 = -(d^3 + 2d - 1 - m). Generic ratio (m = 0): d^3 + 2d - 1;
   m = d (lambda Z = Z): d^3 + d - 1. The same number comes out of the iterated route (2.3): chi_c(A^1, j_!L tensor Q_2) =
   (d^2 + 1)(1 - 2d + m) - d^2 + (d - m) d^2 = 1 - 2d - d^3 + m.
 * d = 1 (f = x - a): D_2 = 2, D_3 = 2 (c_1 != -c_2) or 1 (c_1 = -c_2). Explicit check: with g = sum_u chi(u) psi(u),
   T(w) = g chi(w) psi(a w) for w != 0 and T(0) = 0, so S_2 = g chi(b_1) sum_x chi(x(x - a)) psi(a b_1 x)
   (a Salie/Bessel type sum of rank 2: weight-one pair) and
   S_3 = chi(b_1 b_2) g^2 [ sum_{x != 0} chi(x - a) psi(a (b_1 + b_2) x) ], which for b_1 + b_2 != 0 is chi(...) g^2 [ g' psi chi(.)  - chi(-a) ],
   two terms (sizes q^{3/2} and q), and for b_1 + b_2 = 0 is -chi(-a b_1 b_2) g^2, ONE term (size q); by Hasse-Davenport
   S_3 over F_{q^n} is -beta^n, beta = chi(-a b_1 b_2) g^2. This is the case c_1 = -c_2. PROVED (elementary Gauss sums). The
   cohomology in that case is still in degree 3 of dimension 1: a direct change of variables u = x_1 - x_3 shows
   it (PROVED): the sheaf R pr_!(chi(x_3 - a) chi(x_3 + u - a)) on the u-line has R^1 = Q_l (constant, rank 1) and
   R^2 = delta_0(-1); the delta_0 part contributes H^*_c(A^1, j_!L) = 0, and the constant part contributes
   H^*_c(A^2_{x_2,u}, chi(x_2 - a) psi(b x_2 u)) = stalk of j_!L at x_2 = 0 in degree 2 (rank one). So H^3_c has dimension 1 and
   everything else vanishes: consistent with D_3 = d^3 + d - 1 = 1 for d = 1, m = 1.

## 6. Exact computations (CHECKED)

Script: compute/C/fsum.py (Python 3.14, integer arithmetic only: finite fields F_{p^n} built from a primitive
polynomial with exp/log tables, sums as elements of the group ring Z[Z/p] reduced to Z[zeta_p], additive-character
transform as an exact p-ary transform on group-ring vectors, Newton identities with Fractions in Q(zeta_p)). The k = 3
sum is computed in the center form S_h = sum_x t(x) T(b_1 x) T(b_2 x); the code compares it with the brute-force triple
sum over x_1, x_2, x_3 at n = 1, 2 (all "brute check: OK"). The check is: the sequence S_n (n = 1..N) is the n-th power sum
(sign +1 for k = 2, -1 for k = 3) of D numbers: all elementary symmetric polynomials e_{D+1}, ..., e_N vanish and e_D != 0.
Output files in compute/C/out/. (The interpretation of the e_k as "eigenvalues of Frobenius on H^{k or k+1}" is from the
trace formula and uses no weights; but the number of eigenvalues counted here is the net count in the alternating sum:
it can only fall below the true dimension if there are cancellations between H^k and H^{k+1}, and the pattern of exact
dimensions is the one predicted by Euler-Poincare, which supports no cancellation.)

| d | f over F_p | k | c | p | N (max n) | D observed | D predicted | file |
|---|---|---|---|---|---|---|---|---|
| 1 | x - 1 | 2 | (1), h=1 | 3 | 5 | 2 | d^2+1 = 2 | d1_k2_p3_h1.txt |
| 1 | x - 1 | 2 | (1), h=1,2 | 5 | 5 | 2, 2 | 2 | d1_k2_p5_h1.txt, d1_k2_p5_h2.txt |
| 2 | x^2 - 1 | 2 | (1), h=1 | 3 | 10 | 5 | 5 | d2_k2_p3.txt |
| 3 | x^3 - x + 1 | 2 | (1), h=1 | 3 | 13 | 10 (e_11 = e_12 = e_13 = 0) | 10 | d3_k2_p3.txt |
| 1 | x - 1 | 3 | (1,1), h=1; lambda = -1, m = 0 | 3 | 6 | 2 | 2 | d1_k3_p3_c11.txt |
| 1 | x - 1 | 3 | (1,2), h=1; lambda = 1, m = 1 | 3 | 6 | 1 | 1 | d1_k3_p3_c12.txt |
| 1 | x - 1 | 3 | (1,1), h=1; m = 0 | 5 | 5 | 2 | 2 | d1_k3_p5_c11.txt |
| 1 | x - 1 | 3 | (1,4), h=1; lambda = 1, m = 1 | 5 | 5 | 1 | 1 | d1_k3_p5_c14.txt |
| 1 | x - 1 | 3 | (1,2), h=3; lambda = 2, m = 0 | 5 | 5 | 2 | 2 | d1_k3_p5_c12_h3.txt |
| 2 | x^2 - 1 | 3 | (1,1), h=1; lambda = -1, m = 2 | 3 | 12 | 9 (e_10..e_12 = 0) | d^3+2d-1-m = 9 | d2_k3_p3_c11.txt |
| 2 | x^2 - 1 | 3 | (1,2), h=2; lambda = 1, m = 2 | 3 | 12 | 9 | 9 | d2_k3_p3_c12_h2.txt |

All eleven rows agree with the prediction, including the m-dependence (d = 1: 2 versus 1; d = 2 with m = 2: 9 rather than
11). The dependence on h (h = 1, 2 and 3) and on c_1, c_2 other than through m is absent, as predicted. Not tested: d = 2
with m = 0 or 1 at k = 3 (needs p >= 5 and n >= 13, too large for the machine rules), d = 3 at k = 3 (needs n >= 33).
Weights were not used anywhere to produce the numbers; I did not compute absolute values.

Note on the first run (d=1, k=2, p=3): output was
"S_1 = -1 + zeta, S_2 = 15 zeta, S_3 = -24 - 48 zeta, S_4 = -63 - 63 zeta, S_5 = 558 + 279 zeta, e_k nonzero for k in [1,2]". 

## 7. What I found about Claim B (and Claim A's input)

 1. PROVED for k = 2 and k = 3: H^{k+1}_c(A^k, F_h) = 0 for all c_i != 0 and all h != 0, with no condition on the ratios,
    using only (F2) and that Q_1 is lisse on G_m. So (P_2^c) and (P_3^c) hold for every c, not just outside the hypersurfaces
    of Claim B. The hypothesis "Z cap Sigma_i = empty" of Claim B is therefore sufficient but not necessary for this
    conclusion at k <= 3.
 2. The obstruction to vanishing of H^{k+1} is of a different, more local type than the one in Claim B: it needs a
    root z of f at which the local monodromy of Q_{k-1} has the quadratic character as an eigenvalue (so that L tensor Q
    has an invariant vector). Tracking the tame characters in the local Fourier transform (CITED, HINT) shows that the
    singular points of Q_2 and Q_3 have unipotent monodromy (the characters chi_2 from L at infinity and chi_2 from the
    local transform cancel) so the first place where a trivial constituent can appear is Q_4 at a point of rho_4 Sigma_2 that
    is also a root, i.e. k = 5 and rho_4 rho_2 in R'. This is a hint that Claim B's hypothesis becomes relevant, in the
    form "Z cap Sigma_i with a chi_2-type character", only at k >= 5; and that for k = 4 the center-variable form
    S = sum_{x_3} t(x_3) T(b_3 x_3) Q_2(x_3) gives H^5 = 0 for every c as well (HINT, not proved here: requires the
    unipotence of Q_2 at the points of Sigma_2 meeting Z).
 3. Step 3 of Claim B ("at a root where Q_i is lisse the monodromy of L tensor Q_i is -1 times the identity, so j_! = j_*") is
    correct but stronger than needed: what is needed is that the inertia has no eigenvalue 1 on L tensor Q_i at z.
 4. Step 4 (the inclusion Sing(Q_i) in Sigma_i): replaceable by Deligne-Laumon + Fourier inversion + EP (section 4), so
    stationary phase is not needed for the location of singularities, but is still needed for local data (characters,
    ranks of the pieces) wherever those are used.
 5. I found no error in steps 1, 2, 5. At k = 2 and 3 the computed dimensions agree with the whole picture (rank d^2+1
    of Q_2 with the drop at -(c_1/c_2)Z).
 6. NOT decided: whether M_k (or M_2, M_3) is irreducible in the bad-ratio case. It is not needed for H^{k+1} = 0 at
    k = 2, 3. What would decide it: the structure of the monodromy group of M_1, in particular that M_1 is not induced
    and has no nontrivial self-tensor decomposition; the exact sequence for H^1_c(A^1, G_3) is not needed.
 7. For Claim A: the input (P_k^c) at k = 2, 3 now has a proof (above), with the single non-elementary input "Q_1 is lisse on
    G_m", which holds by Deligne-Laumon or by FT preserving irreducibility.


