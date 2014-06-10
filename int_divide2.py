#! /usr/bin/env python
#encoding:utf-8

"""
给你一个小于50的数字 a ，请写出一个算法得到所有可能的数字集合，每个数字集合满足以下条件：

1. 集合中所有数字的和等于a;

2. 集合中的所有数字均大于1；

3. 集合中可以出现重复数字；

例如：

2 -> {2},
3->{3},
4->{[4], [2, 2]},
5->{[5], [3, 2]},
6->{[6], [4, 2], [3, 3], [2, 2, 2]}
7->{[7], [5, 2], [4, 3], [3, 2, 2]}
8->{[8], [6, 2], [5, 3], [4, 4], [4, 2, 2], [3, 3, 2], [2, 2, 2, 2]}
"""

def divide(m,r,out):
    temp = []
    out
    if(r==0):
        return True 
    m1=r
    while m1>1:
        if(m1<=m):
            out.append(m1)
            if(divide(m1,r-m1,out)):
                print temp

            out.pop()
        m1-=1
    return False


n=6
out=[]
divide(n-1,n,out)


