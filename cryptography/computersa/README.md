# PicoCTF_2017: ComputeRSA

**Category:** Cryptography
**Points:** 50
**Description:**

>RSA encryption/decryption is based on a formula that anyone can find and use, as long as they know the values to plug in. Given the encrypted number 150815, d = 1941, and N = 435979, what is the decrypted number?

**Hint:**

>decrypted = (encrypted) ^ d mod N

## Write-up
Math time! Since most calculators have a character limit, let's use a Python calculator!

    >>> decrypt = (150815 ** 1941) % 435979
    >>> print(decrypt)
    133337

Therefore the flag is `133337`.