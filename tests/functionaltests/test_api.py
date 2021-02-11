import requests
import unittest

host = "192.168.0.139"
headers = {"Content-Type": "application/json"}


def test_gpio_set_pin():
    response = requests.request(
        "PUT", f"http://{host}/api/v1/gpio/2", headers=headers, json={"value": True}
    )
    assert response.ok
    assert response.json() == {"message": "changed", "value": 1}


class Resourcetesting():

    def setUp(self):
        self.payload = None
        self.response = None
        self.path = None

    def test_get_resource(self):
        response = requests.request(
            "GET", f"{self.path}/1", headers=headers
        )
        assert response.ok

    def test_get_resources(self):
        response = requests.request(
            "GET", f"{self.path}", headers=headers
        )
        assert response.ok

    def test_post_resource(self):
        response = requests.request(
            "POST", f"{self.path}", headers=headers, json=self.payload
        )

        assert response.ok

    def test_put_resource(self):
        response = requests.request(
            "PUT", f"{self.path}/23", headers=headers, json=self.payload
        )

        assert response.ok
        assert response.json() == self.response

    def test_post_and_get_and_delete_resource(self):
        post_response = requests.request(
            "POST", f"{self.path}", headers=headers, json=self.payload
        )
        id = int(post_response.json()["id"])
        assert post_response.ok

        get_response = requests.request(
            "GET", f"{self.path}/{id}", headers=headers
        )
        assert get_response.ok
        assert get_response.content == post_response.content

        # TODO: #18 with postman this works. there must be a problem with the headers..
        delete_response = requests.request(
            "DELETE", f"{self.path}/{id}", headers=headers
        )
        assert delete_response.ok
        get_response = requests.request(
            "GET", f"{self.path}/{id}", headers=headers
        )
        assert get_response.status_code == 404

    def test_post_and_get_resource(self):
        post_response = requests.request(
            "POST", f"{self.path}", headers=headers, json=self.payload
        )
        id = int(post_response.json()["id"])
        assert post_response.ok

        get_response = requests.request(
            "GET", f"{self.path}/{id}", headers=headers
        )
        assert get_response.ok
        assert get_response.content == post_response.content

        # TODO: #18 with postman this works. there must be a problem with the headers..


class SideHandlerTestCase(Resourcetesting, unittest.TestCase):

    def setUp(self):
        self.payload = {
            "event-id": "side-1",
            "request": {
                "uri": "https://www.toggl.com/api/v8/time_entries/start",
                "method": "POST",
                "headers": {
                    "Authorization": "Basic NzQwYzIzZjhjYTEwMzQwMDY3Mjk5NTllMzNjYTg5ODY6YXBpX3Rva2Vu",
                    "Content-Type": "application/json"
                },
                "payload": "{ \"time_entry\":\n  { \"description\": \"triggered by smartcube\",\n \"tags\": [\"triggered by smartcube\"],\n    \"pid\":164777840,\n    \"created_with\":\"curl\"\n    }\n}"
            },
            "expected-response-code": 200
        }

        self.response = dict(self.payload)
        self.response["id"] = 23
        self.path = f"http://{host}/api/v1/handlers"


class WifiTestCase(Resourcetesting, unittest.TestCase):
    def setUp(self):
        self.payload = {
            "ssid": "test",
            "password": "123"
        }
        self.path = f"http://{host}/api/v1/system/config/wifis"

        self.response = dict(self.payload)
        self.response["id"] = 23


class UserTestCase(Resourcetesting, unittest.TestCase):
    def setUp(self):
        self.payload = {
            "username": "test",
            "password": "123"
        }
        self.response = dict(self.payload)
        self.response["id"] = 23

        self.path = f"http://{host}/api/v1/users"
