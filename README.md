# 🧅 SubPecordonion (v1.0)

⚡ **A fast, modular recon utility for security testing** ⚡

---

## 🚀 About

**SubPecordonion** is a lightweight, modular reconnaissance tool written in Python. It's designed for penetration testers, bug bounty hunters, and security researchers who need a fast, reliable way to discover subdomains, identify live hosts, scan top ports, and spider targets for hidden endpoints.

This tool combines multiple recon techniques into a single script to help you quickly map an attack surface during the initial phases of a security assessment.

---

## ⚙️ Features

| Feature                     | Description                                              |
| --------------------------- | -------------------------------------------------------- |
| ☠ **Subdomain Enumeration** | Discovery with multi-engine depth for maximum coverage.  |
| 💀 **Live Host Detection**  | Filtering of subdomains to identify only active targets. |
| ⚔ **Top 100 Port Scanning** | Fast scanning for exposed services on live hosts.        |
| 🕷 **Katana Spidering**     | Uncovering hidden endpoints and parameterized URLs.      |

---

## 🔧 Installation

1. **Clone the repository**

```bash
git clone https://github.com/DanishAbbas72/SubPecordonion.git
cd SubPecordonion
```

2. **Requirements**

* Python 3.x

Check your Python version:

```bash
python3 --version
```

3. **Install dependencies** (if `requirements.txt` exists):

```bash
pip3 install -r requirements.txt
```

> If you don’t have a `requirements.txt`, install the packages used in the project manually.

---

## 🖥️ Usage

Run the tool from the project directory:

```bash
python3 SubPecordonion.py
```

The tool will launch an interactive terminal and prompt you to enter a target domain.

Example:

```
Enter target domain: example.com
```

---

## 🖼 Example Workflow (Screenshots / Output placeholders)

1. **🔍 Tool Launch & Subdomain Enumeration**

   * The tool starts and actively finds subdomains for the target.
   * *Placeholder for screenshot: `docs/screenshots/01-enumeration.png`*

2. **🌐 Live Host Detection & Summary**

   * Results are filtered to show only live and accessible hosts.
   * *Placeholder for screenshot: `docs/screenshots/02-live-hosts.png`*

3. **⚡ Port Scanning & 🕷 Katana Spidering**

   * Scans live hosts for open ports and uses Katana to crawl for hidden endpoints.
   * *Placeholder for screenshot: `docs/screenshots/03-ports-endpoints.png`*

> Add real screenshots to the `docs/screenshots/` folder and update the paths above.

---

## 🧩 Output & Logs

* The tool prints progress to the terminal. You can redirect output to a file if desired:

```bash
python3 SubPecordonion.py > output.txt
```

* Optionally add a logging facility (e.g. Python `logging`) to write structured logs to `logs/`.

---

## 🛠️ Configuration

* Customize scanning options and engines inside the script or via a configuration file (if provided).
* Consider adding a `config.yaml` or `config.json` for user-adjustable settings (engines, timeouts, port lists).

---

## ✍️ Contribution

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m "feat: add ..."`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Create a Pull Request

Please follow responsible disclosure and ensure any new features or fixes include appropriate tests or documentation.

---

## 🛡 Disclaimer

This tool is intended **for educational and authorized security testing only**. The author is **not responsible** for misuse. Always obtain explicit permission from the asset owner before running reconnaissance or scanning tools.

---

## 📝 License

Specify a license for the project (e.g., MIT, Apache-2.0). If you want, add a `LICENSE` file with the chosen license.

---

## 👤 Author

**Danish Abbas**

---

## 📌 Next steps / Suggestions

* Add a `requirements.txt` listing required Python packages.
* Add example configuration file (`config.yaml`).
* Add real screenshots to `docs/screenshots/` and update corresponding placeholders.
* Consider splitting functionality into modules and exposing a CLI using `argparse` or `click` for non-interactive automation.

---

*Generated README for SubPecordonion (v1.0).*
