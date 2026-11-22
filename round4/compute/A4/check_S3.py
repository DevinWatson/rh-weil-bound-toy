"""Exact check of the S3 counting claim over a prime field F_P: the number of c in (F_P^*)^(k-1) violating
(G_k) (Z meets Sigma_i for some 2<=i<=k-1) is at most (number of monomial conditions)*(P-1)^(k-2).
Sigma_1={0}, Sigma_2=rho_2 Z, Sigma_i=rho_i (Z u Sigma_{i-2}), rho_i=-c_{i-1}/c_i. Integers mod P only."""
import itertools, sys
P = int(sys.argv[1]); k = int(sys.argv[2]); Z = set(int(a) for a in sys.argv[3].split(","))
d = len(Z)
inv = {a: pow(a, P - 2, P) for a in range(1, P)}
def violates(c):  # c[1..k-1]
    rho = {i: (-c[i - 1] * inv[c[i]]) % P for i in range(2, k)}
    Sig = {1: {0}}
    for i in range(2, k):
        base = set(Z) | (Sig[i - 2] if i - 2 >= 1 else set())
        Sig[i] = {(rho[i] * z) % P for z in base}
        if Sig[i] & Z:
            return True
    return False
bad = 0; tot = 0
for tup in itertools.product(range(1, P), repeat=k - 1):
    c = (None,) + tup
    tot += 1
    if k > 2 and violates(c):
        bad += 1
# R_ratio and condition count (distinct monomials x distinct ratios in F_P)
R = {(a * inv[b]) % P for a in Z for b in Z}
nconds = 0
for i in range(2, k):
    for m in range(0, i // 2):   # products rho_i rho_{i-2} ... rho_{i-2m}, index i-2m >= 2
        if i - 2 * m >= 2:
            nconds += len(R)
# draft's coarse bound
draft = (k * k // 2 + k) * d * d
print(f"P={P} k={k} Z={sorted(Z)} d={d} total={tot} violating={bad} fraction={bad/tot:.4f} nconds(F_P ratios)={nconds} bound_count={nconds*(P-1)**(k-2)} draft_Q-1>{draft}? {P-1>draft}")
print("bound ok:", bad <= nconds * (P - 1) ** (k - 2), " good c exist:", bad < tot)
