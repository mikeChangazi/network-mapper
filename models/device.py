
class Device:

    def __init__(self, ip,
                 mac,
                 vendor,
                 first_seen = None,
                 last_seen= None,
                 trusted = False ):

        self.ip = ip
        self.mac = mac
        self.vendor = vendor

        self.first_seen = first_seen
        self.last_seen = last_seen

        self.trusted = trusted


    def __repr__(self):

        return (

        f"Device("
        f"ip : {self.ip},\n "

        f"mac : {self.mac},\n "

        f"vendor : {self.vendor}),\n"

        f"first_seen: {self.first_seen},\n"

        f"last_seen: {self.last_seen},\n"

        f"trusted : {self.trusted}\n"

        )

