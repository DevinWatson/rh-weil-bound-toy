import random, itertools
from lib import *

random.seed(20261120)
out = []
fails = 0
cases = 0
for nm in POLYS:
    for p in (5, 7, 11, 13):
        if not good(nm, p):
            out.append(f"skip {nm} p={p} (not good)")
            continue
        t = tv(nm, p)
        M = int(t.sum())
        for k in (2, 3, 4, 5):
            if p ** k > 170000:
                continue
            for _ in range(3):
                c = [1] + [random.randrange(p) for _ in range(k - 2)]
                br = core.brute(t, c, k, p)
                N = [int(v) for v in Nall(t, c, k, p)]
                z = int(Nzero(t, c, k, p))
                ok = (br == N) and z == br[0] and sum(N) == M ** k
                cases += 1
                if not ok:
                    fails += 1
                    out.append(f"FAIL {nm} p={p} k={k} c={c}")
out.append(f"validation brute-force vs Nall/Nzero and sum_s N(s)=M^k: cases={cases} failures={fails}")

# closed form for N_4 : N_4 = -p + t0^2 M^2 + sum_{r in F_p} C(r) C(tau(r)), tau(r) = -(c3/c1)(r+e), e=c2/c3  (c3 != 0)
def Cvec(t, p):
    x = np.arange(p)
    return [int((t * t[(r * x) % p]).sum()) for r in range(p)]

f4 = 0; f4n = 0
for nm in POLYS:
    for p in (7, 11, 13):
        if not good(nm, p):
            continue
        t = tv(nm, p); M = int(t.sum()); t0 = int(t[0]); C = Cvec(t, p)
        for c2 in range(p):
            for c3 in range(1, p):
                c1 = 1
                e = c2 * pow(c3, -1, p) % p
                tot = -p + t0 * t0 * M * M
                for r in range(p):
                    tau = (-(c3 * pow(c1, -1, p)) * (r + e)) % p
                    tot += C[r] * C[tau]
                N = int(Nzero(t, [c1, c2, c3], 4, p))
                f4n += 1
                if tot != N:
                    f4 += 1
out.append(f"closed form N_4 = -p + t0^2 M^2 + sum_r C(r)C(tau r): cases={f4n} mismatches={f4}")
open("v1_out.txt", "w").write("\n".join(out) + "\n")
print("\n".join(out[-6:]))
