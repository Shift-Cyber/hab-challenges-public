# Coredump - 100pts
### 01-C-RKBOH
Author: Nate Singer (Helix)<br>
Challenge Resources: [./resources/zyjlp-corruption/](./resources/zyjlp-corruption/)

Writing secure, high-quality software is difficult--what happens when you don't?

## Challenge Prompt
Now that we have at least inspected the binary, lets go a bit deeper. You can't just overflow the buffer with a bunch of A's--reverse engineer the software and figure out your payload format. Smash the stack to get the flag, no control necessary yet. Once you have a working exploit, fire it against the remote target to get the real flag.

*All challenges in this section use the same binary. The target is x86 and ASLR is on but it shouldn't be relevant to any of your exploits.*

corruption-sha256sum:`da69ccc4478fa246f53dce
f5db3694cfb49365c86e59f58a1ab5ce33f1ad3df1`

## Solution Guide
[solve.py](./resources/zyjlp-corruption/solve.py)

1. Pull the binary into Ghidra or binja and start reversing
2. Find the fgets in main and subsequent check for "UNLOCK" string
3. Determine that your payload must start with that value, then send excesss data to smash the stack

flag: `flag{look_like_ur_a_real_RE}`
