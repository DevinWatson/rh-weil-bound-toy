import sys, os, csv
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction
from ff import *
HERE = os.path.dirname(os.path.abspath(__file__))
CUB = {"x^3+x+1": [1, 1, 0, 1], "x^3-x": [0, -1, 0, 1]}
def dec(fr, d=3):
    neg = fr < 0; fr = abs(fr)
    ip = fr.numerator // fr.denominator; rem = fr - ip
    return ("-" if neg else "") + str(ip) + "." + str((rem.numerator * 10 ** d) // rem.denominator).zfill(d)
N4 = {}
for fn in ("crosscheck.tsv", "scan_N4_to_499.tsv"):
    for r in csv.DictReader(open(os.path.join(HERE, fn)), delimiter="\t"):
        N4[(r["f"], int(r["p"]))] = (int(r["M"]), int(r["N_4"]))
out = open(os.path.join(HERE, "special_out.txt"), "w")
def P(s):
    print(s); out.write(s + "\n")
bands = [(5, 100), (101, 200), (201, 350), (351, 500)]
res = {}
for (name, p), (M, N) in sorted(N4.items(), key=lambda kv: kv[0][1]):
    if p < 5 or p > 500:
        continue
    F = Field(p, 1)
    t = F.t_of([c % p for c in CUB[name]])
    x = np.arange(p)
    def D(c):
        return int((t * t[F.mul[np.int32(c % p), x]]).sum())
    t0 = int(t[0])
    c1 = 1
    c2 = int(F.neg[F.add[1, 1]])  # -2
    # also the c with c = -1-c  i.e. c = -1/2: D(c)^2
    chalf = int(F.neg[F.mul[1, F.inv[2]]])
    D1, Dm2, Dh = D(1), D(c2), D(chalf)
    special = D1 * (Dm2 - t0 * t0) + Dm2 * (D1 - t0 * t0)
    special_half = Dh * (Dh - t0 * t0)
    res[(name, p)] = (N, special, special_half, D1)
for name in CUB:
    P("== %s: N4 vs the c=1 / c=-2 terms of the D-convolution (special = D(1)(D(-2)-t0^2)+D(-2)(D(1)-t0^2); half = D(-1/2)(D(-1/2)-t0^2))" % name)
    for lo, hi in bands:
        sel = [(p, v) for (f, p), v in res.items() if f == name and lo <= p <= hi]
        if not sel:
            continue
        mN = sum(Fraction(v[0] ** 2, p ** 3) for p, v in sel) / len(sel)
        mS = sum(Fraction(v[1] ** 2, p ** 3) for p, v in sel) / len(sel)
        mH = sum(Fraction(v[2] ** 2, p ** 3) for p, v in sel) / len(sel)
        mR = sum(Fraction((v[0] - v[1] - v[2]) ** 2, p ** 3) for p, v in sel) / len(sel)
        P("p in [%d,%d] (%d primes): mean N^2/p^3 %s ; mean special^2/p^3 %s ; mean half^2/p^3 %s ; mean (N-special-half)^2/p^3 %s" % (lo, hi, len(sel), dec(mN), dec(mS), dec(mH), dec(mR)))
