
# TCS HACKQUEST CTF CHALLENGE REPORT TEMPLATE
# ===========================================

## REPORT METADATA
- **Challenge Name:** [Challenge Title]
- **Category:** [Web/Crypto/Forensics/Pwn/Reverse/Misc]
- **Difficulty:** [Beginner/Intermediate/Expert]
- **Points:** [Point Value]
- **Date Solved:** [DD/MM/YYYY]
- **Time Taken:** [HH:MM:SS]
- **Solver Name:** [Your Name]
- **TCS Reference ID:** [CT/DT Number]

---

## 1. EXECUTIVE SUMMARY (2-3 sentences)
Provide a brief overview of what the challenge was about and how you solved it.

Example:
"This challenge involved exploiting an SQL injection vulnerability in a web application's login form. 
By identifying a vulnerable parameter and crafting a UNION-based SQL injection payload, I was able to 
extract the admin credentials from the database and retrieve the flag."

---

## 2. CHALLENGE DESCRIPTION
Paste the exact challenge description provided by TCS HackQuest.

Example:
"Can you bypass the authentication system and retrieve the admin flag?
URL: http://challenge.hackquest.tcs/login
Credentials: guest/guest"

---

## 3. INITIAL RECONNAISSANCE

### 3.1 Information Gathering
Document your initial analysis and what you observed.

- What did you see when you first accessed the challenge?
- What technologies were in use? (Check HTTP headers, page source, etc.)
- What functionality is available?
- Any interesting files, directories, or parameters?

**Tools Used:**
- [ ] Nmap
- [ ] Burp Suite
- [ ] Browser DevTools
- [ ] Curl/Wget
- [ ] Other: ___________

**Observations:**
```
[Document your findings here]
Example:
- Application runs on Apache/2.4.41
- Login form with username/password fields
- Client-side validation present
- No rate limiting observed
```

---

## 4. VULNERABILITY IDENTIFICATION

### 4.1 Testing Methodology
Describe how you identified the vulnerability.

**Test Cases Performed:**
1. Test 1: [Describe what you tested]
   - Result: [Success/Failure]
   - Observation: [What you learned]

2. Test 2: [Describe what you tested]
   - Result: [Success/Failure]
   - Observation: [What you learned]

### 4.2 Vulnerability Details
- **Vulnerability Type:** [SQL Injection / XSS / Command Injection / etc.]
- **Affected Parameter:** [Parameter name]
- **Location:** [URL or function where vulnerability exists]
- **Risk Level:** [Critical/High/Medium/Low]

**Proof of Concept:**
```
[Paste the malicious input that proves the vulnerability]
Example:
Username: admin' OR '1'='1
Password: anything
```

---

## 5. EXPLOITATION

### 5.1 Exploitation Steps (Detailed Step-by-Step)

**Step 1: [First Action]**
```
Command/Input:
[Paste exact command or input]

Output/Response:
[Paste the response you got]

Screenshot: [Include screenshot if available]
```

**Step 2: [Second Action]**
```
Command/Input:
[Paste exact command or input]

Output/Response:
[Paste the response you got]

Screenshot: [Include screenshot if available]
```

[Continue for all steps...]

### 5.2 Tools and Scripts Used
List all tools and any custom scripts you wrote.

**Tools:**
- Burp Suite (for intercepting requests)
- SQLmap (for automated SQL injection)
- Python script (for automation)

**Custom Scripts:**
```python
# If you wrote any scripts, include them here
import requests

url = "http://challenge.hackquest.tcs/login"
payload = {"username": "admin' OR '1'='1", "password": "test"}
response = requests.post(url, data=payload)
print(response.text)
```

---

## 6. FLAG CAPTURE

### 6.1 Flag Location
Describe where and how you found the flag.

Example:
"After successfully logging in as admin, the flag was displayed on the dashboard page."

### 6.2 Flag Format
```
FLAG: TCS{this_is_example_flag_123456}
```

### 6.3 Flag Screenshot
**IMPORTANT: Include screenshot showing:**
- The flag clearly visible
- Timestamp visible (use system clock or screenshot timestamp)
- Challenge name/URL visible in the same screenshot

[INSERT SCREENSHOT HERE]

