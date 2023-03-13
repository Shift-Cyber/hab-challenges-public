# Brain - 125pts
### 01-W-WAYZ6
*Author: Nate Singer (Helix)*

Web applications, also known as "web apps," are software programs that run on the internet. They can be accessed using a web browser, like Google Chrome or Safari, on any device that has internet access. Web apps can do many things, like let you check your email, shop online, or play games. They are different from traditional desktop apps that you have to install on your computer. Web apps are built using programming languages like HTML, CSS, and JavaScript, and they run on servers that are connected to the internet. Examples of web apps include Google Docs, Facebook, and Instagram.

## Teaching Points
1. How can you continue to use a website without reauthenticating every time?
2. Can an attacker bypass authentication if they obtain this token?
3. Whats the difference between headers and cookies?

## Challenge Prompt
Only admins can get flags... follow the rules!

**Flag:** flag{insaayne_in_da_membrain}

## Solution Guide
1. Set the header flag-sauce
2. Set the url query param to the secret value through intruder
3. Set the query parameter give-me-that-flag to hand-it-over
4. Forge the JWT (no signature validation)

## Reference Material
### What is BurpSuite
Burp Suite is a web application security testing platform that provides a suite of tools for security testing of web applications. It is widely used by security professionals and penetration testers to identify and exploit vulnerabilities in web applications. The suite consists of various tools for tasks such as intercepting and modifying web traffic, discovering and testing for vulnerabilities, and automating security scans. Some of the most popular tools included in the suite are the Burp Proxy, Burp Scanner, and Burp Intruder. These tools allow security professionals to test and validate the security of web applications, both during the development process and after deployment.

### What is OWASP ZAP
OWASP ZAP (Zed Attack Proxy) is an open-source web application security tool that helps identify vulnerabilities in web applications. It is designed to be used by both professional security testers and less experienced users who are looking to test the security of their own web applications.

OWASP ZAP provides a graphical user interface and a set of automated tools for testing the security of web applications. Some of the features offered by OWASP ZAP include vulnerability scanning, active and passive vulnerability testing, and a proxy for intercepting and modifying web traffic. The tool also provides a set of plugins that can be used to extend its functionality and integrate it with other tools and platforms.

OWASP ZAP is one of the most popular web application security testing tools available, and it is widely used by organizations around the world to ensure the security of their web applications. Its popularity can be attributed to its ease of use, powerful features, and the fact that it is open-source and free to use.

### How do I use Intruder for brute force attacks in BurpSuite?
Intruder in Burp Suite is a powerful tool that can be used to perform brute force attacks on web applications. The basic steps for using Intruder for brute force attacks in Burp Suite are as follows:

1. Capture the request: First, you need to capture the request you want to test. This can be done by sending a request to the target web application through the Burp Suite Proxy, and then selecting the request in the Proxy history tab.
2. Launch Intruder: Next, you need to launch Intruder by right-clicking on the captured request and selecting "Send to Intruder".
3. Configure the attack type: In the Intruder tab, select the "Brute Force" attack type and choose the appropriate options for the attack. For example, you can specify the type of payload to be used for the attack, the attack method, and the position of the payload in the request.
4. Configure the payloads: Next, you need to configure the payloads that will be used in the attack. For a brute force attack, you can specify a list of commonly used passwords or generate a list of payloads using a custom rule set.
5. Start the attack: Once you have configured the attack, you can start the attack by clicking the "Start Attack" button. Intruder will send a series of requests to the target web application, each with a different payload.
6. Analyze the results: After the attack is complete, you can analyze the results in the Intruder tab. The results will show you which requests resulted in a valid response and which ones failed. If any of the payloads resulted in a valid response, it is likely that the target web application is vulnerable to brute force attacks.
