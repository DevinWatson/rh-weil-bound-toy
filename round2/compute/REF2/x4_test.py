# REF2: test K4T's exceptional list against the full table of N_4 over c = (1,c2,c3), c2,c3 != 0.
import sys, random, time
from lib import *

def poly_from_roots(p, roots):
    co = [1]
    for z in roots:
        new = [0] * (len(co) + 1)
        for i, a in enumerate(co):
            new[i] = (new[i] + a) % p
            new[i + 1] = (new[i + 1] - a * z) % p
        co = new
    return co

def ratio_set(p, roots):
    S = {0}
    for z in roots:
        for w in roots:
            S.add((w * pow(z, -1, p)) % p)
    return S

def mu_set(p, roots):
    rs = set(roots)
    mu = set()
    for rho in range(1, p):
        if {(rho * z) % p for z in roots} == rs:
            mu.add(rho)
    return mu

def run(p, roots, label, out, thr=0.8, co=None, Sov=None, muov=None):
    if co is None:
        co = poly_from_roots(p, roots)
    t = t_from_poly(p, co)
    assert t[0] != 0
    C = Carray(p, t)
    N = N4_table_c1_is_1(p, t, C)
    # verify FFT table by direct integer evaluation on a sample
    rnd = random.Random(1)
    bad = 0
    for _ in range(300):
        c2 = rnd.randrange(1, p); c3 = rnd.randrange(1, p)
        if N4_formula(p, t, C, (1, c2, c3)) != int(N[c2, c3]):
            bad += 1
    S = Sov if Sov is not None else ratio_set(p, roots)
    mu = muov if muov is not None else mu_set(p, roots)
    # classify
    X0 = set(); X1 = set(); X4 = set()
    for s in S:
        for s2 in S:
            # c2 + c3 s + s2 = 0  (c1=1)
            for c3 in range(1, p):
                c2 = (-(c3 * s) - s2) % p
                if c2 == 0:
                    continue
                X4.add((c2, c3))
    for r1 in mu:
        for r2 in mu:
            for c3 in range(1, p):
                c2 = (-(c3 * r1) - r2) % p
                if c2:
                    X1.add((c2, c3))
    for c3 in range(1, p):
        c2 = (-1 - c3) % p
        if c2:
            X0.add((c2, c3))
    X1 |= X0
    X4 |= X1
    P2 = float(p) * p
    vals = {}
    allc = [(c2, c3) for c2 in range(1, p) for c3 in range(1, p)]
    def stats(keys):
        a = np.array([N[c2, c3] for (c2, c3) in keys], dtype=np.float64) / P2
        if len(a) == 0:
            return "n=0"
        return "n=%d mean=%.3f std=%.3f min=%.3f max=%.3f" % (len(a), a.mean(), a.std(), a.min(), a.max())
    gen = [k for k in allc if k not in X4]
    x4m1 = [k for k in X4 if k not in X1]
    x1m0 = [k for k in X1 if k not in X0]
    print("== %s p=%d roots=%s |S|=%d |mu|=%d fftverify_bad=%d" % (label, p, roots, len(S), len(mu), bad), file=out)
    print("  generic (not X4):      " + stats(gen), file=out)
    print("  X0 (c1+c2+c3=0):       " + stats(list(X0)), file=out)
    print("  X1 minus X0:           " + stats(x1m0), file=out)
    print("  X4 minus X1:           " + stats(x4m1), file=out)
    # flagged by size, outside X1 and outside X4
    flag = [(c2, c3) for (c2, c3) in allc if abs(N[c2, c3]) > thr * P2]
    fX1 = [k for k in flag if k in X1]
    fX4 = [k for k in flag if (k in X4 and k not in X1)]
    fG = [k for k in flag if k not in X4]
    print("  |N|>%.1f p^2: total %d ; in X1 %d ; in X4\\X1 %d ; outside X4 %d" % (thr, len(flag), len(fX1), len(fX4), len(fG)), file=out)
    # X1 members NOT flagged
    nf = [k for k in X1 if abs(N[k]) <= thr * P2]
    print("  X1 members with |N|<=%.1f p^2: %d of %d (mean N/p^2 of those %.3f)" % (thr, len(nf), len(X1), (np.mean([N[k] for k in nf]) / P2) if nf else 0.0), file=out)
    for k in fG[:5]:
        print("    outside-X4 flagged example c=(1,%d,%d) N/p^2=%.3f" % (k[0], k[1], N[k] / P2), file=out)
    for k in fX4[:5]:
        print("    X4\\X1 flagged example c=(1,%d,%d) N/p^2=%.3f" % (k[0], k[1], N[k] / P2), file=out)
    out.flush()

if __name__ == "__main__":
    out = open("x4_test_out.txt", "a")
    print("brute-force check of the N_4 formula (independent routine here)", file=out)
    for p, roots in [(7, [1, 2, 4]), (11, [1, 2, 5]), (11, [3, 4, 7])]:
        t = t_from_poly(p, poly_from_roots(p, roots)); C = Carray(p, t)
        bad = 0; n = 0
        for c2 in range(1, p):
            for c3 in range(1, p):
                n += 1
                if brute_N4(p, t, (1, c2, c3)) != N4_formula(p, t, C, (1, c2, c3)):
                    bad += 1
        print("  p=%d roots=%s cases=%d mismatches=%d" % (p, roots, n, bad), file=out)
    out.flush()
    which = sys.argv[1]
    if which == "split":
        p = int(sys.argv[2]); rnd = random.Random(int(sys.argv[3]))
        for _ in range(int(sys.argv[4])):
            roots = rnd.sample(range(1, p), 3)
            run(p, roots, "split cubic", out)
    elif which == "cyc2":  # f = x^d - a with a any nonzero residue, S from mu_d in F_p
        p = int(sys.argv[2]); d = int(sys.argv[3]); a = int(sys.argv[4])
        mud = {x for x in range(1, p) if pow(x, d, p) == 1}
        assert len(mud) == d
        run(p, [], "x^%d-%d (S from mu_d)" % (d, a), out, co=[1] + [0] * (d - 1) + [(-a) % p], Sov={0} | mud, muov=mud)
    elif which == "cyc":  # f = x^d - a, d | p-1
        p = int(sys.argv[2]); d = int(sys.argv[3]); a = int(sys.argv[4])
        # roots: d-th roots of a
        roots = [x for x in range(1, p) if pow(x, d, p) == a % p]
        assert len(roots) == d, roots
        run(p, roots, "x^%d-%d" % (d, a), out)
    out.close()
