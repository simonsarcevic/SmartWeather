from abc import ABC

from Sensors.Sensor import Sensor
from interface.Source import Source

class HumiditySensor(Sensor, Source, ABC):
    def __init__(self, name, unit, value):
        Sensor.__init__(self, name, unit, value)

    def show(self):
        print(f"Humidity Sensor: {Sensor.getvalue(self)}")