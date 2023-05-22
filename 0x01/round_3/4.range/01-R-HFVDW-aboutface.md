# AboutFace - 150pts
### 01-R-HFVDW
Author: Nate Singer (Helix)<br>
Challenge Resources: [./resources/hfvdw-aboutface/](./resources/hfvdw-aboutface/)

Can you get on the range? Can you break things? How many things can you break?

## Challenge Prompt
Different box this time, your target is now `10.128.0.4`--straight to root. Remember that there may be non-vulnerable services on the machine. Recon is the #1 focus. 

Once you have access to the box stay at the top of the hill and listen for flags on localhost:5000/tcp. You will get alive notices once every 60 seconds while you are connected so you can be sure that you'll receive flags at the specific release times. To see the release times check out the other section.

**Caviets**
You are root. This means you can do whatever you want, for the most part. You are welcome to lock people out but only in specific ways. If you accidentially take down any of the existing services or remove Nate's ability to SSH in for monitoring the machine will be reverted to the last known-good snapshot and you will probably lose access. This also goes for changing the flag files. If we determine that the flags has been altered the machine will also be reverted. Lastly, if someone has concurrent access for four flags in a row we may block them from future access to give others the opportunity to attack the machine--we'll decide this in real time during the weekend depending on how things go.

## Solution Guide
1. Recon the box with nmap and determine there are a handful of open ports
2. Banner grab to eventually find a webserver on 10000/tcp, determine service is webmin
3. Search for MSF exploits for webmin and find `exploit/linux/http/webmin_backdoor`
4. Set the exploit options for RHOST and reverse shell LHOST options
5. Execute and gain access as root, find the flag at `/root/flag.txt`

flag: `flag{bestow_the_crown}`
