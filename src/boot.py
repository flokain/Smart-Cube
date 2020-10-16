import network

network.WLAN(network.STA_IF).active(False)  # WiFi station interface
network.WLAN(network.AP_IF).active(False)  # access-point interface