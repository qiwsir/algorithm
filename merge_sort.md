#问题

归并排序

#思路说明

归并操作过程：

1. 申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列
2. 设定两个指针，最初位置分别为两个已经排序序列的起始位置
3. 比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置
4. 重复步骤3直到某一指针达到序列尾
5. 将另一序列剩下的所有元素直接复制到合并序列尾

上述说法是理论表述，下面用一个实际例子说明：

例如一个无序数组[6,2,3,1,7]

首先将这个数组通过递归方式进行分解，直到：[6],[2],[3],[1],[7]

然后开始合并排序，也是用递归的方式进行：

1. 两个两个合并排序，得到：[2,6],[1,3],[7]
2. 上一步中，其实也是按照本步骤的方式合并的，只不过由于每个list中一个数，不能完全显示过程。下面则可以完全显示过程。
    
    初始：
    a = [2,6]
    b = [1,3]
    c = []
    第1步，顺序从a,b中取出一个数字：2,1
    比较大小后放入c中，并将该数字从原list中删除，结果是：
    a = [2,6]
    b = [3]
    c = [1]
    第2步，继续从a,b中按照顺序取出数字，也就是重复上面步骤，这次是：2,3
    比较大小后放入c中，并将该数字从原list中删除，结果是：
    a = [6]
    b = [3]
    c = [1,2]
    第3步,再重复前边的步骤,结果是：
    a = [6]
    b = []
    c = [1,2,3]
    最后一步，将6追加到c中，结果形成了：
    a = []
    b = []
    c = [1,2,3,6]

3. 通过反复应用上面的流程，实现[1,2,3,6]与[7]的合并
4. 最终得到排序结果[1,2,3,6,7]

本文列举了三种python的实现方法。

#解决(Python)

	#! /usr/bin/env python
	#coding:utf-8
	
	#方法1：将前面讲述的过程翻译过来了，略先拙笨
	
	def merge_sort(seq):
	    if len(seq) ==1:
	        return seq
	    else:
	        middle = len(seq)/2
	        left = merge_sort(seq[:middle])
	        right = merge_sort(seq[middle:])
	
	        i = 0   #left 计数
	        j = 0   #right 计数
	        k = 0   #总计数
	
	        while i < len(left) and j < len(right):
	            if left[i] < right [j]:
	                seq[k] = left[i]
	                i +=1
	                k +=1
	            else:
	                seq[k] = right[j]
	                j +=1
	                k +=1
	        
	        remain = left if i<j else right
	        r = i if remain ==left else j
	
	        while r<len(remain):
	            seq[k] = remain[r]
	            r +=1
	            k +=1
	
	        return seq
	
	#方法2：在按照顺序取数值方面，应用了list.pop()方法，代码更紧凑简洁
	#此方法来[自维基百科：归并操作](http://zh.wikipedia.org/zh/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F)
	
	def merge_sort(lst):   #此方法来自维基百科：http://zh.wikipedia.org/zh/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F
	    if len(lst) <= 1:
	        return lst
	                 
	    def merge(left, right):
	        merged = []
	        
	        while left and right:
	            merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
	        
	        while left:
	            merged.append(left.pop(0))
	        
	        while right:
	            merged.append(right.pop(0))
	        
	        return merged
	        
	    middle = int(len(lst) / 2) 
	    left = merge_sort(lst[:middle])
	    right = merge_sort(lst[middle:])
	    return merge(left, right)
	
	#方法3：原来在python的模块heapq中就提供了归并排序的方法，只要将分解后的结果导入该方法即可
	#强大。
	#以下方法来自[resettacode](http://rosettacode.org/wiki/Sorting_algorithms/Merge_sort#Python),并稍作修改
	
	from heapq import merge
	 
	def merge_sort(seq):
	    if len(seq) <= 1:
	        return m
	    else:              
	        middle = len(seq)/2
	        left = merge_sort(seq[:middle])
	        right = merge_sort(seq[middle:])
	        return list(merge(left, right))         #heapq.merge()
	
	if __name__=="__main__":
	    seq = [1,3,6,2,4]
	    print merge_sort(seq)
