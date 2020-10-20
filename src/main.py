#!/usr/bin/env micropython
import logging
from smartcube import server

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

from wifi_manager import WifiManager

log.debug("start connecting")
WifiManager.start_managing()
server.run()