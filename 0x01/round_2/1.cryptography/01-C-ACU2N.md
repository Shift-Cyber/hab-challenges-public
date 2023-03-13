# Matchmaker - 100pts
### 01-C-ACU2N
*Author: Nate Singer (Helix)*

Cryptography is the practice of keeping information secure and private. It involves using math and special techniques to convert regular information, called plaintext, into secret code, called ciphertext. This makes it hard for others to read the information without the key to decrypt it, which is like a secret code to convert the ciphertext back into plaintext. Cryptography is used to protect sensitive information, like credit card numbers and personal information online, and is also used in things like phone and internet communication to keep them private.

## Teaching Points
1. The key is what secures data, cryptosystems are public knowledge
2. Why can a cryptosystem be public knowledge?
3. How many keys are required for a secure cryptosystem?

## Challenge Prompt
There are a variety of symmetric cryptosystems out there, but most of them involve a logic block called a XOR. The key is "hab"(UTF8). We're giving you the key and the algorithm, how hard can it be?

```Dg0DDxoRBz4PHQIKNxIbBQwHHBMbFQ==```

## Solution Guide
1. Open cyberchef and take the input "From Base64"
2. Use the XOR block and input the key with format UTF8
3. Retrieve the flag and profit

## Reference Material
### What is symmetric encryption?
Symmetric encryption is a method of encrypting data in which the same secret key is used both for encrypting the original data, and for decrypting the encrypted data. Examples of symmetric encryption algorithms include AES and DES.

Symmetric encryption is generally faster and more efficient than asymmetric encryption, making it well-suited for encrypting large amounts of data. However, the main drawback of symmetric encryption is that the secret key must be exchanged between the sender and receiver before any data can be encrypted or decrypted, and this exchange must be done securely to ensure the security of the communication.

Asymmetric encryption, on the other hand, uses a pair of keys, one for encryption and one for decryption, which are mathematically related but not identical. This allows for the secure exchange of information without the need to share a secret key. However, asymmetric encryption is generally slower and less efficient than symmetric encryption.

In summary, symmetric encryption is a method of encrypting data in which the same secret key is used both for encrypting the original data and for decrypting the encrypted data. It's efficient, fast and suitable for encrypting large amount of data but key exchange could be a challenge. Asymmetric encryption uses a pair of keys, one for encryption and one for decryption and it's more secure for key exchange but less efficient than symmetric encryption.

### Why are good cryptosystems public knowledge (open source)?
Most cryptography is open source because it allows for transparency and security through peer review. When the source code and algorithms used for encryption and decryption are publicly available, they can be studied and evaluated by experts in the field. These experts can then identify and report any weaknesses or vulnerabilities in the encryption system, allowing them to be fixed before they can be exploited by attackers.

Additionally, open-source cryptography allows for the community to verify that the encryption system is not deliberately weakened or 'backdoored' by any government, organization or individual. Open source cryptography is often considered to be more secure than proprietary cryptography because it allows for a larger number of people to review the code, which increases the chances of detecting and fixing any vulnerabilities.

In summary, open-source cryptography is used to improve the transparency and security of encryption systems. By making the source code and algorithms publicly available, it allows for peer review and community validation, which can increase the security of the encryption system and detect vulnerabilities before they can be exploited by attackers.

### What is a one time pad?
A one-time pad (OTP) is a type of encryption system that uses a truly random key that is the same length as the plaintext message, and is used for encryption and decryption only once. The key is used to encrypt the plaintext by performing a bitwise exclusive-or (XOR) operation between the plaintext and the key. To decrypt the ciphertext, the same key is used to perform the XOR operation again, resulting in the original plaintext.

OTP is considered to be the only truly unbreakable encryption method as long as the key is truly random and is used only once. This is because the OTP encrypts the plaintext into a completely random string of letters and numbers, that is completely different from the original, in a way that no statistical pattern can be found. The ciphertext contains no information about the plaintext, making it impossible to decrypt the message without the key.

However, OTP has some practical limitations, such as the need for a secure way to distribute and store the key, and the need for the key to be as long as the plaintext, which can be impractical for large amounts of data.

In summary, OTP is a type of encryption system that uses a truly random key that is the same length as the plaintext message, used for encryption and decryption only once. It is considered to be the only truly unbreakable encryption method as long as the key is truly random and used only once. But it has some practical limitations.

### What is plaintext and ciphertext?
Plaintext is the original message or information that you want to send or keep secret. It's like the original note you wrote to your friend before you put it in a secret code. Ciphertext is the encoded or encrypted version of the plaintext. It's like the secret code version of the note you wrote to your friend. It's not readable or understandable unless you have the key to decode it. So, in short, plaintext is the original message and ciphertext is the coded or encrypted version of the message.
