# Exact fibre sums S_h(F_{3^n}) = sum t(x1)..t(xk) psi(h Q_c(x)), f = x - a (d=1), q=3, values in Z[omega] (pairs (a,b)=a+b*omega).
# Exact integer arithmetic (int64 pairs). Used only to TEST Claim B's dimension formula for d=1 (HINT/CHECKED as stated in report).
import ctypes, sys, json
ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x4000)
import numpy as np
p=3
def pmulmod(a,b,poly,n):
    r=np.convolve(a,b)%p
    # reduce modulo monic poly (list length n+1, poly[n]=1)
    for i in range(len(r)-1,n-1,-1):
        c=r[i]
        if c:
            r[i-n:i+1]=(r[i-n:i+1]-c*np.array(poly))%p
    return r[:n]
def ppow(poly,n,e):
    res=np.zeros(n,dtype=np.int64);res[0]=1
    base=np.zeros(n,dtype=np.int64)
    if n>1: base[1]=1
    else: base[0]=(-poly[0])%p
    while e:
        if e&1: res=pmulmod(res,base,poly,n)
        base=pmulmod(base,base,poly,n); e>>=1
    return res
def primes_of(m):
    f=[];d=2
    while d*d<=m:
        if m%d==0:
            f.append(d)
            while m%d==0:m//=d
        d+=1
    if m>1:f.append(m)
    return f
def find_primitive(n):
    q=p**n; fs=primes_of(q-1)
    rng=np.random.default_rng(12345+n)
    while True:
        poly=[int(v) for v in rng.integers(0,p,n)]+[1]
        if poly[0]==0: continue
        one=np.zeros(n,dtype=np.int64);one[0]=1
        if not np.array_equal(ppow(poly,n,q-1),one): continue
        if all(not np.array_equal(ppow(poly,n,(q-1)//r),one) for r in fs):
            return poly
def build(n):
    q=p**n; poly=find_primitive(n)
    pw=np.array([p**j for j in range(n)],dtype=np.int64)
    exp=np.zeros(q-1,dtype=np.int64); vecs=np.zeros((q-1,n),dtype=np.int64)
    cur=[0]*n; cur[0]=1
    pl=poly[:n]
    for i in range(q-1):
        exp[i]=sum(cur[j]*pw[j] for j in range(n)) if n<=0 else 0
        vecs[i]=cur
        top=cur[-1]
        cur=[0]+cur[:-1]
        if top:
            cur=[(cur[j]-top*pl[j])%p for j in range(n)]
    codes=vecs@pw
    log=np.full(q,-1,dtype=np.int64); log[codes]=np.arange(q-1)
    return q,poly,pw,codes,log,vecs
def trace_of_pow(m,q,n,codes,vecs):
    # Tr(g^m) as element of F_p: sum of conjugates g^{m p^s}; sum of vectors; result lies in F_p (vector (c,0..0))
    tot=np.zeros(n,dtype=np.int64)
    for s in range(n):
        tot=(tot+vecs[(m*p**s)%(q-1)])%p
    assert all(tot[1:]==0)
    return int(tot[0])
def wmul(x,k):
    a,b=x
    for _ in range(k%3):
        a,b=-b,a-b
    return a,b
def dft_axis(re,im,ax):
    re=np.moveaxis(re,ax,0);im=np.moveaxis(im,ax,0)
    x=[(re[m],im[m]) for m in range(3)]
    outs=[]
    for u in range(3):
        sa=np.zeros_like(re[0]);sb=np.zeros_like(re[0])
        for m in range(3):
            a,b=wmul(x[m],(m*u)%3)
            sa=sa+a;sb=sb+b
        outs.append((sa,sb))
    re2=np.stack([o[0] for o in outs]);im2=np.stack([o[1] for o in outs])
    return np.moveaxis(re2,0,ax),np.moveaxis(im2,0,ax)
_cache={}
def run(n,a,cs,h=1):
    if n not in _cache: _cache.clear(); _cache[n]=build(n)
    q,poly,pw,codes,log,vecs=_cache[n]
    # chi table over codes
    chi=np.zeros(q,dtype=np.int64)
    chi[codes]=np.where(np.arange(q-1)%2==0,1,-1)
    allc=np.arange(q)
    d0=allc%p
    shifted=allc-d0+((d0-a)%p)
    t=chi[shifted]
    # Gram matrix B_ij = Tr(x^{i+j}) with basis x^i
    trs=[trace_of_pow(m,q,n,codes,vecs) for m in range(2*n-1)]
    B=np.array([[trs[i+j] for j in range(n)] for i in range(n)],dtype=np.int64)
    # digits of all codes: code = sum d_j p^j
    Y=np.stack([(allc//p**j)%p for j in range(n)],axis=1)
    k=len(cs)+1
    re=t.copy().astype(np.int64); im=np.zeros(q,dtype=np.int64)
    for i in range(k-1):
        hc=(h*cs[i])%p
        # hatG(u)=sum_x G(x) w^{x.u}; array axes: reshape (p,)*n in C order => axis0 = digit n-1
        R=re.reshape((p,)*n);I=im.reshape((p,)*n)
        for ax in range(n):
            R,I=dft_axis(R,I,ax)
        Rf=R.reshape(q);If=I.reshape(q)
        U=(hc*(Y@B.T))%p   # u_i = hc * sum_j B_ij y_j
        ucode=U@pw
        Ar=Rf[ucode];Ai=If[ucode]
        re=Ar*t; im=Ai*t
    return int(re.sum()),int(im.sum())
if __name__=="__main__":
    a=int(sys.argv[1]); cs=[int(v) for v in sys.argv[2].split(",")]; N=int(sys.argv[3]); out=sys.argv[4]
    res=[]
    for n in range(1,N+1):
        s=run(n,a,cs)
        res.append(s); print(n,s,flush=True)
        json.dump({"a":a,"cs":cs,"seq":res},open(out,"w"))
