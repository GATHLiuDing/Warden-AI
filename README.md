# Warden-AI 🛡️

## 📌 Executive Summary
As Autonomous AI Agents (CrewAI, AutoGen, etc.) are given access to terminal commands to complete tasks, the risk of **Agentic RCE (Remote Code Execution)** via indirect prompt injection is massive. Warden-AI is a lightweight, zero-trust middleware that hooks into Python's native execution libraries to intercept, analyze, and block malicious commands before the AI can run them on the host system.

## 🛠️ Tech Stack & Architecture
* **Language:** Python 3.x (Standard Library Only - Zero Dependencies)
* **Methodology:** Native `subprocess` and `os.system` function hooking.
* **Cost:** $0 (No external API calls, 100% local heuristic evaluation).

## 🚀 Development Roadmap
* [ ] **Phase 1:** Build the interception hook for `subprocess.run()`.
* [ ] **Phase 2:** Develop the local heuristic rule-engine (blocking `curl`, `wget`, reverse shells).
* [ ] **Phase 3:** Implement the custom `AgentHijackException` circuit breaker.
* [ ] **Phase 4:** Generate clean SOC audit logs for blocked commands.
