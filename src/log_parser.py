import re
from pathlib import Path

LOG_FILE = "/var/log/auth.log"


def parse_auth_log(lines=100):
    """
    Parse the last 'lines' lines from auth.log and summarize SSH activity.
    """

    log_path = Path(LOG_FILE)

    if not log_path.exists():
        return {
            "failed_logins": 0,
            "successful_logins": 0,
            "root_attempts": 0,
            "source_ips": [],
            "events": []
        }

    with log_path.open("r") as file:
        logs = file.readlines()[-lines:]

    failed = 0
    success = 0
    root = 0

    ips = set()
    events = []

    ip_regex = r"(\d+\.\d+\.\d+\.\d+)"

    for line in logs:

        if "Failed password" in line:
            failed += 1
            events.append(line.strip())

        if "Accepted password" in line:
            success += 1
            events.append(line.strip())

        if "root" in line:
            root += 1

        match = re.search(ip_regex, line)

        if match:
            ips.add(match.group())

    return {
        "failed_logins": failed,
        "successful_logins": success,
        "root_attempts": root,
        "source_ips": list(ips),
        "events": events[:10]
    }
