"""Exact checks of the structure of R_n for k=2 and k=3 over F_3^n, f cubic (d=3), n=1..4.
k=2: R_n = -p_n^2 - 2 Q^n t0^n p_n - Q^n, p_n = sum alpha_i^n = -M_n (Newton identities from M_1, M_2 only, then verified on M_3, M_4).
k=3: N = t0 M^2 + (M - t0) B(rho'), rho' = -c_1/c_2, B(rho)=sum_x t(rho x) t(x); R = Q^n N - M^3 compared with the character-sum value.
Everything is integer arithmetic (Z[omega] pairs for the sums)."""
import sys
sys.path.insert(0, r"./round4/compute/A4")
from ff3 import *
out = open(r"./round4/compute/A4/check_k2k3_out.txt", "w")
def P(*a):
    s = " ".join(str(x) for x in a); print(s); out.write(s + "\n"); out.flush()
for name, poly in (("x^3-x+1", [1, 2, 0, 1]), ("x^3-x-1", [2, 2, 0, 1])):
    Fs = {n: Field(n) for n in (1, 2, 3, 4)}
    ts = {n: chi_table(Fs[n], poly) for n in Fs}
    M = {n: int(ts[n].sum()) for n in Fs}
    p = {n: -M[n] for n in Fs}
    e1 = p[1]; e2 = (p[1] ** 2 - p[2]) // 2
    assert (p[1] ** 2 - p[2]) % 2 == 0
    # Newton for 2 eigenvalues: p_n = e1 p_{n-1} - e2 p_{n-2}
    ok_newton = all(p[n] == e1 * p[n - 1] - e2 * p[n - 2] for n in (3, 4))
    P(f"f={name}: M_n={[M[n] for n in (1,2,3,4)]}  e1={e1} e2={e2}  Newton check on n=3,4 (degree-2 L-polynomial): {ok_newton}")
    for n in (1, 2, 3, 4):
        F = Fs[n]; Q = F.N; t = ts[n]
        t0 = int(t[0])
        # k=2
        cs = [1]
        R2 = [0, 0]
        for h in range(1, Q):
            a, b = Smat_sum(F, t, cs, h); R2[0] += a; R2[1] += b
        pred2 = -p[n] ** 2 - 2 * Q * t0 * p[n] - Q
        # t0 over F_{3^n} equals chi(f(0))^n ; here f(0) = +-1 in F_3
        P(f"  n={n} Q^n={Q} k=2 R={tuple(R2)} predicted={pred2} match={R2 == [pred2, 0]}")
        # k=3 with c=(1,1) and c=(1,2)
        for cs3 in ([1, 1], [1, 2], [2, 1]):
            R3 = [0, 0]
            for h in range(1, Q):
                a, b = Smat_sum(F, t, cs3, h); R3[0] += a; R3[1] += b
            c1, c2 = cs3
            rho = (-c1 * pow(c2, -1, 3)) % 3  # -c1/c2 in F_3 (a constant polynomial)
            B = sum(int(t[F.mul[rho, x]]) * int(t[x]) for x in range(Q))
            N3 = t0 * M[n] ** 2 + (M[n] - t0) * B
            pred3 = Q * N3 - M[n] ** 3
            # with u=-M, b=-B: R = u^3 + Q t0 u^2 + Q b u + Q t0 b   (b = -B)
            u = -M[n]; b = -B
            pred3b = u ** 3 + Q * t0 * u * u + Q * b * u + Q * t0 * b
            P(f"  n={n} k=3 c={tuple(cs3)} rho'={rho} R={tuple(R3)} Q*N3-M^3={pred3} A-form={pred3b} match={R3 == [pred3, 0] and pred3 == pred3b}")
P("done")
