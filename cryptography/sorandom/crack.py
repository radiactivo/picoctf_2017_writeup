#! /usr/bin/env python
##
# Script for PicoCTF SoRandom challenge
# Created by Amos (LFlare) Ng
##
import socket
import random

# Open socket
s = socket.socket()
s.connect(("shell2017.picoctf.com", 16768))

# Receive initial instructions
instructions = s.recv(4096).decode("utf-8")
enc_flag = ": ".join(instructions.split(":")[1:]).strip()
flag = ""

# Seed random
random.seed("random")

for c in enc_flag:
    if c.islower():
        flag += chr((ord(c) - ord('a') - random.randrange(0, 26)) % 26 + ord('a'))
    elif c.isupper():
        flag += chr((ord(c) - ord('A') - random.randrange(0, 26)) % 26 + ord('A'))
    elif c.isdigit():
        flag += chr((ord(c) - ord('0') - random.randrange(0, 10)) % 10 + ord('0'))
    else:
        flag += c

print(flag)