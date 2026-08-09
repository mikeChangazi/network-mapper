#Get Mac Address and extract OUI
#se OUI to get vendor name from the database

VENDORS = {"00:50:56" : "VMware",
           "00:0c:29" : "VMware",
           "00:05:69" : "VMware",

           "B8:27:EB" : "Raspberry Pi Foundation",
           "DC:A6:32" : "Raspberry Pi",

           "FC:FB:FB" : "Apple",
           "F4:F5:E8" : "Samsung"}



def get_vendor(mac_address):

    """Returns vendor name from the MAC Address
    """

    #Normalize the MAC address
    mac_address = mac_address.upper()


    #extract OUI from the MAC address
    oui = ":".join(mac_address.split(":")[:3])

    return VENDORS.get(oui, "Unknown")


