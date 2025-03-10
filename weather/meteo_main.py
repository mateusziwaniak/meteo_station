import tkinter as tk
import requests


class WeatherApi:


    def fetch_weather(self):
        api_key = "0b9945acb00a41d892e112008250803"
        location = "Wroclaw"  # Możesz zmienić lokalizację
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=yes"
        response = requests.get(url)
        response.raise_for_status()  # Podniesienie wyjątku, gdy status nie jest 200
        data = response.json()
        return data






weather_service = WeatherApi()
get_data = weather_service.fetch_weather()

print(get_data)

