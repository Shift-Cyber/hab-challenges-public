# Boat - 125pts
### 01-I-LJLHG
*Author: Nate Singer (Helix)*

Cloud computing is a way to use the internet to access and store data and software remotely. Instead of keeping files and programs on your own computer, you can access them through the internet on remote servers. This means you can access your files and programs from any device with an internet connection. It's like renting a space in a big computer building instead of having your own computer. It can also allow for cloud-based software that multiple users can access and collaborate on simultaneously. Cloud computing makes it easy to access and store data and software remotely.

## Teaching Points
1. What is virtual networking?
2. Why would we want to set a specific address on a docker container?
3. What is docker compose?

## Challenge Prompt
Sometimes we need to run a machine on a specific address or virtualize a network, get this running on: `172.22.1.11`.

https://hub.docker.com/r/nathanielsinger/hackabit0x01-infrastructure-container2

**Flag:** flag{its_just_an_address_man}

## Solution Guide
1. Use docker commands to create a subnet as required
2. When the image is run properly it should split out the flag

## Reference Material
### What is virtual networking?
Virtual networking refers to the creation of a virtual version of a network, typically a computer network, within a computer or other device. This virtual network operates in a similar manner to a physical network and can include virtual versions of devices such as servers, switches, and firewalls.

Virtual networking is often used in a variety of contexts, including data centers, cloud computing, and software-defined networking. In these environments, virtual networks provide a way to create isolated network environments that can be easily configured, managed, and scaled. They also provide a way to run multiple network configurations and applications on a single physical infrastructure.

Advantages of virtual networking include reduced hardware costs, increased flexibility, and improved scalability. Additionally, virtual networks can be used to test and develop new network configurations and technologies before implementing them in a physical environment.

### Why would we want to set a specific address on a docker container?
Setting a specific IP address on a Docker container can be useful in certain situations where you want to control the network configuration of your containers. There are several reasons why you might want to do this:

1. Network Isolation: By assigning a unique IP address to each container, you can create isolated network environments for different applications, services, or teams. This can help prevent network-based security threats and improve network performance.
2. Predictable Network Configuration: When you set a specific IP address for a container, you can ensure that the container will always have the same IP address, even if it's moved between hosts or restarted. This makes it easier to manage the network configuration of your containers and maintain predictable network behavior.
3. Communication between Containers: When you have multiple containers running on the same host, you can use specific IP addresses to establish communication between them. For example, you can set up a web server container and a database container, and then configure the web server container to communicate with the database container using its specific IP address.
4. Integration with External Services: If you want to integrate a container with an external service or network, setting a specific IP address can help ensure that the container is reachable and can communicate with the external service.

In summary, setting a specific IP address on a Docker container can provide network predictability, isolation, and control, making it an important tool for managing complex network environments.

### What is Docker Compose?
Docker Compose is a tool for defining and running multi-container Docker applications. It allows you to define the services that make up your application, as well as their configuration, in a single file called a docker-compose.yml file.

With Docker Compose, you can define and start all the services in your application with a single command. For example, you can define a web application that consists of a web server, a database, and a caching service, and then start all these services with a single command, rather than starting each service individually.

Docker Compose also provides other features that make it easier to manage and deploy multi-container applications. For example, it allows you to define environment variables, network configurations, and volumes that can be shared between containers. Additionally, it provides a way to scale individual services and manage the overall health of your application.

Docker Compose is particularly useful for local development and testing, as it provides a way to easily set up and run complex applications on a single machine. It also makes it easier to deploy multi-container applications to production, as you can define and manage the entire application and its dependencies in a single file.