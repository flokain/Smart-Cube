from network import WLAN, STA_IF, AP_IF
from esp import sleep_type, SLEEP_LIGHT
from machine import reset_cause, DEEPSLEEP_RESET
import logging
import gc

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

gc.collect()
log.debug("free memory on boot: %s", gc.mem_free())

# safe power at the cost of lower reaction time (3ms to wake up)
sleep_type(SLEEP_LIGHT)

WLAN(STA_IF).active(True)
WLAN(AP_IF).active(False)
# only activate wifi module on boot if it was woken up
# by a specific event (like shaking, or a hard reset)
log.info("check if should launch wifi")
if not DEEPSLEEP_RESET == reset_cause():
    log.info("launching wifi")

    WLAN(STA_IF).active(True)
    WLAN(AP_IF).active(False)
