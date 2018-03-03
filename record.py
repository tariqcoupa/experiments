#!/usr/bin/python
l = 0
w = 0
s = [3,4,21,36,10,28,35,5,24,42]
for i in range(1, len(s)):
     if s[i-1] < s[i]:
            l = l+1
     else:
            w = w+1
print w-1, l-1 
