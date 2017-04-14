# PicoCTF_2017: A Kaley Ceilidh

**Category:** Web Exploitation
**Points:** 175
**Description:**

>Everyone loves Scottish food [citation needed], but do you ever wish there were more hipster-y options? Well look no further than a [Kaley Ceilidh](http://shell2017.picoctf.com:8080/).

**Hint:**

>There's not a whole lot you can do on this application. If your normal attacks aren't working, perhaps you need to think bigger. Humongous, in fact.
The server probably won't show you anything that contains a "flag" property.

## Write-up
From the clue given, this is a common(_not really_) case of MongoDB exploitation. The basis of this exploit revolves around MongoDB's magical `$where` function followed by a slow bruteforce with time-based blind exploits.

[Python Script](solve.py)

Therefore, the flag is `flag{I_only_eat_0rg4n1c_flages}`.