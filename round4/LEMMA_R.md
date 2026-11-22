# Lemma R: the local structure of the transform, from rank counts alone

Main session, 2026-11-22. Subject: sheaves on the affine line over a finite field, for the toy case (Weil's 1948
bound for y^2 = f(x)). Nothing here says anything about the Riemann Hypothesis for the integers.

Status: PROVED by the main session modulo the cited statements R1 to R5 below. Refereed by one agent
(`reports/C1-lemma-R-referee.md`, 2026-11-22): holds as written, no fatal or repairable defect, ten cosmetic
points, all entered below. Not refereed by a mathematician. Not a theorem.

## Why this file exists

`PROOF_V2.md` S5 proves the induction step through two lemmas (A and B) that use Laumon's vanishing-cycle
statements 2.3.2.1 and 2.3.3.1, the local-global comparison 2.4.2.1, the tame local transforms 2.5.3.1, and a
translation compatibility ("Lemma T(c)", register item C-15) that nobody read at a source. The referee (B2, item
E1) found that 2.4.2.1 is stated on the page only at the origins, so the translation is really needed there.

Lemma R reaches the same conclusions with none of those. It uses only the Euler-Poincare formula on the line,
the behaviour of Swan conductors under a twist by an Artin-Schreier sheaf, and the fact that the transform is an
involutive equivalence that preserves simple perverse sheaves of type T3. Removed from the dependency list of S5:
Laumon 2.3.2.1, 2.3.2.3, 2.3.3.1, 2.4.2.1 to 2.4.3, 2.5.3.1; Lemma T(c) (C-15); SGA 7 XIII 2.1.7.1 and Th.
finitude 2.16 (C-14) as far as S5 is concerned; the exactness remark E4; Gabber-Katz stays unused.

## Inputs (each read on the page image by the main session; statements in my words)

- **R1.** Laumon 2.2.1, journal p. 155 (definitions). For a sheaf F on a smooth curve and a closed point x: generic
  rank r(F), rank of the stalk r_x(F), Swan conductor s_x(F), total drop a_x(F) = r(F) + s_x(F) - r_x(F). They
  extend to complexes by additivity. So for K = (j_*M)[1], M lisse of rank r on a dense open: r(K) = -r,
  r_x(K) = -dim M^(I_x), a_x(K) = -(r - dim M^(I_x) + Sw_x(M)). Write art_x(M) = r - dim M^(I_x) + Sw_x(M) >= 0.
- **R2.** Grothendieck-Ogg-Shafarevich, Laumon 2.2.1.2, journal p. 156: on a smooth projective curve,
  chi(K) = chi(curve) r(K) - sum over closed points of deg(x) a_x(K), for every K in D^b_c (not only perverse
  ones; Step 0 applies it to a sheaf). Statement read. Its proof (Raynaud; SGA 5 X) was read by nobody in this
  project.
