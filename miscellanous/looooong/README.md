# PicoCTF_2017: Looooong

**Category:** Miscellanous
**Points:** 20
**Description:**

>I heard you have some "delusions of grandeur" about your typing speed. How fast can you go at shell2017.picoctf.com:30277?

**Hint:**

>Use the nc command to connect!
I hear python is a good means (among many) to generate the needed input.
It might help to have multiple windows open

## Write-up
With an easily designed [Python script](script.py), the flag prints out easily.

    $ ./script.py 
    To prove your skills, you must pass this test.
    Please give me the 'b' character '563' times, followed by a single '5'.
    To make things interesting, you have 30 seconds.
    Input:

    You got it! You're super quick!
    Flag: with_some_recognition_and_training_delusions_become_glimpses_493092611815c4e8f8eee8df7264c4c0

Therefore, the flag is `with_some_recognition_and_training_delusions_become_glimpses_493092611815c4e8f8eee8df7264c4c0`.