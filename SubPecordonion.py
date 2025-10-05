import subprocess
import os
import time
from datetime import datetime
from colorama import Fore, Style, init
init(autoreset=True)

def banner(show=True):
    """Print the banner only when show is True."""
    if not show:
        return

    print(Fore.RED + Style.BRIGHT + r"""
  ____        _     ____                        _             _             
 / ___| _   _| |__ |  _ \ ___  ___ ___  _ __ __| | ___  _ __ (_) ___  _ __  
 \___ \| | | | '_ \| |_) / _ \/ __/ _ \| '__/ _` |/ _ \| '_ \| |/ _ \| '_ \ 
  ___) | |_| | |_) |  __/  __/ (_| (_) | | | (_| | (_) | | | | | (_) | | | |
 |____/ \__,_|_.__/|_|   \___|\___\___/|_|  \__,_|\___/|_| |_|_|\___/|_| |_|
""")

    print(Fore.RED + Style.BRIGHT + "           ⫷⫷⫷  💻 PΞNTΞSTING T00L v1.0   ⫸⫸⫸\n")
    print(Fore.RED + Style.BRIGHT + "           ⫷⫷⫷  💀CRΞATΞD BY Danish Abbas ⫸⫸⫸\n")
    print(Fore.GREEN + Style.BRIGHT + """
========================================
||  > Subdomain Enumeration            ||
||  > Live Host Detection              ||
||  > Port Scanning (Top 100)          ||
||  > Katana Spidering (live)          ||
========================================
""")


    # Yellow for description block
    print(Fore.YELLOW + Style.BRIGHT + """⚡ A fast, modular recon utility for security testing ⚡ 

☠ Subdomain Enumeration with multi-engine depth ☠

💀 Live host Detection for active targets 💀

⚔ Top 100 Port Scanning for exposed services ⚔

🕷 Katana Spidering to uncover hidden endpoints 🕷

""")


def create_results_folder(domain):
    folder_name = f"{domain}_result"
    os.makedirs(folder_name, exist_ok=True)
    return folder_name

def enumerate_subdomains(domain):
    subdomains = set()
    print(Fore.YELLOW + Style.BRIGHT + "\n+] Enumerating subdomains...")
    start = time.time()

    try:
        proc = subprocess.Popen(
            ["subfinder", "-silent", "-d", domain],
            stdout=subprocess.PIPE, text=True
        )
        for line in proc.stdout:
            line = line.strip()
            if line:
                print(line)
                subdomains.add(line)
    except Exception:
        print(Fore.RED + "[!] SubFinder failed.")

    try:
        proc = subprocess.Popen(
            ["assetfinder", "--subs-only", domain],
            stdout=subprocess.PIPE, text=True
        )
        for line in proc.stdout:
            line = line.strip()
            if line:
                print(line)
                subdomains.add(line)
    except Exception:
        print(Fore.RED + "[!] Assetfinder failed.")

    end = time.time()
    print(Fore.CYAN + f"Total Subdomains found = {len(subdomains)} (Time: {end-start:.2f}s)")
    return sorted(subdomains)

def check_liveness_httpx(subdomains):
    live_hosts = set()
    print(Fore.YELLOW + Style.BRIGHT + "\n+] Checking live hosts...")
    start = time.time()
    try:
        proc = subprocess.Popen(
            ["httpx", "-silent", "-status-code", "-ip"],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True
        )
        out, _ = proc.communicate("\n".join(subdomains))
        for line in out.splitlines():
            if line:
                url = line.split()[0]
                host = url.replace("http://", "").replace("https://", "").split("/")[0]
                print(host)
                live_hosts.add(host)
    except Exception:
        print(Fore.RED + "[!] httpx failed.")
    end = time.time()
    print(Fore.CYAN + f"Total Live Hosts found = {len(live_hosts)} (Time: {end-start:.2f}s)")
    return sorted(live_hosts)

def scan_ports_naabu(live_hosts):
    open_ports = []
    print(Fore.YELLOW + Style.BRIGHT + "\n+] Scanning open ports...")
    start = time.time()
    try:
        proc = subprocess.Popen(
            ["naabu", "-silent", "-top-ports", "100"],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True
        )
        out, _ = proc.communicate("\n".join(live_hosts))
        for line in out.splitlines():
            if ":" in line:
                print(line)
                open_ports.append(line)
    except Exception:
        print(Fore.RED + "[!] naabu failed.")
    end = time.time()
    print(Fore.CYAN + f"Total OpenPorts found = {len(open_ports)} (Time: {end-start:.2f}s)")
    return sorted(open_ports)

def collect_parameterized_urls(domain, live_hosts):
    urls = set()
    print(Fore.YELLOW + Style.BRIGHT + "\n+] Crawling for parameterized URLs (Katana live)...")
    start = time.time()

    for host in live_hosts:
        try:
            proc = subprocess.Popen(
                ["katana", "-u", f"http://{host}", "-d", "3", "-jc", "-silent"],
                stdout=subprocess.PIPE, text=True
            )
            for line in proc.stdout:
                line = line.strip()
                if "?" in line:
                    print(line)
                    urls.add(line)
        except Exception:
            print(Fore.RED + f"[!] Katana failed for {host}")

    # waybackurls
    try:
        proc = subprocess.Popen(["waybackurls", domain], stdout=subprocess.PIPE, text=True)
        for line in proc.stdout:
            line = line.strip()
            if "?" in line:
                print(line)
                urls.add(line)
    except Exception:
        print(Fore.RED + "[!] waybackurls failed.")

    # gau
    try:
        proc = subprocess.Popen(["gau", domain], stdout=subprocess.PIPE, text=True)
        for line in proc.stdout:
            line = line.strip()
            if "?" in line:
                print(line)
                urls.add(line)
    except Exception:
        print(Fore.RED + "[!] gau failed.")

    end = time.time()
    print(Fore.CYAN + f"Total Parameterized URLs found = {len(urls)} (Time: {end-start:.2f}s)")
    return sorted(urls)

def main():
    banner()
    domain = input(Fore.YELLOW + "Enter target domain: ").strip()
    results_folder = create_results_folder(domain)

    subdomains = enumerate_subdomains(domain)
    live_hosts = check_liveness_httpx(subdomains)
    open_ports_all = scan_ports_naabu(live_hosts)
    param_urls = collect_parameterized_urls(domain, live_hosts)

    # Save results
    with open(os.path.join(results_folder, "subdomains.txt"), "w") as f:
        f.write("\n".join(subdomains))
    with open(os.path.join(results_folder, "live.txt"), "w") as f:
        f.write("\n".join(live_hosts))
    with open(os.path.join(results_folder, "openports.txt"), "w") as f:
        f.write("\n".join(open_ports_all))
    with open(os.path.join(results_folder, "parmaURLs.txt"), "w") as f:
        f.write("\n".join(param_urls))

    print(Fore.CYAN + f"\n[+] Process complete. Results saved in: {results_folder}")
    print("    subdomains.txt")
    print("    live.txt")
    print("    openports.txt")
    print("    parmaURLs.txt")

if __name__ == "__main__":
    main()
