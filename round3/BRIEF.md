# Round three: can the route be completed for every k?

Read first: `../TOY_CASE.md` (round one), `../round2/ROUND2.md` and `../round2/MAIN_SESSION_CHECK.md` (round two).
Reports that matter here: `../round2/reports/RED-reduction-check.md`, `GEN-general-k.md`, `LIT-primary-sources.md`,
`K4T-k4-theory.md`. Text dumps of primary sources opened in round two are in `../round2/compute/LIT/`
(LAU.txt is Laumon 1987, KL.txt Katz-Laumon 1985, BBD.txt, SGA1.txt, SGA4h.txt, and others).

This is about character sums over finite fields. The bound in question is Weil's theorem of 1948. The question is
whether the route of footnote 3 of the "Remark" can be made a complete proof that uses no weights. Nothing here
says anything about the Riemann Hypothesis for the integers.

## Setting and what is established

q odd, f squarefree of odd degree d >= 3 over F_q with f(0) != 0, Z its roots, R' the set of ratios z'/z of roots,
chi the quadratic character, t = chi(f), L the rank-one sheaf of chi(f) on the affine line and j_!L its extension
by zero at Z (equal to j_*L, because the monodromy at each root is -1), M = sum of t, alpha_1..alpha_{d-1} the
Frobenius eigenvalues on H = H^1_c(line, j_!L), so M_n = - sum alpha_i^n.
Q_c(x) = c_1 x_1 x_2 + ... + c_{k-1} x_{k-1} x_k, Y = {Q_c = 0}, K = restriction of the k-fold external product,
N = sum of t(x_1)...t(x_k) over Y, S_h = sum over all x of t(x_1)...t(x_k) psi(h Q_c(x)), R = sum over h != 0 of S_h.

Established (rounds one and two; Lean files in `../lean/ToyWeil/`):
- q N = M^k + R and |S_h| <= q^((k-1)/2) * sum |t|^2 <= q^((k+1)/2) for h != 0 (Lean, any finite field).
- If a finite sum of n-th powers with nonzero coefficients is O(rho^n), every base is at most rho (Lean).
- H^j_c(Y, K) = 0 for j < k-1 (every k, f, c).
- With F = (pullback of the external product) tensor L_psi(h Q_c) on (h-line) x A^k:
  H^m_c(A^1 x A^k, F) = H^(m-2)_c(Y, K)(-1); the exact sequence
  0 -> T -> H^(k+1)_c(G_m x A^k, F) -> H^(k-1)_c(Y, K)(-1) -> 0 with T the k-fold tensor power of H;
  and for fixed h != 0 the cohomology of A^k with coefficients in F_h is that of the line with coefficients in
  P_k[-k], where P_1 = j_!L[1] and P_(i+1) = (j_!L) tensor FT_(h c_i)(P_i), FT the l-adic Fourier transform. So the
  fibre cohomology lives in degrees k and k+1 only. (Report RED, round two.)

## Claim A: the reduction (report GEN of round two; NOT refereed)

Call (P_k^c): H^(k+1)_c(A^k over F-bar, F_h) = 0 for all h in a dense open subset of G_m.
Claim A. If (P_k^c) holds for some c with all c_i nonzero, in some finite extension F_Q of F_q, then every alpha_i
satisfies |alpha_i|^k <= q^((k+3)/2).
Argument. Leray over the h-line: with R^(k+1) punctual, the wrong-parity group H^(k+2)_c(G_m x A^k, F) is
H^2_c(G_m, R^k), the coinvariants of the generic local system of R^k, twisted by (-1). So a wrong-parity eigenvalue
is q*beta with beta the Frobenius eigenvalue on a geometrically constant quotient of R^k. At a closed point h_0 of
degree m where the fibre has cohomology in degree k only, beta^m is an eigenvalue of Frobenius on the fibre; the
fibre sum over the extensions of F_(q^m) is then a sum of powers with one sign, bounded by Parseval, so
|beta| <= q^((k+1)/2). Now alpha^k (alpha of largest modulus) is an eigenvalue on T, inside the middle group. Either
its net coefficient in R is nonzero, and the bound on R gives |alpha|^k <= q^((k+3)/2); or it is cancelled by a
wrong-parity eigenvalue q*beta, and then |alpha|^k = q|beta| <= q^((k+3)/2). No sign statement about Y is used.

## Claim B: the fibre statement (main session's sketch; NOT checked by anyone)

