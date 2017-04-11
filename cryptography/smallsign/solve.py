#! /usr/bin/env python3
##
# Script for PicoCTF SmallSign challenge
# Created by Amos (LFlare) Ng
##
import socket
import re
import time

s = socket.socket()
s.connect(("shell2017.picoctf.com", 5596))

def recv_line():
    r = ""
    while "\n" not in r:
        r += s.recv(1).decode()
    print(r)
    return r

def send(o):
    p = str(o) + "\n"
    s.sendall(p.encode())

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def gen_primes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        
        q += 1

recv_line() # Dump initial response

# Get initial n and e variables
n = int(re.findall("N: ([0-9]+)", recv_line())[0])
e = int(re.findall("e: ([0-9]+)", recv_line())[0])

# Get prime dictionaries
mappings = dict()
timeout = time.time() + 55
for i in gen_primes():
    print("Sending: %d" % i)
    send(i)
    signature = int(re.findall("([0-9]+)", recv_line())[1])
    mappings[i] = signature
    if len(mappings) > 400:
        break

# Get challenge
send(-1)
challenge = int(re.findall("([0-9]+)", recv_line())[1])
print(challenge)

# Do challenge
total = 1
factors = prime_factors(challenge)
print("C: %d" % challenge)
print("Prime Factors: " + "*".join(str(factor) for factor in factors))
for factor in factors:
    total *= mappings[factor]

total = total % n
print("Total: %d" % total)

# Try to submit
send(total)
recv_line()