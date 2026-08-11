from network import get_local_ip
from scanner import scan_network
from storage import load_devices, save_devices
from inventory import update_inventory


def main():

    network = "192.168.10.0/24"

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


if __name__ == "__main__":
    main()

