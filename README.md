# 🛡️ AI-Powered SOC Analyst Agent

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![Linux](https://img.shields.io/badge/Platform-Linux-black?style=for-the-badge\&logo=linux)
![Ollama](https://img.shields.io/badge/LLM-Ollama-green?style=for-the-badge)
![Llama 3.2](https://img.shields.io/badge/Model-Llama%203.2-purple?style=for-the-badge)
![MITRE ATT\&CK](https://img.shields.io/badge/MITRE-ATT%26CK-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

An AI-powered Security Operations Center (SOC) Analyst built with **Python** and **Ollama (Llama 3.2)** that analyzes Linux authentication logs, detects suspicious activities, maps threats to the **MITRE ATT&CK** framework, and automatically generates structured incident reports.

---

# 📖 Overview

Modern Security Operations Centers (SOCs) analyze thousands of authentication events every day. Manual investigation is time-consuming and increases incident response time.

This project automates SOC log analysis by combining Python-based log parsing with a locally hosted Large Language Model (LLM). The system summarizes Linux authentication logs, performs AI-assisted threat analysis, maps attacks to the MITRE ATT&CK framework, and generates structured incident reports.

---

# ✨ Features

* Analyze Linux authentication logs (`auth.log`)
* Detect suspicious authentication activity
* AI-powered threat analysis using **Llama 3.2**
* Threat severity assessment
* MITRE ATT&CK technique mapping
* Automated JSON and text incident reports
* Modular Python architecture
* Runs completely offline using a local LLM (Ollama)

---

# 🏗️ Architecture

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
Threat Classification & MITRE ATT&CK Mapping
           │
           ▼
 Incident Report Generator
           │
           ▼
 JSON Report + Text Report
```

---

# 📂 Project Structure

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

# ⚙️ Technologies Used

* Python
* Linux
* Ollama
* Llama 3.2
* JSON
* MITRE ATT&CK Framework
* Git
* GitHub

---

# 🚀 Installation

```bash
git clone https://github.com/nisargant/AI-Powered-SOC-Analyst-Agent.git

cd AI-Powered-SOC-Analyst-Agent

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

---

# ▶️ Run the Project

```bash
python src/soc_agent.py
```

---

# 📄 Sample Output

The AI agent performs the following workflow:

* Reads Linux authentication logs
* Parses authentication events
* Summarizes suspicious activities
* Sends the summary to a local LLM (Llama 3.2)
* Classifies threats
* Maps attacks to MITRE ATT&CK techniques
* Generates JSON and text incident reports

---

# 🧠 MITRE ATT&CK Mapping

Example ATT&CK techniques detected by this project:

| Technique            | ID     |
| -------------------- | ------ |
| Brute Force          | T1110  |
| Valid Accounts       | T1078  |
| Credential Access    | TA0006 |
| Privilege Escalation | TA0004 |

Official MITRE ATT&CK Matrix:

https://attack.mitre.org/matrices/enterprise/

---

# 📸 Screenshots

## Project Setup

![Ollama Installation](Screenshots/01_ollama_installation.png)

![Llama 3.2 Download](Screenshots/02_llama3_model_download.png)

---

## Project Development

![Project Structure](Screenshots/03_project_directory_structure.png)

![SOC Playbook](Screenshots/04_soc_playbook_creation.png)

![Llama Testing](Screenshots/05_llama3_model_testing.png)

![Python Environment](Screenshots/06_python_virtual_environment.png)

---

## Source Code

![AI Analyzer](Screenshots/07_ai_analyzer_module_code.png)

![Configuration](Screenshots/08_project_configuration_file.png)

![Log Parser](Screenshots/09_log_parser_module_code.png)

![Report Generator](Screenshots/10_report_generator_module_code.png)

![Final AI Analyzer](Screenshots/11_final_ai_analyzer_code.png)

![SOC Agent](Screenshots/12_soc_agent_main_program.png)

---

## Testing

![Log Parser Test](Screenshots/13_log_parser_test_success.png)

---

# 🔮 Future Improvements

* Real-time log monitoring
* SSH brute-force detection
* Support for multiple Linux log sources
* Interactive web dashboard
* Email alerting
* Wazuh integration
* Splunk integration

---

# 👨‍💻 Author

**Nisarga N T**

Aspiring SOC Analyst | SIEM | Threat Detection | Incident Response

**GitHub:** https://github.com/nisargant

**LinkedIn:** https://linkedin.com/in/nisarga-n-t

---

# 📄 License

This project is licensed under the MIT License.
