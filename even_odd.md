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

#解决（python)

    def odd(x):return x%2==1    #判断是否为奇数，是则返回true
    def even(x):return x%2==0   

    if __name__=="__main__":
        test_lst = [7,9,12,5,4,9,8,3,12,89]
        print filter(even,test_lst)+filter(odd,test_lst)    #利用filter函数

#解决 (racket 5.2.1)

```racket
#lang racket

; 定义函数 odd-even-separator
; 输入一个由整数构成的列表
; 输出一个新的列表, 其元素取自输入的列表
; 假设输入列表长度为 N, 列表元素中有 k 个偶数, N-k 个奇数
; 那么输出的列表中, 前 k 个元素就是输入列表中的 k 个偶数
; 后 N-k 个元素就是输入列表中的 N-k 个奇数.
(define (odd-even-separator num-array)
  (let* 
      ([odd-arr (filter odd? arr1)]   ; 取出全部奇数形成新列表
       [even-arr (filter even? arr1)] ; 取出全部偶数形成新列表
       [separated-arr 
        (append even-arr odd-arr)])   ; 把两个新列表连接起来
    (displayln separated-arr)))       ; 打印到标准输出

; 函数调用, 正常运行后, 应该显示 (2 6 4 1 3 5 7 9)
(odd-even-separator '(1 3 2 6 5 7 9 4))

```
