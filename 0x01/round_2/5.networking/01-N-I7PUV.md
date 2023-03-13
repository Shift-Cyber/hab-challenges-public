# School - 125pts
### 01-N-I7PUV
*Author: Nate Singer (Helix)*

Networking is the process of connecting different devices like computers and smartphones together so they can communicate and share information. It's like a group of friends sharing information and resources among themselves. Examples of networking include connecting to the internet and connecting computers together in an office or school environment. Networking also involves setting up and maintaining communication protocols, security measures, and other technical aspects to ensure smooth and secure communication among the devices. In summary, networking allows different devices to connect and share information, making it possible to access the internet, share files, and collaborate on projects.

## Teaching Points
1. What is a subnet?
2. What is classful vs classless subnetting?
3. What is a host and broadcast address?

## Challenge Prompt
This ones gonna take a few steps:
- Take the input line by line
- Calculate the network and broadcast addresses of the subnet
- For each network address add up all the forth octets

Your challenge response (flag) is this total.

**Flag:** 25604

## Solution Guide
see solve.py

## Reference Material
### What is a subnet?
A subnet is a smaller network created from a larger network by dividing it into smaller groups of IP addresses. Subnetting is used to help divide a large network into smaller, more manageable segments, which can improve network security, performance, and organization.

In computer networking, an IP address is used to identify a device on a network, and a subnet mask is used to divide a larger network into smaller subnets. The subnet mask is a 32-bit value that determines which portion of an IP address represents the network address and which portion represents the host address. The network address is used to identify the subnet, while the host address is used to identify individual devices on the subnet.

Each subnet has its own network address and broadcast address, which are used to communicate with devices within the subnet. Devices within a subnet can communicate with each other directly, while devices in different subnets must communicate through a router.

### What is classful vs classless subnetting?
Classful and classless subnetting are two different methods used to divide a network into subnets.

Classful subnetting is an older method in which IP addresses are divided into classes (A, B, and C) based on the number of bits used for the network portion of the address. In classful subnetting, the size of the subnets is determined by the class of the IP address, and the subnet mask must be chosen from a predefined set of values that correspond to the IP address class. The disadvantage of classful subnetting is that it is limited in terms of the number of subnets that can be created, and it can lead to wasting of IP addresses if the subnet sizes do not match the actual needs of the network.

Classless subnetting, on the other hand, allows for the subnet mask to be chosen in any value, so that subnets can be created of any size. This allows for a more flexible and efficient use of IP addresses, as the subnet sizes can be chosen to match the specific needs of the network. The most widely used classless subnetting method today is Classless Inter-Domain Routing (CIDR), which uses a slash notation to specify the subnet mask in the IP address.

In summary, classful subnetting is limited in terms of subnet size and address utilization, while classless subnetting is more flexible and efficient in the use of IP addresses.

### What is a host and broadcast address?
In computer networking, a host address is an IP address that is assigned to a specific device on a network. The host address is used to identify and communicate with the device on the network.

A broadcast address is a special IP address that is used to send network messages to all devices on a network, rather than just a single device. The broadcast address is typically used for network management and maintenance tasks, such as updating the routing tables, sending broadcasts for name resolution, or sending broadcasts for network discovery.

When subnetting a network, the network address and broadcast address are assigned for each subnet. The network address is used to identify the subnet, while the broadcast address is used to send messages to all devices on the subnet. The first address in a subnet is typically reserved for the network address, while the last address in the subnet is reserved for the broadcast address. The remaining addresses in the subnet can be assigned to individual devices as host addresses.
