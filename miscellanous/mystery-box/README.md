# PicoCTF_2017: Mystery Box

**Category:** Miscellanous
**Points:** 60
**Description:**

>You've found a mystery machine with a sticky note attached to it! Oh, there's also this picture of the machine you found.

**Hint:**

>It really gets your gears Turing.
I hear there's something Naval about it.

## Write-up
This seems to be a Enigma machine challenge. We are also given the following [note.txt](note.txt) about it.

    Geheimnis: PXQQ TAMY YDBC WGYE LVN
    Umkehrwalze: B
    Grundstellung: PPP
    Ringstellung: LOG
    Steckerbrett: G-L, H-F

Converting to English, we get,

    Secret: PXQQ TAMY YDBC WGYE LVN
    Reversing roller: B
    Basic position: PPP
    Positioning: LOG
    Plug connector: G-L, H-F

Okay. Let's try using an [Enigma machine with all this details filled in](http://enigma.louisedade.co.uk/enigma.html?m3;b;b123;ALOG;APPP;FH-GL).

    PXQQ TAMY YDBC WGYE LVN

gives us

    QUIT EPUZ ZLIN GIND EED
    QUITEPUZZLINGINDEED

Therefore, the flag is `QUITEPUZZLINGINDEED`.