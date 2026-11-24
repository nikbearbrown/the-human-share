import csv, sys, re
src, out = sys.argv[1], sys.argv[2]
rows = list(csv.DictReader(open(src, encoding="utf-8"), delimiter="\t"))
print("columns:", list(rows[0].keys()))
byid = {r["Element ID"]: r for r in rows}
leaf = [r for r in rows if re.fullmatch(r"1\.A\.[1-4]\.[a-z]\.\d+", r["Element ID"])]
print("leaf abilities:", len(leaf))
def name(i): return byid[i]["Element Name"] if i in byid else "not found"
with open(out, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["element_id", "ability", "category", "subcategory", "onet_description"])
    for r in leaf:
        p = r["Element ID"].split(".")
        w.writerow([r["Element ID"], r["Element Name"], name(".".join(p[:3])), name(".".join(p[:4])), r["Description"]])
from collections import Counter
print(Counter(name(".".join(r["Element ID"].split(".")[:3])) for r in leaf))
