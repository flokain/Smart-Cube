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
        """ detect change of the sensor, read the current side up
            and trigger the coresponding handler
        """
        # TODO: #21 refactor to sth like publisher subscriber pattern. not necessary because only one subscriber
        while True:
            if self.sensor.has_changed:
                try:
                    # by conevtion the name of the events are defined int the
                    # Sensor class and must be reflected in the event_id field of the handler class
                    event_id = self.sensor.recent_event
                    handlers = Handler.get_all(event_id=event_id)
                    for h in handlers:
                        h.run(()
                    if len(handlers) == 0:
                        log.info(
                            "no handlers found for event {}".format(event_id))
                except OSError as e:
                    log.error("no handler ran for side. Error was", e)

            await asyncio.sleep(1)

    def __init__(self):
        """ sets up all components which puts the following
            functions in the asyncio event loop
            1. sensor triggered handling
            2. network detection and login
            3. starting WebServer
        """
        self.board=Board(platform)
        self.server=Server(self.board)
        self.sensor=BallSwitchSensor(

        )

        asyncio.get_event_loop().create_task(self.detectAndHandleSensorChange())

    def run(self):
        log.debug("start webserver")
        self.server.run(host="0.0.0.0", port=80)


if __name__ == "__main__":
    c=Cube()
    c.run()
