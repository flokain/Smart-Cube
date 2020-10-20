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
            "uri": "https://www.toggl.com/api/v8/time_entries/start",
            "method": "POST",
            "headers": {
                'Authorization': 'Basic NzQwYzIzZjhjYTEwMzQwMDY3Mjk5NTllMzNjYTg5ODY6YXBpX3Rva2Vu',
                'Content-Type': 'application/json',
            },
            "payload": "{ \"time_entry\":\n  { \"description\": \"postmantest\",\n    \"pid\":151476843,\n    \"created_with\":\"curl\"\n    }\n}"
        },
        "expectedResponse": 201,
    }