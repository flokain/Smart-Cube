# Sources:
https://github.com/BradenM/micropy-cli
http://micropython.org/webrepl/#192.168.0.157:8266/
http://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#
https://github.com/belyalov/tinyweb
https://github.com/mcauser/awesome-micropython (list o fmicropython libraries)

https://www.codeply.com/p?starter=Bootstrap%204 (bootstrap online editor)
# reset board from comandline
```
esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 ~/Arduino/smartcube/micropython/bin/esp8266-20200911-v1.13.bin 
```

pymakr.json needs to accept gz file on upload