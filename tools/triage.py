#!/usr/bin/env python3
"""Read-only normalized case explorer; never supplies answer keys."""
import csv,argparse
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def collect(root):
    for p in sorted(root.rglob("*.csv")):
        with p.open(encoding="utf-8",newline="") as file:
            for row in csv.DictReader(file):
                yield p.relative_to(ROOT).as_posix(),row
def main():
    a=argparse.ArgumentParser()
    group=a.add_mutually_exclusive_group(required=True)
    group.add_argument("--summary",action="store_true")
    group.add_argument("--timeline",action="store_true")
    group.add_argument("--session")
    group.add_argument("--account")
    group.add_argument("--lab")
    a.add_argument("--limit",type=int,default=70)
    v=a.parse_args()
    assert v.limit>0,"--limit must be positive"
    source=ROOT/"evidence"
    if v.lab:
        options=sorted((ROOT/"PRACTICAL_LABS").glob(v.lab+"*/events.csv"))
        if len(options)!=1:a.error("Specify lab number 01 to 10")
        source=options[0].parent
    rows=list(collect(source))
    if v.summary:
        from collections import Counter
        for p,n in sorted(Counter(p for p,_ in rows).items()):print(f"{n:3} records | {p}")
        print("All content is simulated, not native security telemetry.")
        return
    if v.session:rows=[x for x in rows if x[1].get("session_id")==v.session]
    if v.account:rows=[x for x in rows if v.account.lower() in " ".join(x[1].values()).lower()]
    if v.timeline:rows.sort(key=lambda x:(x[1]["timestamp_utc"],x[0]))
    for path,row in rows[:v.limit]:
        ident=row.get("event_id",row.get("record_id","unknown"))
        detail=row.get("result",row.get("status",row.get("requested_action","")))
        print(f'{row["timestamp_utc"]} | {path} | {ident} | {detail}')
    print(f"Displayed {min(len(rows),v.limit)}/{len(rows)} matching records.")
if __name__=="__main__":main()
