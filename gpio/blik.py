#!/usr/bin/python
# -*- encoding: utf-8 -*-

import RPi.GPIO as GPIO
import time

# nastaveni pinu GPIO8 (= hardwerovy pin24) na vystup 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(8, GPIO.OUT) 

# rozsviceni LED (nastaveni pinu na logickou "1")
GPIO.output(8, True)

time.sleep(5)

# zhasnuti LED (nastaveni pinu na logickou "0")
GPIO.output(8, False)