# PicoCTF_2017: Missing Identity

**Category:** Master
**Points:** 100
**Description:**

>Turns out, some of the files back from Master Challenge 1 were corrupted. Restore this one [file](file) and find the flag.

**Hint:**

>What file is this?
What do you expect to find in the file structure?
All characters in the file are lower case or numberical. There will not be any zeros.

## Write-up
This seems to be a zip file, [unzipped contents](unzipped) doesn't appear to contain flags, however we get an interesting error.

    Archive:  picoctf_2017_writeup/master/master_2/file
    file #1:  bad zipfile offset (local header sig):  0

Hmmm... Let's try to extract it with offsets

    $ dd if=file of=flag.png bs=1 count=93628 skip=43

Now we get a black PNG file? Hmm... Courtesy of @zst123, apparently [JD-GUI](http://jd.benow.ca/) happens to fix archives too! Doing a rename on `file` to `file.zip` and running it through JD-GUI gives us the flag! _Even though I'm sure that's cheating, heh!_

Therefore, the [flag](file.zip.src/flag.png) is `zippidydooda29494995`.