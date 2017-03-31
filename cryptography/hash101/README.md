# PicoCTF_2017: Hash101

**Category:** Cryptography
**Points:** 50
**Description:**

>Prove your knowledge of hashes and claim a flag as your prize! Connect to the service at shell2017.picoctf.com:9661

**Hint:**

>All concepts required to complete this challenge, including simple modular math, are quickly found by googling :)

## Write-up
This one is just a mess to document but I'll try my best. Firstly, do take note that none of the values will be the same everytime attempted. We will be using `nc` to connect as well.

    $ nc shell2017.picoctf.com 9661

    Welcome to Hashes 101!

    There are 4 Levels. Complete all and receive a prize!


    -------- LEVEL 1: Text = just 1's and 0's --------
    All text can be represented by numbers. To see how different letters translate to numbers, go to http://www.asciitable.com/

    TO UNLOCK NEXT LEVEL, give me the ASCII representation of 0111000001101100011000010110100101100100

    >plaid
    Correct! Completed level 1

Fairly simple, level 1 just requires a binary conversion.

    ------ LEVEL 2: Numbers can be base ANYTHING -----
    Numbers can be represented many ways. A popular way to represent computer data is in base 16 or 'hex' since it lines up with bytes very well (2 hex characters = 8 binary bits). Other formats include base64, binary, and just regular base10 (decimal)! In a way, that ascii chart represents a system where all text can be seen as "base128" (not including the Extended ASCII codes)

    TO UNLOCK NEXT LEVEL, give me the text you just decoded, plaid, as its hex and decimal equivalent

    hex>706c616964
    Good job! 706c616964 to ASCII -> plaid is plaid
    Now decimal
    dec>482854660452
    Good job! 482854660452 to Hex -> 706c616964 to ASCII -> plaid is plaid
    Correct! Completed level 2

This one was slightly tricky, because it wasn't asking for the decimal representation of the ascii, but rather the **of the hex**.

    ----------- LEVEL 3: Hashing Function ------------
    A Hashing Function intakes any data of any size and irreversibly transforms it to a fixed length number. For example, a simple Hashing Function could be to add up the sum of all the values of all the bytes in the data and get the remainder after dividing by 16 (modulus 16)

    TO UNLOCK NEXT LEVEL, give me a string that will result in a 10 after being transformed with the mentioned example hashing function

    >18
    incorrect. sum of all characters = 105 mod 16 = 9 does not equal 10
    >19
    Correct! Completed level 3

Just bruteforce it, it's modulus 16, not modulus 2^16.

    --------------- LEVEL 4: Real Hash ---------------
    A real Hashing Function is used for many things. This can include checking to ensure a file has not been changed (its hash value would change if any part of it is changed). An important use of hashes is for storing passwords because a Hashing Function cannot be reversed to find the initial data. Therefore if someone steals the hashes, they must try many different inputs to see if they can "crack" it to find what password yields the same hash. Normally, this is too much work (if the password is long enough). But many times, people's passwords are easy to guess... Brute forcing this hash yourself is not a good idea, but there is a strong possibility that, if the password is weak, this hash has been cracked by someone before. Try looking for websites that have stored already cracked hashes.

    TO CLAIM YOUR PRIZE, give me the string password that will result in this MD5 hash (MD5, like most hashes, are represented as hex digits):
    811edc316305926e9883e2c283b8714c

    >k1dk1n
    Correct! Completed level 4

Clue has been given, just look to [HashKiller](https://hashkiller.co.uk/md5-decrypter.aspx)

    You completed all 4 levels! Here is your prize: c3ee093f26ba147ccc451fd13c91ffce

Therefore, the flag is `c3ee093f26ba147ccc451fd13c91ffce`.
