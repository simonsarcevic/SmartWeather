import random
from abc import ABC

from interface.Source import Source


class APISource(Source, ABC):
    def __init__(self, name: str, api_url: str = None):
        self.name = name
        self.api_url = api_url

    def getdata(self):
        if "Temperature" in self.name:
            value = round(random.uniform(25.0, 30.0), 1)
            unit = "Celsius"
        elif "Air pressure" in self.name:
            value = round(random.uniform(900, 130), 1)
            unit = "hPa"
        else:
            value = round(random.uniform(0, 100), 1)
            unit = "%"

        return {
            'name': f"{self.name} (API)",
            'value': value,
            'unit': unit,
        }