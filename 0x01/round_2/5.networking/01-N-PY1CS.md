# Fish - 100pts
### 01-N-PY1CS
*Author: Nate Singer (Helix)*

Networking is the process of connecting different devices like computers and smartphones together so they can communicate and share information. It's like a group of friends sharing information and resources among themselves. Examples of networking include connecting to the internet and connecting computers together in an office or school environment. Networking also involves setting up and maintaining communication protocols, security measures, and other technical aspects to ensure smooth and secure communication among the devices. In summary, networking allows different devices to connect and share information, making it possible to access the internet, share files, and collaborate on projects.

## Teaching Points
1. What is a network protocol?
2. How can we see the most common protocols in a network capture?
3. How can we filter for a specific protocol in a network capture?

## Challenge Prompt
**NON-STANDARD FLAG FORMAT**

*All 75 and 100 point networking challenges use capture-1.pcapng*

What protocol is responsible for the most packets in this capture?

## Solution Guide
1. Navigate to statistics and then protocol hierarchy
2. You should see a very simple breakdown with the top protocols by % of packets

## Reference Material
### What is a network protocol?
A network protocol is a set of rules and standards that determine how devices on a network communicate with each other.

Think of it like a language that devices use to talk to each other. Just like how people from different countries use different languages to communicate, devices on a network use different protocols to communicate.

Network protocols define things like the format of the messages that devices exchange, how those messages are transmitted across the network, and how errors or other issues are handled. Common examples of network protocols include TCP (Transmission Control Protocol), which is used for reliable communication over the internet, and HTTP (Hypertext Transfer Protocol), which is used to transfer web content from servers to clients.

Without network protocols, devices on a network would not be able to communicate effectively, and the internet as we know it would not exist. By following a set of agreed-upon rules and standards, network protocols enable devices to communicate with each other and exchange information in a reliable and standardized way.

### How can we see the most common protocols in a network capture?
You can see the most common protocols in a network capture in Wireshark by following these steps:

1. Open Wireshark and load the capture file that you want to analyze.
2. Click on "Statistics" in the menu bar, then select "Protocol Hierarchy" from the drop-down menu.
3. A new window will open that shows the protocol hierarchy for the capture file. The protocols are listed in descending order of usage, with the most common protocol at the top.
4. You can expand each protocol to see more detailed statistics, such as the number of packets, bytes, and conversations that used that protocol.
5. You can also filter the protocol statistics by using the "Apply a Display Filter" box at the top of the window. This can be helpful if you want to focus on a specific protocol or set of protocols.

By following these steps, you can quickly see the most common protocols in a network capture and get a better understanding of the types of traffic that are present on the network. This information can be useful for troubleshooting network issues, identifying unusual traffic patterns, or optimizing network performance.

### How can we filter for a specific protocol in a network capture?
To filter for a specific protocol in a network capture using Wireshark, you can follow these steps:

1. Open Wireshark and load the capture file that you want to analyze.
2. Click on the "Filter" box located at the top of the Wireshark window.
3. Type the name of the protocol that you want to filter for in the "Filter" box. For example, if you want to filter for HTTP traffic, you would type "http" in the filter box.
4. Hit the "Enter" key or click the "Apply" button next to the filter box.
5. Wireshark will now display only the packets that match the specified protocol filter.

You can also create more advanced filters by using filter expressions. For example, to filter for HTTP traffic to a specific IP address, you could use the filter expression "ip.addr == 192.168.0.1 and http".

By using protocol filters, you can quickly and easily narrow down the network traffic to the specific protocol that you are interested in analyzing. This can be helpful for troubleshooting issues, identifying unusual network activity, or analyzing specific types of network traffic.
