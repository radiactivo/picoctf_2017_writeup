# PicoCTF_2017: Weird RSA

**Category:** Cryptography
**Points:** 90
**Description:**

>We recovered some [data](RSA.txt). It was labeled as RSA, but what in the world are "dq" and "dp"? Can you decrypt the ciphertext for us?

**Hint:**

>

## Write-up
Python and BigInteger to the rescue! Link to [script](solve.py). No idea why it would just work with `m2` alone, I need to learn my RSA more.

Therefore, the flag is `Theres_more_than_one_way_to_RSA`.