from network import get_local_ip
from scanner import scan_network
from storage import load_devices, save_devices
from inventory import update_inventory
from inventory import trust_device

import argparse

NETWORK = "192.168.10.0/24"

def parse_arguments():

    parser = argparse.ArgumentParser(

            description = "Python Network Mapper"

            )

    parser.add_argument(

            "--scan",
            action = "store_true",
            help = "Scan the network"
                        )

    parser.add_argument(

            "--list",
            action = "store_true",
            help = "Lst network devices"

            )


    parser.add_argument(

            "--trust",
            metavar = "MAC",
            help = "Trust a network device by MAC"

            )

    return parser.parse_args()


def scan(network):

    # Scan the network
    current_devices = scan_network(network)

    # Load devices from previous scans
    known_devices = load_devices()

    # Find devices that were not previously known
    current_devices, new_devices = update_inventory(
        current_devices,
        known_devices
    )

    print("\nNew Devices:")

    if new_devices:

        for device in new_devices:
            print(f"NEW DEVICE: {device}")

    else:

        print("No new devices found.")

    # Save the current scan
    save_devices(current_devices)

#load and list devices
def list_devices():

    devices = load_devices()

    print("\nDevice Inventory:")

    if not devices:

        print("No devices in inventory.")

        return

    for device in devices:
        print(device)   


    # Trust a device

def trust(mac):

    devices = load_devices()

    result = trust_device(
            devices,
            mac

            )

    if result:

        save_devices(devices)

        print(
                f"Device {mac}"
                f"has been trusted"
              )

    else:

        print(
                f"Device {mac}"
                f"not found in inventory"
            )


def main():

    args = parse_arguments()

    if args.scan:
        scan(NETWORK)
    

    elif args.list:

        list_devices()

    elif args.trust:

        trust(args.trust)

    else:

        print(

            f"No valid command found"
            f"use --help for available command"


              )



if __name__ == "__main__":
    main()

