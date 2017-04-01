# PicoCTF_2017: LeakedHashes

**Category:** Cryptography
**Points:** 90
**Description:**

>Someone got hacked! Check out some service's password hashes that were leaked at hashdump.txt! Do you think they chose strong passwords? We should check... The service is running at shell2017.picoctf.com:53397!

**Hint:**

>See if you can crack any of the login credentials and then connect to the service as one of the users. What's the chance these hashes have actually already been broken by someone else? Are there websites that host those cracked hashes? Connect from the shell with nc.

## Write-up
Let's try to see what the login looks like.

    $ nc shell2017.picoctf.com 53397
    enter username:
    root
    root's password:

Well, damn, we only have root's hash. Let's do a simple `cat hashdump.txt | cut -d ':' -f 2` to retreive all password hashes and go down to our local rainbow table site to [solve all the hashes](solved.txt). We are unable to find out what's root's password but never mind that, let's try `christene`.

    $ nc shell2017.picoctf.com 53397
    enter username:
    christene
    christene's password:3lf1n
    welcome to shady file server. would you like to access the cat ascii art database? y/n
    y

         /\_/\ 
        ( o o )
      G-==_Y_==-M
          `-'
          
      /\ /\ 
      (O o)
    =(: ^ :)=  
      '*v*'
      
     |\_/|     
     (. .)
      =w= (\   
     / ^ \//   
    (|| ||)
    ,""_""_ .

         /\_/\ 
        ( o o )
       -==_Y_==- 
          `-'
        /\**/\ 
       ( o_o  )_)
       ,(u  u  ,),
      {}{}{}{}{}{}
      
      /\_/\ 
     ( o.o )
      > ^ <
      
           /\_/\ 
      /\  / o o \ 
     //\ \~(*)~/
     `  \/   ^ /
        | \|| ||  
        \ '|| ||  
         \)()-())
         
       A_A
      (-.-)
       |-|   
      /   \  
     |     |  __
     |  || | |  \___
     \_||_/_/
     
         /\__/\ 
        /`    '\ 
      === 0  0 ===
        \  --  /    - flag is 53c0bedf15f745eeed4a6c6c30a10f30

       /        \ 
      /          \ 
     |            |
      \  ||  ||  /
       \_oo__oo_/#######o
       
      /\___/\ 
     ( o   o )
     (  =^=  ) 
     (        )
     (         )
     (          )))))))))))
     
     /\ /\ 
     (O o)
    =(:^:)=  
       U
       
        _,,/|
        \o o' 
        =_~_=
        /   \ (\ 
       (////_)//
       ~~~
       
       /\     /\ 
      {  `---'  }
      {  O   O  }  
    ~~|~   V   ~|~~  
       \  \|/  /   
        `-----'__
        /     \  `^\_
       {       }\ |\_\_   W
       |  \_/  |/ /  \_\_( )
        \__/  /(_E     \__/
          (  /
           MM
           
                  ("`-''-/").___..--''"`-._
                   `6_ 6  )   `-.  (     ).`-.__.`)
                   (_Y_.)'  ._   )  `._ `. ``-..-'
                 _..`--'_..-_/  /--'_.' ,'
               (il),-''  (li),'  ((!.-'
               
    from http://user.xmission.com/~emailbox/ascii_cats.htm

Easy.
Therefore, the flag is `53c0bedf15f745eeed4a6c6c30a10f30`
