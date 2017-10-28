import RPi.GPIO as GPIO
import time
 
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
#
import sys

# print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
arg1 = str(sys.argv[1]) 
arg2 = str(sys.argv[2])
arg3 = str(sys.argv[3])

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Raspberry Pi pin configuration:
RST = None
 
# 128x64 display with hardware I2C:
fontPath="/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf"
sans16 = ImageFont.truetype(fontPath, 16)
fontPath="/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Bold.ttf"
sans16b = ImageFont.truetype(fontPath, 16)

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
leftD = 0
topD = 7
displEn = True


def doOLEDiko(obrName):
  obr = pygame.image.load("iko/"+obrName)
  for x in range(128):
    for y in range(16):
         col = obr.get_at((x,y)) 
         if col[0]>7:
           draw.point((x,y),fill=0)
         else:
           draw.point((x,y),fill=255)         
  disp.image(image)
  disp.display()

def doOLEDinfo():
   for x in range(hA):
    for y in range(55,hB):
      if myMatrix[x,y]==7:
        draw.point((x,y),fill=255)
      else:
        draw.point((x,y),fill=0)
   disp.image(image)
   disp.display()

def doInfoBig(text):
  global dislpEn,tftEn
  if displEn:
    draw.rectangle((0,15,width,55), outline=0, fill=0)
    draw.text((leftD, topD+15),text,  font=sans16b, fill=255)
    disp.image(image)
    disp.display()
  else:
    print("Displ." + text)
  if tftEn:
    co="S"+text+"*"
    s.write(co)  

def doInfoBig2(text):
  global dislpEn,tftEn
  if displEn:
    draw.rectangle((0,15,width,55), outline=0, fill=0)
    draw.text((leftD, topD+33),text,  font=sans16, fill=255)
    disp.image(image)
    disp.display()
  else:
    print("Displ." + text)
  if tftEn:
    co="S"+text+"*"
    s.write(co)  


def doInfoBig12(text1,text2):
  global dislpEn
  if displEn:
    draw.rectangle((0,15,width,55), outline=0, fill=0)
    draw.text((leftD, topD+15),text1,  font=sans16b, fill=255)
    draw.text((leftD, topD+33),text2,  font=sans16, fill=255)
    disp.image(image)
    disp.display()
  else:
    print("Displ." + text1 + " # " + text2)

def doInfo3(text1,text2,text3):
  global dislpEn
  if displEn:
    #draw.rectangle((0,15,width,55), outline=0, fill=0)
    draw.text((leftD, topD),text1,  font=sans16, fill=255)
    draw.text((leftD, topD+19),text2,  font=sans16, fill=255)
    draw.text((leftD, topD+38),text3,  font=sans16, fill=255)
    disp.image(image)
    disp.display()
  else:
    print("Displ." + text1 + " # " + text2)

# -----------------------------------------------------Initialize library.
print("oled2 - start")
disp.begin()
 
# Clear display.
disp.clear()
disp.display()
 
# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
 
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
 
# Draw a black filled box to clear the image.
#draw.rectangle((0,0,width,height), outline=0, fill=0)
#time.sleep(3)

"""try:
    while 1:
        if GPIO.input(U_pin): # button is released
            draw.polygon([(20, 20), (30, 2), (40, 20)], outline=255, fill=0)  #Up
        else: # button is pressed:
            draw.polygon([(20, 20), (30, 2), (40, 20)], outline=255, fill=1)  #Up filled
 
        if GPIO.input(L_pin): # button is released
            draw.polygon([(0, 30), (18, 21), (18, 41)], outline=255, fill=0)  #left
        else: # button is pressed:
            draw.polygon([(0, 30), (18, 21), (18, 41)], outline=255, fill=1)  #left filled
 
        if GPIO.input(R_pin): # button is released
            draw.polygon([(60, 30), (42, 21), (42, 41)], outline=255, fill=0) #right
        else: # button is pressed:
            draw.polygon([(60, 30), (42, 21), (42, 41)], outline=255, fill=1) #right filled
 
        if GPIO.input(D_pin): # button is released
            draw.polygon([(30, 60), (40, 42), (20, 42)], outline=255, fill=0) #down
        else: # button is pressed:
            draw.polygon([(30, 60), (40, 42), (20, 42)], outline=255, fill=1) #down filled
 
        if GPIO.input(C_pin): # button is released
            draw.rectangle((20, 22,40,40), outline=255, fill=0) #center 
        else: # button is pressed:
            draw.rectangle((20, 22,40,40), outline=255, fill=1) #center filled
 
        if GPIO.input(A_pin): # button is released
            draw.ellipse((70,40,90,60), outline=255, fill=0) #A button
        else: # button is pressed:
            draw.ellipse((70,40,90,60), outline=255, fill=1) #A button filled
 
        if GPIO.input(B_pin): # button is released
            draw.ellipse((100,20,120,40), outline=255, fill=0) #B button
        else: # button is pressed:
            draw.ellipse((100,20,120,40), outline=255, fill=1) #B button filled
 
        # Display image.
"""
#draw.polygon([(20, 20), (30, 2), (40, 20)], outline=255, fill=0)        
#disp.image(image)
#disp.display()
#time.sleep(3)

#doInfoBig12("octopusengine.org","192.168.0.208")
#doInfoBig12(arg1,arg2)
doInfo3(arg1,arg2,arg3)

#print("finish - ok")

