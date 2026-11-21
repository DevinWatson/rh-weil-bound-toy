import ctypes, itertools, sys
ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x4000)
import numpy as np

def matchings(items):
    if not items:
        yield []
        return
    a = items[0]
    for i in range(1, len(items)):
        b = items[i]
        rest = items[1:i] + items[i+1:]
        for m in matchings(rest):
            yield [(a, b)] + m

def analyse(k):
    """rho=1 matchings x_i = x_j.  Edge e (0-based, e=0..k-2) joins positions e,e+1 with coefficient c_{e+1}.
    Q restricted to the plane = sum over classes {A,B} of (sum of c over edges between pairs A,B) y_A y_B;
    edges inside one pair give c y_A^2 (impossible for c != 0).  Returns list of (matching, classes)
    for admissible matchings: no inside edge, every class has >= 2 edges (a class of one edge forces c=0)."""
    out = []
    stats = dict(total=0, adjacent=0, singleton=0, adm=0)
    for m in matchings(list(range(k))):
        stats['total'] += 1
        pid = {}
        for a, (i, j) in enumerate(m):
            pid[i] = a; pid[j] = a
        cls = {}
        inside = False
        for e in range(k - 1):
            A, B = pid[e], pid[e + 1]
            if A == B:
                inside = True; break
            cls.setdefault((min(A, B), max(A, B)), []).append(e)
        if inside:
            stats['adjacent'] += 1; continue
        if any(len(v) < 2 for v in cls.values()):
            stats['singleton'] += 1; continue
        stats['adm'] += 1
        out.append((m, cls))
    return out, stats

def bad_fraction(k, q, adm, maxN=400000, seed=1):
    n = k - 1
    total = (q - 1) ** n
    rng = np.random.default_rng(seed)
    if total <= maxN:
        grids = np.array(list(itertools.product(range(1, q), repeat=n)), dtype=np.int64)
        exact = True
    else:
        grids = rng.integers(1, q, size=(maxN, n), dtype=np.int64)
        exact = False
    bad = np.zeros(len(grids), dtype=bool)
    for m, cls in adm:
        ok = np.ones(len(grids), dtype=bool)
        for key, edges in cls.items():
            s = grids[:, edges].sum(axis=1) % q
            ok &= (s == 0)
        bad |= ok
    return exact, len(grids), int(bad.sum())

if __name__ == '__main__':
    lines = []
    for k in (4, 6, 8, 10, 12):
        adm, st = analyse(k)
        ncls = {}
        for m, cls in adm:
            ncls[len(cls)] = ncls.get(len(cls), 0) + 1
        lines.append(f"k={k}: matchings {st['total']}, with an adjacent pair {st['adjacent']}, with a singleton class {st['singleton']}, admissible {st['adm']}; admissible by number of classes (= codim of c-subspace): {ncls}")
        if adm and k <= 10:
            lines.append("   first admissible: " + str(adm[0][0]) + " classes " + str(adm[0][1]))
        for q in (3, 5, 7, 11):
            if not adm:
                continue
            ex, n, b = bad_fraction(k, q, adm)
            lines.append(f"   q={q}: {'exhaustive' if ex else 'sample'} {n} vectors, {b} lie in a matching plane condition")
    open('matchings_out.txt', 'w').write('\n'.join(lines) + '\n')
    print('\n'.join(lines))
