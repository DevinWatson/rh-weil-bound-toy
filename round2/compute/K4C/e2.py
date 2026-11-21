"""E2: map of the bad set of E(a,b) = sum_r C(r) C(a r + b), all a != 0, all b."""
import sys
from fractions import Fraction
from core import *

PR = (11, 13, 17, 19, 23, 29, 31) + ((37, 41, 43, 47, 53) if "extra" in sys.argv else ())
lines = []
summary = []


def ftypes(p):
    d = {}
    for name, roots in (("3roots(1,2,4)", [1, 2, 4]), ("3roots(1,3,9)", [1, 3, 9])):
        co = poly_from_roots(roots, p)
        if squarefree_mod_p(co, p) and co[0] % p:
            d[name] = (co, roots)
    d["irred_cubic"] = (first_irreducible_cubic(p), [])
    d["quintic"] = (pick_quintic(p), roots_mod_p(pick_quintic(p), p))
    return d


for p in PR:
    for name, (co, roots) in ftypes(p).items():
        t = t_table(p, co)
        C = Cvec(p, t)
        M, t0 = int(t.sum()), int(t[0])
        ratios = sorted({(ej * pow(ei, p - 2, p)) % p for ei in roots for ej in roots if ei != ej})
        E = {(a, b): E_ab(p, C, a, b) for a in range(1, p) for b in range(p)}
        flagged = {k: v for k, v in E.items() if 2 * abs(v) > p * p}
        P1 = {k for k in E if k == (1, 0)}
        P2 = {k for k in E if (k[0] + k[1]) % p == 1}
        lines.append(f"## p={p} f={name} coefs(low first)={co} roots={roots} M={M} t0={t0} ratios_of_roots={ratios}")
        lines.append(f"   flagged pairs (|E|/p^2 > 1/2): {len(flagged)} of {len(E)}")
        for (a, b), v in sorted(flagged.items()):
            tag = []
            if (a, b) in P1: tag.append("a=1,b=0")
            if (a + b) % p == 1: tag.append("a+b=1")
            if a in ratios: tag.append("a=root-ratio")
            if b == 0: tag.append("b=0")
            if a == p - 1: tag.append("a=-1")
            lines.append(f"   (a,b)=({a},{b}) E={v} E/p^2={Fraction(v, p * p)} [{','.join(tag)}]")
        # largest |E|/p^2 among unflagged and among pairs outside P1 u P2
        rest = [(abs(v), k) for k, v in E.items() if k not in P2 and k not in P1]
        mx, kx = max(rest)
        flagged_outside = [k for k in flagged if k not in P2]
        lines.append(f"   max |E| outside (a+b=1 line): {mx} at {kx}, ratio {Fraction(mx, p*p)}; flagged outside a+b=1: {flagged_outside}")
        onP2 = [abs(E[k]) for k in P2]
        lines.append(f"   on a+b=1: min |E|/p^2 = {Fraction(min(onP2), p*p)}  max = {Fraction(max(onP2), p*p)}; signs: {[ (k[0], E[k]) for k in sorted(P2)][:6]}...")
        summary.append((p, name, len(flagged), len(flagged_outside), len(P2), sum(1 for k in P2 if k in flagged), flagged_outside))
lines.append("")
lines.append("SUMMARY: p, f, #flagged, #flagged outside a+b=1, |line a+b=1|, #line flagged, flagged-outside list")
for s in summary:
    lines.append(str(s))
open("e2_out%s.txt" % ("_extra" if "extra" in sys.argv else ""), "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("\n".join(lines[-len(summary) - 2:]))
