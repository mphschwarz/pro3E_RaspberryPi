#! /bin/sh
gpio mode 29 up
while true
do
        if [ `gpio read 29` = "0" ]
        then
                halt
        fi
done