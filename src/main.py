#!/usr/bin/env micropython
import logging
from smartcube.cube import Cube

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

c = Cube()
c = c.server.run(host="0.0.0.0", port=80)