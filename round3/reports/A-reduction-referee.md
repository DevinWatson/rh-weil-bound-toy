# Referee report on Claim A (the reduction), round 3

Started 2026-11-20 20:04 UTC. Setting: character sums over finite fields (Weil 1948). Nothing here concerns the Riemann
Hypothesis for the integers. Part 1 and 2 below were derived by me from the brief and the first two established
lists only, before opening reports RED, GEN or the toy-case text. Weights, purity, Weil conjectures are used nowhere in a proof;
where I use them it is flagged "[interpretation only]".

## 1. Claim A as a theorem (hypotheses explicit)

Data. q odd, F_q, F_Q a finite extension (Q = q^s), psi a nontrivial additive character of F_Q (psi_q o trace),
chi the quadratic character, f in F_q[x] with f not a constant times a square in F-bar[x] (the sheaf L = L_chi(f) is then
geometrically nontrivial; the brief's "squarefree of odd degree >= 3" is one case; f(0) != 0 is NOT used by Claim A),
j : U_f = A^1 - Z -> A^1, t = chi(f) its trace function (t = 0 on Z), H = H^1_c(A^1_Fbar, j_! L), alpha_1..alpha_r its
Frobenius eigenvalues over F_q (r = d-1 in the brief). Integer k >= 2. c = (c_1..c_{k-1}) in (F_Q^*)^{k-1}.
Q_c(x) = sum c_i x_i x_{i+1}. On G_m x A^k over F_Q (coordinates h, x):
F = pr^*(external product of j_!L) tensor L_psi(h Q_c(x)). For a geometric point h of G_m, F_h is its restriction to A^k.
(Frobenius acts over F_Q; the trace function of F at (h,x) in F_{Q^n} is  prod t(x_i) psi_n(h Q_c(x)), t evaluated over F_{Q^n}.)

(P_k^c): there is a dense open U' of G_{m,Fbar} with H^{k+1}_c(A^k_Fbar, F_h)=0 for every geometric point h of U'.
(U' is then automatically defined over F_Q: the complement is the support of R^{k+1} pi_! F.)

Theorem A. Under the above, if (P_k^c) holds over F_Q, then |alpha_i|^k <= q^{(k+3)/2} for every i and every
embedding of Qbar_l in C (equivalently for every complex root: the alpha_i are algebraic).

Inputs used (all "established" in the brief, rechecked below in section 2 where cheap):
(E1) q N = M^k + R, |S_h| <= Q^{(k+1)/2} over every finite field F_Q for h != 0, c_i != 0 (Lean, Cauchy-Schwarz).
(E2) Lean lemma: a finite sum with nonzero coefficients of n-th powers that is O(rho^n) (n over all n >= 1) has all bases <= rho.
(E3) H^j_c(Y,K)=0 for j < k-1. [I re-proved it, see 2(a).]
(E4) For EVERY h != 0 (not just generic) H^j_c(A^k,F_h) = H^{j-k}_c(A^1, P_k), P_k perverse, hence j in {k,k+1}.
     This rests on: tensoring with j_!L (j affine) and Fourier transform (hc_i != 0) preserve perversity; Artin vanishing.
     I did not re-derive that FT preserves perversity (Laumon 1987, 1.3.2.3, NOT OPENED by me).
(E5) H = H^1_c only (H^0_c = H^2_c = 0 because L is geometrically nontrivial); Kunneth for H_c.

## 2. Step by step (my own derivations)

### (a) Exact sequence and the injection of T
A^1_h = G_m u {0}. Long exact sequence of compactly supported cohomology of F on A^1 x A^k:
 H^{m-1}_c({0}xA^k) -> H^m_c(G_m x A^k) -> H^m_c(A^1 x A^k) -> H^m_c({0}xA^k) -> H^{m+1}_c(G_m x A^k).
F restricted to h=0 is the external product K_ext of j_!L (L_psi(0)=1), so by Kunneth H^m_c({0}xA^k)=T in m=k (T=H^{(x)k}), 0 otherwise.
Projecting L_psi(hQ) along h gives q on {Q=0}: H^m_c(A^1xA^k,F)=H^{m-2}_c(Y,K)(-1).
By (E3) this vanishes for m<=k. Hence
 * H^m_c(G_m x A^k,F)=0 for all m <= k   (m<k: both neighbours vanish; m=k: H^{k-1}_c({0}xA^k)=0 and H^k_c(A^1xA^k)=0),
 * 0 -> T -> H^{k+1}_c(G_m x A^k,F) -> H^{k-1}_c(Y,K)(-1) -> 0 exact, Frobenius equivariant, no twist in the connecting map.
 PROVED (modulo E3, which I re-proved: Y is a closed hypersurface in A^k, its complement V is affine, P=K_ext[k] perverse;
 H^j_c(V,P)=0 for j<0 by duality from Artin; H^j_c(A^k,P)=0 for j<0 and nonzero only at j=0; so H^j_c(Y,P|Y)=0 for j < -1, i.e.
 H^j_c(Y,K)=0 for j < k-1).
 Sign check: sum_m (-1)^m Tr = ... gives R=(-1)^{k+1}Tr(H^{k+1}) + (-1)^{k+2}Tr(H^{k+2}) + (higher, see (b)) and the T part of R is
 (-1)^{k+1}Tr(T) = -M^k, consistent with R = qN - M^k.

### (b) Leray over the h-line
pi : G_m x A^k -> G_m. R^b pi_! F has stalk H^b_c(A^k,F_h) (proper base change). By (E4): R^b=0 unless b in {k,k+1}.
(P_k^c) says R^{k+1} is supported on the finite set G_m - U'. So E_2^{a,b}=H^a_c(G_m,R^b) has:
 b=k: a=0,1,2 ; b=k+1: a=0 only (punctual sheaf has H^a_c=0 for a>0).
The only possible differential (d_r: (a,b)->(a+r,b-r+1) with both b-values in {k,k+1}) is d_2 : E_2^{0,k+1} -> E_2^{2,k}.
Also E_2^{0,k}=H^0_c(G_m,R^k) must vanish because H^k_c(G_m x A^k,F)=0 by (a) and nothing hits or leaves it.
Result:
 H^{k+1}_c(G_m x A^k,F): extension of ker(d_2) (a subspace of the stalks of R^{k+1} at the bad points) by H^1_c(G_m,R^k);
 H^{k+2}_c = coker( d_2 : H^0(R^{k+1}) -> H^2_c(G_m,R^k) );
 H^{k+3}_c = 0 and H^m_c = 0 for m <= k and m >= k+3.
In the trace: R = (-1)^{k+1} Tr(.|H^{k+1}) + (-1)^{k+2} Tr(.|H^{k+2}). Right parity = degree k+1, wrong parity = degree k+2.
NOTE: GEN's wording "the wrong-parity group IS H^2_c(G_m,R^k)" is wrong in general: it is a QUOTIENT by the image of d_2 (RED already
said a differential had been left out). The theorem only needs "quotient".

### (c) Wrong-parity group
Let V = R^k|_U (U = lisse locus of R^k intersected with the vanishing locus of R^{k+1}, dense open in G_m). Sequence
0 -> j_{U!}V -> R^k -> (punctual) -> 0 (the kernel of R^k -> j_*j^*R^k, if any, is punctual too, harmless) gives
H^2_c(G_m,R^k)=H^2_c(U,V) since H^1_c,H^2_c of a punctual sheaf are 0. For a lisse sheaf on a smooth geometrically connected
curve, H^2_c(U_Fbar,V) = V_{pi_1^geom}(-1) (duality, V_{pi_1} = coinvariants = maximal geometrically constant quotient C of V).
Hence every eigenvalue of Frobenius on the wrong-parity group is q*beta (Q*beta over F_Q) with beta an eigenvalue on C.
No tameness, no lisse-ness on all of G_m, nothing about the singular points is used.
C carries a Galois action because pi_1^geom is normal in pi_1(U_{F_Q}); V -> pi^*C is a map of sheaves on U_{F_Q}.

### (d) Passage to one fibre, Parseval
Closed point h_0 of U of degree m over F_Q (exists, infinitely many). Frob_{h_0} on the geometric stalk V_{h_0}=H^k_c(A^k,F_{h_0})
maps onto Frob_Q^m on C. So beta^m is an eigenvalue of Frob_{Q^m} on H^k_c(A^k,F_{h_0}) for each eigenvalue beta of C.
The fibre at h_0 has cohomology in degree k only (h_0 in U), so over F_{Q^{mn}}:
  S^{(Q^{mn})}(h_0) = (-1)^k sum_j gamma_j^n,  gamma_j eigenvalues of Frob_{Q^m} on H^k_c(A^k,F_{h_0}) with multiplicity.
(E1) gives |S| <= Q^{mn(k+1)/2} for all n >= 1, h_0 in F_{Q^m}^* subset F_{Q^{mn}}^*, c in F_Q subset (same field). Distinct gammas carry
positive integer coefficients (multiplicities, one sign), so (E2) gives |gamma_j| <= Q^{m(k+1)/2}. Therefore |beta| <= Q^{(k+1)/2}.
PROVED (given E1, E2, E4 and (P_k^c) at h_0).

### (e) Dichotomy and multiplicities
Fix alpha=alpha_i and beta_0 = alpha^k (an eigenvalue of T, product of k copies of alpha; Frobenius over F_Q: use alpha^s,
see (f)). Write R_n = sum over distinct bases lambda of a_lambda lambda^n where
 a_lambda = (-1)^{k+1}( m_{k+1}(lambda) - m_{k+2}(lambda) ),  m_j = multiplicity of lambda among eigenvalues of Frob_Q on H^j_c(G_m x A^k,F).
m_{k+1}(beta_0) >= m_T(beta_0) >= 1 by (a). Two cases:
 * a_{beta_0} != 0: (E1) |R_n| <= (Q^n -1) Q^{n(k+1)/2} < Q^{n(k+3)/2}, (E2) gives |beta_0| <= Q^{(k+3)/2}.
 * a_{beta_0} = 0: m_{k+2}(beta_0)=m_{k+1}(beta_0) >= 1, beta_0 is an eigenvalue on the quotient of C(-1): beta_0=Q*beta, |beta|<=Q^{(k+1)/2}
   by (d), so |beta_0| <= Q^{(k+3)/2}.
Nothing about H^{k+1} other than "contains T" is used; the stalks of R^{k+1} at bad points, ker(d_2), H^1_c(G_m,R^k) never matter,
and cancellations between any two groups are covered by the second case. Distinct bases merge correctly because (E2) is applied to the merged sum.
PROVED.

### (f) Extension field
Run the whole argument over F_Q (all established inputs are for any finite field, c in F_Q^{k-1}). H over F_Q has eigenvalues alpha_i^s.
Conclusion |alpha_i^s|^k <= Q^{(k+3)/2}=q^{s(k+3)/2}, take s-th roots: |alpha_i|^k <= q^{(k+3)/2}. The Gauss-sum-like exponent
(k+1)/2 is relative to the base field of the fibre sum, which is F_{Q^{mn}}, and scales consistently. PROVED.
Subtlety: the quadratic character of F_{Q^n} on elements of F_q is chi(a)^{ns}: t over F_{Q^n} is chi_{Q^n}(f(x)); the L-function identity
M_n = -sum alpha_i^{sn} holds because H over F_Q is the base change of H.

(sections 3 onward are appended below as the work proceeds)

## 3. Tests where the answer is known

All numbers below come from exact integer arithmetic: script `compute/A/check_A.py`, output `compute/A/check_A_out.txt`
(dynamic programming over the path quadric in F_P, P = p^n, n = 1, 2, p in 5, 7, 11, 13; field arithmetic by tables; every comparison reported as True or equal is an
integer comparison; the decimals in the output are display only). Weil's theorem is not used in any proof; where I use it to interpret data it is marked [interpretation only].

### 3.1 Trivial sheaf t = 1 (f constant): the conclusion is false, so a hypothesis fails. PROVED + CHECKED
CHECKED (output file, section "trivial sheaf"), c = (1,...,1), p = 5, 7, 11, 13, k = 2..6: R = qN - q^k satisfies R^2 <= q^(k+3); for even k, R = (q-1) q^(k/2) exactly
(printed ratio 1.0); for odd k, R = (q-1) q^((k+1)/2) (ratio sqrt q). Meanwhile M^k = q^k > q^((k+3)/2) for k >= 4.
So "alpha = q satisfies |alpha|^k <= q^((k+3)/2)" is false for k >= 4, and Theorem A must not apply. What fails:
 * The hypothesis (E5): H^j_c(A^1, j_!L) = 0 for j != 1, i.e. L geometrically nontrivial. For t = 1, H^*_c(A^1, Q_l) is Q_l(-1) in degree 2. Then T = Q_l(-k) sits in degree 2k, not k,
   and step (a) breaks: H^{2k}_c(A^1 x A^k, F) -> H^{2k}_c({0} x A^k) = T is onto, so T does not inject into H^{k+1}_c(G_m x A^k, F) (and for k >= 3 that group is not even in
   the Leray range, which ends at k+3 < 2k+1). The term q^k never occurs in H_c(G_m x A^k): it lives in H^{2k-2}_c(Y)(-1) and is killed by restriction to h = 0.
   The identity R = qN - M^k remains true, which is why the data look innocent: R is small (about q^(k/2+1)), as it must be, and M^k is absent from R.
 * (P_k^c) is NOT what fails. E4 (perversity, fibre degrees k, k+1) holds for t = 1 (P_1 = Q_l[1], FT(P_1) = delta_0(-1), P_2 = delta_0(-1), P_3 = Q_l(-1)[1], alternating; as in RED).
   For k even the fibre is a nondegenerate Gauss sum in degree k, so (P_k^c) is TRUE; for k odd the form has rank k-1 and the fibre is in degree k+1, so (P_k^c) is false.
   Hence for t = 1, k even, every hypothesis of Theorem A except "L geometrically nontrivial" holds, and the conclusion is false: that hypothesis is essential and must be stated.
   For the brief's f (squarefree, odd degree >= 3) it holds. Weakest form: f is not a constant times a square in F-bar[x].

### 3.2 k = 2, all explicit. PROVED (algebra) + CHECKED
N_2 = 2 t0 M - 1 (t0 = chi(f(0)), t0^2 = 1), so qN = 2 q t0 M - q, and over F_{Q^n} (Q = q here)
 R_n = -M_n^2 + 2 q^n t0^n M_n - q^n = -sum_{i,j}(alpha_i alpha_j)^n - 2 sum_i (q t0 alpha_i)^n - q^n.
t0 over F_{q^n} is t0^n: chi_{q^n}(a) = chi_q(a)^n for a in F_q^* (the exponent (q^n-1)/(q-1) = 1 + q + ... is congruent to n mod 2); CHECKED in the script by assertion.
CHECKED: the identity N_2 = 2 t0 M - 1 in 32 (p, n, f, c) combinations, all "N2 ok=True".
Every coefficient is negative = (-1)^(k+1). So H^3 = T + 2*{t0 q alpha_i} + {q} (rank (d-1)^2 + 2(d-1) + 1 = d^2, matching RED), H^4 = 0, C = 0: no wrong parity, no cancellation possible
(a_lambda < 0 for every base). Theorem A gives |alpha|^2 <= q^(5/2), weaker than the elementary |alpha| <= q (from sum alpha^n = O(q^n) and E2), as it should be at k = 2.

### 3.3 k = 3, all explicit. PROVED (algebra) + CHECKED
N_3 = t0 M^2 + (M - t0) B(rho), B(rho) = sum_x chi(f(rho x) f(x)), rho = -c_2/c_1 (Y = {x_2 = 0} u {c_1 x_1 + c_2 x_3 = 0}). CHECKED for n = 1, 2: "N3 ok=True" in all 32 rows.
 * rho != 1 with f(rho x) f(x) squarefree (rho not in R'): even degree 2d, unramified at infinity, B_n = -b_n with b_n = sum_j beta_j^n + chi(rho)^n (2d-2 eigenvalues beta_j and one more).
   With u_n = -M_n: R_n = u^3 + q^n t0^n u^2 + q^n b u + q^n t0^n b. All coefficients positive = (-1)^(k+1). H^5 = 0, C = 0, no wrong parity. (HINT: I did not recheck the claim chi_n(lc) = chi(rho)^n beyond the algebra above.)
 * rho = 1 (c_1 = -c_2): B_n = q^n - r_n, r_n = number of roots of f in F_{q^n}. CHECKED B == P - r in every rho = 1 row. Then
   R_n = u^3 + q^n t0^n u^2 - q^n (q^n - r_n) u - q^n t0^n (q^n - r_n).
   CHECKED: this equals the brute-force qN - M^3 in 8 cases (p = 5, 7; two cubics; n = 1, 2).
   Wrong-parity (negative) terms: -q^{2n} u (eigenvalues q^2 alpha_i, d-1 of them) and -t0^n q^{2n} (eigenvalue t0 q^2). So C contains beta in {q alpha_i} and {t0 q}.
   Fibre bound required by Theorem A: |beta| <= q^((k+1)/2) = q^2. For beta = t0 q: fine. For beta = q alpha_i: it says |alpha_i| <= q, which is the elementary bound (E2 on M_n = O(q^n)). Consistent.
   Dichotomy: the base alpha_i^3 either has net coefficient != 0, giving |alpha_i|^3 <= q^3, or equals a wrong-parity eigenvalue q^2 alpha_j (or t0 q^2), giving |alpha_i|^3 <= q^2 |alpha_j| <= q^3. The conclusion |alpha_i|^3 <= q^3 is true.
   [interpretation only: Weil] |alpha| = sqrt q, so |alpha_i^3| = q^(3/2) < q^(5/2) = |q^2 alpha_j|: no cancellation actually happens.
   Whether (P_3^c) holds at c_1 = -c_2 is not decided here (Claim B's hypothesis fails there, Sigma_2 = Z). What the data say: the wrong-parity eigenvalues are exactly of the form q*beta with beta a h-independent
   eigenvalue (restriction of the fibre class to the plane {c_1 x_1 + c_2 x_3 = 0}, where L_psi(hQ) is trivial; RED), which is the shape step (c) predicts.

### 3.4 k = 4, c_1 + c_2 + c_3 = 0 (planes). PROVED (inequalities) + CHECKED (data)
The wrong-sign class has eigenvalue q^2 in H^4_c(Y,K) (RED: constant quotient Q_l(-2) of R^4 by restriction to the plane P = {x_1 = x_3, x_2 = x_4}; surjectivity of H^4_c(Y,K) -> H^4_c(P,K) is OPEN in RED).
In the geometry of Theorem A: C contains beta = q^2, and the class in H^6_c(G_m x A^4, F) has eigenvalue q beta = q^3.
 * Fibre bound: |beta| = q^2 <= q^((k+1)/2) = q^(5/2). It obeys the bound, with room q^(1/2). Consistency with the data: the fibre sum S_h has main term q^2 (plane), below q^(5/2).
 * The same constant quotient also gives H^1_c(G_m, Q_l(-2)) = Q_l(-2) with eigenvalue q^2 in the RIGHT-parity group H^5 (sign (-1)^(k+1) = -1). Net: R contains +q^3 - q^2 = (q-1) q^2, the sum over h of the constant term q^2.
   CHECKED (exact integers, sum(c) = 0 rows): p = 7, n = 2: R = 110397 against (P-1) P^2 = 115248; p = 11: R = 979 against 1210; D = N_4 - (P-r)^2 has D^2/P^3 <= 0.24 in these rows and 5 to 51 in the generic rows (display).
   Every row satisfies the Parseval bound R^2 <= (P-1)^2 P^5 exactly (True in all).
 * Dichotomy: for base alpha^4 either the net coefficient is nonzero, and |alpha|^4 <= q^(7/2); or it is cancelled by a wrong-parity eigenvalue q beta with |beta| <= q^(5/2), and again |alpha|^4 <= q^(7/2).
   The conclusion is true in both branches (and a priori, with only the elementary |alpha| <= q, it is a real gain). [interpretation only: Weil] |alpha^4| = q^2, the wrong-parity class has modulus q^3, and the right-parity class
   H^1_c(G_m, C) of modulus q^2 has the same sign as T, so cancellation does not occur there either.

## 4. Hypotheses: what is needed and what is not (question 4)
NOT needed: R^k lisse on all of G_m; tameness of anything; the nature or location of the singular points of R^k; f(0) != 0; f squarefree of odd degree (only "L geometrically nontrivial"); any property of Y beyond E3
(affine complement of a hypersurface); the structure of Y at all.
NEEDED:
 (i) L geometrically nontrivial (section 3.1). (ii) All c_i != 0 in F_Q (E1 and E4). (iii) E4 at EVERY h != 0, not only generic h: it makes R^b = 0 for b not in {k, k+1} at the bad points as well, so that the Leray groups are
 exactly those of (b). This holds for every h != 0 (perversity of every P_i needs no generic condition), so it is automatic. (iv) (P_k^c) only at the generic point: R^{k+1} is constructible, so "vanishes on a dense open"
 is the same as "geometric generic stalk is 0". A vanishing at ONE closed point h_0 would not be enough (a constructible sheaf of positive generic rank may have zero stalks at special points). So "(P_k^c) for generic h" is the right
 and sufficient hypothesis; nothing at special h is needed.

## 5. Remaining risks (none is an error in Claim A)
 1. E4 is cited, not re-derived by me: Laumon 1987, 1.3.2.3 (t-exactness of FT), BBD 4.1.1/4.1.2 (affine morphisms), SGA 4 XIV 3.1 (Artin). NOT OPENED by me. Report LIT (round 2) says it OPENED Laumon 1.2.2.1, 1.3.1.1, 1.3.2.3 and
    searched for weights: none. I treat E4 as weight-free on that report's word. Other inputs not opened by me: Kunneth for H_c, Grothendieck-Lefschetz trace formula, proper base change, Poincare duality on curves (SGA 4, SGA 4 1/2), cited only.
 2. E1 and E2 are the round-one Lean theorems; I did not re-run Lean. I re-derived the k = 2 case of E1 by hand (|S|^2 <= Q (sum |t|^2)^2).
 3. The checks in section 3 test identities and bookkeeping (closed forms, signs, wrong-parity terms), not the cohomological inputs.
 4. Novelty: this is the familiar "bound the eigenvalue from a fibre where all classes have one sign, then transport it by a constant quotient" device. I did not search the literature; partial overlap with Katz-Laumon / Laumon 1987 is plausible. HINT only.

## 6. Verdict and corrected theorem

Theorem A' (verified). F_q odd; F_Q/F_q finite; psi nontrivial on F_Q; f in F_q[x] not a constant times a square in F-bar[x]; L = L_chi(f) on {f != 0}, j its inclusion, H = H^1_c(A^1_Fbar, j_!L) with Frobenius eigenvalues alpha_i over F_q;
k >= 2; c in (F_Q^*)^(k-1); F = (external product of j_!L) tensor L_psi(h Q_c(x)) on G_m x A^k over F_Q. Assume (P_k^c): H^{k+1}_c(A^k_Fbar, F_h) = 0 at the geometric generic point of G_m.
Then for every embedding iota of Q-bar_l in C and every i, |alpha_i|^k <= q^((k+3)/2).
Proof: section 2, with the correction that the wrong-parity group is a QUOTIENT of H^2_c(G_m, R^k) = C(-1), not equal to it.

Changes to the brief's Claim A:
 1. "The wrong-parity group H^{k+2}_c(G_m x A^k, F) is H^2_c(G_m, R^k)": say "is the cokernel of d_2: H^0(R^{k+1}) -> H^2_c(G_m,R^k)", a quotient of C(-1). The theorem is unaffected.
 2. Add the hypotheses: L geometrically nontrivial (fails for t = 1, where the conclusion is false for k even >= 4 although (P_k^c) holds); all c_i != 0 in F_Q; E4 at every h != 0 (automatic).
 3. (P_k^c) may be stated at the geometric generic point; a single closed point does not suffice.
 4. "alpha of largest modulus" is unnecessary: the argument applies to every alpha_i.
I found no error in the logic of steps (a) to (f).

## 7. Files
Script ./round3/compute/A/check_A.py ; output ./round3/compute/A/check_A_out.txt ;
this report ./round3/reports/A-reduction-referee.md
