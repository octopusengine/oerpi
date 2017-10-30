import RPi.GPIO as GPIO
import time
 
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
#
import sys

from time import sleep

from octopusEngineHWlib import *

# print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
arg1 = str(sys.argv[1]) 
arg2 = str(sys.argv[2])
arg3 = str(sys.argv[3])


from time import sleep

from octopusEngineHWlib import *

#
#-------------------------main test --------------
if arg1=="c":
  s.write("C") #clear
  sdRQC(0,"Serial Display",7)
  s.write("h35")
  s.write("h200")
  sdRQC(10,"octopusengine.org",7)

  s.write("W5h150")

if arg1== "t":
  sdRQC(3,arg2,arg3)

sleep(1)

