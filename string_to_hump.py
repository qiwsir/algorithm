#! /usr/bin/env python
#coding:utf-8

def convert(one_string,space_character):    #one_string:输入的字符串；space_character:字符串的间隔符，以其做为分隔标志

    string_list = str(one_string).split(space_character)    #将字符串转化为list

    string_hump_list = [word.capitalize() for word in string_list]      #str.capitalize():将字符串的首字母转化为大写

    hump_string = ''.join(string_hump_list)     #将list组合成为字符串，中间无连接符。驼峰样式。

    return hump_string

if __name__=='__main__':
    print convert("ab-cd-ef","-")
