# Engineering repository access audit

**Scenario:** Dummy design repository; all accounts are fictional Northbridge Systems entities. **Case reference:** `ENG-REPO`. **Analyst classification hypothesis:** offboarding exception under review.

## Investigation objective
Differentiate logged success from denied actions and decide whether continued access conflicts with the case's stated validity period. The source is deliberately a compact **synthetic CSV**, not a live SIEM export.

## Investigative questions
1. At `08:48:17Z`, which account generated the remote login and was the result a success or failure? Cite record ID.
2. Did the suspect account successfully read a **restricted file**? Cite the event ID and the result value without guessing.
3. What action or validation occurred at `09:15:00Z`, and is there enough evidence in these ten records to identify the human actor? Explain.

## Kali Linux / offline exercise
```bash
python3 tools/triage.py --lab 07
```

### Report quality check
Include **two record IDs**, the UTC date, a benign comparator and one evidence limitation. Do not call a blocked connection or denied file read successful. These 3 questions are not graded in the main Sherlock.
