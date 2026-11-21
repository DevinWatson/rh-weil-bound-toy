# B-fourier-induction: Claim B in general (round 3, agent B)

Status line (written early, to be refined below): my own derivation reproduces the brief's Sigma_i and the cancellation of h.
Everything below about character sums over finite fields (Weil 1948). Nothing here concerns the Riemann Hypothesis for the integers.

## PART 0. Dimension formula (written early for the exact-computation agent)

Notation: d = deg f, r_i = generic rank of P_i (= rank of the lisse sheaf M_i), eps_k = 1 if k odd, 0 if k even.
Derived by Euler-Poincare (CITED/derived, section 4 below), under the hypothesis of Claim B (Z disjoint from Sigma_i, i<=k-1; f(0)!=0; d odd):

    r_1 = 1, r_2 = d, r_(i+1) = d r_i + r_(i-1)   (Fibonacci polynomials F_i(d), F_0=0, F_1=1)
    D_k = dim H^k_c(A^k, F_h) = r_(k+1) - eps_k,  and H^j_c(A^k,F_h) = 0 for j != k  (if Claim B holds).

    r_1=1, r_2=d, r_3=d^2+1, r_4=d^3+2d, r_5=d^4+3d^2+1, r_6=d^5+4d^3+3d, r_7=d^6+5d^4+6d^2+1
    D_1 = d-1
    D_2 = d^2+1
    D_3 = d^3+2d-1
    D_4 = d^4+3d^2+1
    D_5 = d^5+4d^3+3d-1
    D_6 = d^6+5d^4+6d^2+1
    d=3: D_1..D_6 = 2, 10, 32, 109, 359, 1189.   d=5: D_1..D_6 = 4, 26, 134, 701, 3639, 18901.   d=1: 0, 2, 2, 5, 7, 13.
    Same numbers as an Euler characteristic: (-1)^k chi_c(A^k, F_h) = D_k whenever the hypothesis of Claim B holds (the Euler
    characteristic uses the same induction, so it is not independent of the hypothesis).
    Exact test (d=1, q=3): Hankel ranks of n -> S_h(F_(3^n)) are 2, 2, 5 for k = 2, 3, 4: matches D_2, D_3, D_4 (section 6).
    Where the hypothesis fails (k=3, c=(1,-1); k=5, c=(1,1,1,1)) the ranks are 1 and 6, not 2 and 7.

(Part 0 numbers were first derived from the induction of sections 3-4; they are now partly CHECKED, see section 6.)

## SUMMARY OF FINDINGS (read this first)

1. **I find no error in Claim B.** I rewrote the induction as a proof with numbered steps (section 1). Every step reduces to an explicit
   statement of Laumon 1987, Katz-Laumon 1985, BBD, or the Grothendieck-Ogg-Shafarevich formula, all weight-free as far as I could read
   (table in section 2). Status: **PROVED modulo CITED theorems** (Fourier exactness and involutivity, stationary phase for the Fourier
   transform on A^1, structure of simple perverse sheaves on a curve, GOS, surjectivity of pi_1 under removing points). The Laumon, Katz-Laumon and BBD
   statements were OPENED in the dump (OCR is rough; garbled formulas are flagged). Nothing in the induction uses weights, purity or the Weil bound.
2. **I derived the sets Sigma_i myself and get exactly the brief's Sigma_1 = {0}, Sigma_2 = rho_2 Z, Sigma_i = rho_i (Z u Sigma_(i-2)); h cancels.**
   I also get the exact parity pattern (0 is singular for Q_i iff i is odd), and a derivation of the singular set from Grothendieck-Ogg-Shafarevich
   and proper base change alone (section 3.1), so the location of the finite singular points does not depend on Laumon 2.3.3.1.
3. **Two small repairs to the sketch, neither fatal.**
   (a) R' must contain the ratio 1 (z' = z), i.e. rho_i = 1 must be excluded. I write R = {z'/z : z, z' in Z}, with 1 in R.
   (b) "P_(i+1) is irreducible" needs the surjection pi_1(V - Z) -> pi_1(V) (SGA 1 V 8.2) and transitivity of middle extension (step 5 below);
   the sketch says "irreducible" without these. Both are weight-free.
4. **The hypothesis of Claim B is sufficient, not necessary.** If Q_i is singular at a root z, P_(i+1) = j_!(...) is in general reducible (a
   skyscraper at z appears), the induction as stated stops, but the conclusion can survive. Exactly computed example: d = 1, q = 3, k = 3,
   c = (1,-1) (rho_2 = 1, hypothesis fails): the fibre sum is S = -q^n chi_n(-a), one eigenvalue of weight 2, so the fibre has cohomology
   (apparently) in degree 3 only but of dimension 1, not D_3 = 2 (sections 5, 6).
