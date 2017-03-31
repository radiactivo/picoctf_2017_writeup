# PicoCTF_2017: What Is Web

**Category:** Web Exploitation
**Points:** 20
**Description:**

>Someone told me that some guy came up with the "World Wide Web", using "HTML" and "stuff". Can you help me figure out what that is? [Website](http://shell2017.picoctf.com:52334/).

**Hint:**

>How can you figure out how the webpage is actually built?

## Write-up
Viewing the [page source](index.html) gives us 1/3 of the flag, `fab79c49d9e`, viewing the [CSS source code](hacker.css) gives us 2/3 of the flag, `5ba511a0f24` and lastly viewing the [JS source code](script.js) gives us the last part of the flag `36308e33e85`.

Therefore, the flag is `fab79c49d9e5ba511a0f2436308e33e85`.