import csv, os
HERE = os.path.dirname(os.path.abspath(__file__))
def load(path):
    d = {}
    for r in csv.DictReader(open(path), delimiter="\t"):
        d[(r["f"], int(r["p"]))] = (int(r["M"]), int(r["N_4"]))
    return d
C = load(os.path.join(HERE, "crosscheck.tsv"))
B = load(os.path.join(HERE, "..", "B", "n4_table.tsv"))
only_c = sorted(set(C) - set(B)); only_b = sorted(set(B) - set(C))
mism = [(k, C[k], B[k]) for k in C if k in B and C[k] != B[k]]
agree = sum(1 for k in C if k in B and C[k] == B[k])
print("C rows", len(C), "B rows", len(B), "agree", agree, "mismatch", len(mism))
print("only in C", only_c); print("only in B", only_b)
for m in mism: print("MISMATCH", m)
