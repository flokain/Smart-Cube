import network
import esp
esp.sleep_type(esp.SLEEP_LIGHT) # safe power at the cost of lower reaction time (3ms to wake up)
network.WLAN(network.STA_IF).active(False)  # WiFi station interface
network.WLAN(network.AP_IF).active(False)  # access-point interface