#!/usr/bin/env python
#coding:utf-8

"""
问题
要求定义一个int型数组a,包含100个元素,保存100个随机的4位数。再定义一个
int型数组b，包含10个元素。统计a数组中的元素对10求余等于0的个数，保存
到b[0]中；对10求余等于1的个数，保存到b[1]中，……依此类推。
"""

import random
if __name__=="__main__":
    a = [random.randint(1000,9999) for i in range(101)]
    a_remainder = [i%10 for i in a]
    b = [a_remainder.count(i) for i in range(10)]
    print a
    print a_remainder
    print b


