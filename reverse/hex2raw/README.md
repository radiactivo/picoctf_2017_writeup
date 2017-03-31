# PicoCTF_2017: Hex2Raw

**Category:** Reverse Engineering
**Points:** 20
**Description:**

>This program requires some unprintable characters as input... But how do you print unprintable characters? CLI yourself to /problems/33432c6de9329bca3a3ff26e5538d8f2 and turn that Hex2Raw!

**Hint:**

>Google for easy techniques of getting raw output to command line. In this case, you should be looking for an easy solution.

## Write-up
In simple python,

    $python -c "import base64; print('9b0f7b43804d4abd6f7e1bbe51
    5c55d5'.decode('hex'))" | /problems/33432c6de9329bca3a3ff26e
    5538d8f2/hex2raw
    Give me this in raw form (0x41 -> 'A'):                     
    9b0f7b43804d4abd6f7e1bbe515c55d5                            
                                                                
    You gave me:                                                
    9b0f7b43804d4abd6f7e1bbe515c55d5                            
    Yay! That's what I wanted! Here be the flag:
    84234a119cee0edf78366463973d518c

Therefore, the flag is `84234a119cee0edf78366463973d518c`.