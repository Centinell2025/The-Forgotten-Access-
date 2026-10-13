# Student Guide — Kali Linux / Ubuntu / Windows

1. Review `docs/CASE_BRIEF.md` and `docs/INVESTIGATION_QUESTIONS.md`.
2. Decompress the student archive locally using password `hackthebox` when prompted.
3. Do not attempt to access any domain in the logs. The domain suffix `.test` is reserved for test use.
4. Use `python3 tools/triage.py --summary` to inventory case evidence.
5. Use `python3 tools/triage.py --account jreed.ext` and `python3 tools/triage.py --session VPN-900` to compare identity and session evidence.
6. Use `python3 tools/triage.py --timeline` to review a time-normalized view.
7. Fill in `docs/REPORT_TEMPLATE.md`: each answer needs the exact record ID and source path.
8. Optional labs in `PRACTICAL_LABS/` are **not** HTB-graded questions. Do not confuse these events with the main NB-IR-118 incident.

```bash
python3 tools/verify_student.py
python3 tools/triage.py --summary
python3 tools/triage.py --timeline --limit 25
python3 tools/triage.py --account jreed.ext
python3 tools/triage.py --session VPN-900
python3 tools/checksums.py
```

**Expected discipline:** explain any uncertainty. Prove a blocked upload *attempt* rather than inventing an exfiltrated file. Distinguish the account from an identifiable human operator. There are no live machines or credential-based exploitation steps.
