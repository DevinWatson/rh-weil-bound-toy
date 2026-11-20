import csv, os
from fractions import Fraction
HERE = os.path.dirname(os.path.abspath(__file__))
def dec(fr, d=3):
    neg = fr < 0; fr = abs(fr)
    ip = fr.numerator // fr.denominator; rem = fr - ip
    return ("-" if neg else "") + str(ip) + "." + str((rem.numerator * 10 ** d) // rem.denominator).zfill(d)
rows = []
for fn in ("crosscheck.tsv", "scan_N4_to_499.tsv"):
    for r in csv.DictReader(open(os.path.join(HERE, fn)), delimiter="\t"):
        rows.append((r["f"], int(r["p"]), int(r["M"]), int(r["N_4"])))
out = open(os.path.join(HERE, "scale_out.txt"), "w")
def P(s):
    print(s); out.write(s + "\n")
bands = [(3, 30), (31, 100), (101, 200), (201, 350), (351, 500)]
for name in ("x^3+x+1", "x^3-x"):
    P("== " + name + ": exact means over primes in band of N4^2/p^3 and N4^2/p^4 and max of each (decimals of exact fractions)")
    for lo, hi in bands:
        sel = [(p, N) for (f, p, M, N) in rows if f == name and lo <= p <= hi]
        if not sel:
            continue
        m3 = sum(Fraction(N * N, p ** 3) for p, N in sel) / len(sel)
        m4 = sum(Fraction(N * N, p ** 4) for p, N in sel) / len(sel)
        mx3 = max(Fraction(N * N, p ** 3) for p, N in sel)
        mx4 = max(Fraction(N * N, p ** 4) for p, N in sel)
        P("p in [%d,%d] (%d primes): mean N^2/p^3 = %s  max = %s ; mean N^2/p^4 = %s  max = %s" % (lo, hi, len(sel), dec(m3), dec(mx3), dec(m4), dec(mx4)))
# signs
for name in ("x^3+x+1", "x^3-x"):
    sel = [(p, N) for (f, p, M, N) in rows if f == name]
    pos = sum(1 for p, N in sel if N > 0); neg = sum(1 for p, N in sel if N < 0); z = sum(1 for p, N in sel if N == 0)
    P("%s: sign of N4 over %d primes: positive %d, negative %d, zero %d" % (name, len(sel), pos, neg, z))
    # sign of N4 vs sign of M^4 (always >= 0): count N4 < 0
