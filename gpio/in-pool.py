#!/usr/bin/python
# -*- encoding: utf-8 -*-

import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP) 

print "cekam na stisk tlacitka"
GPIO.wait_for_edge(8, GPIO.FALLING)
print "tlacitko bylo stisknuto"