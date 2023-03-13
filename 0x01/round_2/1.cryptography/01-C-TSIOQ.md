# Trending - 125pts
### 01-C-TSIQQ
*Author: Nate Singer (Helix)*

Cryptography is the practice of keeping information secure and private. It involves using math and special techniques to convert regular information, called plaintext, into secret code, called ciphertext. This makes it hard for others to read the information without the key to decrypt it, which is like a secret code to convert the ciphertext back into plaintext. Cryptography is used to protect sensitive information, like credit card numbers and personal information online, and is also used in things like phone and internet communication to keep them private.

## Teaching Points
1. What is a hash and why is it useful?
2. What makes a good hashing algorithm, can we write our own?
3. If someone writes their own, how can we attack it?

## Challenge Prompt
All the existing hashing algorithms are dumb, why give me a fixed length? If I give you more input you should give me even more output, its only fair! I wrote a new hashing algorithm that improves on the best of the best (MD5)! Check it out and see if you can break it (you probably can't)!

Here's your hash: `b18f21b19e0f86b22d218c86e182214b867b36212576b2617e8c03862d369e`

*the flag is all lowercase ascii characters, curly brackets and underscores*

Reference: hashbrown.py
**Flag:** flag{dont_roll_your_own_crypto}

## Solution Guide
1. Brute force the "otp" to recover this code
2. Use that code to brute force each character

## Reference Material
### Why do we not "roll our own crypt?"
There are several reasons why it is not recommended to write your own cryptography:
1. Lack of expertise: Cryptography is a complex field that requires a deep understanding of mathematics, computer science, and information security. Most people do not have the necessary expertise to create secure cryptography algorithms.
2. Known weaknesses: There are well-known attacks against certain types of cryptography, such as frequency analysis for substitution ciphers. It is important to use established algorithms that have been widely analyzed and tested.
3. Insecurity due to implementation errors: Even if you have a secure algorithm, it is possible to introduce vulnerabilities through implementation errors. For example, a small mistake in the code can render the entire system insecure.
4. Difficulty in getting peer review: Cryptography is an area where it is critical to have outside experts review and validate your work. This is especially important for widely used systems, where a weakness in the cryptography can have serious consequences. However, it can be difficult to get a sufficient number of experts to review your work.
5. Better alternatives exist: There are many established cryptography libraries and tools available, such as OpenSSL, that have been widely tested and used. It is recommended to use these existing tools rather than attempting to write your own cryptography.
In conclusion, writing your own cryptography is not recommended, as it is a complex and specialized field that requires a deep understanding of mathematics, computer science, and information security. There are many established cryptography libraries and tools available that have been widely tested and used, and it is recommended to use these existing tools rather than attempting to write your own cryptography.
