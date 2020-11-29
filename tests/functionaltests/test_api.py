import requests
import unittest
import os
import pprint
import sys
pprint.pprint(sys.path)

host = "10.0.0.20"

headers = {"Content-Type": "application/json"}


def test_gpio_set_pin():
    response = requests.request(
        "PUT", f"http://{host}/api/v1/gpio/2", headers=headers, json={"value": True}
    )
    assert response.ok
    assert response.json() == {"message": "changed", "value": 1}


class SideHandlerTestCase(unittest.TestCase):

    def setUp(self):
        self.payload = {
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

        self.response = {
            "id": 23,
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

    def test_get_side_handler(self):
        response = requests.request(
            "GET", f"http://{host}/api/v1/handler/side/1", headers=headers
        )
        assert response.ok

    def test_post_side_handler(self):
        response = requests.request(
            "POST", f"http://{host}/api/v1/handler/side", headers=headers, json=self.payload
        )

        assert response.ok

    def test_put_side_handler(self):
        response = requests.request(
            "PUT", f"http://{host}/api/v1/handler/side/23", headers=headers, json=self.payload
        )

        assert response.ok
        assert response.json() == self.response

    def test_post_and_get_side_handler(self):
        post_response = requests.request(
            "POST", f"http://{host}/api/v1/handler/side", headers=headers, json=self.payload
        )
        id = post_response.json()["id"]
        assert post_response.ok

        get_response = requests.request(
            "GET", f"http://{host}/api/v1/handler/side/{id}", headers=headers
        )
        assert get_response.ok
        assert get_response.content == post_response.content
