import socket
import psutil
import ipaddress

#get interface details, ip, subnet from lcal device
def get_local_network():


    interfaces = psutil.net_if_addrs()

    for interface_name, addresses in interfaces.items():

        for address in addresses:

            if address.family.name == "AF_INET":

                ip = address.address
                netmask = address.netmask

                if ip.startswith("127."):   #skip loopback address
                    
                    continue
                
                #determine the local network
                network = ipaddress.ip_network(

                        f"{ip}/{netmask}", strict=False

                )

                return str(network)


def get_hostname(ip):

    try:
        hostname = socket.gethostbyaddr(ip)[0]

        return hostname

    except socket.herror:

        return None

    except socket.gaierror:
        return None




if __name__=="__main__":
    main()
