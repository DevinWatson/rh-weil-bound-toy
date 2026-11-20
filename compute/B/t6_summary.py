from fractions import Fraction as F
import statistics as st
B = './compute/B/'
r6 = []
for ln in open(B + 't6_k4_randc.tsv').read().splitlines()[1:]:
    z = ln.split('\t'); r6.append((z[0], int(z[1]), int(z[2]), int(z[3]), int(z[4]), int(z[5]), int(z[6])))
P = max(r[1] for r in r6)
r1 = []
for ln in open(B + 't3_k4.tsv').read().splitlines()[1:]:
    z = ln.split('\t')
    if int(z[1]) <= P: r1.append((z[0], int(z[1]), int(z[2]), int(z[3])))
out = [f"T6: k=4, {len(r6)} random-c values (3 per (f,p)), good primes 3..{P}, seed 20261120; compared with c=1 on the same primes ({len(r1)} values)"]
W = [(3, 50), (50, 150), (150, 300), (300, 700)]
for name in sorted(set(r[0] for r in r6)):
    a = [r for r in r6 if r[0] == name]; b = [r for r in r1 if r[0] == name]
    ma = max(a, key=lambda r: F(r[6] ** 2, r[1] ** 3)); mb = max(b, key=lambda r: F(r[3] ** 2, r[1] ** 3))
    fa = F(ma[6] ** 2, ma[1] ** 3); fb = F(mb[3] ** 2, mb[1] ** 3)
    ga = max(F(r[6] ** 2, r[1] ** 4) for r in a); gb = max(F(r[3] ** 2, r[1] ** 4) for r in b)
    out.append(f"  {name:10s} random c: max N^2/p^3 = {fa} (~{float(fa):.3f}) at p={ma[1]}, c=({ma[2]},{ma[3]},{ma[4]}), N={ma[6]};  max N^2/p^4 = {float(ga):.4f}  |  c=1: max N^2/p^3 = {fb} (~{float(fb):.3f}) at p={mb[1]}; max N^2/p^4 = {float(gb):.4f}")
    wa = []; wb = []
    for lo, hi in W:
        sa = [F(r[6] ** 2, r[1] ** 3) for r in a if lo <= r[1] < hi]; sb = [F(r[3] ** 2, r[1] ** 3) for r in b if lo <= r[1] < hi]
        if sa: wa.append(f"[{lo},{hi}) max {float(max(sa)):.2f} mean {float(sum(sa)/len(sa)):.2f}")
        if sb: wb.append(f"[{lo},{hi}) max {float(max(sb)):.2f} mean {float(sum(sb)/len(sb)):.2f}")
    out.append("      random c windows N^2/p^3: " + "; ".join(wa))
    out.append("      c=1      windows N^2/p^3: " + "; ".join(wb))
    # sign counts
    out.append(f"      sign of N_4 (random c): +{sum(1 for r in a if r[6]>0)} -{sum(1 for r in a if r[6]<0)} 0:{sum(1 for r in a if r[6]==0)};  (c=1): +{sum(1 for r in b if r[3]>0)} -{sum(1 for r in b if r[3]<0)}")
open(B + 't6_summary.txt', 'w').write("\n".join(out) + "\n")
print("\n".join(out))
