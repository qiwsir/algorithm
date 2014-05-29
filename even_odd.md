#问题

一个数组由若干个整数组成，现要求：将偶数放到前面，奇数放到后面，并输出数组。

#解决（python）

    #coding:utf-8
    is_odd_number = lambda data:(data%2!=0)

    def odd_even_sort(lst):
        """利用list conprehension"""
        tmp_list1 = [item for item in lst if is_odd_number(item)]
        tmp_list2 = [item for item in lst if not is_odd_number(item)]

    test_lst = [7,9,12,5,4,9,8,3,12,89]

    print (odd_even_sort(test_lst))

##本问题由黄老师提供并解决，[他的微博](http://weibo.com/qiyeminglu?from=feed&loc=nickname)

