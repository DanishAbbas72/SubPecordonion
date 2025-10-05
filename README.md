# SubPecordonion
SubPecordonion is a lightweight yet powerful Python-based reconnaissance tool designed for penetration testers, bug bounty hunters, and security researchers. Discovering hidden subdomains, Identifying live hosts, Scanning top 100 ports for exposed services, Spidering with Katana to reveal hidden endpoints

# SubPecordonion 🧅 (v1.0)
### A Fast, Modular Reconnaissance Utility for Security Testing

---

## ⚡ Description

**SubPecordonion** (Subdomain Enumeration, Pecordion-like) is a comprehensive and highly efficient **Python-based reconnaissance tool** designed for security professionals and bug bounty hunters. It automates the initial and often tedious steps of security testing by performing a multi-stage target discovery in a single, seamless execution.

From casting a wide net for subdomains to pinpointing open ports and hidden endpoints, SubPecordonion provides a powerful and modular workflow for gathering critical information about your target domain.

### Key Features

* ☠️ **Subdomain Enumeration:** Uses a multi-engine approach to discover a maximum number of subdomains for a given target.
* 💀 **Live Host Detection:** Filters the enumerated subdomains to identify only the hosts that are currently active and responsive.
* ⚔️ **Port Scanning (Top 100):** Scans the active hosts for the top 100 most commonly exposed services, quickly identifying potential entry points.
* 🕷️ **Katana Spidering (Live):** Integrates the powerful **Katana** web crawler to uncover hidden directories, files, and parameterized URLs on the live target, revealing deep-seated endpoints for further testing.

---

## 🛠️ Installation

Follow these simple steps to get **SubPecordonion** up and running on your system (recommended on **Kali Linux** or other Linux distributions).

### 1. Clone the Repository
Use `git clone` to download the tool to your local machine:
```bash
git clone [https://github.com/YourUsername/SubPecordonion.git](https://github.com/YourUsername/SubPecordonion.git)
cd SubPecordonion
