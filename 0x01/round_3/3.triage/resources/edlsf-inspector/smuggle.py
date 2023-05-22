from scapy.all import IP, TCP, send

target_ip = "final.hackabit.com"
target_port = 80

custom_data = (
    "GET / HTTP/1.1\r\n"
    "Host: www.hackabit.com\r\n"
    "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123\r\n"
    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\n"
    "Accept-Language: en-US,en;q=0.9\r\n"
    "Connection: close\r\n"
    "\r\n"
    "fl_nosearch_ag{tcp_streams_reveal_more}"
)

# Create the IP and TCP layers with the custom data
ip_packet = IP(dst=target_ip)
tcp_packet = TCP(dport=target_port)
packet = ip_packet / tcp_packet / custom_data

# Send the packet to the target
send(packet)