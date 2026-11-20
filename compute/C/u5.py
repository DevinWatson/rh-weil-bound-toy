import sys, os, csv
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction
from ff import *

HERE = os.path.dirname(os.path.abspath(__file__))
CUBICS = {"x^3+x+1": [1, 1, 0, 1], "x^3-x": [0, -1, 0, 1]}
rows = list(csv.DictReader(open(os.path.join(HERE, "N_table.tsv")), delimiter="\t"))

def dec(fr, d=4):
    """exact decimal expansion by integer arithmetic (display only), truncated"""
    neg = fr < 0
    fr = abs(fr)
    ip = fr.numerator // fr.denominator
    rem = fr - ip
    frac = (rem.numerator * 10 ** d) // rem.denominator
    return ("-" if neg else "") + str(ip) + "." + str(frac).zfill(d)

out = open(os.path.join(HERE, "u5_out.tsv"), "w")
out.write("p\tf\tn\tq\tM\tN4\tN4^2/q^(3n) exact\t(decimal, truncated)\tN4^2/q^(4n) exact\t(decimal)\tR4=qN4-M^4\tR4^2/q^(5n) (decimal)\tN4 identity via D(c)\n")
idfail = 0
for r in rows:
    p, n, q, M, t0, C, N4 = int(r["p"]), int(r["n"]), int(r["q"]), int(r["M"]), int(r["t0"]), int(r["C"]), int(r["N4"])
    name = r["f"]
    a = Fraction(N4 * N4, q ** (3 * n // 1)) if False else Fraction(N4 * N4, p ** (3 * n))
    b = Fraction(N4 * N4, p ** (4 * n))
    # note q = p^n so q^(3n) in the task's notation, with q the field size, means q^3 per field: N^2/q^3 and N^2/q^4
    # here n indexes the extension, so the task's "q^(3n)" with q=p is p^(3n) = q^3.
    R4 = q * N4 - M ** 4
    Rr = Fraction(R4 * R4, q ** 5)
    # extension check: N4 = sum_{c!=0} D(c)(D(-1-c)-t0^2) + t0^2 M (M-t0) + t0 M (C - t0^2) + t0^2 M^2
    F = Field(p, n)
    t = F.t_of([c % p for c in CUBICS[name]])
    x = np.arange(q)
    D = np.array([int((t * t[F.mul[np.int32(c), x]]).sum()) for c in range(q)], dtype=np.int64)
    s = 0
    for c in range(1, q):
        cm = int(F.neg[F.add[1, c]])  # -1 - c  ( = -(1+c) )
        s += int(D[c]) * (int(D[cm]) - t0 * t0)
    ident = s + t0 * t0 * M * (M - t0) + t0 * M * (C - t0 * t0) + t0 * t0 * M * M
    idok = (ident == N4)
    if not idok:
        idfail += 1
    out.write("\t".join(str(v) for v in [p, name, n, q, M, N4, "%d/%d" % (a.numerator, a.denominator), dec(a), "%d/%d" % (b.numerator, b.denominator), dec(b), R4, dec(Rr), idok]) + "\n")
    print(p, name, n, q, "N4=", N4, "N4^2/q^3=", dec(a), "N4^2/q^4=", dec(b), "R4^2/q^5=", dec(Rr), idok)
out.write("# note: q in the task's N^2/q^(3n) is p, so q^(3n) = (p^n)^3 = field size cubed. identity failures: %d\n" % idfail)
# k=5 for the rows computed
out.write("\n# k=5: p f n q N5 N5^2/Q^4 N5^2/Q^5 with Q the field size p^n\n")
for r in rows:
    if r["N5"] == "":
        continue
    p, n, q, N5 = int(r["p"]), int(r["n"]), int(r["q"]), int(r["N5"])
    out.write("%d\t%s\t%d\t%d\t%d\t%s\t%s\n" % (p, r["f"], n, q, N5, dec(Fraction(N5 * N5, q ** 4)), dec(Fraction(N5 * N5, q ** 5))))
out.close()
print("identity failures", idfail)
