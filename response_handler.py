blocked_ips = set()
locked_accounts = set()

def simulate_response(threat, risk_level):
    ip = threat["ip"]
    user = "admin"   # You can improve this later
    
    actions = []
    
    if risk_level == "High":
        blocked_ips.add(ip)
        actions.append(f"🔴 IP {ip} has been BLOCKED")
        if user not in locked_accounts:
            locked_accounts.add(user)
            actions.append(f"🔴 Account '{user}' has been LOCKED")
    
    elif risk_level == "Medium":
        actions.append(f"🟡 IP {ip} has been added to WATCHLIST")
    
    return actions