from Sensors.Sensor import Sensor

class TempSensor(Sensor):
    def __init__(self, name, unit, value):
        super().__init__(name, unit, value)