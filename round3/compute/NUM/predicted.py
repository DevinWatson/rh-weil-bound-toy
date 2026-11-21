"""Predicted degree D_k = dim H^1_c(A^1, P_k) under Claim B's structure (all P_i middle extensions, slopes <= 1 at infinity,
vanishing-cycle bookkeeping by stationary phase).  This is an Euler-characteristic bookkeeping of the *claimed* picture, my own derivation:
  P_1: rank 1, singular points Z (drop 1 each), tame at infinity.
  FT_b(P): rank = sum of drops; singular at -a/b for each nonzero frequency a of P at infinity (drop = dim of that piece) and at 0 with drop r - W
           (r = rank P, W = total dim of the nonzero-frequency pieces at infinity).
  P_{i+1} = j_!(L (x) FT_{c_i}(P_i)): singular points Z (drop = rank, stalk 0) u sing(FT); frequencies at infinity {c_i s : s in sing(P_i)} with dims drop_s
  (s = 0 gives frequency 0 = tame part).
  dim H^1_c(A^1, P) = sum(drops) + W - r.
Check at k=2: d^2+1, matches the data for f of degree 3 (D=10).  Points kept as exact field elements; coincidences are reported."""
import sys
import numpy as np
from ffl import *
from cond import split_field

def predict(f, e, cexp):
    k = len(cexp) + 1
    M, F, Z = split_field(f, e)
    c = [fq_element(M, e, x) for x in cexp]
    inv = lambda a: F.inv(a)
    mul = lambda a, b: int(F.mul(np.array([a]), np.array([b]))[0])
    neg = lambda a: int(F.neg(np.array([a]))[0])
    # state P_1
    r = 1
    sing = {z: 1 for z in Z}
    freq = {}   # nonzero frequencies at infinity: key code -> dim ; tame dims not tracked
    out = []
    flags = []
    def Hdim(r, sing, freq):
        return sum(sing.values()) + sum(freq.values()) - r
    out.append(Hdim(r, sing, freq))
    for i in range(1, k):          # build P_{i+1} using c_i  (c list index i-1)
        ci = c[i - 1]
        W = sum(freq.values())
        rnew = sum(sing.values())
        newsing = {}
        for a, dim in freq.items():
            w = mul(neg(a), inv(ci))      # -a / b with b = c_i   (FT_{c_i} of P_i)
            newsing[w] = newsing.get(w, 0) + dim
        if r - W > 0:
            newsing[0] = newsing.get(0, 0) + (r - W)
        # P_{i+1}: add Z with full drop
        for z in Z:
            if z in newsing:
                flags.append('coincidence Z & sing(FT) at level %d' % (i + 1))
            newsing[z] = rnew
        newfreq = {}
        for s, dim in sing.items():
            a = mul(ci, s)
            if a != 0:
                newfreq[a] = newfreq.get(a, 0) + dim
        r, sing, freq = rnew, newsing, newfreq
        out.append(Hdim(r, sing, freq))
    return out, flags

if __name__ == '__main__':
    F1 = [2, 1]; F3 = [1, 2, 0, 1]
    tests = [('f1 k=2..6 c=1', F1, 1, [0]*5), ('f3 k=2..5 c=1', F3, 1, [0]*4),
             ('f1 e=2 gen', F1, 2, [7, 6, 4, 7, 3]), ('f3 e=2 gen', F3, 2, [7, 6, 4, 7, 3])]
    for lab, f, e, ce in tests:
        o, fl = predict(f, e, ce)
        print(lab, 'D_1..D_k =', o, fl)
