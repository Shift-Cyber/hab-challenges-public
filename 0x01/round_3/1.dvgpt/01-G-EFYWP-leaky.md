# Leaky - 75pts
### 01-G-EFYWP
Author: Nate Singer (Helix)<br>
Challenge Resources: [./resources/app-1_dvgpt/](./resources/app-1_dvgpt/)

ChatGPT is a powerful tool for nearly anything you can imagine, is it really secure?

## Challenge Prompt
People leave dumb comments about vulnerabilities all over client-side code... most modern web applications don't display all the possible code at once though, for a variety of reasons.

## Solution Guide
1. The first half of the flag is visible when the page is viewed but not the second
2. The second half requires the user to submit input so that the virutal DOM updates to the second component

flag: `flag{the_DOM_is_like_crazy_virtual_maaaan}`

## Hints
1. Modern web frameworks like React and Vue use a virtual DOM where they replace components dynamically with JavaScript
2. How can you get other components to show up on the page if they aren't displayed by default?
