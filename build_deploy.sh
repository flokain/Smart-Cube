#! /bin/bash
device=${SMART_CUBE_PORT:='/dev/ttyUSB0' }

docker run --rm -v $HOME:$HOME -u 1000 -w $PWD/misc/micropython/ports/esp8266/ larsks/esp-open-sdk make
esptool.py --port $device --baud 460800 write_flash --flash_size=detect 0 $PWD/misc/micropython/ports/esp8266/build-GENERIC/firmware-combined.bin
