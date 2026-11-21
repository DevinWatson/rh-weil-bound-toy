import json,time,sys
import fibre_p3 as F
cfgs=[("k2_a1",1,[1]),("k2_a2",2,[1]),("k3_good_11",1,[1,1]),("k3_bad_12",1,[1,2]),("k4_good_111",1,[1,1,1]),("k4_good_111_a2",2,[1,1,1]),("k5_111_1",1,[1,1,1,1])]
N=int(sys.argv[1])
res={c[0]:[] for c in cfgs}
t0=time.time()
for n in range(1,N+1):
    for name,a,cs in cfgs:
        res[name].append(F.run(n,a,cs))
    print(n,round(time.time()-t0,1),flush=True)
    json.dump({"cfgs":{c[0]:{"a":c[1],"cs":c[2],"seq":res[c[0]]} for c in cfgs}},open("p3_sequences.json","w"))
