import pyautogui
import time
import pyperclip
import random
import unidecode
from datetime import datetime
import sys
import lorem




stime = float(sys.argv[1])
ltime = float(sys.argv[2])

def Enter():
    time.sleep(stime*0.2)
    pyautogui.press("enter")
    time.sleep(stime*0.2)
def tab():
    time.sleep(stime*0.2)
    pyautogui.press("tab")
    time.sleep(stime*0.2)

def iclick(string):
    time.sleep(stime/2)
    pyautogui.click(string)
    time.sleep(stime/2)

def iwrite(pic,string):
    iclick(pic)
    pyperclip.copy(string)
    pyautogui.hotkey("ctrl", "v")

def click(x,y):
    pyautogui.moveTo(x,y,duration=0.5)
    pyautogui.click(x,y)
def TEnter():
    tab()
    Enter()
def twrite(string):
    tab()
    pyperclip.copy(string)
    pyautogui.hotkey("ctrl", "v")

def write(x,y,string):
    click(x,y)
    pyperclip.copy(string)
    pyautogui.hotkey("ctrl", "v")
def tscroll(options):
    tab()
    Enter()
    for _ in range  (random.randrange(1,options)):
        pyautogui.press('down')
        time.sleep(stime*0.1)
    Enter()
    time.sleep(stime)
def iscroll(pic,options):
    iclick(pic)
    for _ in range  (random.randrange(1,options)):
        pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(stime)

def scroll_list(x,y,options):
    click(x,y)
    for _ in range  (random.randrange(1,options)):
        pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(stime)
def szamsor(length):
    szamsor=""
    for _ in range(length):
        szamsor+=str(random.randrange(10))
    return szamsor


def adoszam():
    adoszam =""
    for _ in range(8):
        adoszam += str(random.randrange(10))
    adoszam+="-" + str(random.randrange(10)) + "-" + str(random.randrange(10))+str(random.randrange(10))
    return adoszam

titulusok=["PhD","DLA"]
c = open("ceg.txt",'r',encoding="utf8")
cegek=[]
for x in c:
    x=x.strip()
    cegek.append(x)

v = open("ceg.txt",'r',encoding='utf8')
varosok=[]
for x in v:
    x=x.strip()
    varosok.append(x)
k = open("kozterulet.txt",'r',encoding='utf8')
kozterulet=[]
for x in k:
    x=x.strip()
    kozterulet.append(x)

f = open("ferfi.txt","r",encoding="utf8")
n = open("no.txt",'r', encoding="utf8")
v = open("vezeteknev.txt",'r',encoding="utf8")
m = open("ugyfel\\munkak.txt",'r',encoding="utf8")
ferfinevek =[]
noinevek = []
vezeteknevek = []
munkak = []
for x in f:
    x=x.strip()
    ferfinevek.append(x)
f.close()

for x in n:
    x = x.strip()
    noinevek.append(x)
n.close()

for x in v:
    x = x.strip()
    vezeteknevek.append(x)
for x in m:
    x=x.strip()
    munkak.append(x)
f.close()
v.close()
f = open("ferfi.txt","r",encoding="utf8")
n = open("no.txt",'r', encoding="utf8")
v = open("vezeteknev.txt",'r',encoding="utf8")

