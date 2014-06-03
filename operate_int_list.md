#问题

定义一个int型的一维数组，包含10个元素，赋一些随机整数
然后求出所有元素的最大值，最小值，平均值，和值，并输出出来。

#思路说明

本问题是一个普通的对整数数组的操作，在下面的Python解决方法中，主要是尝试了python的一个内置函数reduce。

#解决（Python）

    #! /usr/bin/env python
    #coding:utf-8

    from __future__ import division     #实现精确的除法，例如4/3=1.333333
    import random

    def add(x,y):
        return x+y

    def operate_int_list():
        int_list = [random.randint(1,100) for i in range(10)]     #在1,100范围内，随机选择10个整数组成一个list
        max_num = max(int_list)
        min_num = min(int_list)
        sum_num = reduce(add,int_list)      #这里使用了reduce函数，也可以使用for循环，如下所示
        """
        sum_num = 0
        for i in int_list:
            sum_num = sum_num+i
        """
        ave_num = sum_num/len(int_list)

        return (int_list,max_num,min_num,sum_num,ave_num)

    if __name__=="__main__":
        int_list,max_num,min_num,sum_num,ave_num = operate_int_list()
        print "the int list is:",int_list
        print "max number is:",max_num
        print "min number is:",min_num
        print "the sum of all int in the list:",sum_num
        print "the average of the sum:",ave_num

# 解法 (racket 5.2.1)

```racket
#lang racket

; 定义一个函数 operate-int-list
; 它接受一个正整数输入 n
; 它的输出是一个列表
; 列表的第一项是一个长度为 n 的列表, 此列表的每个元素都是一个 1~100 之间的伪随机数
; 列表的第二、三、四、五项分别为
; 所有伪随机数中的最大者
; 所有伪随机数中的最小者
; 所有伪随机数的总和
; 所有伪随机数中平均值，以有理数形式表示
(define (operate-int-list n)
  (if (<= n 0)
      false
      (let* 
          ([rand1to100 (lambda () (+ 1 (random 100)))]
           [random-list (for/list ([i n]) (rand1to100))]
           [max-int (apply max random-list)]
           [min-int (apply min random-list)]
           [sum (apply + random-list)]
           [average (/ (apply + random-list) (length random-list))])
        (list random-list
              max-int min-int sum average))))

; 函数调用，当程序运行正常时，运算结果在形式上类似于以下结果，
; 但每次的结果列表都有一定的随机性
; '((19 77 15 49 39 84 45 72 75 100) 100 15 575 57½)
(operate-int-list 10)
```
