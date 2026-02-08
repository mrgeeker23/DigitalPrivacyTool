DigitalPrivacy Tool: Real-Time Clipboard Security Monitor
Clipboard-based data leakage represents an overlooked attack vector in enterprise security environments. Employees in SOC teams, financial institutions, and customer service organizations routinely copy sensitive information—passwords, OTPs, customer IDs, payment card numbers—into their system clipboard, where this data remains temporarily accessible, often unencrypted and unmonitored. A single accidental paste into an unsecured channel (Slack, email, browser) can trigger credential compromise, identity theft, or compliance violations.

Technical Implementation:
DigitalPrivacy Tool is a lightweight Python-based clipboard monitoring system that provides real-time detection of sensitive data through a hybrid classification approach. I built the core engine using pyperclip for continuous clipboard polling, implementing regex pattern matching for immediate identification of structured data types including email addresses (RFC 5322 compliant), Indian PAN numbers, payment card sequences (13-16 digits), and phone numbers. For unstructured or ambiguous content that evades regex detection, the system integrates local AI inference via Ollama's Mistral model, which performs contextual analysis to identify passwords, API keys, and other credential patterns without external data transmission.
The architecture maintains privacy-by-design principles: all processing occurs locally with zero cloud dependencies, ensuring sensitive clipboard content never leaves the user's device. When potentially risky data is detected, the system triggers threaded Tkinter popup alerts for immediate user notification while logging all clipboard activity with ISO 8601 timestamps to clipboard_log.txt for post-incident forensic analysis.

Key Technical Components:
Multi-pattern regex engine covering PAN (Indian tax ID), payment cards (Luhn algorithm validation capable), email (RFC-compliant), and phone number formats
Local LLM integration (Mistral 7B) via Ollama API for zero-latency, privacy-preserving inference
Asynchronous alert system using Python threading to prevent UI blocking during active monitoring
Companion log analysis tool (analyze_logs.py) providing statistical reporting on clipboard usage patterns, sensitive data frequency, and temporal analysis

Enterprise Security Applications:
This tool addresses clipboard security gaps in high-risk operational environments including Security Operations Centers (SOC), banking terminals, healthcare administration systems, and customer support desks where PII exposure through copy-paste workflows creates compliance risks under regulations including GDPR Article 32 (security of processing), PCI DSS Requirement 3 (cardholder data protection), and India's DPDP Act 2023. The solution enables organizations to implement clipboard-level Data Loss Prevention (DLP) controls without deploying enterprise-grade endpoint security suites.
Impact & Validation:
By operating entirely offline with local AI inference, the tool demonstrates feasibility of privacy-preserving security monitoring suitable for air-gapped environments and zero-trust architectures. The hybrid detection methodology (regex + LLM) achieves coverage of both structured and unstructured sensitive data patterns while maintaining sub-second response times for real-time user alerts, preventing accidental data exposure before it propagates to external systems.

---

## 📌 Features

- ✅ **Clipboard Monitoring** in real-time
- 🧠 **AI-based classification** for sensitive vs non-sensitive content
- 🔍 **Regex scanning** for known patterns (Email, Phone, PAN, Card)
- 📊 **Log analyzer** script for quick audit reports
- 🔔 **Pop-up alerts** when sensitive data is detected
- 📝 **Automatic logging** with timestamps
- ⚙️ **Zero-setup** — just run and monitor

---

## 📂 Project Structure

DigitalPrivacyTOOOL/
├── clipboard_checker.py # Main monitoring script
├── analyze_logs.py # Log analyzer for summary reports
├── clipboard_log.txt # (Optional) Saved analysis logs
├── screenshots/ # (Optional) GUI popup screenshots
├── requirements.txt # Dependencies
├── .gitignore # Files/folders to exclude
└── README.md # Project documentation


---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/mrgeeker23/DigitalPrivacyTOOOL.git
cd DigitalPrivacyTOOOL


2. Install Required Libraries

pip install pyperclip requests tk

Or use the requirements file:

pip install -r requirements.txt

⚙️ How It Works
Monitors everything copied to your system clipboard

First checks for known sensitive data types using Regex

If nothing is detected, sends the copied text to Mistral via Ollama API for AI classification

Flags anything suspicious and shows a pop-up alert if needed

Logs everything into clipboard_log.txt

Run analyze_logs.py to audit usage and activity

📊 CLIPBOARD LOG ANALYSIS REPORT 📊
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔢 Total Entries: 10
🛡️  Sensitive: 5
✅ Not Sensitive: 5

🕒 Most Recent Entry:
📋 Copied: contact.ashtonhill@gmail.com
📅 Time: 2025-06-19 02:40:30
🤖 AI Response: Sensitive – Looks like an email ID.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✨ Author
Made with ❤️ by Abdul Haseeb and AI — aspiring cybersecurity guy, tech explorer, and AI experimenter.


