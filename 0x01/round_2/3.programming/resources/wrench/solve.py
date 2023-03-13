#!/usr/bin/python3
from pwn import *

# Connect to the target host and port
conn = remote('localhost', 54321)

# Consume first line
conn.recvline()

# Get all data
data = conn.recvuntil((b"total: ")).split(b"\n")

# Compute the flag
total = 0
for value in data:
    # decode the byte string
    value = value.decode("utf-8")
    
    # if its actually an int, add it up
    try: total += int(value)
    except ValueError: pass

conn.sendline(str(total).encode('utf-8'))

#consume newline
conn.recvline()

# get flag
print(conn.recvuntil(b'}').decode('utf-8'))

conn.close()