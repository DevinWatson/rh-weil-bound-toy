"""E5: N_4 over F_{3^n}, n = 2, 4, 6, for c in F_9, two (three) cubics over F_3.
Usage: python e5.py <n> <cubic-name> ...   Appends to e5_out.txt.  Uses agent C's validated field code (compute/C/ff.py), exact ints.
c-entries: 1, 2 = -1 (in F_3) and i with i^2 = -1 (in F_9 \\ F_3; its conjugate -i = i^3 gives the same N_4 because t is
Frobenius invariant for f over F_3, so the choice of root is immaterial).  The embedding of F_9 in F_{3^n} is the unique
subfield; i is found as a square root of -1 inside the field."""
import sys, time
sys.path.insert(0, "./compute/C")
import ff
import numpy as np

CUB = {"x^3+x+1": [1, 1, 0, 1], "x^3-x+1": [1, 2, 0, 1], "x^3+x^2+2": [2, 0, 1, 1]}
n = int(sys.argv[1])
names = sys.argv[2:]
F = ff.Field(3, n)
q = F.q
i_code = next(a for a in range(q) if int(F.mul[a, a]) == 2)
one, mone = 1, 2
cs = {
    "(1,1,1) [sum 0, control]": (1, 1, 1),
    "(1,1,-1)": (1, 1, 2),
    "(1,1,i)": (1, 1, i_code),
    "(1,i,i)": (1, i_code, i_code),
    "(i,1,1)": (i_code, 1, 1),
    "(1,i,1)": (1, i_code, 1),
    "(i,i,i) [sum 3i=0, control]": (i_code, i_code, i_code),
    "(1,i,-1-i) [sum 0, control]": (1, i_code, int(F.neg[int(F.add[1, i_code])])),
}
with open("e5_out.txt", "a", encoding="utf-8") as fh:
    for nm in names:
        t = F.t_of(CUB[nm])
        M = int(t.sum())
        for cn, c in cs.items():
            s = int(F.add[int(F.add[c[0], c[1]]), c[2]])
            t0 = time.time()
            v = ff.N_fast(F, t, list(c), 4)
            line = f"q={q} (F_3^{n}) f={nm} M={M} c={cn} codes={c} c1+c2+c3={'0' if s == 0 else 'nonzero'} N_4={v} N_4/q^2={v/q**2:.4f} (float for reading only) [{time.time()-t0:.1f}s]"
            print(line, flush=True)
            fh.write(line + "\n")
