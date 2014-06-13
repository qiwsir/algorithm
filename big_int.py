#!/usr/bin/env python
#coding:utf-8

"""
对于大整数计算，一般都要用某种方法转化，否则会溢出。但是python无此担忧了。

Python支持“无限精度”的整数，一般情况下不用考虑整数溢出的问题，而且Python Int 整数类型与任意精度的Long整数类可以无缝转换，超过Int 范围的情况都将转换成Long类型。

注意：前面的“无限精度”是有引号的。事实上也是有限制的，对于32位的机器，其上限是：2^32-1。真的足够大了。

为什么Python能够做到呢？请有兴趣刨根问底的去看Python的有关源码。本文不赘述。

在其它语言中，通常用“分治法”解决大整数相乘问题。

但是，这里提供一个非常有意思的计算两个整数相乘的方法，算是做为大整数相乘的演示。

两个整数相乘：阿拉伯乘法.详细描述见：http://ualr.edu/lasmoller/medievalmult.html

"""

def arabic_multiplication(num1,num2):
    num_lst1 = [int(i) for i in str(num1)]  #将int类型的123，转化为list类型的[1,2,3]，每个元素都是int类型
    num_lst2 = [int(i) for i in str(num2)]

    #两个list中整数两两相乘
    int_martix = [[i*j for i in num_lst1] for j in num_lst2]
    
    #将上述元素为数字的list转化为元素类型是str，主要是将9-->'09'
    str_martix = [map(convert_to_str,int_martix[i]) for i in range(len(int_martix))]
    
    #将上述各个list中的两位数字分开：['01','29','03']-->[0,2,0],[1,9,3]
    martix = [[int(str_martix[i][j][z]) for j in range(len(str_martix[i]))] for i in range(len(str_martix)) for z in range(2)]
    
    #计算阿拉伯乘法表的左侧开始各项和
    sum_left = summ_left(martix)

    #计算阿拉伯乘法表的底部开始各项和
    sum_end = summ_end(martix)

    #将上述两个结果合并后翻转
    sum_left.extend(sum_end)
    sum_left.reverse()

    #取得各个和的个位的数字（如果进位则加上）
    result = take_digit(sum_left)
    
    #翻转结果并合并为一个结果字符串数值
    result.reverse()
    int_result = "".join(result)
    print "%d*%d="%(num1,num2)
    print int_result


#将int类型转化为str类型，9-->'09'

def convert_to_str(num):
    if num<10:
        return "0"+str(num)
    else:
        return str(num)


#计算阿拉伯乘法表格左侧开始的各项之和

def summ_left(lst):
    summ = []
    x = [i for i in range(len(lst))]
    y = [j for j in range(len(lst[0]))]
    sx = [i for i in x if i%2==0]
    for i in sx:
        s=0
        j=0
        while i>=0 and j<=y[-1]:
            s = s+ lst[i][j]
            if i%2==1:
                j = j+1
            else:
                j = j
            i = i-1
        summ.append(s)
    return summ



#计算阿拉伯乘法表格底部开始的各项之和

def summ_end(lst):
    summ=[]
    y = [j for j in range(len(lst[0]))]
    ex = len(lst)-1
    for m in range(len(y)):
        s = 0
        i=ex
        j=m
        while i>=0 and j<=y[-1]:
            s= s+lst[i][j]
            if i%2==1:
                j = j+1
            else:
                j=j
            i = i-1
        summ.append(s)
    
    return summ

#得到各个元素的个位数，如果是大于10则向下一个进位

def take_digit(lst):
    tmp = 0
    digit_list = []
    for m in range(len(lst)):
        lstm = 0
        lstm = lst[m]+tmp
        if lstm<10:
            tmp = 0
            digit_list.append(str(lstm))
        else:
            tmp = lstm/10
            mm = lstm-tmp*10
            digit_list.append(str(mm))
    return digit_list


if __name__=="__main__":
    arabic_multiplication(469,37)
