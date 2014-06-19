#!/usr/bin/env python
#coding:utf-8

"""
统计一个一维数组中的各个元素的个数，然后删除多出来的重复元素，并输出结果。
例如：[1,2,2,2,3,3,3,3,3]-->[1,2,3]
"""

def count_element(one_list):
    element_number = {}
    for e in one_list:
        number = one_list.count(e)      #数出某个元素的个数
        element_number[e] = number     #生成类似：{1:1,2:3,3:5}的结果，key-element,value-元素的个数
    return element_number

#函数count_element(one_list)的功能，可以用collections模块中的Counter完成

from collections import Counter

def count_element2(one_list):
    return Counter(one_list)

def no_repeat_element(element_number):      #element_number是count_element(one_list)的返回值
    no_repeat_list = [key for key in element_number]
    return no_repeat_list

"""
另外一种删除重复元素方法

list_a = [1,1,2,2,2,3,3,3,3,3,]
list_b = list(set(list_a))

"""


if __name__=="__main__":

    ls = ["a","a","b","b",'b','c','c']
    el_num=count_element(ls)
    print el_num
    no_repeat = no_repeat_element(el_num)
    print no_repeat
    print "another way is:"
    no_repeat2 = list(set(ls))
    print no_repeat2
    print "-------"
    el_num2=count_element2(ls)
    print el_num2
    no_repeat = no_repeat_element(el_num)
    print no_repeat

"""
the result is :

{'a': 2, 'c': 2, 'b': 3}
['a', 'c', 'b']
another way is:
['a', 'c', 'b']
-------
Counter({'b': 3, 'a': 2, 'c': 2})
['a', 'c', 'b']

"""
