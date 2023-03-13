# Bites - 125pts
### 01-P-XRVEO
*Author: Nate Singer (Helix)*

Programming is the process of creating instructions for a computer to follow using a specific language. These instructions, called code, tell the computer what to do, like creating a game or displaying information on a website. There are many different programming languages, each with their own rules and syntax. Once the code is written, it needs to be run or executed so the computer can follow the instructions. Programming is used in many fields and is a powerful tool to automate tasks, solve problems, and create new things.

## Teaching Points
1. What is binary data?
2. Why is data displayed as hex if files are just 1's and 0's?
3. How can we read bytes from a file programatically?

## Challenge Prompt
*NON-STANDARD FLAG FORMAT*

Here's a blob of data. Thats it. Just Data. Not any specific data. Just 1's and 0's...

Process this file. There are series of bytes from 0x02 to 0xFF. Each of these strings of bytes are surrounded by a null byte (0x00). Finally, there are also byte strings of all 0x01. Your mission is to add up all the bytes in the byte strings that are not 0x01 byte strings. The flag is the integer value of all those bytes added up.


## Solution Guide
1. Read the raw bytes from the file
2. Split the file up into strings of bytes by the null bytes
3. Drop the byte strings that are all 0x01 and add up the other ones

See the `solve.py` file

## Reference Material
### Why is data displayed as hex if its just 1's and 0's?
Data is displayed as hexadecimal (hex) representation because it provides a more compact and human-readable representation of binary data.

In computers, data is stored and processed as binary, which consists of 1's and 0's. However, it can be difficult for humans to read and understand binary data, especially for large amounts of data.

Hexadecimal is a numbering system that uses 16 digits (0-9 and A-F) to represent binary data. Each hex digit represents 4 bits of binary data, so 2 hex digits can represent a single byte (8 bits) of data.

By converting binary data to hexadecimal representation, it becomes easier to read and understand the data. For example, the binary number 10011001 can be represented as the hexadecimal number 0x99. This representation is easier to read and remember, compared to the binary representation.

In addition, hexadecimal representation is often used in computer programming and debugging to inspect and manipulate binary data. Tools like hex editors and debuggers allow you to view and modify binary data in hexadecimal representation, making it easier to work with binary data in a more human-readable format.

### What is binary data vs text?
Binary data and text are two different forms of representation of information.

Binary data, also known as binary file or binary code, is a type of digital data that is stored in a computer file as a series of 1's and 0's. This form of data is not human-readable, but can be understood by a computer and processed by software applications. Examples of binary data include executable files, image files, audio files, and video files.

Text, on the other hand, is a type of digital data that consists of human-readable characters, such as letters, numbers, and symbols. Text data can be represented in many different formats, such as ASCII, Unicode, or UTF-8. This form of data is used to store information such as written text, code, and configuration files.

In summary, binary data is a machine-readable representation of information, while text is a human-readable representation of information.

### How can I read a binary data file one byte at a time with Python3?
You can read binary data one byte at a time in Python by using the open function with mode 'rb' (for "read binary"), then using the read method of the file object to read the desired number of bytes. Here's an example that reads one byte at a time:

```
with open("file.bin", "rb") as f:
    byte = f.read(1)
    while byte:
        # do something with byte
        byte = f.read(1)
```

In this example, the read method is called with an argument of 1, so it returns one byte of data each time it's called. The loop continues until the read method returns an empty byte string, indicating that there is no more data to be read from the file.
