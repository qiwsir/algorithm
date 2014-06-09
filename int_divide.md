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
	    tm=r
	    while tm>0:
	        if(tm<=m):
	            out.append(tm)
	            if(divide(tm,r-tm,out_list)):
	                print out
	            out.pop()
	        tm = tm-1
	    return False
	
	
	n=6
	output=[]
	int_divided(n-1,n,output)
