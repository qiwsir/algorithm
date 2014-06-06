#问题

要求定义一个int型数组a,包含100个元素,保存100个随机的4位数。再定义一个int型数组b，包含10个元素。统计a数组中的元素对10求余等于0的个数，保存到b[0]中；对10求余等于1的个数，保存到b[1]中，……依此类推。

#解决（python）

    #!/usr/bin/env python
    #coding:utf-8

    import random
    if __name__=="__main__":
        a = [random.randint(1000,9999) for i in range(101)]
        a_remainder = [i%10 for i in a]
        b = [a_remainder.count(i) for i in range(10)]
        print a
        print a_remainder
        print b

#解决 (racket 5.2.1)

```racket
#lang racket

; 定义函数 equal-to-k
; 它接受一个整数输入 k
; 它输出一个只返回 true/false 的匿名函数
; 当 k = 1 时, equal-to-k 的功能可以这样理解
; (equal-to-k 1) => true
; (equal-to-k 2) => false
(define (filter-by-k k) 
  (lambda (n) (if (= k n) true false)))

; 定义函数 random-list-100-remainder-stats
; 它不接受任何输入
; 它输出一个整数型列表 b, 其每个元素的定义如下
; > 给定一个整数型列表 a,包含 100 个元素,保存 100 个随机的 4 位数。
; > 整数型列表 b，包含 10 个元素。
; > 统计a列表中的元素对10求余等于0的个数，保存到b[0]中；
; > 对10求余等于1的个数，保存到b[1]中，……依此类推。
(define (random-list-100-remainder-stats)
  (let*
      ([rand-e4 (lambda () (+ 1000 (random 9000)))]     ; 定义 1000~9999 之间的随机数"生成器"
       [rand-list-100 (for/list ([i 100]) (rand-e4))]   ; 生成长度为 100 的列表, 其中每个元素都是 1000~9999 之间的随机数
       [get-remainder-by-10 (lambda (n) (modulo n 10))] ; 定义对某整数除以 10 取余数的"生成器"
       [remainder-list-100 (map get-remainder-by-10 rand-list-100)] ; 对前面长为 100 的列表批量除以 10 取余数
       ; 最后, 对余数做统计, 生成 b 列表
       [remainder-list-stats (for/list ([k (in-range 0 10)]) (count (filter-by-k k) remainder-list-100))])
    ; 把生成的 b 列表输出出来
    remainder-list-stats))

; 函数调用, 正常执行时, 应输出一个整数的列表
; 此列表的展现形式类似于 '(7 11 13 10 5 11 6 11 12 14)
(random-list-100-remainder-stats)
```
