#!/usr/bin/env python3

# https://www.geeksforgeeks.org/binary-search-bisect-in-python/

# Python code to demonstrate working
# of binary search in library
from bisect import bisect_left

def BinarySearch(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1

a  = [1, 2, 4, 4, 8]
x = 4
idx = BinarySearch(a, x)
if idx == -1:
    print(x, "is absent")
else:
    print("First occurrence of", x, "is present at", idx)
