# B: exact computations over prime fields (footnote 3, path quadric)

Scope: this report is about character sums over F_p only. It says nothing about the Riemann Hypothesis for the integers.
All code and outputs are in `./compute/B/` (called `B/` below).
Labels: PROVED / CITED / CHECKED (exact integer arithmetic; script and output named) / HINT (floating point or heuristic) / OPEN.
Only exact int64 or Python-int arithmetic produces CHECKED figures; the one numerical piece (T4) uses mpmath interval arithmetic and is labelled so.

Notation: t(x)=chi(f(x)), t0=t(0), M=sum t, m=sum t^2 = p - #{roots of f in F_p}, C = sum_x t(x)t(-x), Q_c = c_1x_1x_2+..., N_k(s), N_k=N_k(0), S_h = sum_x prod t(x_i) e(hQ_c(x)), q N_k = M^k + R_k.

## T1. Integer dynamic programme (`B/core.py`, `B/t1_validate.py`, output `B/t1_output.txt`)
- Method: state[v][r] = signed weighted count of (x_1..x_j) with x_j=v, partial Q = r. A transition adds x_{j+1}=w: new[w][r'] = t(w) sum_v old[v][r' - c v w]. For each w the sum over v is a cyclic skew-diagonal sum, done with one strided view; cost p^3 per variable. N_k(0) skips the last transition (cost p^2).
- Overflow margin: every state entry and every partial sum is bounded in absolute value by p^k. `core._guard` asserts p^k < 2^62 (about 4.6e18). Largest case run: k=6, p=601, p^6 = 4.7e16, margin about 100.
- CHECKED: DP vector N_k(s) (all s) and N_k(0) equal brute-force enumeration for all p in {3,5,7,11}, k=1..4, four polynomials (x^3+x+1, x^3-x, x^2+3, x^5+x+1), coefficient vectors c = all-ones plus two random ones: 192 cases, 0 mismatches. The skew-sum DP also equals a naive Python-int DP (nested loops, object dtype) for p in {13,17,23}, k in {3,5}, random c: 24 cases.

