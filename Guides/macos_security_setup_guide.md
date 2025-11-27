
# TCS HACKQUEST - macOS SECURITY ENVIRONMENT SETUP GUIDE
# ========================================================

## PHASE 1: ESSENTIAL TOOL INSTALLATION ON macOS
## ==============================================

### 1. Install Homebrew (Package Manager)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2. Install Command Line Tools
```bash
# Network scanning
brew install nmap

# Network analysis
brew install wireshark

# DNS tools
brew install dnsutils

# Network utilities
brew install netcat

# Web testing
brew install curl wget

# Text processing
brew install jq

# Python and pip
brew install python3

# Git
brew install git

# File analysis
brew install binwalk
brew install exiftool
brew install foremost

# Password cracking
brew install john
brew install hashcat

# Cryptography
brew install openssl

# Steganography
brew install steghide

# Disassembler/Debugger
brew install radare2
brew install gdb

# Other essentials
brew install tmux
brew install tree
brew install htop
```

### 3. Install GUI Applications via Homebrew Cask
```bash
# Burp Suite Community Edition
brew install --cask burpsuite

# Wireshark GUI
brew install --cask wireshark

# Docker Desktop
brew install --cask docker

# VS Code
brew install --cask visual-studio-code

# Postman (API testing)
brew install --cask postman

# UTM (Virtual Machine)
brew install --cask utm
```

### 4. Python Security Tools
```bash
# Create virtual environment
python3 -m venv ~/ctf-env
source ~/ctf-env/bin/activate

# Install common CTF tools
pip install pwntools
pip install requests
pip install beautifulsoup4
pip install pycryptodome
pip install z3-solver
pip install angr
pip install frida-tools
pip install scapy
pip install paramiko
pip install impacket
```

## PHASE 2: KALI LINUX SETUP (via UTM for ARM Mac)
## ================================================

### Download and Setup:
1. Download UTM: https://mac.getutm.app/
2. Download Kali Linux ARM64: https://www.kali.org/get-kali/#kali-installer-images
   - Get the ARM64 installer image
3. Create VM in UTM:
   - Memory: 4GB minimum (8GB recommended)
   - CPU cores: 4
   - Storage: 40GB minimum

### Initial Kali Setup Commands:
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install essential tools
sudo apt install -y kali-linux-headless

# Install specific tool categories
sudo apt install -y kali-tools-web
sudo apt install -y kali-tools-crypto-stego
sudo apt install -y kali-tools-forensics
sudo apt install -y kali-tools-reverse-engineering
sudo apt install -y kali-tools-exploitation
```

## PHASE 3: WEB SECURITY TOOLS SETUP
## ===================================

### Burp Suite Configuration:
1. Install FoxyProxy extension in browser
2. Configure proxy: localhost:8080
3. Import Burp CA certificate
4. Practice on DVWA and PortSwigger Academy

### SQL Injection Tools:
```bash
# SQLmap
brew install sqlmap

# Or install via pip
pip install sqlmap
```

### Directory Busting:
```bash
# Install gobuster
brew install gobuster

# Install dirb (via Kali)
sudo apt install dirb
```

## PHASE 4: DOCKER CONTAINERS FOR PRACTICE
## =========================================

```bash
# Pull vulnerable applications
docker pull vulnerables/web-dvwa
docker pull bkimminich/juice-shop
docker pull webgoat/webgoat-8.0

# Run DVWA
docker run -d -p 80:80 vulnerables/web-dvwa

# Run Juice Shop
docker run -d -p 3000:3000 bkimminich/juice-shop

# Run WebGoat
docker run -d -p 8080:8080 webgoat/webgoat-8.0
```

## PHASE 5: CRYPTOGRAPHY TOOLS
## ============================

```bash
# Hash cracking
brew install hashcat
brew install john-jumbo

# Encoding/Decoding
pip install base58
pip install pycryptodome

# Online tools (bookmark these):
# - CyberChef: https://gchq.github.io/CyberChef/
# - dCode: https://www.dcode.fr/
# - CrackStation: https://crackstation.net/
```

## PHASE 6: REVERSE ENGINEERING SETUP
## ====================================

```bash
# Ghidra (Download from NSA website)
# https://ghidra-sre.org/

# Radare2 (already installed via brew)
r2 -v

# IDA Free (Download from Hex-Rays)
# https://hex-rays.com/ida-free/

# Hopper Disassembler (macOS native)
brew install --cask hopper-disassembler

# For dynamic analysis
brew install lldb
```

## PHASE 7: FORENSICS & STEGANOGRAPHY
## ===================================

```bash
# File analysis
brew install binwalk
brew install foremost
brew install exiftool
brew install sleuthkit

# Steganography
brew install steghide
brew install stegseek

# Image analysis
pip install pillow
pip install stegano

# Volatility (memory forensics)
pip install volatility3
```

## PHASE 8: NETWORK TOOLS
## =======================

```bash
# Scanning
brew install nmap
brew install masscan

# Sniffing
brew install wireshark
brew install tcpdump

# VPN/Tunneling
brew install openvpn

# Practice: Use nmap on local network
nmap -sV localhost
```

## USEFUL ALIASES TO ADD TO ~/.zshrc or ~/.bashrc
## ================================================

```bash
# Add these to your shell config
alias ll='ls -lah'
alias ports='netstat -tulanp'
alias myip='curl ifconfig.me'
alias serve='python3 -m http.server 8000'
alias sqlmap-basic='sqlmap -u'
alias nmap-quick='nmap -sV -sC -O'
alias burp='open -a "Burp Suite Community Edition"'
```

## FOLDER STRUCTURE FOR CTF ORGANIZATION
## =======================================

```bash
mkdir -p ~/CTF/{tools,challenges,writeups,resources,scripts}
mkdir -p ~/CTF/challenges/{web,crypto,forensics,pwn,reverse,misc}
mkdir -p ~/CTF/resources/{wordlists,payloads,cheatsheets}
```

## ESSENTIAL WORDLISTS
## ====================

```bash
# Download SecLists
git clone https://github.com/danielmiessler/SecLists.git ~/CTF/resources/SecLists

# Download RockYou wordlist
curl -o ~/CTF/resources/rockyou.txt https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
```

## VERIFICATION CHECKLIST
## =======================

After setup, verify everything works:

```bash
# Check installations
nmap --version
wireshark --version
python3 --version
docker --version
burpsuite --version
radare2 -v
sqlmap --version
hashcat --version

# Test Python tools
python3 -c "import pwn; print('pwntools OK')"
python3 -c "import requests; print('requests OK')"

# Test network connectivity
nmap -sV scanme.nmap.org
```

## NOTES FOR macOS USERS
## ======================

1. **Wireshark Permission Issues**: 
   - Run: sudo chown $(whoami) /dev/bpf*
   - Or install ChmodBPF via Homebrew

2. **Gatekeeper Issues**:
   - System Settings > Privacy & Security > Allow apps from identified developers

3. **Firewall**:
   - Enable macOS firewall for security
   - Allow necessary applications

4. **Performance**:
   - Close unnecessary apps during CTF
   - Monitor Activity Monitor for resource usage

5. **Time Management**:
   - Use Pomodoro technique
   - Take regular breaks
