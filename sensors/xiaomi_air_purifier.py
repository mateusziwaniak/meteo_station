from miio import AirPurifierMiot
import time


class XiaomiAirQuality:
    """Klasa do odczytu jakości powietrza (PM2.5) z oczyszczacza Xiaomi."""

    def __init__(self, ip, token, model="miot"):
        """
        Inicjalizacja z adresem IP, tokenem i modelem oczyszczacza.
        model: 'miot' dla nowszych modeli (np. 3H, 4), 'classic' dla starszych (np. 2, 2S).
        """
        self.ip = ip
        self.token = token
        if model == "miot":
            self.device = AirPurifierMiot(ip=self.ip, token=self.token)
        elif model == "classic":
            from miio import AirPurifier
            self.device = AirPurifier(ip=self.ip, token=self.token)
        else:
            raise ValueError("Nieprawidłowy model: użyj 'miot' lub 'classic'")
        self.pm25 = None
        self.last_update = None

    def update(self):
        """Aktualizacja danych z oczyszczacza."""
        try:
            status = self.device.status()  # pobranie aktualnego statusu
            self.pm25 = status.aqi  # PM2.5 w µg/m³
            self.av_pm25 = status.average_aqi  # PM2.5 w µg/m³
            self.temp = status.temperature
            self.hum = status.humidity
            self.last_update = time.ctime()
            print(f"[{self.ip}] PM2.5: {self.pm25} µg/m³ (zaktualizowano: {self.last_update})\n"
                  f"[{self.ip}] Avg PM2.5: {self.av_pm25} µg/m³ (zaktualizowano: {self.last_update})\n"
                  f"[{self.ip}] Temp: {self.temp} C (zaktualizowano: {self.last_update})\n"
                  f"[{self.ip}] Humidity: {self.hum} % (zaktualizowano: {self.last_update})\n"
                  )
            return True
        except Exception as e:
            print(f"[{self.ip}] Błąd podczas aktualizacji: {e}")
            return False

    def get_pm25(self):
        """Zwraca aktualną wartość PM2.5."""
        if self.pm25 is None:
            print(f"[{self.ip}] Brak danych - uruchom update() najpierw.")
        return self.pm25

    def run(self, interval=60):
        """Uruchamia ciągły odczyt w pętli z zadanym interwałem (w sekundach)."""
        print(f"[{self.ip}] Rozpoczynanie monitorowania jakości powietrza co {interval} sekund...")
        while True:
            self.update()
            time.sleep(interval)
