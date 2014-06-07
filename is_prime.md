#问题

判断一个数是否为素数

#思路说明

这个问题有多种解法，以下的解法来自网络整理。供参考使用。

#解决（Python）

	#! /usr/bin/env python
	#coding:utf-8
	
	"""
	"""
	
	#方法一
	
	import math  
	         
	def isPrime1(n):  
	    if n <= 1:  
	        return False 
	    for i in range(2, int(math.sqrt(n)) + 1):  
	        if n % i == 0:  
	            return False
	        
	    return True
	
	#方法二
	
	def isPrime2(n):
	    if n <= 1:
	        return False
	                  
	    i = 2
	    while i*i <= n:
	        if n % i == 0:
	            return False
	        i += 1
	    return True
	
	#方法三
	
	from itertools import count
	
	def isPrime3(n):
	    if n <= 1:
	        return False
	    for i in count(2):
	        if i * i > n:
	            return True
	        if n % i == 0:
	            return Fals
	
	#方法四
	
	def isPrime4(n):
	    if n <= 1:
	        return False
	    if n == 2:
	        return True
	    if n % 2 == 0:
	        return False
	    i = 3
	    while i * i <= n:
	        if n % i == 0:
	            return False
	        i += 2
	    return True
	
	
	if __name__=="__main__":
	    a=isPrime4(5)
	    print a
