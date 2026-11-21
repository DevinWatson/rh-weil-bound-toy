import json,time
import fibre_p3 as F
d=json.load(open("p3_sequences.json"))
t0=time.time()
for name,c in d["cfgs"].items():
    s=F.run(13,c["a"],c["cs"])
    c["seq"].append(list(s)); print(name,s,round(time.time()-t0,1),flush=True)
json.dump(d,open("p3_sequences_n13.json","w"))
