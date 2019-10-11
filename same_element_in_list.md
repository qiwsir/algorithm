# 问题

统计一个一维数组中的各个元素的个数，然后删除多出来的重复元素，并输出结果。

例如：[1,2,2,2,3,3,3,3,3]-->[1,2,3]

## 解决思路

将重复元素的列表中的重复元素进行统计，并将统计结果放在dictionary中，key为元素，value为该元素的个数

**更新此步方法：** 上述步骤的功能，能够通过另外一个方法实现，即collections.Counter()

然后通过for获取key，得到一个新的列表，就是没有重复元素的列表



## 解决（Python）

```python
#!/usr/bin/env python
#coding:utf-8


def count_element(one_list):
	element_number = {}
	for e in one_list:
		number = one_list.count(e)      #数出某个元素的个数
		element_number[e] = number     #生成类似：{1:1,2:3,3:5}的结果，key-element,value-元素的个数
	return element_number

#应用collections.Counter()实现count_element(one_list)函数功能，为了便于调试和说明，在另外一个函数里面使用

from collections import Counter

def count_element2(one_list):
	return Counter(one_list)


def no_repeat_element(element_number):      #element_number是count_element(one_list)的返回值
	no_repeat_list = [key for key in element_number]
	return no_repeat_list

if __name__=="__main__":
	ls = ["a","a","b","b",'b','c','c']
	el_num=count_element(ls)
	print el_num
	no_repeat = no_repeat_element(el_num)
	print no_repeat

```

## 解决（python）

无重复元素个数统计，只有新数组输出

```python
list_a = [1,1,2,2,2,3,3,3,3,3,]
list_b = list(set(list_a))
```

## qiwsir#gmail.com (# to @)
