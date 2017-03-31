# PicoCTF_2017: Leaf of the Tree

**Category:** Miscellanous
**Points:** 20
**Description:**

>We found this annoyingly named directory tree starting at /problems/a47d10dd80018fc6e7e1c5094c1ca323. It would be pretty lame to type out all of those directory names but maybe there is something in there worth finding? And maybe we dont need to type out all those names...? Follow the trunk, using cat and ls!

**Hint:**

>Tab completion is a wonderful, wonderful thing

## Write-up
I am a big fan of not wasting time by tab completion, thus we are going to cheat and use `find`.

    $ find /problems/a47d10dd80018fc6e7e1c5094c1ca323/ -type f
    /problems/a47d10dd80018fc6e7e1c5094c1ca323/trunk/trunkbe9c/trunk8ec3/branch4118/leaf33d8                                
    /problems/a47d10dd80018fc6e7e1c5094c1ca323/trunk/trunkbe9c/trunk8ec3/trunk708d/trunk664c/branchcd3c/leaf29a9            
    /problems/a47d10dd80018fc6e7e1c5094c1ca323/trunk/trunkbe9c/trunk8ec3/trunk708d/trunk664c/branchcd3c/leaf280d            
    /problems/a47d10dd80018fc6e7e1c5094c1ca323/trunk/trunkbe9c/trunk8ec3/trunk708d/trunk664c/trunk430b/branch8979/leaf184f  
    /problems/a47d10dd80018fc6e7e1c5094c1ca323/trunk/trunkbe9c/trunk8ec3/trunk708d/trunk664c/trunk430b/branch8979/leaf52a9  
    /problems/a47d10dd80018fc6e7e1c5094c1ca323/trunk/trunkbe9c/trunk8ec3/trunk708d/trunk664c/trunk430b/trunk122c/trunkc000/flag                                                         
    /problems/a47d10dd80018fc6e7e1c5094c1ca323/trunk/trunkbe9c/trunk8ec3/trunk708d/trunk664c/trunk430b/trunk122c/trunkc000/branch8211/leaffbf3                                          
    /problems/a47d10dd80018fc6e7e1c5094c1ca323/trunk/trunkbe9c/trunk8ec3/trunk708d/trunk664c/trunk430b/trunk122c/branch67f2/leaf5dd4                                                    
    /problems/a47d10dd80018fc6e7e1c5094c1ca323/trunk/trunkbe9c/trunk8ec3/trunk708d/trunk664c/trunk430b/trunk122c/branch67f2/leaf7813                                                    
    /problems/a47d10dd80018fc6e7e1c5094c1ca323/trunk/trunkbe9c/trunk8ec3/trunk708d/trunk664c/trunk430b/trunk122c/branch3c2e/leaff81e

Hmm, that flag file looks interesting.

    $ cat /problems/a47d10dd80018fc6e7e1c5094c1ca323/trunk/trunkbe9c/trunk8ec3/trunk708d/trunk664c/trunk430b/trunk122c/trunkc000/flag
    5e3d48f32a6d6e17a8102d3cbae36283

Therefore, the flag is `5e3d48f32a6d6e17a8102d3cbae36283`.  