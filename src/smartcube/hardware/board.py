import gc
import os
import logging
import network
import machine
from wifi_manager import WifiManager


log = logging.getLogger(__name__)


class Board:

    pins = {2: "D4", 4: "D2", 5: "D1", 12: "D6", 13: "D7", 14: "D5", 15: "D8", 16: "D0"}

    def __init__(self, device):
        # Set all pins to OUT m od
        log.debug("initalizing board %s", device)
        if hasattr(machine, "Pin"):
            for p, d in self.pins.items():
                machine.Pin(p, machine.Pin.OUT)

        log.debug("free memory: %s", gc.mem_free())
        WifiManager.start_managing()
        log.debug("Wifi config loaded")
        log.debug("free memory: %s", gc.mem_free())

    @property
    def memory(self):
        return {
            "mem_alloc": gc.mem_alloc(),
            "mem_free": gc.mem_free(),
            "mem_total": gc.mem_alloc() + gc.mem_free(),
        }

    @property
    def storage(self):
        return {
            "flash_total": (os.statvfs("//")[0] * os.statvfs("//")[2]) / 1048576,
            "flash_free": (os.statvfs("//")[0] * os.statvfs("//")[3]) / 1048576,
            "flash_alloc": (os.statvfs("//")[0] * os.statvfs("//")[2]) / 1048576 - (os.statvfs("//")[0] * os.statvfs("//")[3]) / 1048576,
        }

    @property
    def network(self):
        sta_if = network.WLAN(network.STA_IF)
        ifconfig = sta_if.ifconfig()
        return {
            "ip": ifconfig[0],
            "netmask": ifconfig[1],
            "gateway": ifconfig[2],
            "dns": ifconfig[3],
        }

    def Pin(self, id: int):
        return machine.Pin(id)