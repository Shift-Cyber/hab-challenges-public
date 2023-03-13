# Pancakes - 100pts
### 01-P-AZWQN
*Author: Nate Singer (Helix)*

Programming is the process of creating instructions for a computer to follow using a specific language. These instructions, called code, tell the computer what to do, like creating a game or displaying information on a website. There are many different programming languages, each with their own rules and syntax. Once the code is written, it needs to be run or executed so the computer can follow the instructions. Programming is used in many fields and is a powerful tool to automate tasks, solve problems, and create new things.

## Teaching Points
1. What is a compiler?
2. What's the difference between executable binaries and interpreted code?
3. What is a computer architecture?
4. How do we identify the architecture of a file in Linux?

## Challenge Prompt
Okay we're doing it again, just giving you the flag... should be easy enough right? Well now lets talk about compiled code. This is the same code compiled for a bunch of different architectures. First, figure out which binary is compatible with your system, then just run it to get the flag!

## Solution Guide
1. Use the `file` command to determine which architectures are in use
2. Either locate the one that will run on your system (likely x86) or use an emulator like qemu to run another
3. You can also reverse engineer the files with a software like Ghidra

*See the reference material for the Makefiles and code used to generate these challenges.*

## Reference Material
### What is a compiler?
A compiler is a software program that translates source code written in a high-level programming language into machine code that can be executed directly by a computer. The resulting machine code is typically stored in a file that can be run independently of the original source code.

### What's the difference between executable binaries and interpreted code?
An executable binary is a file that contains machine code that a computer can run directly. When you write a program in a compiled language, the compiler turns your code into an executable binary that can be run on a computer.

On the other hand, interpreted code is code that is read and executed by a program called an interpreter. When you write a program in an interpreted language, you don't need to compile it. Instead, the interpreter reads your code and runs it line by line, translating it into machine code as it goes.

Think of it like this: an executable binary is like a recipe book that you can follow step by step, while interpreted code is like a cooking show where the chef explains what they're doing as they go along. Both get the job done, but they work in different ways.

### What is a computer architecture?
Computer architecture is like the blueprint for how a computer is built and how it works. It's like the design of a house, where you decide how many rooms it will have, how big they will be, and where they will be located.

In the same way, computer architecture includes things like the types of processors, memory, storage, and input/output devices that a computer has, as well as how they are connected and work together. It also includes the way that the computer processes and executes instructions, like a set of rules that the computer follows to perform different tasks.

Understanding computer architecture is important because it helps us design and build computers that are faster, more efficient, and can perform more complex tasks. It's like having a good plan for building a house so that it's sturdy and functional, but also comfortable and pleasant to live in.

### Why does computer architecture matter for compilers?
Understanding computer architecture is important for compilers because different computer architectures have different characteristics, such as the way they handle memory, the size of data types they can process efficiently, and the instructions they can execute.

Compilers need to be designed to work with specific computer architectures to generate optimized code that takes full advantage of the computer's capabilities. For example, a compiler that is optimized for a specific type of processor can generate code that uses the processor's special instructions to perform certain tasks more efficiently.

In addition, compilers also need to be aware of how different parts of a computer interact with each other, such as the CPU, memory, and I/O devices. This knowledge allows the compiler to generate code that minimizes data movement between different parts of the computer, which can help improve performance.

Therefore, having a good understanding of computer architecture is crucial for designing and building effective compilers that can generate efficient and optimized machine code for a specific computer architecture.

### How do we identify the architecture of a file in Linux?
In Linux, you can identify the architecture of a file using the "file" command, which displays the type of file and other information about it, including the architecture.

To identify the architecture of a file, you can use the following command:

```
file <file_name>
```

For example, to identify the architecture of a file named "myprogram", you can run the following command:

```
file myprogram
```

The output will include information about the file type and architecture, for example:

```
myprogram: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=0123456789abcdef0123456789abcdef01234567, not stripped
```

In this example, the architecture is "x86-64", which indicates a 64-bit x86 processor architecture.
