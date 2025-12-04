from abc import ABC

from Sensors.Sensor import Sensor
from interface.Source import Source

class TempSensor(Sensor, Source, ABC):
    def __init__(self, name, unit, value):
        super().__init__(name, unit, value)

    def show(self):
        print(f"Temperature: {Sensor.getvalue(self)}")