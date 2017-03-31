# PicoCTF_2017: Tutorial 3

**Category:** Tutorial
**Points:** 0
**Description:**

>Robin handed me some color [codes](codes.txt) the other day. They don't look like anything to me though. Can you help me find her favorite shade of red?

**Hint:**

>Once again, there are tools on the interwebz that can help! (There's a clear theme here, from the easiest pico problems, to the hardest ones in other CTFs, search engines are your friend!)

## Write-up
Unfortunately, making an automated tool would be more troublesome. We can use deductive guessing here though, since we know colour codes are RGB. Therefore, we are looking for a value there's greater in the first two hexadecimal digits than the rest.

    7A3B00
    6000C7
    67C700
    42FFFC
    C70002 <- this seems like the most likely candidate, and it's red too!
    0003C7
    007A78

Therefore, the flag is, `C70002`.