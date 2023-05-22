# Santa - 75pts
### 01-C-ZYJLP
Author: Nate Singer (Helix)<br>
Challenge Resources: [./resources/zyjlp-corruption/](./resources/zyjlp-corruption/)

Writing secure, high-quality software is difficult--what happens when you don't?

## Challenge Prompt
You all asked for it so here it is, an intro to binary exploitation!

Let's get started nice and simple, baby steps to reverse engineering (RE).

*All challenges in this section use the same binary. The target is x86 and ASLR is on but it shouldn't be relevant to any of your exploits.*

corruption-sha256sum:`da69ccc4478fa246f53dce
f5db3694cfb49365c86e59f58a1ab5ce33f1ad3df1`

## Solution Guide
1. Dump strings for the binary, flag is a plaintext string.

flag: `flag{baby_steps_gift_just_for_you}`
