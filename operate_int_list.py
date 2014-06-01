#! /usr/bin/env python
#coding:utf-8

"""
问题描述：

定义一个int型的一维数组，包含10个元素，赋一些随机整数
然后求出所有元素的最大值，最小值，平均值，和值，并输出出来。
"""

from __future__ import division     #实现精确的除法，例如4/3=1.333333
import random

def add(x,y):
    return x+y

def operate_int_list():
    int_list = [random.randint(1,100) for i in range(10)]     #在1,100范围内，随机选择10个整数组成一个list
    max_num = max(int_list)
    min_num = min(int_list)
    sum_num = reduce(add,int_list)      #这里使用了reduce函数，也可以使用for循环，如下所示
    """
    sum_num = 0
    for i in int_list:
        sum_num = sum_num+i
    """
    ave_num = sum_num/len(int_list)

    return (int_list,max_num,min_num,sum_num,ave_num)

if __name__=="__main__":
    int_list,max_num,min_num,sum_num,ave_num = operate_int_list()
    print "the int list is:",int_list
    print "max number is:",max_num
    print "min number is:",min_num
    print "the sum of all int in the list:",sum_num
    print "the average of the sum:",ave_num
