import service as s


def ugyfel():
    try:
        s.driver.get("https://erp2.schonherz.hu/ugyfelek")
        s.btn_click(" Új ügyfél ")
        cegnev = s.random.choice(s.cegek)
        s.counter+=1
        print(str(s.counter) + "  " + s.datetime.now().strftime("%H:%M:%S") + "-" + cegnev)
        s.write("name",cegnev)
        s.write("taxNumber",s.adoszam())

        vevo = s.coinflip()
        if vevo:
            s.checkbox("Vevő")
        else:
            s.checkbox("Szállító")
        s.btn_click(" Mentés")
        s.write("groupTaxNumber",s.adoszam())
        s.write("registrationNumber",s.szamsor(10))
        s.place("Székhely")
        s.place("Levelezési cím")

        try:
            string = '[ng-reflect-name="salesId"]'
            element_present = s.EC.presence_of_element_located((s.By.CSS_SELECTOR, string))
            s.WebDriverWait(s.driver, s.timeout).until(element_present)
        except:
            print("Timed out waiting for page to load")
        element = s.driver.find_element_by_css_selector(string)
        element.click()
        s.time.sleep(s.ltime)
        selectOptions = s.driver.find_elements_by_xpath("//mat-option[@role = 'option']")
        element.send_keys("K")
        s.time.sleep(s.ltime)
        for _ in range(0, 3):
            element.send_keys(s.Keys.DOWN)
            s.time.sleep(0.1)
        element.send_keys(s.Keys.SPACE)

        s.dropdown("channelId")
        s.write("clientInfo",s.lorem.sentence())

        if s.coinflip():
            s.checkbox("E-számla")
            s.time.sleep(s.ltime)
            s.write("electronicInvoiceEmail1",cegnev.split()[0]+"@mail.com")
            if s.coinflip():
                s.write("electronicInvoiceEmail2", cegnev.split()[0] + "@mail2.com")



        if s.coinflip():
            s.checkbox("home office ")

        if s.coinflip():
            s.checkbox("Auto")

        s.label()

        s.btn_click("Mentés")

        id= s.get_id()

        s.add("Besorolás ")
        s.dropdown("year")
        s.btn_click(" Mentés")

        s.driver.get("https://erp2.schonherz.hu/ugyfelek/"+id+"/kontaktok")
        for _ in range(s.random.randrange(2,5)):
            s.btn_click("Hozzáadás")
            knev=s.random.choice(s.ferfinevek+s.noinevek)
            vnev=s.random.choice(s.vezeteknevek)
            s.write("name",vnev+" "+knev)
            s.write("phoneNumber",s.telszam())
            s.write("email",s.email(vnev,knev))
            s.write("title",s.random.choice(s.titulusok))
            s.write("comment",s.lorem.sentence())
            s.label()
            s.btn_click(" Mentés")

        s.driver.get("https://erp2.schonherz.hu/ugyfelek/"+id+"/szerzodesek")


        for _ in range(s.random.randrange(1,5)):
            s.btn_click("Hozzáadás")
            s.write("name",s.word())
            s.dropdown("typeId")
            date= s.date()
            s.write("startDate",date[0])
            s.write("endDate",date[1])
            s.checkbox("Folyamatos?")
            s.write("paymentDeadline",str(s.random.randrange(30)))
            s.write("link","https://erp2.schonherz.hu/ugyfelek/"+id+"/szerzodesek")
            s.btn_click(" Mentés")


        for _ in range(s.random.randrange(5)):
            s.driver.get("https://erp2.schonherz.hu/ugyfelek/" + id + "/virtualis-tig-sablon")
            s.btn_click("Hozzáadás")
            s.write("name",s.word())
            s.write("invoiceComment",s.lorem.sentence())
            s.write("comment",s.lorem.sentence())
            s.btn_click(" Mentés")

        s.driver.get("https://erp2.schonherz.hu/ugyfelek/"+id+"/megrendelesek")
        s.btn_click("Hozzáadás")
        s.write("name",s.word())
        s.dropdown("typeId")
        s.dropdown("officeId")
        s.dropdown("contractId")
        s.btn_click(" Mentés")


        s.time.sleep(5)
        id = s.get_id()

        s.driver.get("https://erp2.schonherz.hu/megrendelesek/"+id+"/reszletek")
        if s.coinflip():
            s.btn_click("Aktiválás")
            s.btn_click(" Igen")
        if s.coinflip():
            s.btn_click("Lezárás")
            s.dropdown("id")
            s.write("name",s.lorem.sentence())
            s.btn_click(" Mentés")
        for _ in range(s.random.randrange(5)):
            s.driver.get("https://erp2.schonherz.hu/megrendelesek/"+id+"/hirdetesek")
            s.btn_click("Új hirdetés")
            s.write("name",s.random.choice(s.munkak))
            s.btn_click(" Mentés")




        for _ in range(s.random.randrange(5)):
            s.driver.get("https://erp2.schonherz.hu/megrendelesek/" + id + "/dolgozok")
            s.btn_click("Új dolgozó")
            s.write("idSearch",str(s.random.randrange(10,5000)))
            s.btn_click(" Keresés")
            s.time.sleep(2)
            s.label()
            s.write("start",s.date()[0])
            s.btn_click(" Mentés")
            s.time.sleep(s.ltime)
            if s.coinflip():
                s.btn_click("Új szakmai gyakorlat")
                s.label()
                s.write("startDate",s.date()[0])
                s.write("targetHours",str(s.random.randrange(20,41)))
                s.btn_click(" Mentés")
    except Exception as e:
        print(e)
        s.time.sleep(10)

