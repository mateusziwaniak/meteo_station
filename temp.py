# from miio.discovery import Discovery
#
# discovery = Discovery()
# devices = discovery.discover()
# for dev in devices:
#     print(f"Device: {dev['ip']} - Model: {dev['model']} - Token: {dev['token']}")


import asyncio

# Asynchroniczna funkcja, która symuluje opóźnienie (np. operację sieciową)
async def greet(name: str) -> str:
    print(f"Rozpoczynam pozdrowienie dla {name}...")
    await asyncio.sleep(1)  # Symulacja opóźnienia
    return f"Cześć, {name}!"

# Główna funkcja asynchroniczna, która uruchamia kilka zadań jednocześnie
async def main():
    names = ["Alice", "Bob", "Charlie"]
    # Tworzymy listę coroutine (zamiast od razu wykonywać funkcję, tworzymy coroutine)
    tasks = [greet(name) for name in names]
    # await asyncio.gather uruchamia wszystkie zadania równocześnie i czeka na ich zakończenie
    greetings = await asyncio.gather(*tasks)
    for greeting in greetings:
        print(greeting)

# Uruchomienie event loop, który "odpalą" nasze coroutine
if __name__ == "__main__":
    asyncio.run(main())