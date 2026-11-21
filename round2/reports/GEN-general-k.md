# GEN. General even k (round two)

Scope: character sums over finite fields, where Weil (1948) is a theorem. The question is only whether the route of the note is a valid proof and what it needs. Nothing here concerns the Riemann Hypothesis for the integers, and nothing here is evidence about it.

Labels: PROVED (full argument given), CITED (author, title, year, statement; theorem numbers from memory unless marked), CHECKED (exact integer or rational arithmetic, script and output named), OPEN, HINT. No proof uses weights, purity, the Weil bound or the Weil conjectures. Weight language appears only where marked "(interpretation)".

Files: compute/GEN/matchings.py (output matchings_out.txt), compute/GEN/cavg.py (output cavg_out.txt). Both ran as one process at below-normal priority, a few minutes at most.

Notation: Q = q^m is the field of definition of c, so c in (F_Q^*)^(k-1) and the counts N_n(c) are over F_(Q^n). M_n = -sum alpha_i^(mn) over F_(Q^n). Y, K, N, R, T, R^b as in the brief and in RED. B = Q^((k+3)/2). R_n = Q^n N_n - M_n^k, and |R_n| <= C B^n (iterated Parseval, round one).

## 0. Result in one page

1. PROVED (modulo CITED weight-free inputs listed in 1.1): for every even k, f, and c with all c_i != 0, H^j_c(Y,K) = 0 unless j in {k-1, k, k+1}; in the trace formula H^(k-1) and H^(k+1) carry the sign (-1)^(k-1), only H^k carries the opposite sign. This is what the first-phase reports give together, after re-checking the dependencies (section 1). Exactly one thing remains open about Y: whether H^k_c(Y,K) can contain the eigenvalue alpha_*^k / Q with large multiplicity. It is known to vanish for k = 4 outside an explicit finite union of lines (K4T Theorem D), and to be nonzero on the lines X1.
2. NEW, PROVED given one input (section 3): the route does not need (S_k) or (W*) at all. It needs only
   (P_k) H^(k+1)_c(A^k_{F-bar}, F_h) = 0 for generic h, equivalently R^(k+1) is a punctual sheaf on G_m.
   Proposition X: if (P_k) holds, then |alpha_*|^(mk) <= Q^((k+3)/2) for any c with all c_i != 0, that is |alpha_*| <= q^(1/2 + 3/(2k)). The reason: a wrong-parity class that cancels alpha_*^k has to be a constant quotient of R^k with Frobenius eigenvalue of modulus above Q^((k+1)/2), and Parseval at a generic fixed h forbids such an eigenvalue when R^(k+1)_h = 0.
3. HINT, high risk, written out so that it can be refereed (section 4): a stationary-phase bookkeeping of the tame inertia characters of P_i at infinity gives a period-4 pattern, with a trivial character present only for i = 3 mod 4. If that bookkeeping is right, (P_k) holds for every even k, for every c, and the route is a complete weight-free proof of |alpha| <= sqrt(q) for y^2 = f(x). I have not checked it against Laumon's text (his sections 2.3.3 and 2.5 were not opened by anyone), nobody else has seen it, and it is much stronger than anything the first phase suggested. Treat it as a claim to be attacked, not as a result.
4. PROVED (section 2): for k >= 6 no coordinate-matching linear subspace of dimension k/2 lies in Y for any c in (F-bar^*)^(k-1), for any f, with any scalars or shifts. The k = 4 failure mechanism (planes, Theorem B of K4T) is special to k = 4. CHECKED for k <= 12 (matchings_out.txt).
5. The exponent argument survives the passage to F_(q^m) with no dependence of the exponent on m (section 2.3). Only the constants and the requirement Q >= Q_0 depend on m.
6. PROVED (section 3.4): a plane-type or any Tate-type class of eigenvalue modulus q^(k/2) can cancel alpha_*^k only for at most one value of k. Supersingular-type (alpha^s = q^r) is handled by Proposition X without any such discussion, if (P_k) holds.

## 1. The strongest general statement proved by the first phase

### 1.1 Dependencies I re-checked and what I rely on

