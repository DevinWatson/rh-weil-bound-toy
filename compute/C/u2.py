import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ff import *

CUBICS = {"x^3+x+1": [1, 1, 0, 1], "x^3-x": [0, -1, 0, 1]}
NMAX = {3: 6, 5: 4, 7: 3}
out = []
bad = 0
for p in (3, 5, 7):
    for name, co in CUBICS.items():
        co_p = [c % p for c in co]
        M = {0: -2}
        t0s = {}
        for n in range(1, NMAX[p] + 1):
            F = Field(p, n)
            t = F.t_of(co_p)
            M[n] = int(t.sum())
            t0s[n] = int(t[0])
            if n == 1:
                # independent Euler-criterion check of M_1
                m1 = 0
                for x in range(p):
                    v = sum(co_p[i] * pow(x, i, p) for i in range(4)) % p
                    m1 += 0 if v == 0 else (1 if pow(v, (p - 1) // 2, p) == 1 else -1)
                assert m1 == M[1], (m1, M[1])
        for n in range(1, NMAX[p] + 1):
            pred = None
            if n >= 2:
                pred = -M[1] * M[n - 1] - p * M[n - 2]
            ok = (pred is None) or pred == M[n]
            # Hasse-Weil: s_n = -M_n ; s_n^2 <= 4 p^n (exact)
            hw = M[n] ** 2 <= 4 * p ** n
            if not ok or not hw:
                bad += 1
            out.append((p, name, n, p ** n, M[n], pred, ok, hw))
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "u2_out.tsv"), "w") as fh:
    fh.write("p\tf\tn\tq\tM_n\trecurrence_prediction\trec_ok\tHasse_ok\n")
    for r in out:
        fh.write("\t".join(str(v) for v in r) + "\n")
    fh.write("# recurrence: M_n = -M_1 M_{n-1} - p M_{n-2}, M_0 = -2. failures: %d\n" % bad)
print("failures", bad)
for r in out:
    print(r)
