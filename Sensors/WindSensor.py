from abc import ABC
from http.client import responses
import requests

from Sensors.Sensor import Sensor
from interface.Source import Source

class WindSensor(Sensor, Source, ABC):
    def __init__(self):
        self.url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=relative_humidity_2m,temperature_2m,wind_speed_10m"

    def show(self):
        responses = requests.get(self.url)
        data = responses.json()
        wind_speed = data['hourly']['wind_speed_10m'][0]

        print(f'Wind Speed: {wind_speed}km/h')
