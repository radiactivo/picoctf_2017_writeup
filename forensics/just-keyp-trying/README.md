# PicoCTF_2017: Just Keyp Trying

**Category:** Forensics
**Points:** 80
**Description:**

>Here's an interesting capture of some data. But what exactly is this data? Take a look: [data.pcap](data.pcap)

**Hint:**

>Find out what kind of packets these are. What does the info column say in Wireshark/Cloudshark?
What changes between packets? What does that data look like?
Maybe take a look at http://www.usb.org/developers/hidpage/Hut1_12v2.pdf?

## Write-up
Another challenge, this time testing on your capabilities to read the title. We will extract the USB additional capture data and extract only the 3rd column where the keypress event is encoded into.

    $ tshark -r data.pcap -T fields -e usb.capdata | grep -v '00:00:00:00:00:00:00:00' | cut -d ':' -f 3
    09
    0f
    04
    0a
    00
    2f
    00
    13
    15
    20
    22
    22
    00
    2d
    00
    27
    11
    1a
    04
    15
    07
    16
    00
    2d
    00
    07
    08
    04
    09
    06
    05
    20
    1f
    00
    30
    00
    00
    06

Consulting the [USB specification manual](http://www.usb.org/developers/hidpage/Hut1_12v2.pdf?) for KEYPAD, granted in the challenge name, 
    
    09  F
    0f  L
    04  A
    0a  G
    00  
    2f  {
    00
    13  P
    15  R
    20  3
    22  5
    22  5
    00  
    2d  _
    00
    27  0
    11  N
    1a  W
    04  A
    15  R
    07  D
    16  S
    00
    2d  _
    00
    07  D
    08  E
    04  A
    09  F
    06  C
    05  B
    20  3
    1f  2
    00  
    30  }
    00
    00
    06  C

Therefore, the flag is `flag{pr355_0nwards_deafcb32}`.