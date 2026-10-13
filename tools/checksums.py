#!/usr/bin/env python3
"""Print SHA-256 of all distributed training evidence files."""
import hashlib
from pathlib import Path
root=Path(__file__).resolve().parents[1]
for folder in ("evidence","PRACTICAL_LABS"):
    for path in sorted((root/folder).rglob("*.csv")):
        print(hashlib.sha256(path.read_bytes()).hexdigest()+"  "+path.relative_to(root).as_posix())
