import json, sys
from modp_fibre import lseries, hypothesis_k, rho
d = json.load(open(sys.argv[1]))
P = d['P']; N = d['NMAX']
def formula(dd, k):
    rr = [None, 1, dd]
    for i in range(2, k + 2):
        rr.append(dd * rr[i] + rr[i - 1])
    return rr[k + 1] - (1 if k % 2 == 1 else 0)
lines = ['P = %d, omega = %d, f = x - 1 (d=1), h = 1, q = 5, n up to %d' % (P, d['omega'], N)]
seen = set()
for key, vals in d['S'].items():
    if key in seen: continue
    seen.add(key)
    cs = tuple(int(x) for x in key.split(','))
    k = len(cs) + 1
    S = {int(n): v for n, v in vals.items()}
    nn = max(S)
    L = lseries(S, k, P, nn)
    nz = [i for i, v in enumerate(L) if v != 0]
    deg = max(nz)
    trailing = nn - deg
    bad = hypothesis_k(list(cs), k)
    hyp = 'holds' if not bad else 'FAILS at (i,m)=%s' % bad
    pred = formula(1, k)
    lines.append('k=%d c=%s hypothesis %s | predicted D_k (hyp holds) = %d | last nonzero L index = %d of %d, trailing zeros = %d, nonzero idx = %s' % (k, cs, hyp, pred, deg, nn, trailing, nz))
txt = '\n'.join(lines)
print(txt)
open(sys.argv[2], 'w').write(txt + '\n')
