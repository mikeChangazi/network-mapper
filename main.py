from network import get_local_network
from scanner import scan_network
from storage import load_devices, save_devices
from inventory import (update_inventory, trust_device, untrust_device)
from display import display_inventory

import argparse

def parse_arguments():

    parser = argparse.ArgumentParser(

            description = "Python Network Mapper"

            )

    parser.add_argument(

            "--scan",
            action = "store_true",
            help = "Scan The Network"
                        )

    parser.add_argument(

            "--list",
            action = "store_true",
            help = "List Network Devices"

            )


    parser.add_argument(

            "--trust",
            metavar = "MAC",
            help = "Trust a Network Device by MAC"

            )

    parser.add_argument(

            "--untrust",
            metavar = "MAC",
            help = "Remove Device from Trusted List by MAC"


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

    print("\nNew Devices:\n")

    if new_devices:

        print (f" New devices found {len(new_devices)}")

        #for device in new_devices:
         #   print(f"new device: {device}")

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

    #for device in devices:
    #   print(device)

    display_inventory(devices)


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


def untrust(mac):

    devices = load_devices()

    result = untrust_device(
        devices,
        mac
    )

    if result:

        save_devices(devices)

        print(
            f"Device {mac} "
            f"has been marked as untrusted."
        )

    else:

        print(
            f"Device {mac} "
            f"was not found in inventory."
        )


def main():

    args = parse_arguments()

    if args.scan:
        network = get_local_network()
        scan(network)
    

    elif args.list:

        list_devices()

    elif args.trust:

        trust(args.trust)

    elif args.untrust:

        untrust(args.untrust)

    else:

        print(

            f"No valid command found"
            f"use --help for available command"


              )



if __name__ == "__main__":
    main()

