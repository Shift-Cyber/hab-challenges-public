# Hancock - 125pts
### 01-C-KYMV9
*Author: Nate Singer (Helix)*

Cryptography is the practice of keeping information secure and private. It involves using math and special techniques to convert regular information, called plaintext, into secret code, called ciphertext. This makes it hard for others to read the information without the key to decrypt it, which is like a secret code to convert the ciphertext back into plaintext. Cryptography is used to protect sensitive information, like credit card numbers and personal information online, and is also used in things like phone and internet communication to keep them private.

## Teaching Points
1. How can I send only YOU data if you never gave me a secret key?
2. What is message signing and how does it work?
3. Where is asymmetric encryption used in the real world?

## Challenge Prompt
I stole this session token from someone and it looks like all I need to do is change admin to true for all the power... no idea who signed it though... can you figure out the secret for me so that we can get some pwnage going?

*The secret for this token is somewhere in the RockYou wordlist*
https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt

`eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxMjM0NTY3ODkwLCJhZG1pbiI6ZmFsc2V9.QR_da_OHe58LBwBRt5S_aTcbMkBhEFqJkFn7zUq7Yyc`

## Solution Guide
1. Decode the token without the signature and identify the algorithm as HS256
2. Stage the rockyou wordlist and jwt-cracker script (https://github.com/mazen160/jwt-pwn)
3. Crack the JSON Web Token
```
python3 jwt-cracker.py  --jwt eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxMjM0NTY3ODkwLCJhZG1pbiI6ZmFsc2V9.QR_da_OHe58LBwBRt5S_aTcbMkBhEFqJkFn7zUq7Yyc -w ../rockyou.txt
```

NON-STANDARD FLAG FORMAT
**Flag:** ghosthunter

## Reference Material
### What is a session token?
Session tokens are similar to digital tickets that help a website remember who you are and what you're allowed to do. When you log into a website, it creates a session for you and gives you a token, which is like a ticket. Whenever you visit the site, you show this ticket to the website, and it lets you in and knows who you are. This helps the website keep track of your activities and personalize your experience.

Think of it like a wristband you get at an amusement park. The wristband proves you've paid to get in, and whenever you go on a ride, you show the wristband to the attendant, who knows you're allowed to be there. In the same way, the session token proves to the website that you're logged in, and lets you access certain features or information that are unique to you.

### What is a JSON web token?
A JSON Web Token (JWT) is like a digital ID card that helps identify you when you visit websites or use apps. It's made up of a string of text that contains information about who you are and what you're allowed to do. When you log in to a website, it sends a JWT to your device, which you then send back to the website with each request you make. This helps the website know it's really you, and what you're allowed to do on the site. Think of it like a key that opens certain doors in a building: the JWT is the key that lets you into certain parts of a website or app, and proves who you are.

### What is cryptographic signing?
Cryptographic signatures are like secret codes that prove who sent a message and that the message wasn't changed along the way. When you send a message, anyone can read it, but if you add a secret code to it, only the person you're sending it to can know for sure that the message came from you and that it wasn't changed by anyone else.

### How is a JSON web token signed?
A JSON Web Token (JWT) is signed to make sure that the information in it can't be tampered with or changed. It's like adding a secret message to a postcard. When you send a postcard, anyone can read what's written on it, but if you add a secret message that only the person you're sending it to knows, they can be sure that the message wasn't changed along the way.

In the same way, when a JWT is signed, a secret code is added to it that proves that the information in the JWT hasn't been changed. When a website sends a JWT to your device, it includes the secret code. When you send the JWT back to the website with each request, the website checks the secret code to make sure it hasn't been changed. If the secret code is missing or incorrect, the website knows that the JWT has been tampered with, and it won't let you in.

Signing the JWT helps keep your information secure and prevents unauthorized changes. It's like locking a box with a secret code: only people who know the code can get into the box and see what's inside.

### What is asymmetric encryption?
Asymmetric encryption is like a secret code that helps keep information safe when it's sent from one place to another. When you send a message, anyone can read it, but if you use asymmetric encryption, only the person you're sending it to can read it.

Think of it like a locked box with a key. When you send the box to someone, only they have the key to unlock it and see what's inside. In the same way, when you send information using asymmetric encryption, only the person you're sending it to has the secret code to unlock the message and read it.

Asymmetric encryption uses two keys: a public key and a private key. The public key is like a lock that anyone can use to lock the box and send it to the owner of the private key, who can unlock it. This helps keep the information safe, even if it's sent over the internet or other public networks. Only the person with the private key can unlock the message and read what's inside.

### External References
- JSON Web Tokens https://jwt.io/
- What are Digital Signatures? - Computerphile (https://www.youtube.com/watch?v=s22eJ1eVLTU)
