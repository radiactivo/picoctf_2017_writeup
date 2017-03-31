#! /usr/bin/env python3
##
# Script for PicoCTF Looooong challenge
# Created by Amos (LFlare) Ng
##
import re
import socket

# Open socket
s = socket.socket()
s.connect(("shell2017.picoctf.com", 30277))

# Receive initial instructions
instructions = s.recv(4096).decode("utf-8")
print(instructions)

# Parse instructions
letter = re.search("'([A-Za-z])' character", instructions).group(1)
count = int(re.search("'([0-9]+)' times", instructions).group(1))
end = re.search("followed by a single '([a-zA-Z0-9])'", instructions).group(1)

# Parse reply
reply = (letter * count) + end + "\n"

# Send reply
s.send(reply.encode("utf-8"))

# Receive reply to reply
print(s.recv(4096).decode("utf-8"))
