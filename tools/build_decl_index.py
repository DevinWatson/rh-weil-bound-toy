"""Write a name index of every declaration in the archive: kind, name as written, module, line.

Output: E:/claude-scratch/alpoge-lean-20261120/decl-names.tsv (read-only use; search it with declgrep.py).
"""
import multiprocessing as mp
import re
import sys

sys.path.insert(0, "<workspace>/remark-review-20261120")
import tarstore  # noqa: E402

DECL = re.compile(r"^[ \t]*(?:@\[[^\]]*\][ \t\n]*)?(?:(?:private|protected|noncomputable|nonrec|scoped|local)[ \t]+)*(theorem|lemma|def|abbrev|structure|class|inductive|instance)[ \t]+([^\s:(\[{]+)", re.M)
_store = None


def work(chunk):
    global _store
    if _store is None:
        _store = tarstore.Store()
    rows = []
    for name in chunk:
        text = _store.read(name).decode("utf-8", errors="replace")
        mod = name[len("lean/src/"):-len(".lean")].replace("/", ".")
        for m in DECL.finditer(text):
            rows.append(f"{m.group(1)}\t{m.group(2)}\t{mod}\t{text.count(chr(10), 0, m.start()) + 1}\n")
    return rows


def main():
    st = tarstore.Store()
    names = sorted(n for n in st.names() if n.endswith(".lean"))
    chunks = [names[i:i + 400] for i in range(0, len(names), 400)]
    n = 0
    with mp.Pool(6) as pool, open(tarstore.ROOT + "/decl-names.tsv", "w", encoding="utf-8", newline="\n") as out:
        for rows in pool.imap(work, chunks, chunksize=1):
            out.writelines(rows)
            n += len(rows)
    print("declarations indexed:", n)


if __name__ == "__main__":
    main()
