B = './compute/B/'
out = []
for k in (4, 5, 6):
    rows = [ln.split('\t') for ln in open(B + f't3_k{k}.tsv').read().splitlines()[1:]]
    rows = [(r[0], int(r[1]), int(r[2]), int(r[3])) for r in rows]
    out.append(f"k={k} ({len(rows)} rows):")
    for name in sorted(set(r[0] for r in rows)):
        rr = [r for r in rows if r[0] == name]
        pos = sum(1 for r in rr if r[3] > 0); neg = sum(1 for r in rr if r[3] < 0); z = len(rr) - pos - neg
        # sign of M^k: for k even always >=0 ; k odd = sign(M)
        opp = sum(1 for r in rr if r[3] != 0 and r[2] != 0 and (r[3] > 0) != ((r[2] ** k) > 0))
        same = sum(1 for r in rr if r[3] != 0 and r[2] != 0 and (r[3] > 0) == ((r[2] ** k) > 0))
        out.append(f"   {name:10s} N>0: {pos}, N<0: {neg}, N=0: {z};  among rows with N!=0 and M!=0: sign(N)=sign(M^k) {same}, opposite {opp}")
open(B + 't3c_signs.txt', 'w').write("\n".join(out) + "\n")
print("\n".join(out))
