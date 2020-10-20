#!/usr/bin/env micropython
import logging
from smartcube.hardware import Hardware
from smartcube.server import Server
log = logging.getLogger(__name__)
# PINs available for use


class cube:

    def __init__(self, hardware: Hardware):
        self.hardware = Hardware()
        self.server = Server(hardware)
        self.server.run(host="0.0.0.0", port=80)


if __name__ == "__main__":
    log.debug("start webserver")
    cube.start()