#print(cegek)
while True:
#click(500,600)
    iclick("ugyfel\\uj_ugyfel.png")
    twrite(random.choice(cegek))
    twrite(adoszam())
    vevo = random.randrange(2)
    tab()
    if not vevo:
        tab()
    pyautogui.press("space")
    iclick("mentes.png")

    #sales
    scroll_list(1150,470,3)

    #iclick("sales.png")
    click(500,470)
    pyautogui.press("k")
    time.sleep(stime/5)
    pyautogui.press("down")
    time.sleep(stime/5)
    pyautogui.press("down")
    time.sleep(stime/5)
    pyautogui.press("down")
    time.sleep(stime/5)
    pyautogui.press("enter")
    time.sleep(stime/5)

    #szerkesztes

    #iwrite("ugyfel\\csoportos_adoszam.png",adoszam())
    write(420,330,adoszam())
    cegjegyzekszam = str(random.randrange(10))+ "-"+str(random.randrange(10)) + "-" + szamsor(6)
    write(1060,330,cegjegyzekszam)
    #iwrite("ugyfel\\cegjegyzekszam.png")
    click(400,400)
    #iclick("ugyfel\\szekhely.png")
    twrite(szamsor(4))
    twrite(random.choice(varosok))
    kozt = random.choice(kozterulet).split()
    twrite(kozt[0])
    twrite(kozt[-1])
    twrite(szamsor(1))
    iclick("ok.png")

    click(1250,400)
    #iclick("ugyfel\\levelezesi_cim.png")
    twrite(szamsor(4))
    twrite(random.choice(varosok))
    kozt = random.choice(kozterulet).split()
    twrite(kozt[0])
    twrite(kozt[-1])
    twrite(szamsor(1))
    iclick("ok.png")

    #write(1100,590,lorem.paragraph())
    #iwrite("ugyfel\\ceg_info.png",lorem.paragraph())

    label = random.randrange(2)
    tries=0
    while tries<3:

        try:
            if label==0:
                #click(400,680)
                iclick("ugyfel\\clientlabel1.png")
            elif label == 1:
                #click(500,680)
                iclick("ugyfel\\clientlabel2.png")
            tries= 3
        except:
            
            tries+=1
            print("nem ismert fel egy képet, újrapróbálkozás..")
            time.sleep(3)

    iclick("ugyfel\\mentes.png")

    iclick("ugyfel\\kontaktok.png")
    iclick("ugyfel\\hozzaadas.png")
    vnev=random.choice(vezeteknevek)
    knev=random.choice(ferfinevek+noinevek)
    twrite(vnev+ " " + knev)
    telszam='06' + str(random.randrange(1,10)) + '0'
        
    for x in range(7):
        telszam += str(random.randrange(10))
    twrite(telszam)
    twrite(unidecode.unidecode(vnev+knev+"@gmail.com").lower())
    tab()
    if random.randrange(2):
        pyautogui.press("space")
    if  not random.randrange(10):
        twrite(random.choice(titulusok))
    else:
        tab()
    twrite(lorem.sentence())
    if label==0:
        #click(400,680)
        iclick("ugyfel\\CCPO1.png")
    elif label == 1:
        #click(500,680)
        iclick("ugyfel\\CCPO2.png")
    elif label == 2:
        #click(600,860)
        iclick("ugyfel\\CCPO3.png")
    iclick("mentes.png")

    iclick("ugyfel\\szerzodesek.png")
    iclick("ugyfel\\hozzaadas.png")
    twrite(lorem.sentence().split()[0])
    tscroll(3)
    tab()
    tab()
    Enter()
    startdate = random.randrange(10)
    enddate = random.randrange(startdate,20)
    for _ in range(startdate):
        time.sleep(stime/5)
        pyautogui.press("right")
    Enter()
    tab()
    tab()
    Enter()
    for _ in range(enddate):
        time.sleep(stime/2)
        pyautogui.press("right")
    Enter()
    tab()
    if random.randrange(2):
        pyautogui.press("space")
    twrite(str(random.randrange(20)))
    twrite("https://bit.ly/3Bq4jeX")
    TEnter()
    # clientlabel 1: 400, 680 clientlabel2:500,680 clientlabel3:600,680

        #kontaktok: 530,190
        #reszletek:400,190
        #szerződések:680,190
        #megrendelések:830,190 
        #virtuális TIG sablon: 1000,190
    iclick("ugyfel\\tig.png")
    iclick("ugyfel\\hozzaadas.png")
    twrite(lorem.sentence())
    twrite(lorem.sentence())
    twrite(lorem.sentence())
    TEnter()
    iclick("ugyfel\\szamlazasra_kuld.png")
    iclick("ugyfel\\vir_tig.png")
    iclick("ugyfel\\plus.png")
    time.sleep(ltime)
    tab()
    tab()
    tab()
    tab()
    tab()
    Enter()
    startdate = random.randrange(10)
    enddate = random.randrange(startdate,20)
    for _ in range(startdate):
        time.sleep(stime/5)
        pyautogui.press("right")
    Enter()
    tab()
    tab()
    Enter()
    for _ in range(enddate):
        time.sleep(stime/2)
        pyautogui.press("right")
    Enter()
    iclick("ugyfel\\plus_gray.png")
    tscroll(3)
    twrite(str(random.randrange(1000)))
    tscroll(3)
    twrite(str(random.randrange(1000)))
    tscroll(3)
    twrite(lorem.sentence())
    TEnter()
    #time.sleep(20)
            
    iclick("ugyfel\\megrendelesek.png")
    iclick("ugyfel\\hozzaadas.png")
    twrite(random.choice(munkak))
    tscroll(3)
    tscroll(3)
    tscroll(2)
    TEnter()

    time.sleep(ltime)
    iclick("megrendeles\\dolgozok.png")
    iclick("megrendeles\\uj_dolgozo.png")
    twrite(str(random.randrange(2,500)))
    time.sleep(ltime)
    tab()
    tab()
    TEnter()
    #iclick("megrendeles\\kereses.png")
    click(800,670)
    click(800,750)
    TEnter()
    startdate = random.randrange(10)
    for _ in range(startdate):
        time.sleep(stime/5)
        pyautogui.press("right")
    Enter()
    TEnter()

    if random.randrange(2):
        iclick("megrendeles\\uj_szakmai_gyakorlat.png")
        click(800,500)
        tab()
        tab()
        TEnter()
        startdate = random.randrange(10)
        for _ in range(startdate):
            time.sleep(stime/5)
            pyautogui.press("right")
        Enter()
        twrite(str(random.randrange(20,41)))
        TEnter()
    time.sleep(ltime)
    iclick("megrendeles\\hirdetesek.png")
    iclick("megrendeles\\uj_hirdetes.png")
    twrite(random.choice(munkak))
    TEnter()
    time.sleep(ltime)
    pyautogui.press("browserback")
    time.sleep(ltime)
    iclick("megrendeles\\arak.png")
    iclick("megrendeles\\uj_ar.png")
    twrite(random.choice(munkak))
    tab()
    if random.randrange(2):
        pyautogui.press("space")


    tscroll(3)
    twrite(str(random.randrange(1000,1500)))
    twrite(str(random.randrange(500,1500)))
    tscroll(3)
    startdate = random.randrange(10)
    tab()
    TEnter()
    for _ in range(startdate):
        time.sleep(stime/5)
        pyautogui.press("right")
    Enter()
    for _ in range(12):
        time.sleep(stime/5)
        pyautogui.press("right")
    Enter()

    time.sleep(ltime)
    tipus = random.randrange(5)
    if tipus == 0:
        iclick("megrendeles\\hetkoznap.png")
    elif tipus == 1:
        iclick("megrendeles\\szombat.png")
    elif tipus == 2:
        iclick("megrendeles\\vasarnap.png")
    elif tipus == 3:
        iclick("megrendeles\\unnepnap.png")
    elif tipus == 4:
        iclick("megrendeles\\szakmai_gyak.png")

    iclick("mentes.png")
    #iclick("megrendeles\\reszletek.png")
    time.sleep(ltime)
    iclick("ugyfel\\ugyfelek_dropdown.png")
    iclick("ugyfel\\ugyfelek.png")
        


