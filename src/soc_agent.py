from log_parser import parse_auth_log
from ai_analyzer import analyze_summary
from report_generator import save_reports


def main():
    print("=" * 60)
    print(" AI Powered SOC Analyst Agent ")
    print("=" * 60)

    print("\n[1] Parsing authentication logs...")
    summary = parse_auth_log()

    print(summary)

    print("\n[2] Sending summary to Local AI...")

    result = analyze_summary(summary)

    print("\n[3] AI Analysis Complete!\n")

    print(result)

    print("\n[4] Saving Incident Report...")

    json_report, txt_report = save_reports(result)

    print(f"\nJSON Report : {json_report}")
    print(f"TEXT Report : {txt_report}")

    print("\nProject Completed Successfully!")


if __name__ == "__main__":
    main()
