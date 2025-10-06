# 🛡️ Digital Privacy Tool — Clipboard Monitoring & Sensitive Data Detection

A real-time clipboard monitoring tool that detects sensitive information like emails, phone numbers, credit card numbers, and PAN using both **local regex patterns** and an **AI-powered analysis** via [Ollama](https://ollama.com/) + [Mistral](https://mistral.ai/). Designed with cybersecurity best practices and a lightweight **popup alert GUI** using `Tkinter`.

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