5. **Dimension formula, tested by exact computation (d = 1, q = 3, exact integers in Z[omega], exact Hankel ranks over Q(omega)):** ranks 2, 2, 5 for
   k = 2, 3, 4 = D_2, D_3, D_4 of section 0/4. Where the hypothesis fails (k = 3 with rho_2 = 1; k = 5 with rho_4 rho_2 = 1) the rank is 1 and 6, not 2 and 7.
   That is the expected behaviour (section 6).
6. **Novelty warning.** The skeleton (FT preserves simple perverse sheaves; singularities by stationary phase; irreducibility of the twist by pi_1-surjectivity)
   is the standard Katz-Laumon apparatus. I did not open Katz or Kiehl-Weissauer, and I did not find Claim B stated in this form in what I opened. That does not
   mean it is not in the literature (OPEN).

## 1. The induction as a proof with numbered steps

Throughout: k-bar algebraically closed of characteristic p odd, l != p, psi a nontrivial character of F_p, all sheaves geometric. f squarefree of degree d >= 1,
Z its roots, f(0) != 0. L = L_chi(f): rank one, lisse on A^1 - Z, tame, I_z acts by the quadratic character at each z (simple root, p odd).
c_1..c_(k-1) nonzero, h != 0. rho_i = -c_(i-1)/c_i (2 <= i <= k-1). R = {z'/z : z, z' in Z} (so 1 is in R).
FT_b(K) = Rpr'_!(pr^*K tensor L_psi(b x x'))[1] (this is x' -> b x' composed with Laumon's FT of 1.4.1.1).

**Step 0 (Fubini, shifts; task point (a)).** Put G_1 = j_!L, G_(i+1) = j_!L tensor Rpr'_!(pr^*G_i tensor L_psi(h c_i x x')) (no shift), P_i := G_i[i].
Then P_1 = j_!L[1] and P_(i+1) = (j_!L) tensor FT_(h c_i)(P_i): FT_b(G_i[i]) = Rpr'_!(...)[i+1], and G_(i+1)[i+1] = j_!L tensor that.
The sheaf F_h on A^k is (box product of j_!L) tensor L_psi(h Q_c). Integrate x_1 out with the projection formula for Rpr_! (SGA 4 XVII 5.2.9, the tool Laumon uses in 1.2.2.1), get G_2(x_2) = j_!L(x_2) tensor Rpr_!(...), then x_2, and so on. Hence
    H^m_c(A^k, F_h) = H^m_c(A^1, G_k) = H^(m-k)_c(A^1, P_k).                         (PROVED; formal; no weights)

**Invariant (I_i)**, for 1 <= i <= k. S_i := finite set where M_i is not lisse.
 (1) P_i = j_!*(M_i[1]), M_i nonzero irreducible lisse on A^1 - S_i; so P_i is a simple perverse sheaf;
 (2) Z is contained in S_i and each z in Z acts on M_i by the scalar -1 (stalk of P_i at z is 0);
 (3) M_i is tame at every point of S_i;
 (4) as I_inf-module M_i,inf = T^0 + sum over a in A_i of L_psi(a y) tensor T^a, with T^0, T^a tame, A_i a finite subset of k-bar^* (slopes 0 or 1 only);
 (5) A_i = h c_(i-1) (S_(i-1) - {0}) for i >= 2, and T^0 != 0 iff 0 in S_(i-1) (i >= 2); for i = 1: A_1 empty, T^0 = L_inf, one-dimensional.

**Step 1 (i = 1).** P_1 = j_*L[1] = j_!L[1], simple by BBD 4.3.1(ii), M_1 = L, S_1 = Z, tame everywhere. (1)-(5) hold. PROVED.

