GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def display_inventory(devices):

    print()
    print("NETWORK INVENTORY")
    print("=" * 90)

    print(
        f"{'IP':<16}"
        f"{'MAC':<20}"
        f"{'VENDOR':<15}"
        f"{'STATUS':<20}"
        f"{'TRUST':<20}"
    )

    print("-" * 90)

    online_count = 0
    offline_count = 0
    trusted_count = 0

    for device in devices:

        # Status
        if device.online:

            status = f"{GREEN}ONLINE{RESET}"
            online_count += 1

        else:

            status = f"{RED}OFFLINE{RESET}"
            offline_count += 1


        # Trust
        if device.trusted:

            trust = f"{GREEN}TRUSTED{RESET}"
            trusted_count += 1

        else:

            trust = f"{YELLOW}UNTRUSTED{RESET}"


        print(
            f"{device.ip:<16}"
            f"{device.mac:<20}"
            f"{device.vendor:<15}"
            f"{status:<29}"
            f"{trust}"
        )


    print("=" * 90)

    print(
        f"\nTotal: {len(devices)}    "
        f"Online: {online_count}    "
        f"Offline: {offline_count}    "
        f"Trusted: {trusted_count}"
    )
