"""H4: same exact tangency test as h3 but over F_p with random root triples and random nonzero coefficients c.
Counts, for fixed p, how many (S, sigma) strata are tangent to Y, as k grows.  Exact integer arithmetic mod p.
Tangent means: the linear system  A_cc u = -A_cS a ,  a^T A_Sc u = -a^T A_SS a  has a solution over F_p
(this is a critical point of Q|F on Y with all coordinates in F_p; solutions over the algebraic closure are the right notion
for Bertini, so this UNDER-reports tangency over Fbar_p).  Ignores the condition x_j notin Z for j notin S (over-reports).
"""
import ctypes, itertools, random, sys
ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x4000)

def rank_mod(M, p):
    M = [row[:] for row in M]
    r = 0
    rows = len(M); cols = len(M[0]) if rows else 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i][c] % p:
                piv = i; break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c], -1, p)
        M[r] = [(v * inv) % p for v in M[r]]
        for i in range(rows):
            if i != r and M[i][c] % p:
                f = M[i][c]
                M[i] = [(vi - f * vr) % p for vi, vr in zip(M[i], M[r])]
        r += 1
        if r == rows:
            break
    return r

def count_tangent(k, p, roots, c):
    A = [[0] * k for _ in range(k)]
    for i in range(k - 1):
        A[i][i + 1] = c[i] % p; A[i + 1][i] = c[i] % p
    d = len(roots)
    n_tan = 0
    first = None
    for s in range(1, k + 1):
        for S in itertools.combinations(range(k), s):
            Sc = [j for j in range(k) if j not in S]
            for sig in itertools.product(range(d), repeat=s):
                a = [roots[i] for i in sig]
                const = sum(a[x] * A[S[x]][S[y]] * a[y] for x in range(s) for y in range(s)) % p
                if Sc:
                    coef = []
                    rhs = []
                    for j in Sc:
                        coef.append([A[j][l] for l in Sc])
                        rhs.append((-sum(A[j][S[x]] * a[x] for x in range(s))) % p)
                    coef.append([sum(a[x] * A[S[x]][l] for x in range(s)) % p for l in Sc])
                    rhs.append((-const) % p)
                    aug = [row + [rv] for row, rv in zip(coef, rhs)]
                    ok = rank_mod(coef, p) == rank_mod(aug, p)
                else:
                    ok = (const == 0)
                if ok:
                    n_tan += 1
                    if first is None:
                        first = (S, sig)
    return n_tan, first

if __name__ == "__main__":
    k = int(sys.argv[1]); p = int(sys.argv[2]); trials = int(sys.argv[3]); d = 3
    rng = random.Random(20261120 + 7 * k + p)
    with_tan = 0; tot_tan = 0
    for _ in range(trials):
        roots = rng.sample(range(1, p), d)
        c = [rng.randint(1, p - 1) for _ in range(k - 1)]
        n, first = count_tangent(k, p, roots, c)
        with_tan += (n > 0); tot_tan += n
    print("k=%d p=%d trials=%d: root/coefficient draws with at least one tangent stratum: %d ; total tangent strata: %d (of %d strata per draw)"
          % (k, p, trials, with_tan, tot_tan, 4 ** k - 1), flush=True)
