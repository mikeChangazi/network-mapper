import json
from models.device import Device

FILE_PATH = "data/devices.json"

def save_devices(devices):

    data = []

    for device in devices:

        #create a dictionary of device objects

        device_data = {

                "ip": device.ip,
                "mac": device.mac,
                "vendor": device.vendor,
                "first_seen": device.first_seen,
                "last_seen": device.last_seen,
                "trusted": device.trusted,
                "online": device.online

                }

        #appends the dictionary to alist

        data.append(device_data)

    with open(FILE_PATH, "w") as file:

        json.dump(

                data,
                file,
                indent=4
                
                )

def load_devices():

    try:
        with open(FILE_PATH, 'r') as file:

            data = json.load(file)

    except FileNotFoundError:
        return []

    devices = []

    for device_data in data:

        device = Device(

                device_data["ip"],
                device_data["mac"],
                device_data["vendor"],
                device_data.get("first_seen"),
                device_data.get("last_seen"),
                device_data.get("trusted"),
                device_data.get("online", False)

                )

        devices.append(device)

    return devices



if __name__ == '__main__':

    device = Device(

        "192.168.10.50",
        "AA:BB:CC:11:22:33",
        "Test Vendor",
        "2026-08-09T15:00:00",
        "2026-08-09T15:00:00",
        False
    )

    save_devices([device])

    devices = load_devices()

    print("Loaded devices:")

    for device in devices:
        print(device)


