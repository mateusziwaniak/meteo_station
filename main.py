from sensors.sensor_reader import SensorReader
from weather.weather_api import WeatherAPI
from data.data_manager import DataManager
from display.display_manager import DisplayManager

# XIAOMI MACs
XIAOMI_SENSOR_SALON = "A4:C1:38:57:C8:02"
XIAOMI_BATHROOM_SENSOR = "A4:C1:38:14:A3:7B"

# from sensors.sensor_reader import SensorReader
# from weather.weather_api import WeatherAPI
# from data.data_manager import DataManager
# from display.display_manager import DisplayManager


class MeteoApp:
    def __init__(self):
        self.sensor_reader = SensorReader()
        self.weather_api = WeatherAPI(api_key='TWÓJ_API_KEY')
        self.data_manager = DataManager()
        self.display_manager = DisplayManager()

    def run(self):
        # Odczyt danych z sensorów
        sensor_data = self.sensor_reader.read_sensors()

        # # Pobieranie danych z API
        # weather_data = self.weather_api.get_current_weather()
        #
        # # Łączenie danych
        # combined_data = {**sensor_data, **weather_data}
        #
        # # Przechowywanie danych
        # self.data_manager.save_data(combined_data)
        #
        # # Wyświetlanie danych
        # self.display_manager.show(combined_data)


if __name__ == '__main__':
    app = MeteoApp()
    app.run()
