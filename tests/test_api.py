import requests

host = "10.42.0.70"

payload = "{\"value\": true}"
headers = {
  'Content-Type': 'application/json'
}
response = requests.request("PUT", f"http://{host}/api/gpio/2", headers=headers, data = payload)

def test_gpio_set_pin():
    response = requests.request("PUT", f"http://{host}/api/gpio/2", headers=headers, data = payload)
    assert response.ok
    assert response.json() ==  {'message': 'changed', 'value': 1}

def test_gpio_set_pin():
    response = requests.request("PUT", f"http://{host}/api/gpio/2", headers=headers, data = payload)
    assert response.ok
    assert response.json() ==  {'message': 'changed', 'value': 1}

