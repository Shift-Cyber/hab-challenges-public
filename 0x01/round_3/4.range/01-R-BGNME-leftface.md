# LeftFace - 125pts
### 01-R-BGNME
Author: Nate Singer (Helix)<br>
Challenge Resources: [./resources/bgnme-leftface/](./resources/bgnme-leftface/)

Can you get on the range? Can you break things? How many things can you break?

## Challenge Prompt
With access to `10.128.0.5` your goal is to escalate priveleges to the `breakme-harder` user. Ultimately your goal is simply to read out the flag in `/home/breakme-harder/`.

## Solution Guide
1. Notice that there is a file in breakme that is owned by breakme-harder in /home/breakme
2. Determine that this file is probably the compiled result of escalate.c
3. Find that the program just reads a file and also has the SUID bit set to allow owner exec
4. Use this SUID application to read out the file

flag: `flag{evaluate_this_my_dude}`
