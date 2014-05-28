#! /usr/bin/env python
#coding:utf-8

str1 = "jjjjjjddddddllooppxx"
    
def most_character_number(one_string):
    """利用字典key来统计次数"""
    str_dict = {}
    for item in one_string:
        if item in str_dict:
            str_dict[item] +=1
        else:
            str_dict[item] =1
        
    str_dict = {str_dict[key]:key for key in str_dict}
    return (max(str_dict),str_dict[max(str_dict)])

print (most_character_number(str1))
