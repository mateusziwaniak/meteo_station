from datetime import datetime

# from sensors.sensor_reader import SensorReader
# from weather.weather_api import WeatherAPI
# from data.data_manager import DataManager
# from display.display_manager import DisplayManager

from data.mariadb_main import MeteoDataWriter
from weather.meteo_main import WeatherApi

# XIAOMI MACs
XIAOMI_SENSOR_SALON = "A4:C1:38:57:C8:02"
XIAOMI_BATHROOM_SENSOR = "A4:C1:38:14:A3:7B"

# from sensors.sensor_reader import SensorReader
# from weather.weather_api import WeatherAPI
# from data.data_manager import DataManager
# from display.display_manager import DisplayManager


class MeteoApp:
    def __init__(self):
        pass
        # self.sensor_reader = SensorReader()
        # self.weather_api = WeatherAPI(api_key='TWÓJ_API_KEY')
        # self.data_manager = DataManager()
        # self.display_manager = DisplayManager()

    def run(self):
        # Odczyt danych z sensorów
        # sensor_data = self.sensor_reader.read_sensors()

        # Pobieranie danych z API
        weather_service = WeatherApi
        weather_data = weather_service.fetch_weather()
        #
        # # Łączenie danych
        # combined_data = {**sensor_data, **weather_data}
        #
        # # Przechowywanie danych
        # self.data_manager.save_data(combined_data)
        #
        # # Wyświetlanie danych
        # self.display_manager.show(combined_data)

        # Create an instance of the MeteoDataWriter with your DB credentials
        # writer = MeteoDataWriter(
        #     host="192.168.1.18",
        #     port=3306,
        #     user="user_meteo",
        #     password="Meteo2025!",
        #     database="meteo_db"
        # )
        #
        # current_time = datetime.now()
        #
        # # Insert a reading; additional fields (pressure, wind_speed) are optional.
        # writer.write_reading(temperature=22.5, humidity=55.0, pressure=1013.25, wind_speed=3.5, timestamp=current_time)
        #
        # # Close the connection when done
        # writer.close()







if __name__ == '__main__':
    app = MeteoApp()
    app.run()
