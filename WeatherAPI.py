import requests

class WeatherAPI:
    def __init__(self):
        self.url = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,wind_speed_10m,temperature_80m'


    def getdata(self):
        url = self.url
        data = requests.get(url).json()
        temp = data['hourly']['temperature_2m'][0]
        wind_speed = data['hourly']['wind_speed_10m'][0]

        print(f'Temperatur: {temp}°C Wind: {wind_speed}km/h')


