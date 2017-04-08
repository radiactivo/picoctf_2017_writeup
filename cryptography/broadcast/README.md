# PicoCTF_2017: Broadcast

**Category:** Cryptography
**Points:** 120
**Description:**

>You stumbled upon a group [Message](clue.txt). Can you figure out what they were sending? The string sent is ascii encoded as a hex number (submit the ascii string as the flag)

**Hint:**

>The same message, with a small exponent, is being encrypted with several different n values

## Write-up
This challenge involves the RSA Hastad Broadcast attack. In a true TLDR fashion, this attack refers to how if a small exponent is used and when a significant number of ciphertexts and public keys have been intercepted, the ciphertext can then be easily cracked.

[Sample pythonic script](solve.py).

    $ ./solve.py 
    Flag: broadcast_with_small_e_is_killer_20472673112

Therefore, the flag is `broadcast_with_small_e_is_killer_20472673112`.