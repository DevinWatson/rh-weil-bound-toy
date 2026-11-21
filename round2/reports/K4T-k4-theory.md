# K4T. The case k = 4 (round two)

Scope: character sums over finite fields. The bound in question (Weil 1948) is a theorem; the question is whether the route of the note is a valid proof and what it needs. Nothing here says anything about the Riemann Hypothesis for the integers.

Labels: PROVED (full argument given here), CITED (author, title, year, statement; numbers from memory unless marked), CHECKED (exact integer or rational arithmetic, script and output named), OPEN, HINT. No proof below uses weights, purity, the Weil bound or the Weil conjectures. Weights are used only in section 8, to read data, and each use is marked.

Files: `compute/K4T/k4t_checks.py`, output `compute/K4T/k4t_checks_out.txt` (exact integers and sympy rationals, one process, below normal priority, 2 s).

## 0. Result in one page

Setting: q odd, f squarefree of odd degree d >= 3 over F_q, f(0) != 0, Z = roots of f in F-bar, chi quadratic, t = chi(f), c = (c_1, c_2, c_3) in (F-bar^*)^3, e = c_2/c_3, tau(r) = -(c_3/c_1)(r + e), Y = {Q_c = 0}, K as in the brief. All cohomology is geometric (over F-bar); vanishing there gives vanishing as a Frobenius module.

Define
- mu = {rho in F-bar^* : rho Z = Z} (finite cyclic, order m dividing d, prime to p);
- R' = {z'/z : z, z' in Z} (contains 1 and all of mu);
- S = {0} union R' (at most d^2 - d + 2 points). S contains every finite point where V (section 2) is ramified.

What is decided (c_1 + c_2 + c_3 != 0 throughout, since the case c_1 + c_2 + c_3 = 0 is the known failure):

