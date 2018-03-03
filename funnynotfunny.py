#!/bin/python

import sys

def funnyString(s):
    srev = s[::-1]
    for i in range(1,len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) == abs(ord(srev[i]) - ord(srev[i-1])):
            return "Funny"
        else:
            return "Not Funny"

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = funnyString(s)
    print(result)
