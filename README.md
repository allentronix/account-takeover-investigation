# Account Takeover Investigation

A practice SOC investigation I built for my portfolio. I wrote a
Python script to go through a set of auth logs, looked up the
suspicious IP on AbuseIPDB, and wrote up an incident report. The
logs are simulated.

## Scenario

An employee account (t.walker) had several failed logins in a row,
then a successful login and a passed MFA check, all from the same
suspicious IP.

## Tools

- Python
- CSV auth logs
- AbuseIPDB
- Git / GitHub
- MITRE ATT&CK

## How I Investigated It

1. Went through the auth logs.
2. Looked for repeated failed logins.
3. Looked for successful logins after those failures.
4. Looked for MFA failures followed by a success.
5. Checked the source IP's reputation.
6. Put the evidence together.
7. Wrote up the findings and what to do next.

## Running the Script

From the root of the repo:

```
python3 detections/analyze_auth.py
```

It prints failed login counts for each username and IP, plus an
alert for any successful login after 5 or more failures and any
MFA success after a failure.

## What I Found

- Five failed logins on t.walker.
- A successful login right after the failures.
- An MFA failure followed by a success.
- A session created from the suspicious IP.
- The IP is a Tor exit node with a 100% abuse confidence score on
  AbuseIPDB.

## Detection Rules

- Multiple failed logins
- Successful login after repeated failures
- MFA failure followed by success

Details are in
[detection-rules.md](detections/detection-rules.md).

## Assessment

I rated this High severity because the activity looks like an
account takeover. It's still suspected, not confirmed. The full
reasoning is in the
[incident report](investigation/incident-report.md).

## MITRE ATT&CK

- T1110 - Brute Force
- T1078 - Valid Accounts
- T1090.003 - Multi-hop Proxy

## Repo Structure

```
account-takeover-investigation/
├── detections/      detection rules and analysis script
├── evidence/        auth logs
├── investigation/   incident report
└── README.md
```
