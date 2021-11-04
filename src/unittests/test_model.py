import unittest
from smartcube.models import Model, Handler
import logging
log = logging.getLogger(__name__)


class SerializeTestcase(unittest.TestCase):
    def test_serialize_Handler(self):
        t = {
            "request": {
                "uri": "https://www.toggl.com/api/v8/time_entries/start",
                "method": "POST",
                "headers": {
                    "Authorization": "Basic NzQwYzIzZjhjYTEwMzQwMDY3Mjk5NTllMzNjYTg5ODY6YXBpX3Rva2Vu",
                    "Content-Type": "application/json"
                },
                "payload": "{ \"time_entry\":\n  { \"description\": \"triggered by smartcube\",\n \"tags\": [\"triggered by smartcube\"],\n    \"pid\":164777840,\n    \"created_with\":\"curl\"\n    }\n}"
            },
            "expected_response_code": 200
        }
        c = Handler.from_dict(t)
        log.debug(c)
        assert t == Model.JSONEncodeModel(c)

    def test_fail_malformed_input_serialize_Handler(self):
        t = {
            "THIS_DOES_NOT EXIST": {
                "uri": "https://www.toggl.com/api/v8/time_entries/start",
                "method": "POST",
                "headers": {
                    "Authorization": "Basic NzQwYzIzZjhjYTEwMzQwMDY3Mjk5NTllMzNjYTg5ODY6YXBpX3Rva2Vu",
                    "Content-Type": "application/json"
                },
                "payload": "{ \"time_entry\":\n  { \"description\": \"triggered by smartcube\",\n \"tags\": [\"triggered by smartcube\"],\n    \"pid\":164777840,\n    \"created_with\":\"curl\"\n    }\n}"
            },
            "expected_response_code": 200
        }
        with self.assertRaises(KeyError):
            Handler.from_dict(t)
