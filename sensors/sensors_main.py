import asyncio

from bleak import BleakScanner

from sensors.xiaomi_air_purifier import XiaomiAirQuality
from sensors.xiaomi_temp_humid import XiaomiSensor


async def main():
    # Tworzenie instancji dla dwóch sensorów
    sensor_salon = XiaomiSensor("A4:C1:38:57:C8:02", "Salon")
    bathroom_sensor = XiaomiSensor("A4:C1:38:14:A3:7B", "Łazienka")

    # Uruchomienie nasłuchiwania dla obu sensorów równolegle
    tasks = [
        sensor_salon.start_listening(),
        bathroom_sensor.start_listening()
    ]
    await asyncio.gather(*tasks)

    # Rozłączenie po zakończeniu
    await sensor_salon.disconnect()
    await bathroom_sensor.disconnect()


if __name__ == "__main__":

    # Zastąp poniższe wartości swoimi danymi
    air_purifier = XiaomiAirQuality(
        ip="192.168.1.13",  # Adres IP Twojego oczyszczacza
        token="0828622c7d7bd7a08bec153f09a06e23",  # Token urządzenia
        model="classic"  # Zmień na 'classic', jeśli masz starszy model
    )

    # Pojedynczy odczyt
    air_purifier.update()
    pm25_value = air_purifier.get_pm25()
    print(f"Jednorazowy odczyt PM2.5: {pm25_value} µg/m³")

    # Ciągłe monitorowanie (odkomentuj, jeśli chcesz)
    # air_purifier.run(interval=60)


    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

