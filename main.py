#Importar librerias
import requests 
import telegram
import random
import time
import os
import logging
import psycopg2
from datetime import date
from telegram.ext import Updater, PrefixHandler, Filters, MessageHandler, CallbackQueryHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from pyunsplash import PyUnsplash
from bs4 import BeautifulSoup

#Constantes globales
TOKEN = '2062575752:AAF4SYcb1bdmVqV5lN5qXSFlyYbIrOwTVIM'
NOW = date.today()
INF = "-1001563177371"
SCRP = "-1001502720349"
TEST = "-1001504320804"

#Configuración de logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')
logger = logging.getLogger()

#Funciones

#Funcion Agregar el archivo
def files(dato):
    F = open("cursos.txt", "a")
    F.write(f"{dato}\n")
    F.close()

#Scrapper de cursos
def start_scp(update, context):
    def scrapp():
        print("\n------Scrapping Web Iniciado------\n")
        KEYS = ["Python", "PHP", "HTML", "CSS", "PostgreSQL", "Mysql", "JavaScript", "C#", "C++", "SQL", "Bootstrap", "MongoDB", "Angular", "Hacker", "Hacking", "Hackeo", "Linux", "web", "Web", "React", "forense", ""]
        r = requests.get("https://blog.facialix.com/cupones/")
        d = r.text
        s = BeautifulSoup(d, "html.parser")
        t = s.find_all("h2", "sek-pg-title")
        im = s.find_all("figure", "sek-pg-thumbnail")
        #Iterar los datos extraidos del scrapper
        for y in t:
            su = y.find_all("a")
            titulo = su[0].text
            link = su[0].attrs.get("href")
            b1 = InlineKeyboardButton(text="Entra al Curso", url=link)
            #Iterar llaves y hacer un chequeo
            for x in KEYS:
                if x in titulo:
                    FILE = open("cursos.txt", "r")
                    r = FILE.read()
                    FILE.close()
                    if titulo in r:
                        print("No hay cursos")
                        pass
                    else:
                        pu = PyUnsplash(api_key="lPDPAJGmT_KIhQAKVaVytFajtrSVEBxvK1PYfiEKlDc")
                        photos = pu.photos(type_='random', count=1, featured=True, query=x)
                        [photo] = photos.entries
                        foto = photo.link_download
                        context.bot.send_photo(chat_id=INF, photo=foto, parse_mode="HTML", caption=f"<b>\n{titulo}\n</b>" ,reply_markup=InlineKeyboardMarkup([[b1]]))
                        context.bot.send_photo(chat_id=SCRP, photo=foto, parse_mode="HTML", caption=f"<b>\n{titulo}\n</b>" ,reply_markup=InlineKeyboardMarkup([[b1]]))
                        files(dato=titulo)
                        print(titulo)
                    break
                else:
                    pass
                    #print("No hay cursos sobre eso")
        time.sleep(3600)
        scrapp()
    scrapp()

#Comando /start
def start(update, context):
    b1 = InlineKeyboardButton(text='GROUP CHK', url='https://t.me/ChatNOTORIOUS')
    b2 = InlineKeyboardButton(text='CC CHANNEL', url='https://t.me/joinchat/8buuJybmaiswNTcx')
    b3 = InlineKeyboardButton(text='Commands', callback_data='editcmd')
    frase = random.choice(['Have a nice day! :3', 'I hope you are well!', 'I wish you the best!'])
    em = random.choice(['❤️‍🔥', '❣️', '🔥', '🌨', '🧸'])
    e = update.message.reply_text(parse_mode='Markdown', text=f"*Welcome @{update.effective_user['username']} {em}\n━━━━━━━━━━━━━━━━━\nI hope you are well, I Andy and I will help you in what I can.\nTry to display my commands using: \n/cmds\n\n{frase.title()}\n━━━━━━━━━━━━━━━━━━\nBy: @ChatNOTORIOUS*", reply_markup=InlineKeyboardMarkup([[b1, b2], [b3]]))

