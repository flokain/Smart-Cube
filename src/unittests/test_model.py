import unittest
from smartcube.models import Model, Handler


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
            "expectedResponse": 200
        }
        c = Handler.from_dict(t)
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
            "expectedResponse": 200
        }
        with self.assertRaises(KeyError):
            Handler.from_dict(t)
    
    def test_get_and_execute_handler_by_event_name(self):
        assert False
