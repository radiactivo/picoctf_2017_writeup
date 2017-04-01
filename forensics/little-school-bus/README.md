# PicoCTF_2017: Little School Bus

**Category:** Forensics
**Points:** 75
**Description:**

>Can you help me find the data in this [littleschoolbus.bmp](littleschoolbus.bmp)?

**Hint:**

>Look at least significant bit encoding!!

## Write-up
First, we need to convert `littleschoolbus.bmp` to a ASCII binary form, then we need to extract the least significant bit? Maybe add bits together?

    with open("littleschoolbus.bmp", "rb") as file:
        data = file.read()

        bits = ""
        for c in data:
            lsb = str(c & 0x1)
            bits += lsb

        bytess = [chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)]
        lsbstr = "".join(bytess)
        print(lsbstr)
        if "flag" in lsbstr:
            break

Hmm... doesn't seem to contain the flag! I know, let's make it keep removing front bits till we get "flag"!

    for iter in range(16):
        with open("littleschoolbus.bmp", "rb") as file:
            data = file.read()
            data = data[iter:]

            bits = ""
            for c in data:
                lsb = str(c & 0x1)
                bits += lsb

            bytess = [chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)]
            lsbstr = "".join(bytess)
            print(lsbstr)
            if "flag" in lsbstr:
                break

Putting this into [search.py](search.py) and running it, we get,

    $ ./search.py
    # Lots of random crap
    ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿó°¤Ç­?ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ
    flag{remember_kids_protect_your_headers_5e31}ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿñü¿ÿÿÿÿÿÿÿÿÿÿÿÿÿÿ;lvØ^ÈÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÒY#YÿÿÿÿÿÿÿÿÿÿÿÿÿûÆã±Ûd=ÿÛÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿñ9lü;ÿÿÿÿÿÿÿÿÿÿÿÿñ¢NÛm°ÿÿÿýÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿòçÿÿüÿÿÿÿÿÿÿÿÿ
    # Even more random crap

Well, that worked!
Therefore, the flag is `flag{remember_kids_protect_your_headers_5e31`.