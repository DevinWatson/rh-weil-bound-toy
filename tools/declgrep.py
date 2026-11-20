"""Search the declaration-name index of the archive.

usage: python -I declgrep.py <regex> [max_hits]
Prints: kind  name  module:line   (the regex is matched against "name<TAB>module")
To read a module's text afterwards:
  python -I <workspace>/remark-review-20261120/tgrep.py --cat lean/src/<Module/Path>.lean [max_chars]
"""
import re
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass
pat = re.compile(sys.argv[1])
cap = int(sys.argv[2]) if len(sys.argv) > 2 else 60
hits = 0
with open("E:/claude-scratch/alpoge-lean-20261120/decl-names.tsv", encoding="utf-8") as f:
    for line in f:
        kind, name, mod, ln = line.rstrip("\n").split("\t")
        if pat.search(name + "\t" + mod):
            hits += 1
            if hits <= cap:
                print(f"{kind}\t{name}\t{mod}:{ln}")
print(f"-- {hits} declarations match")
