from Sensors.Sensor import Sensor

class HumiditySensor(Sensor):
    def __init__(self, name, unit, value):
        Sensor.__init__(self, name, unit, value)