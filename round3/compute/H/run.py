"""usage: python run.py configs_module out.jsonl mmax [budget_seconds]
Configs: list of dict(name, e, f (F_3 coeffs low->high), cexp (gamma exponents, None=0 not allowed), hexp, k)
Loops over field degree m (outer) and configs (inner) so each field is built once. Appends JSON lines."""
import sys, json, time, importlib
import numpy as np
from ffl import *

mod = importlib.import_module(sys.argv[1])
outf = sys.argv[2]
mmax = int(sys.argv[3])
budget = float(sys.argv[4]) if len(sys.argv) > 4 else 540
t0 = time.time()

done = set()
try:
    for line in open(outf):
        r = json.loads(line)
        done.add((r['name'], r['n']))
except FileNotFoundError:
    pass

dead = set()
for m in range(1, mmax + 1):
    F = None
    chicache = {}
    for cfg in mod.CONFIGS:
        e = cfg['e']
        if m % e or cfg['name'] in dead:
            continue
        n = m // e
        if (cfg['name'], n) in done:
            continue
        if time.time() - t0 > budget:
            print('time budget reached at m =', m); sys.exit(0)
        if F is None:
            ts = time.time(); F = field(m); print('field', m, 'built in %.1fs' % (time.time() - ts), flush=True)
        key = tuple(cfg['f'])
        if key not in chicache:
            chicache[key] = chi_array(F, list(cfg['f']))
        t = chicache[key]
        cc = [fq_element(m, e, x) for x in cfg['cexp']]
        hh = fq_element(m, e, cfg['hexp'])
        ts = time.time()
        try:
            a, b, mx = fibre_sum(F, t, cc, hh)
        except OverflowError as ex:
            print(cfg['name'], 'n', n, 'OVERFLOW', ex); dead.add(cfg['name']); continue
        # float sanity check of the sum magnitude (S bounded by Q^((k+1)/2) *2)
        assert abs(a) + abs(b) < 4 * float(F.Q) ** ((cfg['k'] + 1) / 2) + 10, ('sum too large', cfg['name'], n, a, b)
        rec = dict(name=cfg['name'], e=e, n=n, m=m, k=cfg['k'], f=cfg['f'], cexp=cfg['cexp'], hexp=cfg['hexp'], a=a, b=b, maxcoord=mx)
        with open(outf, 'a') as fh:
            fh.write(json.dumps(rec) + '\n')
        print(cfg['name'], 'n', n, 'S =', a, '+', b, 'w  (%.1fs, maxcoord %.2e)' % (time.time() - ts, mx), flush=True)
print('finished, total %.0fs' % (time.time() - t0))
