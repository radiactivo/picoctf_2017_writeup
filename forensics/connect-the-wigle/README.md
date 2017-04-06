# PicoCTF_2017: Connect The Wigle

**Category:** Forensics
**Points:** 140
**Description:**

>Identify the data contained within [wigle](wigle) and determine how to visualize it. Update 16:26 EST 1 Apr If you feel that you are close, make a private piazza post with what you have, and an admin will help out.

**Hint:**

>Perhaps they've been storing data in a database. How do we access the information?
How can we visualize this data? Maybe we just need to take a step back to get the big picture?
Try zero in the first word of the flag, if you think it's an O.
If you think you're super close, make a private piazza post with what you think it is.

## Write-up
The solution to this challenge was very simple, except that if you are an over-thinker and over-analyzer like me, you tend to miss out on the easiest step.

Firstly, analysing the file tells us that it's an SQLite file, so let's open it up and view the data. Next, dumping the `lat` and `lon` to a CSV file and plotting it on a map... wait for it... gives us

![flag](flag.png)

My original attempt was foolish, trying to deduce any erroneous locations in the data and ploting that instead.

Therefore, the flag is `flag{f0und_m3_ee263b5f}`.