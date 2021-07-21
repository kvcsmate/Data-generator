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

c = open("ceg.txt",'r',encoding="utf8")
cegek=[]
for x in c:
    x=x.strip()
    cegek.append(x)

random.seed(datetime.now())
#print(cegek)
#while True:
click(500,600)
twrite(random.choice(cegek))
adoszam =""
for _ in range(8):
    adoszam += str(random.randrange(10))
adoszam+="-" + str(random.randrange(10)) + "-" + str(random.randrange(10))+str(random.randrange(10))
twrite(adoszam)
vevo = random.randrange(2)
tab()
if not vevo:
    tab()
pyautogui.press("space")
if vevo:
    tab()
TEnter()


  
        