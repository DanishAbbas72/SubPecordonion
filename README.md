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

1. **🔍 Tool Launch **

![image](https://github.com/user-attachments/assets/74743755-f565-483d-a4ef-98c0ab7cc02c)

2. ** ☠️ Subdomain Enumeration **

![image](https://github.com/user-attachments/assets/cee4c4e4-cc75-47b5-af45-4bbc3b2eb4b5)


3. **🌐 Live Host Detection & Summary**

![image](https://github.com/user-attachments/assets/f4b10709-84b8-4648-8062-d7ee1900177e)


4. **⚡ Port Scanning & 🕷 Katana Spidering**

  ![image](https://github.com/user-attachments/assets/60c58dd1-e9aa-4158-976f-6bf13da326c1)

---


## 🧩 Output & Logs

* The tool prints progress to the terminal. You can redirect output to a file if desired:

```bash
python3 SubPecordonion.py > output.txt
```

* Optionally add a logging facility (e.g. Python `logging`) to write structured logs to `logs/`.

---


## ✍️ Contribution

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m "feat: add ..."`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Create a Pull Request

---

## 🛡 Disclaimer

This tool is intended **for educational and authorized security testing only**. The author is **not responsible** for misuse. Always obtain explicit permission from the asset owner before running reconnaissance or scanning tools.

---


## 👤 Author

**Danish Abbas**

---

