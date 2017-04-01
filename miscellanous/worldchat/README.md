# PicoCTF_2017: WorldChat

**Category:** Miscellanous
**Points:** 30
**Description:**

>We think someone is trying to transmit a flag over WorldChat. Unfortunately, there are so many other people talking that we can't really keep track of what is going on! Go see if you can find the messenger at shell2017.picoctf.com:11511. Remember to use Ctrl-C to cut the connection if it overwhelms you!

**Hint:**

>There are cool command line tools that can filter out lines with specific keywords in them. Check out 'grep'! You can use the '|' character to put all the output into another process or command (like the grep process)

## Write-up
Bash piping~

    $ nc shell2017.picoctf.com 11511 | grep flag
    06:37:16 personwithflag: My friend would like to meet you to help me spell 'raspberry' correctly
    06:37:16 whatisflag: my homegirlz need to meet up to understand me
    06:37:18 whatisflag: A dog with a cape has attacked my toes for the future of humanity
    06:37:18 ihazflag: my parents , in my opinion, are our best chance for the future of humanity
    06:37:18 personwithflag: that girl from that movie has attacked my toes for what, I do not know
    06:37:18 whatisflag: A huge moose gives me hope to make a rasberry pie
    06:37:19 whatisflag: Hungry jackolanterns give me hope for the future of humanity
    06:37:20 personwithflag: Anyone but me has attacked my toes to help me spell 'raspberry' correctly
    06:37:20 personwithflag: I wants to see me to drink your milkshake
    06:37:20 noihazflag: my parents , in my well-educated opinion, are our best chance to drink your milkshake
    06:37:20 ihazflag: Cats with hats give me hope to drink your milkshake
    06:37:20 noihazflag: My sworn enemy wants to see me to understand me
    06:37:21 personwithflag: Cats with hats , in my well-educated opinion, are our best chance to generate fusion power
    06:37:21 flagperson: this is part 1/8 of the flag - 8d84
    06:37:22 ihazflag: We are the best of friends to help me spell 'raspberry' correctly
    06:37:22 ihazflag: my homegirlz give me hope to create a self driving car
    06:37:22 noihazflag: Cats with hats give me hope to create a self driving car
    06:37:22 flagperson: this is part 2/8 of the flag - 913f

We seem to spot a common pattern `this is part 1/8 of the flag - 8d84`, let's try regexp!

    $ nc shell2017.picoctf.com 11511 | grep -Eo "this is part [0-9]\/8 of the flag - [a-z0-9]{4}"
    this is part 1/8 of the flag - 8d84
    this is part 2/8 of the flag - 913f
    this is part 3/8 of the flag - 84bd
    this is part 4/8 of the flag - 68a4
    this is part 5/8 of the flag - 6576
    this is part 6/8 of the flag - 3e48
    this is part 7/8 of the flag - d9d9
    this is part 8/8 of the flag - ca1c

Therefore, the flag is `8d84913f84bd68a465763e48d9d9ca1c`.