#Editar Comandos
def cmde(update, context):
    qr = update.callback_query
    ret = InlineKeyboardButton(text='Return', callback_data='return')
    qr.edit_message_text(parse_mode='Markdown', text=f'*>_. My Commands 🤖\n━━━━━━━━━━━━━━━━\n$ /bin Make a query of your bin\n$ /rnd Make a fake info query\n$ /p Request the chat id\n━━━━━━━━━━━━━━━━\nBy: @ChatNOTORIOUS*', reply_markup=InlineKeyboardMarkup([[ret]]))

#Editar return
def back(update, context):
    qr = update.callback_query
    b1 = InlineKeyboardButton(text='GROUP CHK', url='https://t.me/ChatNOTORIOUS')
    b2 = InlineKeyboardButton(text='CC CHANNEL', url='https://t.me/joinchat/8buuJybmaiswNTcx')
    b3 = InlineKeyboardButton(text='Commands', callback_data='editcmd')
    frase = random.choice(['Have a nice day! :3', 'I hope you are well!', 'I wish you the best!'])
    em = random.choice(['❤️‍🔥', '❣️', '🔥', '🌨', '🧸'])
    qr.edit_message_text(parse_mode='Markdown', text=f"*Welcome @{update.effective_user['username']} {em}\n━━━━━━━━━━━━━━━━━\nI hope you are well, I Andy and I will help you in what I can.\nTry to display my commands using: \n/cmds\n\n{frase.title()}\n━━━━━━━━━━━━━━━━━━\nBy: @ChatNOTORIOUS*", reply_markup=InlineKeyboardMarkup([[b1, b2], [b3]]))

#Comando /cmds
def cmds(update, context):
    update.message.reply_text(parse_mode='Markdown', text=f'*>_. My Commands 🤖\n━━━━━━━━━━━━━━━━\n$ /bin Make a query of your bin\n$ /rnd Make a fake info query\n$ /p Request the chat id\n━━━━━━━━━━━━━━━━\nBy: @InfernoChannel*')

#Comando /bin
def bin(update, context):
    chat_id = update.effective_chat['id']
    args = context.args 
    if len(args) > 0:
        username = update.effective_user['username']
        b = args[0]
        bins = b[0:6]
        url = f"https://theminers.cf/apis/bin/{bins}"
        r = requests.get(url)
        try:
            data = r.json()
            b = data['bin']
            brand = data['brand']
            typec = data['type']
            level = data['level']
            bank = data['bank']['name']
            phone = data['bank']['phone']
            site = data['bank']['site']
            cty = data['country']['name']
            cuy = data['country']['currency']
            flag = data['country']['flag']
            code = data['country']['ISO2']
            e1 = update.message.reply_text(parse_mode='Markdown', text=f'*>_.Bin Lookup*')
            context.bot.edit_message_text(chat_id=chat_id, message_id=e1.message_id, parse_mode='Markdown', text=f'* >_.Bin Lookup ❤️‍🔥\n━━━━━━━━━━━━━━━\n$Bin: {b}(✅)\n$Brand: {brand.title()}\n$Type: {typec.title()}\n$Level: {level.title()}\n\n¢Bank: {bank.title()}\n¢Phone: {phone}\n¢Page: {site}\n\n∆Country: {cty.title()}\n∆Flag: {flag}\n∆Code: {code.upper()}\n∆Currency: {cuy.upper()}\n━━━━━━━━━━━━━━━\nChk: @{username} *')
        except:
            update.message.reply_text(parse_mode='Markdown', text=f'*>_.Invalid ❤️‍🩹*')
    else:
        update.message.reply_text(parse_mode='Markdown', text="*>_.You got a mistake ❤️‍🩹\n━━━━━━━━━━━━━━━\n$Fix: /bin 482727*")

