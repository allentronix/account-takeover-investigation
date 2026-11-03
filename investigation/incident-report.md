# Incident Report: PHISH/ATO-001

## 1. Incident Overview

- Incident ID: ATO-001
- Incident Type: Suspected Account Takeover
- Target Account: j.smith
- Incident Date: 2026-10-28
- Severity: High
- Status: Investigated (Simulated)

## 2. Executive Summary

Authentication logs revealed suspicious activity targeting the
j.smith account. Five consecutive failed login attempts were
followed by successful authentication from the same IP address.

The source IP was subsequently investigated using AbuseIPDB.
It was identified as a Tor exit node with a 100% abuse
confidence score and 6,994 reported abuse records.

The authentication sequence and external IP reputation indicate
a high likelihood of malicious authentication activity.

Account compromise cannot be definitively confirmed from the
available logs alone.

## 3. Timeline

| Timestamp (UTC) | Event |
|-----------------|-------|
| 08:15:10 | First failed login |
| 08:15:42 | Second failed login |
| 08:16:01 | Third failed login |
| 08:16:33 | Fourth failed login |
| 08:17:02 | Fifth failed login |
| 08:17:30 | Successful login |
| 08:18:05 | MFA failure |
| 08:19:11 | MFA success |
| 08:20:15 | Session created |

## 4. Indicators of Compromise

- Username: j.smith
- Source IP: 185.220.101.45
- Hostname: tor-exit-45.for-privacy.net
- ASN: AS60729
- IP classification: Tor exit node
- Abuse confidence score: 100%
- Abuse reports: 6,994

## 5. Detection Findings

- Five consecutive authentication failures.
- Successful authentication following repeated failures.
- MFA failure followed by successful MFA.
- Session creation from suspicious source IP.
- External IP reputation indicates significant abuse risk.

## 6. MITRE ATT&CK Mapping

- T1110: Brute Force
- T1078: Valid Accounts
- T1090.003: Proxy - Multi-hop Proxy

These mappings represent plausible techniques based on the
observed behavior, not definitive attribution.

## 7. Recommended Response

1. Revoke active sessions and refresh tokens.
2. Reset the affected user's password.
3. Require MFA re-enrollment if compromise is suspected.
4. Review recent account activity and mailbox changes.
5. Investigate other accounts contacted by the source IP.
6. Block the IP where appropriate, considering Tor usage policies.
7. Notify the account owner and document remediation.

## 8. Conclusion

The evidence supports a HIGH-severity suspected account
takeover investigation.

Successful authentication following repeated failures,
MFA challenges, session creation, and suspicious IP reputation
justify immediate containment and further investigation.

The available evidence does not independently prove that
the legitimate account owner was compromised.
