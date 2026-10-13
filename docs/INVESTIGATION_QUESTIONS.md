# Investigation Questions — Easy (10 scored answers)

**Case:** NB-IR-118, fictional Northbridge Systems Ltd.
**Rules:** Use exact strings, UTC timestamps, record IDs and evidence filenames. The data is entirely simulated.

1. Which contractor account was scheduled for deactivation, and at what exact UTC time did its access authorization end?
2. Which offboarding ticket was not applied successfully, and what directory-audit event ID shows the failed disable attempt?
3. What is the first **successful remote VPN authentication** for the expired contractor? Give its event ID and UTC timestamp.
4. Identify the VPN session ID and remote device associated with that successful authentication.
5. Which file server and full filename were accessed in the **first successful** share read in the suspect VPN session?
6. Name the second distinct file successfully read through that session and give its file event ID.
7. Which external domain received a blocked POST attempt from that session, and what was the recorded outbound byte count?
8. Which employee's VPN login is independently explained by an approved change request? Give the employee account and ticket number.
9. What SOC alert first formally classified the expired-account activity as an incident, and when was it opened (UTC)?
10. What directory event proves the account was **disabled**, and what later authentication event confirms the disable took effect?

**Important:** A successful login identifies account activity, not the person controlling it. A denied share read is not a successful read; a blocked POST does not establish data theft. Accepted response variants must be checked during instructor review.
