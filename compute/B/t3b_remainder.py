"""Exact split q N = M^k + R, R = pN - M^k. Window maxima (exact Fractions) of
N^2/p^(k-1), N^2/p^k, R^2/p^(k+1), R^2/p^(k+2), and M^(2k)/p^(k+1) (the M^k term alone)."""
from fractions import Fraction as F
B = './compute/B/'
out = []
W = [(3, 50), (50, 150), (150, 300), (300, 700)]
for k in (4, 5, 6):
    rows = []
    for ln in open(B + f't3_k{k}.tsv').read().splitlines()[1:]:
        f, p, M, N = ln.split('\t'); rows.append((f, int(p), int(M), int(N)))
    out.append(f"== k={k} ==")
    for name in sorted(set(r[0] for r in rows)):
        rr = [r for r in rows if r[0] == name]
        out.append(f"  {name}")
        stats = [
            (f"N^2/p^{k-1}", lambda f_, p, M, N: F(N * N, p ** (k - 1))),
            (f"N^2/p^{k}", lambda f_, p, M, N: F(N * N, p ** k)),
            (f"R^2/p^{k+1}", lambda f_, p, M, N: F((p * N - M ** k) ** 2, p ** (k + 1))),
            (f"R^2/p^{k+2}", lambda f_, p, M, N: F((p * N - M ** k) ** 2, p ** (k + 2))),
            (f"M^{2*k}/p^{k+1}", lambda f_, p, M, N: F(M ** (2 * k), p ** (k + 1))),
        ]
        for lab, fn in stats:
            ws = []
            for lo, hi in W:
                sel = [r for r in rr if lo <= r[1] < hi]
                if sel:
                    ws.append(f"[{lo},{hi}):{float(max(fn(*r) for r in sel)):.3f}")
            out.append(f"     max {lab:14s} " + "  ".join(ws))
open(B + 't3b_remainder.txt', 'w').write("\n".join(out) + "\n")
print("\n".join(out))
