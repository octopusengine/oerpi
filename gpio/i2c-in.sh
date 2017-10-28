#!/bin/sh

# podle verze vaseho raspicka si zmente cislo i2c kanalu

sudo i2cset -y 0 0x20 0x01 0xFF   # Starsi verze RasPi (256MB) 
#sudo i2cset -y 1 0x20 0x01 0xFF  # Novejsi verze RasPi (512MB)


while [ True ]
do

  tlf=""   # tlacitko F1
  tlu=""   # tlacitko NAHORU (Up)
  tli=""   # tlacitko INSERT
  tll=""   # tlacitko VLEVO (Left)
  tld=""   # tlacitko DOLU (Down)
  tlr=""   # tlacitko VPRAVO (Right)

  stavgpb=`sudo i2cget -y 0 0x20 0x13` # Starsi verze RasPi (256MB) 
  #stavgpb=`sudo i2cget -y 1 0x20 0x13` # Novejsi verze RasPi (512MB)


  if [ $(($stavgpb & 128)) -eq "0" ]; then tlf="F1" ;fi
  if [ $(($stavgpb & 64)) -eq "0" ]; then tlu="Nahoru" ;fi
  if [ $(($stavgpb & 32)) -eq "0" ]; then tli="Insert" ;fi
  if [ $(($stavgpb & 16)) -eq "0" ]; then tll="Vlevo" ;fi
  if [ $(($stavgpb & 8)) -eq "0" ]; then tld="Dolu" ;fi
  if [ $(($stavgpb & 4)) -eq "0" ]; then tlr="Vpravo" ;fi


  echo " Stisknuta tlacitka : "  $tlf  $tlu  $tli  $tll  $tld  $tlr

  sleep 0.5

done