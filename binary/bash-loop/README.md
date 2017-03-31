# PicoCTF_2017: Bash Loop

**Category:** Binary Exploitation
**Points:** 40
**Description:**

>We found a program that is hiding a flag but requires you to guess the number it is thinking of. Chances are Linux has an easy way to try all the numbers... Go to /problems/bd058e83a119c78a006543d23d9f6422 and try it out!

**Hint:**

>Either use SSH or use the Web Shell to get onto the shell server and navigate to the correct directory. Then do a quick Google search on 'bash loops'. You may need to use grep to filter out the responses as well!

## Write-up
Simple simple, just this code is sufficient!

    $ for iter in {0..4096}; do /problems/bd058e83a119c78a006543d23d9f6422/bashloop $iter | grep -v "Nope. Pick another number between 0 and 4096"; done
    Yay! That's the number! Here be the flag: d3aaad36e3947ceed96a916ca92d33b4 

Therefore, the flag is `d3aaad36e3947ceed96a916ca92d33b4`.