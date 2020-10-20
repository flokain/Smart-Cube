import network, os, machine, gc
import logging
log = logging.getLogger(__name__)


class Hardware:

    pins = {2: "D4", 4: "D2", 5: "D1", 12: "D6", 13: "D7", 14: "D5", 15: "D8", 16: "D0"}
    device = "ESP8266"

    def __init__(self,device):
        # Set all pins to OUT m od
        log.debug("initalizing hardware for %s", self.device)
        if hasattr(machine, "Pin"):
            for p, d in pins.items():
                machine.Pin(p, machine.Pin.OUT)

    @property
    def memory(self):
        return
        {
            "allocated": gc.mem_alloc(),
            "free": gc.mem_free(),
            "total": gc.mem_alloc() + gc.mem_free(),
        }

    @property
    def storage(self):
        return
        {
            "flash_total": (os.statvfs("//")[0] * os.statvfs("//")[2]) / 1048576,
            "flash_free": (os.statvfs("//")[0] * os.statvfs("//")[3]) / 1048576,
            "flash_alloc": (os.statvfs("//")[0] * os.statvfs("//")[2]) / 1048576
            - (os.statvfs("//")[0] * os.statvfs("//")[3]) / 1048576,
        }

    @property
    def network(self):
        sta_if = network.WLAN(network.STA_IF)
        ifconfig = sta_if.ifconfig()
        return
        {
            "ip": ifconfig[0],
            "netmask": ifconfig[1],
            "gateway": ifconfig[2],
            "dns": ifconfig[3],
        }


    @property
    def Pin(self, id: int):
        return machine.Pin

    