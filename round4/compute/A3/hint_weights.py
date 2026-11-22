"""HINT ONLY (floating point, never certifying): moduli of the reciprocal roots gamma of the exact L-polynomials for hypothesis-valid,
fully determined data points. Compare |gamma| with q^{i/2} (the weight-theoretic value, NOT used in any proof) and with the elementary
bound q^{(i+1)/2} (S1/S8 of the draft). Reads raw_*.json, recomputes exact polynomials, then calls numpy.roots."""
import sys, json, cmath
import numpy as np
from a3lib import *
from run_cases import build_configs

def main(fam, nmax, maxrows=400):
    raw = json.load(open(f"raw_{fam}_n{nmax}.json"))["res"]
    cfgs = build_configs(fam)
    w3 = complex(-0.5, 3 ** 0.5 / 2)
    stats = {}
    for (cid, p, u, Z, h, cs, K, ws) in cfgs:
        q = p ** u
        if isinstance(Z, dict): pred = predict_poly(p, u, Z["m"], Z["f"], h, cs, K); FF = pred["F"]
        else: pred = predict(p, u, Z, h, cs, K); FF = None
        valid = True
        for i in range(1, K + 1):
            if i >= 2 and pred["conflict"][i]: valid = False
            if not valid: break
            for w in ws:
                wk = (None if w < 0 else w) if FF is None else FF.codeq(q, w)
                D = pred["r"][i + 1] - pred["Sigma"][i].get(wk, 0)
                if D >= nmax or D == 0: continue
                ps = []
                for n in range(1, nmax + 1):
                    a, b = raw[f"{cid}|{n}|{i}|{w}"]
                    sg = 1 if i % 2 == 0 else -1
                    ps.append(ZW(sg * a, sg * b))
                c = newton_series(ps, D)
                coeffs = [complex(x.a) + complex(x.b) * w3 for x in c]   # hint float
                # prod(1 - gamma T) = sum coeffs[j] T^j ; gamma = reciprocal roots: roots of reversed polynomial
                gam = np.roots(coeffs[::-1][::1][::-1][::-1]) if False else np.roots(list(reversed(coeffs)))
                # np.roots(list) takes highest-degree first: poly in T is coeffs[0]+...+coeffs[D]T^D; reciprocal roots gamma satisfy sum coeffs[j] gamma^{D-j}=0
                gam = np.roots(coeffs)  # highest degree first = coeffs[0]... which is sum coeffs[j] x^{D-j}: roots x = gamma
                mods = np.abs(gam)
                key = (fam, i, D)
                lo, hi = mods.min() / q ** (i / 2), mods.max() / q ** (i / 2)
                s = stats.setdefault(key, [lo, hi, 0])
                s[0] = min(s[0], lo); s[1] = max(s[1], hi); s[2] += 1
    for k in sorted(stats):
        print(f"HINT {k}: over {stats[k][2]} polys, min |gamma|/q^(i/2) = {stats[k][0]:.4f}, max |gamma|/q^(i/2) = {stats[k][1]:.4f}  (elementary bound allows up to q^(1/2) = {(3 if 'p3' in k[0] else 4)**0.5:.3f})")
if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))
