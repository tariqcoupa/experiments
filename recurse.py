#!/usr/bin/python

import sys

def tripleRecursion(n, m, k):
    
    arr=[[0 for i in range(n)] for j in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            arr[i][j] = raw_input()
            if i == 0 and j == 0:
                arr[i][j] = m
            elif i == j:
                arr[i][j] = arr[i-1][j-1] + k
            elif i < j:
                arr[i][j] = arr[i][j-1] - 1
            elif i > j:
                arr[i][j] = arr[i-1][j] - 1
    print arr    

tripleRecursion(4, 3, 1)
