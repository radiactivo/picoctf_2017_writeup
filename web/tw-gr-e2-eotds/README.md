# PicoCTF_2017: TW_GR_E2_EoTDS

**Category:** Web Exploitation
**Points:** 120
**Description:**

>Given the relative success of the first release, it was no surprise that a second installment in the TW:GR series was released. I can't beat this one either, though... those darn spatulas put an induction cooktop in the floor so I can't get to the flag! Can you get it for me? You can play the game [here](http://shell2017.picoctf.com:5753/).

**Hint:**

>Toasters can't go through induction cooktops because they're made of metal. However, it looks like there's a nice, friendly spatula on the last floor; and better yet, he's made of rubber! I'm sure he could be persuaded to go pick up the flag and bring it back to you.

## Write-up
This one was a fun one, making use of the Spatula's AI that forces it to go down a corridor if it already sees one. There's no real way to explain this but as the bot is moving down the vertical corridor in the room, move down, in the opposite direction. This tricks it's shortest distance movement AI to force it to get the flag for you.

Therefore, the flag is `i_dont_want_to_say_goodbye__gets_me_every_time_2fa00d62583c852b0e5ae11dcdcbabe1`.