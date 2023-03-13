#!/usr/bin/python3

import hashlib
import string

test_hash = "b18f21b19e0f86b22d218c86e182214b867b36212576b2617e8c03862d369e"
crib = "flag{"

otp = []

# step through two chars at a time
for i in range(0,10,2):

    # get two of the chars from the test_hash
    test_hash_chars = test_hash[i:i+2]

    # for each of the 10 possible ints
    for q in range(10):
        test_c = chr(ord(crib[i // 2]) - q)
        test_c_hash2 = hashlib.md5(test_c.encode('ascii')).hexdigest()[0:2]

        # if we found a match save it and move on
        if test_hash_chars == test_c_hash2:
            otp.append(str(q))
            break

# display brute forced otp
print(f"Brute forced otp using crib: {''.join(list(otp))}")

# decipher the full value
for i in range(0,len(test_hash),2):

    # get two of the chars from the test_hash
    test_hash_chars = test_hash[i:i+2]
    
    # brute force character
    for q in string.ascii_lowercase + '{}_':
        calculated_character = chr(ord(q) - int(otp[(i // 2) % 5]))
        guess_md5_hash2 = hashlib.md5(calculated_character.encode('ascii')).hexdigest()[0:2]

        if test_hash_chars == guess_md5_hash2:
            print(q, end="")
            break

# new line post output
print()