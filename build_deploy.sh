#! /bin/bash

docker run --rm -v $HOME:$HOME -u 1000 -w $PWD/misc/micropython/ports/esp8266/ larsks/esp-open-sdk make
esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 $PWD/misc/micropython/ports/esp8266/build-GENERIC/firmware-combined.bin

