import sys
from fractions import Fraction
B = './compute/B/'
out = []
for k in (4, 5, 6):
    rows = []
    for ln in open(B + f't3_k{k}.tsv').read().splitlines()[1:]:
        f, p, M, N = ln.split('\t'); rows.append((f, int(p), int(M), int(N)))
    Pk = max(r[1] for r in rows)
    out.append(f"== k={k}: {len(rows)} (f,p) rows, all good primes 3..{Pk} ==")
    for name in sorted(set(r[0] for r in rows)):
        rr = [r for r in rows if r[0] == name]
        a = max(rr, key=lambda r: Fraction(r[3] ** 2, r[1] ** (k - 1)))
        b = max(rr, key=lambda r: Fraction(r[3] ** 2, r[1] ** k))
        fa = Fraction(a[3] ** 2, a[1] ** (k - 1)); fb = Fraction(b[3] ** 2, b[1] ** k)
        out.append(f"  {name:10s} max N^2/p^{k-1} = {fa} (~{float(fa):.4f}) at p={a[1]}, N={a[3]}, M={a[2]};   max N^2/p^{k} = {fb} (~{float(fb):.5f}) at p={b[1]}, N={b[3]}")
        # trend over p windows (HINT-level display, exact fractions underlying)
        w = []
        for lo, hi in [(3, 50), (50, 150), (150, 300), (300, 700)]:
            sel = [r for r in rr if lo <= r[1] < hi]
            if sel:
                m = max(Fraction(r[3] ** 2, r[1] ** (k - 1)) for r in sel)
                w.append(f"[{lo},{hi}):{float(m):.3f}")
        out.append("      window maxima of N^2/p^%d: " % (k - 1) + "  ".join(w))
    a = max(rows, key=lambda r: Fraction(r[3] ** 2, r[1] ** (k - 1)))
    b = max(rows, key=lambda r: Fraction(r[3] ** 2, r[1] ** k))
    fa = Fraction(a[3] ** 2, a[1] ** (k - 1)); fb = Fraction(b[3] ** 2, b[1] ** k)
    out.append(f"  OVERALL max N^2/p^{k-1} = {fa} at {a[0]}, p={a[1]};  max N^2/p^{k} = {fb} at {b[0]}, p={b[1]}")
    # large-p only (p>=100)
    big = [r for r in rows if r[1] >= 100]
    a2 = max(big, key=lambda r: Fraction(r[3] ** 2, r[1] ** (k - 1)))
    out.append(f"  p>=100 only: max N^2/p^{k-1} = {Fraction(a2[3]**2, a2[1]**(k-1))} (~{float(Fraction(a2[3]**2, a2[1]**(k-1))):.3f}) at {a2[0]}, p={a2[1]}")
open(B + 't3_summary.txt', 'w').write("\n".join(out) + "\n")
print("\n".join(out))
