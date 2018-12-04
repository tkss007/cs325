#!/usr/bin/env python
import sys
import math
import time
import datetime
import random

def mergesort(lst):
    if (len(lst) <= 1): return lst
    left = mergesort(lst[:len(lst) / 2])
    right = mergesort(lst[len(lst) / 2:len(lst)])
    result = []
    while len(left) > 0 and len(right) > 0:
        if (left[0] > right[0]):
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))

    if (len(left) > 0):
        result.extend(mergesort(left))
    else:
        result.extend(mergesort(right))
    return result


# insert_sort
def insertsort(l):
    for i in range(len(l)):
        min_index = i
        for j in range(i + 1, len(l)):
            if l[min_index] > l[j]:
                min_index = j
        tmp = l[i]
        l[i] = l[min_index]
        l[min_index] = tmp
    return l


def main():
    n = 20000
    print n
    lst = [random.randint(0, 10000) for _ in range(n)]


    starttime = datetime.datetime.now()
    print mergesort(lst)
    endtime = datetime.datetime.now()
    print (endtime - starttime)


    starttime = datetime.datetime.now()
    print insertsort(lst)
    endtime = datetime.datetime.now()
    print (endtime - starttime)

if __name__ == "__main__":
    main()
