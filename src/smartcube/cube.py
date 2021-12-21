#!/usr/bin/env micropython

import logging
from sys import platform
import uasyncio as asyncio

from smartcube.hardware.board import Board
from smartcube.hardware.sensor import BallSwitchSensor
from smartcube.server import Server
from smartcube.models.handler import Handler

log = logging.getLogger(__name__)


class Cube:
    async def detectAndHandleSensorChange(self):
        """detect change of the sensor, read the current side up
        and trigger the coresponding handler
        """
        # TODO: #21 refactor to sth like publisher subscriber pattern. not necessary because only one subscriber
        while True:
            if self.sensor.has_changed:
                try:
                    handler = Handler.get_by_id(str(self.sensor.side_up))
                    handler.run()
                except (OSError, KeyError):
                    log.error("no handler ran for side".format(id))

            await asyncio.sleep(1)

    def __init__(self):
        """sets up all components which puts the following
        functions in the asyncio event loop
        1. sensor triggered handling
        2. network detection and login
        3. starting WebServer
        """
        self.board = Board(platform)
        self.server = Server(self.board)
        self.sensor = BallSwitchSensor()

        asyncio.get_event_loop().create_task(self.detectAndHandleSensorChange())

    def run_server(self):
        log.debug("start webserver")
        self.server.run(host="0.0.0.0", port=80)


if __name__ == "__main__":
    c = Cube()
    c.run_server()
