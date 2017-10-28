

gpio-admin export 4
echo out > /sys/devices/virtual/gpio/gpio4/direction
echo 1 > /sys/devices/virtual/gpio/gpio4/value

echo 0 > /sys/devices/virtual/gpio/gpio4/value
gpio-admin unexport 4

gpio-admin export 21
cat /sys/devices/virtual/gpio/gpio21/value

gpio-admin unexport 21