#Comando /rnd
def rnd(update, context):
    args = context.args
    username = update.effective_user['username']
    btn = InlineKeyboardButton(text='Regen', callback_data='regen')
    if len(args) == 1:
        args = args[0]
        if len(args) == 2:
            url = f'https://randomuser.me/api/1.2/?nat={args}'
            r = requests.get(url)
            try:
                data = r.json()
                name = data['results'][0]['name']['first']
                lname = data['results'][0]['name']['last']
                gen = data['results'][0]['gender']
                mail = data['results'][0]['email']
                ph = data['results'][0]['cell']
                pc = data['results'][0]['location']['postcode']
                date = data['results'][0]['registered']['date']
                year = data['results'][0]['registered']['age']
                pic = data['results'][0]['picture']['medium']
                est = data['results'][0]['location']['state']
                city = data['results'][0]['location']['city']
                calle = data['results'][0]['location']['street']
                tz = data['results'][0]['location']['timezone']['description']
                rint = random.randint(1, 1000)
                rp = random.choice(['.', '_', 'a', 'AM', 'babygirl'])
                eml = random.choice(['@gmail.com', '@outlook.com', '@yahoo.com', '@MX.com'])
                update.message.reply_text(parse_mode='Markdown', text=f'*>_.Random Tool❤️‍🔥\n━━━━━━━━━━━━━━━\n$Name: {name.title()} {lname.title()}\n$Gender: {gen.capitalize()}\n$Birthday: {date.title()}\n$Age: {year}\n$Mail: {name}{rp}{lname}{rint}{eml}\n$Phone: {ph}\n\n∆State: {est.title()}\n∆City: {city.title()}\n∆ZipCode: {pc}\n∆Street: {calle.title()}\n∆Timezone: {tz.title()}\n━━━━━━━━━━━━━━━\nChk: @{username}*', reply_markup=InlineKeyboardMarkup([[btn]]))
            except:
                update.message.reply_text(parse_mode='Markdown', text='*>_.Wrong country ❤️‍🩹*')
        else:
            update.message.reply_text(parse_mode='Markdown', text='*>_.You got a mistake ❤️‍🩹\n━━━━━━━━━━━━━━━\n$Fix: /rnd MX*')
    else:
        update.message.reply_text(parse_mode='Markdown', text='*>_.You got a mistake ❤️‍🩹\n━━━━━━━━━━━━━━━\n$Fix: /rnd MX*')

#Regen fake data
def regen(update, context):
    username = update.effective_user['username']
    btn = InlineKeyboardButton(text='Regen', callback_data='regen')
    qr = update.callback_query
    url = f'https://randomuser.me/api/1.2/?nat=rnd'
    r = requests.get(url)
    data = r.json()
    name = data['results'][0]['name']['first']
    lname = data['results'][0]['name']['last']
    gen = data['results'][0]['gender']
    mail = data['results'][0]['email']
    ph = data['results'][0]['cell']
    pc = data['results'][0]['location']['postcode']
    date = data['results'][0]['registered']['date']
    year = data['results'][0]['registered']['age']
    pic = data['results'][0]['picture']['medium']
    est = data['results'][0]['location']['state']
    city = data['results'][0]['location']['city']
    calle = data['results'][0]['location']['street']
    tz = data['results'][0]['location']['timezone']['description']
    rint = random.randint(1, 1000)
    rp = random.choice(['.', '_', 'a', 'loc', 'babygirl'])
    eml = random.choice(['@gmail.com', '@outlook.com', '@yahoo.com', '@MX.com'])
    qr.edit_message_text(parse_mode='Markdown', text=f'*>_.Random Tool❤️‍🔥\n━━━━━━━━━━━━━━━\n$Name: {name.title()} {lname.title()}\n$Gender: {gen.capitalize()}\n$Birthday: {date.title()}\n$Age: {year}\n$Mail: {name}{rp}{lname}{rint}{eml}\n$Phone: {ph}\n\n∆State: {est.title()}\n∆City: {city.title()}\n∆ZipCode: {pc}\n∆Street: {calle.title()}\n∆Timezone: {tz.title()}\n━━━━━━━━━━━━━━━\nChk: @{username}*', reply_markup=InlineKeyboardMarkup([[btn]]))

#Comando #p
def p(update, context):
    chat_id = update.effective_chat['id']
    cname = update.effective_chat['title']
    update.message.reply_text(parse_mode='HTML', text=f'<b>Chat:</b> <code>{chat_id}</code>\n<b>Name:</b> {cname}')

