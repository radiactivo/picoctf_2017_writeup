#! /usr/bin/env python2 -u
##
# Script for PicoCTF Encrypted Shell challenge
# Created by Amos (LFlare) Ng
##
import binascii
import math

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Random import random
from hashlib import sha256
from pwn import *

BLOCK_SIZE = 16
R = Random.new()

# Define functions
def pad(m):
    o = BLOCK_SIZE - len(m) % BLOCK_SIZE
    return m + o * chr(o)

def unpad(p):
    return p[0:-ord(p[-1])]

def encrypt(KEY, m):
    IV = R.read(BLOCK_SIZE)
    aes = AES.new(KEY, AES.MODE_CBC, IV)
    c = aes.encrypt(pad(m))
    return (IV + c).encode('hex')

def decrypt(KEY, data):
    data = data.decode("hex")
    IV, data = data[:BLOCK_SIZE], data[BLOCK_SIZE:]
    aes = AES.new(KEY, AES.MODE_CBC, IV)
    m = unpad(aes.decrypt(data))
    return m

# def send_encrypted(KEY, m):
#     IV = R.read(BLOCK_SIZE)
#     aes = AES.new(KEY, AES.MODE_CBC, IV)
#     c = aes.encrypt(pad(m))
#     print (IV + c).encode('hex')

# def read_encrypted(KEY):
#     data = raw_input("").decode('hex')
#     IV, data = data[:BLOCK_SIZE], data[BLOCK_SIZE:]
#     aes = AES.new(KEY, AES.MODE_CBC, IV)
#     m = unpad(aes.decrypt(data))
#     return m

def baby_steps_giant_steps(a,b,p,N = None):
    if not N: N = 1 + int(math.sqrt(p))
    #initialize baby_steps table
    print("Calculating steps")
    baby_steps = {}
    baby_step = 1
    for r in range(N+1):
        if r % 2**16 == 0:
            print("Percent done: %f" % float(r/(N+1)))
        baby_steps[baby_step] = r
        baby_step = baby_step * a % p
    #now take the giant steps
    print("Calculating strides")
    giant_stride = pow(a,(p-2)*N,p)
    giant_step = b
    for q in range(N+1):
        if q % 2**10 == 0:
            print("Percent done: %f" % float(q/(N+1)))
        if giant_step in baby_steps:
            return q*N + baby_steps[giant_step]
        else:
            giant_step = giant_step * giant_stride % p
    return "No Match"

# Define variables we already got [NEVER CHANGES]
p = 174807157365465092731323561678522236549173502913317875393564963123330281052524687450754910240009920154525635325209526987433833785499384204819179549544106498491589834195860008906875039418684191252537604123129659746721614402346449135195832955793815709136053198207712511838753919608894095907732099313139446299843
g = 41899070570517490692126143234857256603477072005476801644745865627893958675820606802876173648371028044404957307185876963051595214534530501331532626624926034521316281025445575243636197258111995884364277423716373007329751928366973332463469104730271236078593527144954324116802080620822212777139186990364810367977

# Define variables we got via PCAP
A = 67181814729672809761944050466345552000714783646540901930077503693498170494471454851066298597679442852319568001289661546435648233238995196316802191778255119575580452230094899649977878518905088843026410218490949156120753891179173584607658377516175604936785812188749505637009707185810818784317824948312833338391
B = 163474327496165970317455611040194226229768110972536491568651758882130515040592302060545195664691105903502590602299991774324422854288488808643183406531411211451668819946091756019968807934251380152454678794309029552368443330724418857477641084315795148167477913305656197307417202915201190742468386527305175908680

# Calculate a
# a = baby_steps_giant_steps(g, A, p, N=8388608)
a = 64470505087224
# Calculate common K and KEY
K = pow(B, a, p)
KEY = sha256(str(K).encode()).digest()

# Get password from pcap
password = "93dc028122341e84d2c6da68877a709d76ebd64cb13b2e1df5c69d798cb38f3014fcc821ccb1fb9ccf49ce23877f1b3d6f7db349b0c0e5d421a3b98ab591dd9a".decode("hex")
IV, password = password[:BLOCK_SIZE], password[BLOCK_SIZE:]
aes = AES.new(KEY, AES.MODE_CBC, IV)
password = unpad(aes.decrypt(password))
print("Password: %s" % password)

# Create a tube
t = remote("shell2017.picoctf.com", 38314)

# Receive A value
t.recvuntil("A = ")
A = int(t.recvuntil("\nPlease supply B: ", drop=True))
print("A: %d" % A)

# Generate our own key
b = random.randint(1, 2**46)
B = pow(g, b, p)
print("b: %d" % b)
print("B: %d" % B)

# Send our B
t.sendline(str(B))

# Generate shared key
K = pow(A, b, p)
KEY = sha256(str(K)).digest()
print("KEY: %s" % KEY)

t.sendline(encrypt(KEY, password))

# Check if we have shell :D
while True:
    payload = raw_input("$ ")
    print("SEND<< " + payload)

    payload = encrypt(KEY, payload)
    print("RAWSEND<< " + payload)

    t.sendline(payload)

    reply = t.recv()
    print("RAWRECV>> " + reply)

    reply = decrypt(KEY, reply)
    print("RECV>> " + reply)
