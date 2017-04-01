# PicoCTF_2017: SoRandom

**Category:** Cryptography
**Points:** 75
**Description:**

>We found [sorandom.py](sorandom.py) running at shell2017.picoctf.com:16768. It seems to be outputting the flag but randomizing all the characters first. Is there anyway to get back the original flag?

**Hint:**

>How random can computers be?

## Write-up
Firstly, it doesn't seem to be a random random.
    
    $ nc shell2017.picoctf.com 16768
    Unguessably Randomized Flag: BNZQ:449xg472190mwx6869b8pt10rwo92624

Looking in the `sorandom.py` code, we see that the random generator has already been preseeded!

    random.seed("random")

Okay, [let's crack our Python knuckles and get to work.](crack.py)

    $ ./crack.py
    FLAG: 107bd559693aef6692e1ed55ebe29514

Therefore, the flag is `107bd559693aef6692e1ed55ebe29514`.