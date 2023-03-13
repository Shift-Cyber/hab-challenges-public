# Delegate - 100pts
### 01-W-9FHJZ
*Author: Nate Singer (Helix)*

Web applications, also known as "web apps," are software programs that run on the internet. They can be accessed using a web browser, like Google Chrome or Safari, on any device that has internet access. Web apps can do many things, like let you check your email, shop online, or play games. They are different from traditional desktop apps that you have to install on your computer. Web apps are built using programming languages like HTML, CSS, and JavaScript, and they run on servers that are connected to the internet. Examples of web apps include Google Docs, Facebook, and Instagram.

## Teaching Points
1. What is a webhook?
2. Can we use a webhook to determine exploitation?
3. How can we harvest data with webhooks or redirection?

## Challenge Prompt
When we get code execution by compromising a web application, we generally want to exfiltrate some data. The staff did the hard part and gave you code execution, now just exfil that data!
https://erpvlnzxrh.qualifier.hackabit.com/delegate

## Solution Guide
1. Generate an epoch sometime in the near future
2. Setup a request bin or local server to receive connections
3. Trigger the POST request to the destination until it hits and sends the flag as a header

## Reference Material
### What is a webhook?
A webhook is like a special phone number that a website gives to another website. When something happens on the first website, like someone buying something, it calls the special phone number and gives the second website a message about what happened.

Think of it like this, Imagine you and your friends have a group chat. When one of your friends buys a new video game, they want to tell the rest of the group. Instead of typing it out and sending the message to the group chat, they set up a webhook between the video game store and the group chat. Now, every time they buy a new game, the store automatically sends a message to the group chat telling everyone what they bought. This way, your friend doesn't have to manually send a message every time they buy a game and the rest of the group is always up-to-date.

Webhooks are a way for different websites to talk to each other and share information automatically, instead of needing a person to do it manually.

### What is a RequestBin?
RequestBin is a simple online service that allows you to inspect and debug HTTP requests. It acts as a "dummy" endpoint for webhooks and other HTTP requests, allowing you to see the request headers, query string, and POST data of incoming requests.

When you create a RequestBin, it will give you a unique URL that you can use as the endpoint for your webhooks or other HTTP requests. When a request is sent to that URL, RequestBin will capture the request data and make it available for you to view and inspect. This can be useful for development and testing, as it allows you to see exactly what data is being sent by the webhook or other HTTP request, without having to build and run a full-featured endpoint. It can also be used for example in case you have a webhook set up in a website and you want to test it, you can use a requestbin as the endpoint to check if the webhook is working properly and what data it's sending.

### What is an epoch ie: "epoch time?"
Epoch time, also known as Unix time or POSIX time, is the number of seconds that have elapsed since January 1, 1970, at 00:00:00 Coordinated Universal Time (UTC). This point in time is called the "epoch."

Epoch time is commonly used in computer systems and programming languages as a way to represent and manipulate date and time. Because it is a simple count of seconds, it is easy to perform arithmetic operations on epoch time values, such as adding or subtracting a number of seconds to find a new date and time. In summary, Epoch time is a standard way to represent time in computing and networking, it is a count of seconds that have passed since the reference date of January 1, 1970, and it allows for easy arithmetic operations and conversions to other date and time formats.

### What is port forwarding?
Port forwarding is like a virtual doorman for your computer. When you have a website or a game server running on your computer, you want people from all over the internet to be able to access it. However, your computer is behind a firewall (like a security guard) that only lets certain people in.

Port forwarding is a way to tell the firewall which door to use. Imagine your computer is a house and your website is a room inside. The firewall is the front door and the internet is the street. When someone on the street wants to visit your website, they knock on the front door (the firewall). The port forwarding is like giving the firewall a note that says "let this person in and take them to room X" (the website or the game server).

So, Port forwarding allows specific traffic to reach specific devices on your local network based on the port number, even though the device is behind a firewall. It's like giving a key to a friend so they can enter your house through the back door instead of the front door.

### External References
- https://requestbin.com/
- https://www.youtube.com/watch?v=-5wpm-gesOY
