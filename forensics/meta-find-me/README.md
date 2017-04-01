# PicoCTF_2017: Meta Find Me

**Category:** Forensics
**Points:** 70
**Description:**

>Find the location of the flag in the image: [image.jpg](image.jpg). Note: Latitude and longitude values are in degrees with no degree symbols,/direction letters, minutes, seconds, or periods. They should only be digits. The flag is not just a set of coordinates - if you think that, keep looking!

**Hint:**

>How can images store location data? Perhaps search for GPS info on photos.

## Write-up
Looking onto the GPS section of the image's metadata reveals

    Latitude: 7° 0’ 0” N
    Longitude: 96° 0’ 0” E

Without degree symbols, direction letters, minutes, seconds or periods, we get
    
    Latitude: 7
    Longitude: 96

Now, `7, 96` is not the answer, nor is any other combinations. So what are we missing? Let's open the file in hex form and do a search for `flag`.

    00005bb0:  0001 0300 1003 0203 0600 0000 0000 0000 0000 0000 00ff fe00  :........................
    00005bc8:  7522 596f 7572 2066 6c61 6720 6973 2066 6c61 675f 325f 6d65  :u"Your flag is flag_2_me
    00005be0:  7461 5f34 5f6d 655f 3c6c 6174 3e5f 3c6c 6f6e 3e5f 3163 3166  :ta_4_me_<lat>_<lon>_1c1f
    00005bf8:  2e20 4e6f 7720 6669 6e64 2074 6865 2047 5053 2063 6f6f 7264  :. Now find the GPS coord
    00005c10:  696e 6174 6573 206f 6620 7468 6973 2069 6d61 6765 2120 2844  :inates of this image! (D
    00005c28:  6567 7265 6573 206f 6e6c 7920 706c 6561 7365 2922 ffdb 0084  :egrees only please)"....

Easily found, we now have the format. Piecing together, we replace `<lat>` and `<lon>` with our previous coordinates.

Therefore, the flag is `flag_2_meta_4_me_7_96_1c1f`.