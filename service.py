from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import unidecode
from datetime import datetime
import sys
import lorem

stime = 1  # float(sys.argv[1])
ltime = 2  # float(sys.argv[2])
timeout = 20

print(sys.argv)
counter = 0
def get_id():
    string = driver.current_url
    strings = string.split("/")
    for item in strings:
        if item.isdecimal():
            return item
def word():
    return lorem.sentence().split()[0]
def date():
    startyr = random.randrange(2000,2022)
    endyr= startyr + random.randrange(1,10)
    startm = random.randrange(1,13)
    endm =  random.randrange(1,13)
    startd = random.randrange(1,28)
    endd = random.randrange(1, 28)
    startdate= str(startyr)+"."+str(startm)+"."+str(startd)
    enddate=str(endyr)+"."+str(endm)+"."+str(endm)
    return [startdate,enddate]

def add(title):
    string = "//*[contains(text(), '"+title+"')]/button"
    try:
        element_present = EC.presence_of_element_located((By.XPATH, string))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        print("Timed out waiting for page to load")
    button = driver.find_element_by_xpath(string)  # "//*[contains(text(), 'Hívások ')]/button"
    button.click()
    time.sleep(stime)


def coinflip():
    return random.randrange(2)


def btn_click(name):
    btn_text = "//button[text()='" + name + "']"
    try:
        element_present = EC.presence_of_element_located((By.XPATH,btn_text))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        print("Timed out waiting for page to load")
    time.sleep(ltime)

    element = driver.find_element_by_xpath(btn_text)
    element.click()


def click(name):
    try:
        string = '[ng-reflect-name="' + name + '"]'
        element_present = EC.presence_of_element_located((By.CSS_SELECTOR,string))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        print("Timed out waiting for page to load")

    element = driver.find_element_by_css_selector(string)

    element.click()
    time.sleep(stime)
    return element


def dropdown(name):
    try:
        string = '[ng-reflect-name="' + name + '"]'
        element_present = EC.presence_of_element_located((By.CSS_SELECTOR, string))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        print("Timed out waiting for page to load")
    element = driver.find_element_by_css_selector(string)


    element.click()
    time.sleep(stime)
    selectOptions = driver.find_elements_by_xpath("//mat-option[@role = 'option']")
    time.sleep(stime)
    num = random.randrange(1, len(selectOptions))
    for _ in range(0,num):
        element.send_keys(Keys.DOWN)
        time.sleep(0.1)
    element.send_keys(Keys.SPACE)
    time.sleep(stime)
    return num
    # element.select_by_index(random.randrange(len(element.options)))


def write(name, text):
    element = click(name)
    element.send_keys(text)


def checkbox(label):
    try:
        string = '[ng-reflect-label="' + label + '"]'
        element_present = EC.presence_of_element_located((By.CSS_SELECTOR,string))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        print("Timed out waiting for page to load")
    element = driver.find_element_by_css_selector(string)
    element.click()
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
    adoszam+="-" + str(random.randrange(10)) + "-" + str(random.randrange(10))+str(
        random.randrange(10))
    return adoszam
def place(label):
    try:
        string = '[ng-reflect-label="' + label + '"]'
        element_present = EC.presence_of_element_located((By.CSS_SELECTOR, string))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        print("Timed out waiting for page to load")
    element = driver.find_element_by_css_selector(string)

    element.click()
    write("zipCode",str(szamsor(4)))
    write("city",random.choice(varosok))
    kozt = random.choice(kozterulet).split()
    write("publicDomain", kozt[0])
    write("publicDomainType",kozt[-1])
    write("buildingNumber",str(random.randrange(200)))
    btn_click(" OK")

def label():
    elements= driver.find_elements_by_class_name("label")
    element = random.choice(elements)

    element.click()
    time.sleep(stime)

titulusok=["PhD","DLA"]
c = open("ceg.txt",'r',encoding="utf8")
cegek=[]
for x in c:
    x=x.strip()
    cegek.append(x)

v = open("varosok.txt",'r',encoding='utf8')
varosok=[]
for x in v:
    x=x.strip()
    varosok.append(x)
k = open("kozterulet.txt",'r',encoding='utf8')
kozterulet=[]
for x in k:
    x=x.strip()
    kozterulet.append(x)

def telszam():
    telszam = '06' + str(random.randrange(1, 10)) + '0'

    for x in range(7):
        telszam += str(random.randrange(10))
    return telszam

def email(vnev,knev):
    domains=["com",'hu','org','ru','net']
    mails = ['gmail','freemail','citromail','hotmail']
    return unidecode.unidecode(vnev.lower() + str(knev.lower()) +szamsor(random.randrange(3))+ '@' +random.choice(mails)+'.'+random.choice(domains))

f = open("ferfi.txt","r",encoding="utf8")
n = open("no.txt",'r', encoding="utf8")
v = open("vezeteknev.txt",'r',encoding="utf8")
m = open("ugyfel\\munkak.txt",'r',encoding="utf8")
k = open("kozep.txt", 'r', encoding='utf8')
ferfinevek =[]
noinevek = []
vezeteknevek = []
munkak = []
kozep = []
for x in k:
    x=x.strip()
    kozep.append(x)
k.close()
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
m.close()
v.close()



try:
    driver = webdriver.Chrome()
    actions = ActionChains(driver)
    driver.get('https://erp2.schonherz.hu/')
    driver.maximize_window()
    # time.sleep(5)

    write("email", 'emailcím')


    write("password", 'jelszó')
    submit_btn = driver.find_element_by_class_name("btn")
    submit_btn.click()
    time.sleep(5)
except Exception as e:
    print(e)
    print('driver closing on error')
    time.sleep(10)
    driver.close()
