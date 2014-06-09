#问题

最大连续子数组，求一个有正，有负数的数组(有正和负数，没有全是负数的情况)，连续子数组之最大和。
要求时间复杂度为O(n)

#解决（Python）

	#coding:utf-8
	
	def max_array(lst):
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

##迪艾姆python培训 黄哥所写 咨询:qq:1465376564  
##迪艾姆python远程视频培训班

# python 解法转译为 racket (racket 5.2.1)

经过推敲, 发现上述 python 的解法已经比较简单. 
在 O(n) 的时间复杂度限制下, 无论是换种解决策略或者进一步优化现有策略, 都没有想出好点子.
为了保持进度, 仅仅将 python 的解法实现转译为 racket 语言实现.

```racket

(define (max-array number-list)
  (let*
    ([this-sum 0]
     [max-sum 0])
    (for ([item number-list])
      (begin 
        (set! this-sum (+ this-sum item))
        (if (> this-sum max-sum)
          (set! max-sum this-sum)
          (if (< this-sum 0)
            (set! this-sum 0)
            '()))))
    max-sum))

; 函数调用, 正常运行后, 将输出一个整数 20.
(max-array '(-2 11 -4 13 -5 -2))

```

如果不限制 O(n) , 并且刻意消除 set! 这样的赋值操作, 
那么比较直观但浪费时间的解法如下:

```racket
#lang racket

(define number-list '(-2 11 -4 13 -5 -2))

(define (iterate-by-n a-list n)  ; 用穷举法列出某个列表中, 长度为 n 的所有连续子列表
  (let*
    ([len (length a-list)]
     [last-idx (- len n)])
    (for/list ([i (+ last-idx 1)])
      (take 
       (take-right a-list (- len i))
       n))))

(define (max-array number-list)
  (let 
    ([list-of-every-length   ; 用穷举法列出所有 "可能长度" 的连续子列表
      (for/list 
        ([i (in-range 1 (+ (length number-list) 1))])
          (iterate-by-n number-list i))])
    (apply max   ; 求所有可能的连续子列表分别求和, 求出其中的最大和
      (map (lambda (l) (apply + l))
        (apply append list-of-every-length)))))

; 函数调用, 正常运行的情况下, 将输出整数 20
(max-array number-list)
```