1. PROVED (Theorem A). H^j_c(Y,K) = 0 for j = 5, 6, and for j <= 2 (round one). H^4_c(Y,K) has a two-step filtration with pieces E^{0,4} and E^{2,2}.
2. PROVED (Theorem B). E^{0,4} != 0 iff there are rho, rho' in mu with c_2 + c_3 rho + c_1 rho' = 0. In that case H^4_c != 0 and (S_4) FAILS. For mu = {1} this is exactly c_1 + c_2 + c_3 = 0. For mu != {1} it is a new, larger bad set (planes {x_4 = rho x_2, x_1 = rho' x_3}).
3. PROVED (Theorem C, the heart). The coinvariants of V on the r-line vanish: V_pi = 0, for every f except possibly f = x^d - a (mu = mu_d), where dim V_pi <= 1 (and = 0 modulo a rank-two irreducibility statement, section 5.3). V is tame everywhere, including r = infinity: PROVED by an Euler characteristic count (this removes the "Swan = 0 assumed" caveat of report I).
4. PROVED (Theorem D). If no s, s' in S satisfy c_2 + c_3 s + c_1 s' = 0 (the singular sets of V and tau^* V are disjoint) and f is not of the form x^d - a, then E^{2,2} = 0, hence **H^4_c(Y,K) = 0 and (S_4) holds**, and for mu = {1}: dim H^3_c(Y,K) = 4d^3 - 3d^2 + 4d - 1 (92 for d = 3, 444 for d = 5).
5. Exceptional list. The complete list of conditions on c for which the argument does not give vanishing is: (X1) a pair rho, rho' in mu with c_2 + c_3 rho + c_1 rho' = 0 (nonvanishing PROVED); (X4) a pair s, s' in S with c_2 + c_3 s + c_1 s' = 0 (the singular sets meet; X1 is contained in X4); (X2) f = x^d - a. (X0 is c_1 + c_2 + c_3 = 0, the case X1 with rho = rho' = 1.) Each X4 condition is a line in the plane of (c_1 : c_2 : c_3); there are at most (d^2 - d + 2)^2 - 1 of them (63 for d = 3). Detailed in section 7.
6. OPEN, conditional. For mu = {1}, X4 is not by itself a failure. Assuming (Irr) the local system W (section 2) is irreducible and (Loc0) its local monodromy at r = 0 has eigenvalue -1, then H^4_c = 0 for EVERY c with c_1 + c_2 + c_3 != 0 (section 6). Neither (Irr) nor (Loc0) is proved here. (Irr) is a Lefschetz-pencil statement; the usual proof is weight-free but needs the conjugacy of vanishing cycles, which I did not establish.

So: for k = 4, outside an explicit finite union of lines in c-space (and f not of the form x^d - a), the sign statement (S_4) is PROVED without weights. This is a genuine weight-free case of (S_k). It also shows what the exceptional sets look like: they are caused by coincidences of the singular points of V and tau^*V, and by multiplicative symmetries of Z.

## 1. Check of report I, section 3

Verified, with the following findings.

- 3.1 (Segre parametrisation) correct. CHECKED by hand and by 3.2.
- 3.2 (point count N_4 = -q + t_0^2 M^2 + sum_r C(r) C(tau(r))) correct. CHECKED again: `k4t_checks.py` part A, 48 cases (p = 5, 7, random cubics, four values of c each), brute force over all p^4 points, 0 mismatches (`k4t_checks_out.txt`, line A).
- 3.3 (H^5_c = H^6_c = 0) correct. I redid the Leray argument for pi: Y minus 0 -> P^1: R^1 is constant (stalk K_0), R^2 has generic stalk V(r) tensor V(tau r), R^3 and R^4 are skyscrapers, so the only terms of total degree >= 5 vanish (H^a(P^1, skyscraper) = 0 for a > 0, and a <= 2).
- 3.4(a),(b) correct, but E^{0,4} != 0 is wider than "c_1 + c_2 + c_3 = 0" as soon as mu != {1}: see Theorem B.
- 3.4(c) contains an inaccuracy of orientation. V(r) = H^1_c(A^1, j_! L_g), g = f(x) f(rx), sits in 0 -> L_{chi(r)} -> V -> W -> 0, with the rank-one class AT INFINITY as the SUB and W (rank 2d - 2) as the quotient (the kernel of "forget supports" H^1_c -> H^1). Report I wrote "extension of L by W", which can be read either way. Proof of the orientation: the triangle on A^1 gives 0 -> H^0(I_infty, L_g) -> H^1_c -> H^1 -> H^1(I_infty, L_g); L_g is unramified at infinity (even degree, constant leading coefficient r^d), geometrically nontrivial; Frobenius on H^0(I_infty, L_g) is chi(r^d) = chi(r) (d odd). PROVED. W is the image, W = H^1(P^1, j_* L_g), rank 2d - 2, self dual up to twist by cup product.
- 3.4(c) point (iii) uses irreducibility of W "of Lefschetz pencil type, exact statement and weight-free proof NOT located". Still unproved here. But my Theorem D shows it is not needed away from the coincidence lines.
- 3.5 (Euler characteristic). The formula is correct. CHECKED: sympy re-derivation from stalk dimensions gives chi_c(Y,K) = -4d^3 + 3d^2 - 4d + 1, = -92 (d = 3), -444 (d = 5) (output line C). The assumption "Swan = 0 at the singular points" is now PROVED (Theorem C, step 1). One more remark: at r in mu not equal to 1 the stalk of V has dimension d (not d + 1), because the d coincidences are compensated by H^2_c = Q_l(-1); report I's count is for mu = {1}.

Nothing else in section 3 is wrong.

## 2. The sheaf V and the structure of the fibration

Notation. T = A^2 with coordinates (x, r), K_T = extension by zero of L_chi(f(x) f(rx)) from {f(x) f(rx) != 0}. p: T -> A^1_r. V := R^1 p_! K_T. F := j_! L_chi(f) on A^1_x; F is rank one, geometrically nontrivial, ramified (monodromy -1) at every root and at infinity, so j_! F = j_* F, H^*_c(A^1, F) = H^1_c only, of dimension d - 1; call it H. Put H_c^*(G_m, F) = H^1_c only, of dimension d (sequence of the point 0, F_0 is rank one since f(0) != 0).

Stalks of V (PROVED, proper base change): for r != 0, the number of removed points of the fibre is 2d - c_r, where c_r = #{(z, z') : z' = r z}; h^2 = 1 iff r in mu; dim V_r = (2d - c_r) - 1 + h^2. Generic: 2d - 1. r = 0: d - 1. r in R' not in mu: 2d - 1 - c_r. r in mu: d. Sum over r != 0 of c_r = d^2 (one r per ordered pair).

Structure (PROVED): V has sub L_{chi(r)} and quotient W (section 1); W is lisse off S, self dual up to twist. Generic rank 2d - 1.

Fibration of Y minus 0 over P^1 (report I, verified above): E_2^{a,b} = H^a(P^1, R^b pi_! K) with R^1 = Q_l constant, R^2 = G_2 (generic stalk V(r) tensor V(tau r)), R^3 skyscraper (stalk of rank dim V at the points where exactly one factor is geometrically trivial), R^4 skyscraper (both trivial). H^4_c(Y,K) = H^4_c(Y minus 0, K) (sequence of the origin). Degree 4: E^{2,2}, E^{1,3} = 0, E^{0,4}. Differentials: d_2: E_2^{0,3} -> E_2^{2,2} is the only one that can touch E^{2,2}; E^{0,4} receives and emits none (targets E_2^{2,3} = 0 and E_3^{3,2} = 0 because P^1 has cohomological dimension 2 and R^3 is a skyscraper). So

 (Theorem A) H^4_c(Y,K) has a filtration with pieces E_2^{0,4} and coker(d_2: E_2^{0,3} -> E_2^{2,2}). PROVED.

Reduction of E_2^{2,2} to monodromy (PROVED). For a constructible sheaf G on P^1 with open lisse part U_0 (a finite set removed, including infinity): H^2(P^1, G) = H^2_c(U_0, G|U_0) because a skyscraper sheaf has no H^1 and H^2. And H^2_c(U_0, lisse E) = (E_eta)_{pi_1(U_0)} (-1) (coinvariants of the geometric fundamental group; Poincare duality on a curve, SGA 4 XVIII 3.2.5). So

 E_2^{2,2} = (V tensor tau^*V)_{pi_1(U_0)} (-1).

This is the statement "coinvariants of V(r) tensor V(tau r)" of report I, now with a proof. It is dual to Hom_pi(V, tau^*V^vee).

## 3. Tameness of V (PROVED, new)

Claim: V is tame at every point of P^1_r, in particular at r = 0 and r = infinity. The proof uses only the Euler characteristic of the total space T.

(a) Cohomology of T (PROVED). Split T = U' union line, U' = {x != 0}, line = {x = 0}. On U' put y = r x: U' = G_m x A^1 with sheaf F|_{G_m} boxtimes F. Kunneth (CITED: SGA 4 XVII 5.4.3): H^*_c(U') = H^1_c(G_m,F) tensor H^1_c(A^1,F) in degree 2 only, dimension d(d-1). On the line x = 0 the sheaf is constant (t_0^2 = 1): H^*_c = Q_l(-1) in degree 2. The sequence of the closed line gives H^j_c(T) = 0 for j != 2, dim H^2_c(T) = d(d-1) + 1, so chi_c(T) = d^2 - d + 1 and **H^3_c(T) = 0**.

(b) Same Euler characteristic from p. chi_c(T) = chi_c(A^1, R^2 p_!) - chi_c(A^1, R^1 p_!). R^2 p_! is a skyscraper, stalk Q_l(-1) at each r in mu: chi_c = |mu|. For R^1 = V: generic rank 2d - 1, and by Grothendieck-Ogg-Shafarevich (CITED: Raynaud, Bourbaki 286 / SGA 5 X 7.1: chi_c(U,E) = rank chi_c(U) - sum of Swan conductors at the missing points of P^1, then add stalk dimensions at constructible points) chi_c(A^1, V) = (2d - 1) - sum_r (deficit at r) - Sw_total, deficit(r) = (2d - 1) - dim V_r. Deficits: d at r = 0; c_r - h^2_r at r != 0, summing to d^2 - |mu|. So chi_c(V) = d - 1 - d^2 + |mu| - Sw_total and chi_c(T) = d^2 - d + 1 + Sw_total.

(c) Compare with (a): Sw_total = 0. Every Swan conductor is >= 0, so all vanish: **V is tame at every point, including 0, the points of R', 1 and infinity.** CHECKED symbolically (sympy, output line D: difference of the two Euler characteristics is 0). The same holds for tau^*V and for V^vee; and R^2 pi_! K = V tensor tau^* V is tame.

This is the only place where wild ramification could have entered; it is now excluded without any weight argument.

## 4. The lemma of S-c, verified and corrected

Lemma (S-c, corrected form). Let A, B be lisse, tame at every finite point and at infinity, on open subsets of A^1 over F-bar; let S_A, S_B be their finite singular sets (finite points where they are not lisse). Suppose S_A and S_B are disjoint (no condition at infinity). On the common open U_0, every pi_1(U_0)-map phi: A -> B factors through A -> A_pi -> B^pi, where A_pi are the coinvariants and B^pi the invariants of pi_1(U_0). Hence Hom_pi(A, B) = Hom(A_pi, B^pi).

Proof (PROVED). For s in S_A, B is unramified at s, so every g in the inertia group I_s acts trivially on B and phi((g-1)v) = (g-1)phi(v) = 0. The kernel of phi is pi_1-stable, so it contains the submodule N generated by all (g-1)A, g in I_s, s in S_A. The quotient A/N has trivial action of all inertia groups at finite points of S_A; A is lisse at the points of S_B, so I_s acts trivially there too. So pi_1(U_0) acts on A/N through the quotient by the normal closure of all finite inertia, that is through pi_1(A^1) (kernel of pi_1(U) -> pi_1(X) = normal closure of inertia: SGA 1 V 8.2, number from memory). The action is tame at infinity, so it factors through the tame quotient pi_1^t(A^1), which is trivial: a connected tame finite etale cover Y -> A^1 of degree n has 2g_Y - 2 = -2n + (n - #fibre over infinity) <= -n - 1 by Riemann-Hurwitz (Hartshorne IV 2.4), forcing n = 1. So A/N is a trivial module, equal to A_pi, and the image of phi is a trivial submodule of B, so lies in B^pi. QED.

Corrections to the brief's wording: (i) disjointness is needed only at finite points: a common singular point at infinity does no harm, only tameness there is used; (ii) the lemma gives Hom = Hom(A_pi, B^pi), the two sides being coinvariants of A and invariants of B, both over the same group pi_1(U_0); since V is lisse on a bigger set than U_0, V_{pi_1(U_0)} = V_{pi_1(U_V)}.

Consequence (PROVED). If S and tau^{-1}(S) are disjoint (finite points) then
 (V tensor tau^*V)_pi dual to Hom_pi(V, tau^*V^vee) = Hom(V_pi, (tau^*V^vee)^pi), of dimension (dim V_pi)^2 (using (tau^*V^vee)^pi dual to (tau^*V)_pi, an isomorphic copy of V_pi since tau is an automorphism of A^1).
So E_2^{2,2} = 0 as soon as V_pi = 0.

## 5. The coinvariants V_pi (suggestion S-d, completed and corrected)

### 5.1 Reduction to the total space (PROVED)
V_pi(-1) = H^2_c(A^1, V) = E_2^{2,1} of the Leray sequence of p. In that sequence E_2^{a,b} is nonzero only for b = 1, 2, a = 0, 1, 2 (R^0 = 0; R^2 skyscraper; H^0_c(A^1, V) = 0 since H^1_c(T) = 0). The only differential reaching E_2^{2,1} is d_2: E_2^{0,2} -> E_2^{2,1}, and H^3_c(T) = 0 (section 3(a)) forces it to be surjective. So

 V_pi(-1) = E_2^{0,2} / E_infty^{0,2} = coker( H^2_c(T) -> prod_{rho in mu} H^2_c(T_rho) ), T_rho = {r = rho}.

The brief's S-d ("bounds H^3_c of the total space, hence the coinvariants") is therefore true only after this step: H^3_c(T) = 0 gives dim V_pi <= |mu| (the skyscraper is the source of d_2), not V_pi = 0. The product structure does not say whether d_2 vanishes; a computation of the restriction map is needed.

### 5.2 The restriction map on the open part (PROVED)
H^2_c(T) is generated by the image of H^2_c(U') = H^1_c(G_m,F) tensor H and one more class (lifting the generator of H^2_c(line)). I compute the part coming from U'. On U' the fibre T_rho meets U' in Delta_rho = {y = rho x} (closed in U'), and H^2_c(Delta_rho) -> H^2_c(T_rho) is an isomorphism (adding one point). The restriction H^2_c(U') -> H^2_c(Delta_rho) = Q_l(-1) is obtained by pulling back along the proper map (id, iota_rho): G_m -> G_m x A^1, iota_rho(x) = rho x: it sends a tensor b to <a, iota_rho^* b>, where the pairing H^1_c(G_m, F) x H^1(G_m, F) -> H^2_c(G_m, F tensor F) = Q_l(-1) is the Poincare duality pairing (perfect: F = j_* L is its own dual, SGA 4 XVIII 3.2.5), and iota_rho^* = iota^* sigma_rho, with iota^*: H^1(A^1,F) -> H^1(G_m,F) the restriction and sigma_rho the automorphism of H induced by x -> rho x (rho Z = Z, f(rho x) = rho^d f(x)). Note H = H^1_c(A^1, F) = H^1(A^1, F) (j_* F = j_! F and the monodromy at infinity is nontrivial: kernel and cokernel of "forget supports" vanish).
The map iota^* is injective: its kernel is H^1_{0}(A^1, F) = 0 by purity (H^i_{x}(F) = H^{i-2}(x, F_x(-1)) for lisse F, SGA 4 XVI), so iota^*(H) is a hyperplane of H^1(G_m, F) (dim d, against d - 1). Therefore the functionals a tensor b -> <a, iota^* sigma_rho b>, rho in mu, are linearly independent exactly when the operators sigma_rho (rho in mu) are linearly independent in End(H).

### 5.3 Count (PROVED, except the last case)
(i) mu = {1} (generic f): one functional, nonzero, so the restriction is onto Q_l(-1) and **V_pi = 0.** (This is the main case. No genericity of c, no irreducibility is used.)
(ii) mu cyclic of order m > 1. The sigma_rho form a representation of mu (after rescaling by constants, irrelevant for independence) on H. Lefschetz fixed point formula for an automorphism of prime-to-p order (CITED: Deligne-Lusztig 1976, Thm 3.2; SGA 4 1/2, Rapport 3.2): for rho != 1 the only fixed point in A^1 is 0, so tr(rho | H^*_c) = eps(rho) (the scalar by which rho acts on F_0), and tr(rho | H) = -eps(rho); tr(1|H) = d - 1. Hence the multiplicity of a character chi of mu in H is d/m - [chi = eps]. If d/m >= 3 (that is m < d, d/m odd) every character occurs, the sigma_rho are independent (the span of the operators has dimension equal to the number of distinct characters occurring) and **V_pi = 0.**
(iii) m = d (so Z is one mu_d-orbit, f = x^d - a, a != 0). Exactly one character (eps) is missing; the restriction from U' has corank 1, so dim V_pi <= 1 and I did not decide it by the product structure. Route to V_pi = 0 (HINT, not fully written): the x-line has the automorphisms x -> zeta x; V(r) is the sum over characters chi of mu_d of H^1_c(A^1_w, L_{(w-a)(sw-a)} tensor L_chi(w)), s = r^d. For chi = 1 this is the quadratic sum, equal to -chi(s) for s != 1 (PROVED, classical: sum over w of chi(alpha w^2 + beta w + gamma) = -chi(alpha) when the discriminant a^2 (s-1)^2 is nonzero), giving geometrically L_chi(r^d) = L_chi(r), the class at infinity. For chi != 1 a rank two sheaf W_chi on the s-line with local exponents (0 and -A - 3/2 at s = 0; -1/2 and A + 1 at infinity; integral and unipotent at s = 1, A the exponent of chi); a common eigenline compatible with the product of local monodromies is impossible (sum of exponents mod Z), so W_chi is irreducible with a nontrivial transvection at s = 1 (HINT for the local exponents), and an irreducible module whose group contains the normal closure of a nontrivial transvection has no trivial quotient, also after the degree-d Kummer pullback (the loops around the preimages of s = 1 lie in the normal subgroup). This gives V_pi = 0 for f = x^d - a, but the local-exponent claim is not proved here. Status: OPEN-detail. I list f = x^d - a as (X2).

Summary (Theorem C): V_pi = 0 for all f with mu = {1} or m < d, unconditional; for f = x^d - a, dim V_pi <= 1.

## 6. Theorem D, and what to add when the singular sets meet

Theorem D (PROVED). Let c_1 + c_2 + c_3 != 0, f not of the form x^d - a, and suppose there are no s, s' in S with c_2 + c_3 s + c_1 s' = 0. Then E_2^{2,2} = 0 and E_2^{0,4} = 0, so H^4_c(Y,K) = 0, so (S_4) holds: H^j_c(Y,K) = 0 for j != 3. If moreover mu = {1}, dim H^3_c = 4d^3 - 3d^2 + 4d - 1.
Proof. tau(s) = s' means -(c_3/c_1)(s + e) = s', that is c_2 + c_3 s + c_1 s' = 0. So the hypothesis is S disjoint from tau^{-1}(S): Lemma of section 4 and V_pi = 0 give E_2^{2,2} = 0. E_2^{0,4} = 0 because the pair (rho, rho') of Theorem B lies in S x S. The dimension: all other H^j_c vanish (lower half, Theorem A), so dim H^3_c = -chi_c(Y,K), which section 1 (CHECKED) gives as 4d^3 - 3d^2 + 4d - 1 for mu = {1} when the special points are distinct (this is the case when S meets tau^{-1}S nowhere). QED.

Theorem B (PROVED). E_2^{0,4} = sum over r in P^1 of H^4_c(Pi_r minus 0, K) has the stalk Q_l(-2) at r iff both factors L_chi(f(x) f(rx)) and L_chi(f(u) f(tau(r) u)) are geometrically trivial, that is r in mu and tau(r) in mu (the fibre r = infinity has factors t_0 L_f, never trivial). Such r = rho gives the plane {x_4 = rho x_2, x_1 = rho' x_3} in Y (Q vanishes there exactly when c_2 + c_3 rho + c_1 rho' = 0), on which K is geometrically trivial. E^{0,4} survives (no differential in or out, section 2), so H^4_c(Y,K) != 0 with Frobenius eigenvalues q^2 times roots of unity from chi(rho^d rho'^d)... PROVED for each such pair. For mu = {1} this reduces to c_1 + c_2 + c_3 = 0, which is Theorem 4 of report I, now seen as a special case.

### Case where the singular sets meet but X1 fails (X4 minus X1): reduction, OPEN
By the lemma's proof, a nonzero phi in Hom_pi(V, tau^*V^vee) has image Im that is a quotient of V and a sub of B = tau^*V^vee, unramified outside Sigma = S intersect tau^{-1}S. Hence a Jordan-Holder factor X of V is also one of B. V has the factors of L_{chi(r)} (rank one, ramified at 0) and of W (all of W, if W is irreducible); B has those of L_{chi(tau r)} (ramified at tau^{-1}(0) = -e != 0, so L_chi(r) is not one of them since e != 0) and of tau^*W^vee. Assume mu = {1} and
- (Irr) W is irreducible;
- (Loc0) the local monodromy T_0 of W at r = 0 has eigenvalue -1 (HINT: stable reduction as r -> 0: the curve y^2 = f(x) f(rx) splits into the x-cluster, with constant monodromy, and the cluster of roots z/r that run to infinity, which after x = u/r carries the twist chi(r^{-d}) = chi(r); so T_0 on V has eigenvalue -1 with multiplicity d and +1 with multiplicity d - 1, and on W the same with multiplicity d - 1 each. The monodromy of W at all finite s != 0 is unipotent, product of Picard-Lefschetz transvections, CITED SGA 7 XV.)
Then a common factor must be W isomorphic to tau^*W^vee (L cannot occur, rank). But T_0 on tau^*W^vee is the monodromy of W^vee at tau(0) = -c_2/c_1 != 0, unipotent, while T_0 on W has the eigenvalue -1: contradiction. So Hom_pi = 0 and E_2^{2,2} = 0 for every c.
**Conditional Theorem (OPEN).** If mu = {1}, (Irr) and (Loc0) hold, then H^4_c(Y,K) = 0 for all c with c_1 + c_2 + c_3 != 0, with no exceptional line at all.
What I did not prove: (Irr): the weight-free argument (SGA 7 XVIII 6.6 style: a submodule of the vanishing space containing a vanishing cycle contains all conjugates; a submodule containing none is orthogonal to all vanishing cycles by the transvection formula; perfect cup-product pairing) needs that the vanishing cycles at the different points z'/z are conjugate in the monodromy group, which in characteristic 0 follows from the braid relation between half twists along arcs sharing one endpoint (the pairs (z_i, z'_j/r) form a connected bipartite graph); I did not write this, nor the passage to characteristic p. (Loc0): the two-scale analysis is standard but not written. Both are HINT-level here.

d_2 (explicitly). In every case where E_2^{2,2} = 0, d_2: E_2^{0,3} -> E_2^{2,2} is irrelevant. E_2^{0,3} is a skyscraper (stalk of rank dim V(tau rho) at r = rho in mu, resp. dim V(rho) at tau^{-1}(rho)) and could only matter where E_2^{2,2} != 0, which only happens in X4 minus X1 or for f = x^d - a: not decided; in X1 the class E^{0,4} is nonzero anyway.

## 7. The exceptional list, complete

All conditions are on c in (F-bar^*)^3 (equivalently on (c_1 : c_2 : c_3)); c_1 + c_2 + c_3 != 0 assumed unless said. Let S, mu, R' as in section 0.

| id | condition | consequence | status |
|---|---|---|---|
| X0 | c_1 + c_2 + c_3 = 0 (tau(1) = 1) | H^4_c != 0, eigenvalue q^2, (S_4) fails | PROVED (report I, Theorem B) |
| X1 | exists rho, rho' in mu with c_2 + c_3 rho + c_1 rho' = 0 | same, one q^2-class per pair | PROVED (Theorem B); contains X0; new only if mu != {1} |
| X2 | f = x^d - a, a != 0 (mu = mu_d) | dim V_pi <= 1; if V_pi != 0 then E_2^{2,2} = (V_pi tensor V_pi')(-1) != 0 unless killed by d_2 | OPEN (HINT: V_pi = 0) |
| X4 | exists s, s' in S with c_2 + c_3 s + c_1 s' = 0 | singular sets of V and tau^*V meet at s (resp. tau(s) = s'); lemma does not apply | OPEN (Conditional Theorem: vanishes if (Irr), (Loc0)) |
| none | none of the above | H^4_c = 0, (S_4) holds | PROVED (Theorem D) |

Content of X4, case by case (all finite sets are subsets of F-bar):
- s = 0, s' != 0 (the point 0 of V meets tau^{-1}(S)): c_2/c_1 = -s', s' in R', that is tau(0) = -c_2/c_1 in R'.
- s != 0, s' = 0: -e = -c_2/c_3 = s in R' (tau^{-1}(0) = -e in R').
- s, s' in R' both nonzero: c_2 + c_3 s + c_1 s' = 0 with s = z'/z, s' = w'/w.
- s = 0 = s' would force c_2 = 0, excluded.
- s = s' = 1: X0.
Number: at most |S|^2 - 1 <= (d^2 - d + 2)^2 - 1 lines in P^2 (63 for d = 3), a proper closed subset; over F_q a line of F-bar-coordinates with s, s' not in F_q has at most one rational point, so for q large rational c avoid the set except for the lines defined over F_q.
Not exceptional (checked): r = infinity (tau(infinity) = infinity is always common to both singular sets, but both sheaves are tame there, section 3); the points r = 0 and r = -e as such (they enter only through s = 0 and s' = 0 above).

Statement about the special points requested in the brief:
- r = 0 and r = -e: V has stalk d - 1, local monodromy of finite order on the part twisted by chi(r) (HINT, Loc0), ramified; tau^*V has the same at r = -e. Handled by 0 in S.
- r = infinity (fibre [0:1]): both factors t_0 L_f, stalk (d-1)^2, not special for the coinvariants; tame (section 3).
- r = 1 (and rho in mu): stalk d (d in mu case), local monodromy a product of d commuting transvections (unipotent); this is the point responsible for X0, X1.
- ratio points z'/z: stalk 2d - 1 - c_r, one transvection per collision, unipotent.

## 8. Consistency with the exact data

Weights are used in this section only to interpret numbers: a class with Frobenius eigenvalue q^2 shows up as N_4 ~ +q^2; the 92 (resp. more) classes of H^3_c give N_4 of size at most 92 q^{3/2} if they have weight <= 3.

CHECKED (`k4t_checks.py`, output `k4t_checks_out.txt`; exact integer N_4 from the formula of section 1):
- Generic c, generic f: N_4/p^2 is small and of both signs; existing data (report I, B, C): N_4 of size p^{3/2} for generic c. Consistent with Theorem D (no q^2 class) and with dim H^3_c = 92.
- X0 (c_1 + c_2 + c_3 = 0): N_4/p^2 near 1 (report I data; also in my table E, third row: means 0.71 to 1.24 for p = 13 to 127, f = x^3 - a).
- X1 with mu = mu_3 (f = x^3 - a, p = 1 mod 3, a = 1..8): for c = (1, -1 - w, 1) (pairs (rho, rho') = (w, 1) and (1, w)) and for c = (1, 1, 1) (pairs (w, w^2), (w^2, w)) the mean of N_4/p^2 is 1.50 to 2.28 for p = 13 to 127, about TWO, as predicted by two planes; for c = (1, 1, -2) (only the pair (1, 1)) about ONE. Not the generic value near 0. (Output E.) Table E, p = 7 is polluted by an accidental extra pair ((1,2,3) mod 7 lies on an X1 line), harmless.
- X4 minus X1 for generic f (roots in F_p, c on the lines c_2 + c_3 s + c_1 s' = 0, s, s' in S, (s, s') != (1, 1), 24 cases for each of p = 31, 61, 101, 131): the means of N_4/p^2 are 0.16, 0.06, -0.02, 0.10, against 0.16, 0.05, -0.03, 0.01 for random c (output F). No q^2 trend, as predicted. This does not test E_2^{2,2}: a class there would have eigenvalue of size about q, far below the noise.
- Total space: sum_r C(r) = M^2 - t_0 M + q for 150 cases (p up to 103, d = 3, 5): 0 failures (output B). This is the exact point count of T, consistent with H^2_c(T) of dimension d(d-1) + 1 containing the eigenvalue q of the line x = 0, and it is the basis of the zero Swan count.
- Euler characteristics (sympy): chi_c(Y,K) = -4d^3 + 3d^2 - 4d + 1; chi_c(T) from p equals d^2 - d + 1, the total Swan conductor is 0 (output C, D).

The k = 4 data in the toy-case folder give no instance contradicting Theorem D; none could, since Theorem D is a vanishing statement about a class of size at most q^2.

## 9. Standard facts used, with citations

All CITED from memory; numbers need a check against the primary texts.
1. Kunneth for H_c: SGA 4 XVII 5.4.3 (Deligne). Proper base change: SGA 4 XII 5.1.
2. Grothendieck-Ogg-Shafarevich / Euler-Poincare on a curve: Raynaud, "Caracteristique d'Euler-Poincare d'un faisceau et cohomologie des varietes abeliennes", Seminaire Bourbaki 286 (1965); SGA 5 X 7.1. Swan conductor >= 0, = 0 iff the wild inertia acts trivially (Serre, Local Fields, ch. 6; Katz, GKM 1.9).
3. Poincare duality on curves: SGA 4 XVIII 3.2.5. Purity for a point on a smooth curve: SGA 4 XVI / SGA 4 1/2.
4. Kernel of pi_1(U) -> pi_1(X) is the normal closure of inertia: SGA 1 V 8.2 (tame version XIII).
5. Riemann-Hurwitz, tame case: Hartshorne, Algebraic Geometry, IV 2.4. Gives pi_1^t(A^1) = 1.
6. Lefschetz fixed point formula for automorphisms of prime-to-p order: Deligne-Lusztig, Representations of reductive groups over finite fields, Ann. Math. 103 (1976), Thm 3.2; SGA 4 1/2, Rapport.
7. Picard-Lefschetz formula for nodal degenerations (in HINT only): SGA 7 XV (Deligne), irreducibility of vanishing cohomology: SGA 7 XVIII 6.6 (Katz) (not used in any PROVED statement).
8. Artin vanishing lower half: report I, Proposition 1; round-one result, not re-proved here.

Not used: purity, Weil conjectures, the Weil bound, Hodge theory.

## 10. Verdict and what remains

- For k = 4 the sign statement (S_4) is now proved weight-free outside an explicit finite union of lines in c-space (X4, containing X1 and X0) and f not of the form x^d - a. In the same range dim H^3_c(Y,K) = 4d^3 - 3d^2 + 4d - 1 for mu = {1}.
- It FAILS on X1 (planes; X0 is the special case seen by report I) and the failing locus is larger than c_1 + c_2 + c_3 = 0 for f with a multiplicative symmetry (mu != {1}); this is a new exceptional condition for the computing agents' maps of the bad set: **for f = x^3 - a the bad set contains the lines c_2 + c_3 rho + c_1 rho' = 0, rho, rho' cube roots of unity (nine lines); data confirm (section 8).**
- Open: (a) X4 minus X1 when mu = {1} (needs (Irr) and (Loc0); my reduction shows it is the only remaining step and that it is a monodromy statement about one family on the line); (b) f = x^d - a (one class, V_pi, possibly nonzero); (c) d_2 in the exceptional cases. The proof of vanishing needs no weights, so it is not circular; it uses the special geometry of k = 4 (a family of planes over a line, tame fundamental group of the affine line trivial). Whether anything similar exists for k >= 5 is OPEN; I make no claim (HINT only: the base of such a fibration has dimension >= 2).
- Relation to the claim "weights are needed": in this case the statement V_pi = 0 and the lemma replace any use of purity or irreducibility; the price is the finite exceptional set. This says nothing about k >= 5 and does not by itself make the route a proof of the Weil bound: (W*) needs the input for infinitely many k.
