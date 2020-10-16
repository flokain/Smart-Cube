import uasyncio as asyncio
import logging
from wifi_manager import WifiManager

logging.basicConfig(level=logging.INFO)
WifiManager.start_managing()
asyncio.get_event_loop().run_forever()
