import requests
from bs4 import BeautifulSoup
import time
def scrapp():
    try:
        KEYS = ["CSS", "css", "Css", "HTML", "html", "Html", "PYTHON", "Python", "python", "JavaScript", "Javascript", "JAVASCRIPT", "PHP", "php", "Php"]
        r = requests.get("https://blog.facialix.com/cupones/")
        d = r.text
        if "python" in d or "php" in d:
            s = BeautifulSoup(d)
            t = s.find_all("h2", "sek-pg-title")
            for x in t:
                su = x.find_all("a")
                sub = su[0].text
                if KEYS in sub:
                    print(f"{sub}\n{sub.attrs.get('href')}\n\n")
                    time.sleep(5)
        else:
            pass
    except Exception as a:
        print(a)

scrapp()