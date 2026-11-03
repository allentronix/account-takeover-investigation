# Account Takeover Detection Rules

I wrote these three rules based on the t.walker incident. Each one
groups events by username and source IP.

## Rule 1: Multiple Failed Logins

- Triggers on: 5 or more failed logins
- Severity: Medium
- Why: Could be someone brute-forcing the password

## Rule 2: Successful Login After Failures

- Triggers on: A successful login after 5 or more failures
- Severity: High
- Why: The attacker may have found the right password

## Rule 3: MFA Failure Then Success

- Triggers on: A failed MFA attempt followed by a successful one
- Severity: Medium
- Why: Could mean someone without the real MFA device got through

## Notes

An alert from these rules doesn't mean the account was
compromised. A real user who mistyped their password can trigger
them too, so an analyst still needs to check each alert.
