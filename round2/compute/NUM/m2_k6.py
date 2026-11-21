"""M2: k = 6.  Exhaustive c=(1,c2..c5) for p=5,7; random 400 (seed recorded) for p=11,13; plus all c in the predicted sets for p=11,13,17.
Predicted bad sets: perfect matchings sigma of {1..6}; subspace x_i = x_sigma(i) (dim 3) lies in Q_c = 0 iff all coefficients of the
quadratic form in the 3 pair variables y vanish.  Edges (i,i+1) (c_i) between pair a and pair b contribute c_i to the coefficient of y_a y_b;
an edge inside a pair contributes c_i to y_a^2.  'Brief set' = matchings with no adjacent pair."""
import random, sys, itertools
from fractions import Fraction
from lib import *

K = 6
SEED = 20261120


def matchings(n):
    def rec(rem):
        if not rem:
            yield []
            return
        a = rem[0]
        for j in range(1, len(rem)):
            b = rem[j]
            for m in rec(rem[1:j] + rem[j + 1:]):
                yield [(a, b)] + m
    return list(rec(list(range(1, n + 1))))


def conds(m):
    """list of linear conditions: each a sorted tuple of edge indices i (c_i) whose sum must vanish; plus label."""
    pid = {}
    for a, (u, v) in enumerate(m):
        pid[u] = a; pid[v] = a
    cond = {}
    for i in range(1, K):
        a, b = pid[i], pid[i + 1]
        key = (min(a, b), max(a, b))
        cond.setdefault(key, []).append(i)
    return cond


ALL = matchings(K)
assert len(ALL) == 15
INFO = []
for m in ALL:
    adj = any(abs(u - v) == 1 for u, v in m)
    INFO.append((m, adj, conds(m)))
BRIEF = [x for x in INFO if not x[1]]


def describe(x):
    m, adj, cond = x
    s = "matching " + " ".join(f"{u}-{v}" for u, v in m) + (" (has adjacent pair)" if adj else "") + ": "
    parts = []
    for key, idx in sorted(cond.items()):
        lab = "y%d^2" % (key[0] + 1) if key[0] == key[1] else "y%dy%d" % (key[0] + 1, key[1] + 1)
        parts.append(f"[{lab}] " + "+".join(f"c{i}" for i in idx) + " = 0")
    # pair variables with no edge between them give no condition
    return s + "; ".join(parts)


def holds(x, c, p):
    cond = x[2]
    return all(sum(c[i - 1] for i in idx) % p == 0 for idx in cond.values())


with open("m2_matchings.txt", "w") as fh:
    fh.write("All 15 perfect matchings of {1..6}; conditions on c1..c5 for x_i = x_sigma(i) to lie in {Q_c = 0}\n")
    fh.write("Brief set = matchings with no adjacent pair (equivalently every c_i joins two different pairs).\n\n")
    for x in INFO:
        fh.write(describe(x) + "\n")
    fh.write(f"\nbrief set size {len(BRIEF)}\n")
print(open("m2_matchings.txt").read())


def run_one(nm, p, c, t, M):
    N = int(Nzero(t, c, K, p))
    E = Fraction(N) - Fraction(M ** K, p)
    pb = [i for i, x in enumerate(BRIEF) if holds(x, c, p)]
    pa = [i for i, x in enumerate(INFO) if holds(x, c, p)]
    return N, E, pb, pa


def header():
    return "poly\tp\tc2\tc3\tc4\tc5\tN6\tM\troots\tN/p^3\t2N>=p^3\tE=N-M^6/p (exact)\t2E>=p^3\tbrief_matchings_predicting\tany_matching_predicting\n"


def fmt(nm, p, c, N, E, pb, pa, M, r0):
    return f"{nm}\t{p}\t{c[1]}\t{c[2]}\t{c[3]}\t{c[4]}\t{N}\t{M}\t{r0}\t{Fraction(N, p**3)}\t{int(2*N>=p**3)}\t{E}\t{int(2*E>=p**3)}\t{','.join(map(str,pb))}\t{','.join(map(str,pa))}\n"


mode = sys.argv[1]
t0 = now()
if mode == "exh":
    jobs = [("f3", 5), ("f3", 7), ("f4", 5), ("f2", 7), ("f1", 5), ("f1", 7)]
    fh = open("m2_exhaustive.tsv", "w"); fh.write(header())
    for nm, p in jobs:
        if not good(nm, p):
            print("excluded", nm, p); continue
        t = tv(nm, p); M = int(t.sum()); r0 = int((t == 0).sum())
        for c2, c3, c4, c5 in itertools.product(range(p), repeat=4):
            c = [1, c2, c3, c4, c5]
            N, E, pb, pa = run_one(nm, p, c, t, M)
            fh.write(fmt(nm, p, c, N, E, pb, pa, M, r0))
        print(nm, p, "done", round(now() - t0, 1))
    fh.close()
elif mode == "exh2":
    ps = [int(x) for x in sys.argv[2].split(",")]
    fh = open("m2_exhaustive_%s.tsv" % sys.argv[2].replace(",", "_"), "w"); fh.write(header())
    for nm in ("f1", "f3", "f2", "f4"):
        for p in ps:
            if not good(nm, p):
                continue
            t = tv(nm, p); M = int(t.sum()); r0 = int((t == 0).sum())
            for c2, c3, c4, c5 in itertools.product(range(p), repeat=4):
                c = [1, c2, c3, c4, c5]
                N, E, pb, pa = run_one(nm, p, c, t, M)
                fh.write(fmt(nm, p, c, N, E, pb, pa, M, r0))
            print(nm, p, "done", round(now() - t0, 1), flush=True)
    fh.close()
elif mode == "rnd":
    rng = random.Random(SEED)
    fh = open("m2_random.tsv", "w"); fh.write(header())
    jobs = [("f1", 11), ("f1", 13), ("f3", 11), ("f3", 13), ("f2", 11), ("f2", 13), ("f4", 11), ("f4", 13)]
    for nm, p in jobs:
        if not good(nm, p):
            print("excluded", nm, p); continue
        t = tv(nm, p); M = int(t.sum()); r0 = int((t == 0).sum())
        for _ in range(400):
            c = [1] + [rng.randrange(p) for _ in range(4)]
            N, E, pb, pa = run_one(nm, p, c, t, M)
            fh.write(fmt(nm, p, c, N, E, pb, pa, M, r0))
        print(nm, p, "done", round(now() - t0, 1))
    fh.close()
elif mode == "pred":
    # all c with c1=1 in the union of the brief-set predicted subspaces, p = 11, 13, 17 ; polys f1, f3 (and f2,f4 when good)
    fh = open("m2_predicted.tsv", "w"); fh.write(header())
    for nm in ("f1", "f3", "f2", "f4"):
        for p in (11, 13, 17):
            if not good(nm, p):
                continue
            t = tv(nm, p); M = int(t.sum()); r0 = int((t == 0).sum())
            seen = set()
            for c2, c3, c4, c5 in itertools.product(range(p), repeat=4):
                c = [1, c2, c3, c4, c5]
                if not any(holds(x, c, p) for x in BRIEF):
                    continue
                N, E, pb, pa = run_one(nm, p, c, t, M)
                fh.write(fmt(nm, p, c, N, E, pb, pa, M, r0))
            print(nm, p, "done", round(now() - t0, 1))
    fh.close()
print("total", round(now() - t0, 1), "s")
