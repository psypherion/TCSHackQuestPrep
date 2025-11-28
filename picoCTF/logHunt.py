import re
logpath: str = "server.log"

def read_log_file(logpath: str) -> str:
    with open(logpath, "r") as file:
        return file.read()
    

logcontent = read_log_file(logpath=logpath)

# Find all regex pattern "[*] INFO FLAGPART:"

pattern = r"INFO FLAGPART:\s*(.*)"
matches = re.findall(pattern, logcontent)
print(matches)

# find unique parts
unique_parts = set(matches)
print(unique_parts)