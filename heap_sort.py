#! /usr/bin/evn python
#coding:utf-8

from heapq import *

def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h,value)
    return [heappop(h) for i in range(len(h))]

if __name__=="__main__":
    print heapsort([1,3,5,9,2])
