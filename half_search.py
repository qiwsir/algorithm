#! /usr/bin/env python
#coding:utf-8

#折半查找某个元素在list中的位置

def half_search(lst,value,left,right):
    length = len(lst)
    while left<right:
        middle = (right-left)/2
        if lst[middle]>value:
            right = middle-1
        elif lst[middle]<value:
            left = middle+1
        else:
            return middle 

#如果该元素在list中不止一个，可以用下面方法找出所有位置分布

def find_value_location(lst,value):
    result = [i for i in range(len(lst)) if value==lst[i]]    
    return result


if __name__=="__main__":
    lst=sorted([2,4,4,5,9])
    length = len(lst)
    left = 0
    right = length-1
    value =4 
    result = half_search(lst,value,left,right)
    if result:
        print result
    else:
        print "There is no the value that you want to search."
    lst2=[2,4,5,4,2]
    result2 = find_value_location(lst2,4)
    print result2
