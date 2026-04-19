from log_generator import generate_logs
from log_analyzer import parse_log_file
from threat_detector import detect_threats
from response_handler import simulate_response, blocked_ips, locked_accounts
import os

def classify_risk(failed_attempts):
    if failed_attempts >= 10:
        return "High"
    elif failed_attempts >= 5:
        return "Medium"
    else:
        return "Low"

def main():
    print("🚀 Starting Log-Based Intrusion Detection & Automated Response System\n")
    
    # 1. Generate simulated logs
    log_file = generate_logs(250)
    
    # 2. Analyze logs
    logs = parse_log_file(log_file)
    print(f"📊 Analyzed {len(logs)} log entries\n")
    
    # 3. Detect threats
    threats = detect_threats(logs, fail_threshold=5, time_window_minutes=5)
    
    # 4. Process threats
    print("🔍 Threat Detection Results:")
    os.makedirs("reports", exist_ok=True)
    
    with open("reports/alerts.txt", "w", encoding="utf-8") as report:
        report.write("LOG-BASED INTRUSION DETECTION REPORT\n")
        report.write("="*60 + "\n\n")
        
        if not threats:
            print("✅ No threats detected.")
            report.write("No suspicious activity detected.\n")
        else:
            for threat in threats:
                risk = classify_risk(threat["failed_attempts"])
                print(f"🚨 ALERT: {risk} Risk from IP {threat['ip']}")
                print(f"   Failed attempts: {threat['failed_attempts']} in {threat['time_window']}")
                
                actions = simulate_response(threat, risk)
                
                # Write to report (safe for Windows)
                report.write(f"ALERT: {risk} Risk\n")
                report.write(f"IP: {threat['ip']}\n")
                report.write(f"Failed Attempts: {threat['failed_attempts']}\n")
                report.write(f"Time Window: {threat['time_window']}\n")
                report.write(f"First Attempt: {threat['first_attempt']}\n")
                report.write(f"Last Attempt: {threat['last_attempt']}\n")
                report.write("Actions Taken:\n")
                for action in actions:
                    # Remove emojis for file writing
                    clean_action = action.replace("🔴", "[BLOCKED]").replace("🟡", "[WATCHLIST]")
                    report.write(f"   - {clean_action}\n")
                report.write("-"*50 + "\n\n")
                
                # Print to console with emojis (this is fine)
                for action in actions:
                    print(f"   → {action}")
                print()
    
    # Final summary
    print("\n📋 Final Status:")
    print(f"   Blocked IPs     : {len(blocked_ips)}")
    print(f"   Locked Accounts : {len(locked_accounts)}")
    print(f"   Full report saved to: reports/alerts.txt")
    
    print("\n✅ Project executed successfully! (Educational simulation)")

if __name__ == "__main__":
    main()