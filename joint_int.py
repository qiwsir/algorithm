#! /user/bin/env python
#coding:utf-8

"""
把一个int型数组中的数字拼成一个串，这个串代表的数字最小;

对这个问题的理解：

１、有一个元素是int类型的list；

２、将上述list中的每个元素的数字分别取出来，然后将这些数字的顺序进行从新排列，并将其中的最小整数输入，就是题目中要求的最小数字。

如果按照上述理解，在解题中，最应当小心的是数字如果很大，比如list中的某个int元素是：222222222222227777777777776666666666699999999999888888888...很大的整数，就不得不转化为字符串操作了。

所以，在本问题中，基本思路是：

１、将list中的int元素转换为str；
２、将所有数字(str类型）装入到一个list2
３、对list2进行排序
４、将list2中的数字（str类型）组装成一个数值(str类型)
"""

def joint_int(lst):
    str_list = [str(i) for i in lst]
    str_lonely = [str_list[i][j] for i in range(len(str_list)) for j in range(len(str_list[i]))]
    
    sorted_str = sorted(str_lonely)
    return "".join(sorted_str)

print joint_int([1230975,4087644567856])


