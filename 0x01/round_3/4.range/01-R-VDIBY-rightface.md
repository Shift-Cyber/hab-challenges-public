# RightFace - 100pts
### 01-R-VDIBY
Author: Nate Singer (Helix)<br>

Can you get on the range? Can you break things? How many things can you break?

## Challenge Prompt
If you did the more advanced challenges during the qualifier this should already be familiar.

Your goal here is to compromise the `10.128.0.5` machine and get access as the `breakme` user.

Remember that there may be non-vulnerable services on the machine. Recon is the #1 priority.

## Solution Guide
1. Scan the box with nmap and determine that port tcp/21 is open
2. Banner grab and determine `220 (vsFTPd 2.3.4)` probably means vulnerable
3. Locate MSF exploit `exploit/unix/ftp/vsftpd_234_backdoor`
4. Set options and fire for a shell as `breakme` user
5. List out to find `flag.txt` in immediate home directory

flag: `flag{remember_this_one?_pays_to_be_a_winner}`
