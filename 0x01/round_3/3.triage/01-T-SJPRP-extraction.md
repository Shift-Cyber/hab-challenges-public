# Extraction - 150pts
### 01-T-SJPRP
Author: Nate Singer (Helix)<br>
Challenge Resources: [./resources/sjprp-extraction/](./resources/sjprp-extraction/)

It's hard to find excellent hackers, but its even harder to find excellent defenders.

## Challenge Prompt
Check out the pcap file, something weird is going on in here...

Both challenges for this section use the same pcapng file.

triage.pcapng-sha256sum:caa094f0de3b78ce168e01e894218cbd5fcfbc10a909e93fc0980ca74dd89cc6

## Solution Guide
1. Inspect the flag and notice that there are a bunch of rapid sequential DNS requests to the same host
2. See that the only thing changing aside from metadata is the subdomain, extract this and find 8 bit strings
3. Convert those 8 bit strings back to their respective ASCII characters

flag: `flag{what_firewall?_what_IDS?}`
