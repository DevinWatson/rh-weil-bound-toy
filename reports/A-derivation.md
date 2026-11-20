# A. Derivation of footnote 3 (path quadric, quadratic character, hyperelliptic case)

Scope: this is the Weil bound for the hyperelliptic curve y^2 = f(x). It is a theorem (Weil 1948). The question here is whether THIS route is a proof and what it needs. Nothing here concerns the Riemann Hypothesis for the integers.
Labels: PROVED, CITED, CHECKED, OPEN, HINT. Hand checks only; no script was run, so nothing below is labelled CHECKED except small hand numerics, which are labelled "hand".

## 0. Setting

q odd prime power, psi = e_q a nontrivial additive character of F_q, f in F_q[x] squarefree of odd degree d >= 3, chi the quadratic character (chi(0)=0), t(x)=chi(f(x)), M = sum_x t(x). Let r = number of roots of f in F_q. For F_{q^n} use chi_n = chi o Norm, t_n(x)=chi_n(f(x)), M_n.

0.1 CITED (F. K. Schmidt 1931; A. Weil, "Sur les courbes algebriques et les varietes qui s'en deduisent", 1948; for hyperelliptic curves already Artin's thesis 1924). The smooth projective model C of y^2=f(x) has genus g=(d-1)/2 and one point at infinity (d odd). Its zeta function is rational, Z(T)=P(T)/((1-T)(1-qT)), P(T)=prod_{i=1}^{d-1}(1-alpha_i T) in Z[T]. No Riemann hypothesis is used for this.
0.2 PROVED from 0.1. Each x in F_{q^n} contributes 1+chi_n(f(x)) points, so #C(F_{q^n}) = q^n + 1 + M_n, hence M_n = -sum_i alpha_i^n for all n >= 1.
0.3 Target (Weil 1948, CITED, the theorem to be re-proved): |alpha_i| = sqrt(q). Equivalent forms: |M_n| <= (d-1) q^{n/2} for all n. PROVED equivalence from 0.2 and Lemma L below (one direction is the triangle inequality, the other is Lemma L with B = q^{1/2}).

**Lemma L (PROVED).** Let gamma_1..gamma_s be distinct nonzero complex numbers, r_j nonzero integers, R_n = sum_j r_j gamma_j^n for n >= 1. If |R_n| <= C B^n for all n then |gamma_j| <= B for all j.
Proof. sum_n R_n T^n converges for |T|<1/B, so the rational function sum_j r_j gamma_j T/(1-gamma_j T) is analytic on |T|<1/B. Its poles at T=1/gamma_j are genuine (distinct points, nonzero residue), so |1/gamma_j| >= 1/B. QED.
Note that Lemma L is exactly where "no cancellation" is used: it needs r_j != 0 at the eigenvalue one cares about.

## 1. The identity qN = M^k + R and the Parseval bound

Let k >= 2, Q(x)=x_1x_2+x_2x_3+...+x_{k-1}x_k, t^{(k)}(x)=prod t(x_i), N = sum over x in F_q^k with Q(x)=0 of prod t(x_i). For h in F_q put S(h)=sum_{x in F_q^k} prod t(x_i) psi(h Q(x)).

**1.1 (PROVED) Identity.** sum_{h in F_q} S(h) = sum_x prod t(x_i) sum_h psi(hQ(x)) = q N, because sum_h psi(hc)=q if c=0 and 0 otherwise. The term h=0 is S(0)=M^k. Define R = sum_{h != 0} S(h). Then qN = M^k + R. The same holds over every F_{q^n} (replace q, t, psi by q^n, t_n, psi o Tr), with R_n, N_n, M_n.

**1.2 (PROVED) Parseval step.** For h != 0 define T_h g(x) = sum_y psi(hxy) g(y) on functions F_q -> C. Orthogonality of characters gives sum_x psi(hx(y-y'))=q delta_{yy'}, so ||T_h g||_2^2 = q ||g||_2^2 (Parseval).
Put G_k = t and G_j(x_j) = t(x_j) (T_h G_{j+1})(x_j) for j=k-1,...,1. Then S(h) = sum_{x_1} G_1(x_1) = <1_{t != 0}, G_1>. Since |t| <= 1, ||G_j|| <= ||T_h G_{j+1}|| = sqrt(q) ||G_{j+1}||, a loss of sqrt(q) at each of k-1 steps. Thus ||G_1|| <= q^{(k-1)/2} ||t||, ||t||^2 = q - r, and Cauchy-Schwarz gives
 |S(h)| <= sqrt(q-r) * q^{(k-1)/2} * sqrt(q-r) = (q-r) q^{(k-1)/2} <= q^{(k+1)/2}.
(Parseval is applied k-1 times, as the footnote says.) Summing over the q-1 values h != 0:

**|R| <= (q-1)(q-r) q^{(k-1)/2} < q^{(k+3)/2}**, and the same over F_{q^n}: |R_n| < q^{n(k+3)/2}, with constant 1 independent of n.

**1.3 What this bound is and is not.** The true size of qN is about q^{(k+1)/2} (N is a sum over a variety of dimension k-1, square root would give q^{(k-1)/2}). The Parseval bound q^{(k+3)/2} is larger than qN, so R is NOT shown to be small compared with qN. It is not "square root quality" for R itself; it is a bound with a fixed loss of q^{3/2} in the k-th power, which is harmless because only the exponent per factor, (k+3)/(2k), matters. Truth for each S(h) is about q^{k/2}; the Parseval loss is a factor sqrt(q) per h. (HINT, heuristic square-root count; not used.)
(Hand check, q=3, f=x^3-x+1: t(x)=1 for all x, M=3. k=3: N=15 by direct count, R=qN-M^3=45-27=18, bound (q-1)(q-r)q^{(k-1)/2}=2*3*3=18; equality, since S(h)=9 for h=1,2. k=2: N=5, R=15-9=6, bound 2*3*sqrt3=10.4.)
Coefficients c_i on the quadric (sum c_i x_i x_{i+1}, c_i in F_q^*) change nothing in 1.1 or 1.2.

## 2. What is needed about N ("definite sign from middle cohomology")

**2.1 (CITED) Cohomological form of the counts.** Grothendieck-Lefschetz trace formula (SGA 4 1/2, "Rapport"/"Fonctions L modulo l^n et modulo p", SGA 5 Exp. XV): for a constructible Q_l-sheaf F on a variety V over F_q, sum_{x in V(F_{q^n})} Tr(Frob_x|F) = sum_i (-1)^i Tr(Frob^n | H^i_c(V_{Fbar_q}, F)). No weights or purity are used in this statement. Künneth for compact supports (SGA 4 XVII 5.4.3). Let L=L_chi(f) on U=A^1 minus Z(f), j: U -> A^1; Euler-Poincare (Grothendieck-Ogg-Shafarevich, SGA 5 Exp. X; sheaf tame, Swan 0) gives H^i_c(A^1, j_!L)=0 for i != 1 and dim H^1_c = d-1 (H^2_c=0 since L is geometrically nontrivial). Its Frobenius eigenvalues are the alpha_i of 0.2. So by Künneth H^i_c(A^k, (j_!L)^{boxtimes k}) is zero except i=k, where it is the k-fold tensor power with eigenvalue multiset A = {alpha_{i_1}...alpha_{i_k}}, |A|=(d-1)^k, and
 M_n^k = (-1)^k sum_{gamma in A} gamma^n. (PROVED from 0.2 or from Künneth; both agree.)

**2.2 The input, weakest sufficient form (W).** By 2.1 and 1.1, R_n = q^n N_n - M_n^k is a finite exponential polynomial R_n = sum_gamma r_gamma gamma^n (r_gamma in Z), uniquely determined by the integer sequence. Let alpha_* be a value of maximal modulus among the alpha_i, and gamma_* = alpha_*^k in A.
 (W_k): r_{gamma_*} != 0, i.e. the eigenvalue alpha_*^k of M^k is not cancelled by the exponential-polynomial expansion of q^n N_n.
Writing q^n N_n = sum_gamma c_gamma gamma^n, this reads c_{gamma_*} != (-1)^k a_{gamma_*}, where a_{gamma_*} >= 1 is the multiplicity of gamma_* in A. Nothing more is needed. It is a statement about integers, and it is what the argument literally uses.

**2.3 Natural form (S), the one the footnote means.** Let Y = {Q=0} in A^k over Fbar_q and K = (j_!L)^{boxtimes k}|_Y. Then
 (S_k): H^i_c(Y, K) = 0 for all i != k-1 (middle cohomology only), or at least for all i with i not congruent to k-1 mod 2.
Under (S_k) the trace formula gives q N_n = (-1)^{k-1} sum_{gamma in E} gamma^n for an honest multiset E (the eigenvalues of H^{k-1}_c(Y,K)(-1), with the Tate twist (-1) accounting for the factor q; the identity H^*_c(A^k x A^1, K (x) L_psi(hQ)) = H_c^{*-2}(Y,K)(-1) is the cohomological version of 1.1, CITED standard fibre integral). Since M^k enters with sign (-1)^k, and N with sign (-1)^{k-1}, R = qN - M^k = (-1)^{k-1}( sum_E gamma^n + sum_A gamma^n ): all multiplicities in R have the same sign, so r_{gamma_*} = (-1)^{k-1}(e_{gamma_*} + a_{gamma_*}) != 0. (S_k) implies (W_k). This is the footnote's "opposite signs meaning no cancellation of inverse roots".

**2.4 Stronger pointwise form (P).** (-1)^{k-1} N_n >= 0 for all n (for even k: N_n <= 0 for all n). Then M_n^k = q^n N_n - R_n gives |M_n|^k <= |R_n| directly for k even. (P) is stronger than (S) in spirit but is FALSE already for k=2: see 4.1 (q=3, f=x^3-x+1 gives N=5>0 with k=2). So "definite sign" can only mean the cohomological sign (S), not a sign of the integers N_n. Odd k would need N_n and M_n of opposite sign, which is not a definite-sign statement at all; use (S) there.
Also note: (S) concerns eigenvalues, so it needs the geometric statement for all n at once; the variety is defined over F_q so this is automatic.

## 3. The exponent and the passage k -> infinity

Assume (W_k) for one k. By 1.2, |R_n| <= (q^n-1)(q^n-r_n) q^{n(k-1)/2} < B^n with B = q^{(k+3)/2}. Lemma L (with r_{gamma_*} != 0) gives |gamma_*| <= B, i.e. |alpha_*|^k <= q^{(k+3)/2}:
 **|alpha_i| <= q^{1/2 + 3/(2k)} for all i**, so c = 3/2 and |M_n| <= (d-1) q^{n(1/2+3/(2k))}.
Table: k=3 gives q^1 (the trivial bound), k=4 gives q^{7/8}, k=6 gives q^{3/4}, k=8 gives q^{11/16}. The method beats the trivial bound only for k >= 4.
If (W_k) holds for infinitely many k (for the same f, q), then |alpha_i| <= q^{1/2}: the tensor power trick, constants disappear in the k-th root. (PROVED given the inputs.) Note the bound is uniform in n, which is what makes the k-th root trick work.

**Where the sign is used, exactly.** Only to know r_{gamma_*} != 0 in Lemma L. Without it R may have lost gamma_*, and then |R_n| small says nothing about M. Concrete failure (hand): take t = 1 (trivial sheaf) k=4: Y is the hyperbolic quadric cone, #Y = q^3+q^2-q, qN = q^4+q^3-q^2, M^4 = q^4, so R = q^3 - q^2, far below |M|^4 = q^4. The top class of Y (degree 2(k-1), eigenvalue q^{k-1}, sign +) cancels the eigenvalue q^k of M^k (also sign +, even degrees); in (S) terms, the vanishing of H^{2k-2}_c(Y,K) and all higher-than-middle degrees is violated. The argument therefore uses nontriviality of L in a way no formal manipulation can supply: it is precisely the information that H^1 of the curve has no weight-2 part.
**Multiplicity**: if different eigenvalues coincide, they simply add; no problem because all multiplicities have the same sign. If the signs were mixed (E could contain gamma_* with multiplicity -a), r_{gamma_*} could vanish.

## 4. Small cases by hand

Assume f(0) != 0, t0 = t(0) = chi(f(0)) = +-1; note chi_n(f(0)) = t0^n. Q for k=2 is x_1x_2, for k=3 is x_2(x_1+x_3).

**4.1 k=2 (PROVED).** Zeros: x_1=0 or x_2=0. N = 2 t0 M - t0^2 = 2 t0 M - 1. Over F_{q^n}: N_n = 2 t0^n M_n - 1 = -[ 2 sum_i (t0 alpha_i)^n + 1 ]. So (S_2) holds in the form q N = (-1)^{1} sum_E with E = {q t0 alpha_i (twice each), q}: a genuine multiset, sign (-1)^{k-1} = -1. M^2 = +sum alpha_i alpha_j, sign +. So R_n = -(sum_E + sum_A): same sign, no cancellation. But the pointwise sign (P) fails: q=3, f=x^3-x+1 (t == 1, M=3, t0=1): N=5 > 0 (hand count: 3+3-1), while -[2(alpha+alphabar)+1] = -[2(-3)+1] = 5 (alpha=(-3+-sqrt(-3))/2). Output bound: |alpha_i alpha_j| <= q^{5/2}, useless (trivial bound is q^2).
If f(0)=0: N=0, E empty, R=-M^2, signs trivially fine.
Euler characteristic check (hand): chi_c(Y^0), Y^0 = Y cap (A^1 minus Z)^2 gives 2(1-d)-1 = 1-2d = -(dim E) with dim E = 2(d-1)+1, consistent.

**4.2 k=3 (PROVED, assuming f(0)!=0 and g(x)=f(x)f(-x) squarefree, i.e. roots a_i != +-a_j, a_i != 0).** N = N_A + N_B - N_{A cap B} for A={x_2=0}, B={x_1+x_3=0}: N_A = t0 M^2, N_B = M C, N_{A cap B} = t0 C, where C = sum_x t(x) t(-x) = sum_x chi(g(x)). So
 **N = t0 M^2 + (M - t0) C.**
g has even degree 2d, leading coeff -lc(f)^2 (d odd), so by the same curve count C_n = -sum_{j=1}^{2d-2} delta_j^n - eps^n, eps = chi(-1) (CITED rationality as in 0.1 for the curve y^2=g(x)). Then
 N_n = t0^n sum_{i,j}(alpha_i alpha_j)^n + sum_{i,j}(alpha_i delta_j)^n + sum_i (eps alpha_i)^n + t0^n sum_j delta_j^n + (t0 eps)^n,
every term with coefficient +1, as (S_3) requires (sign (-1)^{k-1}=+1). M^3 = -sum alpha_i alpha_j alpha_l, sign -1. So R = qN - M^3 has all coefficients +1: no cancellation. dim E = (d-1)^2 + (d-1)(2d-2) + (d-1) + (2d-2) + 1 = 3d^2-3d+1.
Euler characteristic check (hand): chi_c(Y^0) for k=3 = (1-d)^2 + (1-2d)(1-d) - (1-2d) = 3d^2-3d+1, equal to dim E. Consistent.
Hand numerics (q=3, f=x^3-x+1): M=3, C=3, N = 9 + 2*3 = 15, direct count 9+9-3 = 15 (all weights 1); g(x) is 1 on F_3, curve y^2=g has 6 points, Sum delta_j = -2, matching C=-Sum delta - eps with eps=chi(-1)=-1.
f(0)=0 variant: N = M C with C = sum_{x != 0} chi(g~(x)) where f=x f~, g=-x^2 f~(x) f~(-x); C_n = -sum delta~_j^n - 2 eps^n (assuming generic squarefree g~), so N_n = sum alpha_i delta~_j + 2 sum (eps alpha_i)^n, again all +; (PROVED in the same way).
Output at k=3: |alpha_i|^3 <= q^3, i.e. the trivial bound. So both explicit cases are sign-consistent but give nothing beyond trivial.

**4.3 k=4 (HINT, not verified).** Q = x_2(x_1+x_3) + x_3 x_4 is a nondegenerate hyperbolic form; N is no longer a polynomial in one-variable sums: it contains a genuinely new two-variable object. A hand count of the point-polynomial of Y^0 for generic roots and evaluation at q=1 gives chi_c(Y^0) = 1 - 4d + 3d^2 - 4d^3 (<0, matching sign (-1)^{k-1}); for d=3 this predicts dim E = 92 if (S_4) holds. This relies on genericity assumptions on Z and on the polynomial-count heuristic; it must be machine-checked before use. Its sign is only a necessary condition for (S_4).

## 5. Assessment of the input (S) / (W)

What is needed: for infinitely many k, (W_k) for the fixed f; naturally the cohomological sign (S_k).

**Theorems that apply (all CITED, none uses weights):**
- Grothendieck-Lefschetz and Künneth: put N_n, M_n^k and R_n in exponential polynomial form (2.1). No gap.
- Artin vanishing (SGA 4 XIV 3.1; BBD Astérisque 100, Thm 4.1.1): for P perverse on an affine variety Y, H^i(Y,P)=0 for i>0 and H^i_c(Y,P)=0 for i<0. If i^*P[-1] is perverse, this gives H^i_c(Y,K)=0 for i<k-1: only the lower half of (S_k). Duality does not give the upper half.
- Weak Lefschetz / Bertini for perverse sheaves and non-characteristic restriction (Goresky-MacPherson, "Stratified Morse Theory" 1988; Katz, "Perversity and exponential sums", 1990s; Kiehl-Weissauer, Weil conjectures, perverse sheaves and l-adic Fourier transform, 2001, Ch. III-IV): if Y is non-characteristic for P = (j_!L[1])^{boxtimes k} (and j_!=j_*=j_{!*} here since L has monodromy -1 at every root), then i^*P[-1] is perverse. This supplies the hypothesis of Artin vanishing; it still yields only the lower half. 
- Vanishing above the middle degree (generic vanishing for perverse sheaves on tori and similar): Gabber-Loeser, "Faisceaux pervers l-adiques sur un tore", Duke Math. J. 1996; Krämer-Weissauer; Bhatt-Schnell-Scholze. These apply off a finite union of translates of subtori in character space. The quadratic character is a torsion character, which is the typical exceptional locus. I know no theorem that gives (S_k) for it. OPEN: I could not prove (S_k) for any k >= 4, and I did not find a citable theorem that does.

**Genericity conditions (hand-derived, PROVED for the algebra, applicability OPEN).** Y is non-characteristic to the stratum F_S = {x_i = a_i, i in S}, a_i roots of f, iff there is no point of Y cap F_S that is a critical point of Q|_{F_S}. Write A for the matrix of Q (Q = x^T A x / 2). For k even A is invertible (path adjacency, det = +-1); critical points have x = A^{-1} lambda with lambda supported on S, so x_S = B lambda with B = (A^{-1})_{SS}, and Q = lambda.a / 2. Tangency requires B lambda = a and lambda.a = 0. 
 - |S|=1: B_11=0 forces a = 0: so for f(0)!=0 each single hyperplane x_i=a is transversal (PROVED).
 - Larger S: tangency can occur when the roots satisfy linear relations, e.g. k=4, S={1,2,4}: B_SS=[[0,1,-1],[1,0,0],[-1,0,0]] (A^{-1} for P_4 is [[0,1,0,-1],[1,0,0,0],[0,0,0,1],[-1,0,1,0]], hand verified A*A^{-1}=I), solvable iff a_4=-a_2, so a pair of roots r, -r in Z breaks it. For general k the conditions are polynomial relations among the roots with repeated entries allowed, and I did not show they can be avoided for one f at all k. OPEN.
 - k odd: Q is degenerate with kernel (1,0,-1,0,1,...); Y is singular along a line, which meets the root hyperplanes x_i=a at points (+-a ...); I found for k=7, S={3} a critical point on Y in the stratum x_3=a, so for the plain path quadric non-characteristic restriction FAILS for odd k >= 7 and the Bertini route needs the coefficients c_i ("quadric coefficients too", as the footnote says). Whether generic coefficients repair every stratum is OPEN.
 - Coefficients must lie in F_q (the counting identity needs F_q-rational quadric). Genericity over Fbar_q does not give F_q-points of the good locus once the number and degree of the conditions grow with k at fixed q; Poonen's Bertini over finite fields (Ann. of Math. 2004) concerns hypersurfaces of high degree, not a fixed quadric shape. So the k -> infinity limit at FIXED q is a real extra gap. OPEN.

**Circularity.** The steps 1, 2.1, 2.2, 3, Lemma L and the trace formula use no weights and no Weil bound. Any proof of (S_k) that goes through purity of H^i_c(Y,K) or Deligne's Weil II applied to Y or to the sheaf would already contain the weight statement for H^1_c(A^1, j_!L) (a restriction to a coordinate line), i.e. the toy theorem itself: circular. The reduction is therefore only interesting if (S_k) can be proved by vanishing/Lefschetz theorems alone. The failing example t=1 shows (S_k) is not formal: it fails for the trivial sheaf where the conclusion is false.
Other remarks: (a) the hypothesis is equivalent to a non-cancellation statement, so the mechanism is a "positivity of point counts" argument in the spirit of Deligne's Weil I, section 1 (Rankin-type use of non-negativity of counts for tensor powers; section number to be checked by the literature agent), with the Euler-characteristic sign replacing non-negativity. Whether the exact sign-from-middle-cohomology route has appeared in print I could not determine (OPEN, literature agent). (b) The second half of footnote 3 (Gabber's hypersurface in Katz, chi -> chi(disc), the order-#mu_K Gauss sum, the cover of GL_2, the complete graph) makes no checkable statement; I did not treat it. (c) The inputs (S_k) for k = 2, 3 hold by closed formula (section 4) but give no bound beyond trivial; the first case that matters is k = 4.

## 6. Paper inputs (exact citations)

1. F. K. Schmidt, "Analytische Zahlentheorie in Körpern der Charakteristik p", Math. Z. 33 (1931) 1-32; E. Artin, thesis, Leipzig 1921, Math. Z. 19 (1924) 153-246 (hyperelliptic zeta, rationality). Used: 0.1 rationality, P of degree d-1.
2. A. Weil, "Sur les courbes algébriques et les variétés qui s'en déduisent", Hermann 1948 (RH for curves); "On some exponential sums", Proc. NAS 34 (1948) 204-207. Used: the theorem being re-proved (target only, not input).
3. A. Grothendieck, trace formula: SGA 5 Exp. XV; Deligne SGA 4 1/2 "Fonctions L modulo l^n et modulo p". Used: 2.1.
4. SGA 4, Exp. XVII Thm 5.4.3 (Künneth), Exp. XIV Thm 3.1 (Artin vanishing). Used: 2.1 and section 5.
5. Grothendieck-Ogg-Shafarevich: SGA 5 Exp. X (Raynaud, Séminaire Bourbaki 286, 1965). Used: dim H^1_c = d-1, tame Euler characteristic.
6. Beilinson-Bernstein-Deligne, "Faisceaux pervers", Astérisque 100 (1982), Thm 4.1.1, Sections 4.1-4.2 (Artin vanishing for perverse sheaves). Used: 5.
7. Goresky-MacPherson, Stratified Morse Theory, Springer 1988 (Lefschetz hyperplane theorems for perverse/constructible sheaves); Kiehl-Weissauer, Weil Conjectures, Perverse Sheaves and l-adic Fourier Transform, Springer 2001; N. Katz, "Perversity and exponential sums" (in Algebraic Number Theory, Adv. Stud. Pure Math. 17, 1989). Used: 5 (non-characteristic restriction; exact statement numbers to be confirmed).
8. O. Gabber, F. Loeser, "Faisceaux pervers l-adiques sur un tore", Duke Math. J. 83 (1996) 501-606. Used: 5 (generic vanishing, torsion exceptions).
9. B. Poonen, "Bertini theorems over finite fields", Ann. of Math. 160 (2004) 1099-1127. Used: 5 (F_q-rational genericity).
10. P. Deligne, "La conjecture de Weil I", Publ. IHES 43 (1974) 273-307; "La conjecture de Weil II", Publ. IHES 52 (1980) 137-252. Used only as the circular alternative in 5; also the comparison in 5(a).
11. Parseval/orthogonality of additive characters (standard; proved in 1.2). Lemma L proved here.
12. Not cited or not checked: S. A. Stepanov 1969, E. Bombieri, Séminaire Bourbaki no. 430 (1972/73), W. M. Schmidt, LNM 536 (1976) for elementary proofs of the same bound; listed so the literature agent can compare, not used.

## Summary of status
- PROVED: identity qN=M^k+R; bound |R| <= (q-1)(q-r)q^{(k-1)/2} < q^{(k+3)/2}; Lemma L; exponent 1/2+3/(2k); the limit k -> infinity given (W_k) infinitely often; closed forms N for k=2,3 and the sign pattern (-1)^{k-1} there; the necessary failure for t=1.
- CITED: rationality of zeta, trace formula, Künneth, Artin vanishing, Euler characteristic.
- OPEN: (S_k) or (W_k) for any k >= 4; non-characteristic restriction for all strata and all k with F_q-rational coefficients; genericity uniform in k at fixed q; whether this route is in the literature.
- HINT: k=4 Euler characteristic count 1-4d+3d^2-4d^3; heuristic sizes in 1.3.
- The argument is NOT a complete proof; the whole difficulty is concentrated in the unproven sign input.
