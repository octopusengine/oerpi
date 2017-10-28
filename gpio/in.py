#!/usr/bin/python
# -*- encoding: utf-8 -*-

import RPi.GPIO as GPIO
import time

# nastaveni pinu GPIO8 (= hardwerovy pin24) na vstup a pripojeni vnitrniho Pull-Up odporu
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP) 

# nekonecna smycka pro cteni a zobrazovani aktualniho stavu portu
while True:    
  print GPIO.input(8)
  time.sleep(0.5)