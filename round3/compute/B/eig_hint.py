# FLOATING POINT, HINT ONLY: roots of the order-D recurrence for the d=1, q=3 sequences; moduli compared with 3^(w/2).
import json,numpy as np,cmath
d=json.load(open("p3_sequences_n13.json"))
w=cmath.exp(2j*cmath.pi/3)
for name,D in [("k2_a1",2),("k3_good_11",2),("k4_good_111",5),("k3_bad_12",1),("k5_111_1",6)]:
    c=d["cfgs"][name]; s=np.array([a+b*w for a,b in c["seq"]])
    # solve s_{n+D}= sum_j c_j s_{n+D-1-j}, least squares on 13-D equations
    A=np.array([[s[n+D-1-j] for j in range(D)] for n in range(len(s)-D)])
    y=np.array([s[n+D] for n in range(len(s)-D)])
    # scale to avoid conditioning blow-up: use q^{-n/2}-type normalisation not needed for D<=6 at this size
    cj,res,rk,sv=np.linalg.lstsq(A,y,rcond=None)
    roots=np.roots(np.concatenate([[1],-cj]))
    print(name,"D=",D,"moduli/3^(1/2):",sorted(round(abs(r)/3**0.5,4) for r in roots))
