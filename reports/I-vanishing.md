# I. The vanishing statement that carries the argument

Scope: the toy statement is the Weil bound for y^2 = f(x), a theorem (Weil 1948). This report asks only whether the cohomological sign statement (S_k) that footnote 3 needs can be proved, for which k, f and c. Nothing here says anything about the Riemann Hypothesis for the integers.

Labels: PROVED (full argument here), CITED (standard theorem), CHECKED (exact integer computation, script and output named), OPEN, HINT. Proofs below use no weights, no Weil conjectures and no Weil bound. Where I use them to interpret data this is said explicitly and the label is HINT.

Files: compute/I/i_k4.py, output compute/I/i_k4_out.txt (exact integer arithmetic, one process, below normal priority; formulas checked against brute-force enumeration).

## 0. Setting and the statement

q odd, F-bar = algebraic closure of F_q, f in F_q[x] squarefree of odd degree d >= 3 with root set Z (d points of F-bar). U = A^1 minus Z, j: U -> A^1, L = L_chi(f) the rank-one Kummer sheaf on U (quadratic character, tame, geometric monodromy -1 at each root, trivial Swan). Quadric Q_c(x) = c_1 x_1x_2 + ... + c_{k-1} x_{k-1}x_k with c_i in F_q^*; Y = {Q_c = 0} in A^k; K = ((j_!L)^{boxtimes k})|_Y, the extension by zero of L^{boxtimes k} from Y^0 = Y cap U^k.

(S_k): H^j_c(Y, K) = 0 for all j != k-1.

Basic facts used throughout (CITED, SGA 5 X and SGA 4 XVII): for F = j_!M with M lisse of rank one on a dense open of A^1, H^0_c(A^1, F) = 0, H^2_c(A^1, F) = (coinvariants of M)(-1) (dimension 0, or 1 exactly when M is geometrically trivial), and dim H^1_c = (number of removed points) - 1 + dim H^2_c, because chi_c(A^1, F) = 1 - m with m the number of removed points (tame at infinity, Swan 0). For F = j_!L: dim H^1_c = d-1. Künneth (SGA 4 XVII 5.4.3) gives H^*_c of exterior products.

Roots and symmetry: write Stab(Z) for the finite subgroup {sigma in Aff_1(F-bar): sigma(Z) = Z}, and mu(Z) = {r in F-bar^*: rZ = Z}. Since f is squarefree, f(x) f(rx) is a square times a constant iff r in mu(Z) (PROVED: both factors are squarefree, so the product is a square iff the root sets agree).

## 1. Lower degrees: H^j_c(Y,K) = 0 for j < k-1

**Proposition 1 (PROVED, no genericity).** For every k >= 2, every nonzero polynomial Q (not only the path quadric) and every f: H^j_c(Y, K) = 0 for j < k-1.

Proof.
1. P := (j_!L[1])^{boxtimes k} = G[k], G = (j_!L)^{boxtimes k} a constructible sheaf supported on the closure of U^k, i.e. on all of A^k. P is perverse on A^k: j is an affine open immersion of a smooth curve, so j_!L[1] is perverse, and an external product of perverse sheaves over an algebraically closed field is perverse (CITED: BBD, Astérisque 100, Prop. 4.2.8; section numbers to be confirmed by the literature agent).
2. Let i: Y -> A^k be the closed immersion and u: V = A^k minus Y -> A^k the open complement. V = {Q != 0} is a principal open set, so u is an AFFINE open immersion. For an affine open immersion u_! and u_* are t-exact (CITED: BBD Thm 4.1.1 and Cor. 4.1.3; Artin).
3. Distinguished triangle i_*i^*P[-1] -> u_!u^*P -> P -> . Both u_!u^*P and P are perverse. Put A = i_*i^*P[-1]. The long exact sequence of perverse cohomology gives pH^j(A) = 0 unless j is 0 or 1.
4. i^*P[-1] = K[k-1], a single sheaf K placed in perverse-degree -(k-1), and dim supp K <= dim Y = k-1. By the support condition defining the perverse range (dim supp H^{-m} <= m), K[k-1] lies in pD^{<=0}. Hence pH^1(A) = 0 and A is perverse. So K[k-1] is a perverse sheaf on Y. (No non-characteristic or transversality hypothesis is needed. This is the point: K is a sheaf in ONE degree, and Y is a hypersurface with affine complement.)
5. Y is affine. Artin vanishing for perverse sheaves (CITED: SGA 4 XIV 3.1 with duality; BBD Cor. 4.1.2) gives H^i_c(Y, perverse) = 0 for i < 0. With i = j-(k-1), H^j_c(Y, K) = H^{j-k+1}_c(Y, K[k-1]) = 0 for j < k-1. QED

