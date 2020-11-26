import btree
import unittest
from smartcube.models import Wifi, Model
import os
setattr(Model, 'database', 'database/test_smartcube_database')


class DataBaseTestCase(unittest.TestCase):
    def setUp(self):
        setattr(Model, 'database', 'database/test_smartcube_database')

    def tearDown(self):
        try:
            os.remove('database/test_smartcube_database')
        except OSError:
            pass
        finally:
            setattr(Model, 'database', 'database/smartcube_database')

class Test_save_and_recieve_Wifi_with_ID(DataBaseTestCase):
    def test_save_and_recieve_Wifi_with_ID(self):
        a = Wifi(ssid="GLUBBE", password="GLUBBE0619")
        id = a.save(32)
        b = Wifi.get_by_id(32)
        assert a == b

class Test_save_and_recieve_Wifi(DataBaseTestCase):
    # TODO: #4 fix KeyError when saving to new database and autogen ID.
    def test_save_and_recieve_Wifi(self):
        a = Wifi(ssid="GLUBBE", password="GLUBBE0619")
        for i in range(1, 4):
            id = a.save()
            b = Wifi.get_by_id(id)
            assert a == b

class Test_save_and_recieve_all_Wifi(DataBaseTestCase):
    def test_save_and_recieve_Wifi(self):
        a = Wifi(ssid="GLUBBE", password="GLUBBE0619")
        a.save()
        b = Wifi(ssid="test", password="test")
        b.save()
        all= Wifi.get_all()
        assert b in all
        # TODO: #4 fix KeyError when saving to new database and autogen ID.
        assert a in all




# suite = unittest.TestSuite()
# suite.addTest(ModelTests)
# runner = unittest.TestRunner()
# result = runner.run(suite)

