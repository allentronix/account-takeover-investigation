# Account Takeover Detection Rules

## Rule 1: Multiple Failed Login Attempts

- Detection: 5 or more failed login attempts
- Grouping: Username + source IP
- Severity: Medium
- Purpose: Identify possible brute-force activity

## Rule 2: Successful Login After Repeated Failures

- Detection: Successful login following 5 or more failures
- Grouping: Username + source IP
- Severity: High
- Purpose: Identify possible credential compromise

## Rule 3: MFA Failure Followed by Success

- Detection: Failed MFA followed by successful MFA
- Grouping: Username + source IP
- Severity: Medium
- Purpose: Identify suspicious authentication sequences

## Investigation Notes

These rules generate alerts for suspicious authentication activity.
Alerts require analyst validation before confirming account compromise.
