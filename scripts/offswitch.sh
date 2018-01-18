#! /bin/sh
gpio mode 29 up
gpio mode 28 out
gpio write 28 1
while true
do
        if [ `gpio read 29` = "0" ]
        then
                gpiowrite 28 0
                halt
        fi
done