This replaces A's remark that only the lower half is obtained "under non-characteristic restriction". It needs no condition on the roots, no f(0) != 0 and no condition on c. It is consistent with all exact data below (H^0_c = H^1_c = 0 in the k = 2 and k = 3 computations, and the fibration computation for k = 4).

For the t = 1 control (trivial sheaf) the same proof gives that Q_Y[k-1] is perverse (lci hypersurface), which is the standard statement.

**The upper half is not formal.** By Verdier duality, H^j_c(Y,K) = 0 for j > k-1 is equivalent to H^s(Y, D(K[k-1])) = 0 for s < 0, a vanishing in the direction opposite to Artin's. It is false for t = 1 (the cone has H^{2k-2}_c = Q_l(-(k-1))) and false for the special c found in sections 2 and 3 below. Whatever proves it must use the specific sheaf L and the specific quadric.

## 2. k = 2 and k = 3 (PROVED)

### k = 2
Q = c_1 x_1x_2, Y = L_1 cup L_2 with L_1 = {x_1 = 0}, L_2 = {x_2 = 0}, meeting in the origin O.

Case f(0) = 0: the stalk of j_!L at 0 is zero, so K = 0 and every H^j_c vanishes.

Case f(0) != 0. The sequence 0 -> K -> K|_{L_1} + K|_{L_2} -> K_O -> 0 of sheaves on Y is exact. K|_{L_i} = (stalk L_{f(0)}) tensor j_!L on the other coordinate, so H^*_c(L_i, K) is H^1_c only, dimension d-1; K_O has rank one. The long exact sequence reads 0 -> H^0(O) = Q_l -> H^1_c(Y,K) -> H^1_c(L_1) + H^1_c(L_2) -> H^1_c(O) = 0 and gives H^j_c(Y,K) = 0 for j != 1, dim H^1_c = 2(d-1)+1 = 2d-1. Frobenius eigenvalues on H^1_c(Y,K): t_0 alpha_i (twice each) and 1, t_0 = chi(f(0)). This agrees with N_2 = -[2 sum (t_0 alpha_i)^n + 1] of A. **(S_2) holds for every c_1 != 0 and every squarefree f, with no further condition.**

### k = 3
Q = x_2 (c_1x_1 + c_2x_3). Y = A cup B, A = {x_2 = 0}, B = {c_1x_1 + c_2x_3 = 0}, A cap B = {x_2 = 0, x_3 = -lambda x_1}, lambda = c_1/c_2. Put mu_* = -1/lambda = -c_2/c_1 and g(x) = f(x) f(-lambda x); the roots of g are Z cup mu_* Z, and m := |Z cup mu_* Z| (distinct roots; m = 2d when Z and mu_* Z are disjoint, e.g. generically).

**Theorem 3 (PROVED).** Assume f(0) != 0 and g is not a constant times a square, i.e. mu_* Z != Z (equivalently mu_* not in mu(Z)). Then H^j_c(Y,K) = 0 for j != 2 and
 dim H^2_c(Y,K) = (d-1)^2 + (m-1)(d-1) + (m-1),
