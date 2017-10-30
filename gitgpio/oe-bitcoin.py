import time
import urllib2
import json
from octopusEngineHWlib import *

print "octopusengine/api ---"

tim = urllib2.urlopen("http://www.octopusengine.eu/api/datetime.php").read()
print "datetime >>>"
print str(tim)


s.write("C") #clear
sdRQC(0,"today BITCOIN graph",7)
s.write("h35")
s.write("h200")
sdRQC(10,"octopusengine.org",7)

#s.write("W5h150")

sleep(1)

print "bitcoin: bitstamp ---"

bcfile = urllib2.urlopen("https://www.bitstamp.net/api/ticker/").read()
print "ticker >>>"
jObj = json.loads(bcfile)

#print str(jObj["timestamp"])
#print str(jObj["last"])

def bc2gr(bc):
  gr=(bc-4000)/20
  return (gr)

tt=1
nas=20 #3 ok 
sy=200

s.write("W8") # blue horizontal lines 300, 400, 600, 700
for ha in range(4000,8000,1000):
	s.write("h")
	hg=str(sy-bc2gr(ha))
	s.write(hg)
	time.sleep(0.2)

s.write("W3") # red horizontal line 500
s.write("h")
hg=str(sy-bc2gr(5000))
s.write(hg)

s.write("W3") # 
for kurz in range(900):
  try:
    jObj = json.loads(urllib2.urlopen("https://www.bitstamp.net/api/ticker/").read())
    
    lastNum =int(float(jObj["last"]))
    sdRQC(2,str(jObj["last"])+ " USD/BTC",2)
    
    px=str(int(tt/nas))
    py=sy-bc2gr(lastNum) 
    print tt, lastNum, py

    sdPXYC(px,py,2) # send one x,y point to display
  except:
   print "net.err"  
    
  time.sleep(30)
  tt +=1



