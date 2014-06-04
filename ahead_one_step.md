#问题

定义一个int型的一维数组，包含10个元素，分别赋值为1~10， 然后将数组中的元素都向前移一个位置，

即，a[0]=a[1],a[1]=a[2],…最后一个元素的值是原来第一个元素的值，然后输出这个数组。

#解决(Python)

	#!/usr/bin/env python
	#coding:utf-8
	
	
	def ahead_one():
	    a = [i for i in range(10)]
	    b = a.pop(0)
	    a.append(b)
	    return a
	
	if __name__ =="__main__":
	    print ahead_one()

#解决(racket 5.2.1)

```racket
#lang racket

; 定义函数 ahead-one
; 输入为一个整数列表 int-list，假设其长度为 N
; 输出为长度相同的整数列表，其第 N 位的元素为 int-list 的第 1 位的元素，
; 其 1~N-1 位的元素为 int-list 的第 2~N 位的元素
(define (ahead-one int-list)
  (append (rest int-list) (list (first int-list))))

; 函数调用，正常运行时应输出 '(2 3 4 5 6 7 8 9 10 1)
(ahead-one (list 1 2 3 4 5 6 7 8 9 10))
```
