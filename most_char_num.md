#问题：

查找字符串中出现最多的字符和个数？

如 sdsdsddssssssdd -> 字符最多的是s，出现9次

#思路说明

利用python中的collections模块的Counter，[查此函数详细内容](https://docs.python.org/2/library/collections.html).对字符串进行统计。

然后将结果转化为字典类型。

特别注意，在字符串中可能会出现数量并列第一的字符，因此要通过循环找出最大数之后，再通过循环找出最大数对应的字母（键）。

#解答1(python)

    import collections

    def most_character_number(one_string):
        static_result = collections.Counter(one_string) 
        result = dict(static_result)                            
        most_number = max([value for value in result.values()])
        most_character = [key for key,value in result.items() if value==most_number]
        return (most_number,most_character)

    if __name__ == "__main__":
        (most_num,most_char) = most_character_number("yyyyyyddddddkuuuiii")
        print ("The most character is:%s"%most_num)
        print ("The number is:")
        for char in most_char:
            print char

#解答2(python)

    str1 = "sdsdsddssssssssdd"
    
    def most_character_number(one_string):
        """利用字典key来统计次数"""
        str_dict = {}
        for item in one_string:
            if item in str_dict:
                str_dict[item] +=1
            else:
                str_dict[item] =1

        
        str_dict = {str_dict[key]:key for key in str_dict}
        return (max(str_dict),str_dict[max(str_dict)])

    print (most_character_number(str1))

解答2由黄老师提供，[他的微博](http://weibo.com/qiyeminglu)。

##欢迎接龙，可以按照上面格式继续。

------

#解答3 (racket 5.2.1)

```racket
#lang racket

; 需要引用 scheme 标准库中的 list 库 (SRFI-1)
(require srfi/1)

; 定义函数 get-key-by-value
; 输入一个 Hash 表和一个 a-value (用于反向查找 key 的 value)
; 输出 value 等于 a-value 的那些 key,
; 换言之, 此 key 满足条件 (hash-ref key) == a-value.
(define (get-key-by-value a-hash a-value)
  (hash-for-each a-hash
    (lambda (k v)
      (if (= a-value (hash-ref a-hash k))
        (printf "~a: ~a~n" k v) '()))))

; 定义函数 char-cmp
; 输入一个 preset-char (预设字符)
; 返回一个的匿名函数 (其内部包含 preset-char)
; > 其输入为 char-to-be-compared (待比较的字符)
; > 当 char-to-be-compared 与 preset-char 
; > 相等时输出 true, 否则输出 false
(define (char-cmp preset-char)
  (lambda (char-to-be-compared)
    (if (char=? preset-char char-to-be-compared) true false)))

; 定义函数 most-character-number
; 输入一个 a-string 任意字符串
; 输出 a-string 中出现次数最多的字符, 及其出现次数
(define (most-character-number a-string)
  (let*
    ([all-chars-list (string->list a-string)]
     [key-chars-list (delete-duplicates all-chars-list)]
     [result-hash (make-hash)])
    (for ([key-char key-chars-list])
      (hash-set! result-hash
        key-char (count (char-cmp key-char) all-chars-list)))
      (get-key-by-value 
        result-hash 
        (apply max (hash-values result-hash)))))

; 以下函数调用在正常运行之后, 应该显示
; f: 3
; d: 3
; a: 3
(most-character-number "ssfdaa dffda ")
```

##联系老齐：qiwsir#gmail.com
