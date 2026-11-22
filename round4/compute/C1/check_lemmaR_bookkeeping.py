# C1: re-predict stalk dimensions of Q_i = F_b(P_i) from the statements (1),(2),(4) of Lemma R alone
# (exact integers, no floating point), and compare with the COMPUTED column of the main-session engine output.
# Points are pairs (root_id, scalar mod p); the point 0 is (None, 0). Case 1: root z = 1 in F_3. Case 2: roots outside F_3.
import re, sys
P = 3
def norm(pt):
    r, s = pt
    s %= P
    return (None, 0) if (r is None or s == 0) else (r, s)
def scale(pt, c):  # multiply point by c in F_p
    return norm((pt[0], pt[1] * c))
def run(d, roots, rho, kmax):
    # state of P_i: dict point -> m_i(point) ; rank r_i
    Z = {norm((r, 1)): 1 for r in roots}   # roots with m_1 = 1
    m = {pt: 1 for pt in Z}; r = 1
    out = {}
    drops_prev = {norm((None, 0)): 1}      # i=1: N_1 singular at 0 with drop n_0 = 1 (L tame at infinity)
    for i in range(1, kmax + 1):
        # Q_i = F_b(P_i): rank = sum m ; drops
        if i == 1:
            drops = {norm((None, 0)): 1}
        else:
            drops = {scale(s, rho[i]): mult for s, mult in prev_m.items()}   # sing = rho_i * S_{i-1}, drop = m_{i-1}(s)
        rankQ = sum(m.values())
        out[i] = (rankQ, dict(drops))
        if i == kmax: break
        # P_{i+1} = j_!L (x) Q_i : need (G): no root among drops
        for pt in drops:
            assert pt not in Z, ("(G) fails at stage", i)
        newm = {pt: rankQ for pt in Z}      # at roots: m = rank Q_i (scalar chi != 1, N lisse)
        for pt, dr in drops.items():
            newm[pt] = dr                    # elsewhere: m = drop of N
        prev_m = m
        m = newm
    return out
def fval(pt, rootval):
    r, s = pt
    if r is None: return 0
    return None if rootval is None else (s * rootval) % P
# case 1: q=3, f=x-1, c=(1,1,1,1), rho_i = -1 ; case 2: f=x^3-x+1 (roots not in F_3), c=(1,1), rho_2=-1
cases = {1: dict(d=1, roots=['z'], rootval=1, rho={i: (-1) % P for i in range(2, 9)}, kmax=4),
         2: dict(d=3, roots=['z1', 'z2', 'z3'], rootval=None, rho={2: (-1) % P}, kmax=2)}
path = './compute/main-session-check/round4_check_out.txt'
lines = open(path).read().splitlines()
cur = None; res = {1: [], 2: []}
for ln in lines:
    mm = re.match(r'== case (\d+):', ln)
    if mm: cur = int(mm.group(1)) if mm.group(1) in ('1', '2') else None
    mm = re.match(r'\s+q3 d\d\s+h=(\d)\s+Q_(\d) at y=(\d)\s+N=\d+ predicted\s+(\d+) computed\s+(\d+)\s+AGREE \(valid\)', ln)
    if mm and cur in (1, 2):
        res[cur].append((int(mm.group(1)), int(mm.group(2)), int(mm.group(3)), int(mm.group(5))))
tot = bad = 0
for cs, cfg in cases.items():
    out = run(cfg['d'], cfg['roots'], cfg['rho'], cfg['kmax'])
    for h, i, y, comp in res[cs]:
        rankQ, drops = out[i]
        pred = rankQ - sum(dr for pt, dr in drops.items() if fval(pt, cfg['rootval']) == y)
        tot += 1
        if pred != comp:
            bad += 1; print('MISMATCH case', cs, 'h', h, 'Q', i, 'y', y, 'pred', pred, 'computed', comp)
    print('case', cs, 'ranks', [out[i][0] for i in sorted(out)])
print('compared', tot, 'values, mismatches', bad)
