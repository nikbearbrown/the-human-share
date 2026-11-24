import csv, sys
from collections import Counter
d = sys.argv[1]
FACETS = ["Pattern & Association","Embodied & Sensorimotor","Social & Personal","Metacognitive & Supervisory",
          "Causal & Counterfactual","Collective & Distributed","Existential & Wisdom"]
OK_PRIMARY = set(FACETS) | {"no_fit"}
OK_FIT = {"strong","partial","weak","n/a"}
HDR = ["element_id","ability","primary_facet","secondary_facets","fit","rationale"]
def load(p):
    with open(p, encoding="utf-8", newline="") as f:
        r = csv.reader(f, delimiter="\t")
        hdr = next(r); rows = [x for x in r if x]
    return hdr, rows
_, ab = load(f"{d}/abilities.tsv")
ids = [x[0] for x in ab]; meta = {x[0]: x for x in ab}
runs = {}
problems = []
for name in ["a","b"]:
    hdr, rows = load(f"{d}/run-{name}.tsv")
    if hdr != HDR: problems.append(f"run-{name}: header {hdr}")
    m = {}
    for x in rows:
        if len(x) != 6: problems.append(f"run-{name}: {len(x)} fields in {x[:2]}"); continue
        eid, abil, prim, sec, fit, rat = [v.strip() for v in x]
        if eid in m: problems.append(f"run-{name}: duplicate {eid}")
        if eid not in meta: problems.append(f"run-{name}: unknown id {eid}")
        elif abil != meta[eid][1]: problems.append(f"run-{name}: name mismatch {eid} {abil}")
        if prim not in OK_PRIMARY: problems.append(f"run-{name}: bad primary {eid} {prim!r}")
        secs = [s.strip() for s in sec.split(";") if s.strip()]
        for s in secs:
            if s not in FACETS: problems.append(f"run-{name}: bad secondary {eid} {s!r}")
            if s == prim: problems.append(f"run-{name}: secondary repeats primary {eid}")
        if fit not in OK_FIT: problems.append(f"run-{name}: bad fit {eid} {fit!r}")
        if (prim == "no_fit") != (fit == "n/a"): problems.append(f"run-{name}: fit/no_fit mismatch {eid}")
        m[eid] = dict(primary=prim, secondary=secs, fit=fit, rationale=rat)
    missing = [i for i in ids if i not in m]
    if missing: problems.append(f"run-{name}: missing {missing}")
    runs[name] = m
print("VALIDATION:", "OK" if not problems else "PROBLEMS"); [print("  ", p) for p in problems]
if problems: sys.exit(1)
A, B = runs["a"], runs["b"]
labels = FACETS + ["no_fit"]
ca = Counter(A[i]["primary"] for i in ids); cb = Counter(B[i]["primary"] for i in ids)
print("\nPRIMARY COUNTS (facet | run A | run B)")
for l in labels: print(f"  {l} | {ca[l]} | {cb[l]}")
agree = [i for i in ids if A[i]["primary"] == B[i]["primary"]]
n = len(ids); po = len(agree)/n
pe = sum((ca[l]/n)*(cb[l]/n) for l in labels)
kappa = (po-pe)/(1-pe) if pe < 1 else float("nan")
print(f"\nAGREEMENT on primary: {len(agree)}/{n} = {po:.3f}; Cohen's kappa = {kappa:.3f}")
cats = Counter(meta[i][2] for i in ids)
print("\nAGREEMENT BY O*NET CATEGORY")
for c in cats:
    ii = [i for i in ids if meta[i][2] == c]
    print(f"  {c}: {sum(A[i]['primary']==B[i]['primary'] for i in ii)}/{len(ii)}")
two = {"Pattern & Association","Embodied & Sensorimotor"}
for nm, R, C in [("A",A,ca),("B",B,cb)]:
    print(f"\nRUN {nm}: primary in P&A or E&S = {sum(R[i]['primary'] in two for i in ids)}/52; "
          f"facets with zero primary = {[f for f in FACETS if C[f]==0]}")
    sec = Counter(s for i in ids for s in R[i]["secondary"])
    anyf = Counter(f for i in ids for f in set([R[i]['primary']] + R[i]['secondary']) if f in FACETS)
    print(f"  secondary counts: {dict(sec)}")
    print(f"  facets with zero abilities as primary OR secondary = {[f for f in FACETS if anyf[f]==0]}")
    print(f"  fit counts: {dict(Counter(R[i]['fit'] for i in ids))}")
both_two = sum(A[i]['primary'] in two and B[i]['primary'] in two for i in ids)
print(f"\nBOTH runs put primary in P&A or E&S: {both_two}/52")
print("\nDISAGREEMENTS (id | ability | A | B)")
for i in ids:
    if A[i]["primary"] != B[i]["primary"]:
        print(f"  {i} | {meta[i][1]} | {A[i]['primary']} ({A[i]['fit']}) | {B[i]['primary']} ({B[i]['fit']})")
print("\nAGREED no_fit or weak:")
for i in ids:
    if A[i]["primary"] == B[i]["primary"] and (A[i]["primary"]=="no_fit" or "weak" in (A[i]['fit'],B[i]['fit'])):
        print(f"  {i} | {meta[i][1]} | {A[i]['primary']} | fit A {A[i]['fit']} B {B[i]['fit']}")
with open(f"{d}/comparison.tsv","w",encoding="utf-8",newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["element_id","ability","category","primary_a","primary_b","agree","fit_a","fit_b","secondary_a","secondary_b"])
    for i in ids:
        w.writerow([i, meta[i][1], meta[i][2], A[i]["primary"], B[i]["primary"],
                    "yes" if A[i]["primary"]==B[i]["primary"] else "no", A[i]["fit"], B[i]["fit"],
                    "; ".join(A[i]["secondary"]), "; ".join(B[i]["secondary"])])
print("\nwrote comparison.tsv")
