import random
import socket
import struct

# Private IP address ranges
private_ip_ranges = [
    (3232235520, 3232235775),   # 192.168.0.0/24
    (2886729728, 2886729983),   # 172.16.0.0/24
    (167772160, 184549375),     # 10.0.0.0/8
]

# Function to generate a random private IP address
def generate_private_ip():
    # Pick a random range
    range_start, range_end = random.choice(private_ip_ranges)
    # Generate a random IP address within the range
    ip = random.randint(range_start, range_end)
    # Convert the integer to an IP address string
    ip = '.'.join(map(str, [ip >> 24, ip >> 16 & 255, ip >> 8 & 255, ip & 255]))
    return ip

# Function to convert an IP address string to an integer
def ip_to_int(ip_address):
    return struct.unpack("!I", socket.inet_aton(ip_address))[0]

# Function to generate a random subnet mask represented as a CIDR range
def generate_subnet_mask():
    return random.randint(8, 30)

# Generate a bunch of random private IP addresses with subnet masks
with open("school.txt","wt") as fio:
    for i in range(1000):
        ip = generate_private_ip()
        subnet_mask = generate_subnet_mask()
        cidr = f"{ip}/{subnet_mask}"
        
        fio.write(f"{cidr}\n")