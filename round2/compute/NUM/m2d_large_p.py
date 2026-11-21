"""k=6 at larger p: brief-set predicted c (three one-parameter families with c1=1) and 60 random c, per prime. Exact."""
import sys, random, statistics
from fractions import Fraction
sys.argv = [sys.argv[0], "none"]
exec(open("m2_k6.py").read().split("mode = sys.argv[1]")[0])   # reuse BRIEF, holds, K
BUDGET = 520
t_start = now()
def families(p):
    S = set()
    for u in range(p):
        S.add((1, p - 1, 0, u, (-u) % p))          # A: 1-3 2-5 4-6 : c2=-c1, c3=0, c5=-c4
        S.add((1, u, 0, p - 1, (-u) % p))          # B: 1-4 2-5 3-6 : c4=-c1, c3=0, c5=-c2
        S.add((1, u, (-u) % p, p - 1, 0))          # D: 1-5 2-4 3-6 : c4=-c1, c5=0, c3=-c2
    return sorted(S)
fh = open("m2d_large_p.tsv", "w")
fh.write("poly\tp\tkind\tc2\tc3\tc4\tc5\tN6\tM\troots\tN/p^3 (exact)\tE=N-M^6/p\n")
summ = []
jobs = [(nm, p) for p in (23, 29, 41, 53, 67, 83, 101) for nm in ("f1", "f3")]
rng = random.Random(20261120)
for nm, p in jobs:
    if now() - t_start > BUDGET:
        summ.append(f"budget reached before {nm} p={p}"); continue
    if not good(nm, p): 
        summ.append(f"{nm} p={p} excluded"); continue
    t = tv(nm, p); M = int(t.sum()); r0 = int((t == 0).sum())
    fam = families(p)
    assert all(any(holds(x, list(c), p) for x in BRIEF) for c in fam)
    pl = []; rd = []
    for c in fam:
        N = int(Nzero(t, list(c), 6, p)); E = Fraction(N) - Fraction(M ** 6, p)
        fh.write(f"{nm}\t{p}\tplane\t{c[1]}\t{c[2]}\t{c[3]}\t{c[4]}\t{N}\t{M}\t{r0}\t{Fraction(N,p**3)}\t{E}\n"); pl.append((N, E))
    for _ in range(60):
        c = [1] + [rng.randrange(p) for _ in range(4)]
        N = int(Nzero(t, c, 6, p)); E = Fraction(N) - Fraction(M ** 6, p)
        fh.write(f"{nm}\t{p}\trandom\t{c[1]}\t{c[2]}\t{c[3]}\t{c[4]}\t{N}\t{M}\t{r0}\t{Fraction(N,p**3)}\t{E}\n"); rd.append((N, E))
    fh.flush()
    nb = sum(1 for N, E in pl if 2 * N >= p ** 3); nbE = sum(1 for N, E in pl if 2 * E >= p ** 3)
    rb = sum(1 for N, E in rd if 2 * N >= p ** 3); rbE = sum(1 for N, E in rd if 2 * E >= p ** 3)
    summ.append(f"{nm} p={p} M={M} roots={r0}: planes n={len(pl)} N/p^3>=1/2: {nb}, E/p^3>=1/2: {nbE}, median N/p^3={statistics.median([N/p**3 for N,E in pl]):.3f}, (p-r0)^3/p^3={(p-r0)**3/p**3:.3f} | random n={len(rd)} N/p^3>=1/2: {rb}, E>=: {rbE}, max N/p^3={max(N/p**3 for N,E in rd):.3f} | elapsed {now()-t_start:.0f}s")
    print(summ[-1], flush=True)
fh.close()
open("m2d_large_p_summary.txt", "w").write("\n".join(summ) + "\n")
