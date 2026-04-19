import random
import datetime
import os

def generate_logs(num_entries=200):
    os.makedirs("logs", exist_ok=True)
    log_file = "logs/security.log"
    
    users = ["admin", "user1", "student", "manager", "test"]
    ips = ["192.168.1.105", "192.168.1.110", "10.0.0.45", "172.16.0.22", "192.168.1.200"]
    attack_ip = "192.168.1.200"  # This IP will do brute-force attack
    
    with open(log_file, "w") as f:
        current_time = datetime.datetime.now() - datetime.timedelta(minutes=30)
        
        for i in range(num_entries):
            current_time += datetime.timedelta(seconds=random.randint(10, 60))
            timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
            
            if i > 120 and random.random() < 0.7:  # Simulate attack in last 80 entries
                ip = attack_ip
                user = "admin"
                status = "FAILED"
            else:
                ip = random.choice(ips)
                user = random.choice(users)
                status = "SUCCESS" if random.random() > 0.6 else "FAILED"
            
            line = f"{timestamp} | {ip} | {user} | {status}\n"
            f.write(line)
    
    print(f"✅ Generated {num_entries} log entries in logs/security.log")
    return log_file