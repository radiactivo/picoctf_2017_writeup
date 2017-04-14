# PicoCTF_2017: Encrypted Shell

**Category:** Cryptography
**Points:** 190
**Description:**

>[This service gives a shell](dhshell.py), but it's password protected! We were able intercept [this encrypted traffic](traffic.pcap) which may contain a successful password authentication. Can you get shell access and read the contents of flag.txt?
The service is running at shell2017.picoctf.com:38314.

**Hint:**

>Are any of the parameters used in the key exchange weaker than they should be?

## Write-up
This challenge revolves on breaking the Diffie-Hellman key exchange. The hint given tells us that something is weak and upon observing the server code closely, we find that `a = random.randint(1, 2**46)`, which is surprisingly, a very small number.

So, we are then able to use the "Baby Step Giant Step" algorithm to try and reverse `a` from the given `A`. Additionally, since we know the range of `a`, we can run a `sqrt(a)` to limit the amount of small steps we have to take.

[Code](dhshell.py)

Therefore, the flag is `467de743e8f82e09b555426e322adba5`.