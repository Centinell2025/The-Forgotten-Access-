# CENTINELL — The Forgotten Access

**A fictional defensive DFIR/SOC Sherlock — target difficulty Easy**

Publisher: **Beacon of the Eagle LLC / Centinell Suite Defense**.
Victim organization in this simulated story: **Northbridge Systems Ltd.**

## Investigation
A former contractor's identity was not disabled on schedule. An unexpected remote login appears while a legitimate IT employee is performing approved maintenance. Correlate HR, directory, VPN, file-share, proxy and SOC evidence to distinguish an expired account from benign background activity and establish what was blocked versus successfully accessed.

### HTB student deliverable
**[Download Sherlock ZIP](downloads/CENTINELL-The-Forgotten-Access-SHERLOCK-STUDENT.zip)** — password: **`hackthebox`** (traditional ZIP encryption for training distribution, not confidential storage).

- [Main case brief](docs/CASE_BRIEF.md)
- [10 graded investigation questions](docs/INVESTIGATION_QUESTIONS.md)
- [Student guide with Kali Linux / Python workflow](docs/STUDENT_GUIDE.md)
- [Blank analyst worksheet](docs/REPORT_TEMPLATE.md)
- [10 optional industry-style practical investigations](PRACTICAL_LABS/README.md) — 30 additional practice questions.
- [Safety, provenance and limitations](docs/SAFETY_AND_SCOPE.md)

### Offline tests
```bash
python3 tools/verify_student.py
python3 tools/triage.py --summary
python3 tools/triage.py --timeline --limit 10
python3 tools/triage.py --session VPN-900
python3 tools/checksums.py
```
The 10 graded questions are separate from the 10 ungraded exercises. **No answer key or instructor write-up is publicly distributed.**

### Submitter checklist
- [x] Student-safe incident and decoy records; exact record IDs
- [x] 10 main investigation questions, 10 additional exercises, offline analysis and validators
- [x] Encrypted student ZIP with password `hackthebox`
- [ ] Independent full blind solve and HTB difficulty assessment
- [ ] Private instructor walkthrough with actual analyst screenshots
- [ ] HTB acceptance (not yet submitted/confirmed)

Contact publisher: beaconoftheeagle@centinellsuitedefence.com
