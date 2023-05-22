# Controller - 150pts
### 01-C-DRWPE
Author: Nate Singer (Helix)<br>
Challenge Resources: [./resources/zyjlp-corruption/](./resources/zyjlp-corruption/)

Writing secure, high-quality software is difficult--what happens when you don't?

## Challenge Prompt
Nice, last step, you have a leak but not for the right function, how can we tackle this problem?

*All challenges in this section use the same binary. The target is x86 and ASLR is on but it shouldn't be relevant to any of your exploits.*

corruption-sha256sum:`da69ccc4478fa246f53dce
f5db3694cfb49365c86e59f58a1ab5ce33f1ad3df1`

## Solution Guide
[solve.py](./resources/zyjlp-corruption/solve.py)

1. Determine that we have another function to dump this flag via reversing
2. With this knowledge, locally calulate the offset as 67 bytes
3. Smash the instruction pointer with the leaked flag value plus the offset to dump the flag out

flag: `flag{almost_totally_full_control}`
