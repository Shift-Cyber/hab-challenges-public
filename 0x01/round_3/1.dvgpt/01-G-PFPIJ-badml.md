# BadML - 125pts
### 01-G-PFPIJ
Author: Nate Singer (Helix)<br>
Challenge Resources: [./resources/app-1_dvgpt/](./resources/app-1_dvgpt/)

ChatGPT is a powerful tool for nearly anything you can imagine, is it really secure?

## Challenge Prompt
Where does all this data come from? Have you found all the app endpoints?

*The flag is located at* `./flag.txt`

## Solution Guide
1. Look through the traffic and see the GET to `/footer?message=default`
2. Play with it until you get the error: `Message file not found or inaccessible.`
3. Set this to flag.txt to pull the flag

flag: `flag{LFI_LetsgoFindIt}`
