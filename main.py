'''
Bot web scrapper de cursos UDEMY para el canal de DarkSeoul 
Make: @ImportThisQ
V: 0.1

Update: Imagenes diractas del curso agregadas

PreUpdate: Pexels API Images Rnd

Next Update: Bases de datos implementadas
'''

import time
import logging
from typing import Text
import requests 
import telegram
from bs4 import BeautifulSoup
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, PrefixHandler

#Constantes globales
TOKEN =      '2062575752:AAF4SYcb1bdmVqV5lN5qXSFlyYbIrOwTVIM'
KEYS =       ["Python", "PHP", "HTML", "CSS", "PostgreSQL", "Mysql", "JavaScript", "C#", "C++", "SQL", "Bootstrap", "MongoDB", "Angular", "Hacker", "Hacking", "Hackeo", "Linux", "Web", "web", "Docker", "Git", "VS CODE", "Visual Studio Code", "Heroku", "Malware"]
INF =        "-1001563177371"
DKS =        "-1001777627801"
SCRP =       "-1001502720349"
TEST =       "-1001504320804"
CONTADOR =   0


logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')
logger = logging.getLogger()

#Funciones

#Funcion Agregar el archivo
def files(dato):
    F = open("cursos.txt", "a")
    F.write(f"{dato}\n")
    F.close()
    
    print(f"{dato} -> scrappeado\n")

#Scrapper de cursos
def start_scp(update, context):
    
    b1 = InlineKeyboardButton(text="CHAT", url="https://t.me/DarkSeoulChat")
    bg = InlineKeyboardButton(text="CHAT", url="https://t.me/GLBTeamChat")
    b3 = InlineKeyboardButton(text="About", url="https://t.me/AboutSWQz")
    
    while CONTADOR == 0:
        
            try:
    
                #Declaracion de llaves 
                r =           requests.get("https://blog.facialix.com/cupones/")
                d =           r.text
                s =           BeautifulSoup(d, "html.parser")
                articulo =    s.find_all("article", "sek-has-thumb")
                
                print("Inicio de web scrapping")
                
                #Iterar los datos extraidos del scrapper
                for i in articulo:
                    
                    A =      i.find_all("div", "sek-pg-content")
                    CON =    A[0].find_all("a")[0]
                    FIG =    i.find_all("img")[0]
                    imagen = FIG.attrs.get("data-sek-src")
                    enlace = CON.attrs.get("href")
                    titulo = CON.text
                    
                    for i in KEYS:
                        
                        if i in titulo:
                            
                            with open("cursos.txt", "r") as a:
                                
                                x = a.read()
                            
                                if titulo in x:
                                
                                    pass
                                    
                                else:
                                    
                                    b2 = InlineKeyboardButton(text="¡Join Course!", url=enlace)
                                    
                                    context.bot.send_photo(chat_id=DKS, photo=imagen, parse_mode="HTML", caption=f"━━━━━━━━━━━━━━━━\n $ 𝙲𝙾𝚄𝚁𝚂𝙴𝚂 | ᴅᴋꜱ\n━━━━━━━━━━━━━━━━\n\n<b>¡{titulo}!</b>\n\n━━━━━━━━━━━━━━━━" ,reply_markup=InlineKeyboardMarkup([[b3, b1], [b2]]))
                                    context.bot.send_photo(chat_id=SCRP, photo=imagen, parse_mode="HTML", caption=f"━━━━━━━━━━━━━━━━\n $ 𝙲𝙾𝚄𝚁𝚂𝙴𝚂 | 𝙂𝙇𝘽[ϟ]\n━━━━━━━━━━━━━━━━\n\n<b>¡{titulo}!</b>\n\n━━━━━━━━━━━━━━━━" ,reply_markup=InlineKeyboardMarkup([[b3, bg], [b2]]))
                                    context.bot.send_photo(chat_id=TEST, photo=imagen, parse_mode="HTML", caption=f"━━━━━━━━━━━━━━━━\n $ 𝙲𝙾𝚄𝚁𝚂𝙴𝚂 | 𝙂𝙇𝘽[ϟ]\n━━━━━━━━━━━━━━━━\n\n<b>¡{titulo}!</b>\n\n━━━━━━━━━━━━━━━━" ,reply_markup=InlineKeyboardMarkup([[b3, b1], [b2]]))
                                    
                                    files(dato=titulo)
                                    
                                break
                            
                        else:
                            
                            pass
                            
                        
                            
                
            except Exception as a:
            
                print(f"Hay un error: {a}")
            
            time.sleep(7200)
            
    else:
    
        print("Error")
    

if __name__ == '__main__':
    botsito = telegram.Bot(token = TOKEN)

updater = Updater(botsito.token, use_context=True)

dp = updater.dispatcher

dp.add_handler(PrefixHandler(['def$', 'Import'], 'ws', start_scp))

updater.start_polling()
print('Bot cargado...')
updater.idle()