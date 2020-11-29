import network
import esp
# safe power at the cost of lower reaction time (3ms to wake up)
esp.sleep_type(esp.SLEEP_LIGHT)
network.WLAN(network.STA_IF).active(False)  # WiFi station interface
network.WLAN(network.AP_IF).active(False)  # access-point interface
