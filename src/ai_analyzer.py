import json
import requests
from config import OLLAMA_URL, MODEL


def analyze_summary(summary):

    prompt = f"""
You are a SOC Analyst.

Analyze the following security summary.

Security Summary:

Failed Logins: {summary['failed_logins']}

Successful Logins: {summary['successful_logins']}

Root Attempts: {summary['root_attempts']}

Source IPs:
{summary['source_ips']}

Events:
{summary['events']}

Respond ONLY in valid JSON.

Example:

{{
 "threat_type":"",
 "severity":"",
 "mitre_attack":"",
 "confidence":"",
 "reason":"",
 "recommended_actions":[]
}}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=300
    )

    return json.loads(response.json()["response"])
