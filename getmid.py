#!/usr/bin/python
def get_middle(s):
    mid = len(s)/2
    if len(s)%2 == 1:
        print s[mid]
    elif len(s)%2 == 0:
        print "%s%s" %(s[mid-1],s[mid])

get_middle("of")

