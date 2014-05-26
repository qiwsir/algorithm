#! /usr/bin/env python
#coding:utf-8

def convert(one_string,space_character):    #one_string:输入的字符串；space_character:字符串的间隔符，以其做为分隔标志

    string_list = str(one_string).split(space_character)    #将字符串转化为list
    first = string_list[0].lower()
    others = string_list[1:] 

    others_capital = [word.capitalize() for word in others]      #str.capitalize():将字符串的首字母转化为大写

    others_capital[0:0] = [first]

    hump_string = ''.join(others_capital)     #将list组合成为字符串，中间无连接符。

    return hump_string

if __name__=='__main__':
    print "the string is:ab-cd-ef"
    print "convert to hump:"
    print convert("ab-cd-ef","-")
