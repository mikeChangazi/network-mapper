
class Device:

    def __init__(self, ip,
                 mac,
                 vendor,
                 first_seen = None,
                 last_seen= None,
                 trusted = False,
                 online = False):

        self.ip = ip
        self.mac = mac
        self.vendor = vendor

        self.first_seen = first_seen
        self.last_seen = last_seen

        self.trusted = trusted
        self.online = online


    def __repr__(self):

        return (

        f"Device("

        f"ip : {self.ip},"
        f"mac : {self.mac},"
        f"vendor : {self.vendor}),"

        f"first_seen: {self.first_seen},"
        f"last_seen: {self.last_seen},"

        f"trusted : {self.trusted},"
        f"online : {self.online}"

        )

