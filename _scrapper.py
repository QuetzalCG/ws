import requests
from bs4 import BeautifulSoup
import time
   
def files(dato):
    F = open("cursos.txt", "a")
    F.write(f"{dato}\n")
    F.close()

def scrapp():
    try:
        KEYS = ["Python", "PHP", "HTML", "CSS", "PostgreSQL", "Mysql", "JavaScript", "C#", "C++", "SQL", "Bootstrap", "MongoDB", "Angular", "Hacker", "Hacking", "Hackeo", "Linux"]
        r = requests.get("https://blog.facialix.com/cupones/")
        d = r.text
        s = BeautifulSoup(d, "html.parser")
        t = s.find_all("h2", "sek-pg-title")
        for x in t:
            su = x.find_all("a")
            titulo = su[0].text
            link = su[0].attrs.get("href")
            curso = f"\n{titulo}|{link}"
            for y in KEYS:
                if y in titulo:
                    print(curso)
                    print("Hay un curso sobre: " + y + "\n")
                    break
                else:
                    pass
    except Exception as a:
        print("Hay un error: " + a)

scrapp()