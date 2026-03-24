# Warden-AI 🛡️

## 📌 Executive Summary
As Autonomous AI Agents (CrewAI, AutoGen, etc.) are given access to terminal commands to complete tasks, the risk of **Agentic RCE (Remote Code Execution)** via indirect prompt injection is massive. Warden-AI is a lightweight, zero-trust middleware that hooks into Python's native execution libraries to intercept, analyze, and block malicious commands before the AI can run them on the host system.

## 💥 What I want to say here
This is a Cyber Security project that I work on long time ago, if any developer want to use this as an idea on building their own AI chatbot with backend access, feel free to go on.
For your information, this is a very lightweight but effective version of blocking RCE using Chatbot, with only using Python integrated stuff so you wouldn't need to install any requirement, and no, it didn't call any API, so for the new learner, *maybe..* you could use it as an idea as well? idk, this is just a very simple stuff that anyone could make tbh..

* **Zero Dependencies:** No bloated pip packages required.
* **Decoupled Rules:** The security heuristics (like blocking shell chains) live in a separate JSON file. You can update the threat blocklist without messing with the core execution code.
* **Real-Time SOC Alerts:** If an agent goes rogue, Warden kills the process and instantly fires a forensic JSON audit log directly to your Discord.

## 🔧 How to Use It (Developer Guide) *really?*
### 1. Set up the Config
Clone this repository and open the warden_rules.json file. You will see fields for blocked binaries and blocked shell chains. You will also see a field for a webhook URL. Paste your Discord Webhook URL into that field so you receive live alerts when an attack is intercepted.

### 2. Lock Down Your Agent
Drop the warden.py and warden_rules.json files directly into the root folder of your own AI project.

To activate the firewall, simply open your main AI agent script and add the import statement for warden at the very top of your file (just type: import warden).

That is literally it. Warden automatically hooks into the background libraries. If your AI agent is tricked into doing something malicious like opening a reverse shell or downloading unauthorized binaries, Warden steps in, blocks the execution, crashes the rogue agent, and hits your Discord with the alert.

## 🛠️ Tech Stack & Architecture
* **Language:** Python 3.x (Standard Library Only - Zero Dependencies)
* **Methodology:** Native `subprocess` and `os.system` function hooking.
* **Cost:** $0 (No external API calls, 100% local heuristic evaluation).

## 🚀 Development Roadmap
* [x] **Phase 1:** Build the interception hook for `subprocess.run()`.
* [x] **Phase 2:** Develop the local heuristic rule-engine (blocking `curl`, `wget`, reverse shells).
* [x] **Phase 3:** Implement the custom `AgentHijackException` circuit breaker.
* [x] **Phase 4:** Generate clean SOC audit logs for blocked commands.
* [x] **Phase 5:** Decouple security heuristics into a JSON config and add DevSecOps webhook support.
