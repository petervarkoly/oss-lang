#!/usr/bin/python
import json
import sys
import collections


def analyze(h,deep):
    for item in h.items():
       if isinstance(item[1],dict):
           deep+=1
           print '"',item[0],'"{"'
           analyze(item[1],deep)
           deep-=1
       print deep*" ",item[0],":",item[1]

f_name=sys.argv[1]

j_hash = json.load(open(f_name,"r"))
d = collections.OrderedDict()
for key1 in sorted(j_hash.keys()):
    print key1
    b = collections.OrderedDict()
    for key2 in sorted(j_hash[key1].keys()):
        print key2,j_hash[key1][key2]
        b.setdefault(key2,j_hash[key1][key2])
    d.setdefault(key1,b)

print d
