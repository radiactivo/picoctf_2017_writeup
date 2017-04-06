# PicoCTF_2017: A Thing Called The Stack

**Category:** Reverse Engineering
**Points:** 60
**Description:**

>A friend was stacking dinner plates, and handed you [this](assembly.s), saying something about a "stack". Can you find the difference between the value of esp at the end of the code, and the location of the saved return address? Assume a 32 bit system. Submit the answer as a hexidecimal number, with no extraneous 0s. For example, the decimal number 2015 would be submitted as 0x7df, not 0x000007df

**Hint:**

>Where is the return address saved on the stack?
Which commands actually affect the stack?

## Write-up
Stacks are a common thing in the computerverse, simply because it's a highly efficient way of storing data by appending. To solve this challenge, you need to visualize the stack after the assembly code.

    [stack]
    ebp:        [old ebp]
    ebp-4:      [ebp]
    ebp-8:      [edi]
    ebp-12:     [esi]
    ebp-16:     [ebx]
    ebp-264:    0x1     <- esp
    ebp-268:    0x2
    ebp-272:    0x3
    ebp-276:    0x4

It so happens that we only need to find the difference, which is `264` or `0x108` in hexadecimal.

Therefore, the flag is `0x108`.