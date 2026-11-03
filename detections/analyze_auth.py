import csv
from collections import defaultdict

LOG_FILE = "evidence/auth-logs.csv"

failed_logins = defaultdict(int)
successful_after_failures = []
failed_mfa = defaultdict(int)
successful_mfa = []

with open(LOG_FILE, newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        key = (row["username"], row["source_ip"])

        if row["event_type"] == "login":
            if row["status"] == "failure":
                failed_logins[key] += 1

            elif row["status"] == "success":
                if failed_logins[key] >= 5:
                    successful_after_failures.append(
                        (row["username"], row["source_ip"], row["timestamp"])
                    )

        if row["event_type"] == "mfa":
            if row["status"] == "failure":
                failed_mfa[key] += 1

            elif row["status"] == "success":
                if failed_mfa[key] > 0:
                    successful_mfa.append(
                        (row["username"], row["source_ip"], row["timestamp"])
                    )

print("=== FAILED LOGIN SUMMARY ===")
for (username, ip), count in failed_logins.items():
    print(f"{username} | {ip} | {count} failures")

print("\n=== SUCCESSFUL LOGIN AFTER FAILURES ===")
for username, ip, timestamp in successful_after_failures:
    print(f"ALERT: {username} | {ip} | {timestamp}")

print("\n=== MFA FAILURE FOLLOWED BY SUCCESS ===")
for username, ip, timestamp in successful_mfa:
    print(f"ALERT: {username} | {ip} | {timestamp}")