which is 3d^2-3d+1 for m = 2d (this agrees with A's hand count).

Proof. Sheaves on the pieces: K|_A = t_0-twist of j_!L boxtimes j_!L on the (x_1,x_3)-plane: H^*_c in degree 2 only, dimension (d-1)^2. On B (coordinates x_1, x_2): K|_B = j_!L_g(x_1) boxtimes j_!L(x_2), L_g := L_chi(g) restricted to the complement of the roots of g, extended by zero, tame (unramified at infinity because deg g is even). g non-square makes L_g geometrically nontrivial, so H^0_c = H^2_c = 0 and H^1_c has dimension m-1 (Euler characteristic 1-m). So H^*_c(B,K) is degree 2 only, dimension (m-1)(d-1). K|_{A cap B} = t_0-twist of j_!L_g on the line: H^1_c only, dimension m-1. The sequence 0 -> K -> K|_A + K|_B -> K|_{A cap B} -> 0 gives
 0 -> H^1_c(A cap B) -> H^2_c(Y,K) -> H^2_c(A) + H^2_c(B) -> 0
and H^j_c(Y,K) = 0 for all other j (all other terms vanish; the restriction maps H^1_c(A)+H^1_c(B) -> H^1_c(A cap B) have zero source). The dimensions add as stated. If f(0) = 0 then K|_A = 0 and H^*_c(Y,K) = H^*_c(B,K) = H^2_c only, again for mu_* Z not equal Z (on nonzero roots). QED

Where it fails (CHECKED + PROVED formula): if mu_* in mu(Z), the polynomial g is a square. The simplest case is c_1 = -c_2 (mu_* = 1; g = f^2; any f). Then C = sum_x t(x)t(x) = q - r_0 and N_3 = t_0 M^2 + (M - t_0)(q - r_0), which contains the term M q = -(sum alpha_i) q: coefficient -1 at the eigenvalue q alpha_i, the wrong sign (+1 is required for (S_3)). Exact data (compute/I/i_k4_out.txt, E3, f random cubic): p = 7: N_3 = 3 for c = (1,1), -13 for c = (1,-1); p = 13: -1 versus -14; p = 17: 13 versus -43; the sign is not the one predicted by (S_3) for c = (1,-1). The odd cubic x^3 - x of B and C is this phenomenon with c = (1,1), since mu_* = -1 and Z = -Z. (HINT for the identification of the failing class with H^3_c; the data are exact.)

So at k = 3 the vanishing holds exactly outside the degenerate locus mu_* Z = Z, and fails on it. Output of the argument at k = 3 is the trivial bound (A).

## 3. k = 4 (PROVED reduction; H^5_c = H^6_c = 0 PROVED; H^4_c decided for c1+c2+c3 = 0, reduced to a monodromy statement otherwise)

### 3.1 The Segre parametrisation (PROVED)
Put s = c_1x_1 + c_2x_3. Then Q = x_2 s + c_3 x_3x_4 = det [[x_2, -c_3x_3],[x_4, s]]. So Y is the cone of 2x2 matrices of rank <= 1: x_2 = lam_1 mu_1, -c_3x_3 = lam_1 mu_2, x_4 = lam_2 mu_1, s = lam_2 mu_2, hence
 x_1 = mu_2 (lam_2 + e lam_1)/c_1, e = c_2/c_3.
Y minus {0} -> P^1 (the column space [lam] = [lam_1:lam_2] of the matrix) is a Zariski-locally trivial bundle with fibre A^2 minus 0 (the planes Pi_lam = {lam tensor mu}). These planes meet only at the origin. On Pi_lam, with rho = (lam_1, lam_2) and rho' = (-lam_1/c_3, (lam_2 + e lam_1)/c_1):
 K|_{Pi_lam} = [ L_{f(rho_1 mu_1) f(rho_2 mu_1)} ] boxtimes [ L_{f(rho'_1 mu_2) f(rho'_2 mu_2)} ] (extended by zero).
Each factor is j_! of a rank-one sheaf on the line; it is geometrically trivial iff its ratio is in mu(Z): r = lam_2/lam_1 for the first and r' = tau(r) := -(c_3/c_1)(r + e) for the second.

### 3.2 Exact point-count formula (PROVED, CHECKED)
With C(r) = sum_x t(x) t(rx) (t = chi(f)):
 **N_4 = -q + t_0^2 M^2 + sum_{r in F_q} C(r) C(tau(r)).**
Proof: Y(F_q) minus 0 is the disjoint union of the F_q-points of the planes Pi_[lam], [lam] in P^1(F_q); each plane contributes A*B - 1 (the -1 removes the origin), A = C(r), B = C(tau(r)) for [lam] = [1:r], and A = B = t_0 M for [lam] = [0:1]. N_4 = 1 + sum_[lam] (AB - 1). CHECKED: identity equals brute-force enumeration in 36 random cases (p = 3, 5, 7, deg 3 and 5, random c) plus 4 cases at p = 11, 13: 0 mismatches (i_k4_out.txt, E0). This is a clean two-variable convolution of the one-variable object C, the "new two-variable object" A mentioned for k = 4.

### 3.3 H^5_c = H^6_c = 0 (PROVED, every c in (F-bar^*)^3, f(0) != 0)
Leray for pi: Y minus 0 -> P^1 (proper base): E_2^{a,b} = H^a(P^1, R^b pi_! K).
- Fibre cohomology H^b_c(Pi_lam minus 0, K): by the sequence of the origin, b = 1: one-dimensional, R^1 pi_! K is the constant sheaf (stalk K_O); b = 2: H^1 tensor H^1 of the two factors, rank (2d-1)^2 for generic lam; b = 3, 4 occur only when a factor is geometrically trivial, b = 3 if one is, b = 4 if both are. The number of lam where this happens is finite (mu(Z) finite). So R^3, R^4 are skyscraper sheaves.
- Hence E_2^{a,b} is nonzero only for (a,b) with a <= 2, b in {1,2}, or a = 0, b in {3,4}: total degree a+b <= 4.
- H^j_c(Y,K) = H^j_c(Y minus 0, K) for j >= 2. Therefore **H^j_c(Y,K) = 0 for j = 5, 6** (and j >= 7 trivially), for every c and every squarefree f with f(0) != 0. This part of the needed vanishing at k = 4 is proved unconditionally.

### 3.4 H^4_c(Y,K)
The only terms of total degree 4 are E_2^{2,2} = H^2(P^1, R^2 pi_!K) = (geometric coinvariants of the generic fibre local system V(r) boxtimes V(tau r), twist (-1)), where V(r) = H^1_c(A^1, j_!L_{f(x)f(rx)}), and E_2^{0,4}; the differential d_2: E_2^{0,3} -> E_2^{2,2} can kill part of E_2^{2,2}. So
 H^4_c(Y,K) = E_2^{0,4} + coker(d_2: E_2^{0,3} -> E_2^{2,2}) (up to the usual extension).

**(a) The class E_2^{0,4}** is nonzero iff some lam has BOTH factors geometrically trivial, i.e. iff mu(Z) cap tau^{-1}(mu(Z)) is nonempty. Since 1 is in mu(Z), this contains the case tau(1) = 1, which means **c_1 + c_2 + c_3 = 0**. When mu(Z) = {1}, E_2^{0,4} != 0 iff c_1 + c_2 + c_3 = 0.

**(b) Theorem 4 (PROVED): if c_1 + c_2 + c_3 = 0 then H^4_c(Y,K) != 0, so (S_4) FAILS.** Proof: then the plane Pi = {x_1 = x_3, x_2 = x_4} lies in Y: Q|_Pi = x_1x_2 (c_1 + c_2 + c_3) = 0. On Pi, K|_Pi = L_{f(x_1)^2} boxtimes L_{f(x_2)^2} = (j'_!Q_l) boxtimes (j'_!Q_l), j': A^1 minus Z -> A^1, so H^4_c(Pi,K) = H^2_c(A^1, j'_!Q_l)^{otimes 2} = Q_l(-2), one-dimensional with Frobenius eigenvalue q^2. In the sequence H^4_c(Y,K) -> H^4_c(Pi,K) -> H^5_c(Y minus Pi, K), the last group is zero: Y minus Pi is the family over P^1 minus {[1:1]} and the E_2-argument of 3.3 applies verbatim (total degree <= 4 on every fibration; the unique doubly-special plane has been removed). So H^4_c(Y,K) surjects onto a one-dimensional space with eigenvalue q^2: N_4 contains a term +q^{2n}, sign opposite to (-1)^{k-1} = -1. QED.

