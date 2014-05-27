#! /usr/bin/env python
#coding:utf-8

#问题：

#查找字符串中出现最多的字符和个数？

#如 sdsdsddssssssdd -> 字符最多的是s，出现9次

import collections

def most_character_number(one_string):
    static_result = collections.Counter(one_string)             #统计字母及其数量，返回类似Counter({'a': 3, 'b': 3, 'c': 1})形式结果
    result = dict(static_result)                                #转化为dict类型
    most_number = max([value for value in result.values()])     #通过循环，找出dict的值中最大数
    most_character = [key for key,value in result.items() if value==most_number]    #找出最大数对应的key
    return (most_number,most_character)

if __name__ == "__main__":
    (most_num,most_char) = most_character_number("yyyyyyddddddkuuuiii")
    print ("The most character is:%s"%most_num)
    print ("The number is:")
    for char in most_char:
        print char
