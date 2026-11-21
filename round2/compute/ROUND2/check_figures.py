import ctypes, re
ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x4000)
base = "./round2/compute/"
# RED plane rows
mx = 0.0
n = 0
ps = []
for line in open(base + "RED/k4_plane_out.txt", encoding="utf8"):
    if "c1+c2+c3=0 sum 0" in line:
        n += 1
        m = re.search(r"D2/p3 ([0-9.]+)", line)
        v = float(m.group(1))
        mx = max(mx, v)
        ps.append(int(line.split()[1]))
print("RED plane rows", n, "max D2/p3", mx, "max p", max(ps))
# NUM m1c totals
tot_bad = 0
tot_P = 0
tot_Ptotal = 0
tot_Pnotbad = 0
for line in open(base + "NUM/m1c_all_primes.txt", encoding="utf8"):
    if line.startswith(("f1", "f2", "f3", "f4")):
        parts = line.split("|")
        bad = int(parts[1])
        cls = parts[2].split()
        P = int(cls[0])
        ptot = int(parts[3])
        pnb = int(parts[4])
        tot_bad += bad
        tot_P += P
        tot_Ptotal += ptot
        tot_Pnotbad += pnb
print("NUM m1c: bad", tot_bad, "P", tot_P, "plane total", tot_Ptotal, "plane not bad", tot_Pnotbad)
