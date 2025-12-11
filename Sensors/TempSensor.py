from abc import ABC
import requests

from Sensors.Sensor import Sensor
from interface.Source import Source

class TempSensor(Sensor, Source, ABC):
    def __init__(self):
        self.url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=relative_humidity_2m,temperature_2m,wind_speed_10m"

    def show(self):
        responses = requests.get(self.url)
        data = responses.json()
        temp = data['hourly']['temperature_2m'][0]

        print(f'Temperature: {temp}°C')
