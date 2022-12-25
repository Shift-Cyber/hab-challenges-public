<img src=".rsrc/banner.png"/>

# Hack a Bit 0x01
Challenge Respository for the 2022-2023 Competition Season


## Overview
The Hack a Bit 2022-2023 competition season, marked 0x01 is the first year that Shift Cyber and the College Options Foundation have come together to put on a cyber competition. Throughout three rounds, competitors will battle it out by hacking, cracking, and attcking challenges. This repository contains all quiz questions, challenges and supporting infrastructure from the 0x01 competition. Details for each round are specified in following sections.


## Challenge Overview
### [Round 1](./round_1)
Round one is designed to test a competitors current competency level. It is a quick quiz within the Flexiquiz testing environment. Limited to 30 minutes, the competitor answers 30 questions within six catagories of cyber security. The first round is designed to achieve a baseline and allow staff to scope the second round approperiately.

### Round 2
*pending release...*

### Round 3
*pending release...*


## Infrastructure
Shift Cyber runs Hack a Bit on a flexible cloud backend within Google Cloud Platform. Specific details will be provided in the challenge descriptors on an as-required basis, but here are a few notes of general importance. Most challenges were developed as containerized applications and scaled in a dedicated Kubernetes cluster. As a result, for challenges that require state, a session token is used to maintain that state and Google Traffic Director retains routing configuration based on that state token. For any challenge using transport encryption (TLS), a reverse proxy is setup through that load balancer as well. Again, more details are provided in specific challenge context but this is significant in the point that you will not require this context to run the challenges locally.
