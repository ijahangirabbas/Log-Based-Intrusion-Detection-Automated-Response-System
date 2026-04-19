from datetime import datetime, timedelta
from collections import defaultdict

def parse_log_file(log_file):
    logs = []
    with open(log_file, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = [p.strip() for p in line.split("|")]
            if len(parts) == 4:
                timestamp_str, ip, user, status = parts
                timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
                logs.append({
                    "timestamp": timestamp,
                    "ip": ip,
                    "user": user,
                    "status": status
                })
    return logs