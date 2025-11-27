from Sensors.HumiditySensor import HumiditySensor
from Sensors.TempSensor import TempSensor
from Sensors.WindSensor import WindSensor
from station.WeatherStation import WeatherStation


class Main:
    if __name__ == "__main__":


        temp = TempSensor("Temperatur-Sensor", "Celsius", 31)
        wind = WindSensor("Wind-Sensor", "km/h", 45)
        humidity = HumiditySensor("Feuchtigkeits-Sensor", "%", 95)
        station = WeatherStation()

        station.addsensor(temp)
        station.getsensors()