Screenshot file name: `challenge_name_flag_YYYY-MM-DD_HH-MM-SS.png`

---

## 7. TECHNICAL ANALYSIS

### 7.1 Root Cause Analysis
Explain why the vulnerability existed.

Example:
"The application failed to properly sanitize user input before passing it to SQL queries. 
The developer used string concatenation instead of parameterized queries, making it 
vulnerable to SQL injection attacks."

### 7.2 Attack Flow Diagram
```
User Input → Web Form → Backend Processing → Database Query → Response
     ↓             ↓              ↓                  ↓            ↓
  Malicious   No Validation  Query Construction  Malicious     Flag
   Payload                   (String concat)      Query      Revealed
```

---

## 8. REMEDIATION RECOMMENDATIONS

### 8.1 Immediate Fixes
What should be done right now to fix this vulnerability?

1. **Use Parameterized Queries**
   ```python
   # Bad (Vulnerable)
   query = "SELECT * FROM users WHERE username='" + user_input + "'"

   # Good (Secure)
   query = "SELECT * FROM users WHERE username=?"
   cursor.execute(query, (user_input,))
   ```

2. **Input Validation**
   - Implement whitelist-based input validation
   - Sanitize all user inputs
   - Use prepared statements

3. **Additional Security Measures**
   - Implement rate limiting
   - Add Web Application Firewall (WAF)
   - Enable SQL error suppression in production

---

## 9. LESSONS LEARNED

### 9.1 What I Learned
Document what you learned from this challenge.

- Technical skills gained: [e.g., SQL injection techniques]
- Tools learned: [e.g., SQLmap usage]
- Concepts understood: [e.g., OWASP Top 10 vulnerabilities]

### 9.2 Challenges Faced
What difficulties did you encounter?

- [Difficulty 1 and how you overcame it]
- [Difficulty 2 and how you overcame it]

### 9.3 Alternative Approaches
Were there other ways to solve this challenge?

1. Approach 1: [Describe alternative method]
2. Approach 2: [Describe another method]

---

## 10. REFERENCES

### 10.1 Tools Used
- Burp Suite Community Edition v2024.1
- SQLmap v1.7
- Python 3.11
- Kali Linux 2024.1

### 10.2 Resources Referenced
List any writeups, documentation, or guides you consulted.

1. OWASP SQL Injection Guide: https://owasp.org/www-community/attacks/SQL_Injection
2. PortSwigger SQL Injection Cheat Sheet
3. [Other resources]

### 10.3 Similar CTF Challenges
Reference similar challenges for learning.

- PicoCTF: SQL Direct (2023)
- HackTheBox: SQLI Login Bypass
- [Other similar challenges]

---

## 11. APPENDIX

### 11.1 Complete Request/Response Logs
```
[Include full HTTP requests and responses if relevant]

POST /login HTTP/1.1
Host: challenge.hackquest.tcs
Content-Type: application/x-www-form-urlencoded
Content-Length: 45

username=admin'+OR+'1'='1&password=test
```

### 11.2 Code Snippets
[Any additional code or scripts]

### 11.3 Network Traffic Captures
[If you captured network traffic with Wireshark, include relevant packets]

---

## CHECKLIST BEFORE SUBMISSION ✓

- [ ] All screenshots include timestamp
- [ ] Flag is clearly visible in screenshot
- [ ] Step-by-step approach is documented
- [ ] All tools used are listed
- [ ] Report follows the provided template
- [ ] Grammar and spelling checked
- [ ] File size is within limit (check TCS requirements)
- [ ] Report is saved as PDF format
- [ ] File naming: `HackQuest_YourName_ChallengeName_YYYYMMDD.pdf`

---

## REPORT FORMATTING GUIDELINES

1. **Font:** Use Arial or Calibri, 11pt for body text
2. **Headings:** Bold and larger font (14pt for main, 12pt for sub)
3. **Code Blocks:** Use monospace font (Courier New, 10pt)
4. **Screenshots:** High quality (min 1920x1080), clearly labeled
5. **Page Numbers:** Include page numbers in footer
6. **Table of Contents:** Auto-generate if report is longer than 5 pages

---

END OF TEMPLATE
