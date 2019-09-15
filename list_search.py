#!/usr/bin/env python3

# from bisect import bisect_left
def bisect_array_left(a, x, d, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid][d] < x[d]: lo = mid+1
        else: hi = mid
    return lo

# from bisect import bisect_right
def bisect_array_right(a, x, d, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x[d] < a[mid][d]: hi = mid
        else: lo = mid+1
    return lo

a = [
    [1, 1],
    [2, 1],
    [2, 2],
    [2, 1000],
    [500, 1],
    [500, 2],
    [500, 500],
    [1000, 1000],
]
x = [2, 2]
idxl = bisect_array_left(a, x, 0)
idxr = bisect_array_right(a, x, 0, lo=idxl) - 1
idx = bisect_array_left(a, x, 1, lo=idxl, hi=idxr)
print(idx)
