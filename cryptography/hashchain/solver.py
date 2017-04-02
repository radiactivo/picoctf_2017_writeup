#! /usr/bin/python
##
import md5
import sys

userid = sys.argv[1]
prev_hash = sys.argv[2]

seed = md5.new(str(userid)).hexdigest()
hashc = seed

while prev_hash not in hashc:
    hashc = md5.new(hashc).hexdigest()
    print(hashc)