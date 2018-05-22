# 问题

快速排序，这是一个经典的算法，本文给出几种python的写法，供参考。

特别是python能用一句话实现快速排序。

# 思路说明

快速排序是C.R.A.Hoare于1962年提出的一种划分交换排序。它采用了一种分治的策略，通常称其为分治法(Divide-and-ConquerMethod)。

（1） 分治法的基本思想

分治法的基本思想是：将原问题分解为若干个规模更小但结构与原问题相似的子问题。递归地解这些子问题，然后将这些子问题的解组合为原问题的解。

（2）快速排序的基本思想

设当前待排序的无序区为R[low..high]，利用分治法可将快速排序的基本思想描述为：

### 分解：

在R[low..high]中任选一个记录作为基准(Pivot)，以此基准将当前无序区划分为左、右两个较小的子区间R[low..pivotpos-1)和R[pivotpos+1..high]，并使左边子区间中所有记录的关键字均小于等于基准记录(不妨记为pivot)的关键字pivot.key，右边的子区间中所有记录的关键字均大于等于pivot.key，而基准记录pivot则位于正确的位置(pivotpos)上，它无须参加后续的排序。

注意：

划分的关键是要求出基准记录所在的位置pivotpos。划分的结果可以简单地表示为(注意pivot=R[pivotpos])：

R[low..pivotpos-1].keys≤R[pivotpos].key≤R[pivotpos+1..high].keys

其中low≤pivotpos≤high。

### 求解：

通过递归调用快速排序对左、右子区间R[low..pivotpos-1]和R[pivotpos+1..high]快速排序。

### 组合：

因为当"求解"步骤中的两个递归调用结束时，其左、右两个子区间已有序。对快速排序而言，"组合"步骤无须做什么，可看作是空操作。

### 解决(Python)
	
```python
	#!/usr/bin/env python
	#coding:utf-8
	
	#方法1
	
	def quickSort(arr):
	    less = []
	    pivotList = []
	    more = []
	    if len(arr) <= 1:
	        return arr
	    else:
	        pivot = arr[0]      #将第一个值做为基准
	        for i in arr:
	            if i < pivot:
	                less.append(i)
	            elif i > pivot:
	                more.append(i)
	            else:
	                pivotList.append(i)
	
	        less = quickSort(less)      #得到第一轮分组之后，继续将分组进行下去。
	        more = quickSort(more)
	
	        return less + pivotList + more
	
	# 方法2
	# 分为<, >, = 三种情况，如果分为两种情况的话函数调用次数会增加许多，以后几个好像都有相似的问题
	# 如果测试1000个100以内的整数，如果分为<, >=两种情况共调用函数1801次，分为<, >, = 三种情况，共调用函数201次
	def qsort(L):
	    return (qsort([y for y in L[1:] if y <  L[0]]) + L[:1] + [y for y in L[1:] if y == L[0] + qsort([y for y in L[1:] if y > L[0]])) if len(L) > 1 else L
	
	#方法3
	#基本思想同上，只是写法上又有所变化
	
	def qsort(list):
	    if not list:
	        return []
	    else:
	        pivot = list[0]
	        less = [x for x in list     if x <  pivot]
	        more = [x for x in list[1:] if x >= pivot]
	        return qsort(less) + [pivot] + qsort(more)
	
	#方法4
	
	from random import *
	
	def qSort(a):
	    if len(a) <= 1:
	        return a
	    else:
	        q = choice(a)       #基准的选择不同于前，是从数组中任意选择一个值做为基准
	        return qSort([elem for elem in a if elem < q]) + [q] * a.count(q) + qSort([elem for elem in a if elem > q])
	
	
	#方法5
	#这个最狠了，一句话搞定快速排序，瞠目结舌吧。
	
	qs = lambda xs : ( (len(xs) <= 1 and [xs]) or [ qs( [x for x in xs[1:] if x < xs[0]] ) + [xs[0]] + qs( [x for x in xs[1:] if x >= xs[0]] ) ] )[0]
	
	
	if __name__=="__main__":
	    a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
	    print quickSort(a)
	    print qSort(a)
	
	    print qs(a)
```
