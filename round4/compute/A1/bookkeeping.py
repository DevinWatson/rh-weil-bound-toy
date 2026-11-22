"""A1 bookkeeping check (exact rational arithmetic, no floating point).

Models the combinatorial data of the induction invariant derived in A1:
  S_1 = Z, m_z(P_1) = 1;
  Sigma_1 = {0} with block rank 1 (the tame part of L at infinity);
  for i >= 2: Sigma_i = rho_i * S_{i-1}, rho_i = -c_{i-1}/c_i, block rank of rho_i*s in Q_i
              equals the block rank at infinity of P_i coming from s in S_{i-1}, which is m_s(P_{i-1});
  S_{i+1} = Z u Sigma_i (disjoint union if Z and Sigma_i do not meet), m_z(P_{i+1}) = r_{i+1} for z in Z,
  and m_w(P_{i+1}) for w in Sigma_i is the block rank of Q_i at w.
Ranks: r_1 = 1 and r_{i+1} = sum over s in S_i of m_s(P_i) (Laumon 2.3.1.1 (i), no slopes > 1).
Prediction to compare: r_2 = d, r_{i+1} = d r_i + r_{i-1}.

The points are formal: Z is a set of d distinct nonzero rationals standing for the roots, and the c_i are
rationals. This checks the bookkeeping (indices, scalings, signs, closed form), not the sheaf theory.
Run: python bookkeeping.py   (pure python, one process, no threads)
"""
from fractions import Fraction as Fr
import itertools, random, sys

def run(Z, c, kmax, label, out):
    d = len(Z)
    # c is a list indexed 1..kmax-1 (c[0] unused)
    rho = {i: -c[i-1] / c[i] for i in range(2, kmax)}
    # S[i]: dict point -> block rank m_s(P_i) (multiset merged by adding)
    S = {1: {z: 1 for z in Z}}
    Sigma = {}            # Sigma[i] = dict point -> rank of vanishing cycles of Q_i there
    r = {1: 1}
    first_fail = None
    out.append("== %s: d=%d, c=%s" % (label, d, [str(x) for x in c[1:kmax]]))
    for i in range(1, kmax):
        # rank of next = sum of block ranks at singular points of P_i
        r[i+1] = sum(S[i].values())
        # singular points of Q_i
        if i == 1:
            Sigma[1] = {Fr(0): 1}           # block a=0 (tame part of L at infinity), rank 1
        else:
            Sigma[i] = {}
            for s, m in S[i-1].items():
                w = rho[i] * s
                Sigma[i][w] = Sigma[i].get(w, 0) + m   # rank of Q_i's vanishing cycles at w = block rank of s in P_i
            # block rank at infinity of P_i from s in S_{i-1} is the rank of the vanishing cycles of Q_{i-1}...
        # intersection with Z
        meet = sorted(set(Z) & set(Sigma[i]))
        if meet and first_fail is None:
            first_fail = i
        # S_{i+1} = Z u Sigma_i ; rank m_z(P_{i+1}) = r_{i+1} for z in Z \ Sigma_i
        S[i+1] = {}
        for z in Z:
            S[i+1][z] = r[i+1]
        for w, m in Sigma[i].items():
            if w in S[i+1]:
                S[i+1][w] = None      # collision: invariant not applicable
            else:
                S[i+1][w] = m
        if any(v is None for v in S[i+1].values()):
            out.append("  i=%d: Sigma_%d meets Z in %d point(s): condition fails here" % (i, i, len(meet)))
            break
        out.append("  i=%d: |S_%d|=%d, r_%d=%d, |Sigma_%d|=%d, Sigma_%d meets Z: %s" %
                   (i, i+1, len(S[i+1]), i+1, r[i+1], i, len(Sigma[i]), i, bool(meet)))
    # compare ranks with the recursion
    ok = True
    for i in range(2, max(r)):
        pred = d * r[i] + r[i-1]
        if r.get(i+1) is not None and i in r and (i+1) in r and first_fail is None or (first_fail is not None and i < first_fail):
            if r[i+1] != pred:
                ok = False
                out.append("  rank mismatch at i=%d: %d vs %d" % (i, r[i+1], pred))
    out.append("  ranks r_1..: %s ; recursion d r_i + r_{i-1} matches while condition holds: %s" %
               ([r[i] for i in sorted(r)], ok))
    return first_fail

