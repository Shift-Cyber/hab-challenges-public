# Hammer -150pts
### 01-I-IHAL3
*Author: Nate Singer (Helix)*

Cloud computing is a way to use the internet to access and store data and software remotely. Instead of keeping files and programs on your own computer, you can access them through the internet on remote servers. This means you can access your files and programs from any device with an internet connection. It's like renting a space in a big computer building instead of having your own computer. It can also allow for cloud-based software that multiple users can access and collaborate on simultaneously. Cloud computing makes it easy to access and store data and software remotely.

## Teaching Points
1. What is Nmap?
2. What is banner grabbing?
3. What is metasploit?

## Challenge Prompt
Check out `oslyxpzcgs.qualifier.hackabit.com` and see if you can find the vuln. No help on this one, nothing crazy though... enumerate harder :)

The flag is stored in an environment variable.

**Flag:** flag{looks_like_you_found_the_right_nail}

## Solution Guide
1. exploit vsftpd 2.3.4 backdoor with telnet using USER someuser:) PASS somepass
2. connect to bind shell on tcp/6200

## Reference Material
### What is NMAP?
Nmap (Network Mapper) is a powerful open-source tool for network exploration and security auditing. It is used to discover hosts and services on a computer network, thus creating a "map" of the network. Nmap sends packets to network hosts and then analyzes the responses to determine what hosts and services are available, what operating systems and software versions they are running, and what vulnerabilities might be present.

Nmap is a command-line tool that runs on various operating systems such as Windows, Linux, and macOS. It has a wide range of features that make it an essential tool for network administrators, security professionals, and penetration testers. For example, it can perform host discovery, port scanning, service and application identification, OS detection, and vulnerability scanning. Nmap also supports a range of advanced features such as scripting, performance optimization, and flexible output options.

### What is banner grabbing?
Banner grabbing is a technique used by security professionals, hackers, and network administrators to obtain information about a remote system by analyzing the banner or response message that is returned when a connection is established with a service or application.

The banner is a message that is displayed by the service or application to identify itself and provide other information, such as the version number and other configuration details. The banner is often sent in clear text, which makes it possible to gather information about the remote system.

Banner grabbing can be performed manually by connecting to a service using telnet or netcat, and then reading the banner message that is returned. However, automated tools such as Nmap can also be used to perform banner grabbing on a large scale, making it a common technique used in network reconnaissance and vulnerability scanning.

Banner grabbing can be used for legitimate purposes such as system identification and vulnerability assessment, but it can also be used by attackers to identify specific vulnerabilities or to gain unauthorized access to a system. Therefore, it is important to protect against banner grabbing by disabling unnecessary services or modifying the banner message to avoid revealing sensitive information.

### What is Metasploit?
Metasploit is a widely used open-source framework for developing, testing, and executing exploits against remote systems. It provides a collection of pre-written exploit modules that can be used to test the security of a network, identify vulnerabilities, and launch attacks.

Metasploit has a powerful command-line interface and a graphical user interface (GUI) that makes it accessible to users with different levels of technical expertise. It also has a large and active community of developers who contribute to the framework by creating new modules and maintaining the existing ones.

The framework provides a wide range of tools, including exploit modules, payload modules, auxiliary modules, and post-exploitation modules. Exploit modules are designed to exploit vulnerabilities in target systems, while payload modules provide the means to deliver a malicious payload, such as a backdoor, to the target system. Auxiliary modules are used to perform specific tasks, such as port scanning or password cracking, while post-exploitation modules are used to maintain access to a system after it has been compromised.

Metasploit can be used for both offensive and defensive purposes. Penetration testers and ethical hackers use it to identify and test vulnerabilities in their own systems or in those of their clients, while security professionals and system administrators use it to identify vulnerabilities and implement security measures to protect against them.

It is important to note that Metasploit should only be used in a legal and ethical manner, with the proper authorization and consent from the target system owner. Misusing Metasploit can lead to serious legal and ethical consequences.