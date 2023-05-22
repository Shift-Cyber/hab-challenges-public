# Connection - 75pts
### 01-R-FHPXX
Author: Nate Singer (Helix)<br>
Challenge Resources: [./resources/fhpxx-connection/](./resources/fhpxx-connection/)

Can you get on the range? Can you break things? How many things can you break?

## Challenge Prompt
Author: Nate Singer (Helix)<br>

This section is a series of challenges in a semi-isolated cyber range. Your goal is to compromise the boxes and get the flags. Your first challenge is more of a sanity-check/confirmation. We wanted to use private keys for this but logistics of distributing them was challenge so its just password login for now. Check your email, at exactly 5pm PST Friday you received a credential and IP address for this jumpbox.

You will use this jumpbox to attack other machines in the network. We've installed nmap, metasploit and netcat for your convience. If you want other tooling installed later please reach out to staff and will consider those requests as you ask. Remember that you can use techniques like proxychains over SSH to emulate much of this functionality.

We're not gonna tell you were the flag is but I'm sure you can figure it out.

## Solution Guide
1. Login to the range with your provided username and password
2. Use the find command to locate the flag file: `find / -name flag.txt`
3. Cat out the flag to standard out, cat /opt/flag

flag: `flag{welcome_to_the_range}`
