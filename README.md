# 🔐 PRODIGY_CS_03 — Cybersecurity Task 3: Password Complexity Checker

This is Task 3 of the Cybersecurity track from Prodigy Infotech.

## 📌 Project Overview

In today's threat landscape, password security is a frontline defense mechanism. This tool helps users understand how secure their passwords are by checking them against five essential complexity criteria:

- ✅ Minimum length requirement
- ✅ Presence of **uppercase** and **lowercase** letters
- ✅ Inclusion of **numerical digits**
- ✅ Use of **special characters**

The script not only provides a **strength rating** (Weak, Medium, Strong) but also gives **actionable feedback** to help users create stronger passwords.

---

## 💻 Features

- 🧠 **Intelligent Complexity Check**  
  Uses regular expressions to verify password structure and composition.

- 🔍 **Real-Time Feedback**  
  Users are given immediate feedback on what makes their password weak or strong.

- 🧪 **Score-Based Strength Assessment**  
  Passwords are scored out of 5, and rated as:
  - `Strong` 💪
  - `Medium` ⚠️
  - `Weak` 🚫

- 🎯 **Beginner-Friendly Script**  
  Built with simplicity in mind — clean, readable, and easy to extend.

---

## 🛠️ Tech Stack

- Language: **Python 3**
- Dependencies: None (standard library only)
- Platform: Linux / Kali Linux

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Jetlin_Figarez/PRODIGY_CS_03.git
cd PRODIGY_CS_03

# 2. Run the script

python3 password_checker.py

# 3. Example Output

Enter your password to test: Cyber@123

--- Password Analysis ---
Password: Cyber@123
✅ Strong Password 💪

# 📂 Repository Structure

PRODIGY_CS_03/
├── password_checker.py   # Main script
└── README.md             # Documentation

# 📈 Future Improvements

🔐 Add a password generator for strong alternatives

🌐 Build a web-based version with Flask

📊 Export password analysis reports in JSON/CSV

🧪 Integrate with hash leak databases (e.g., HaveIBeenPwned)


