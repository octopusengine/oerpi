#!/bin/bash
#oe / octopusengine 2015-17
#wget https://raw.githubusercontent.com/octopusengine/linux/master/sh/oe.sh
#chmod 755 ../oe.sh

okEnd() {
  echo -n "end > "
  i=0
  while [ "$i" -le 16 ]; do
    i=$((i + 1))
    echo -n "."
    sleep 0.1
  done
  echo; echo "OK"
}

echo
if [[ $1 = "h" ]]; then
  echo "----- octopus engine help -----"
  echo "$1 h(help) / c(clear) / i(info)"
  echo "$2 m(raM/HD) / b(btc/ltc) / c(crypto test)"
fi

if [[ $1 = "c" ]]; then
  echo "----- octopus engine -----"
  clear  
fi

if [[ $1 = "i" ]]; then
  echo "----- octopus engine info -----"
  uname -a
  w=whoami
  echo "whoami > `$w`" 
  d=pwd
  echo "pwd > `$d`"
  #r=$(which)
  r=which
  echo "which > `$r`"
  sleep 1s  
fi

price1=123
if [[ $2 = "b" ]]; then
  echo "----- BTC/LTC -----"
  price1=$(wget -qO- https://www.bitstamp.net/api/v2/ticker/btcusd/ | grep -E -o 'last": "[0-9.]+"' | grep -E -o '[0-9]+.[0-9]{2}')
  echo "$price1 BTC/USD"
  sleep 1s
  price2=$(wget -qO- https://api.bitfinex.com/v1/pubticker/ltcusd | grep -E -o 'last_price":"[0-9.]+"' | grep -E -o '[0-9.]+')
  echo "$price2 LTC/USD"
  #price3=$(wget -qO- https://api.bitfinex.com/v1/pubticker/vtcusd | grep -E -o 'last_price":"[0-9.]+"' | grep -E -o '[0-9.]+')
  #echo "$price3 VTC/USD"
  sleep 1s
  python oeoled.py Octopus_engine $price1 $price2
fi

if [[ $2 = "c" ]]; then
  echo "----- crypto -----"
  echo -n "Test Hash" | sha256sum 
  i=0; while ! (echo -n "OctopusEngine$i" | sha256sum | tr -d "\n"; echo " (nonce=$i)")|grep -E "^00"; do let i++; done  
fi

if [[ $2 = "m" ]]; then
  echo "----- memory RAM..HD -----"
  echo "free>"
  free
  echo "dp -h>"
  df -h
fi

#if [[ $(which toilet) = "" ]]; then
#                echo $price
#        else
#toilet -t -f bigascii12 $price
#fi
#echo $x

#toilet -t -f bigascii12 $price1

okEnd
