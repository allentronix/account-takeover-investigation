# Incident Report: PHISH/ATO-001

## Overview

- Incident ID: ATO-001
- Type: Suspected account takeover
- Account: t.walker
- Date: 2026-10-28
- Severity: High
- Status: Investigated (simulated)

## Summary

The auth logs show five failed logins on t.walker in under two
minutes, then a successful login from the same IP. MFA failed
once, passed on the second try, and a session was created.

I looked up the IP on AbuseIPDB. It's a Tor exit node with a 100%
abuse confidence score and 6,994 reports.

t.walker normally logs in from 192.168.1.25 in London, including
at 08:00 that morning and again at 09:05, so this doesn't look
like their usual activity. I can't confirm the account was
compromised from these logs alone, but I'd treat it as likely.

## Timeline

| Time (UTC) | Event |
|------------|-------|
| 08:15:10 | Failed login 1 |
| 08:15:42 | Failed login 2 |
| 08:16:01 | Failed login 3 |
| 08:16:33 | Failed login 4 |
| 08:17:02 | Failed login 5 |
| 08:17:30 | Successful login |
| 08:18:05 | MFA failed |
| 08:19:11 | MFA passed |
| 08:20:15 | Session created |

## Indicators

- Username: t.walker
- Source IP: 185.220.101.45
- Hostname: tor-exit-45.for-privacy.net
- ASN: AS60729
- IP type: Tor exit node
- Abuse confidence score: 100%
- Abuse reports: 6,994

## Findings

- Five failed logins in a row from one IP.
- A successful login right after those failures, which suggests
  the attacker ended up with the right password.
- An MFA failure followed by an MFA pass. The logs don't show how
  MFA was passed.
- A session created from the Tor IP.
- No other events from this IP after the session was created, so
  I can't tell what was done with the session, if anything.

## MITRE ATT&CK Mapping

- T1110: Brute Force
- T1078: Valid Accounts
- T1090.003: Proxy: Multi-hop Proxy

These are my best fit for what the logs show. They aren't proof
of how the attacker actually got in.

## Recommended Response

1. Revoke active sessions and refresh tokens.
2. Reset t.walker's password.
3. Have the user re-enroll MFA if compromise is suspected.
4. Check recent account activity and mailbox changes.
5. Check whether the IP tried any other accounts.
6. Block the IP if that fits our Tor policy.
7. Tell the account owner and write down what was done.

## Conclusion

I rated this High. A successful login after repeated failures,
plus the MFA activity, the session, and the IP's reputation, is
enough to contain the account now and keep investigating.

This doesn't prove the account was compromised, though. Talking
to t.walker and checking what happened after 08:20 would help
settle that.
