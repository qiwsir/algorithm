#coding:utf-8

def max_array(lst):
    """面试题：最大连续子数组，求一个有正，有负数的数组(有正和负数，没有全是负数的情况)，
    连续子数组之最大和。
    迪艾姆python培训 黄哥所写 咨询:qq:1465376564  
    迪艾姆python远程视频培训班
    要求时间复杂度为O(n)
    """
    this_sum = 0
    max_sum = 0
    for item in lst:
        this_sum += item
        if this_sum > max_sum:
            max_sum = this_sum
        elif this_sum < 0:
            this_sum = 0
    return max_sum

test_lst = [-2,11,-4,13,-5,-2]
print(max_array(test_lst))
