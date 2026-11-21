"""Bookkeeping prediction of deg L (Euler-characteristic picture of Claim B, with E's coincidence rule), f = x - 1 over F_5, points in F_5."""
import json
p = 5
inv = lambda a: pow(a, -1, p)
def predict(cs, a=1):
    k = len(cs) + 1
    Z = [a % p]
    r = 1; sing = {z: 1 for z in Z}; freq = {}; T0 = 1
    out = [sum(sing.values()) + sum(freq.values()) - r]
    coinc = []
    for i in range(1, k):
        ci = cs[i - 1]
        rnew = sum(sing.values())
        newsing = {}
        for aa, dim in freq.items():
            w = (-aa * inv(ci)) % p
            newsing[w] = newsing.get(w, 0) + dim
        if T0:
            newsing[0] = newsing.get(0, 0) + T0
        for z in Z:
            if z in newsing: coinc.append(i + 1)
            newsing[z] = rnew
        newfreq = {}; newT0 = 0
        for s, dim in sing.items():
            if s == 0: newT0 += dim
            else:
                aa = (ci * s) % p
                newfreq[aa] = newfreq.get(aa, 0) + dim
        r, sing, freq, T0 = rnew, newsing, newfreq, newT0
        out.append(sum(sing.values()) + sum(freq.values()) - r)
    return out[-1], coinc
cfg = json.load(open('cfg.json'))
seen=set()
for c in cfg:
    if tuple(c) in seen: continue
    seen.add(tuple(c))
    print(tuple(c), predict(c))
