from collections import defaultdict
from datetime import timedelta

def detect_threats(logs, fail_threshold=5, time_window_minutes=5):
    ip_attempts = defaultdict(list)
    
    for log in logs:
        if log["status"] == "FAILED":
            ip_attempts[log["ip"]].append(log["timestamp"])
    
    threats = []
    
    for ip, times in ip_attempts.items():
        times.sort()
        # Sliding window to check attempts in time window
        for i in range(len(times)):
            window_start = times[i]
            count = 1
            for j in range(i+1, len(times)):
                if times[j] - window_start <= timedelta(minutes=time_window_minutes):
                    count += 1
                else:
                    break
            if count >= fail_threshold:
                threats.append({
                    "ip": ip,
                    "failed_attempts": count,
                    "time_window": f"{time_window_minutes} minutes",
                    "first_attempt": times[i],
                    "last_attempt": times[i+count-1]
                })
                break  # report only once per IP
    
    return threats