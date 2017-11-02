#var/lib/mpd/playlists
# simple library for raspberry pi + serialdisplay (arduino) 
# 2013 basic test
# 2016/05
# 2017/10 RPI2/3 and 3DWARF shield
# octopusengine.org - FB/Instagram/...
# ------------------------------
import sys, os, subprocess, time
from socket import gethostname, gethostbyname #getIp
from time import sleep
from gpiozero import PWMLED
import RPi.GPIO as GPIO

COVER = 16
TOWER = 26
TANK = 21
PIEZ = 20
JMP1 = TOWER
RELE1=18

f1=1000
f2=2000
f1a=440
f2a=880
f3a=1760

pz = PWMLED(PIEZ)
pz.frequency = f1

#  ...
#       -   - GND
#  S 19 -   - 16 COVER
#  T 26 -   - 20 PIEZO
#   GND -   - 21 TANK
#       -----

# setup pins
# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM)
#GPIO.setup(BTNS1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
# GPIO.setup(COVER, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
# GPIO.setup(TOWER, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# GPIO.setup(RELE1, GPIO.OUT)# beep 
# GPIO.setup(PIEZ, GPIO.OUT)# beep 
# beep = GPIO.PWM(PIEZ, 1500)   

def isJmp1():
   if not GPIO.input(JMP1): return True
   else: return False     
   
def isJmp2():
   if not GPIO.input(COVER): return True
   else: return False 
   
 #----------------------------------------beep

#pip(1600,0.03) #first, after init 
#pip3x(2)
 
def pip(f,long):
  print ("beep")
  pz.value = 0.5
  pz.frequency=f1 
  sleep(0.1)
  pz.value = 0
     
def pip1():  
  print ("beep1")
  pz.value = 0.5
  pz.frequency=f2a
  sleep(0.1)
  pz.value = 0

def pip2():
  print ("beep2")
  pz.value = 0.5
  pz.frequency=f2a
  sleep(0.1)
  pz.value = 0
  sleep(0.5)
  pz.frequency=f3a
  pz.value=0.5
  sleep(0.1)
  pz.value = 0
  sleep(0.5)

def pip3x(x):
  for num in range(x):  
    pz.value = 0.5
    sleep(0.1)
    pz.value = 0
    sleep(1) 

# ======tft serial monitor====================
import serial
s = serial.Serial(port='/dev/ttyAMA0',baudrate=9600,                                                   
            timeout=3.0,
            xonxoff=False, rtscts=False, 
            writeTimeout=3.0,
            dsrdtr=False, interCharTimeout=None)
# ===============================================
def sdW(textString):    # simple command write  
  s.write(textString)   # 
  sleep(0.1)

def sdRQC(row,textString,col): # row position + string + color 
  lenLim = 25 #len limit for standard font size
  s.write("W"+str(col)) # set color W or c
  s.write("R"+str(row)) 
  s.write("Q"+textString[:lenLim]+"*")   # Q string *
  sleep(0.1)
  
def sdArrQ(rStart,arrText):  # block of text (several lines) from row position / last set color 
   rr=rStart
   for row in (arrText):
     sdRQC(rr,row,1)
     rr=rr+1  
  
def sdPXYC(px,py,col): # pixel x,y + color  
  s.write("W"+str(col)) # set color W or c
  s.write("P"+str(px)) 
  s.write(","+str(py)) 
  sleep(0.05)

def sdPXY(px,py): # pixel x,y  
  s.write("P"+str(px)) 
  s.write(","+str(py)) 
  sleep(0.001)

def sdpXY(px,py): # pixel x,y  
  s.write("p"+str(px)) 
  s.write(","+str(py)) 
  sleep(0.0001)
  
#======get IP ============================
def getIp():
   try:
    arg='ip route list'
    p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
    data = p.communicate()
    split_data = data[0].split()
    ipaddr = split_data[split_data.index('src')+1]
   except:
     ipaddr ="ip.Err"
   #print "ip: " ip
   return ipaddr

#====== get procesor temp ============================
def getProcTemp():  
   try:
     pytemp = subprocess.check_output(['vcgencmd', 'measure_temp'], universal_newlines=True)
     #ipoutput = subprocess.check_output(['vcgencmd measure_temp'], universal_newlines=True, 'w'))
     #print pytemp 
     eq_index = pytemp.find('=')+1 
     #if eq_index>0:
     var_name = pytemp[:eq_index].strip()
     value = pytemp[eq_index:eq_index+4]
     numvalue=float(value)
   except:
     numvalue = -1
   return numvalue 


# ====== get dallas temp ===============================
#sudo nano /boot/config.txt >> dtoverlay=w1-gpio,gpiopin=4
try:
 import glob 
 os.system('modprobe w1-gpio')
 os.system('modprobe w1-therm')
 
 base_dir = '/sys/bus/w1/devices/'
 device_folder = glob.glob(base_dir + '28*')[0]
 device_file = device_folder + '/w1_slave'

except:
 err=True
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def getDallTemp(): #get dallas senson temperature
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.1) #0.2 ok
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        #return temp_c, temp_f
        return float(int(temp_c*10))/10

#-------------------------end --------------
