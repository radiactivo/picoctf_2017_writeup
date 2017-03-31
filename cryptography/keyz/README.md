# PicoCTF_2017: Keyz

**Category:** Cryptography
**Points:** 20
**Description:**

>While webshells are nice, it'd be nice to be able to login directly. To do so, please add your own public key to ~/.ssh/authorized_keys, using the webshell. Make sure to copy it correctly! The key is in the ssh banner, displayed when you login remotely with ssh, to shell2017.picoctf.com

**Hint:**

>There are plenty of tutorials out there. This one worked for me: https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2

## Write-up
Really simple, this one. Firstly, generate an *id_rsa* identity. Might as well go for the 4096-bit key while you are at it.

    $ ssh-keygen -b 4096
    Generating public/private rsa key pair.
    Enter file in which to save the key (/root/.ssh/id_rsa): 
    Created directory '/root/.ssh'.
    Enter passphrase (empty for no passphrase): 
    Enter same passphrase again: 
    Your identification has been saved in /root/.ssh/id_rsa.
    Your public key has been saved in /root/.ssh/id_rsa.pub.
    The key fingerprint is:
    SHA256:dc9Jgcpa7Ieh+HOc0YltffBabS66IupucLeUJwfgvao root@23ee096bfcb4
    The key's randomart image is:
    +---[RSA 4096]----+
    |                 |
    |  .     .  .     |
    | . o  .   ooo .  |
    |  . o    o+.+= . |
    |     +  S  =  +  |
    |. . * o.+.* .    |
    | o  .=o.+  .     |
    |  o oo *=.       |
    |E=+. .+++.       |
    +----[SHA256]-----+
    # No, none of that is real duh

Then, copy the contents of `~/.ssh/id_rsa.pub` into the clipboard. Next, open up PicoCTF web shell and create the folder `.ssh`. Then, run this command.

    $ echo "{PASTE_HERE}" >> ~/.ssh/authorized_keys

Now try SSH-ing into the box at `shell2017.picoctf.com` from your computer!

    $ ssh lflare@shell2017.picoctf.com
    The authenticity of host 'shell2017.picoctf.com (34.206.4.227)' can't be established.
    ECDSA key fingerprint is SHA256:ZIqVNC9hm15Z6mdDFCWC/H0+5MzSzXEhW3a+iHP1HM4.
    Are you sure you want to continue connecting (yes/no)? yes
    Warning: Permanently added 'shell2017.picoctf.com,34.206.4.227' (ECDSA) to the list of known hosts.
    Congratulations on setting up SSH key authentication!
    Here is your flag: who_needs_pwords_anyways

Therefore, the flag is `who_needs_pwords_anyways`.