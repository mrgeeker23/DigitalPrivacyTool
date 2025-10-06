import re
from collections import Counter

def analyze_logs(filename="clipboard_log.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = file.read()

        copied_items = re.findall(r"Copied: (.+)", data)
        ai_responses = re.findall(r"AI Response: (.+)", data)
        timestamps = re.findall(r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]", data)

        print("\n📊 CLIPBOARD LOG ANALYSIS REPORT 📊")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"🔢 Total Entries: {len(copied_items)}")

        sens_count = sum(1 for r in ai_responses if "Sensitive" in r)
        not_sens_count = len(ai_responses) - sens_count
        print(f"🛡️  Sensitive: {sens_count}")
        print(f"✅ Not Sensitive: {not_sens_count}")

        # Local pattern counts
        patterns = {
            "Email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
            "Phone": r"\b\d{10}\b",
            "PAN": r"\b[A-Z]{5}[0-9]{4}[A-Z]\b",
            "Card": r"\b(?:\d[ -]*?){13,16}\b"
        }

        local_counts = Counter()
        for item in copied_items:
            for label, pattern in patterns.items():
                if re.search(pattern, item):
                    local_counts[label] += 1

        print("\n🔍 Local Pattern Detections:")
        for label, count in local_counts.items():
            print(f"   - {label}: {count}")

        if copied_items:
            print("\n🕒 Most Recent Entry:")
            print(f"📋 Copied: {copied_items[-1]}")
            print(f"📅 Time: {timestamps[-1]}")
            print(f"🤖 AI Response: {ai_responses[-1]}")

        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    except FileNotFoundError:
        print("[❌] Log file not found!")
    except Exception as e:
        print(f"[⚠️] Error during analysis: {e}")

if __name__ == "__main__":
    analyze_logs()
