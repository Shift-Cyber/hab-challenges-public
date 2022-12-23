<img src=".rsrc/banner.png"/>

# Hack a Bit - Challenge Release
This is the official competition repository for Hack a Bit challenges. Once a round ends, quiz questions, challenges and supporting infrastructure will be published here, publicly, for everyone to view. You will also be able to run most of the challenges locally if you'd like to continue working on them after the round ends. Challenges are organized by year and then by round, please see the following for more information:

| ID   | Year      | Status  |
| ---- | --------- | ------- |
| 0x01 | 2022-2023 | Ongoing |

Shift Cyber believes that there is enormous value in being able to see and interact with the competition challenges after the final round ends. Many of the existing competitions don't publish challenges and lose out on a great learning opportunity as a result. Comeptiton staff believe that open sourcing competition material is just one more step towards providing beter, compehensive learning opportunities for students.

Please reach out to contact@shiftcyber.com if you have any questions.


## Infrastructure Note
Shift Cyber runs Hack a Bit on a flexible cloud backend within Google Cloud Platform. Specific details will be provided in the challenge descriptors on an as-required basis, but here are a few notes of general importance. Most challenges were developed as containerized applications and scaled in a dedicated Kubernetes cluster. As a result, for challenges that require state, a session token is used to maintain that state and Google Traffic Director retains routing configuration based on that state token. For any challenge using transport encryption (TLS), a reverse proxy is setup through that load balancer as well. Again, more details are provided in specific challenge context but this is significant in the point that you will not require this context to run the challenges locally.
