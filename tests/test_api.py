import requests

host = "10.42.0.70"

payload = '{"value": true}'
headers = {"Content-Type": "application/json"}


def test_gpio_set_pin():
    response = requests.request(
        "PUT", f"http://{host}/api/v1/gpio/2", headers=headers, data=payload
    )
    assert response.ok
    assert response.json() == {"message": "changed", "value": 1}


def test_gpio_get_side_handler():
    response = requests.request(
        "GET", f"http://{host}/api/v1/handler/side/1", headers=headers
    )
    assert response.ok

    assert response.json() == {
        "request": {
            "uri": "http://my-remote-service.com/webhook-to-trigger",
            "method": "POST",
            "headers": {
                "Authorization": "Basic NzQwYzefIzZjhjYTEwMadadasd",
                "accept": "application/json",
            },
            "payload": "sample body as string",
        },
        "expectedResponse": 201,
    }
