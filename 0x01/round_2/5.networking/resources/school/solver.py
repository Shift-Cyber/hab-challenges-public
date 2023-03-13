import socket
import struct


def split_ip_and_cidr(ip_and_cidr):
    parts = ip_and_cidr.split("/")
    ip = parts[0]
    cidr = int(parts[1])
    return ip, cidr

def get_network_and_host_addresses(ip_and_cidr):
    ip, cidr = split_ip_and_cidr(ip_and_cidr)
    # Convert the IP address string to an integer
    ip_int = struct.unpack("!I", socket.inet_aton(ip))[0]
    # Calculate the network address
    network_int = ip_int & (0xffffffff << (32 - cidr))
    network = socket.inet_ntoa(struct.pack("!I", network_int))
    # Calculate the broadcast address
    broadcast_int = network_int + (1 << (32 - cidr)) - 1
    broadcast = socket.inet_ntoa(struct.pack("!I", broadcast_int))
    return network


network_last_octet_total = 0

with open("school.txt","rt") as fio:
    for line in fio:
        network_last_octet_total += int(get_network_and_host_addresses(line).split('.')[3])

print(network_last_octet_total)
