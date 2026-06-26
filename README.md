# 🛡️ AI-Powered SOC Analyst Agent

An AI-powered Security Operations Center (SOC) Analyst built with Python and Ollama (Llama 3.2) that analyzes Linux authentication logs, identifies suspicious activities, classifies threats, maps them to the MITRE ATT&CK framework, and automatically generates incident reports.

---

## 📖 Overview

Modern Security Operations Centers (SOCs) process thousands of security events every day. Manual log analysis is time-consuming and can delay incident response.

This project automates part of the SOC workflow by combining traditional log parsing with a local Large Language Model (LLM). It reads Linux authentication logs, summarizes security events, performs AI-assisted threat analysis, and generates structured incident reports.

---

## ✨ Features

* Analyze Linux authentication logs (`auth.log`)
* Detect suspicious login activity
* AI-assisted threat classification using Llama 3.2
* Severity assessment
* MITRE ATT&CK mapping
* Automated incident report generation
* JSON and text report output
* Modular Python architecture
* Runs entirely with a local LLM (no cloud API required)

---

## 🏗️ Architecture

```text
Linux Authentication Logs
           │
           ▼
     Log Parser (Python)
           │
           ▼
     Event Summarization
           │
           ▼
 AI Analyzer (Llama 3.2 via Ollama)
           │
           ▼
Threat Classification & MITRE Mapping
           │
           ▼
 Incident Report Generator
           │
           ▼
 JSON Report + Text Report
```

---

## 📂 Project Structure

```text
AI-Powered-SOC-Analyst-Agent/

├── playbook/
├── reports/
├── Screenshots/
├── src/
│   ├── ai_analyzer.py
│   ├── config.py
│   ├── log_parser.py
│   ├── report_generator.py
│   └── soc_agent.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚙️ Technologies Used

* Python
* Linux
* Ollama
* Llama 3.2
* JSON
* MITRE ATT&CK Framework
* Git
* GitHub

---

## 🚀 Installation

```bash
git clone https://github.com/nisargant/AI-Powered-SOC-Analyst-Agent.git

cd AI-Powered-SOC-Analyst-Agent

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python src/soc_agent.py
```

---

## 📄 Sample Output

The AI agent:

* Reads Linux authentication logs
* Parses security events
* Sends summarized events to a local LLM
* Generates AI-assisted threat analysis
* Creates JSON and text incident reports

---

## 🧠 MITRE ATT&CK

Example mappings include:

* Credential Access
* Brute Force
* Valid Accounts
* Privilege Escalation

---

## 📸 Screenshots

Project screenshots are available in the **Screenshots** folder.

---

## 🔮 Future Improvements

* Real-time log monitoring
* SSH brute-force detection
* Multiple log source support
* Web dashboard
* Email alerts
* Wazuh integration
* Splunk integration

---

## 👨‍💻 Author

**Nisarga N T**

Aspiring SOC Analyst | SIEM | Threat Detection | Incident Response
