# 🧅 SubPecordonion (v1.0)

**⚡ A fast, modular recon utility for security testing ⚡**

| Feature | Description |
| :--- | :--- |
| ☠ **Subdomain Enumeration** | Discovery with multi-engine depth for maximum coverage. |
| 💀 **Live Host Detection** | Filtering of subdomains to identify only active targets. |
| ⚔ **Top 100 Port Scanning** | Fast scanning for exposed services on live hosts. |
| 🕷 **Katana Spidering** | Uncovering hidden endpoints and parameterized URLs. |

---

## 📖 Description

**SubPecordonion** is a lightweight yet powerful reconnaissance tool designed for penetration testers, bug bounty hunters, and security researchers.

It combines multiple recon techniques into a single modular Python script, helping you quickly map attack surfaces and uncover hidden assets in the initial stages of a security assessment.

---

## ⚙️ Installation

### 1. Cloning the Repository
Clone the repository and navigate into the project directory using your specific link:
```bash
git clone https://github.com/DanishAbbas72/SubPecordonion.git
cd SubPecordonion

📦 Requirements
SubPecordonion is built on Python 3. You can install all necessary dependencies using pip
# Ensure you have Python 3 installed
python3 --version

🖥️ Usage
Running SubPecordonion is straightforward. Simply execute the script with python3 from the tool's directory:
python3 SubPecordonion.py
The tool will launch its interactive terminal, prompting you to Enter target domain.

🖼 Example
Below are the screenshots of SubPecordonion in action, demonstrating its sequential workflow.

1. 🔍 Tool Launch & Subdomain Enumeration
The tool starts and begins actively finding subdomains for the target.

Initial Screen:

2. 🌐 Live Host Detection & Summary
After enumeration, the tool filters the results to report only the live and accessible hosts.

Live Hosts Found:

3. ⚡ Port Scanning & 🕷 Katana Spidering
The final stage scans live hosts for open ports and then uses Katana to crawl deep into the target for hidden endpoints.

Ports and Endpoints:

✍️ Created By
Danish Abbas

🛡 Disclaimer
This tool is intended for educational and authorized security testing purposes only.

The author is not responsible for any misuse or damage caused by this program. Always ensure you have explicit permission from the asset owner before running any security tools against a target.

