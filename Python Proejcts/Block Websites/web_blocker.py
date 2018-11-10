# C:\WINDOWS\system32\drivers\etc
import time
from datetime import datetime as dt

host_temp = "hosts"
host_path = r"C:\WINDOWS\system32\drivers\etc"
redirect = "127.0.0.1"

websites = ["www.facebook.com"]

while True:
    # if time is betwen 08-18, and 20:06
    if (dt(dt.now().year, dt.now().month, dt.now().day, 00) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 6) or dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18) or dt(dt.now().year, dt.now().month, dt.now().day, 20) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 23, 59, 59)):
        with open("hosts", 'r+') as file:
            content = file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        print("Now you can open")

    time.sleep(5)
