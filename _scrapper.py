from os import write
import requests
from bs4 import BeautifulSoup
try:
    url = "https://blog.facialix.com/cupones/"
    #url = "https://google.com"
    r = requests.get(url=url)
    d = r.text
    if "python" in d or "php" in d:
        s = BeautifulSoup(d)
        t = s.find_all("h2", "sek-pg-title")
        for x in t:
            su = x.find_all("a")
            print(f"{su[0].text}\n{su[0].attrs.get('href')}\n\n")
            
        
    else:
        print("No hay cursos de esos lenguajes ")
except Exception as a:
    print(a)
