# PicoCTF_2017: TW_GR_E4_STW

**Category:** Web Exploitation
**Points:** 200
**Description:**

>Many saw the fourth installment of Toaster Wars: Going Rogue as a return to grace after the relative mediocrity of the third. I'm just glad it was made at all. And hey, they added some nifty new online scoreboard features, too!

**Hint:**

>Ooh, what a nifty scoreboard! If we get a bunch of people playing at once, we can have a race through the dungeon!

## Write-up
Execute this command right under Level 3 staircase to move up twice :D
    
    socket.emit("action", {type: "move", direction: 2});
    socket.emit("action", {type: "move", direction: 2});

Therefore, the flag is `im_still_upset_you_dont_get_to_keep_the_cute_scarves_in_the_postgame_a44703668b068b3fa9a7a83a8f466ace`.