**Exact data confirm this** (CHECKED, i_k4_out.txt E1, E2; N_4 from the exact formula above, f random squarefree cubics and quintics with f(0) != 0, 8 polynomials per prime):
- c with c_1+c_2+c_3 = 0 (here c = (1,1,-2)): mean N_4/p^2 over f is 0.75, 1.07, 0.89, 1.08, 0.99, 0.87, 1.03, 0.89, 1.07, 0.97, 1.05, 1.06, 0.88, 0.95, 1.05, 0.96, 0.96, 0.97, 0.99, 0.97 for p = 5, 7, 11, ..., 79; minimum of N_4/p^2 over the sample is >= 0.36 overall and >= 0.48 from p = 23 on. N_4 = p^2 + O(p^{3/2}) as predicted by one class q^2 with sign +.
- c with c_1+c_2+c_3 != 0 ((1,1,1) and (1,2,3)): mean N_4/p^2 is 0.30, 0.43, 0.10, 0.19, 0.06, 0.20, 0.15, 0.29, 0.21, -0.01, 0.23, 0.15, 0.02, 0.18, 0.19, 0.24, -0.04, 0.14, 0.03, -0.04 for c = (1,1,1), range of N_4/p^2 within [-0.6, 0.9] for p >= 37, with no persistent positive q^2 term.
- p = 3, c = (1,1,1) has sum 3 = 0: N_4 over F_3 equals 1, 5 or 9 for twelve random f (all positive, N_4 about q^2 = 9), versus c = (1,1,2) (sum 1): values 9, -1, -3, 33, -3, ... of both signs (E2). This is the "wrong-sign q^2 term at p = 3" that C reported (HINT) and now explained: **it comes from the plane Pi, not from arithmetic accident**.
Weights are used only to read the data (a q^2 class would be the only source of a persistent N_4/p^2 -> 1 trend); the proof of Theorem 4 does not use them.

