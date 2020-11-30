#! /bin/sh
device=${SMART_CUBE_PATH:='/dev/ttyUSB0' }
device_group=$(stat -c "%g" $device)

docker run --rm -v $PWD/misc/micropython:/micropython -u 1000 -w /micropython/mpy-cross/ larsks/esp-open-sdk make
docker run --rm -v $PWD/misc/micropython:/micropython -u 1000 -w /micropython/ports/esp8266/ larsks/esp-open-sdk make clean
docker run --rm -v $PWD/misc/micropython:/micropython -u 1000 -w /micropython/ports/esp8266/ larsks/esp-open-sdk make
docker run --rm --device=$device -v $PWD/misc/micropython:/micropython -u 1000:$device_group -w /micropython/ports/esp8266/ --entrypoint="/bin/sh" larsks/esp-open-sdk -c "esptool.py --port=$device erase_flash"
docker run --rm --device=$device -v $PWD/misc/micropython:/micropython -u 1000:$device_group -w /micropython/ports/esp8266/ --entrypoint="/bin/sh" larsks/esp-open-sdk -c "esptool.py --port=$device --baud=460800 write_flash --flash_size detect 0 build-GENERIC/firmware-combined.bin"

