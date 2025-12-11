from abc import ABC

from Sensors.Sensor import Sensor
from interface.Source import Source
import requests

class HumiditySensor(Sensor, Source, ABC):
    def __init__(self):
        self.url = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=relative_humidity_2m,temperature_2m,wind_speed_10m'

    def show(self):
        response = requests.get(self.url)
        data = response.json()
        humidity = data['hourly']['relative_humidity_2m'][0]

        print(f'Humidity: {humidity}%')