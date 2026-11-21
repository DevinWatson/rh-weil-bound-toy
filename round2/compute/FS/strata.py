import ctypes, itertools, sympy as sp
ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x4000)

def analyse(k):
    c = sp.symbols('c1:%d' % k)
    x = sp.symbols('x1:%d' % (k + 1))
    out = []
    for s in range(1, k + 1):
        for I in itertools.combinations(range(1, k + 1), s):
            # homogeneous Qtilde = sum c_a X_a X_{a+1} prod_{i != a,a+1} Z_i ; at infinity X=1,Z=0 ; else X=x_i, Z=1
            E = 0
            minord = None
            for a in range(1, k):
                term = c[a - 1]
                for i in range(1, k + 1):
                    if i in (a, a + 1):
                        term *= (1 if i in I else x[i - 1])
                    else:
                        term *= (0 if i in I else 1)
                E += term
            contained = sp.expand(E) == 0
            # vanishing order in the u_i, i in I: min over edges of |I minus edge|
            ords = [len([i for i in I if i not in (a, a + 1)]) for a in range(1, k)]
            dim_in_Ybar = (k - s) if contained else (k - s - 1)
            out.append((I, contained, dim_in_Ybar, min(ords)))
    return out

for k in range(3, 9):
    res = analyse(k)
    divs_contained = [I for I, cont, d, o in res if cont and d == k - 2]
    divs_other = [I for I, cont, d, o in res if (not cont) and d == k - 2]
    nonadj = [I for I in divs_contained]
    # checks
    ok_pairs = all(len(I) == 2 and I[1] - I[0] >= 2 for I in divs_contained)
    contained_small = [I for I, cont, d, o in res if cont and len(I) <= 2]
    exp_pairs = (k - 1) * (k - 2) // 2
    cont3 = all(cont for I, cont, d, o in res if len(I) >= 3)
    print("k=%d: boundary divisors from contained strata: %d (expected non-adjacent pairs %d), only non-adjacent pairs: %s; "
          "single-infinity divisors S_a cut out by l_a=0: %d (expected %d); all |I|>=3 strata contained: %s; "
          "adjacent pairs contained: %s" % (
              k, len(divs_contained), exp_pairs, ok_pairs, len(divs_other), k, cont3,
              any(cont for I, cont, d, o in res if len(I) == 2 and I[1] - I[0] == 1)))