def closed_form_Sigma(Z, c, i):
    """Sigma_i as {pi(i,m) z : m = i, i-2, ..., >= 2} u ({0} if i odd), pi(i,m) = rho_i rho_{i-2} ... rho_m."""
    kmax = len(c)
    rho = {j: -c[j-1] / c[j] for j in range(2, kmax)}
    pts = set()
    if i % 2 == 1:
        pts.add(Fr(0))
    m = i
    prod = Fr(1)
    while m >= 2:
        prod *= rho[m]
        for z in Z:
            pts.add(prod * z)
        m -= 2
    return pts

def main():
    out = []
    random.seed(20261121)
    kmax = 9
    # generic example
    Z = [Fr(2), Fr(-3), Fr(5), Fr(7, 3), Fr(-11, 2)]
    c = [None] + [Fr(random.randint(1, 40), random.randint(1, 40)) * random.choice([1, -1]) for _ in range(kmax)]
    run(Z, c, kmax, "generic c", out)
    # closed form check against recursion for sets (using the same generic c)
    # rebuild recursion sets
    d = len(Z)
    rho = {i: -c[i-1] / c[i] for i in range(2, kmax)}
    S = {1: set(Z)}
    Sig = {1: {Fr(0)}}
    S[2] = set(Z) | Sig[1]
    for i in range(2, kmax):
        Sig[i] = {rho[i] * s for s in S[i-1]}
        S[i+1] = set(Z) | Sig[i]
    allgood = all(Sig[i] == closed_form_Sigma(Z, c, i) for i in range(1, kmax))
    out.append("closed form Sigma_i = {pi(i,m) z} u {0 if i odd} agrees with the recursion for i<=%d: %s" % (kmax-1, allgood))
    # plain quadric c = 1: rho = -1 for all i
    c1 = [None] + [Fr(1)] * kmax
    ff = run(Z, c1, kmax, "plain quadric c_i = 1", out)
    out.append("plain quadric: first i with Z meeting Sigma_i: %s (prediction: 4, since rho_4 rho_2 = 1 is in R')" % ff)
    # the two known failures of the sign statement
    # k=3, c_1=-c_2 : rho_2 = 1
    c3 = [None, Fr(3), Fr(-3), Fr(5)] + [Fr(1)] * (kmax - 3)
    ff = run(Z, c3, kmax, "c_1 = -c_2 (rho_2 = 1)", out)
    out.append("rho_2=1: first i with Z meeting Sigma_i: %s (prediction: 2)" % ff)
    # k=4, c=(1,1,-2): rho_2=-1, rho_3=1/2 ; condition for k=4 is i<=3
    c4 = [None, Fr(1), Fr(1), Fr(-2)] + [Fr(7, 5)] * (kmax - 3)
    ff = run(Z, c4, kmax, "c=(1,1,-2,...)", out)
    out.append("c=(1,1,-2,..): first i with Z meeting Sigma_i: %s (so k=4 with c=(1,1,-2) is inside the range i<=3 iff this is >= 4 or None)" % ff)
    # ratio condition explicit: Z = {2,-3,5,7/3,-11/2}; R' contains 1 and ratios
    Rp = {a / b for a in Z for b in Z}
    out.append("R' has %d elements (d=%d, d(d-1)+1 = %d)" % (len(Rp), d, d*(d-1)+1))
    txt = "\n".join(out)
    print(txt)
    with open(sys.argv[1] if len(sys.argv) > 1 else "bookkeeping_output.txt", "w", encoding="utf-8") as f:
        f.write(txt + "\n")

main()
