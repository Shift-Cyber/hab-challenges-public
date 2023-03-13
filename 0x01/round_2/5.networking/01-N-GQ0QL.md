# Phonebook - 75pts
### 01-N-GQ0QL
*Author: Nate Singer (Helix)*

Networking is the process of connecting different devices like computers and smartphones together so they can communicate and share information. It's like a group of friends sharing information and resources among themselves. Examples of networking include connecting to the internet and connecting computers together in an office or school environment. Networking also involves setting up and maintaining communication protocols, security measures, and other technical aspects to ensure smooth and secure communication among the devices. In summary, networking allows different devices to connect and share information, making it possible to access the internet, share files, and collaborate on projects.

## Teaching Points
1. What is DNS?
2. What kinds of records can a DNS server hold?
3. How are DNS records looked up?

## Challenge Prompt
Check out the DNS records for ```qualifier.hackabit.com```... there's soemthing interesting there, all kinds of data...

## Solution Guide
1. Use dig or other record lookup tools to checkout the domain
2. There should be a flag record easily visible

## Reference Material
### What is DNS?
Imagine that the internet is like a giant phone book with millions of phone numbers for websites instead of people. Just like how you look up a friend's phone number in the phone book, your computer looks up the phone number (or IP address) of the website you want to visit on the internet.

DNS (Domain Name System) is like the operator that helps your computer find the phone number of the website you want to visit. Instead of looking up websites by their IP address (which is a long string of numbers), DNS translates the easy-to-remember website name (like google.com) to the corresponding IP address.

When you type a website name into your web browser, your computer sends a request to a DNS server to translate the website name into an IP address. The DNS server then returns the IP address to your computer, which can then connect to the website's server and display the webpage you want to see.

So, in simple terms, DNS is like a giant phone book for the internet that helps your computer find the websites you want to visit by translating the easy-to-remember website name into its corresponding IP address.


### What kinds of records can a DNS server hold?
A DNS (Domain Name System) server can serve different types of DNS records, each of which serves a different purpose. Here are some of the most common types of DNS records:

1. A (Address) record: This type of record maps a hostname (such as "example.com") to an IPv4 address (such as "192.0.2.1").
2. AAAA (IPv6 Address) record: This type of record maps a hostname to an IPv6 address.
3. MX (Mail Exchange) record: This type of record specifies the mail servers that are responsible for accepting email messages on behalf of a domain.
4. CNAME (Canonical Name) record: This type of record specifies an alias for a hostname, allowing multiple names to resolve to the same IP address.
5. TXT (Text) record: This type of record contains arbitrary text that can be used for various purposes, such as adding a human-readable description or specifying SPF (Sender Policy Framework) policies for email validation.
6. NS (Name Server) record: This type of record identifies the authoritative DNS servers for a domain.
7. SOA (Start of Authority) record: This type of record specifies the primary authoritative DNS server for a zone, and contains information about the zone's configuration.
8. These are just a few examples of the types of DNS records that a DNS server can serve. Each record type has a specific function and is used to help resolve domain names and provide services on the internet.


### How are DNS records looked up?
DNS (Domain Name System) records are looked up through a hierarchical system of servers that work together to translate human-readable domain names (such as www.example.com) into IP addresses (such as 192.0.2.1) that are used to identify and locate computer systems on the internet.

1. The process of looking up a DNS record typically involves the following steps:
2. The client computer sends a query to a local DNS resolver, such as the DNS server provided by the Internet Service Provider (ISP) or a local network.
3. If the local resolver has the requested DNS record cached in its memory, it returns the record to the client.
4. If the local resolver does not have the requested record cached, it forwards the query to a root DNS server.
5. The root DNS server responds to the query by referring the resolver to the top-level domain (TLD) server for the requested domain (such as .com, .org, .edu, etc.).
6. The TLD server responds to the query by referring the resolver to the authoritative DNS server for the requested domain.
7. The authoritative DNS server for the domain responds to the query by returning the requested DNS record, such as an IP address for a website.
8. The local DNS resolver caches the returned DNS record and returns it to the client.

The client computer can then use the returned IP address to establish a connection to the server associated with the domain name.

This process allows DNS queries to be resolved quickly and efficiently, and it enables the internet to function as a distributed and decentralized system of interconnected computers and networks.
