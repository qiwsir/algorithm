#问题

二分查找

list.index()无法应对大规模数据的查询，需要用其它方法解决，这里谈的就是二分查找

#思路说明

在查找方面，python中有list.index()的方法。例如：

    >>> a=[2,4,1,9,3]           #list可以是无序，也可以是有序
    >>> a.index(4)              #找到后返回该值在list中的位置
    1
    >>> a.index(5)              #如果没有该值，则报错
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: 5 is not in list

这是python中基本的查找方法，虽然简单，但是，如果由于其时间复杂度为O(n)，对于大规模的查询恐怕是不足以胜任的。二分查找就是一种替代方法。

二分查找的对象是：有序数组。这点特别需要注意。要把数组排好序先。怎么排序，可以参看我这里多篇排序问题的文章。

基本步骤：

1. 从数组的中间元素开始，如果中间元素正好是要查找的元素，则搜素过程结束；
2. 如果某一特定元素大于或者小于中间元素，则在数组大于或小于中间元素的那一半中查找，而且跟开始一样从中间元素开始比较。
3. 如果在某一步骤数组为空，则代表找不到。

这种搜索算法每一次比较都使搜索范围缩小一半。时间复杂度：O(logn)

#解决(Python)

	def binarySearch(lst, value,low,high):          #low,high是lst的查找范围
	    if high < low:
	        return -1
	    mid = (low + high)/2
	    if lst[mid] > value:
	        return binarySearch(lst, value, low, mid-1)
	    elif lst[mid] < value:
	        return binarySearch(lst, value, mid+1, high)
	    else:
	        return mid
	
	#也可以不用递归方法，而采用循环，如下：
	 
	def bsearch(l, value):
	    lo, hi = 0, len(l)-1
	    while lo <= hi:
	        mid = (lo + hi) / 2
	        if l[mid] < value:
	            lo = mid + 1
	        elif value < l[mid]:
	            hi = mid - 1
	        else:
	            return mid
	    return -1
	 
	if __name__ == '__main__':
	    l = range(50)
	    print binarySearch(l,10,0,49)
	    print bsearch(l,10)

对于python，不能忽视其强大的标准库。经查阅，发现标准库中就有一个模块，名为：bisect。其文档中有这样一句话：

>>This module provides support for maintaining a list in sorted order without having to sort the list after each insertion. For long lists of items with expensive comparison operations, this can be an improvement over the more common approach. The module is called bisect because it uses a basic bisection algorithm to do its work. The source code may be most useful as a working example of the algorithm (the boundary conditions are already right!).

当我把这段话输入到百度翻译中，天才的百度翻译给我的结果是：

>>这个模块提供支持，维护list in order for without having to类法术the list After each插入。久lists of items以及昂贵的比较操作，这可以改善over the more common approach年。bisect because it is called the模块基本分割算法用to do its work。源代码可能是最有用的工作example of the算法（the边界条件are already right！）。

这就是百度的水平，只可惜在贵国不能用google。

看官就凭借自己的英语水平理解吧。这段话的关键点是在说明：

- 模块接受排序后的列表。
- 本模块同样适用于长列表项。因为它就是用二分查找方法实现的，有兴趣可以看其源码（源码是一个很好的二分查找算法的例子，特别是很好地解决了边界条件极端的问题.)
- 关于bisect模块的更多内容，可以参看[官方文档](https://docs.python.org/2/library/bisect.html)

下面演示这个模块的一个函数
	
	from bisect import *
	
	def bisectSearch(lst, x):          
	    i = bisect_left(lst, x)         #bisect_left(lst,x)，得到x在已经排序的lst中的位置
	    if i != len(lst) and lst[i] == x:
	        return i
	    raise ValueError
	
	if __name__=="__main__":
	    lst = sorted([2,5,3,8])
	    print bisectSearch(lst,5)
