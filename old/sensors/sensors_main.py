import asyncio
import os
from flask.cli import load_dotenv

from old.sensors.xiaomi_air_purifier import XiaomiAirQuality
from old.sensors.xiaomi_temp_humid import XiaomiSensor

load_dotenv()

async def main():
    # Inicjalizacja oczyszczacza powietrza i jednorazowy odczyt
    air_purifier = XiaomiAirQuality(
        ip="192.168.1.13",  # Adres IP oczyszczacza
        token=os.getenv("AIR_PURIFIER_TOKEN"),  # Token urządzenia
        model="classic"  # Zmień na 'classic' jeśli masz starszy model
    )
    # air_purifier.run()

    air_purifier.update()

    # Tworzenie instancji dla dwóch sensorów
    sensor_salon = XiaomiSensor("A4:C1:38:57:C8:02", "Salon")
    bathroom_sensor = XiaomiSensor("A4:C1:38:14:A3:7B", "Łazienka")

    # Odczyt z pierwszego sensora (Salon)
    print("Odczyt z sensora Salon:")
    await sensor_salon.start_listening()
    await sensor_salon.disconnect()

    # Odczyt z drugiego sensora (Łazienka)
    print("Odczyt z sensora Łazienka:")
    await bathroom_sensor.start_listening()
    await bathroom_sensor.disconnect()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Wystąpił błąd: {e}")