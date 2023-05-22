# Coverup - 125pts
### 01-T-TEPGG
Author: First Last (Handle)<br>
Challenge Resources: [./resources/tepgg-coverup/](./resources/tepgg-coverup/)

It's hard to find excellent hackers, but its even harder to find excellent defenders.

## Challenge Prompt
There is a challenge hidden in coverup.jpg, extract the flag and profit.

challenge.jpg-SHA256:f5c569d91e91fa753151f570fd1534316205b25b40e1037e8a4af86e1bdd0672

## Solution Guide
1. steghide extract -sf challenge.jpg

flag: `flag{the_truth_is_burried_deep}`