**Consequence for the Remark's setting.** The plain path quadric c = (1,1,1) at k = 4 fails (S_4) in characteristic 3. In F_3 the choice c = (1,1,2) (sum 1) avoids it. For q = 3, 5, 7, ... the locus c_1+c_2+c_3 = 0 has a fraction about 1/q of (F_q^*)^3.

**(c) The remaining question (OPEN).** For c_1+c_2+c_3 != 0, and mu(Z) cap tau^{-1}mu(Z) = empty, H^4_c reduces to the coinvariants of V(r) boxtimes V(tau r) on the r-line, modulo d_2. Structure of V(r) (hyperelliptic, weights used only to describe it): an extension of the rank-one Kummer sheaf L_chi(r) (the class "at infinity", weight 0, geometric monodromy -1 at r = 0, infinity) by a rank 2d-2 piece W(r) (the H^1 of the genus d-1 curve y^2 = f(x)f(rx)). The coinvariants vanish if (i) L_chi(r tau(r)) = L_chi(-(c_3/c_1) r (r + e)) is geometrically nontrivial (true: a quadratic with distinct roots is not a square), (ii) W has no rank-one constituent, and (iii) W and tau^*W^(dual) share no irreducible constituent, which follows from irreducibility of W together with the fact that W has d^2-d (+1) singular points r = z'/z while tau^*W has the translated, scaled copy: for generic f and c the two singular sets differ, and a pseudo-reflection at a point where one of them is smooth contradicts an isomorphism. Irreducibility of such a Picard-Lefschetz family is a theorem of Lefschetz-pencil type (CITED in spirit: Katz, SGA 7 XVIII and Deligne; exact statement and weight-free proof NOT located; this is a gap, not a result). Everything in (c) is OPEN, but it is now a finite monodromy question about one explicit family on A^1.

