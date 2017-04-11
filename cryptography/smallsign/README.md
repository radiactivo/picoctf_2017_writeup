# PicoCTF_2017: SmallSign

**Category:** Cryptography
**Points:** 140
**Description:**

>This service outputs a flag if you can forge an RSA signature!
nc shell2017.picoctf.com 5596
[smallsign.py](smallsign.py)

**Hint:**

>RSA encryption (and decryption) is multiplicative.

## Write-up
This challenge mainly focuses on a simple concept of RSA, which is it's multiplicativity? Is that a word? Well, basically, this concept states that for a given signature of `m1`, `s1` and a signature of `m2`, `s2` would end up in the form where (`m1` * `m2`) = (`s1` * `s2`).

In this challenge, we are given the ability to make the server sign as many integers as we want for 60 seconds and then we have to also solve the challenge in that same time. This challenge is a random integer from `0` to `2**32`, which is a large number and something we cannot possibly get the server to sign to, within 60 seconds. However, we can take a shortcut and just try getting the server to sign a couple prime factors and then hoping for the RNG to get us a challenge that is factored up by the prime factors we have.

Lo and behold, [python script](solve.py) and shell loops.

    while true; do
        python3 -u smallsign.py | tee -a log
        sleep 3
    done

Therefore, the flag is `damnitiforgottosavetheflag`.