## T2. Closed forms for N_2, N_3 (`B/t2_closed_forms.py`, `B/t2_output.txt`)
Derivation (PROVED, elementary):
- k=2: Q=c x1x2 = 0 iff x1=0 or x2=0, so N_2 = 2 t0 M - t0^2 for every c. For s != 0, N_2(s) = sum_{x != 0} t(x) t(s/(c x)).
- k=3: Q = x2(c1x1+c2x3). x2=0 contributes t0 M^2. x2 != 0 forces x3 = -(c1/c2)x1, contributing (M - t0) sum_x t(x)t(-lam x), lam = c1/c2. For c=1: **N_3 = t0 M^2 + (M - t0) C**, C = sum_x t(x)t(-x).
- CHECKED: all formulas hold (also N_2(s) for every s != 0, and the general-c versions with random c) for all 315 pairs (odd prime p <= 199) x (7 polynomials, including x^3-x which has f(0)=0, x^2+1, x^4+x^2-1; bad primes not skipped since only t as a function matters). 0 failures.
- Consequence, PROVED: if f(x)f(-x) = -f(x)^2 (f odd, e.g. x^3-x) then C = chi(-1)(p - #roots), of order p, so N_3 ~ chi(-1) M p ~ p^{3/2}, not p^{(k-1)/2}=p. For f with f(x)f(-x) not a constant times a square, C is a quadratic-character sum with |C| <= (deg - 1)sqrt(p) (Weil, CITED) and N_3 = O(p).

## Table early: `B/n4_table.tsv` (columns f, p, M, N_4; c all ones; 5 polynomials; good primes 3..199; 217 rows). The same columns for good primes up to 653 are in `B/t3_k4.tsv`. Bad primes skipped: x^3+x+1: 31; x^3-x: 2; x^3+2x+5: 7, 101; x^5+x+1: 3, 7, 23; x^5-5x+3: 5, 7 (sympy discriminants; x^3-x at p=3 has t identically 0, row kept with N=0).

## T3. Size of N_k (`B/t3_run.py`, data `B/t3_k4.tsv`, `B/t3_k5.tsv`, `B/t3_k6.tsv`; summaries `B/t3_summary.txt`, `B/t3b_remainder.txt`, `B/t3c_signs.txt`)
- Ranges reached in one 8-minute run per k (all good primes 3..P_k for all five f): **P_4 = 653, P_5 = 613, P_6 = 601** (582, 547, 537 rows).
- CHECKED exact maxima (Fractions) of N_k^2/p^{k-1} over everything computed:
  - k=4: 2096704/29791 ~ 70.38 (x^3+2x+5, p=31). For p >= 100: 9469625344/186169411 ~ 50.87 (x^3+2x+5, p=571). Per-f maxima over all p: 70.4, 42.3, 33.2, 36.1, 38.6 (all five f).
  - k=5: 85598097701776/43617904801 ~ 1962.45 (x^3-x, p=457). Excluding x^3-x the per-f maxima are 68.8 to 294 (294.33 for x^5-5x+3, p=521, explained below; 121 at p=3 for x^3+2x+5).
  - k=6: 125425346122448100/38387392786601 ~ 3267.36 (x^5-5x+3, p=521). Other f: per-f maxima 25.3 (x^5+x+1), 36.9, 79.2 (x^3-x), 280.3 (x^3+2x+5, p=3).
- CHECKED exact maxima of N_k^2/p^k: k=4: 121/9 (p=3); k=5: 121/3 (p=3); k=6: 841/9 (p=3); all at the smallest prime of x^3+2x+5. Ignoring p<50 the maxima are small (windows in `t3b_remainder.txt`): for generic f, N_k^2/p^k in the window p in [300,700) is between 0.03 and 0.57 for every f and k, with two exceptions (k=5 x^3-x: 4.29, discussed below; k=6 x^5-5x+3: 6.27 at p=521, the M^k spike), and otherwise it decreases from window to window.
- Where the large values of N_k^2/p^{k-1} come from (CHECKED, exact): qN = M^k + R, and the M^k part alone, M^{2k}/p^{k+1}, equals 3563.7 (k=6) and 321.4 (k=5) at x^5-5x+3, p=521 (M=-76, M^2/p ~ 11): so those spikes are the M^k term, with M ~ 3.3 sqrt(p) at small p. That term is O((deg-1)^{2k}/p) in N^2/p^{k-1} by Weil (CITED) and decays only like 1/p, invisible at p <= 650 for k=5,6.
- The remainder R = pN - M^k (exact): max R^2/p^{k+1} per window is about 8 to 50 for generic f and all three k with no clear trend (top-window maxima for k=4: 50.9, 41.9, 37.9, 37.6 for the four generic f; k=6: 11.3, 9.0, 8.1, 12.2; k=5: 33.8, 49.9, 42.8, 18.0); R^2/p^{k+2} decreases (0.03 to 0.12 at p in [300,700)). So the data are consistent with **R of size p^{(k+1)/2} times a bounded random-looking constant (HINT, not proved)**, hence N = R/p + M^k/p of size p^{(k-1)/2} for generic f, plus the M^k/p term, which is smaller asymptotically but not at p <= 650.
- Answer to the question "p^{(k-1)/2} or larger?": for the generic polynomials (x^3+x+1, x^3+2x+5, x^5+x+1, x^5-5x+3), N_k^2/p^{k-1} stays in the tens to low hundreds up to p ~ 600 (explained exactly above) and N_k^2/p^k shrinks, so no growth beyond p^{(k-1)/2} is seen in this range (HINT: range small, tails heavy). **For the odd polynomial x^3-x and k=5, N_5 is of size p^{5/2}**: N_5^2/p^5 has window maxima 2.74, 4.98, 4.60, 4.29 (p<50, 50-150, 150-300, 300-700), N_5^2/p^4 grows 79, 483, 1110, 1962. This is larger than p^{(k-1)/2} = p^2 and is the k=5 analogue of the T2 fact for k=3 (an odd f has t(-x) = chi(-1) t(x)). For x^3-x at k=4 and 6 the ratio N^2/p^k decreases (0.06 and 0.16 in the top window).
- Signs (`t3c_signs.txt`, CHECKED counts): N_k takes both signs for every f and k (e.g. k=4: x^3+2x+5: 56 positive, 60 negative; x^5-5x+3: 53 positive, 63 negative). Among rows with N != 0 and M != 0 the sign of N equals the sign of M^k in about half, opposite in about half (k=4 totals: same 254, opposite 244 over the five f). x^3-x, k=5 is the one exception: N=0 in 58 of 110 rows (p = 3 mod 4: PROVED by x -> -x, since chi(-1)^5 = -1) and, when nonzero, N has the sign of M in 52 of 53 rows. There is no fixed sign of N_k at the level of a single prime p.

## T4. Parseval (`B/t4_parseval.py`, `B/t4_parseval.tsv`, `B/t4_summary.txt`)
- PROVED (the trivial bound by iterating Parseval): for h != 0, |S_h| <= m p^{(k-1)/2}. Proof: S_h = a^T F_1 D F_2 D ... F_{k-1} a with a=(t(x))_x, D=diag(t), F_i = (e(h c_i x y))_{x,y}. Each F_i satisfies F_i F_i^* = p I (so operator norm sqrt(p)), ||D||<=1, ||a||^2 = m. Hence |R_k| <= (p-1) m p^{(k-1)/2} and |N_k| <= (M^k + (p-1) m p^{(k-1)/2})/p ~ p^{(k+1)/2}, which is a factor p above the cohomological size p^{(k-1)/2}; the bound does not by itself give the size claimed in the footnote.
- Parseval identity: sum_h |S_h|^2 = p sum_s N_k(s)^2, with S_0 = M^k = sum_s N_k(s).
- CHECKED (exact): sum_s N_k(s) = M^k for all 348 cases (f,p,k): five polynomials, good primes p <= 101 (p=3 x^3-x excluded: t identically 0), k = 4,5,6, c = all ones. N_k(s) for all s from the DP.
- CHECKED (interval arithmetic, mpmath iv at 100 bits, enclosures for every S_h computed as sum_s N(s) exp(2 pi i h s/p), cos/sin tables as intervals): in all 348 cases the exact integer p sum N(s)^2 lies in the enclosure of M^{2k} + sum_{h != 0}|S_h|^2, and every |S_h|^2 has upper endpoint <= p^{k-1} m^2. One case is an exact equality: p=3, x^3+2x+5, k=5, |S_h|^2 = 729 = p^{k-1}m^2; the interval upper endpoint exceeds 729 by less than 1e-20 relative and cannot certify "<=", so it is recorded as TIGHT in the TSV (the bound itself is PROVED above).
- CHECKED (interval upper endpoints): max over h != 0 and p <= 101 of |S_h|^2 / p^k is at most 14.99, 12.35, 13.16 (x^3+2x+5, k=4,5,6), 10.06, 16.57, 11.66 (x^3+x+1), 31.74, 25.46, 26.02 (x^3-x), 11.05, 10.39, 11.48 (x^5+x+1), 10.81, 11.70, 14.22 (x^5-5x+3). So the observed |S_h|^2 is of order p^k (square-root cancellation in k variables), well below the proved p^{k-1}m^2 ~ p^{k+1}: the Parseval bound is off by a factor about p/10 in |S_h|^2 in this range. (OPEN whether this p^{k/2} size of S_h can be proved by an argument of the kind footnote 3 sketches.)

## T5. Strata of N_4 (`B/t5_strata.py`, `B/t5_strata.tsv`, `B/t5_analysis.txt`, `B/t5_check.txt`)
Strata of {x1x2+x2x3+x3x4=0}: A={x3=0,x2=0}, B={x3=0,x2!=0}, Cstr={x3!=0}. The three stratum sums were computed by direct enumeration (O(p^3), independent of closed forms; for x3!=0, x4 = -x2(x1+x3)/x3) for p <= 199, seven polynomials (the five plus x^3+x+3, x^2+x+3), 307 (f,p) cases.
PROVED closed forms (checked below):
- A = t0^2 M^2.
- B = t0^2 M (M - t0)  (x1 must be 0, x4 free).
- Cstr = C1 + C2 + E with C1 = t0^2 M (M - t0) (x2 = 0, forces x4 = 0), C2 = t0 (M - t0)(C - t0^2) (x2 != 0, x1 = -x3, x4 = 0), E = sum_{a != 0} G(a) G(1-a), G(a) = sum_{x != 0} t(x) t(-a x) (put u = x1+x3 = a x3).
- Hence N_4 = t0^2 M^2 + 2 t0^2 M (M - t0) + t0 (M - t0)(C - t0^2) + E.
CHECKED: for all 307 cases the enumerated A, B, Cstr equal the closed forms, and A+B+Cstr equals the DP value N_4: 0 failures.
What the data show (`t5_analysis.txt`; no interpretation beyond this):
- A, B, C1 are >= 0 always (A = t0^2 M^2; B = C1 = t0^2 M(M - t0) = t0^2(M^2 - t0 M) >= 0 for integer M). So A+B+C1 = t0^2(3M^2 - 2 t0 M) >= 0 and is >= M^2 when M != 0: a definite positive sign, but of size about p (since |M| = O(sqrt p) by Weil, CITED), below the p^{3/2} scale of N_4.
- C2 and E take both signs. Counts over primes <= 199 (A/B/C1: positive, negative, zero): C2 has sign counts like 15/24/5 (x^3+x+1); E like 20/23/1; N_4 like 29/15/0 for x^3+x+1 and 21/22/0 for x^5-5x+3. For x^3-x (t0=0) A=B=C1=C2=0 and N_4 = E.
- E/p^{3/2} has mean between -0.66 and +0.50 over p>100 and max absolute value 3.3 to 5.1 (p<=199); no fixed sign. A float64 least-squares fit (HINT only) of E and of N_4 on {p, M^2, t0 M, t0 p, 1} leaves a residual about as large as the data (rms 2849 vs 2958): no polynomial in p, M, t0 is visible in E beyond the exact terms above.
- So over F_p the exact N_4 splits into a nonnegative polynomial part of size p and a part E of size p^{3/2} that takes both signs for each f tested.

## T6. Random coefficient vectors, k=4 (`B/t6_randc.py`, `B/t6_k4_randc.tsv`, `B/t6_summary.txt`, `B/t6b_odd.txt`)
Seed 20261120 (python random.Random, c_i uniform in 1..p-1), three vectors per (f,p), five f, good primes 3..563: 1506 values (CHECKED exact; N_4(0) from the DP, validated against brute force with random c in T1).
- Exact maxima of N_4^2/p^3 with random c, per f: 567009/12167 ~ 46.6 (x^3+2x+5, p=23), 805594689/30080231 ~ 26.8 (x^3+x+1, p=311), 33505105936/95443993 ~ 351.0 (x^3-x, p=457), 1343735649/36264691 ~ 37.1 (x^5+x+1, p=331), 7243371664/141420761 ~ 51.2 (x^5-5x+3, p=521). With c = 1 on the same primes: about 70.4, 42.3, 33.2, 36.1, 38.6. Max N_4^2/p^4 (random c): 13.4 (p=3), 1.17, 1.69, 0.51, 0.80; window maxima for p in [300,700): 0.088, 0.086, 0.768, 0.112, 0.098.
- So for the four non-odd f the size does not change with c: N_4 is of size p^{3/2} times a bounded-looking constant (maxima of N^2/p^3 in the range 25 to 51, mean about 3 to 4 at p in [300,700)), and N^2/p^4 decays. **For x^3-x with random c, N_4 reaches p^2**: N^2/p^4 window maxima 1.09, 1.69, 0.95, 0.77 (p<50, 50-150, 150-300, 300-700) with no decay, e.g. N = 183044 at p=457 (c = (385,53,125)), while with c = 1 the same ratio decays (1.45, 0.13, 0.12, 0.06). The ten largest cases do not satisfy simple relations among c (only 3 of 10 have c_i = +-c_j); no explanation is offered (OPEN). It is an odd-f effect (t(-x) = chi(-1) t(x), and for x -> 1/x one has f(1/x) = -f(x)/x^4); the other four polynomials are not odd.
- Signs of N_4 with random c: both signs for every f (e.g. x^3+2x+5: 168 positive, 132 negative).

## Summary for the main session
1. CHECKED/PROVED: N_2, N_3 closed forms; N_4 stratum decomposition N_4 = t0^2M^2 + 2t0^2M(M-t0) + t0(M-t0)(C-t0^2) + E with E = sum_{a!=0} G(a)G(1-a).
2. PROVED: |S_h| <= m p^{(k-1)/2} for h != 0 (iterated Parseval), giving only N_k = O(p^{(k+1)/2}); CHECKED (interval): |S_h|^2 observed is about p^k, far below that bound for p <= 101.
3. CHECKED: for generic f, N_k up to p ~ 600 is p^{(k-1)/2} times a bounded-looking constant, apart from the M^k/p term, which dominates only at small p. For odd f (x^3-x) and k odd (k=3, 5), or with random c at k=4, N_k is of size p^{k/2}, larger than p^{(k-1)/2} (CHECKED data, not explained: OPEN).
4. N_k takes both signs as a function of p, for every f and k tested (CHECKED); the data give no polynomial in p, M, t0 with a definite sign except the nonnegative A+B+C1 of size p.
5. Nothing here is evidence about the Riemann Hypothesis for the integers. Finite computations over F_p cannot show that an argument for all primes is valid.
