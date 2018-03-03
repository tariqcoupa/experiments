#!/usr/bin/python
import heapq

nums = [1,3,6,2,7,9,23,45,88]
print (heapq.nlargest(2, nums))
print (heapq.nsmallest(1, nums))

