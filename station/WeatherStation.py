from Sensors.Sensor import Sensor


class WeatherStation:
    def __init__(self):
        self.sensors = []

    def addsensor(self, sensor):
        self.sensors.append(sensor)
        print(f"Sensor {sensor} added")

    def getsensors(self):
        for s in self.sensors:
            s.showdata()