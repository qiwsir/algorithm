#问题

查找某个值在list中的位置

#解决思路

可以用折半查询的方法解决此问题。

#解决（Python）

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

	if __name__=="__main__":
	    lst=sorted([2,4,5,9])　　　　#折半算法中list要进行排序
	    length = len(lst)
	    left = 0
	    right = length-1
	    value =4 
	    result = half_search(lst,value,left,right)
	    if result:
	        print result
	    else:
	        print "There is no the value that you want to search."
    
#再思考

对于上面的折半方法，在python中，可以通过一个函数实现

    lst = sorted([2,4,5,9])　　　　#这里进行排序，主要是为了得到与上面方法一样的结果。事实上，list.index()可以针对任何list操作，不一定非要排序
    result = lst.index(4)

此外，如果遇到list中有多个相同的元素，应该如何将这些元素的位置都查询出来呢？下面的方法是用python实现。

    def find_value_location(lst,value):
        result = [i for i in range(len(lst)) if value==lst[i]]    
        return result

##qiwsir#gmail.com
