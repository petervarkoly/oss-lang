#!/usr/bin/python
import json
import sys


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

deep=1
analyze(j_hash,deep)
