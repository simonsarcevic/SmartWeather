from Sensors.Sensor import Sensor


class WeatherStation:
    def __init__(self):
        self.sensors = []

    def addsensor(self, sensor):
        self.sensors.append(sensor)

    def getsensors(self):
        for s in self.sensors:

            s.showdata()
