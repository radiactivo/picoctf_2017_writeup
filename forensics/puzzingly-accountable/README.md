# PicoCTF_2017: Puzzingly Accountable

**Category:** Forensics
**Points:** 100
**Description:**

>We need to find a password. It's likely that the updated passwords were sent over the network. Let's see if that's true: [data.pcap](data.pcap). Update 16:26 EST 1 Apr If you feel that you are close, make a private piazza post with what you have, and an admin will help out. The ones and sevens unfortunately look like each other.

**Hint:**

>How does an image end up on your computer? What type of packets are involved?

## Write-up
A challenge that tests whether you noticed a `/secret/*.png` GET request and then a manual individual TCP stream of each GET request to pngs.

Therefore, the flag is `953c5041c35bfebdf8625c3d517daa65`.