"""Exact check (symbolic): the draft's closed form of Sigma_i (S3) against the recursion Sigma_i = rho_i (Z u Sigma_{i-2}), Sigma_1={0}, for i <= 14.
Elements are pairs (frozenset-free tuple of rho-indices, root tag) with root tag 'Z' or 'zero'; 'zero' absorbs rho's."""
def rec(imax):
    Sig = {0: set(), 1: {('zero',)}}
    # Sigma_i = rho_i * (Z u Sigma_{i-2}); Sigma_0 := empty (so Sigma_2 = rho_2 Z)
    for i in range(2, imax + 1):
        new = set()
        new.add(((i,), 'Z'))
        for s in Sig[i - 2]:
            if s == ('zero',): new.add(('zero',))
            else: new.add(((i,) + s[0], 'Z'))
        Sig[i] = new
    return Sig
def closed(i):
    out = set()
    for m in range(0, i // 2):     # 0 <= m <= floor(i/2)-1
        out.add((tuple(i - 2 * j for j in range(m + 1)), 'Z'))
    if i % 2 == 1: out.add(('zero',))
    return out
Sig = rec(14)
bad = [i for i in range(1, 15) if Sig[i] != closed(i)]
print("closed form of S3 equals recursion for i=1..14:", not bad, bad)
