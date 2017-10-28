#!/usr/bin/python
# -*- encoding: utf-8 -*-

import RPi.GPIO as GPIO
import time
Led = 9

# setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Led, GPIO.OUT) 

for i in range(3):
   GPIO.output(Led, True)
   time.sleep(1)
   GPIO.output(Led, False)
   time.sleep(1)
   GPIO.output(Led, True)
   
GPIO.output(Led, False)   