#Comando /me
def me(update, context):
    UID = update.effective_user['id']
    NAME = update.effective_user['first_name']
    LNAME = update.effective_user['last_name']
    USERN = update.effective_user['username']
    try:
        c = psycopg2.connect(
            host='localhost',
            port='5432',
            user='Quetzal',
            password='admin',
            database='andy'
        )
        cu = c.cursor()
        cu.execute(f"SELECT rango, creditos FROM usuarios WHERE ids='{UID}'")
        r = cu.fetchall()
        update.message.reply_text(parse_mode='Markdown', text=f'*>_.Your Info ❤️‍🔥\n━━━━━━━━━━━━━━━\nNAME: {NAME}\nL. NAME: {LNAME}\nID: {UID}\nRANK: {r[0][0]}\nCREDITS: {r[0][1]}\nUSER: @{USERN}*')
        c.close()
        cu.close()
        
    except Exception as e:
        UID = update.effective_user['id']
        c = psycopg2.connect(
            host='localhost',
            port='5432',
            user='Quetzal',
            password='admin',
            database='andy'
        )
        cu = c.cursor()
        s = f"INSERT INTO usuarios(ids, rango, creditos) VALUES('{UID}', 'Free', 0)"
        cu.execute(s)
        c.commit()
        cu.execute(f"SELECT rango, creditos FROM usuarios WHERE ids='{UID}'")
        r = cu.fetchall()
        update.message.reply_text(parse_mode='Markdown', text=f'*>_.Your Info ❤️‍🔥\n━━━━━━━━━━━━━━━\nNAME: {NAME}\nL. NAME: {LNAME}\nID: {UID}\nRANK: {r[0][0]}\nCREDITS: {r[0][1]}\nUSER: @{USERN}*')
        context.bot.send_message(chat_id='1768587060', text=f"New Join Alert\n--------\n@{USERN}\n\n#{UID}")
        c.close()
        cu.close()
        
    except:
        update.message.reply_text(parse_mode='Markdown', text=f'*Algo salio mal :/*')
        
#Comando /upgrade
def upg(update, context):
    args = context.args 
    UID = update.effective_user['id']
    if len(args) > 0:
        args = args[0]
        c = psycopg2.connect(
            host='localhost',
            port='5432',
            user='Quetzal',
            password='admin',
            database='andy'
        )
        cu = c.cursor()
        cu.execute(f"SELECT rango FROM usuarios WHERE ids='{UID}'")
        rango = cu.fetchall()
        rng = rango[0][0]
        c.close()
        cu.close()
        if rng == 'Owner' or rng == 'Admin':
            args = args.split('|')
            uid = args[0]
            rang = args[1]
            crd = args[2]
            crd = int(crd)
            c = psycopg2.connect(
            host='localhost',
            port='5432',
            user='Quetzal',
            password='admin',
            database='andy')
            cu = c.cursor()
            s = f"UPDATE usuarios SET rango='{rang}', creditos={crd} WHERE ids='{uid}'"
            try: 
                cu.execute(s)
                c.commit()
                update.message.reply_text(parse_mode='Markdown', text='*The account has been updated.*')
                c.close()
                cu.close()
            except Exception as a:
                update.message.reply_text(f'Something went wrong .\n\n{a}')
                print(a)
        else:
            update.message.reply_text(parse_mode='Markdown', text='You cannot use this function')
    else:
        update.message.reply_text(parse_mode='Markdown', text="Everything's fine? Handsome")

#Comando agregar chats al scrapper
def push(update, context):
    UID = update.effective_user['id']
    args = context.args
    if len(args) == 1:
        c = psycopg2.connect(host='localhost',port='5432',user='Quetzal',password='admin',database='andy')
        cu = c.cursor()
        cu.execute(f"SELECT rango FROM usuarios WHERE ids='{UID}'")
        a = cu.fetchall()
        c.close()
        rng = a[0][0]
        cu.close()
        if rng == 'Owner' or rng == 'CoOwner':
            args = args[0]
            args =args.split('|')
            CID = args[0]
            N = args[1]
            c = psycopg2.connect(host='loalhost',port='5432',user='Quetzal',password='admin',database='andy')
            cu = c.cursor()
            cu.execute(f"INSERT INTO chats(cid, cname) VALUES('{CID}', '{N}')")
            c.commit()
            c.close()
            cu.close()
            update.message.reply_text(parse_mode='Markdown', text='<b>This chat:</b> {CID} <b>is now scrapped</b>')
        else:
            update.message.reply_text(parse_mode='Markdown', text='*You cannot use this function.*')
    else:
        update.message.reply_text(parse_mode='Markdown', text='*Is something wrong? Handsome*')

