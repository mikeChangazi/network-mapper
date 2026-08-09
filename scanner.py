
from scapy.all import ARP, Ether, srp
from models.device import Device
from vendor import get_vendor

def scan_network(network):

    print(f"\nScanning network: {network}")

    devices = []


    #scapy creates an ARP request packet

    arp_request = ARP(
            pdst = network   #the arp request desination is the given network

    )
    

    #creates an Ethernet frame with broadcast MAC destination

    broadcast = Ether(

            dst = "ff:ff:ff:ff:ff:ff"  #destination is broadcast MAC address
    )


    #arp request is stacked ontop on Ethernet frame

    packet = broadcast / arp_request
    # In scapy, this '/' does not mean devide. It means stack one protocol on top of another
    # The '/' build the packet by encapsulating the ARP request inside Ethernet frame
    #print(packet.show())

    answered = srp(

            packet,
            timeout=2,
            verbose=False

    )[0]
    
    for sent, recieved in answered:
        vendor = get_vendor(recieved.hwsrc)

        device = Device(
                recieved.psrc,
                recieved.hwsrc,
                vendor

                )

        devices.append(device)

    return devices

