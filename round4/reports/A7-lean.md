# A7: Lean (S1, S10), round four

Written 2026-11-21 22:57 UTC. Setting: character sums over finite fields (Weil 1948). Nothing here concerns RH for the integers.
Both files compiled with `lean_check.sh` (Lean 4.34.1, Mathlib of ~/mlslice), exit 0, zero `sorry`, axioms printed for every theorem
(output: `round4/compute/A7/ToyWeil.Weighted.log`, `ToyWeil.Unbounded.log`; same logs in `lean/logs/`). Every theorem depends only on
`propext, Classical.choice, Quot.sound`. My own proofs; the companion study's files were not consulted.

## What existed
`Identity.lean`/`Parseval.lean` state `q N = M^k + R` and the fibre bound only for the PLAIN path quadric (all coefficients 1; `pathQuadric`, `gseq` with `psi (h*x*y)`). So item (1) was needed. `Endgame2.lean` `endgame_fibres` assumes one fixed field for all k >= 2 (the draft's own flagged mismatch, S10). `no_cancellation_signed3` is already field-agnostic.

## (1) `ToyWeil/Weighted.lean` (CHECKED)
Definitions: `pathQuadricW c x = sum_{i<k} c i * x_i * x_{i+1}` on `Fin (k+1) -> F`, `c : N -> F`; `gseqW`, `SsumW`, `NcountW`, `RsumW`.
Theorems (all general field F with Fintype, psi : AddChar F C, psi != 0):
- `pathQuadricW_snoc`, `gseqW_path`, `SsumW_eq_path_sum`: the iterated sums equal the sum over x in F^(n+1) of prod t(x_i) psi(h Q_c(x)). No hypothesis on c.
- `identityW`: `|F| * NcountW c t n = (sum t)^(n+1) + RsumW psi c t n`, k = n+1 variables, NO hypothesis on c (zero coefficients allowed for the identity).
- `gseqW_sq_bound`, `iterated_boundW`: for h != 0 and c 0..c n nonzero, `|SsumW (n+2)| <= sqrt|F|^(n+1) B^n sum |t|^2`.
- `identity_bound_oneW`: for |t| <= 1, n >= 1, c i != 0 for i < n (exactly the k-1 coefficients c_1..c_{k-1} of the draft, 0-indexed): `|q N - M^(n+1)| <= (q-1) q sqrt(q)^n`. This is the form S1/S9 uses ((Q^n-1) Q^{n(k+1)/2} with k = n+1: here q*sqrt(q)^n = q^{(n+2)/2} = q^{(k+1)/2}, matches the draft's fibre bound `|F|^{(k+1)/2}` per h).
Hypothesis check against the draft: draft S1 says "all c_i != 0, h != 0 over every finite field F"; matches. The coefficients are only needed nonzero in the field in which h lives; c_i in F_Q stays nonzero in F_{Q^n}.

## (2) `ToyWeil/Unbounded.lean` (CHECKED)
- `pow_root_step`: x^(s k) <= r^(s (k+3)), s >= 1, x,r >= 0  =>  x^k <= r^(k+3) (exact s-th root, no limit).
- `le_of_pow_le_unbounded`: if for every K some k >= K has x^k <= r^(k+3), then x <= r.
- `endgame_unbounded`: for alpha in C, q > 1, an unbounded set of k each with its own s >= 1 and `|alpha|^(s k) <= q^(s (k+3)/2)` (real power, as in the draft), conclude `|alpha| <= sqrt q`. This is the S10 statement the brief asks for.
- `dichotomy_field_dep`: the signed three-family dichotomy of S9 with explicit field `Q = q^s` and `rho = (q^s)^((k+3)/2)` (it is `no_cancellation_signed3` specialised; fixed k and Q there is no real dependence problem, field degree varying with k only matters across k).
- `endgame_fibres_var`: the full endgame with s depending on k, unbounded set of k (instead of every k >= 2): hypothesis, for each K some k >= K and s >= 1 with families e, b and constant C such that for all n >= 1 `|sum_I (prod_j alpha(I_j)^s)^n + sum e^n - sum b^n| <= C (q^{s(k+3)/2})^n` and `|b_j| <= q^{s(k+3)/2}`; conclusion `|alpha_i| <= sqrt q` for all i. The tensor-power eigenvalues over F_{q^s} are modelled as the products of the s-th powers, as S0/S2 conventions state.

## Referee notes on the draft (S1, S9, S10) from the formalisation
1. S10 is correct as written once the s-th root is taken at the level of real numbers: no error. The "limit in k" is now in Lean (`le_of_pow_le_unbounded`).
2. What the Lean statements do NOT cover, to be kept on the list: (a) that psi_n = psi o Tr is a nontrivial character of F_{Q^n} (trace surjective; standard, not formalised; `identityW` takes psi as given); (b) all cohomological steps S4 to S8, in particular that R_n is the signed trace sum over H^{k+1}_c, H^{k+2}_c: the Lean hypothesis in `endgame_fibres_var` is exactly that identity, so Lean proves "trace identity + bound => eigenvalue bound", not the identity; (c) the constant C: S9 needs `|R_n| <= C rho^n` with C independent of n; the Lean bound gives `|R_n| <= (Q^n-1) Q^{n(k+1)/2} < Q^{n(k+3)/2}`, so C = 1 works, but the step from `identity_bound_oneW` (a bound on q N - M^k = R) to the hypothesis `h` of `dichotomy_field_dep` (where R_n is rewritten as the signed eigenvalue sum) is not itself a Lean theorem.
3. Index convention: Lean uses 0-based `c 0..c (k-2)`; the draft's `c_1..c_{k-1}`.
4. No error found in S1, S2, S9 or S10 as stated. Verdict on A7 scope: items (1) and (2) are done.

## Files
`./lean/ToyWeil/Weighted.lean`
`./lean/ToyWeil/Unbounded.lean`
