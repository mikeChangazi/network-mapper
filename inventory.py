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
            device.online = True

            device.hostname = (

                    device.hostname
                    or known_device.hostname

                    )

        else:
            device.first_seen = now
            device.last_seen = now
            device.trusted = False
            device.online = True


            new_devices.append(device)

    # Find previously known devices that were NOT
    # found during the current scan

    current_macs = set()

    for device in current_devices:
        current_macs.add(device.mac)


    for device in known_devices:

        if device.mac not in current_macs:

            device.online = False

            current_devices.append(device)

    
    return current_devices, new_devices

def trust_device(devices, mac):

    for device in devices:

        if device.mac.lower() == mac.lower():

            device.trusted = True

            return True

    return False



def untrust_device(devices, mac):

    for device in devices:

        if device.mac.lower() == mac.lower():

            device.trusted = False

            return True

    return False
