# PicoCTF_2017: Raw2Hex

**Category:** Reverse Engineering
**Points:** 20
**Description:**

>This program just prints a flag in raw form. All we need to do is convert the output to hex and we have it! CLI yourself to /problems/45f3b0abcf176b7cf7c1536b28d05d72 and turn that Raw2Hex!

**Hint:**

>Google is always very helpful in these circumstances. In this case, you should be looking for an easy solution.

## Write-up
This seems like another question of bash piping... Running `/problems/45f3b0abcf176b7cf7c1536b28d05d72/raw2hex` gives us raw binary data, with additional placeholder text infront. That needs to be filtered out first.

    # Accomplished by using ':' as a delimiter.
    $ /problems/45f3b0abcf176b7cf7c1536b28d05d72/raw2hex | cut -d ':' -f 2

Now, to hex it, we can simply use `xxd`, the wondertool~

    $ /problems/45f3b0abcf176b7cf7c1536b28d05d72/raw2hex | cut -d ':' -f 2 | xxd -plain
    cc76ae5c1b19d06897338d2deaa50bf00a

Therefore, the flag is `cc76ae5c1b19d06897338d2deaa50bf00a`.