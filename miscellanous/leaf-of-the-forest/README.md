# PicoCTF_2017: Leaf of the Forest

**Category:** Miscellanous
**Points:** 30
**Description:**

>We found an even bigger directory tree hiding a flag starting at /problems/7d91c03dff81a9c95bffb6d69358c92d. It would be impossible to find the file named flag manually...

**Hint:**

>Is there a search function in Linux? Like if I wanted to 'find' something...

## Write-up
Well, apparently the solution for the previous [challenge](../leaf-of-the-tree/) is used for this one. So, lets `find` the flag!

    $ find /problems/7d91c03dff81a9c95bffb6d69358c92d/ -type f -name flag -exec cat {} \;
    7ffb59b2f309c09959ba333d0af88565

Easy!
Therefore, the flag is `7ffb59b2f309c09959ba333d0af88565`.