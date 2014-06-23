#! /usr/bin/env python
#coding:utf-8
"""
#solve 1

def merge_sort(seq):
    if len(seq) ==1:
        return seq
    else:
        middle = len(seq)/2
        left = merge_sort(seq[:middle])
        right = merge_sort(seq[middle:])

        i = 0   #left 计数
        j = 0   #right 计数
        k = 0   #总计数

        while i < len(left) and j < len(right):
            if left[i] < right [j]:
                seq[k] = left[i]
                i +=1
                k +=1
            else:
                seq[k] = right[j]
                j +=1
                k +=1
        
        remain = left if i<j else right
        r = i if remain ==left else j

        while r<len(remain):
            seq[k] = remain[r]
            r +=1
            k +=1

        return seq

#solve 2

def merge_sort(lst):   #此方法来自维基百科：http://zh.wikipedia.org/zh/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F
    if len(lst) <= 1:
        return lst
                 
    def merge(left, right):
        merged = []
        
        while left and right:
            merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        
        while left:
            merged.append(left.pop(0))
        
        while right:
            merged.append(right.pop(0))
        
        return merged
        
    middle = int(len(lst) / 2) 
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merge(left, right)
"""
#solve 3
#以下方法来自：http://rosettacode.org/wiki/Sorting_algorithms/Merge_sort#Python
#稍作修改

from heapq import merge
 
def merge_sort(seq):
    if len(seq) <= 1:
        return seq
    else:
        middle = len(seq)/2
        left = merge_sort(seq[:middle])
        right = merge_sort(seq[middle:])
        return list(merge(left,right))

if __name__=="__main__":
    seq = [1,3,6,2,4]
    print merge_sort(seq)
