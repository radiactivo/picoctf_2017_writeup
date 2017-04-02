# PicoCTF_2017: HashChain

**Category:** Cryptography
**Points:** 90
**Description:**

>We found a service hiding a flag! It seems to be using some kind of MD5 Hash Chain authentication to identify who is allowed to see the flag. Maybe there is a flaw you can exploit? [hcexample.py](hcexample.py) has some example code on how to calculate iterations of the MD5 hash chain. Connect to it at shell2017.picoctf.com:58801!

**Hint:**

>Connect from the shell with nc. Read up on how Hash Chains work and try to identify what could make this cryptosystem weak.

## Write-up
Another simple one, exploiting vulnerabilities of predictable seeds. In this case, believe it or not, the user ID is the seed! So, we create a [solver.py](solver.py) that will use the user id and generate hashes for us.

    $ nc shell2017.picoctf.com 58801

    *******************************************
    ***            FlagKeeper 1.1           ***
    *  now with HASHCHAIN AUTHENTICATION! XD  *
    *******************************************

    Would you like to register(r) or get flag(f)?

    r/f?

    f
    This flag only for user 6208
    Please authenticate as user 6208
    a9afc1eebbc4c86a23cc8d81c051b0cb
    Next token?

    $ ./solver.py 6208 a9afc1eebbc4c86a23cc8d81c051b0cb
    10fc2240d4916b2e77469cf1e310d22c
    21f044c80db74b5fe6c1faea4593512e
    785e2cffc39f5753eeb2dc33dedd546e
    5fe144923873f76361753cf7e9773816
    14fc0a59aca14517eb2ef5521e6d0d8f
    d1c2a8cd294372365f9b173a025c1356
    d8cff89e75d3cbbdb49c8c35b9fdc65b
    b441b8decd5049a69fb7c48921ff59bb
    4a99caa88953724ba0396a3098da8a21
    017e464d609a4f580a5e409a5185ed1f
    fa1390f653c274e8854654e264a703fb
    832eb443801ea8650935cd818ca2e72d
    763bcb5d8858172c6a83a19ee3bad41e
    6ccff5926c6ee56eeab799c59a14fc5b
    3ccdf2678dc619572864232848ebc61b
    8b9697ab88e52b678ecc6f02d3ff7d3f
    4d7ed0551984b59bbf1c0ebec93b57cb
    b2f7cd6698baf204e7f2ceecbdaf8d60
    bc50f9a7eed1c52f6221d8fa0b594fd9
    9e4b40d0d7f67b3f79ee5fd820b2efab
    74865bfe0fd00a6895e651a5b031faf3
    a1f6ef4844eaa64579a38deadb06b700
    046aff6dd89aec2d411056efc4641f42
    87ce9a8edd77ade35fd903ad5cc161be
    75a9de906c65374f87313cda61fa1566
    1006016b4424e74dde5c0e42ce86371a
    439828238fe9b93c5f35370c27ae237f
    2236ab32061954a6773f3d6d98da2db4
    c2705c59cc6b8ce46998908d05dc89fd
    25c4691e9d5f447e81b61309508793d8
    f48ed291cac07e5639053eace029b8c5
    487ce2d711a764022cec0687af37fb59
    d2e22f4ad1f3a862e7ee1cee6c326a70
    62338b9dc6a88321dfddf7a7c582ee54
    89e45113e4688b368765ebcc7693cab2
    bdfa144ea642b3cc51cce69f6d1393c4
    204c882eaff2d36a4afa3b4178c9ec1a
    8992c417a6972f2c34931cf36be96098
    5395457726827c22670cbec7205084e8
    9f457e1c4e215e004135ad36ab6f3a67
    d6505f6ef735778beb26caeb9dca12b4
    654fe8ee272ab72e7bb5ee6e05a87ded
    1ad124933659f5143c419f2e5f82c6bb
    003b352e33d5ad4e7950b5399931aad6
    9abbb42a69cb55e8e31424615f1de491
    256b1e8a197f8843244399e4a7d00324
    20510ee116cf9ade89e8baf9c513b4af
    9241b69fecb4acb2588d1097c269b231
    8c778ead2a496380e52366c8395b4fbb
    32e9e49597708d25b416a73a151ae032
    f6267eac8bb8c33881c168e3a9e2ecda
    2547d685fd5b874450ea49972a5e896a
    8214a9ae89884045032246ddb5bcd701
    334f9aac6adc3e20ac20ccd240e21938
    d850a69a279dd554eb05028c255c0835
    8ed0b3507e5b7b00908cadac03df3a13
    4b0d94c219dfd2f8f5b26265e3a4869f
    7d3bc53a55fd9f254d89b63816152760
    f611ae0d6e3e242c49ebc33a82a28cba
    a61025c4277dd1dd903b06ab810dc9cb
    72f7441a0b91a030ce80d4acd4791d69
    854f7c124bc5ea5015b030023092896b
    ee064316439b3bee22d758a3ea6fa3df
    57aca98fc6a975788bac5713bdead972
    703c170f27d71bd4b004af41bb59e9e2
    b619b9e5be45e1302680f9b6f29bb702
    1ce4a7c6db3e137ba49599d57d60b244
    f33d66ad31eb668393837531dbdfe2b3
    463451762aa1c8725b39fbd652cc3a34
    74ef9bad440ea442d9153f0989998e61
    f0133bb28202f10847166ad8bbd00e68
    b00bcdd13c31df88648cc63dec51c74e
    43314ede7bc7f8cc6b21f47ed0b2aa2a
    4216d8ed5569f552e98df7ab78115d79
    5f07053cb1bc8190d02ce3240a626497
    a287e9f97b73dcee12c0d1984037ca0d
    debab078f0535660963fb32f601a67e3
    2f2b7adb6d838021eaa7a6d17fe2399f
    a251e04b98e16eed4a6daa120bfe22a3
    32fb70d6635fe446e8455a815fd9f11d
    ffbbfb30b80d894335ea6fea2611ff1e
    c3f14e02b8dadfc237e9ae3765a7257c
    427bd88899374a0279ec2fb5ca30cdab
    1f75d730830d25f9ae070a7e3631dff4
    d7b4b7009c97daafe6def7c1a9720a03
    6fdf380e749e0d47cf01ea0f19a6f77f
    18b423b6e259fdfb758ac258d3cd39f7
    d4f35971293652b92671586cd91be608
    c71f5a31122ced70d1307090683aa2f2
    fb8deb304d10a20b661fa9a7a8e90888
    d92f1345626304a6186eee13d9950413
    e22c4da6e22aca3dddf5b7a674d3a3fd
    cd634164f94963ac6574d1c4384a8dc3
    12eb5d2067008f68ab22be3f1cf0e1aa
    2438d9a778a83a027f6871c94a968bcc
    815418113755cc74b66dd64edbee9bb0 <- Enter this one
    a9afc1eebbc4c86a23cc8d81c051b0cb

    815418113755cc74b66dd64edbee9bb0
    Hello user 6208! Here's the flag: 9494f4171092452602fa545ab927e99e

Therefore, the flag is `9494f4171092452602fa545ab927e99e`.

