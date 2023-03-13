#!/usr/bin/python3

import sys
import hashlib
import random
import string

try:
    # get a five character string to use for randomness (lol)
    one_time_pad_or_something = ''.join(random.choices(string.digits, k=5))
    print(one_time_pad_or_something)
    
    # itterate over each character in the input
    for index,character in enumerate(sys.argv[1]):

        # get md5 hash of (that character plus minus pad)
        calculated_character = chr(ord(character) - int(one_time_pad_or_something[index % 5]))
        full_md5_hash = hashlib.md5(calculated_character.encode('ascii'))

        # take the first four characters and print them to the screen
        print(full_md5_hash.hexdigest()[0:2], end="")
    
    # new line at end of output
    print()

# verify that we got input in position
except IndexError: sys.exit("Usage: python3 hashbrown.py <plaintext>")
