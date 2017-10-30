# menu (serial Display / oled / ...)
# python test - raspberry + DWARF shield + serialdisplay (arduino) 
# octopusengine.org

import random, sys, os, time
from time import sleep
from gpio.octopusEngineHWlib import *

from gpiozero import LED
from gpiozero import Button
from signal import pause

butNum=0
menuMax=10

def goButt1():
    global butNum
    butNum=butNum+1
    if (butNum==menuMax):
      butNum=1 
    btx="Menu: "+str(butNum)
    print(btx)
    sdRQC(7,btx,2)
    pip1()    
   
button1 = Button(21) #DW.TAN
button1.when_pressed = goButt1
led = LED(9) #DW.Led

pip2()
led.on()
sleep(0.3)
led.off()

serialDisp=True
oledDispl=False
dallasTemp=False
# 
#-------------------------main test --------------
s.write("C") #clear
sdRQC(0,"RPi-test: menu.py",7)
s.write("h35")
s.write("h200")
sdRQC(10,"octopusengine.org",7)

s.write("W5h150")
if oledDispl:
  os.system("python /home/pi/gpio/oeoled.py OctopusEngine IP: ...")

for delta in range (0,10):
  led.on()
  sleep(0.1)
  led.off()
  sleep(0.2)

pip1()

#sdRQC(2,"raspberry pi test",1)
#sdRQC(4,"IP addres:",1)
#sleep(1)

txt="> ip: "+getIp()
print txt
  
pause()
