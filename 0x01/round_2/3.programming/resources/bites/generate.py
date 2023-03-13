#!/usr/bin/python3

import random

data_strings = []

for i in range(100):
    single_data_string = []

    single_data_string.append(b"\x00")
    for i in range(random.randint(30,50)):
        single_data_string.append(bytes([random.randint(2, 255)]))
    single_data_string.append(b"\x00")

    data_strings.append(b''.join(single_data_string))

    single_data_string = []
    
    for i in range(random.randint(10,20)):
        single_data_string.append(b"\x01")
    single_data_string.append(b"\x00")

    data_strings.append(b''.join(single_data_string))

with open("data.bin", "wb") as fio:
    for data_string in data_strings:
        fio.write(data_string)

