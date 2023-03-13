# Banker - 150pts
### 01-C-DWTRK
*Author: Nate Singer (Helix)*

Cryptography is the practice of keeping information secure and private. It involves using math and special techniques to convert regular information, called plaintext, into secret code, called ciphertext. This makes it hard for others to read the information without the key to decrypt it, which is like a secret code to convert the ciphertext back into plaintext. Cryptography is used to protect sensitive information, like credit card numbers and personal information online, and is also used in things like phone and internet communication to keep them private.

## Teaching Points
1. If a hash is good, does that mean our password is unbreakable?
2. How can we recover the plaintext of properly hashed data?
3. Why does the type of algorithm matter (speed)?

## Challenge Prompt
**NON-STANDARD FLAG FORMAT**

Crack this pin code. It's between 4-8 characters and all numeric.

`320f5cef77246cdce15f9b66e9e4f3ad22f506f9cd28d85e7ccc8839b301e736`

## Solution Guide
1. Use hashid to determine the hash format is (likely) SHA-256
2. Setup John the Ripper to do a pin brute force with numeric chars between 4-8 length
3. Run `jonh --format=raw-sha256 -mask=?d?d?d?d?d?d?d?d inputfile.txt`

## Reference Material
### What is John the Ripper?
John the Ripper is a popular open-source software program used for password cracking, which is the process of recovering passwords from stored or transmitted data. It is named after the infamous 19th-century serial killer Jack the Ripper.

John the Ripper is a command-line tool that is used by security professionals, penetration testers, and system administrators to test the strength of password security for a particular system or set of files. It is capable of brute-force attacks, dictionary attacks, and hybrid attacks, which combine dictionary words with common passwords to increase the chances of success.

The program supports a wide range of operating systems and platforms, and can crack passwords for a variety of file types, including Unix password files, Windows NT/2000/XP/2003/Vista/7 password hashes, and more.

While John the Ripper can be used for legitimate purposes, it can also be used for malicious purposes, such as hacking into someone's accounts or stealing sensitive information. It is important to note that using John the Ripper to crack passwords without permission is illegal and unethical. You have our permission to use it here.

### How does a bruteforce attack work?
A bruteforce attack is like trying every possible combination of a password until you find the right one. It's kind of like trying every key on a keychain until one of them unlocks a door.

Let's say you have a password that is made up of four digits, like "1234". A bruteforce attack would start with the combination "0000" and then try "0001", "0002", "0003", and so on, until it eventually tries "1234" and unlocks the password.

The reason it's called a bruteforce attack is because it doesn't use any clever tricks or shortcuts to try and guess the password. It just tries every possible combination until it finds the right one. Depending on how long the password is and how many possible combinations there are, a bruteforce attack can take a very long time to succeed.

That's why it's important to use strong passwords that are hard to guess. Instead of using something like "1234", you should use a longer passphrase. The longer the password the harder it will be for a machine to crack.

### Why does the type of hashing algorithm affect attack speed?
The hashing algorithm used to create a password hash affects attack speed because some algorithms are more computationally expensive than others, which makes it more difficult and time-consuming to crack the password.

A hashing algorithm is a mathematical function that takes input data (such as a password) and generates a fixed-size output value, called a hash. A good hashing algorithm should be irreversible, meaning that it is difficult or impossible to determine the original input data based on the hash value alone. This makes it more difficult to crack a password using brute-force or dictionary attacks.

However, some hashing algorithms are designed to be faster and less computationally expensive than others. For example, the MD5 hashing algorithm is very fast but is now considered insecure because it is susceptible to collision attacks, where different input values produce the same hash output. In contrast, the SHA-256 hashing algorithm is slower but is considered more secure because it is resistant to collision attacks.

When an attacker attempts to crack a password hash, they often use specialized software or hardware that can try millions or billions of password combinations per second. If the hashing algorithm used to create the password hash is fast and computationally inexpensive, it is easier for the attacker to try many different passwords quickly. On the other hand, if the algorithm is slower and more computationally expensive, it takes longer for the attacker to try each password, making the attack more difficult and time-consuming. This is why it's important to use secure, slow hashing algorithms when storing passwords, to make it more difficult for attackers to crack them.