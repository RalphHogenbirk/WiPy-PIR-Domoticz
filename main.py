import time
from network import WLAN
from machine import Pin
from domoticz import Domoticz

wl = WLAN(WLAN.STA)
d = Domoticz("<ip>", 8080 ,"<basic hash>")

#flags
running = True
button_pressed = False
pir_triggered = False

#callbacks
def pirTriggered(pin):
    global pir_triggered
    pir_triggered = True

def buttonPressed(pin):
    global button_pressed
    button_pressed = True


pir = Pin('GP4',mode=Pin.IN,pull=Pin.PULL_UP)
pir.irq(trigger=Pin.IRQ_RISING, handler=pirTriggered)
    
pir = Pin('GP17',mode=Pin.IN,pull=Pin.PULL_UP)
pir.irq(trigger=Pin.IRQ_FALLING, handler=buttonPressed)

# main loop
print("Starting main loop")
while running:
    time.sleep_ms(500)
    if pir_triggered:
        pir_triggered = False
        result = d.setVariable('Presence:LivingRoom','1')
        print("HTTP Status: "+str(result))
    elif button_pressed:
        button_pressed = False
        running = False

print("Exited main loop")