Define rho_i = -c_(i-1)/c_i for 2 <= i <= k-1, and finite sets Sigma_1 = {0}, Sigma_2 = rho_2 Z,
Sigma_i = rho_i (Z union Sigma_(i-2)) for i >= 3.
Claim B. If Z is disjoint from Sigma_i for every i <= k-1 (a condition on the ratios of the c_i and on the roots
only; it holds for c outside finitely many hypersurfaces of the torus, and it does not involve h), then for EVERY
h != 0 the cohomology H^j_c(A^k, F_h) vanishes for j != k.
Sketch. By induction every P_i is an irreducible perverse sheaf on the line, the middle extension of an irreducible
lisse sheaf M_i:
 1. P_1 = j_!L[1] is irreducible (rank one, ramified at each root).
 2. The Fourier transform is an auto-equivalence of perverse sheaves on the line (involutivity and exactness,
    Laumon 1987, 1.2.2.1 and 1.3.2.3), so Q_i = FT(P_i) is irreducible perverse. It is not punctual, because P_i is
    ramified at the roots and so is not of the form L_psi(a x)[1].
 3. P_(i+1) = j_!(L tensor Q_i restricted to the complement of Z). Away from Z it is locally Q_i twisted by a
    rank-one lisse sheaf. At a root z where Q_i is lisse, the monodromy of L tensor Q_i is -1 times the identity,
    so extension by zero equals the middle extension there. Hence, if Z is disjoint from the finite singular set of
    Q_i, P_(i+1) is the middle extension of the irreducible lisse sheaf L tensor (generic part of Q_i): irreducible.
 4. The finite singular set of Q_i is contained in Sigma_i. Reason: stationary phase (Laumon 2.3.3.1, with the local
    transforms of 2.5.3.1). FT_(b)(P) can be singular at a finite point w != 0 only if P at infinity has a
    component L_psi(a x) tensor (tame) with a + b w = 0, and at w = 0 only if P at infinity has a part of slope < 1.
    And the monodromy at infinity of FT_(b)(P) is the sum over the finite singular points s of P of
    L_psi(b s y) tensor (tame). By induction all local monodromies are "tame" at finite points and
    "sum of L_psi(linear) tensor tame" at infinity; P_i has finite singular set Z union Sigma_(i-1), so
    P_(i+1) = L tensor FT_(h c_i)(P_i) has frequencies h c_i s at infinity, s in Z union Sigma_(i-1), and
    FT_(h c_(i+1)) of it is singular only at w = -(c_i/c_(i+1)) s, and at 0 when s = 0 occurs. The h cancels.
 5. Then H^1_c(line, P_k) is the constant quotient of the irreducible sheaf M_k (twisted), and M_k is ramified at
    the roots, hence not constant: the group is zero. H^(-1)_c vanishes by Artin. So the fibre cohomology is in
    degree k only.
Remarks. (a) For the plain all-ones quadric the hypothesis fails from i = 4 on (rho_4 rho_2 = 1 is in R'), so the
proof needs coefficients in general position; whether the conclusion fails there is a separate question. (b) The
known failures of the sign statement at k = 3 (c_1 = -c_2) and k = 4 (c_1 + c_2 + c_3 = 0) are not failures of
Claim B: at k = 4 with c = (1, 1, -2) the hypothesis of Claim B holds for generic f.

## If A and B both hold

For every k choose c in general position in a finite extension. Then |alpha| <= q^(1/2 + 3/(2k)) for every k, hence
|alpha| <= sqrt(q): Weil's bound for y^2 = f(x), by a route that uses the trace formula, Künneth, base change,
Artin vanishing, the Fourier transform with its stationary phase, and Parseval, and no weights.

A warning about novelty. Laumon's 1987 paper proves Deligne's main theorem of Weil II with the Fourier transform,
and the textbook of Kiehl and Weissauer presents that proof with a Plancherel argument. This route may be a
special case or a rediscovery of that proof. Finding out is part of the job.

## Rules for every agent

- Label every claim PROVED (full argument given), CITED (author, title, year, statement number, and whether you
  OPENED the source), CHECKED (exact arithmetic; script and output file named), OPEN or HINT.
- No proof may use weights, purity, the Weil bound or the Weil conjectures. When you cite a theorem, say whether
  its own proof uses them, if you can tell from the source.
- Claims A and B above are unchecked sketches by interested parties. Finding the error is the most valuable thing
  you can do. A proof with a hole presented as complete is the worst result.
- Floating point may suggest, never certify.
- Write only under `round3/` (the Lean agent also in `../lean/ToyWeil/`). Never extract, build or run the Lean
  archive of the claimed proof.
