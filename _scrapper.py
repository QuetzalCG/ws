import requests
from bs4 import BeautifulSoup
import time
   
def files(dato):
    F = open("cursos.txt", "a")
    F.write(f"{dato}\n")
    F.close()

def scrapp():
    try:
        #Declaracion de llaves 
        KEYS = ["Python", "PHP", "HTML", "CSS", "PostgreSQL", "Mysql", "JavaScript", "C#", "C++", "SQL", "Bootstrap", "MongoDB", "Angular", "Hacker", "Hacking", "Hackeo", "Linux"]
        r = requests.get("https://blog.facialix.com/cupones/")
        d = r.text
        s = BeautifulSoup(d, "html.parser")
        t = s.find_all("h2", "sek-pg-title")
        #Iterar los datos extraidos del scrapper
        for y in t:
            su = y.find_all("a")
            titulo = su[0].text
            link = su[0].attrs.get("href")
            curso = f"\n{titulo}|{link}"
            #Iterar llaves y hacer un chequeo
            for y in KEYS:
                if y in titulo:
                    FILE = open("cursos.txt", "r")
                    r = FILE.read()
                    FILE.close()
                    if titulo in r:
                        pass
                    else:
                        files(titulo)
                        print(f"{curso}")
                    break
                else:
                    pass
        time.sleep(18000)
        scrapp()
    except Exception as a:
        print(f"Hay un error: {a}")


scrapp()