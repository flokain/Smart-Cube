#! /bin/sh
device=${SMART_CUBE_PATH:='/dev/ttyUSB0' }
device_group=$(stat -c "%g" $device)

# TODO: overwrite  changes in the firmware files

# for more ram  
# in main.c STATIC char heap[44 * 1024];
sed -i 's/STATIC char heap.*/STATIC char heap[44 * 1024];/g' $PWD/misc/micropython/ports/esp8266/main.c
# for more firmware storage  
# in esp8266.ld   irom0_0_seg :  org = 0x40209000, len = 0xa7000
sed -i 's/    irom0_0_seg :  org = 0x40209000, len = .*/    irom0_0_seg :  org = 0x40209000, len = 0xa7000/g' $PWD/misc/micropython/ports/esp8266/boards/esp8266.ld
# for bigger buffer for TLS can be parsed to Makefile. TODO: #16 test https calls with the new firmware
# in Makefile AXTLS_DEFS_EXTRA = -Dabort=abort_ -DRT_MAX_PLAIN_LENGTH=1024 -DRT_EXTRA=8192

# add project libraries to the module folder
micropython -m upip install -p $PWD/misc/micropython/ports/esp8266/modules/ -r requirements.txt
cp -r $PWD/misc/micropython-wifimanager/wifi_manager $PWD/misc/micropython/ports/esp8266/modules/
cp -r $PWD/misc/tinyweb/tinyweb $PWD/misc/micropython/ports/esp8266/modules/
rm -r $PWD/misc/micropython/ports/esp8266/modules/smartcube
cp -r $PWD/src/smartcube $PWD/misc/micropython/ports/esp8266/modules/

docker run --rm -v $PWD/misc/micropython:/micropython -u 1000 -w /micropython/mpy-cross/ larsks/esp-open-sdk make
docker run --rm -v $PWD/misc/micropython:/micropython -u 1000 -w /micropython/ports/esp8266/ larsks/esp-open-sdk make AXTLS_DEFS_EXTRA="-Dabort=abort_ -DRT_MAX_PLAIN_LENGTH=1024 -DRT_EXTRA=8192"
docker run --rm --device=$device -v $PWD/misc/micropython:/micropython -u 1000:$device_group  -w /micropython/ports/esp8266/ larsks/esp-open-sdk make PORT=$device BAUD=460800 deploy
