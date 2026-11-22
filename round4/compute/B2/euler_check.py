# B2: independent exact check of the Euler characteristic of j_* M_k implied by invariant J of PROOF_V2 S5.
# Points of S_i carry (is_root, m) with m = rank of the non-invariant part of M_i at that point (roots: m = r_i).
# Claimed: dim H^0_c(A^1,P_k) = -chi_c(A^1, j_*M_k) = r_{k+1} - [k odd].
import sys
def run(d,K):
    # S[i] list of (isroot, m)
    S={0:[(False,1)]}   # S_0 = {0}, m_0(0)=1 (rank of the a=0 tame block of M_1 = L)
    r={1:1}
    S[1]=[(True,1)]*d
    out=[]
    for i in range(1,K+1):
        # M_i: rank r[i], points S[i]
        ri=r[i]
        pts=S[i]
        # block structure at infinity: frequencies from S_{i-1} (for i>=2) ; for i=1 only a=0 block rank 1
        if i==1:
            blocks=[(True,1)]  # a=0
            n0=1
        else:
            blocks=[(s_is_root,mm) for (s_is_root,mm) in S[i-1]]  # block rank = m_{i-1}(s)
            # is a=0 present: need a point 0 in S_{i-1}: it is the non-root point coming from S_{i-3}... track below
        # track which points are zero: we need explicit tracking, redo with ids
        break
    return None
# explicit tracking with labels
def run2(d,K):
    # each point: (label, m); label 'z' root, 'zero' for point 0, else tuple tag
    # Sigma_i = rho_i * S_{i-1}; point 0 maps to 0 (label 'zero' kept).
    S={0:[('zero',1)]}
    r={1:1}
    S[1]=[('z',1)]*d
    res=[]
    for i in range(1,K+1):
        ri=r[i]
        pts=S[i]
        # rank of M_{i+1}= rank N_i = sum over S_i of m
        rn=sum(m for (_,m) in pts)
        # roots in S_i carry m=r_i; check
        for (lab,m) in pts:
            if lab=='z': assert m==ri,(i,m,ri)
        # blocks of M_i at infinity: from S_{i-1}
        if i==1:
            swan=0
        else:
            n0=sum(m for (lab,m) in S[i-1] if lab=='zero')
            swan=ri-n0
            assert sum(m for (_,m) in S[i-1])==ri,(i,)
        chiU=1-len(pts)   # P^1 minus (pts + infinity)  : 2-(len+1)
        inv=sum(ri-m for (_,m) in pts)
        chi=ri*chiU-swan+inv
        res.append((i,ri,-chi, rn-(1 if i%2==1 else 0)))
        r[i+1]=rn
        # S_{i+1} = Z (m=r_{i+1}) U rho_i * S_{i-1}  with m_{i+1}(rho_i s)=m_{i-1}(s)
        sig=[(('zero' if lab=='zero' else 'o'),m) for (lab,m) in S[i-1]]
        if i==1: sig=[('zero',1)]
        S[i+1]=[('z',rn)]*d+sig
    return res
bad=0
for d in (1,2,3,4,5,6,7,9):
    for (i,ri,dimH,claim) in run2(d,14):
        ok = dimH==claim
        if not ok: bad+=1
        print(d,i,ri,dimH,claim,'OK' if ok else 'MISMATCH')
print('mismatches',bad)
