# PicoCTF_2017: Special Agent User

**Category:** Forensics
**Points:** 50
**Description:**

>We can get into the Administrator's computer with a browser exploit. But first, we need to figure out what browser they're using. Perhaps this information is located in a network packet capture we took: [data.pcap](data.pcap). Enter the browser and version as "BrowserName BrowserVersion". NOTE: We're just looking for up to 3 levels of subversions for the browser version (ie. Version 1.2.3 for Version 1.2.3.4) and ignore any 0th subversions (ie. 1.2 for 1.2.0)

**Hint:**

>Where can we find information on the browser in networking data? Maybe try reading up on user-agent strings.

## Write-up
Looking in packet `#93`, we find the User-Agent(_I get the reference_)

    Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36

Attempting to pass `Mozilla 5.0`, `Safari 537.37` results as invalid flag but `Chrome 36.0.1985` results in the correct flag.

Therefore, the flag is `Chrome 36.0.1985`.