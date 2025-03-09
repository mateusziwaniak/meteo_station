from miio.discovery import Discovery

discovery = Discovery()
devices = discovery.discover()
for dev in devices:
    print(f"Device: {dev['ip']} - Model: {dev['model']} - Token: {dev['token']}")