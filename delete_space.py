#! /usr/bin/env python
#coding:utf-8

#删除一个字符串中连续超过一次的空格。
def del_space(string):
    split_string = string.split(" ")    #以空格为分割，生成list，list中如果含有空格，则该空格是连续空格中的后一个
    string_list = [i for i in string if i!=""]
    result_string = " ".join(string_list)
    return result_string

if __name__=="__main__":
    one_str = "Hello,  I am  Qiwsir."
    string = del_space(one_str)
    print one_str
    print string
