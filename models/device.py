
class Device:

    def __init__(self, ip, mac, vendor):

        self.ip = ip
        self.mac = mac
        self.vendor = vendor


    def __repr__(self):

        return (

        f"Device("
        f"ip : {self.ip}, "
        f"mac : {self.mac}, "
        f"vendor : {self.vendor})"

        )

