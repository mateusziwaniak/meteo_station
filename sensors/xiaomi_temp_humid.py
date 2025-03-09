import asyncio
from bleak import BleakClient, BleakScanner


class XiaomiSensor:
    """Klasa do odczytu danych z sensorów Xiaomi LYWSD03MMC."""

    # UUID charakterystyki dla temperatury i wilgotności
    TEMP_HUMID_UUID = "ebe0ccc1-7a0a-4b0c-8a1a-6ff2997da3a6"

    def __init__(self, address, name):
        """Inicjalizacja sensora z adresem MAC i nazwą."""
        self.address = address
        self.name = name
        self.client = None
        self.is_connected = False

    def decode_data(self, data):
        """Dekodowanie danych z sensora."""
        if len(data) >= 3:
            temp = int.from_bytes(data[0:2], byteorder='little') / 100  # Temperatura w °C
            humid = data[2]  # Wilgotność w %
            return {"temperature": temp, "humidity": humid}
        else:
            print(f"[{self.name}] Błąd: Za mało danych")
            return None

    async def notification_handler(self, sender, data):
        """Obsługa powiadomień z sensora."""
        print(f"[{self.name}] Odebrano dane: {data.hex('-')}")
        decoded_data = self.decode_data(data)
        if decoded_data:
            print(
                f"[{self.name}] Temperatura: {decoded_data['temperature']}°C, Wilgotność: {decoded_data['humidity']}%")

    async def connect(self, retries=5, delay=10):
        """Łączenie z sensorem z ponawianiem prób."""
        for attempt in range(retries):
            try:
                self.client = BleakClient(self.address, timeout=30)
                await self.client.connect()
                if self.client.is_connected:
                    self.is_connected = True
                    print(f"[{self.name}] Połączono z {self.address}")
                    return True
                else:
                    print(f"[{self.name}] Nie udało się połączyć (próba {attempt + 1}/{retries})")
            except Exception as e:
                print(f"[{self.name}] Błąd połączenia (próba {attempt + 1}/{retries}): {e}")

            if attempt < retries - 1:
                print(f"[{self.name}] Ponawiam za {delay} sekund...")
                await asyncio.sleep(delay)

        print(f"[{self.name}] Nie udało się połączyć po {retries} próbach")
        return False

    async def start_listening(self, duration=10):
        """Rozpoczęcie nasłuchiwania danych przez określony czas (w sekundach)."""
        if not self.is_connected:
            if not await self.connect():
                return

        await self.client.start_notify(self.TEMP_HUMID_UUID, self.notification_handler)
        print(f"[{self.name}] Nasłuchiwanie danych...")
        await asyncio.sleep(duration)
        await self.client.stop_notify(self.TEMP_HUMID_UUID)
        print(f"[{self.name}] Zakończono nasłuchiwanie")

    async def disconnect(self):
        """Rozłączenie z sensorem."""
        if self.client and self.is_connected:
            await self.client.disconnect()
            self.is_connected = False
            print(f"[{self.name}] Rozłączono z {self.address}")
