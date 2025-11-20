from Sensors.HumiditySensor import HumiditySensor
from Sensors.TempSensor import TempSensor
from Sensors.WindSensor import WindSensor


class Main:
    if __name__ == "__main__":

        temp = TempSensor("Temperatur-Sensor", "Celsius", 31)
        wind = WindSensor("Wind-Sensor", "km/h", 45)
        humidity = HumiditySensor("Feuchtigkeits-Sensor", "%", 95)

        sensors = [temp, wind, humidity]
        for s in sensors:
            s.showdata()
