import requests
import time
from bs4 import BeautifulSoup
   
def files(dato):
    
    F = open("cursos.txt", "a")
    F.write(f"{dato}\n")
    F.close()

def scrapp():
    
    while "a":
    
        try:
        
            #Declaracion de llaves 
            KEYS =        ["Python", "PHP", "HTML", "CSS", "PostgreSQL", "Mysql", "JavaScript", "C#", "C++", "SQL", "Bootstrap", "MongoDB", "Angular", "Hacker", "Hacking", "Hackeo", "Linux", "Web", "web"]
            r =           requests.get("https://blog.facialix.com/cupones/")
            d =           r.text
            s =           BeautifulSoup(d, "html.parser")
            articulo =    s.find_all("article", "sek-has-thumb")
            
            #Iterar los datos extraidos del scrapper
            for i in articulo:
                
                A = i.find_all("div", "sek-pg-content")
                CON = A[0].find_all("a")[0]
                FIG = i.find_all("img")[0]
                imagen = FIG.attrs.get("data-sek-src")
                enlace = CON.attrs.get("href")
                titulo = CON.text
                
                for i in KEYS:
                    
                    if i in titulo:
                        
                        print(f"{titulo}|{enlace}|{imagen}\n\n")
                        
                    else:
                        
                        pass
            
        except Exception as a:
        
            print(f"Hay un error: {a}")
            
        time.sleep(7)
        

# def olas():
    
#     get = scrapp()
    
#     print(get)
    
scrapp()





    
    