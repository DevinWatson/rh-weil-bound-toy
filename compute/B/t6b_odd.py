from fractions import Fraction as F
B = './compute/B/'
rows = []
for ln in open(B + 't6_k4_randc.tsv').read().splitlines()[1:]:
    z = ln.split('\t'); rows.append((z[0], *map(int, z[1:])))
out = []
for name in sorted(set(r[0] for r in rows)):
    a = [r for r in rows if r[0] == name]
    ws = []
    for lo, hi in [(3, 50), (50, 150), (150, 300), (300, 700)]:
        s = [F(r[6] ** 2, r[1] ** 4) for r in a if lo <= r[1] < hi]
        ws.append(f"[{lo},{hi}) {float(max(s)):.3f}")
    out.append(f"{name:10s} random c: window max N^2/p^4: " + "  ".join(ws))
a = [r for r in rows if r[0] == 'x^3-x']
a.sort(key=lambda r: -F(r[6] ** 2, r[1] ** 4))
out.append("x^3-x, ten largest N^2/p^4 (random c): p, p mod 4, c, N, N^2/p^4, and whether c1*c3 = c2^2 or c1 = +-c2 or c2 = +-c3 or c1 = +-c3")
for r in a[:10]:
    p, c1, c2, c3 = r[1], r[2], r[3], r[4]
    rel = [lab for lab, v in [("c1c3=c2^2", c1 * c3 % p == c2 * c2 % p), ("c1=+-c2", (c1 - c2) % p == 0 or (c1 + c2) % p == 0),
                              ("c2=+-c3", (c2 - c3) % p == 0 or (c2 + c3) % p == 0), ("c1=+-c3", (c1 - c3) % p == 0 or (c1 + c3) % p == 0)] if v]
    out.append(f"   p={p} ({p%4}) c=({c1},{c2},{c3}) N={r[6]} ratio={float(F(r[6]**2, p**4)):.3f} relations: {rel}")
open(B + 't6b_odd.txt', 'w').write("\n".join(out) + "\n")
print("\n".join(out))
