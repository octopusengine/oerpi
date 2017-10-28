#!/usr/bin/python
# -*- encoding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


# priklad na rozkmitani pinu GPIO8 frekvenci 2Hz se stridou 30%
pin = 8                               # GPIO8 (= hardwerovy pin24)
frekvence = 2                         # frekvence signalu = 2 Hz
strida = 30                           # signal bude 30% casu v logicke "1" a 70% casu v logicke "0"
GPIO.setup(pin, GPIO.OUT)             # GPIO8 prepne na vystup
signal1 = GPIO.PWM(pin , frekvence)   # nastaveni pinu do PWM vystupniho rezimu 
signal1.start(strida)                 # spusteni signalu


# jiny priklad na vedlejsim GPIO pinu (frekvence 5Hz, strida 80%)
pin = 7                               # GPIO8 (= hardwerovy pin26)
frekvence = 5                         # frekvence signalu = 5 Hz
strida = 80                           # signal bude 80% casu v logicke "1" a 20% casu v logicke "0"
GPIO.setup(pin, GPIO.OUT)             # GPIO8 prepne na vystup
signal2 = GPIO.PWM(pin , frekvence)   # nastaveni pinu do PWM vystupniho rezimu 
signal2.start(strida)                 # spusteni signalu



time.sleep(5)
signal1.stop()     # po 5 sekundach se prvni signal zastavi

time.sleep(2)     
signal2.stop()     # po dalsich dvou sekundach se zastavi i druhy signal