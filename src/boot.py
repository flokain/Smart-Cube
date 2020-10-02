# boot.py - - runs on boot-up
import time
import machine
import network
import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("networking")

wlan = network.WLAN(network.STA_IF)

# scan networks
networks = wlan.scan()
log.debug('scanning networks')
for n in networks:
    log.debug("SSID: {}".format(str(n[0].decode("utf-8"))))
# check if any of the found network SSID matches a stored config
# connect to network
# check internet access
# cant connect to any network launching Accesspoint
# start webserver

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('GLUBBE', 'GLUBBE0619')
        while not wlan.isconnected():
            pass
    print('network config: ', wlan.ifconfig())

do_connect()