I did not re-derive RED or FS. I re-read their arguments and checked that they hang together with K4T and the main-session note. The inputs that are CITED and used (all weight-free according to LIT, which grepped Laumon chapter 1 and the Katz-Laumon appendix and found no weights; Laumon chapters 2-4 were NOT opened):
- (I1) Artin vanishing and perverse t-exactness: BBD 4.1.1, 4.1.2 (opened by LIT).
- (I2) Kunneth for H_c and proper base change: SGA 4 XVII 5.4, XII 5.1.
- (I3) Fourier transform preserves perverse sheaves on A^1 and commutes with base change in the sense used by RED claim 3: Laumon 1987 1.3.1.1, 1.3.2.3 (opened by LIT); Katz-Laumon 1985 2.1.3.
- (I4) Leray spectral sequence, Grothendieck-Lefschetz trace formula.

### 1.2 Theorem G (general even k, any c with all c_i != 0)

(a) PROVED (FS S-a, RED claim 2 lower half, main session): H^j_c(Y,K) = 0 for j < k-1.
(b) PROVED given I1-I3 (RED claim 4): H^j_c(Y,K) = 0 for j >= k+2. Corroborated independently at k = 4 by K4T Theorem A (H^5_c = H^6_c = 0 by a different fibration), and at k = 2, 3 by round one.
(c) PROVED (RED 2.3 and claim 5(c)): in R = sum_m (-1)^m tr H^m_c(G_m x A^k, F) the k-fold products of eigenvalues (the space T) enter with sign (-1)^(k+1), as do H^(k-1)_c(Y,K)(-1) and H^(k+1)_c(Y,K)(-1); only H^k_c(Y,K)(-1) enters with sign (-1)^k. For even k: T, H^(k-1), H^(k+1) enter with sign minus, H^k with sign plus.
(d) PROVED (RED 5.3, 5.4): the Leray structure over h: classes of H^k_c(Y,K)(-1) are of two kinds: the quotient of (R^k_eta)_(pi_1)(-1) by the image of d_2 from punctual sections of R^(k+1), and H^1_c(G_m, R^(k+1)).

### 1.3 What remains open, stated exactly

