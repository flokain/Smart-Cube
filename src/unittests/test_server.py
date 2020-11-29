import logging
from smartcube.cube import Cube
from test.test_db import DataBaseTestCase
from smartcube.models import Model


class APITestCase(DataBaseTestCase):
    def setUp(self):
        c = Cube()
        c.server.run(host="0.0.0.0", port=80)
        DataBaseTestCase.setUp()
    def tearDown(self):
        try:
            os.remove('database/test_smartcube_database')
        except OSError:
            pass
        finally:
            setattr(Model, 'database', 'database/smartcube_database')