For c = (1,1,1), p != 3 and generic f the data show N_4/p^2 -> 0 (above), which is what coinvariants = 0 predicts for the top-weight part of H^4_c; lower-weight H^4 classes would not be visible in this statistic.

### 3.5 Euler characteristic and the size of H^3_c (CHECKED arithmetic; Swan = 0 assumed)
From 3.1-3.3 the Euler characteristic of Y minus 0 is -2 (R^1, since chi(P^1) = 2) + chi(P^1, R^2) - chi(P^1, R^3). Stalk dimensions on P^1: rank (2d-1)^2 at a generic point; (d-1)(2d-1) at r = 0 and r = -e; (d-1)^2 at r = infinity; d(2d-1) at r = 1 and at tau^{-1}(1); (2d-2)(2d-1) at the 2(d^2-d) ratio points z'/z (z != z') of the two families; R^3 has stalk 2d-1 at r = 1 and at tau^{-1}(1). Using that R^2 is tamely ramified at its singular points,
 chi_c(Y,K) = -2 + (2(2d-1)^2 + D) - 2(2d-1) + 1 = 1 - 4d + 3d^2 - 4d^3,
D = -2d(2d-1) - d(3d-2) - 2(2d-1)(d-1) - 2d(d-1)(2d-1) (sympy, i_k4_out.txt E4: difference from A's independent hand count is exactly 0). For d = 3: chi_c = -92. So dim H^3_c - dim H^4_c = 92 for d = 3 (generic f, c). If H^4_c = 0 then dim H^3_c = 92, matching A's prediction dim E = 92. The tame (Swan 0) assumption at the singular points of R^2 is NOT proved here (OPEN); the match with A's count is evidence that it holds.

## 4. General k

### 4.1 What is proved for every k
- Proposition 1: H^j_c(Y,K) = 0 for j < k-1, for every f, every c, every k.
- k even, Q nondegenerate; k odd, Q degenerate: no restriction needed in Proposition 1.
- Reformulations (PROVED, short): with W = A^k x A^1_h, F = K tensor L_psi(hQ), H^j_c(Y,K)(-1) = H^{j+2}_c(W, F), and H^*_c(A^k, K) = M^k in degree k. By Proposition 1, the map H^k_c(A^k,K) (the M^k eigenvalues) -> H^{k+1}_c(G_m x A^k, F) = H^1_c(G_m, Phi) is injective when Phi = R^kpr_!F is the single-degree Fourier sheaf on G_m (assumption). Then (S_k) is equivalent to: H^2_c(G_m, Phi) = 0 (no geometrically trivial quotient of Phi). This is the exact form of "R = qN - M^k has one sign": sign (-1)^{k-1} iff H^2_c(G_m, Phi) = 0. It is a statement about the iterated Fourier transform sheaf; it is not proved.

### 4.2 Obstructions found (PROVED for k = 3, 4; mechanism general)
If Y contains a closed subvariety Pi of dimension s on which K|_Pi is geometrically trivial on a dense open set in s' of the s directions, then H^{s+s'}_c(Pi, K) != 0, and this survives to Y unless killed by H^{s+s'+1}_c(Y minus Pi, K). When s + s' > k-1 this is a failure of the upper half.
- k = 3: Pi = B = {x_3 = -lam x_1} with lam = -1 (c_1 = -c_2): s = 2, s' = 1, degree 3 > 2.
- k = 4: Pi = {x_1 = x_3, x_2 = x_4} when c_1+c_2+c_3 = 0: s = s' = 2, degree 4 > 3, survival PROVED (Theorem 4).
- k = 2m: for a perfect matching sigma of {1..2m} with no adjacent pair, Pi_sigma = {x_i = x_sigma(i)} has dimension m and lies in Y iff, for each pair of pairs, the sum of the c_i on edges joining them is zero (C(m,2) linear conditions on the 2m-1 coefficients). K|_Pi is a product of f^2-type sheaves, so H^{2m}_c(Pi, K) = Q_l(-m) != 0 and 2m > k-1. (Survival into H^k_c(Y,K) not proved beyond k = 4.) More generally ratios u in mu(Z) replace the identification x_i = x_sigma(i).
These bad sets are proper closed subsets of c-space, and a count (number of perfect matchings (2m-1)!! versus q^{C(m,2)}) shows that for q = 3 and m >= 3 there are F_q-rational c outside all of them: so the particular genericity obstruction "F_q-rational c avoid a growing family of hyperplanes" is not an obstruction for this family. Other bad sets (non-perfect isotropic configurations, other strata of the root arrangement) are not enumerated: OPEN.

### 4.3 The cleanest statement I believe (OPEN for k >= 4 in general)

**Conjecture S (what the argument needs).** Let q be odd, f in F_q[x] squarefree of odd degree d >= 3 with f(0) != 0 and Stab(Z) = {1} (Z has no nontrivial affine symmetry over F-bar; this excludes odd cubics after translation, translation-invariant f when p | d, and similar). There is a proper closed subscheme B_k of G_m^{k-1} defined over Z, containing at least the hyperplanes of 4.2 (k = 3: c_1 + c_2 = 0; k = 4: c_1+c_2+c_3 = 0; k = 2m: the matching hyperplanes), such that for every c in G_m^{k-1}(F_q) outside B_k:
 H^j_c(Y_c, K_f) = 0 for all j != k-1, and dim H^{k-1}_c = (-1)^{k-1} chi_c(Y_c, K_f).
Status: PROVED for k = 2 (any c), k = 3 (c outside the one hyperplane, f with mu_* not in mu(Z)); lower half PROVED for all k; for k = 4 upper half PROVED except H^4_c, which is exactly the coinvariants/d_2 statement of 3.4(c) away from c_1+c_2+c_3 = 0 and FAILS on it.

**Standard result that would prove the upper half.** None known to me. It is a Lefschetz-type vanishing in the direction opposite to Artin: for the perverse sheaf K[k-1] on the affine hypersurface Y, H^s(Y, D(K[k-1])) = 0 for s < 0. Candidate tools:
1. Goresky-MacPherson / Hamm-Le Lefschetz theorems for generic hyperplane sections of affine varieties and perverse sheaves (give the lower half, as in Proposition 1; upper half not covered).
2. Generic vanishing on tori (Gabber-Loeser Duke 1996; Krämer-Weissauer; Bhatt-Schnell-Scholze): good for characters off a finite union of torsion translates of subtori; the quadratic character is torsion, hence in the typical exceptional set.
3. Katz, "Perversity and exponential sums" (the Gabber hypersurface argument in the second half of footnote 3): vanishing of H^i_c(A^n, P tensor L_psi(F)) for i != n for suitable F; I could not match its hypotheses to F = hQ, which is a quadratic form, not a generic polynomial of degree prime to p.
4. The induction by Fourier transform of section 4.1: (S_k) iff the Fourier sheaf Phi has no trivial quotient.

**What remains to verify to apply any such theorem.**
(i) Single-degree concentration of H^*_c(A^k, K tensor L_psi(hQ)) for h != 0 (follows from an iterated Fourier-transform argument if every stage is a perverse sheaf with no punctual or L_psi constituents; not checked beyond k = 2, 3, 4).
(ii) Absence of trivial quotient of Phi, which reduces to non-existence of isotropic configurations of 4.2 and to monodromy irreducibility statements as in 3.4(c).
(iii) Stab(Z) = {1} and f(0) != 0 (these conditions rule out the degenerate-sheaf phenomena found so far that produce wrong-sign classes, not shown to be sufficient or necessary in general: a symmetry appears in k = 4 as f(x) f(ax+b) a square for (a,b) = (1, b) when b is a translation symmetry).
(iv) F_q-rational c outside B_k for the given q and all k; uniformity in k at fixed q (A's concern) is not settled by the matching count alone.
(v) Every claim must be re-proved without weights; any proof through purity of H^i_c(Y,K) or Weil II contains the toy theorem (circular).

## 5. What this does to the argument

1. The cohomological input (S_k) is NOT a formality and is false for explicit simple choices: c = (1,-1) at k = 3 (any f), and at k = 4 every c with c_1+c_2+c_3 = 0 (for example (1,1,-2) in any odd characteristic, and (1,1,1) in characteristic 3), where a class with eigenvalue q^2 appears in H^4_c with the wrong parity. The plain path quadric with all c_i = 1 is in the bad set whenever 3 = 0 in F_q (k = 4).
2. For f with a symmetry (odd f, translation-invariant f), additional wrong-sign classes appear (k = 3 with Z = -Z: x^3 - x).
3. The lower half is true and elementary; the upper half is where all the content is, and for k >= 4 it is unproved. Note that a pure-weight or purity argument for it would be circular (A).
4. Even if (S_k) held for all k outside B_k, A's section 3 shows only |alpha| <= q^{1/2 + 3/(2k)}; the passage to q^{1/2} needs infinitely many k for the same (q, f), hence B_k(F_q) != everything for infinitely many k.

## 6. Paper inputs
- Artin vanishing for perverse sheaves, t-exactness of affine u_! (BBD, Astérisque 100: Thm 4.1.1, Cor. 4.1.2, 4.1.3; external products Prop. 4.2.8); SGA 4 XIV 3.1.
- Künneth for compact supports (SGA 4 XVII 5.4.3); Grothendieck-Ogg-Shafarevich (SGA 5 X); lci hypersurface Q[n] perverse (follows from the triangle in the proof above).
- Lefschetz-pencil irreducibility of vanishing-cycle local systems (Katz/Deligne, SGA 7 XVIII): statement not located, used only in the OPEN part 3.4(c).
- Section and statement numbers are from memory and must be confirmed by the literature agent.

## 7. Status table

| statement | status |
|---|---|
| H^j_c(Y,K) = 0, j < k-1, all k, f, c | PROVED (Prop. 1) |
| (S_2), all c, f | PROVED |
| (S_3), f(0) != 0, mu_* Z != Z, dim 3d^2-3d+1 (m = 2d) | PROVED |
| (S_3) fails for c_1 = -c_2 (any f) | exact formula PROVED; class identification HINT |
| k = 4: H^5_c = H^6_c = 0, all c, f(0) != 0 | PROVED |
| k = 4: c_1+c_2+c_3 = 0 implies H^4_c != 0 (so (S_4) false) | PROVED; CHECKED by data |
| k = 4: N_4 = -q + t_0^2 M^2 + sum C(r) C(tau r) | PROVED, CHECKED (40 cases, 0 mismatches) |
| k = 4: chi_c(Y,K) = 1-4d+3d^2-4d^3 (-92 at d = 3) | derived with Swan = 0 assumed; matches A's hand count; CHECKED arithmetic |
| k = 4: H^4_c = 0 for c_1+c_2+c_3 != 0, generic f | OPEN (monodromy); data HINT toward vanishing of its top-weight part |
| k >= 5: (S_k) for any c | OPEN |
