import json
from datetime import datetime
from pathlib import Path

REPORT_FOLDER = Path("reports")
REPORT_FOLDER.mkdir(exist_ok=True)


def save_reports(result):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    json_file = REPORT_FOLDER / f"incident_{timestamp}.json"
    txt_file = REPORT_FOLDER / f"incident_{timestamp}.txt"

    # Save JSON
    with open(json_file, "w") as f:
        json.dump(result, f, indent=4)

    # Save Text Report
    with open(txt_file, "w") as f:
        f.write("========== AI SOC INCIDENT REPORT ==========\n\n")

        f.write(f"Threat Type : {result.get('threat_type')}\n")
        f.write(f"Severity    : {result.get('severity')}\n")
        f.write(f"MITRE       : {result.get('mitre_attack')}\n")
        f.write(f"Confidence  : {result.get('confidence')}\n\n")

        f.write("Reason\n")
        f.write("-----------------------------------------\n")
        f.write(result.get("reason", "") + "\n\n")

        f.write("Recommended Actions\n")
        f.write("-----------------------------------------\n")

        for action in result.get("recommended_actions", []):
            f.write(f"- {action}\n")

    return json_file, txt_file