#Comando para agregar canales a scrappear 
def post(update, context):
    UID = update.effective_user['id']
    args = context.args
    if len(args) == 1:
        c = psycopg2.connect(host='localhost',port='5432',user='Quetzal',password='admin',database='andy')
        cu = c.cursor()
        cu.execute(f"SELECT rango FROM usuarios WHERE ids='{UID}'")
        a = cu.fetchall()
        c.close()
        rng = a[0][0]
        cu.close()
        if rng == 'Owner' or rng == 'CoOwner':
            args = args[0]
            args =args.split('|')
            CID = args[0]
            N = args[1]
            c = psycopg2.connect(host='localhost',port='5432',user='Quetzal',password='admin',database='andy')
            cu = c.cursor()
            cu.execute(f"INSERT INTO canales(chid, chname) VALUES('{CID}', '{N}')")
            c.commit()
            c.close()
            cu.close()
            update.message.reply_text(parse_mode='HTML', text=f"<b>Now I'll post ccs on the channel:</b> <code>{CID}</code>")
        else:
            update.message.reply_text(parse_mode='Markdown', text='*You cannot use this function.*')
    else:
        update.message.reply_text(parse_mode='Markdown', text='*Is something wrong? Handsome.*')

#Quitar canales a los cuales postear 
def unpost(update, context):
    args = context.args
    UID = update.effective_user['id']
    if len(args) > 0:
        c = psycopg2.connect(host='localhost',port='5432',user='Quetzal',password='admin',database='andy')
        cu = c.cursor()
        cu.execute(f"SELECT rango FROM usuarios WHERE ids='{UID}'")
        a = cu.fetchall()
        c.close()
        cu.close()
        rng = a[0][0]
        if rng == 'Owner' or rng == 'CoOwner':
            CID = args[0]
            c = psycopg2.connect(host='localhost',port='5432',user='Quetzal',password='admin',database='andy')
            cu = c.cursor()
            cu.execute(f"DELETE FROM canales WHERE chid='{CID}'")
            c.commit()
            c.close()
            cu.close()
            update.message.reply_text(parse_mode='HTML', text=f'<b>I will no longer post ccs on the channel:</b> <code>{CID}</code>')
        else:
            update.message.reply_text(parse_mode='Markdown', text='*You cannot use this function.*')
    else:
        update.message.reply_text(parse_mode='Markdown', text='*Is something wrong? Handsome*')

#Comando para quitar chats de la lista de scrappeados
def unpush(update, context):
    args = context.args
    UID = update.effective_user['id']
    if len(args) > 0:
        c = psycopg2.connect(host='localhost',port='5432',user='Quetzal',password='admin',database='andy')
        cu = c.cursor()
        cu.execute(f"SELECT rango FROM usuarios WHERE ids='{UID}'")
        a = cu.fetchall()
        c.close()
        cu.close()
        rng = a[0][0]
        if rng == 'Owner' or rng == 'CoOwner':
            CID = args[0]
            c = psycopg2.connect(host='localhost',port='5432',user='Quetzal',password='admin',database='andy')
            cu = c.cursor()
            cu.execute(f"DELETE FROM chats WHERE cid='{CID}'")
            c.commit()
            c.close()
            cu.close()
            update.message.reply_text(parse_mode='HTML', text='<b>This chat:</b> <code>{CID}</code><b>is now not scrapped</b>')
        else:
            update.message.reply_text(parse_mode='Markdown', text='*You cannot use this function.*')
    else:
        update.message.reply_text(parse_mode='Markdown', text='*Is something wrong? Handsome*')

