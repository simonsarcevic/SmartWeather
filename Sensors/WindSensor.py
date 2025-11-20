from Sensors.Sensor import Sensor

class WindSensor(Sensor):
    def __init__(self, name, unit, value):
        super().__init__(name, unit, value)