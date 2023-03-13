# Nevermind - 100pts
### 01-W-5AHCX
*Author: Nate Singer (Helix)*

Web applications, also known as "web apps," are software programs that run on the internet. They can be accessed using a web browser, like Google Chrome or Safari, on any device that has internet access. Web apps can do many things, like let you check your email, shop online, or play games. They are different from traditional desktop apps that you have to install on your computer. Web apps are built using programming languages like HTML, CSS, and JavaScript, and they run on servers that are connected to the internet. Examples of web apps include Google Docs, Facebook, and Instagram.

## Teaching Points
1. What are request types in regards to web applications?
2. Why do we care about using the right request type?
3. How can we send different types of requests?

## Challenge Prompt
If you take something, you gotta put it back, or something at least:
https://erpvlnzxrh.qualifier.hackabit.com/nevermind

## Solution Guide
1. Download the provided image
2. Hash it and post back the hash to receive the flag

## Reference Material
### What is a checksum?
A checksum is a way to check if a file or data you have is the exact same as the original. Imagine you're getting a recipe from a friend over the phone, but you're worried that you might have misunderstood some of the instructions. To make sure you have the right recipe, your friend could give you a "checksum" of the recipe, which is like a special code that they came up with using the recipe. Then, after you write down the recipe, you can use the same method to make your own checksum and compare it to your friend's. If the checksums match, you know you have the correct recipe. If not, you know there's a mistake and you'll need to double-check the instructions.

Checksums can also be used for digital files, like pictures or videos, to make sure that what you're downloading is the same as the original and wasn't changed or corrupted during the download process.

### What are request methods?
A request method is a way for a client (such as a web browser) to communicate with a server (such as a website) and ask it to perform a specific action. The most commonly used request methods in HTTP (Hypertext Transfer Protocol) are:

1. GET: This is used to retrieve information from the server. For example, when you enter a URL into your web browser and press enter, the browser sends a GET request to the server to retrieve the webpage associated with that URL.
2. POST: This is used to send information to the server. For example, when you fill out a form on a webpage and click the submit button, the browser sends a POST request to the server with the form data.
3. PUT: This is used to update information on the server. For example, when you want to change the content of a web page, the browser sends a PUT request to the server with the updated content.
4. DELETE: This is used to delete information from the server. For example, when you want to delete a file or a record from a database, the browser sends a DELETE request to the server.

There are other request methods as well like HEAD, OPTIONS, CONNECT, TRACE, PATCH but they are not as common as the above mentioned ones. Each request method has its own specific use case, and the server will respond differently depending on which method is used.

### How can we submit web requests in testing/development?
There are several ways to manually generate web requests without using a web browser, here are a few examples:

1. cURL: cURL is a command-line tool that allows you to send web requests from the terminal or command prompt. It can be used to send GET, POST, PUT, and DELETE requests, among others. It's like a phone call but instead of talking to someone, you're sending messages to a website.
2. Postman: This is an API development tool that allows you to easily send web requests, inspect the response, and view the headers. It's like a phone call but instead of talking to a person, you're talking to a computer.
3. Python: Python is a programming language that can be used to send web requests using a library called "requests." This allows you to send GET, POST, PUT, and DELETE requests, among others. It's like sending a message to a friend but instead of sending it to a person, you're sending it to a website.

### External Reference
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST
- https://www.postman.com/
