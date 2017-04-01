# PicoCTF_2017: Programmers Assemble

**Category:** Reverse Engineering
**Points:** 75
**Description:**

>You found a text [file](assembly.s) with some really low level code. Some value at the beginning has been X'ed out. Can you figure out what should be there, to make main return the value 0x1? Submit the answer as a hexidecimal number, with no extraneous 0s. For example, the decimal number 2015 would be submitted as 0x7df, not 0x000007df

**Hint:**

>All of the commands can be found [here](https://en.wikipedia.org/wiki/X86_assembly_language) along with what they do.
It may be useful to be able to run the code, with test values.

## Write-up
So, first assembly challenge done.  We are given an assembly piece of code and let's identify what each part does.

    .global main                ; start main

    main:
        mov $XXXXXXX, %eax.     ; move XXXXXXX into EAX 
        mov $0, %ebx            ; move 0 into EBX
        mov $0x7, %ecx          ; move 7 into ECX
    loop:
        test %eax, %eax         ; if eax is 0
        jz fin                  ; jump to finish
        add %ecx, %ebx          ; else, add ecx to ebx
        dec %eax                ; decrement eax
        jmp loop                ; loop back
    fin:
        cmp $0xb47f, %ebx       ; if ebx = 46207,
        je good                 ; jump to good
        mov $0, %eax            ; else, move 0 return value to eax
        jmp end                 ; jump to return
    good:
        mov $1, %eax            ; move 1 return value to eax
    end:
        ret                     ; exit

Simple! We want the file to return `0x1`, so we naturally want `good:` to execute. However, for good to execute, we need `%ebx` to equal `46207` or `0xb47f`. The only way `%ebx` is actually incremented is by `%ecx`, whom adds `0x7` everytime the loop loops.

So, how do we get `%ebx` up to `46207`? Simple! We just have to loop `46207 / 7 = 6601` times! So, `XXXXXXX` has to be `6601`! Converting `6601` to hex gives us `0x19C9`

Therefore, the flag is `0x19C9`.