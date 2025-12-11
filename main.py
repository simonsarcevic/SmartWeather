from Sensors.HumiditySensor import HumiditySensor
from Sensors.TempSensor import TempSensor
from Sensors.WindSensor import WindSensor
from station.WeatherStation import WeatherStation
from interface.WeatherAPI import WeatherAPI


class Main:
    if __name__ == "__main__":


        temp = TempSensor()
        wind = WindSensor()
        humidity = HumiditySensor()

        sensors = [temp, humidity, wind]
        for sensor in sensors:
            sensor.show()