from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random
import unidecode
from datetime import datetime, timedelta
import sys
import lorem


stime = 0.1  # float(sys.argv[1])
ltime = 0.5  # float(sys.argv[2])
timeout = 2
#print(sys.argv)
counter = 0
print("futási idő órában:")
est_rtime = float(sys.argv[1])
runtime = datetime.now() + timedelta(hours=est_rtime)


def get_id():
    string = driver.current_url
    strings = string.split("/")
    for item in strings:
        if item.isdecimal():
            return item


def add(selector):
    string = "//*[contains(text(), '" + selector + "')]/button"
    try:
        element_present = EC.presence_of_element_located((By.XPATH, string))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        print("Timed out waiting for page to load")
    button = driver.find_element_by_xpath(string)  # "//*[contains(text(), 'Hívások ')]/button"
    button.click()


def coinflip():
    return random.randrange(2)


def btn_click(name):
    btn_text = "//button[text()='" + name + "']"
    try:
        element_present = EC.presence_of_element_located((By.XPATH, btn_text))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        print("Timed out waiting for page to load")
    time.sleep(ltime)

    driver.find_element_by_xpath(btn_text).click()
    time.sleep(ltime)

def click(selector):
    try:
        string = '[ng-reflect-name="' + selector + '"]'
        element_present = EC.presence_of_element_located((By.CSS_SELECTOR, string))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        print("Timed out waiting for page to load")

    element = driver.find_element_by_css_selector(string)

    element.click()
    return element


def dropdown(selector):
    try:
        string = '[ng-reflect-name="' + selector + '"]'
        element_present = EC.presence_of_element_located((By.CSS_SELECTOR, string))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        print("Timed out waiting for page to load")
    element = driver.find_element_by_css_selector(string)
    element.click()
    time.sleep(ltime)
    selectOptions = driver.find_elements_by_xpath("//mat-option[@role = 'option']")
    time.sleep(ltime)
    num = random.randrange(1, len(selectOptions))
    for _ in range(num):
        element.send_keys(Keys.DOWN)
        time.sleep(0.1)
    element.send_keys(Keys.SPACE)
    time.sleep(ltime)
    return num
    # element.select_by_index(random.randrange(len(element.options)))


def write(selector, text):
    element = click(selector)
    element.send_keys(text)


def checkbox(selector):
    try:
        string = '[ng-reflect-label="' + selector + '"]'
        element_present = EC.presence_of_element_located((By.CSS_SELECTOR, string))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        print("Timed out waiting for page to load")
    element = driver.find_element_by_css_selector(string)
    element.click()


f = open("ferfi.txt", "r", encoding="utf8")
n = open("no.txt", 'r', encoding="utf8")
v = open("vezeteknev.txt", 'r', encoding="utf8")
k = open("kozep.txt", 'r', encoding='utf8')
ferfinevek = []
noinevek = []
vezeteknevek = []
kozep = []
for x in f:
    x = x.strip()
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
    x = x.strip()
    kozep.append(x)
k.close()

ferfie = False
vnev = ""
knev = ""
telszam = ""
email = ""

try:
    driver = webdriver.Chrome()
    driver.get('https://erp2.schonherz.hu/')
    # time.sleep(5)

    write("email", 'kvcsmate98@gmail.com')

    write("password", 'Selenium123')
    submit_btn = driver.find_element_by_class_name("btn")
    submit_btn.click()
    time.sleep(5)
except Exception as e:
    print(e)
    print('driver closing on error')
    time.sleep(10)
    driver.close()
while datetime.now()<runtime:
    try:
        driver.get('https://erp2.schonherz.hu/szemelyek')
        time.sleep(ltime)
        # új személy
        btn_click(" Új személy ")
        time.sleep(ltime)
        vnev = random.choice(vezeteknevek)
        write("lastName", vnev)
        knev = ""
        if random.randrange(2):
            knev = random.choice(ferfinevek)
            ferfie = True
        else:
            knev = random.choice(noinevek)
            ferfie = False
        write("firstName", knev)
        email = unidecode.unidecode(vnev.lower() + str(knev.lower()) + '@gmail.com')
        write("email", email)
        btn_click(" Mentés")
        counter += 1
        print(str(counter) + "  " + datetime.now().strftime("%H:%M:%S") + "-" + vnev + " " + knev)
        # szemelyek/id/szerkesztes
        telszam = '06' + str(random.randrange(1, 10)) + '0'
        for x in range(7):
            telszam += str(random.randrange(10))
        write("phoneNumber", telszam)
        driver.find_element_by_css_selector('[ng-reflect-name="sex"]').click()
        if ferfie:
            driver.find_element_by_css_selector('[ng-reflect-value="Férfi"]').click()
        else:
            driver.find_element_by_css_selector('[ng-reflect-value="Nő"]').click()

        szerkesztes_checkbox = ["Kért hírlevelet", "Azonnali kezdés", "Jogosítvány", "Üzemorvosi igazolása van"]
        for i in range(len(szerkesztes_checkbox)):
            if coinflip():
                checkbox(szerkesztes_checkbox[i])
        write("9", str(random.randrange(3)))
        write("11", lorem.sentence())
        btn_click("Mentés")
        time.sleep(ltime)

        add('Hívások ')
        dropdown("statusId")
        write('comment', lorem.sentence())
        btn_click(" Mentés")
        add("Iskolák ")
        school = not (dropdown("typeId") % 2)

        if school:
            ##  egyetem
            dropdown("universityId")
            write("education", 'BsC')
        else:
            ## középiskola
            write("name", random.choice(kozep))
            write("education", 'érettségi')

        ## kezdés éve: 900 570
        kezdes = random.randrange(2000, 2019)
        write("startYear", str(kezdes))
        befejezes = kezdes + 3 + random.randrange(2)
        write("endYear", str(befejezes))
        ## mentés
        btn_click(" Mentés")

        add("Nyelvtudás ")
        dropdown("languageId")
        dropdown("levelId")
        dropdown("usecaseId")
        checkbox("Tesztelve")
        write("comment", lorem.sentence())
        btn_click(" Mentés")

        root = 'https://erp2.schonherz.hu/szemelyek/' + get_id()
        driver.get(root + '/tesztek')

        btn_click("Hozzáadás")
        dropdown("typeId")
        write("result", str(random.randrange(100)))
        write("comment", lorem.sentence())
        btn_click(" Mentés")

        time.sleep(2)










    # print any exceptions such as element not found error, then close browser
    except Exception as e:
        print(e)
        exception_type, exception_object, exception_traceback = sys.exc_info()
        filename = exception_traceback.tb_frame.f_code.co_filename
        line_number = exception_traceback.tb_lineno

        print("Exception type: ", exception_type)
        print("File name: ", filename)
        print("Line number: ", line_number)
        time.sleep(10)
time.sleep(10)
driver.close()
