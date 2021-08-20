import service as s
ferfie = False
vnev = ""
knev = ""
telszam = ""
email = ""

def szemely():
    try:
        s.driver.get('https://erp2.schonherz.hu/szemelyek')
        s.time.sleep(s.ltime)
        # új személy
        s.btn_click(" Új személy ")
        s.time.sleep(s.ltime)
        vnev = s.random.choice(s.vezeteknevek)
        s.write("lastName", vnev)
        knev = ""
        if s.random.randrange(2):
            knev = s.random.choice(s.ferfinevek)
            ferfie = True
        else:
            knev = s.random.choice(s.noinevek)
            ferfie = False
        s.write("firstName", knev)
        email = s.email(vnev,knev
                        )
        s.write("email", email)
        s.btn_click(" Mentés")
        s.counter +=1
        print(str(s.counter)+"  "+s.datetime.now().strftime("%H:%M:%S")+"-"+vnev+" "+knev)
        # szemelyek/id/szerkesztes
        telszam = '06' + str(s.random.randrange(1, 10)) + '0'
        for x in range(7):
            telszam += str(s.random.randrange(10))
        s.write("phoneNumber", telszam)
        s.driver.find_element_by_css_selector('[ng-reflect-name="sex"]').click()
        if ferfie:
            s.driver.find_element_by_css_selector('[ng-reflect-value="Férfi"]').click()
        else:
            s.driver.find_element_by_css_selector('[ng-reflect-value="Nő"]').click()

        szerkesztes_checkbox = ["Kért hírlevelet", "Azonnali kezdés", "Jogosítvány", "Üzemorvosi igazolása van"]
        for i in range(len(szerkesztes_checkbox)):
            if s.coinflip():
                s.checkbox(szerkesztes_checkbox[i])
        s.write("9", str(s.random.randrange(3)))
        eghatrany = ["szemüveges","mozgáskorlátozott","hallássérült","diszlexiás","színtévesztő","színvak","látássérült"]
        s.write("11", s.random.choice(eghatrany))
        s.btn_click("Mentés")
        s.time.sleep(s.ltime)
        for _ in range(s.random.randrange(3)):
            s.add('Hívások ')
            s.dropdown("statusId")
            s.write('comment',s.lorem.sentence())
            s.btn_click(" Mentés")
        for _ in range(s.random.randrange(1,3)):
            s.add("Iskolák ")
            school =  not (s.dropdown("typeId") % 2 )

            if school:
                ##  egyetem
                s.dropdown("universityId")
                s.write("education", 'BsC')
            else:
                ## középiskola
                s.write("name",s.random.choice(s.kozep))
                s.write("education", 'érettségi')

            ## kezdés éve: 900 570
            kezdes = s.random.randrange(2000, 2019)
            s.write("startYear", str(kezdes))
            befejezes = kezdes + 3 + s.random.randrange(2)
            s.write("endYear", str(befejezes))
            ## mentés
            s.btn_click(" Mentés")
        for _ in range(s.random.randrange(1,4)):
            s.add("Nyelvtudás ")
            s.dropdown("languageId")
            s.dropdown("levelId")
            s.dropdown("usecaseId")
            if s.coinflip():
                s.checkbox("Tesztelve")
            s.write("comment", s.lorem.sentence())
            s.btn_click(" Mentés")



        root = 'https://erp2.schonherz.hu/szemelyek/'+ s.get_id()
        s.driver.get(root+'/tesztek')

        for _ in range(s.random.randrange(5)):
            s.btn_click("Hozzáadás")
            s.dropdown("typeId")
            s.write("result",str(s.random.randrange(100)))
            s.write("comment",s.lorem.sentence())
            s.btn_click(" Mentés")
            s.time.sleep(2)
# print any exceptions such as element not found error, then close browser
    except Exception as e:
        print(e)
        exception_type, exception_object, exception_traceback = s.sys.exc_info()
        filename = exception_traceback.tb_frame.f_code.co_filename
        line_number = exception_traceback.tb_lineno

        print("Exception type: ", exception_type)
        print("File name: ", filename)
        print("Line number: ", line_number)
        s.time.sleep(10)
