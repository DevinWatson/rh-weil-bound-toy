"""Run a case family: exact stalk L-series degrees vs prediction from invariant (I_i) of S5.
usage: python run_cases.py <family> <nmax>"""
import sys, json, time, itertools
from a3lib import *

def build_configs(fam):
    cfgs = []   # (id, p, u, Z, h, cs, K, ws)
    if fam == "p3d1":      # q=3, chi quadratic, f = x-1 (root code 0 = 1), c_i in {1,-1} = codes 0,1
        p, u, Z = 3, 1, [0]
        ws = [-1, 0, 1]
        for K in (4, 5, 6):
            for cs in itertools.product([0, 1], repeat=K):
                if cs[0] != 0: continue
                for h in (0, 1):
                    if K == 6 and h == 1 and cs not in [(0,)*6, (0,1,0,1,0,1)]: continue
                    if K == 6 and cs not in [(0,)*6, (0,1,0,1,0,1), (0,0,1,1,0,0), (0,1,1,0,0,1), (0,0,0,1,1,1), (0,1,0,0,1,0)]: continue
                    cfgs.append((f"d1K{K}h{h}c{''.join(map(str,cs))}", p, u, Z, h, list(cs), K, ws))
    elif fam == "p2d1":    # q=4, chi cubic, f = x-1, c_i in F_4^* (codes 0,1,2), K<=5
        p, u, Z = 2, 2, [0]
        ws = [-1, 0, 1, 2]
        inv_count = 0
        for K in (3, 4, 5):
            for cs in itertools.product([0, 1, 2], repeat=K):
                if cs[0] != 0: continue
                if K == 5:
                    pr = predict(p, u, Z, 0, list(cs), K)
                    valid = not any(pr["conflict"][j] for j in range(2, K + 1))
                    if not valid:
                        inv_count += 1
                        if inv_count > 6: continue
                cfgs.append((f"q4d1K{K}h0c{''.join(map(str,cs))}", p, u, Z, 0, list(cs), K, ws))
        cfgs.append(("q4d1K5h1c0101", p, u, Z, 1, [0, 1, 0, 1, 0], 5, ws))
        cfgs.append(("q4d1K5h2c0101", p, u, Z, 2, [0, 1, 0, 1, 0], 5, ws))
    elif fam == "p2d2irr":   # q=4, chi cubic, f = x^2+x+xi irreducible over F_4 (d=2), roots in F_16
        p, u = 2, 2
        Z = {"f": [1, 0, 0], "m": 2}
        ws = [-1, 0, 1, 2]
        for K in (3, 4):
            for cs in itertools.product([0, 1, 2], repeat=K):
                if cs[0] != 0: continue
                cfgs.append((f"q4d2irrK{K}h0c{''.join(map(str,cs))}", p, u, Z, 0, list(cs), K, ws))
    elif fam == "p3d3irr":   # q=3, quadratic chi, f = x^3-x+1 irreducible over F_3 (d=3)
        p, u = 3, 1
        # coefficients as codes: 1 -> 0 (xi^0 = 1), -1 -> 1 (xi = 2 = -1), 0 -> -1.  f = 1 - x + x^3 => [0, 1, -1, 0]
        Z = {"f": [0, 1, -1, 0], "m": 3}
        ws = [-1, 0, 1]
        for K in (2, 3):
            for cs in itertools.product([0, 1], repeat=K):
                if cs[0] != 0: continue
                for h in (0, 1):
                    cfgs.append((f"d3K{K}h{h}c{''.join(map(str,cs))}", p, u, Z, h, list(cs), K, ws))
    elif fam == "p2d2irrdeep":   # q=4, d=2 irreducible, K=3, three valid c, for n=13
        p, u = 2, 2
        Z = {"f": [1, 0, 0], "m": 2}
        ws = [-1, 0, 1, 2]
        for cs in ([0, 1, 0], [0, 2, 1], [0, 1, 2]):
            cfgs.append((f"q4d2irrK3h0c{''.join(map(str,cs))}", p, u, Z, 0, list(cs), 3, ws))
    elif fam == "p2d1K6":   # q=4, d=1, all 12 hypothesis-valid K=6 configurations (c_1=1), h=1
        p, u, Z = 2, 2, [0]
        ws = [-1, 0, 1, 2]
        for cs in itertools.product([0, 1, 2], repeat=6):
            if cs[0] != 0: continue
            pr = predict(p, u, Z, 0, list(cs), 6)
            if any(pr["conflict"][j] for j in range(2, 7)): continue
            cfgs.append((f"q4d1K6h0c{''.join(map(str,cs))}", p, u, Z, 0, list(cs), 6, ws))
    elif fam == "p2q16":   # q=16, cubic chi, f = x-1, c in (F_16^*)^K random hypothesis-valid, K=5,6 ; points w in F_16
        import random
        p, u, Z = 2, 4, [0]
        ws = [-1] + list(range(15))
        rnd = random.Random(2026)
        got = {5: 0, 6: 0}
        while got[5] < 20 or got[6] < 10:
            K = 5 if got[5] < 20 else 6
            cs = [rnd.randrange(15) for _ in range(K)]
            pr = predict(p, u, Z, 0, cs, K)
            if any(pr["conflict"][j] for j in range(2, K + 1)): continue
            h = rnd.randrange(15)
            cid = f"q16K{K}h{h}c{'.'.join(map(str,cs))}"
            if any(c[0] == cid for c in cfgs): continue
            cfgs.append((cid, p, u, Z, h, cs, K, ws)); got[K] += 1
    elif fam == "p2d1h":   # q=4, d=1, hypothesis-valid K=5 configs with h = xi, xi^2
        p, u, Z = 2, 2, [0]
        ws = [-1, 0, 1, 2]
        for cs in itertools.product([0, 1, 2], repeat=5):
            if cs[0] != 0: continue
            pr = predict(p, u, Z, 0, list(cs), 5)
            if any(pr["conflict"][j] for j in range(2, 6)): continue
            for h in (1, 2):
                cfgs.append((f"q4d1K5h{h}c{''.join(map(str,cs))}", p, u, Z, h, list(cs), 5, ws))
    elif fam == "p2d3chi1":   # q=4, chi cubic, f = x^3-1 (all of F_4^*), d=3, chi^d = 1 at infinity (unramified there)
        p, u, Z = 2, 2, [0, 1, 2]
        ws = [-1, 0, 1, 2]
        for K in (2, 3):
            for cs in itertools.product([0, 1, 2], repeat=K):
                if cs[0] != 0: continue
                cfgs.append((f"q4d3chi1K{K}h0c{''.join(map(str,cs))}", p, u, Z, 0, list(cs), K, ws))
    elif fam == "p3zero":   # q=3, f = x (root at 0): f(0) = 0, violates S0
        p, u, Z = 3, 1, [None]
        ws = [-1, 0, 1]
        for K in (3, 4):
            for cs in itertools.product([0, 1], repeat=K):
                if cs[0] != 0: continue
                cfgs.append((f"p3zeroK{K}h0c{''.join(map(str,cs))}", p, u, Z, 0, list(cs), K, ws))
    elif fam == "p2d2":    # q=4, chi cubic, f=(x-1)(x-xi), d=2
        p, u, Z = 2, 2, [0, 1]
        ws = [-1, 0, 1, 2]
        for K in (3, 4):
            for cs in itertools.product([0, 1, 2], repeat=K):
                if cs[0] != 0: continue
                cfgs.append((f"q4d2K{K}h0c{''.join(map(str,cs))}", p, u, Z, 0, list(cs), K, ws))
    return cfgs

