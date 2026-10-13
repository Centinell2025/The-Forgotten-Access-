# Case brief — CENTINELL: The Forgotten Access

**Case:** NB-IR-118 | **Difficulty target:** Easy | **Evidence date:** 2026-09-23 UTC
**Company:** Northbridge Systems Ltd. (entirely invented).

HR reports that contractor onboarding and offboarding statuses are not always synchronized. A former contractor's network account was accepted by the corporate VPN after the contract end date. The SOC has several overlapping events from an authorized infrastructure employee, another active contractor, an access-control rule on a file share and a proxy policy block.

You are a newly assigned DFIR/SOC analyst. Determine the timeline, the affected credentials, the records supporting access to dummy resources, how much can actually be inferred about attempted outbound traffic, and which action ended the access.

**Objective:** produce exact answers to ten graded questions using the supplied CSV evidence. You do not need any malware, active domains, real IP addresses or commercial forensic tools. All data and persons are fictional.

**Source map:**
- 01_hr/offboarding.csv — employment status and offboarding requests
- 02_directory/audit.csv — actual identity-state changes
- 03_auth/signins.csv — successful and failed authentication
- 04_vpn/sessions.csv — session/device joins
- 05_files/share_activity.csv — permitted vs denied file events
- 06_proxy/web_egress.csv — blocked vs allowed network requests
- 07_alerts/soc.csv — analyst alert milestones
- 08_change/approvals.csv — benign comparator and authorization

**Limitations:** CSV files are synthetic normalized training exhibits, not native Windows EVTX, Sysmon records, real SIEM exports, packet captures, or evidence of an identifiable attacker. They must not be described as independent native captures.
