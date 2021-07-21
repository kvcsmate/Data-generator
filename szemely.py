import pyautogui
import time
import pyperclip
import random
import unidecode
from datetime import datetime


def Enter():
    time.sleep(0.2)
    pyautogui.press("enter")
    time.sleep(0.2)
def tab():
    time.sleep(0.2)
    pyautogui.press("tab")
    time.sleep(0.2)

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
    pyautogui.press("enter")
    for _ in range  (random.randrange(1,options)):
        pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(1)

def scroll_list(x,y,options):
    click(x,y)
    for _ in range  (random.randrange(1,options)):
        pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(1)



f = open("ferfi.txt","r",encoding="utf8")
n = open("no.txt",'r', encoding="utf8")
v = open("vezeteknev.txt",'r',encoding="utf8")
k = open("kozep.txt",'r',encoding='utf8')
ferfinevek =[]
noinevek = []
vezeteknevek = []
kozep = []
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
v.close()

for x in k:
    x=x.strip()
    kozep.append(x)
k.close()

print(pyautogui.size())
ferfie = False
vnev = ""
knev = ""
telszam = ""
email = ""

for i in range (3,0,-1):
    print("program starts in " + str(i))
    time.sleep(.5)


while True:
    click(500,600)

    ##click(900,500)
    vnev=random.choice(vezeteknevek)
    twrite(vnev)
    ##write(900,500,vnev)

    ##click(900,560)
    if random.randrange(2):
        knev=random.choice(ferfinevek)
        #write(900,560,knev)
        twrite(knev)
        ferfie=True
    else:
        knev=random.choice(noinevek)
        #write(900,560,knev)
        twrite(knev)
        ferfie=False

    ##click(900,630)
    email = unidecode.unidecode(vnev.lower()+str(knev.lower())+'@gmail.com')
    #write(900,630,email)
    twrite(email)
    #click(900,700) ##submit
    TEnter()
    time.sleep(2)
    #click(1200,330) ## telefonszám
    telszam='06' + str(random.randrange(1,10)) + '0'
    
    for x in range(7):
        telszam += str(random.randrange(10))
    write(1200,330,telszam)
    click(500,400) ## Nem
    if ferfie:
        click(450,450)
    else:
        click(500,500)
    ##jogsi
    if random.randrange(2):
        click(350,450)
    ##hírlevél
    if random.randrange(2):
        click(1020,400)
    ##label
    choice = random.randrange(3)
    if choice ==0:
        click(400,540)
    elif choice == 1:
        click(530,540)
    elif choice == 2:
        click(630,540)
    ## szakmai tudás
    choice = random.randrange(3)
    if choice ==0:
        click(420,640)
    elif choice == 1:
        click(550,640)
    elif choice == 2:
        click(680,640)

    click(450,700) ##submit form
    time.sleep(2)


    ##iskolák:430 595
    click(430,595)
    ##  típus 900 440
    school = random.randrange(2)
    ## végzettség: 900 690 ha középiskola, érettségi, ha egyetem, bsc
    click(900,440)
    if school:
        ##  egyetem : 900 535
        click(900,535)
        scroll_list(900,505,3)
        write(900,690,'BsC')
    else:
    ## középiskola: 900 575
        click(900,575)
        write(900,505,random.choice(kozep))
        write(900,690,'érettségi')
    ## kezdés éve: 900 570
    kezdes= random.randrange(2000,2019)
    write(900,570,str(kezdes))
    ## befejezés éve: 900 630
    befejezes = kezdes + 3 + random.randrange(2)
    write(900,630,str(befejezes))
    ## mentés : 870 755
    click(870,755)

    ## nyelv :465 745
    click(465,745)
    ##nyelv 900 450, 10 opció lefele gombbal kiválaszt majd enter
    scroll_list(900,450,10)
    ## szint: 900 510 3 opció
    scroll_list(900,510,3)
    ## használat módja 900 570 3 opció
    scroll_list(900,570,3)
    ##tesztelve: 785 620
    if random.randrange(2):
        click(785,620)

    click(850,750) # mentés

    #hívások
    click(1100,380)
    tscroll(3)
    tab()
    TEnter()
    if random.randrange(2):
        ##dokumentumok: 550 185
        click(550,185)
        ## hozzáadás: 450 270
        click(450,270)
        tscroll(3)
        ## dokumentum típusa: 930 470
        ##      documenttype1 : 900 525
        ##      documenttype2: 900 570
        ##      documenttype3: 900 605
        twrite("diákigazolvány")
        ## megjegyzés: 930 530
        ##  paste diákigazolvány
        ## dokumentum kiválasztása:840 620
        click(840,620)
        time.sleep(1)
        pyperclip.copy('diak.pdf')
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)
        ## paste diak.pdf
        ## enter
        pyautogui.press("enter")
        time.sleep(2)
        
        ##mentés 900 670
        click(900,670)
        ## részletek: 400 185
        click(400,185)


    ##softskillek: 700 185
    if random.randrange(2):
        ##tesztek : 800 185
        click(800,185)
        ## hozzáadás: 450 270
        click(450,270)
        tscroll(3)
        twrite(str(random.randrange(1,100)))
        tab()
        tab()
        tab()
        TEnter()
        ## részletek: 400 185
        click(400,185)

    if random.randrange(2):
         ##jelentkezések : 950 185
        click(950,185)
        ## új jelentkezés: 450 270
        click(450,270)
        ##  ID :850 500 
        twrite(str(1))
        Enter()
        ## paste 1
        ## keresés : 850 630
        ## kiválasztás:820 670
        click(820,670)
        ## mentés : 850 740
        click(850,740)
        ## részletek: 400 185
        click(400,185)
   

    click(1220,900) ## vissza
    ## 1220, 900 ha van iskola és nyelv
    print(vnev+" "+knev)
    timer = random.randrange(5,20)
    print("sleep for " + str(timer) +" seconds" )
    time.sleep(timer)
    if not random.randrange(15):
        print("coffee break!")
        time.sleep(random.randrange(120,300))
        
        
    
