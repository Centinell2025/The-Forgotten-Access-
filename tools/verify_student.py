#!/usr/bin/env python3
"""Validate Easy Sherlock data and encrypted student ZIP with no spoilers."""
from pathlib import Path
import csv,zipfile,re,subprocess,sys
from datetime import datetime
root=Path(__file__).resolve().parents[1]
case=root/"evidence"
sources=sorted(case.rglob("*.csv"))
assert len(sources)==8,len(sources)
ids=set()
for file in sources:
    with file.open(encoding="utf-8",newline="") as f:
        rows=list(csv.DictReader(f))
    assert len(rows)>=3,file
    for r in rows:
        ident=r["event_id"]
        assert ident not in ids,ident
        ids.add(ident)
        assert datetime.fromisoformat(r["timestamp_utc"].replace("Z","+00:00")).utcoffset().total_seconds()==0
        assert not re.search(r"(?<![0-9.])(?:[0-9]{1,3}[.]){3}[0-9]{1,3}(?![0-9.])"," ".join(r.values()))
labs=sorted((root/"PRACTICAL_LABS").glob("*/events.csv"))
assert len(labs)==10
for path in labs:
    with path.open(encoding="utf-8",newline="") as f: rows=list(csv.DictReader(f))
    assert len(rows)==10,path
    assert "## Investigative questions" in (path.parent/"CASE_AND_EXERCISE.md").read_text(encoding="utf-8")
guide=(root/"docs/INVESTIGATION_QUESTIONS.md").read_text(encoding="utf-8")
assert len([line for line in guide.splitlines() if line.startswith(tuple(f"{n}. " for n in range(1,11)))])==10
for argv in (["--summary"],["--timeline","--limit","5"],["--session","VPN-900"],["--lab","01"]):
    p=subprocess.run([sys.executable,str(root/"tools/triage.py"),*argv],capture_output=True,text=True,cwd=root)
    assert p.returncode==0,p.stderr
archive=root/"downloads/CENTINELL-The-Forgotten-Access-SHERLOCK-STUDENT.zip"
assert archive.is_file()
# Student ZIP is password protected but traditional PKZIP is NOT high-security storage.
expected={p.relative_to(root).as_posix():p.read_bytes() for folder in
         ("evidence","docs","PRACTICAL_LABS","tools") for p in (root/folder).rglob("*") if p.is_file()}
expected["README.md"]=(root/"README.md").read_bytes()
with zipfile.ZipFile(archive) as z:
    names=z.namelist()
    assert len(names)==len(set(names))
    assert set(names)==set(expected)
    for info in z.infolist():
        assert info.flag_bits&1,info.filename
        assert z.read(info,pwd=b"hackthebox")==expected[info.filename],info.filename
assert not any(any(s in p.lower() for s in ("instructor","answer_key","solutions","private")) for p in expected)
print(f"PASS: {len(sources)} source families, {len(ids)} main records, 10 lab drills, 100 practice records, 10 main questions, encrypted ZIP {len(expected)} files; 0 instructor answers")
