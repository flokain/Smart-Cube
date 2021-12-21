#!/usr/bin/env micropython
import logging
from smartcube.cube import Cube

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

c = Cube()
c.run_server()
