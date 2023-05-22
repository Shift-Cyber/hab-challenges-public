# bitsANDbytes - 125pts
### 01-C-NAHCW
Author: Nate Singer (Helix)<br>
Challenge Resources: [./resources/zyjlp-corruption/](./resources/zyjlp-corruption/)

Writing secure, high-quality software is difficult--what happens when you don't?

## Challenge Prompt
Now that you have the ability to smash the stack, it's time to get control of the instruction pointer. Use your reverse engineering to figure out proper addresses, we've given you the code required to pull the flag.

*All challenges in this section use the same binary. The target is x86 and ASLR is on but it shouldn't be relevant to any of your exploits.*

corruption-sha256sum:`da69ccc4478fa246f53dce
f5db3694cfb49365c86e59f58a1ab5ce33f1ad3df1`

## Solution Guide
[solve.py](./resources/zyjlp-corruption/solve.py)

1. In reversing, determine that we have a flag dumping function available and its even leaked for us
2. Use a cyclic to determine the proper offset locally and gain control of the instruction pointer
3. Smash the instruction pointer with the leaked flag value to dump the flag out

flag: `flag{big_ret2flag_energy}`