#Lectura continua de mensajes txt
def echo(update, context):
    user_id = update.effective_user['id']   
    text = update.effective_message['text']
    chat_id = update.effective_chat['id']
    username = update.effective_user['username']
    key1 = "Bye bye"
    key2 = "Pene"
    key3 = "CGambler"
    key4 = "Hola, Perseo"
    key7 = "¿Soy gay?"
    key8 = "¿Cuanto me mide?"
    txt = update.effective_message['text']
    UMID = update.effective_message['message_id']
    meid = int(UMID) + 2
    if txt == 'Ey Andy' or txt == 'ey andy' or txt == 'Ey andy':
        update.message.reply_text(parse_mode='HTML', text='<b>Hey, how are you?!</b>')
    elif key2 == text:
            update.message.reply_text(parse_mode="HTML", text="<b>Comes :D</b>")
    elif key3 == text:
        update.message.reply_text(parse_mode="HTML", text="<b>PRO MINECRAFT BUILDERS</b>")
    elif key4 == text:
        update.message.reply_text(parse_mode="HTML", text=f"<b>Hola @{username}, ¿Como estas?</b>")
    elif key7 == text or "Soy gay?" == text or "soy gay?" == text or "¿Soy gay?" == text:
        ent = random.randint(0, 100)
        letters = random.choice(["¡Hay mi vidaaa!", "Ya sal del closet amigue :D", "Ni es tanto compa, aun eres machito :3", "Grrrrr", "Vamo' a la sombrita :3", "Ok pero ahora besáme c:"])
        update.message.reply_text(parse_mode="HTML", text=f'<b>Hey @{username} :)\nEres {ent}% gay\n{letters}</b>')
    elif key8 == text or "Cuanto me mide?" == text or "Cuánto me mide?" == text or "¿Cuánto me mide?" == text or "cuanto me mide?" == text or "¿cuanto me mide?" == text:
        dick = random.randint(1, 25)
        tula = random.choice(["¡Tremenda tula mi bro!", "Tremendo animalon, grrrr... digo digo, WOW!", "Oie vro, es para reproducirse, no para partir mundos", "Peor es nada bro, ¡animo!"])
        update.message.reply_text(parse_mode="HTML", text=f'<b>Hey @{username}\n¡La tula te mide {dick}cm!\n{tula}</b>')
    elif "¿Soy norteño?" == text or "¿soy norteño?" == text or "soy norteño?" == text or "Soy norteño?" == text:
        nrt = random.randint(0, 100)
        frase = random.choice(["Ajuaaa", "Que chille pa", "¡Saca las primas pariente!", "Una miche o k", "¿Pa' cuando la carnilla asada pa' festejar?", "Entonces, ¿Intercambio de primas?"])
        update.message.reply_text(parse_mode="HTML", text=f"<b>¡Hey @{username}!\nTu nivel de norteño es tipo {nrt}%\n{frase}</b>")

if __name__ == '__main__':
    botsito = telegram.Bot(token = TOKEN)

updater = Updater(botsito.token, use_context=True)

dp = updater.dispatcher

dp.add_handler(PrefixHandler(['/', '$', '!', '.', '?', '-', '+', 'def$'], 'start', start))
dp.add_handler(PrefixHandler(['/', '$', '!', '.', '?', '-', '+', 'def$'], 'cmds', cmds))
dp.add_handler(PrefixHandler(['/', '$', '!', '.', '?', '-', '+', 'def$'], 'bin', bin))
dp.add_handler(PrefixHandler(['/', '$', '!', '.', '?', '-', '+', 'def$'], 'rnd', rnd))
dp.add_handler(PrefixHandler(['/', '$', '!', '.', '?', '-', '+', 'def$'], 'p', p))
dp.add_handler(PrefixHandler(['/', '$', '!', '.', '?', '-', '+', 'def$'], 'ws', start_scp))
dp.add_handler(CallbackQueryHandler(pattern='editcmd', callback=cmde))
dp.add_handler(CallbackQueryHandler(pattern='return', callback=back))
dp.add_handler(CallbackQueryHandler(pattern='regen', callback=regen))
dp.add_handler(MessageHandler(Filters.text, echo))
updater.start_polling()
print('Bot cargado...')
updater.idle()