- **R3.** Laumon 2.1.2.7 with its proof, journal p. 153, and 2.1.2.8, 2.1.3, 2.1.4, journal p. 154. Break (slope)
  decomposition V = sum of V_lambda, exact and compatible with sub-quotients; Sw(V) = sum of lambda r(V_lambda);
  tame means slope 0 means Swan 0. For L of rank one with Swan conductor one and W a simple module over the wild
  inertia group P, of slope lambda ("constituent" below always means a simple P-constituent):
  W tensor L has slope max(1, lambda) if lambda != 1, and slope <= 1 if lambda = 1. Hence
  Sw(V tensor L) = r(V_[0,1[) + Sw(V_1 tensor L) + Sw(V_]1,inf[) and Sw(V_1 tensor L) <= r(V_1). The Artin-Schreier
  module L_psi(a x) at infinity (a != 0) has rank one and Swan conductor one; its dual is L_psi(-a x).
- **R4.** The rank of the stalk of F(K) at s' (an Euler characteristic) is minus the Euler characteristic with
  compact supports of K tensor L_psi(x s') on the line. This is the first line of the proof of Laumon 2.3.1.1,
  journal p. 158; it comes from the definition of F and proper base change (register C-2). Only this
  Euler-characteristic form is used below.
- **R5.** Laumon 1.2.2.1, journal p. 141 (involutivity: F'(F(K)) = a^*K(-1), where a is x -> -x and F' is the
  transform from the dual line back, built with the same psi; read on the page by A2 and by the referee C1, not
  by me), 1.3.2.3, 1.3.2.4, journal p. 147, and 1.4.2.1, journal p. 149. F is an equivalence on perverse sheaves
  on the line; it sends simple objects to simple objects; a simple perverse sheaf of type T3 goes to one of type
  T3', which has the form (j'_*N)[1] with N irreducible lisse on a dense open. Here j_* is the ordinary
  pushforward, which on a curve is the middle extension (BBD 2.1.11, not opened).

All of R1 to R5 are statements of chapters 1 and 2 before section 2.3.2. On the pages read by A2, by C1 and by me
(journal pp. 141 to 143, 147, 149, 150, 152 to 156, 158, 159) none of their proofs uses weights or purity. That
claim does not cover what those proofs cite and nobody opened: the proof of R2, BBD 4.1.1, 4.1.2, 4.2.5, 4.3.1,
and Serre and Katz for the break decomposition.

## Statement

Let k be algebraically closed of characteristic p, l != p. Let P = (j_*M)[1] be a simple perverse sheaf of type T3
on the line A, with M irreducible lisse of rank r on A - S, S finite, M not lisse at any point of S. Assume

- (H1) M is tame at every point of S;
- (H2) at infinity, M is isomorphic to the direct sum, over a in a finite set Freq of k, of L_psi(a x) tensor W_a,
  with W_a tame of rank n_a >= 1.

Put m(s) = r - dim M^(I_s) for s in S and m(s) = 0 otherwise. Let F(P) = (j'_*N)[1] (R5). Then:

1. rank N = sum over s in S of m(s).
2. N is lisse exactly outside {-a : a in Freq}; at w = -a, rank N - dim N^(I_w) = n_a.
3. N is tame at every finite point.
4. At infinity', N is isomorphic to the direct sum over s in S of L_psi(s x') tensor W'_s, with W'_s tame of rank
   m(s).

## Proof

**Step 0, the stalk formula.** For every s' in k, R4 gives the rank of the stalk of F(P) at s' as minus the
Euler characteristic with compact supports of (j_*M)[1] tensor L_psi(x s'). Since F(P) = (j'_*N)[1], that rank
is -dim N^(I_s') (the stalk of j'_*N, shifted). Apply R2 on the projective line to the extension by zero of
j_*M tensor L_psi(x s'): the total drop is art_s(M) at s in S (the twist is lisse there), r + Sw_inf(M tensor
L_psi(x s')) at infinity, and zero elsewhere. So

    (E)   dim N^(I_s') = sum over s in S of art_s(M) + Sw_inf(M tensor L_psi(x s')) - r.

**Step 1, forward.** By (H2), M tensor L_psi(x s') at infinity is the sum of L_psi((a + s') x) tensor W_a. By R3 a
block with a + s' != 0 has Swan conductor n_a and the block with a + s' = 0 is tame. So
Sw_inf(M tensor L_psi(x s')) = r - n_(-s'), with n_b = 0 when b is not in Freq (r = sum of the n_a). By (H1),
art_s(M) = m(s). Then (E) reads dim N^(I_s') = sum of m(s) - n_(-s'). N is lisse on a dense open, and there the
left side is rank N; so rank N = sum of m(s), which is (1). (In particular S is not empty.) At every s' outside
-Freq the stalk of j'_*N has full
dimension, so inertia acts trivially and N is lisse there; at w = -a the dimension drops by n_a >= 1. This is (2).

**Step 2, back.** By R5, F'(F(P)) is a^*P(-1) = (j_* a^*M)[1](-1). F' is the same construction, so (E) holds for
the pair (F(P), F'(F(P))): for every sigma in k,

    (E')  dim M^(I_(-sigma)) = sum over w of art_w(N) + Sw_inf'(N tensor L_psi(x' sigma)) - rank N,

with dim M^(I_(-sigma)) = r - m(-sigma), and art_w(N) = n_a + Sw_w(N) at w = -a by (2). Let V' be N at infinity',
with slope parts V'_<1, V'_1, V'_>1. By R3, for sigma != 0,
Sw(V' tensor L_psi(x' sigma)) = r(V'_<1) + Sw(V'_1 tensor L_psi(x' sigma)) + Sw(V'_>1), and for sigma = 0 it is
Sw(V'_<1) + r(V'_1) + Sw(V'_>1).

For all but finitely many sigma, m(-sigma) = 0 and V'_1 tensor L_psi(x' sigma) has all slopes equal to 1 (a simple
constituent W of V'_1 can become of slope < 1 for at most one sigma: if W tensor L_psi(x' sigma) has slope < 1
then W tensor L_psi(x' tau) = (W tensor L_psi(x' sigma)) tensor L_psi(x' (tau - sigma)) has slope 1 for
tau != sigma, by R3). For such sigma, (E') gives

    r = sum of n_a + sum over w of Sw_w(N) + r(V'_<1) + r(V'_1) + Sw(V'_>1) - rank N
      = r + sum over w of Sw_w(N) + (Sw(V'_>1) - r(V'_>1)).

Both extra terms are >= 0, and Sw(V'_>1) > r(V'_>1) unless V'_>1 = 0. Hence Sw_w(N) = 0 for every finite w, which
is (3), and V'_>1 = 0.

**Step 3, the blocks.** Subtracting the generic case from (E') at a given sigma:

    m(-sigma) = r(V'_1) - Sw(V'_1 tensor L_psi(x' sigma))   for sigma != 0,
    m(0)      = r(V'_<1) - Sw(V'_<1).

For sigma != 0 let V'_(1,sigma) be the submodule of V'_1 for which V'_(1,sigma) tensor L_psi(x' sigma) is the
part of slope < 1 of V'_1 tensor L_psi(x' sigma). The rest of V'_1 keeps slope 1 after the twist, so
m(-sigma) = r(V'_(1,sigma)) - Sw(V'_(1,sigma) tensor L_psi(x' sigma)) <= r(V'_(1,sigma)), with equality exactly
when V'_(1,sigma) tensor L_psi(x' sigma) is tame. Likewise m(0) <= r(V'_<1), with equality exactly when V'_<1 is
tame. V'_(1,sigma) is a direct summand of V'_1 as a module over inertia, because the break decomposition of the
twist is canonical and twisting back is an isomorphism. For distinct sigma the modules V'_(1,sigma) have no
simple constituent in common (same argument as in Step 2). Their sum inside V'_1 is direct: a nonzero
intersection of one of them with the sum of the others would contain a simple submodule, which would be a
constituent of both, and the constituents of a sum are among those of the summands. Nothing here uses
semisimplicity. Therefore

    sum over s of m(s) <= sum over sigma != 0 of r(V'_(1,sigma)) + r(V'_<1) <= r(V'_1) + r(V'_<1) <= rank N.

By (1) the two ends are equal, so every inequality is an equality: V'_1 is the direct sum of the V'_(1,sigma);
V'_(1,sigma) = L_psi(-sigma x') tensor (tame of rank m(-sigma)), which is zero when -sigma is not in S; and V'_<1
is tame of rank m(0). With s = -sigma this is (4).

## The sign of the frequencies

The printed primed formula (ii)' of 2.3.1.1 writes the twist as L(s.x'). Step 2 does not quote it: it applies the
unprimed formula to F' and uses F'F = a^*( )(-1), which gives the twist by -s at the point s. So the printed
(ii)' has the opposite sign to what 1.2.2.1 gives (a slip or an unstated convention; open at the source,
harmless here). The sign of (4) is pinned by examples the referee worked out: the skyscraper at s goes to
L_psi(s x')[1], and F' of that is the skyscraper at -s; the transform of the Kummer sheaf translated to s is
L_psi(s x') times the transform of the Kummer sheaf. The composite of the signs of (2) and (4) is
also confirmed by exact computation: for q = 3 the transform Q_2 drops at rho_2 z and not at -rho_2 z
(`../compute/main-session-check/round4_check_out.txt`, case 1, where 1 and -1 are different points).

## Consequence for the induction

With b = h c_i: F_b(P) = [b]^*F(P), so singular points are divided by b and a block L_psi(s x') becomes
L_psi(b s x'). P_(i+1) = (j_!L) tensor F_b(P_i). If no root of f is a singular point of F_b(P_i) (hypothesis (G)),
then at a root z the sheaf L tensor N is tame with inertia acting through the scalar chi != 1 on a module of rank
rank N, so j_! = j_* there and m(z) = rank N; at the other singular points L is lisse, the sheaf stays a
pushforward, stays tame by (3), and m is the drop of (2); at infinity L is tame, so (4) gives (H2) again; M_(i+1) is
irreducible (restriction of an irreducible lisse sheaf to a dense open, tensored with a rank-one sheaf) and is
ramified at the roots, so it is not an Artin-Schreier sheaf and P_(i+1) is simple of type T3. So (H1), (H2) and
"simple of type T3" pass from P_i to P_(i+1), with exactly the sets, multiplicities and ranks of `PROOF_V2.md`
Theorem 1. Characters of the tame parts are not tracked and are not needed.

## Remarks from the referee

(H2) can be weakened to a filtration with the same graded pieces; conclusion (4) still gives a direct sum.
Irreducibility and type T3 are used only to know that F(P) is of the form (j'_*N)[1]. Steps 0 and 1 are Laumon's
own proof of 2.3.1.1 and 2.3.1.2 in sheaf ranks; Steps 2 and 3 are the new part. The lemma's conclusions agree
with Laumon 1.4.3.2 for the Kummer sheaf, and with its translates and Artin-Schreier twists. A Kloosterman sheaf
is outside (H2).

## What is still cited and not read at its source

R2's proof (Raynaud). Proper base change and the formalism for Q_l-bar coefficients (register C-2). Inside R5:
BBD 4.1.1, 4.1.2, 4.2.5, 4.3.1 (OCR only), Katz-Laumon 2.1.3 (OCR only), and the involutivity theorem 1.2.2.1
(read on the page by A2, not by me). The existence and exactness of the break decomposition (Laumon 2.1.1 to
2.1.2.6, citing Serre and Katz).