**Step 2 (Fourier preserves simplicity and type; task points (b), (c)).** Let P = P_i satisfy (I_i), Q := FT_(h c_i)(P).
 - Q is a simple perverse sheaf: Laumon 1.3.2.3 (FT is t-exact, an equivalence of abelian categories) and 1.3.2.4 (simple to simple).
 - Types (BBD 4.3.1(ii), Laumon 1.4.2): a simple perverse sheaf on A^1 is (T1) punctual, or (T2) lisse on all of A^1 of the form L_psi(x s') tensor (constant)[1], or (T3) j_!*(F[1]) with F irreducible, no L_psi subquotient.
   P is not (T1) (generic rank >= 1), not (T2) (its stalk at z in Z is 0, but its generic rank is >= 1, so it is not lisse). So P is (T3), and by Laumon 1.4.2.1(ii) FT exchanges (T3) and (T3'):
   Q = j_!*(M'[1]), M' irreducible lisse on V = A^1 - Sing(Q), Sing(Q) finite and Q not punctual. CITED, OPENED.

**Step 3 (stationary phase).** Facts (derived in section 3):
 (i) Sing(Q) - {0} = { -a/(h c_i) : a in A_i }, and 0 is in Sing(Q) iff T^0 != 0; the drop of rank at -a/(h c_i) is dim T^a and at 0 is dim T^0; the generic rank of Q is r(Q) = sum over s in S_i of a_s(P).
 (ii) Q is tame at its finite singular points, and Q_inf = sum over s in S_i of L_psi(h c_i s y) tensor E_s, with E_s tame of dimension a_s(P) (slope 0 for s = 0); no other contribution.

**Step 4 (multiplication by j_!L; task points (a), (d)).** Assume Z cap Sing(Q) = empty. P_(i+1) = (j_!L) tensor Q is the extension by zero over Z of N = (L tensor Q)|(A^1 - Z).
L is lisse on A^1 - Z, and tensoring with a lisse rank-one sheaf is a t-exact autoequivalence compatible with j_!*, so N = j_!*((L tensor M')|_(V - Z)[1]).
At z in Z, Q is lisse, so I_z acts on (L tensor M')_eta by the scalar -1: no invariants, no coinvariants, hence (Rj_*N)_z = 0 and j_!N = Rj_*N = j_!*N.
So P_(i+1) = j_!*(M_(i+1)[1]) with M_(i+1) = (L tensor M')|_(V-Z) lisse, S_(i+1) = Z u Sing(Q) (disjoint), I_z = -1 for z in Z, tame at Z (L tame, Q lisse) and at Sing(Q) (Step 3(ii)).

**Step 5 (irreducibility).** M' is an irreducible pi_1(V)-representation. pi_1(V - Z) -> pi_1(V) is surjective (SGA 1 V 8.2: V normal connected, V - Z dense open; CITED, NOT OPENED). Restriction along a surjection preserves irreducibility; tensoring with a character does too.
So M_(i+1) is irreducible and P_(i+1) = j_!*(M_(i+1)[1]) is simple (BBD 4.3.1(ii)). Together with Step 4 this is (I_(i+1))(1)-(3).
This is the only place (with Step 4) where Z cap Sing(Q_i) = empty is used.

**Step 6 (infinity).** L_inf is tame; M_(i+1),inf = L_inf tensor Q_inf has shape (I_(i+1))(4) with A_(i+1) = h c_i (S_i - {0}) and T^0_(i+1) = L_inf tensor E_0 (nonzero iff 0 in S_i). That is (I_(i+1))(4),(5).

**Step 7 (the end; task point (f)).** i = k: P_k = j_!*(M_k[1]) with M_k irreducible lisse and I_z = -1 on it for z in Z (nonempty), so M_k is nontrivial, hence not geometrically constant.
 - H^j_c(A^1, P_k) = 0 for j < 0: Artin vanishing for the affine curve A^1 and a perverse sheaf (BBD 4.1.1/4.1.2, SGA 4 XIV); concretely H^(-1)_c(P_k) = H^0_c(A^1, j_*M_k) = 0 since j_*M_k has no sections with compact support on the connected non-compact curve A^1.
 - H^1_c(A^1, P_k) = H^2_c(A^1, j_*M_k) = coinvariants of pi_1(A^1 - S_k) on (M_k)(-1) = 0 since M_k is irreducible and nontrivial (SGA 4 IX / the usual trace computation on a curve; weight-free).
 - H^j_c(A^1, P_k) = 0 for j >= 2 (a sheaf in degree -1 on a curve has H^i_c = 0 for i > 2).
By Step 0, H^m_c(A^k, F_h) = H^(m-k)_c(A^1, P_k) = 0 for m != k. **This is Claim B**, for every h != 0 (h only enters through the nonzero factors h c_i).

## 2. Statements used, numbers, quotations, weight status

(OCR of the dump is rough, quotations are the legible parts. Everything below is in LAU.txt, KL.txt or BBD.txt, which I opened; SGA 1, Raynaud, Katz, Deligne-Laumon Asterisque 83 were NOT OPENED.)

| # | statement | key sentence (OCR) | weights? |
|---|---|---|---|
| L1 | Laumon 1.2.2.1, 1.2.2.3: FT'∘FT(K) = sigma^*K(-r); FT an equivalence | "Théorème (1.2.2.1). — ... F'oF(K) ≅ σ*K(-r)" | no; proof = proper base change + projection formula (read) |
| L2 | Laumon 1.3.1.1 = KL 2.1.3: forgetting supports is an isomorphism on FT | "la flèche d'oubli des supports ... est un isomorphisme" | no; KL 2.4.1-2.4.4 proof by local acyclicity of P^1 x A^1 for L_psi(xy), Artin-Schreier cover, [SGA 4 1/2 Th. finitude] (read) |
| L3 | Laumon 1.3.2.3: FT sends perverse to perverse, equivalence of abelian categories | "F transforme les Ql-faisceaux pervers sur E en ... sur E'" | no; proof uses BBD 4.2.5, 4.1.2, 4.1.1 and L2 (read) |
| L4 | Laumon 1.3.2.4, 1.4.2, 1.4.2.1(ii): simple to simple; types T1,T2,T3; FT exchanges T3 and T3' | "(ii) F échange les types (T3) et (T3')" | no (read) |
| L5 | Laumon 2.2.1.1: for perverse K smooth at x iff a_x(K) = 0 iff r_x(K) = r(K); 2.2.1.2 Grothendieck-Ogg-Shafarevich | "a_x(K) = 0 ... r_x(K) = r(K)" ; GOS "[Ra] et [SGA 5] X 7" | no |
| L6 | stalk of FT by proper base change: r_(s')(K') = -chi_c(A⊗k-bar, K ⊗ L(x s')) (proof of Laumon 2.3.1.1) | line 1085 of LAU.txt | no |
| L7 | Laumon 2.3.1.3(i): F_inf nonzero purely of slopes < 1 => U' = A' - {0'}, r(K') = sum deg(s) a_s(K) | "Si le G_inf-module F_inf est non nul et purement de pentes < 1, alors ... U' = A' - {0'}" | no |
| L8 | Laumon 2.3.2 exact sequence 0 -> H^(-1)(K'_(s')) -> F'_(eta s') -> R^(-1)Phi -> 0 for K perverse | "Comme K' est pervers, cette suite exacte longue se réduit à la suite exacte" | no (SGA 7 XIII only) |
| L9 | Laumon 2.3.3.1: (ii) R^i Phi = 0 for i != -1; (iii) K'_(inf') = ⊕_(s in S) Ind R^(-1)Phi_(s,inf') ⊕ R^(-1)Phi_(inf,inf') | "(iii) on a un isomorphisme fonctoriel en K ∈ Perv(A) ..." (garbled) | no; from 1.3.1.2 (= L2's input) and SGA 7 XIII 2.1.7.1 |
| L10 | Laumon 2.4.3: (i)b F^(0,inf') exact, r(F(V)) = r(V)+Sw(V); (ii)b F^(inf,0') on slopes < 1: rank r - Sw; (iii)b F^(inf,inf')(V) = 0 for V of slopes in [0,1] | "(iii) b) Pour tout V ∈ ob G_[0,1] , F^(inf,inf')(V) = 0" | no; 2.5.3 uses Gabber-Katz 2.2.2.2 (Katz, NOT OPENED) and Gauss sums as modules; 2.5.5 uses involutivity + GOS |
| L11 | Laumon 2.5.3.1: F^(0,inf')(Q_l) = Q_l(-1), F^(inf,inf')(Q_l) = 0; Kummer characters go to Kummer characters twisted by a Gauss-sum module | as stated | no |
| B1 | BBD 4.3.1(i),(ii): finite length; j_!*(irreducible lisse[dim]) simple; every simple perverse sheaf is of this form | "j_!*(L[dim V]) est un faisceau pervers simple sur X. Tous les faisceaux pervers simples sont ainsi obtenus." | no |
| B2 | BBD 4.1.1, 4.1.2 (affine morphisms), 4.2.5 (smooth pullback) | grepped, BBD.txt line 11770 | no |
| S1 | SGA 1 V 8.2: pi_1(U) -> pi_1(X) surjective | NOT OPENED | no |

My section 3.1 avoids Deligne's Swan semicontinuity (Laumon 2.3.2.4, via Laumon Asterisque 83, NOT OPENED); it uses only proper base change and GOS.

## 3. The recursion, derived (task point (e) and task item 3)

### 3.1 Singular set of Q = FT_b(P) from GOS alone (b = h c_i)
Let P = j_!*(M[1]), M lisse on U = A^1 - S, tame at S, slopes at infinity in [0,1], M_inf = T^0 + sum_a L_psi(a y) tensor T^a, rank r, stalk dimension m_s = dim M^(I_s).
By proper base change (L6) the stalk of Q at w is H^0_c(A^1, P tensor L_psi(b w x)) = H^1_c(A^1, j_*M tensor L_psi(b w x)). The group H^0_c is 0 (no compactly supported sections) and H^2_c = 0 for the type (T3) of Step 2 (no constant quotient).
GOS (L5) on P^1 for the extension by zero gives chi_c(A^1, j_*M tensor L_psi(b w x)) = r (1 - |S|) - Sw_inf(M tensor L_psi(b w x)) + sum_s m_s, so
   dim Q_w = sum over s in S of (r - m_s) + Sw_inf(M tensor L_psi(b w y)) - r.
Swan at infinity: the part L_psi(a y) tensor T^a becomes L_psi((a + b w) y) tensor T^a: Swan = dim T^a if a + b w != 0 (slope 1) and Sw(T^a) = 0 if a + b w = 0 (T^a tame). The part T^0 has Swan 0 if b w = 0... more precisely
T^0 tensor L_psi(b w y) has Swan dim T^0 for w != 0 and 0 for w = 0. So:
 - generic w: Sw_inf = r, so r(Q) = sum over S of (r - m_s) = sum a_s(P) (all finite points tame);
 - w != 0: drop = r(Q) - dim Q_w = dim T^a if w = -a/b for a in A (else 0);
 - w = 0: Sw_inf = r - dim T^0, drop = dim T^0.
Since Q = j_!*(M'[1]) (Step 2), Q_w = (M')^(I_w), and w is a singular point iff drop > 0 (L5 (i) <=> (iii)). Therefore
   Sing(Q) - {0} = { -a/b : a in A_i, T^a != 0 }, and 0 in Sing(Q) iff T^0 != 0.        (PROVED from L5, L6; weight-free)

### 3.2 Tameness; infinity of Q
By L8, L9(iii): Q_inf = sum over s in S of L_psi(h c_i s y) tensor E_s (translation by s: L_psi(x + s, y) = L_psi(x,y) tensor L_psi(s, y)); the (inf,inf') term vanishes by L10(iii)b because all slopes of P at infinity are <= 1.
E_s is the vanishing-cycle module of the perverse sheaf P at s. Using 0 -> j_!F -> j_*F -> i_*W -> 0 at s (F = M near s, W the stalk), the module for j_!F is F^(0,inf')(V_s) (tame of rank r(V_s) for V_s tame, L10(i)b, Sw = 0), and the module for i_*W is W with trivial action twisted by the rank-one L_psi(s y). E_s is a sub-quotient/extension of these: tame
(wild inertia is pro-p; an extension of tame modules is tame because the p-group acts through a finite quotient on each graded piece, trivially in characteristic-0 coefficients, so unipotently and with finite order, hence trivially). dim E_s = a_s(P) by section 3.1 (total rank of Q).
[HONEST NOTE: the dump has no single sentence "E_s is tame of rank a_s for the intermediate extension"; I assembled it from L8-L11. My sign bookkeeping of the long exact sequence of vanishing cycles for 0 -> j_!F -> j_*F -> i_*W -> 0 was not
consistent with dim E_s = r - m_s + Sw (it gave r + m_s + Sw), so I take the DIMENSION from the stalk/GOS computation (3.1, solid) and use the sequence only for tameness, where the sign does not matter.]
Tameness at finite w != 0: L8 gives 0 -> Q_w -> (generic stalk) -> R^(-1)Phi_w -> 0, Q_w is the invariants (trivial action), and R^(-1)Phi_w(Q) = F^(inf,0')(T^a) (translate; L9(iii)'s sibling 2.3.2.1(iii), 2.4.2.1(ii)) is tame since T^a is tame (L10(ii)b: Swan(F^(inf,0')V) = Sw(V) = 0).
At w = 0 the same with T^0. So Q is tame at all finite points. PROVED modulo L8-L10.

### 3.3 The recursion for Sigma_i
By 3.1, with b = h c_i and (I_i)(5): Sing(Q_i) - {0} = { -h c_(i-1) s/(h c_i) : s in S_(i-1) - {0} } = rho_i (S_(i-1) - {0}); **h cancels**; and 0 in Sing(Q_i) iff 0 in S_(i-1) (i >= 2), 0 in Sing(Q_1).
With S_(i-1) = Z u Sing(Q_(i-2)) (Step 4, disjoint union) and 0 not in Z:
   Sing(Q_1) = {0};  Sing(Q_2) = rho_2 Z (S_1 = Z contains no 0, so 0 is not singular for Q_2);
   Sing(Q_i) = rho_i (Z u Sing(Q_(i-2))) for i >= 3 (a point 0 in Sing(Q_(i-2)) is carried to 0).
So Sing(Q_i) is contained in Sigma_i with Sigma_1 = {0}, Sigma_2 = rho_2 Z, Sigma_i = rho_i (Z u Sigma_(i-2)): **exactly the brief's sets**, with equality unless two different points of S_(i-1) give the same point (then the drops add; irrelevant for vanishing). 0 is in Sigma_i iff i is odd.
Closed form: Sigma_i = { (rho_i rho_(i-2) ... rho_(i-2m)) z : z in Z, 0 <= m <= floor(i/2) - 1 } u ({0} if i odd).
Z cap Sigma_i = empty iff all products pi_(i,m) = rho_i rho_(i-2) ... rho_(i-2m) (0 <= m <= floor(i/2) - 1) lie outside R, and, for i odd, 0 is not in Z (f(0) != 0).
pi_(i,m) = (-1)^(m+1) prod_(a=0..m) c_(i-1-2a)/c_(i-2a), a nontrivial Laurent monomial, so each condition removes a translate of a proper subtorus of the torus of (c_1..c_(k-1)); finitely many conditions, none depends on h.

### 3.4 Conditions on c for k = 2..6 (need Z cap Sigma_i = empty for i <= k-1; f(0) != 0 for k >= 2)
 | k | conditions (R contains 1) |
 |---|---|
 | 2 | none on c |
 | 3 | rho_2 not in R |
 | 4 | rho_2, rho_3 not in R |
 | 5 | rho_2, rho_3, rho_4, rho_4 rho_2 not in R |
 | 6 | rho_2, rho_3, rho_4, rho_5, rho_4 rho_2, rho_5 rho_3 not in R |
 (k = 7 adds rho_6, rho_6 rho_4, rho_6 rho_4 rho_2.) In c: rho_2 = -c_1/c_2, rho_3 = -c_2/c_3, rho_4 rho_2 = c_3 c_1/(c_4 c_2), rho_5 rho_3 = c_4 c_2/(c_5 c_3).
 The brief's Remark (a) is confirmed: for the all-ones quadric rho_i = -1 and rho_4 rho_2 = 1 is in R, so the hypothesis fails for every k >= 5 (holds for k <= 4 iff -1 is not in R).

## 4. Dimension formula, derivation

Under the hypothesis: r_1 = 1; r_(i+1) = r(Q_i) = sum over S_i of a_s(P_i) = d r_i (each root: stalk 0, drop r_i) + (sum of the finite drops of Q_(i-1)) = d r_i + r_(i-1), because by 3.1 the finite drops of Q_(i-1) are the dim T^a and dim T^0 of P_(i-1) at infinity, which add up to r_(i-1) (for i - 1 = 1: L_inf, dimension 1).
So r_i = F_i(d) with F_0 = 0, F_1 = 1, F_(n+1) = d F_n + F_(n-1): r = 1, d, d^2+1, d^3+2d, d^4+3d^2+1, d^5+4d^3+3d, d^6+5d^4+6d^2+1.
D_k = dim H^0_c(A^1, P_k) = -chi_c(A^1, j_*M_k) = sum_(s in S_k) a_s(P_k) + Sw_inf(M_k) - r_k = r_(k+1) + (r_k - eps_k) - r_k = r_(k+1) - eps_k, eps_k = dim T^0(P_k) = 1 for k odd, 0 for k even
(T^0(P_k) != 0 iff 0 in S_(k-1) iff k - 1 is even, k >= 2; its dimension is the drop of P_(k-1) at 0 = dim T^0(P_(k-2)) = ... = 1). Equivalently D_k = dim of the stalk of Q_k at 0 (L6 at w = 0: stalk at 0 is the cohomology), r_(k+1) minus the drop eps_k at 0: a consistency check of the two derivations.
   D_1 = d - 1;  D_2 = d^2 + 1;  D_3 = d^3 + 2d - 1;  D_4 = d^4 + 3d^2 + 1;  D_5 = d^5 + 4d^3 + 3d - 1;  D_6 = d^6 + 5d^4 + 6d^2 + 1.
 d = 3: 2, 10, 32, 109, 359, 1189.   d = 5: 4, 26, 134, 701, 3639, 18901.   d = 1 (f = x - a): 0, 2, 2, 5, 7, 13.
 Independent direct check of D_2 (not through the induction): the pushforward of j_!L tensor L_psi(h c x_1 x_2) to the x_2-line has rank d on G_m (chi_c = (1 - d) - 1 = -d on a fibre x_2 != 0) and stalk d - 1 at 0;
 chi_c(A^1, j_!L tensor G) = d (1 - (d+1)) - Sw_inf + (d - 1) with Sw_inf = d (d frequencies h c_1 z, slope 1) = -d^2 - 1. So D_2 = d^2 + 1 (CHECKED by hand; and by data at d = 1, section 6).
 If Claim B holds then S_h(F_(q^n)) = (-1)^k sum_(j=1..D_k) beta_j^n (Grothendieck-Lefschetz).

## 5. Delicate points, settled, and known cases

(a) Shifts and t-structure: Step 0 and Step 4. P_1 perverse (j affine, BBD 4.1.1/4.1.2), FT t-exact (L3), P_(i+1) is simple perverse by Steps 4-5 (not by a t-exactness claim about tensoring with j_!L, which is not available in general).
(b) FT preserves simple perverse sheaves: L3, L4 (OPENED). (c) P_i not punctual and not of the form L_psi(a x)[1]: Step 2 (via "not lisse on A^1": stalk 0 at roots, generic rank >= 1). The brief's wording "ramified at the roots" is equivalent but the stalk argument is cleaner.
(d) At a root where Q_i is lisse: Step 4. At a root z where Q_i is singular: j_!N != j_*N iff I_z has a (-1)-eigenvector on the generic stalk of Q_i; then P_(i+1) has a skyscraper constituent at z (length >= 2), FT_(h c_(i+1)) of it is L_psi(h c_(i+1) z y)[1] (rank one, lisse), so Q_(i+1) is no longer simple. The induction must then be run on composition factors, and the final vanishing needs H^1_c(each factor) = 0:
   a factor L_psi(a y) tensor tame [1] (a lisse rank-one nonconstant factor) has H^1_c = 0; a constant factor Q_l[1] has H^1_c = Q_l(-1) != 0. OPEN: not pushed through; the example below suggests constant factors do occur when rho = 1.
(e) Stationary phase, point 0 and slope 0: sections 3.1-3.3. "Tame at finite points and sum of L_psi(linear) tensor tame at infinity" propagates (it is (I_i)(3),(4)). 0 is singular for Q_i iff i is odd. The slope-0 part of P_i at infinity is nonzero iff i is odd, of dimension 1.
(f) Final step: Step 7.

Known cases:
 * **k = 3, c_1 = -c_2** (rho_2 = 1): Sigma_2 = Z, the hypothesis FAILS, Claim B says nothing. Direct look: Q = c_1 x_2 (x_1 - x_3), so S_h = sum_(x_2) t(x_2) A(x_2) A(-x_2) with A = FT_(h c_1)(t); as a sheaf: L tensor Q_1 tensor (-1)^*Q_1 = L tensor End(Q_1)(-1), whose trivial summand L(-1) contributes a copy H(-1) of H = H^1_c(A^1, j_!L) to H^3_c of every fibre, constant in h (HINT: hand derivation; weights used only to say "wrong parity"). This is the geometrically constant quotient mechanism of Claim A, with beta = alpha_i. For d = 1: H = 0 and the exact data show S = -q^n chi_n(-a), one eigenvalue -q (weight 2), in H^3, dimension 1 (CHECKED: Hankel rank 1, section 6; the identity S_n = -q^n chi_n(-a) I derived by hand and it matches S_13 = 3^13 for a = 1).
 * **k = 4, c_1 + c_2 + c_3 = 0**, e.g. c = (1,1,-2): rho_2 = -1, rho_3 = 1/2; both outside R for generic f, so Claim B applies: fibres have cohomology in degree 4 only, dimension d^4 + 3d^2 + 1, for every h != 0. The failure of the sign statement for Y is then not a failure of Claim B; in Claim A's language it sits in H^2_c(G_m, R^4) = coinvariants of R^4, a geometrically constant quotient of the generic local system R^4. Claim B does not say whether such a quotient exists; Claim A says it is harmless. (OPEN: not tested here whether R^4 has a constant quotient at c_1 + c_2 + c_3 = 0; round two's planes indicate yes.)
 * The plain all-ones quadric at k >= 5: hypothesis fails (rho_4 rho_2 = 1). Exact data (d = 1, q = 3, k = 5, c = (1,1,1,1)): Hankel rank 6, not 7.

## 6. Exact test of the dimension formula, d = 1 (CHECKED)

Script `compute/B/fibre_p3.py` (drivers `driver.py`, `driver2.py`; analysis `hankel.py`; outputs `p3_sequences_n13.json`, `hankel_out_n12.txt`, `hankel_out_n13.txt`).
It computes S_h(F_(3^n)) = sum_x t(x_1)...t(x_k) psi(h Q_c(x)) exactly as a + b omega in Z[omega] (int64 pairs; exact 3-point DFT along the n coordinates of F_3^n; Gram matrix Tr(x^(i+j)) for psi(Tr(h c x y)); t(x) = chi(x - a)), for n = 1..13, f = x - a, q = 3, h = 1. Hand check at n = 1, k = 2, a = 1: S = -1 + omega, equals the script's first term.
`hankel.py` computes the exact rank of the Hankel matrices (s_(i+j+1)) over Q(omega) by Gaussian elimination in Fractions. Hankel rank of sum_j m_j beta_j^n = number of distinct beta_j with nonzero net multiplicity.
| case | hypothesis of Claim B | predicted D_k | exact Hankel rank (13 terms) |
|---|---|---|---|
| k=2, c=(1), a=1; a=2 | holds | 2 | 2; 2 (sizes 2..7 all rank 2) |
| k=3, c=(1,1) | rho_2 = -1 not in R = {1}: holds | 2 | 2 |
| k=3, c=(1,2)=(1,-1) | fails (rho_2 = 1) | formula not applicable | 1 |
| k=4, c=(1,1,1), a=1; a=2 | rho_2 = rho_3 = -1: holds | 5 | 5; 5 (sizes 5,6,7 rank 5) |
| k=5, c=(1,1,1,1) | fails (rho_4 rho_2 = 1) | (7 only under hypothesis) | 6 (sizes 6,7 rank 6) |
The three covered cases match D_2 = 2, D_3 = 2, D_4 = 5; the two uncovered cases do not match the formula.
Limits: (i) this does not show vanishing outside degree k (cancellation between degrees would lower the rank, never raise it); (ii) d = 1 has R = {1}, one root; a test with d >= 3 needs >= 2 D_2 = 20 terms, out of reach; (iii) k = 5 under the hypothesis is out of reach at q = 3 (c in {+-1} forces rho_4 rho_2 = 1) and needs 15 terms at q = 5.
HINT (floating point, `compute/B/eig_hint.py`, `eig_hint_out.txt`): recurrence roots have moduli 3 (k=2, both), 3 and 3^(3/2) (k=3, good), 9 (k=4, all five), 3 (k=3, bad), and 3^(5/2) (five of them) with 9 (one) for k=5 (hypothesis fails). Interpretation (uses Weil/Deligne, NOT used in any proof): H^k pure of weight k in the k = 2, 4 examples, mixed for k = 3.

## 7. What could still break (honest list)

1. CITED, not independently checked by me: SGA 1 V 8.2; Gabber-Katz (inside Laumon 2.5.3); GOS (Raynaud); Laumon Asterisque 83 (avoided).
2. The assembly of E_s (3.2) is mine. Only tameness of E_s is used from it, and that needs only: F^(0,inf') of a tame module is tame (L10, read) plus the elementary p-group argument. The dimension comes from GOS.
3. OCR damage in the dump: if the reader doubts L8/L9/L10 as OCR-garbled, the sentences are at LAU.txt lines 1126-1131 (L8), 1176-1179 (L9), 1285-1324 (L10), 1360-1375 (L11).
4. Coincidences: two points s != s' of S_(i-1) cannot give the same frequency (h c_(i-1) != 0), but two of the points rho_i s can coincide; that merges drops and does not affect vanishing.
5. Parity of d: the induction never uses that d is odd (only that L is tame at infinity, p odd). For d even T^0 is the trivial character of dimension 1 and Q_1 has a nonsemisimple (unipotent) monodromy at 0. Not tested. (The brief restricts to odd d anyway.)
6. Use in Claim A: Claim B holds for all h != 0 once c avoids finitely many translated subtori; such c exist over F_Q for Q large (each condition is a nontrivial monomial equation). Claim A needs only a dense open set of h.

## 8. Novelty

This is the standard Katz-Laumon apparatus (FT preserves simple perverse sheaves; singularities from stationary phase; irreducibility of the twist by surjectivity of pi_1). I did not open Katz ESDE or Kiehl-Weissauer, and did not search the web. I did not find Claim B stated in this form in the sources I opened. OPEN.

## 9. Files
 - ./round3/reports/B-fourier-induction.md
 - ./round3/compute/B/: fibre_p3.py, driver.py, driver2.py, hankel.py, eig_hint.py; outputs p3_sequences.json, p3_sequences_n13.json, hankel_out_n12.txt, hankel_out_n13.txt, eig_hint_out.txt, driver_out.txt, driver2_out.txt
