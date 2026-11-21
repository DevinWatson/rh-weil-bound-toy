import json, glob
from predicted import predict
summ={}
for fn in sorted(glob.glob('analysis*.txt.summary.json')):
    summ.update(json.load(open(fn)))
recs={}
for fn in sorted(glob.glob('results*.jsonl')):
    for line in open(fn,encoding='utf-8-sig'):
        r=json.loads(line); recs[r['name']]=r
lines=[]
for name,r in recs.items():
    o,fl=predict(r['f'],r['e'],r['cexp'])
    s=summ[name]
    lines.append("%-18s k=%d e=%d predicted D_k=%-4d (Euler-char bookkeeping; coincidence flags %d) | observed: last nonzero L index %d of N=%d, trailing zeros %d -> %s"%(name,r['k'],r['e'],o[-1],len(fl),s['last_nonzero'],s['N'],s['trailing_zeros'],
        ('POLYNOMIAL deg %d'%s['last_nonzero'] if s['trailing_zeros']>=2 else 'series not terminated within N')))
open('predicted_vs_observed.txt','w').write("\n".join(lines)+"\n"); print("\n".join(lines))
