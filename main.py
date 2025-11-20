from Sensors.HumiditySensor import HumiditySensor
from Sensors.TempSensor import TempSensor
from Sensors.WindSensor import WindSensor


class Main:
    if __name__ == "__main__":
        temp = TempSensor("temp", "Celsius", 2)
        wind = WindSensor("wind", "kWh", 2)
        humidity = HumiditySensor("wet", "%", 2)

        sensors = [temp, wind, humidity]
        for s in sensors:
            s.showdata()
