# Inspector - 100pts
### 01-T-EDLSF
Author: Nate Singer (Helix)<br>
Challenge Resources: [./resources/edlsf-inspector/](./resources/edlsf-inspector/)

It's hard to find excellent hackers, but its even harder to find excellent defenders.

## Challenge Prompt
It's just a simple stream investigation, how hard can it be?

Both challenges for this section use the same pcapng file.

triage.pcapng-sha256sum:caa094f0de3b78ce168e01e894218cbd5fcfbc10a909e93fc0980ca74dd89cc6

## Solution Guide
1. Can either search for curlys or something like g{, or can start by looking for http streams, but may be misleading
2. Eventually find partial flag data and do a TCP stream on a HTTP request instead of the full HTTP request

flag: `flag{tcp_streams_reveal_more}`
flag: `fl_nosearch_ag{tcp_streams_reveal_more}`
