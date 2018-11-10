# C:\WINDOWS\system32\drivers\etc
import time
from datetime import datetime as dt

# Hosts file path for windows 10
host_path = r"C:\WINDOWS\system32\drivers\etc\hosts"
redirect = "127.0.0.1"
# Websites list you want to restrict
websites = ["www.facebook.com"
            ]

while True:
    # if time is betwen 08-18, and 20:06
    if (dt(dt.now().year, dt.now().month, dt.now().day, 00) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 6) or dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18) or dt(dt.now().year, dt.now().month, dt.now().day, 20) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 23, 59, 59)):
        with open(host_path, 'r+') as file:
            content = file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
                    print("This is work hour.")
    else:
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
            print("This is fun hour")
    time.sleep(5)