def main():
    fam, nmax = sys.argv[1], int(sys.argv[2])
    cfgs = build_configs(fam)
    print("family", fam, "configs", len(cfgs), flush=True)
    data = {}
    for (cid, p, u, Z, h, cs, K, ws) in cfgs:
        data[cid] = {}
    def zspec(c):
        Z = c[3]
        if isinstance(Z, dict): return f"{-(len(Z['f'])-1)} {' '.join(map(str, Z['f']))}"
        return f"{len(Z)} {' '.join(str(-1 if x is None else x) for x in Z)}"
    lines_by_cfg = {c[0]: f"{c[0]} {c[4]} {zspec(c)} {c[6]} {' '.join(map(str,c[5]))} {len(c[7])} {' '.join(map(str,c[7]))}" for c in cfgs}
    p, u = cfgs[0][1], cfgs[0][2]
    allres = {}
    for n in range(1, nmax + 1):
        t0 = time.time()
        res = run_engine(p, u, n, list(lines_by_cfg.values()), f"{fam}", xi_poly=("1100" if (p == 2 and u == 4) else None))
        allres.update(res)
        print(f"n={n} done {time.time()-t0:.1f}s", flush=True)
    out = {"family": fam, "nmax": nmax, "res": {f"{k[0]}|{k[1]}|{k[2]}|{k[3]}": v for k, v in allres.items()}}
    json.dump(out, open(f"raw_{fam}_n{nmax}.json", "w"))
if __name__ == "__main__":
    main()
