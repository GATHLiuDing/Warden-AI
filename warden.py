import subprocess
import json
import datetime
import os
import re

# 1. Save the original Python function
_original_subprocess_run = subprocess.run

class AgentHijackException(Exception):
    pass

# 2. Ensure our secure audit log directory exists
if not os.path.exists("audit_logs"):
    os.makedirs("audit_logs")

# 3. The Forensic Logger
def log_incident(command, reason):
    incident = {
        "timestamp": datetime.datetime.now().isoformat(),
        "blocked_command": command,
        "reason": reason,
        "severity": "CRITICAL",
        "action_taken": "BLOCKED_AND_CRASHED"
    }
    # Append the incident to our JSON log file
    with open("audit_logs/warden_alerts.json", "a") as f:
        f.write(json.dumps(incident) + "\n")

# 4. The Advanced Interceptor
def secure_subprocess_run(*args, **kwargs):
    print("\n[🛡️ WARDEN] Intercepting execution request...")
    
    command = args[0] if args else kwargs.get('args')
    cmd_str = " ".join(command) if isinstance(command, list) else str(command)
    
    print(f"[🛡️ WARDEN] Analyzing command: {cmd_str}")

    # --- ADVANCED HEURISTIC ENGINE ---
    
    # Rule A: Block dangerous binaries using regex boundaries (Catches /usr/bin/curl)
    dangerous_binaries = r'\b(curl|wget|nc|netcat|bash|sh|zsh|php|nmap)\b'
    if re.search(dangerous_binaries, cmd_str, re.IGNORECASE):
        reason = "Malicious binary detected in command execution."
        print(f"[🚨 WARDEN-ALERT] {reason}")
        log_incident(cmd_str, reason)
        raise AgentHijackException(f"Restricted RCE attempt: {cmd_str}")
        
    # Rule B: Flag dangerous Shell chaining (Pipes and Redirects)
    # Attackers use things like `echo "bad" > file.txt` or `command1 | command2`
    if kwargs.get('shell') == True:
        if any(char in cmd_str for char in ['|', '>', '<', '&', ';']):
            reason = "Shell chaining/redirection detected (Possible Command Injection)."
            print(f"[🚨 WARDEN-ALERT] {reason}")
            log_incident(cmd_str, reason)
            raise AgentHijackException(reason)

    print("[✅ WARDEN] Command verified safe. Passing to OS...")
    return _original_subprocess_run(*args, **kwargs)

# 5. Inject the Middleware
subprocess.run = secure_subprocess_run
print("[SYSTEM] Warden-AI Advanced Middleware Successfully Injected.")