import service as s
import ugyfel_selenium as ugyfel
import szemely_selenium as szemely
from datetime import datetime,timedelta

worktime = 8
shift_end= datetime.now()+timedelta(hours=worktime)
while datetime.now()<shift_end:
    print(s.datetime.now().strftime("%H:%M:%S")+": új kör")
    multiplier = s.random.randrange(1,20)
    switcher = s.random.randrange(3)
    for _ in range(multiplier):
        if switcher == 0:
            szemely.szemely()
        elif switcher == 1:
            ugyfel.ugyfel()
        else:
            s.time.sleep(5)
            print("zZz")

s.driver.close()