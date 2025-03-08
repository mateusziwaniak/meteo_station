import tkinter as tk
import requests



def fetch_weather():
    api_key = "0b9945acb00a41d892e112008250803"
    location = "Wroclaw"  # Możesz zmienić lokalizację
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=yes"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Podniesienie wyjątku, gdy status nie jest 200
        data = response.json()
        update_ui(data)
    except Exception as e:
        weather_info.set(f"Wystąpił błąd: {e}")


def update_ui(data):
    # Pobieramy podstawowe dane pogodowe
    location_name = data["location"]["name"]
    temp_c = data["current"]["temp_c"]
    feels_like = data["current"]["feelslike_c"]
    humidity = data["current"]["humidity"]
    pressure = data["current"]["pressure_mb"]
    wind_kph = data["current"]["wind_kph"]
    condition = data["current"]["condition"]["text"]



    # Budujemy tekst wyświetlający dane
    info_text = f"Aktualna pogoda dla: {location_name}\n"
    info_text += f"Temperatura: {temp_c} °C\n"
    info_text += f"Temp. Odcz: {feels_like} °C\n"
    info_text += f"Wilgotnosc: {humidity} %\n"
    info_text += f"Cisnienie: {pressure} hPa\n"
    info_text += f"Predk. Wiatru: {wind_kph} Km/h\n"
    info_text += f"Stan pogody: {condition}\n\n"

    # Pobieramy dane o jakości powietrza, jeśli dostępne
    air_quality = data["current"].get("air_quality")
    if air_quality:
        info_text += "Jakość powietrza:\n"
        info_text += f"  PM2.5: {air_quality.get('pm2_5', 'Brak'):.2f}\n" if air_quality.get(
            'pm2_5') is not None else "  PM2.5: Brak\n"
        info_text += f"  PM10: {air_quality.get('pm10', 'Brak'):.2f}\n" if air_quality.get(
            'pm10') is not None else "  PM10: Brak\n"
        info_text += f"  NO2: {air_quality.get('no2', 'Brak'):.2f}\n" if air_quality.get(
            'no2') is not None else "  NO2: Brak\n"
        info_text += f"  SO2: {air_quality.get('so2', 'Brak'):.2f}\n" if air_quality.get(
            'so2') is not None else "  SO2: Brak\n"
        info_text += f"  O3: {air_quality.get('o3', 'Brak'):.2f}\n" if air_quality.get(
            'o3') is not None else "  O3: Brak\n"
        info_text += f"  CO: {air_quality.get('co', 'Brak'):.2f}\n" if air_quality.get(
            'co') is not None else "  CO: Brak\n"
    else:
        info_text += "Brak danych o jakości powietrza.\n"

    weather_info.set(info_text)


# Konfiguracja głównego okna
root = tk.Tk()
root.title("Meteo Station")
root.geometry("400x400")
root.resizable(False, False)

# StringVar do przechowywania informacji pogodowych
weather_info = tk.StringVar()

# Etykieta wyświetlająca dane (możesz dostosować czcionkę, kolory i wyrównanie)
label = tk.Label(root, textvariable=weather_info, justify="left", font=("Helvetica", 12))
label.pack(padx=20, pady=20)

# Przycisk do odświeżenia danych
refresh_button = tk.Button(root, text="Odśwież dane", command=fetch_weather, font=("Helvetica", 10))
refresh_button.pack(pady=10)

# Pobieramy dane przy starcie aplikacji
fetch_weather()

# Uruchamiamy główną pętlę aplikacji
root.mainloop()
