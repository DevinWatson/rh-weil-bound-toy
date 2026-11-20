"""H5: exact tangency test (h3 method) at SPECIAL root configurations, even k, random rational coefficients c and c=1.
Configs: sum of roots zero (trace-zero cubic, e.g. x^3+x+1); a root pair r,-r (plus a third root); both."""
import random, sys
from sympy import Rational
from h3_tangency import tangent_cases
rng = random.Random(5)
def rr(): return Rational(rng.randint(2, 10**6), rng.randint(1, 10**3))
configs = {}
a, b = rr(), rr()
configs["sum zero: r1+r2+r3=0"] = [a, b, -a - b]
configs["pair r,-r plus s"] = [a, -a, b]
configs["pair r,-r, and 2r"] = [a, -a, 2 * a]
configs["generic"] = [a, b, rr()]
for name, roots in configs.items():
    for k in (4, 6):
        for mode in ("ones", "randc"):
            c = [1] * (k - 1) if mode == "ones" else [Rational(rng.randint(1, 10**4), rng.randint(1, 10**2)) for _ in range(k - 1)]
            total, bad = tangent_cases(k, roots, c)
            print("%-26s k=%d c=%-5s tested=%d tangent=%d %s" % (name, k, mode, total, len(bad),
                  ("e.g. S=%s sigma=%s" % ([i+1 for i in bad[0][0]], list(bad[0][1]))) if bad else ""), flush=True)
