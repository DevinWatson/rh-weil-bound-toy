# Exact rank of Hankel matrices of sequences in Z[omega] (omega^2+omega+1=0), Gaussian elimination over Q(omega) with Fractions.
import json,sys
from fractions import Fraction as Fr
def mul(x,y):
    a,b=x;c,d=y
    return (a*c-b*d, a*d+b*c-b*d)
def inv(x):
    a,b=x; N=a*a-a*b+b*b
    return (Fr(a-b)/N, Fr(-b)/N)
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def iszero(x): return x[0]==0 and x[1]==0
def rank(M):
    M=[[ (Fr(a),Fr(b)) for (a,b) in row] for row in M]
    r=0;rows=len(M);cols=len(M[0])
    for c in range(cols):
        piv=None
        for i in range(r,rows):
            if not iszero(M[i][c]): piv=i;break
        if piv is None: continue
        M[r],M[piv]=M[piv],M[r]
        iv=inv(M[r][c])
        for i in range(r+1,rows):
            if not iszero(M[i][c]):
                f=mul(M[i][c],iv)
                M[i]=[sub(M[i][j],mul(f,M[r][j])) for j in range(cols)]
        r+=1
    return r
def hank_ranks(seq):
    # seq[0..N-1] = s_1..s_N. Hankel H_m = (s_{i+j+1})_{0<=i,j<m}, needs 2m-1 terms
    out={}
    N=len(seq)
    m=1
    while 2*m-1<=N:
        H=[[seq[i+j] for j in range(m)] for i in range(m)]
        out[m]=rank(H)
        m+=1
    return out
if __name__=="__main__":
    d=json.load(open(sys.argv[1]))
    for name,c in d["cfgs"].items():
        seq=[tuple(x) for x in c["seq"]]
        hr=hank_ranks(seq)
        print(name,"a=",c["a"],"cs=",c["cs"],"nterms=",len(seq))
        print("   Hankel rank by size m:",hr)
