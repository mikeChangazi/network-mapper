from network import get_local_ip
from scanner import scan_network

def main():

    ip = get_local_ip()

    print("Network Mapper")
    print("\n--------------------------------------------------------------\n")
    print(f"My IP: {ip}")


    network = "192.168.10.0/24"


    print("\n scanning...\n")

    devices = scan_network(network)

    for device in devices:
        print(device)

    print("\nDevices found:", len(devices))


if __name__ == '__main__':
    main()