(S_k') H^k_c(Y,K) = 0, or the weaker (W*): the eigenvalue alpha_*^k/Q does not occur in H^k_c(Y,K) with multiplicity m_k >= m_T + m_(k-1) + m_(k+1), where m_T >= (number of i with alpha_i^m = alpha_*^m)^k >= 1. Known: (S_4) holds outside X4 union X2 (K4T Theorem D, proof uses CITED SGA 4 results and no weights; I did not re-derive it), fails on X1 (Theorem B). Nothing is proved for k >= 6 beyond Theorem G.

Section 3 shows that neither (S_k') nor (W*) is the right target.

## 2. The bad set; existence of good c; passage to F_(q^m)

### 2.1 k = 4, exactly (from K4T, NUM M1, K4C; I rely on them, re-derivation not repeated)

Let mu, R', S, X0, X1, X2, X4 be as in K4T section 0 and 7.
- PROVED bad: X1 (a pair rho, rho' in mu with c_2 + c_3 rho + c_1 rho' = 0), containing X0 (c_1 + c_2 + c_3 = 0). H^4_c != 0, eigenvalue q^2 times a root of unity.
- PROVED good: outside X4 union X2, H^4_c(Y,K) = 0, (S_4) holds (K4T Theorem D).
- OPEN: X4 minus X1 (conditional on W irreducible and eigenvalue -1 at r = 0) and f = x^d - a.
- For f with mu = {1} the proved-bad set is the single plane c_1 + c_2 + c_3 = 0. CHECKED by NUM M1 (m1c_all_primes.txt: 2677 of 2694 such vectors have N/p^2 >= 1/2, p <= 73) and K4C E1 (592 of 592 formula checks).

### 2.2 k >= 6: no coordinate-matching plane (new, PROVED; CHECKED to k = 12)

Claim. Let k = 2s >= 6. For no c in (F-bar^*)^(k-1) and no f does Y contain a linear subspace of dimension s of the form {x_j = a_(ij) x_i + b_(ij) for the pairs (i,j) of a perfect matching of {1..k}} (a_(ij) != 0 scalars, b_(ij) arbitrary).
Proof. On such a subspace with coordinates y_A, one per pair A, the quadratic part of Q_c is sum over classes {A,B} of (sum of c_e a-factors over the edges e = (e, e+1) joining pair A to pair B) y_A y_B, plus c_e a y_A^2 for an edge inside one pair. For Q_c to vanish identically each class must have zero coefficient. An edge inside a pair, or a class consisting of one edge, gives a coefficient c_e times a nonzero scalar, which is nonzero. So every class has at least two edges and no edge is inside a pair. The k-1 = 2s-1 edges of the path form a walk w_1..w_k on the s pairs in which each pair occurs exactly twice. Distinct classes number at most (2s-1)/2, so at most s-1; the walk is connected and covers s vertices, so exactly s-1 classes, forming a tree T_0, and the multiplicities are 2 on s-2 edges and 3 on one edge. For a vertex v, the number of edge-ends of the walk at v is 4 minus the number of endpoints of the walk lying at v (each visit contributes 2, an endpoint 1). A leaf v of T_0 has edge-ends equal to the multiplicity of its edge, 2 or 3. A leaf with multiplicity 2 needs both endpoints of the walk; a leaf with multiplicity 3 needs exactly one endpoint. If s >= 3, T_0 has at least two leaves on different edges. Two leaves cannot both have multiplicity 3 (only one such edge exists); a leaf with multiplicity 2 uses both endpoints, leaving none for the other leaf, which then has edge-ends 2 or 3 but needs 4 or 3 minus an endpoint, impossible. Contradiction. For s = 2 the tree is one edge of multiplicity 3 and the matching {1,3},{2,4} works with c_1 + c_2 + c_3 = 0 (when all a = 1). QED.
CHECKED (matchings.py, matchings_out.txt): perfect matchings 3, 15, 105, 945, 10395 for k = 4, 6, 8, 10, 12; admissible (no inside edge, no singleton class) 1, 0, 0, 0, 0. For k = 4 over F_q^*, the vectors on the plane c_1 + c_2 + c_3 = 0: 2/8, 12/64, 30/216, 90/1000 for q = 3, 5, 7, 11, (these equal (q-1)(q-2) restricted to c_3 != 0 and c_1+c_2+c_3 = 0 in F_q^*: 2, 12, 30, 90, as the output shows).
Consequences. (i) The mechanism of K4T Theorem B (a coordinate plane in Y on which K is geometrically trivial, giving a class q^(k/2) in H^k_c) does not exist for any k >= 6. This explains NUM M2's observation that at k = 6 the only plane-like family has c_3 = 0 (outside the torus). (ii) Subvarieties of dimension k/2 in Y on which K is geometrically trivial and which are not of coordinate-matching linear type are not excluded (HINT: none known). (iii) The statement in round-one notes that "genericity of c fails once k is of order log q" at fixed q (report H) is not supported by this mechanism: since no matching plane exists for k >= 6, no vector in (F_q^*)^(k-1) is excluded by planes. What else could exclude c at fixed q is OPEN.

### 2.3 Good c exist in some extension; the exponent argument survives; exact dependence on m

k = 4 (PROVED, given K4T Theorem D): we may translate x so that f(0) != 0 and f is not of the form x^d - a: the translate f_b(x) = f(x + b) has mu(f_b) != {1} iff b is the fixed point of an affine automorphism of Z with multiplier != 1, and the group of affine automorphisms of Z acts faithfully on Z (d >= 2 points determine an affine map), so at most d(d-1) values of b are excluded, plus the d values with f(b) = 0. Then c must avoid at most L = (d^2 - d + 2)^2 - 1 planes (X4 lines in the plane of (c_1:c_2:c_3)), each containing at most Q^2 points of F_Q^3. Since (Q-1)^3 > L Q^2 once Q >= L + 3, a good c in (F_Q^*)^3 exists for every Q = q^m >= max(L + 3, d^2 + 1). This is an m of size log_q(L + 3), depending on d only. If the planes are not defined over F_Q they have fewer rational points; the bound is an upper bound.
Every k (conditional): the set of c in G_m^(k-1) where a given constructible condition on H^k_c(Y_c,K) holds is constructible by generic base change; if its complement is a proper closed subset Z_k, it lies in a hypersurface of some degree D(k) defined over F_(q^a(k)), and Schwartz-Zippel gives a good c in F_Q^(k-1) as soon as Q > D(k) + 1 and a(k) | m. So m = m(k, f) exists iff the generic fibre is good. Without such a statement (OPEN for k >= 6), existence of a good c is not proved. If instead the route is run with Proposition X (section 3), no condition on c beyond c_i != 0 is needed and any c in (F_Q^*)^(k-1) with Q >= 3 works (it needs the existence of one h in F_Q^* outside a finite exceptional set, so Q large).
At fixed q (no extension), c in (F_q^*)^(k-1): not needed and not claimed. CHECKED data on fractions of vectors in the plane condition: matchings_out.txt.

Exponent argument over F_Q (PROVED, steps 1, 2, 3, 5 of the note with F_q replaced by F_Q): the eigenvalues over F_Q are the alpha_i^m; N_n is counted over F_(Q^n); psi is composed with the trace to F_p and chi with the norm. Parseval gives |S_n(h)| <= (Q^n - r_n) Q^(n(k-1)/2) for each h in F_(Q^n)^*, so |R_n| <= (Q^n - 1)(Q^n - r_n) Q^(n(k-1)/2) < Q^(n(k+3)/2). If the coefficient of gamma_* = alpha_*^(mk) in the unique expansion of R_n is nonzero, no_hidden_growth gives |alpha_*^(mk)| <= Q^((k+3)/2) = q^(m(k+3)/2), so |alpha_*|^k <= q^((k+3)/2) and |alpha_*| <= q^(1/2 + 3/(2k)). The exponent does not depend on m. Dependence on m: only the constant C_Q = (Q-1)(Q - r_Q) and the need for Q >= Q_0(k, f). Distinct alpha_i with equal alpha_i^m merge into one gamma; under (S_k') all merged terms have the same sign, so merging cannot cause cancellation; under Proposition X the coefficient has the sign (-1)^(k+1) and modulus at least 1 for the same reason.

## 3. What the argument really needs

### 3.1 The coefficient of alpha_*^k, exactly

Let gamma_* = alpha_*^(mk), the largest modulus among k-fold products (alpha_*^m of largest modulus). In the virtual representation V_R = sum_(a,b) (-1)^(a+b) [H^a_c(G_m, R^b)] (Leray, valid at the level of virtual representations whatever the differentials), with b in {k, k+1}, a in {0,1,2}:
- sign (-1)^(k+1): H^1_c(G_m,R^k), H^0_c(G_m,R^(k+1)), H^2_c(G_m,R^(k+1)). T lies among H^1_c(G_m,R^k) and H^0_c(G_m,R^(k+1)) at the E_infinity level, so these carry at least m_T >= 1 copies of gamma_*.
- sign (-1)^k: H^0_c(G_m,R^k) = 0 (RED 5.1), H^2_c(G_m,R^k) = (R^k_eta)_(pi_1)(-1) with eigenvalues Q * gamma_A (gamma_A an eigenvalue of Frobenius on the geometrically constant quotient of R^k), and H^1_c(G_m,R^(k+1)).
So the coefficient r_(gamma_*) is zero only if the opposite-sign classes (2,k) and (1,k+1) contain gamma_* with total multiplicity at least that of the same-sign classes, which is at least m_T >= 1. (The d_2 differential from E^(0,k+1) to E^(2,k) changes E_2 to E_infinity but not the virtual count.)

### 3.2 Proposition X (PROVED, given I1-I4 and the lemmas of RED claims 1-4)

Let k be even (the same holds for odd k with signs swapped), c with all c_i != 0, Q = q^m with F_Q large enough that U_0(F_Q) is nonempty. Assume (P_k): R^(k+1) is a skyscraper sheaf on G_m (equivalently H^(k+1)_c(A^k, F_h) = 0 for h outside a finite set). Then |alpha_*^m|^k <= Q^((k+3)/2).
Proof. Suppose |gamma_*| > B = Q^((k+3)/2). Then r_(gamma_*) = 0 by the bound |R_n| <= C B^n and no_hidden_growth. By 3.1 a class of opposite sign must carry gamma_*. (1,k+1) is H^1_c of a skyscraper, which is 0. (2,k) is (R^k_eta)_pi(-1): it would give an eigenvalue gamma_A = gamma_*/Q of Frobenius on a geometrically constant quotient of R^k. Because the quotient is geometrically constant, Frobenius at every rational point h of the lisse locus U_0 acts on it as one fixed operator, so gamma_A is an eigenvalue of F_h on R^k_h for every h in U_0(F_(Q^n)), with the n-th power. Take h in U_0(F_Q) outside the finite set where R^(k+1)_h != 0. Then S_n(h) = (-1)^k tr(F^n | R^k_h) exactly, with positive multiplicities. By Parseval |S_n(h)| <= Q^(n(k+1)/2) for all n, so every eigenvalue of F_h on R^k_h has modulus at most Q^((k+1)/2) (no_hidden_growth with positive coefficients, no cancellation possible). Hence |gamma_A| <= Q^((k+1)/2) and |gamma_*| = Q |gamma_A| <= Q^((k+3)/2) = B, contradicting |gamma_*| > B. So no opposite-sign class carries gamma_*, the coefficient r_(gamma_*) has the sign (-1)^(k+1) and modulus >= m_T >= 1, a contradiction with r_(gamma_*) = 0. QED.
Remarks. (i) The sign statement (S_k) is not used. The classes that make (S_k) fail (the q^2 class at k = 4 on X0) have modulus Q^(k/2) < Q^((k+1)/2) and are irrelevant. (ii) The argument is tight at the threshold: the Parseval bound on R^k_h is Q^((k+1)/2) and the summation over h gives the extra factor Q, exactly B. (iii) Special h where R^(k+1)_h != 0 contribute to H^0_c(G_m, R^(k+1)), same sign as T. (iv) This sharpens RED's open item 1 ("R^(k+1) punctual is needed in addition to the coinvariant statement"): it is in fact sufficient by itself. (v) Nobody has checked this proposition independently; the places where an error could hide are the identification of the Frobenius action on the geometrically constant quotient and the use of E_2 versus E_infinity in the virtual count.

### 3.3 Which eigenvalues occur in the wrong-parity cohomology

From RED (5.3) and the above, the eigenvalues of H^k_c(Y,K) are of two types.
- Type A: eigenvalues gamma_A of Frobenius on geometrically constant quotients of R^k (cokernel of d_2 from punctual sections of R^(k+1)). Each is an eigenvalue of F_h on H^k_c(A^k, F_h) for every h in the lisse locus, hence an algebraic integer and, if R^(k+1)_h = 0 at some h, of modulus at most Q^((k+1)/2) (PROVED, Parseval). Known members: the class q^2 (up to root of unity) of the planes at k = 4 (X1). For k >= 6 no matching-plane class exists (2.2).
- Type B: eigenvalues of H^1_c(G_m, R^(k+1)). Nonzero only if R^(k+1) has positive generic rank; then no bound from Parseval alone.
Can alpha_*^k / Q be one of them for infinitely many k?
- If (P_k) holds for those k: no, by Proposition X, once |alpha_*|^(mk) > Q^((k+3)/2).
- Unconditionally, for Tate-type classes of modulus exactly q^(j): PROVED weight-free that a class of eigenvalue modulus Q^(k/2) (the plane-type class, a Tate twist Q_l(-k/2) times a root of unity) can cancel alpha_*^(mk) only if |alpha_*|^(mk) = Q^(k/2 + 1), i.e. |alpha_*|^k = q^(k/2 + 1); for a fixed alpha_* at most one k satisfies this (write |alpha_*| = q^(1/2 + delta): k delta = 1). So plane-type classes never cancel for infinitely many k, and for k >= 6 they do not exist at all.

### 3.4 The supersingular case

Suppose alpha_*^s = zeta q^r (a root of unity zeta, integers r, s > 0). Then |alpha_*| = q^(r/s). If r/s <= 1/2 there is nothing to prove. If r/s > 1/2, then for k = s l the target alpha_*^k / q = zeta' q^(rl - 1) has the shape of a Tate-type eigenvalue, so the worry in the main-session note is structurally legitimate: such a class cannot be excluded by its form. What excludes it is its size: j_k = rk/s - 1 > k/2 - 1 + delta k with delta = r/s - 1/2 > 0, so |gamma_*| = |alpha_*|^(mk) = Q^(k/2 + k delta) exceeds B = Q^(k/2 + 3/2) as soon as k delta > 3/2. Proposition X then excludes it for those k, if (P_k) holds. Without (P_k) I have no weight-free exclusion; a class of Tate type with exponent above k/2 in degree k is excluded by weights only (interpretation).

### 3.5 An exact c-average (CHECKED, PROVED by counting), and what it does and does not show

For fixed x write u_i = x_i x_(i+1) and j(x) = number of i with u_i != 0. The number of c in (F_Q^*)^(k-1) with sum c_i u_i = 0 is [(Q-1)^(k-1) + (-1)^j (Q-1)^(k-j)] / Q. Hence
 sum over c of Q N_c = (Q-1)^(k-1) M^k + Theta, Theta = sum over x of t(x_1)...t(x_k) (-1)^(j(x)) (Q-1)^(k-j(x)),
and so sum over c of R_c = Theta, evaluated by a two-state transfer matrix. CHECKED (cavg.py, cavg_out.txt): exact equality with brute force in 6 of 6 cases (k = 4, 5, 6; p = 5, 7; two cubics). Size: Theta is at most about Q^k |M|^(k/2) (patterns with at most ceil(k/2) nonzero coordinates dominate), far smaller than the pointwise Parseval size Q^(k+1) Q^((k-1)/2) of sum_c R_c for k >= 6. Consequence (PROVED): for even k >= 6 and |alpha_*| > sqrt(q), the exponential Q^(k-1) alpha_*^k occurs in n -> sum over c in (F_(Q^n)^*)^(k-1) of Q^n N_c(n) with coefficient exactly m_T, because no exponential of Theta or of the lower binomial terms of (Q-1)^(k-1) M^k can have that modulus (comparison above, valid for k >= 6). What it does NOT show: nothing follows for an individual c, since the c-average ranges over c in F_(Q^n) and not over a fixed c. HINT only: this coefficient can be carried by non-constant constituents of the family (degrees a < 2k-2 over the c-torus) and does not imply that every generic c is bad; I did not decide this. I record it because it is an exact, weight-free handle on the c-direction, which may serve in a different attack on (W*).

## 4. Where (P_k) comes from: stationary-phase bookkeeping (HINT, high risk)

Setup (RED claim 3, PROVED given I3): P_1 = L[1], P_(i+1) = L tensor [h c_i]^* FT(P_i), each P_i perverse on A^1, and H^m_c(A^k, F_h) = H^(m-k)_c(A^1, P_k). Then H^(k+1)_c(A^k,F_h) = H^1_c(A^1,P_k) = coker(H^0_c(A^1, H^0 P_k) -> H^2_c(A^1, H^(-1) P_k)), and H^2_c(A^1, H^(-1) P_k) is the coinvariants of the geometric fundamental group of the lisse locus on the generic stalk, a quotient of the coinvariants of the inertia group at infinity. So H^(k+1)_c = 0 whenever the inertia representation of H^(-1) P_k at infinity has no trivial constituent (tame part without the trivial character; wild parts have no coinvariants). PROVED.
Bookkeeping (CITED from memory: Laumon 1987, stationary phase 2.3.3.1, local transforms F^(0,infty'), F^(infty,0') with F(K_chi) = K_(chi-bar) times a Gauss sum for chi != 1, and the trivial character mapped to the trivial character; I did not open these). Let t_i = set of tame characters of the inertia at infinity of H^(-1) P_i, and m_i = the set of characters of the vanishing cycles of P_i at 0. Facts used: (1) the inertia at infinity of FT(P) is the sum over finite singular points s != 0 of L_psi(s y) tensor tame pieces (wild, slope 1) plus the tame piece F^(0,infty')(vanishing cycles at 0), when P has no slope above 1 at infinity (true here); (2) the vanishing cycles of FT(P) at 0 are F^(infty,0')(tame part of P at infinity, slopes < 1); (3) L is unramified at 0 (f(0) != 0) and at infinity has character chi_2 (d odd). Then
 t_1 = {chi_2}, m_1 = {}; and t_(i+1) = chi_2 tensor F^(0,infty')(m_i), m_(i+1) = F^(infty,0')(t_i),
which gives (all characters are 1 or chi_2, self-inverse):
 i = 1: t = {chi_2}, m = {}
 i = 2: t = {}, m = {chi_2}
 i = 3: t = {1}, m = {}
 i = 4: t = {}, m = {1}
 i = 5: t = {chi_2}, m = {}
 and the pattern repeats with period 4. The trivial character occurs in t_i only for i = 3 mod 4, so (P_k) would hold for every even k, for every k = 1 mod 4 and k = 0, 2 mod 4, and fail possibly only at k = 3 mod 4. Consistency: i = 2 gives R^3 = 0 (RED k = 2: tame part of FT(P_1) at infinity vanishes since f(0) != 0); i = 3 reproduces RED's remark that the necessary condition for a constant quotient is met at k = 3; the rank count rank FT(P_2) = d^2 + 1, computed from stationary phase (1 from 0, d from each of the d roots), agrees with the Euler-characteristic count (CHECKED by hand, not by script).
Weak points. (i) the treatment of the trivial character and of Jordan blocks in F^(0,infty'), F^(infty,0'); (ii) whether the singular points s != 0 can ever contribute a tame piece at infinity (I claim never, because L_psi(s y) is wild); (iii) that the stationary phase formulas used are weight-free and hold in characteristic p (p odd, tame, p does not divide the orders involved); (iv) the passage "no trivial inertia constituent implies the coinvariant space vanishes" is an implication in one direction only, which is what is used. A numerical test is possible and not done (section 5, test T1).
Verdict on the claim "weights are needed" of the first phase: if section 4 is right, the route is not circular and needs no weights; if it is wrong the route is back to (S_k') or (W*).

## 5. A plan: the shortest list of statements

Goal: a complete weight-free proof of |alpha| <= sqrt(q) for y^2 = f(x).
1. (I1-I4 plus Laumon sections 2.3, 2.5) Verify in primary sources that the Fourier transform preserves perversity, local Fourier transforms exist and stationary phase holds in positive characteristic, and that their proofs use no weights. Tool: reading Laumon 1987 chapters 1-2, Katz-Laumon appendix, BBD 4.1. Difficulty: low to medium (reading), the main risk is a hidden weight argument in chapter 2.
2. (P_k) for infinitely many k (all even k suffice): H^1_c(A^1, P_k) = 0 for generic h. Tool: the recursion of section 4 with Laumon's stationary phase; one needs the exact local statements for trivial character and unipotent blocks. Difficulty: medium; it is bookkeeping with one delicate case (the trivial character at i = 3 mod 4). If this fails at even k, fall back to 2'.
2'. (fallback) (W*) or (S_k'): no large wrong-parity eigenvalue, for infinitely many even k, for some c. Tool: none known weight-free; k = 4 done outside lines; k >= 6 nothing. Difficulty: very high.
3. Proposition X (section 3.2). Tool: the Leray virtual count, Parseval, no_hidden_growth. Difficulty: low; to be refereed (section 3.2 remark (v)). Lean: the endgame lemma exists; the bookkeeping would need a statement about virtual representations, not formalised.
4. Choice of Q = q^m and h: exists once Q > number of exceptional h; exponent independent of m (2.3). Difficulty: trivial.
5. The limit k to infinity: PROVED, in Lean (endgame).
Tests I recommend before any of this is trusted: T1. Over F_p with p = 3 and Q = 3^n for n up to 15, compute S_n(h) for k = 2 (and k = 3) exactly in Z[omega] by a Walsh-type transform and check that the exponential polynomial has exactly d^2 - d + 1 terms (k = 2, prediction from section 4: R^2 of rank d^2 - d + 1, R^3 = 0). T2. Check section 4 at k = 3: the prediction is that R^4 may be nonzero. T3. Referee Proposition X line by line with a second agent.

## 6. Status table

- Theorem G (a), (b), (c), (d): PROVED given CITED weight-free inputs (not re-derived by me).
- Non-existence of matching planes for k >= 6: PROVED, CHECKED to k = 12.
- k = 4 bad set: proved bad on X1, proved good outside X4 union X2 (K4T), open between.
- Exponent argument over F_(q^m): PROVED, no m in the exponent.
- Proposition X: PROVED conditional on (P_k) and the standard inputs; not independently checked.
- (P_k) for even k: HINT (stationary phase bookkeeping), not checked against Laumon, high risk.
- c-average identity: PROVED and CHECKED (6 of 6 cases exact).
- Weight-free exclusion of Tate-type cancellation: PROVED for planes at most one k; for general Type A or B classes only through (P_k).
- The route as a proof of Weil: OPEN, resting on (P_k) for even k.
