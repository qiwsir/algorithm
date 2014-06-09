#问题

将一个整数，分拆为若干整数的和。例如实现：
4=3+1
4=2+2
4=2+1+1
4=1+1+1+1

#解决(Python)

	#! /usr/bin/env python
	#encoding:utf-8
	
	"""
	"""
	
	def int_divided(m,r,out_list):
	    if(r==0):
	        return True 
	    m1=r
	    while m1>0:
	        if(m1<=m):
	            out.append(m1)
	            if(divide(m1,r-m1,out)):
	                print out
	            out.pop()
	        m1-=1
	    return False
	
	
	n=6
	output=[]
	int_divided(n-1,n,output)
