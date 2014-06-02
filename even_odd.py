#! /usr/bin/env python
#coding:utf-8

'''
#way1

def odd_even_sort(lst):
    
    is_odd_number = lambda data:(data%2!=0)
    tmp_list1 = [item for item in lst if is_odd_number(item)]
    tmp_list2 = [item for item in lst if not is_odd_number(item)]
    return tmp_list1+tmp_list2


if __name__=="__main__":
    test_lst = [7,9,12,5,4,9,8,3,12,89]

    print odd_even_sort(test_lst)

'''

#way2

def odd(x):return x%2==1    
def even(x):return x%2==0   

if __name__=="__main__":
    test_lst = [7,9,12,5,4,9,8,3,12,89]
    print filter(even,test_lst)+filter(odd,test_lst)
