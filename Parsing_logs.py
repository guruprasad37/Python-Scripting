with open("/var/log/syslog", "r") as file:
    logs = file.readlines()

for log in logs:
    if "error" in log.lower():
        print(log)
