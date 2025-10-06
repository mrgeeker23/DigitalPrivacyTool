import pyperclip
import time
import requests
import json
import re
import datetime
import tkinter as tk
from threading import Thread

print("[🚀] Script started successfully!")

def log_to_file(copied_text, ai_response):
    with open("clipboard_log.txt", "a", encoding="utf-8") as logfile:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logfile.write(f"[{timestamp}] Copied: {copied_text}\n")
        logfile.write(f"AI Response: {ai_response}\n")
        logfile.write("-" * 40 + "\n")

# ⛓️ Regex Patterns for local detection
def detect_sensitive_data(text):
    patterns = {
        "Email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "Phone": r"\b\d{10}\b",
        "Card": r"\b(?:\d[ -]*?){13,16}\b",
        "PAN": r"\b[A-Z]{5}[0-9]{4}[A-Z]\b"
    }
    detected = []
    for label, pattern in patterns.items():
        if re.search(pattern, text):
            detected.append(label)
    return detected

# 🤖 Ollama / Mistral AI Fallback
def ask_ollama(text):
    try:
        response = requests.post(
            'http://localhost:11434/api/generate',
            json={
                "model": "mistral",
                "prompt": f"You're a cybersecurity expert. Analyze the following clipboard text: \"{text}\". Determine if it is sensitive (e.g., password, phone number, email, key, ID, or financial info). Respond with just: Sensitive or Not Sensitive and give a short reason.",
                "stream": False
            }
        )
        result = response.json()
        return result["response"].strip()
    except Exception as e:
        return f"[ERROR] Could not reach local AI: {e}"
    
def show_popup_alert(message):
    def popup():
        root = tk.Tk()
        root.title("⚠️ Sensitive Clipboard Alert")
        root.geometry("400x120")
        root.resizable(False, False)
        label = tk.Label(root, text=message, padx=20, pady=20, font=("Arial", 11))
        label.pack()
        button = tk.Button(root, text="OK", command=root.destroy)
        button.pack(pady=10)
        root.mainloop()

    Thread(target=popup).start()

# 📋 Clipboard Monitoring
def monitor_clipboard():
    print("[+] Monitoring clipboard. Press Ctrl+C to stop.\n")
    prev_text = ""
    while True:
        try:
            text = pyperclip.paste()
            if text != prev_text and text.strip() != "":
                print(f"[📋] Copied: {text}\n")

                # Run Regex Detection First
                found = detect_sensitive_data(text)
                if found:
                    local_detection = f"Local Detection: Found {', '.join(found)}"
                    print(f"[⚠️] {local_detection}\n")
                    log_to_file(text, local_detection)
                    show_popup_alert(local_detection)  # 🔔 Show popup

                else:
                    ai_response = ask_ollama(text)
                    print(f"[🤖] Mistral says: {ai_response}\n")
                    log_to_file(text, ai_response)
                    if "Sensitive" in ai_response:
                        show_popup_alert(ai_response)  # 🔔 Show popup for AI result

                prev_text = text
            time.sleep(1)
        except KeyboardInterrupt:
            print("\n[!] Stopped by user.")
            break
if __name__ == "__main__":
    monitor_clipboard()

