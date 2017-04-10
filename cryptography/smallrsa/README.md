# PicoCTF_2017: SmallRSA

**Category:** Cryptography
**Points:** 120
**Description:**

>You intercepted a single message. However, it appears to be encrypted. Can you decrypt it? [Message](clue.txt)

**Hint:**

>Normally, you pick e and generate d from that. What appears to have happened in this case? What is likely about the size of d?

## Write-up
This challenge is an implementation of Wiener's RSA attack. I would like to give credits to [pablocelayes](https://github.com/pablocelayes/rsa-wiener-attack) for his wonderful library for this attack. He saved me from doing math.

[Script](solve.py)

Therefore, the flag is `flag{Are_any_RSA_vals_good_95979862524}`.