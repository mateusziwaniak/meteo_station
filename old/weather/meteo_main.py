import tkinter as tk
import requests
import dotenv
import os


dotenv.load_dotenv()


class WeatherApi:


    def fetch_weather(self):
        api_key = os.getenv("WEATHER_API_KEY")
        location = "Wroclaw"  # Możesz zmienić lokalizację
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=yes"
        response = requests.get(url)
        response.raise_for_status()  # Podniesienie wyjątku, gdy status nie jest 200
        data = response.json()
        return data






weather_service = WeatherApi()
get_data = weather_service.fetch_weather()

print(get_data)

