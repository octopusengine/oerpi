#!/usr/bin/env python
import smbus
import time
import datetime
import os
import sys

#==============================================================
#  Program pro ovladani RTC obvodu PCF8563 pres I2C komunikaci
#==============================================================

bus = smbus.SMBus(1)   #  novejsi varianta RasPi (512MB) 
#bus = smbus.SMBus(0)   #  starsi varianta RasPi (256MB) 


adr =0x51       # I2C adresa obvodu PCF8563

#=============================================
# podprogram pro ulozeni systemoveho casu z RasPi do RTC obvodu
def rtc_zapis():
  
  bus.write_byte_data(adr,0x0D,0b10000011)   # 1Hz vystup
  bus.write_byte_data(adr,0x00,0)            # normalni rezim pocitani casu
  
  # cas se d RTC uklada prepocteny na GMT casovou zonu
  datcas = datetime.datetime.utcnow()    # zjisteni aktualniho casu v RasPi (prepocteno na GMT casovou zonu)
  

  # roky 00 az 99 - registr 0x08
  rokhi = int((datcas.year - 2000) / 10)
  roklo = datcas.year - 2000 - (10 * rokhi)
  bus.write_byte_data(adr,0x08,(rokhi*16) + roklo)
  
  
  # mesice a rozlisovaci bit pro stoleti - registr 0x07
  meshi = int((datcas.month) / 10)
  meslo = datcas.month - (10 * meshi)
  if datcas.year > 1999:
    stoleti = 0
  else:
    stoleti = 128
  bus.write_byte_data(adr,0x07,(meshi*16) + meslo + stoleti)
  
  
  # dny v tydnu - registr 0x06
  # funkce weekday v pythonu vraci 0=pondeli ... 6=nedele
  dvt = datetime.datetime.utcnow().weekday() 
  bus.write_byte_data(adr,0x06,dvt)
  
  
  # dny v mesici - registr 0x05
  denhi = int(datcas.day / 10)
  denlo = datcas.day - (10 * denhi)
  bus.write_byte_data(adr,0x05,(denhi*16) + denlo)
  

  # hodiny - registr 0x04
  hodhi = int(datcas.hour / 10)
  hodlo = datcas.hour - (10 * hodhi)
  bus.write_byte_data(adr,0x04,(hodhi*16) + hodlo)
  
  
  # minuty - registr 0x03  
  minhi = int(datcas.minute / 10)
  minlo = datcas.minute - (10 * minhi)
  bus.write_byte_data(adr,0x03,(minhi*16) + minlo)
  
  
  # sekundy - registr 0x02
  # zaroven se zapisem sekund do RTC se nuluje bit pro testovani napeti baterie
  sekhi = int(datcas.second / 10)
  seklo = datcas.second - (10 * sekhi)
  bus.write_byte_data(adr,0x02,(sekhi*16) + seklo)

  print "Systemovy cas v RasPi :" , datcas , "UTC"
  print "Systemovy cas byl prekopirovan do RTC obvodu."
 


#=============================================
# podprogram pro zjisteni casu v obvodu RTC a jeho zobrazeni, nebo nastaveni casu v RasPi podle RTC
def rtc_info(nastav_cas=False):

  # nazevdne se prizpusobuje Pythonu - funkci weekday   (0=pondeli .... 6=nedele)
  #     (RTC obvod by mel podle kat.listu ty dny posunute)
  nazevdne = ['pondeli' , 'utery' , 'streda' , 'ctvrtek' , 'patek' , 'sobota' , 'nedele' ]
  
  datcas = datetime.datetime.utcnow()   # datcas bude obsahovat aktualni datum a cas v UTC (GMT)
  print "Systemovy cas v RasPi :" , datcas , "UTC"

  
  rtc =  bus.read_i2c_block_data(adr,0x00)

  sek = ((rtc[0x02] & 0b01110000)>>4) *10 + (rtc[0x02] & 0b00001111)   # sekundy
  min = ((rtc[0x03] & 0b01110000)>>4) *10 + (rtc[0x03] & 0b00001111)   # minuty
  hod = ((rtc[0x04] & 0b00110000)>>4) *10 + (rtc[0x04] & 0b00001111)   # hodiny
  den = ((rtc[0x05] & 0b00110000)>>4) *10 + (rtc[0x05] & 0b00001111)   # dny v mesici

  dvt = (rtc[0x06] & 0b00000111)                                  # den v tydnu : 0=Po  1=Ut ..... 6=Ne

  mes = ((rtc[0x07] & 0b00010000)>>4) *10 + (rtc[0x07] & 0b00001111)   # mesic
  rok = ((rtc[0x08] & 0b11110000)>>4) *10 + (rtc[0x08] & 0b00001111)   # rok

  
  
  napeti = ( (rtc[0x02] & 0b10000000))        # v nejvyssim bitu registru c.0 je informace o napeti
  if  napeti == 0 :
    napeti = "Napeti je OK"
  else:
    napeti = "Napeti kleslo pod predepsanou uroven"
  
    
  stoleti = ((rtc[0x07] & 0b10000000))        # v nejvyssim bitu registru c.7 je informace o stoleti 20. nebo 21.
  if  stoleti == 0 :
    stoleti = 2000
  else:
    stoleti = 1900
 
  txtcas = str(hod) + ":" + str(min).rjust(2,"0") + ":"  + str(sek).rjust(2,"0")
  txtdat = str(nazevdne[dvt]) + "  " +  str(den) + "." + str(mes) + "." + str(stoleti + rok) + " " 
  print "Cas v RTC:  " + txtdat + "  " + txtcas + " UTC" 
  
  
  
  if (nastav_cas == True):  # pokud je parametr tohoto podprogramu True, nastavi se RasPi podle RTC
    print "Cas v RasPi byl nastaven na:"
    prikaz="sudo date -u " + (str(mes).rjust(2,"0") +
                              str(den).rjust(2,"0") +
                              str(hod).rjust(2,"0") + 
                              str(min).rjust(2,"0") + 
                              str(stoleti + rok) + "." + 
                              str(sek).rjust(2,"0"))
    os.system (prikaz)






#=============================================
#  ***** hlavni program *****
#=============================================



# vyhodnoceni predavaneho parametru pri spousteni programu
try:                      # odchytavani chyby, ktera by vznikla pri chybejicim parametru
  akce = sys.argv[1]      # parametr spousteneho programu do promenne "akce"
except:                   # kdyz parametr chybi, je nahrazen prazdnym retezcem
  akce=""

akce = akce.lower()       # prevod parametru na mala pismena

# rozeskoky pri ruznych akcich
if (akce == "-i"):        # jen zobrazeni casu v RasPi a RTC
  rtc_info()
  
elif (akce == "-pi2rtc"): # zapis casu do RTC obvodu podle RasPi
  rtc_zapis()

elif (akce == "-rtc2pi"): # nastaveni RasPi podle RTC
  rtc_info(True)



else:                              # pri jakemkoli jinem parametru se zobrazi napoveda
  print "Pripustne parametry:"
  print "... -i        INFO - Jen zobrazi cas v RasPi a v RTC"
  print "... -pi2rtc   Zapise cas z RasPi do RTC"
  print "... -rtc2pi   Zapise cas z RTC do RasPi"
  
