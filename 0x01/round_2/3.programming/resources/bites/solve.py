#!/usr/bin/python3

all_bytes = []

# open the file and ingest the data
with open("data.bin", "rb") as f:
    byte = f.read(1)
    while byte:
        if byte != b"\x01":
            all_bytes.append(byte)
        byte = f.read(1)


# split on null bytes
byte_strings = b''.join(all_bytes).split(b'\x00')

total = 0

for byte_string in byte_strings:
    if not byte_string == b'':
        print(byte_string)
        for byte in byte_string:
            total += byte

print(total)
