"""Analyze raw_*.json: for every config, stage i, point w: exact L-polynomial from the stalk sums, compare with prediction."""
import sys, json
from a3lib import *
from run_cases import build_configs

def main():
    fam, nmax = sys.argv[1], int(sys.argv[2])
    raw = json.load(open(f"raw_{fam}_n{nmax}.json"))["res"]
    cfgs = build_configs(fam)
    lines = []
    summary = {"agree": 0, "undetermined_consistent": 0, "disagree": 0, "hyp_fail_disagree": 0, "hyp_fail_agree": 0, "hyp_fail_undet": 0}
    dis = []
    for (cid, p, u, Z, h, cs, K, ws) in cfgs:
        q, mul, inv, minus1 = make_field(p, u)
        if isinstance(Z, dict):
            pred = predict_poly(p, u, Z["m"], Z["f"], h, cs, K); FF = pred["F"]
        else:
            pred = predict(p, u, Z, h, cs, K); FF = None
        # hypothesis flags: structure of P_i valid iff Z disjoint from Sigma_j, 1<=j<=i-1  (conflict[j+1])
        valid = {}
        ok = True
        for i in range(1, K + 2):
            valid[i] = ok
            if i + 1 <= K and pred["conflict"].get(i + 1, False): ok = False
            if i >= K: pass
        for i in range(1, K + 1):
            for w in ws:
                wk = (None if w < 0 else w) if FF is None else FF.codeq(q, w)
                drop = pred["Sigma"][i].get(wk, 0)
                D = pred["r"][i + 1] - drop
                ps = []
                for n in range(1, nmax + 1):
                    a, b = raw[f"{cid}|{n}|{i}|{w}"]
                    sgn = 1 if i % 2 == 0 else -1
                    ps.append(ZW(sgn * a, sgn * b))
                rep = degree_report(ps)
                last = rep["last_nonzero"]
                if D < nmax:
                    status = "AGREE" if last == D else "DISAGREE"
                else:
                    status = "UNDET(consistent)"  # D >= N: only the first N coefficients are visible; imprimitive Frobenius (Galois permuting Z) can make last nonzero < N
                hyp = valid[i]
                key = ("agree" if status == "AGREE" else "undetermined_consistent" if status.startswith("UNDET") else "disagree")
                if not hyp: key = "hyp_fail_" + {"agree": "agree", "undetermined_consistent": "undet", "disagree": "disagree"}[key]
                summary[key] += 1
                if status == "DISAGREE": dis.append((cid, i, w, D, last, hyp))
                lines.append(f"{cid} i={i} w={w} predicted_dim={D} (r_{i+1}={pred['r'][i+1]}, drop={drop}) observed_last_nonzero_coeff={last} (N={nmax}) integral={rep['integral']} hypothesis_valid_for_Q_i={hyp} -> {status}")
    open(f"analysis_{fam}_n{nmax}.txt", "w").write("\n".join(lines) + "\n")
    print(json.dumps(summary))
    for d in dis[:60]: print("DIS", d)
main()
