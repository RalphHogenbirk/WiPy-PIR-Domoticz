import time
from network import WLAN
from machine import Pin
from domoticz import Domoticz

wl = WLAN(WLAN.STA)
d = Domoticz("<ip>", 8080 ,"<basic hash>")

#config
hold_time_sec = 10

#flags
last_trigger = -10 

pir = Pin('G4',mode=Pin.IN,pull=Pin.PULL_UP)

# main loop
print("Starting main loop")
while True:
    if pir() == 1:
        if time.time() - last_trigger > hold_time_sec:
            last_trigger = time.time()
            print("Presence detected, sending HTTP request")
            try:
                return_code = d.setVariable('Presence:LivingRoom','1')
                print("Request result: "+str(return_code))
            except Exception as e:
                print("Request failed")
                print(e)
    else:
        last_trigger = 0
        print("No presence")

    time.sleep_ms(500)

print("Exited main loop")
