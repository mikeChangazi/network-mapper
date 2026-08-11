from datetime import datetime

def update_inventory(current_devices, known_devices):
    
    known_devices_by_mac = {}

    for device in known_devices:
        known_devices_by_mac[device.mac] = device

    now = datetime.now().isoformat(timespec="seconds")

    new_devices = []

    for device in current_devices:

        if device.mac in known_devices_by_mac:

            known_device = known_devices_by_mac[device.mac]

            device.first_seen = known_device.first_seen
            device.last_seen = now
            device.trusted = known_device.trusted

        else:
            device.first_seen = now
            device.last_seen = now
            device.trusted = False
            new_devices.append(device)

    
    return current_devices, new_devices


