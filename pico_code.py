import machine
import dht
import time
import requests

dht_pin = machine.Pin(2)

dht_sensor = dht.DHT22(dht_pin)
url='http://localhost:5173/api/push-sensor-data'

while True:
    try:
        dht_sensor.measure()

        temperature_celsius = dht_sensor.temperature()
        humidity_percent = dht_sensor.humidity()
        payload={
        "sensor_id":3,
        "humidity":humidity_percent,
        "temperature":temperature_celsius,
        "auth_key":"c00464646b8894b7e7b7cb6413268c77"
                }
        req=requests.post(url,json=payload)
        print(req.json())

    except Exception as e:
        print("Error reading DHT22:", str(e))

    
    time.sleep(300)
