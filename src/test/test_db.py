import unittest
from smartcube.models.base_model_ import Model
from smartcube.models import Wifi
import os
setattr(Model, 'database', 'database/test_smartcube_database')


class Modeltests(unittest.TestCase):
    def test_save_and_recieve_Wifi(self):
        a = Wifi(ssid="GLUBBE", password="GLUBBE0619")
        a.save("/system/config/wifi/32")
        b = Wifi.get_by_id("/system/config/wifi/32")
        assert a == b


suite = unittest.TestSuite()
suite.addTest(Modeltests)
runner = unittest.TestRunner()
result = runner.run(suite)

os.remove('database/test_smartcube_database')
setattr(Model, 'database', 'database/smartcube_database')
