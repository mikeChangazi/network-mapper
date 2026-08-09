import json
from models.device import Device

FILE_PATH = "data/devices.json"

def save_devices(devices):

    data = []

    for device in devices:

        #create a dictionar of device objects

        device_data = {

                "ip": device.ip,
                "mac": device.mac,
                "vendor": device.vendor

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
                device_data["vendor"]

                )
        devices.append(device)

    return devices



if __name__ == '__main__':

    devices = load_devices()

    print("Loaded devices:")

    for device in devices:
        print(device)


