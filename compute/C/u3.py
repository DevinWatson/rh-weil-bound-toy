import sys, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ff import *

HERE = os.path.dirname(os.path.abspath(__file__))
CUBICS = {"x^3+x+1": [1, 1, 0, 1], "x^3-x": [0, -1, 0, 1]}
NMAX = {3: 6, 5: 4, 7: 3}
random.seed(12345)
log = open(os.path.join(HERE, "u3_validation.txt"), "w")
def P(*a):
    s = " ".join(str(x) for x in a)
    print(s); log.write(s + "\n"); log.flush()

# ---- validation: fast vs brute (field tables) vs table-free brute for prime q
nchk = 0; nbad = 0
for (p, n) in [(3, 1), (5, 1), (7, 1), (3, 2)]:
    F = Field(p, n)
    q = F.q
    for name, co in CUBICS.items():
        t = F.t_of([c % p for c in co])
        for k in (2, 3, 4, 5):
            if q ** k > 70000:
                continue
            cs_list = [[1] * (k - 1)] + [[random.randrange(1, q) for _ in range(k - 1)] for _ in range(3)]
            for c in cs_list:
                a = N_fast(F, t, c, k)
                b = N_brute(F, t, c, k)
                extra = None
                if n == 1:
                    extra = N_brute_prime(p, [x % p for x in co], c, k)
                ok = (a == b) and (extra is None or extra == a)
                nchk += 1
                if not ok:
                    nbad += 1
                    P("MISMATCH", p, n, name, k, c, a, b, extra)
P("validation: %d comparisons (fast vs brute vs table-free brute), mismatches: %d" % (nchk, nbad))

# ---- table of N_k, c = all ones
rows = []
for p in (3, 5, 7):
    for name, co in CUBICS.items():
        for n in range(1, NMAX[p] + 1):
            F = Field(p, n)
            q = F.q
            t = F.t_of([c % p for c in co])
            M = int(t.sum())
            C = int((t * t[F.neg[np.arange(q)]]).sum())
            vals = {"M": M, "t0": int(t[0]), "C": C}
            for k in (2, 3, 4, 5):
                if k == 5 and q > 125:
                    vals[5] = ""
                    continue
                t0 = time.time()
                vals[k] = N_fast(F, t, [1] * (k - 1), k)
                P("p=%d f=%s n=%d q=%d k=%d N=%s (%.1fs)" % (p, name, n, q, k, vals[k], time.time() - t0))
            rows.append((p, name, n, q, vals["M"], vals["t0"], vals["C"], vals[2], vals[3], vals[4], vals[5]))
with open(os.path.join(HERE, "N_table.tsv"), "w") as fh:
    fh.write("p\tf\tn\tq\tM\tt0\tC\tN2\tN3\tN4\tN5\n")
    for r in rows:
        fh.write("\t".join(str(v) for v in r) + "\n")
P("done")
