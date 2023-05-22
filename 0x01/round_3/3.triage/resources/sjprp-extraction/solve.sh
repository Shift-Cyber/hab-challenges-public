#!/bin/bash

# Check if the pcap file argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <pcap_file>"
    exit 1
fi

# Set the pcap file path
pcap_file="$1"

# Use tshark to extract DNS requests and print subdomains
tshark -r "$pcap_file" -Y "dns.flags.response eq 0 && dns.qry.type eq 1" -T fields -e dns.qry.name |
while read -r domain; do
    echo -n $domain | awk '{ print substr($0, 1, 11) }' | tr -d '.' | perl -lpe '$_=pack"B*",$_' | tr -d '\n' ;
done
echo ''