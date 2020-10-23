#!/usr/bin/env micropython
import logging, gc
from sys import platform
from smartcube.hardware import Board, Sensor
from smartcube.server import Server
log = logging.getLogger(__name__)
# PINs available for use


class Cube:

    def __init__(self):
        self.board = Board(platform)
        self.server = Server(self.board)    


if __name__ == "__main__":
    log.debug("start webserver")
    c = Cube()
    c = c.server.run(host="0.0.0.0", port=80)
