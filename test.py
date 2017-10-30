#var/lib/mpd/playlists
# python test - raspberry + serialdisplay (arduino) 
# octopusengine.eu

import random, sys, os, time
from time import sleep
from gpio.octopusEngineHWlib import *
from gpiozero import LED
from time import sleep
from gpiozero import Button
from signal import pause

def goButt1():
    btx="Butt1"
    pip1()
    print(btx)
    sdRQC(5,btx,2)
    sleep(1)
    sdRQC(5,"",2)    

button1 = Button(21)
button1.when_pressed = goButt1
led = LED(9)



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
sdRQC(0,"RPi-test.py",7)
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

os.system("python /home/pi/gpio/oeoled.py OctopusEngine IP: "+txt)

#s.write("R7Q"+txt+"*")
sdRQC(2,txt,2)

#sdRQC(7,"temperature:",1)
     
#================================================
print "test ok - end"

tt=1
RunOk=True
while RunOk:
        if dallasTemp:
          t=getDallTemp()
        else:
          t=99
	print(str(t))
        sdRQC(8,"temp: "+str(t),2)
    
        #s.write("W3P")
        #s.write(str(int(tt/2)))
        #s.write(",")
        px=str(int(tt/2))
        py=150-t*2
	#s.write(str(gt))
	sdPXYC(px,py,3)

        time.sleep(1)
        tt=tt+1

        if tt>320: tt=1
        RunOk=False
  
pause()
