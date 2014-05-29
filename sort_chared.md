#问题

已知字母序列【d, g, e, c, f, b, o, a】，请实现一个函数针对输入的一组字符串 input[] = {"bed", "dog", "dear", "eye"}，按照字母顺序排序并打印,结果应为：dear, dog, eye, bed。

#说明

本问题在网上比较常见，但这里尝试用另外一个思路，并且用python来写，与众多用c++的有所不同，且似乎短小了不少。自己感觉比网上参考到的更容易理解。

欢迎指点。

#解决(python)
    #! /usr/bin/env python
    #coding:utf-8

    def char_to_number(by_list,char):    #根据排序依据字母顺序，给另外一个字母编号
        try:
            return by_list.index(char)
        except:
            return 1000

    def sort_by_list(by_list,input_list):  

        result={}
        for word in input_list:
            number_list = [char_to_number(by_list,word[i]) for i in range(len(word))]
            
            #得到形如：{"good":[2,3,3,1],"book":[1,3,3,0]}样式的结果
            result[word] = number_list              
    
        #将得到的result生成[(key1,value1),(key2,value2),...]列表，按照value值排序，取出排序结果中的key即v[0]，生产列表。
        return [v[0] for v in sorted(result.items(),lambda x,y:cmp(x[1],y[1]))]         

    if __name__=="__main__":
        word = ["bed","dog","dear","eye"]
        by_string = ['d','g','e','c','f','b','o','a']
        print "the word list is:"
        print word
        print "\nwill sorted by:"
        print by_string
        print "\nthe result is:"
        print sort_by_list(by_string,word)
    
# 解法 （racket 5.2.1)

**对语言的掌握还不熟练，所以暂未考虑算法效率**

```racket
#lang racket

; 定义一个函数 filter-by-1st-char
; 输入一个字符 a-ch 和一个字符串 a-str
; 如果 a-ch 与 a-str 的第一个字符相同，
; 则以列表方式输出 a-str, 否则输出空列表 '() 
(define (filter-by-1st-char a-ch a-str)
  (if (char=? a-ch (string-ref a-str 0))
    (list a-word) '()))

; 定义一个函数 sort-words-by-char-list
; 它接受以字符串形式输入的一个字符序列 char-list, 
; 和以字符串列表形式输入的一个字符串序列 word-list
; 输出一个列表，其所有列表项即 word-list 中的所有字符串
; 并且将根据每个字符串的首字母，依照 char-list 所提供的顺序排序
; 而并非按一般英文词典的 a-z 顺序排序
(define (sort-words-by-char-list char-list word-list)
  (let 
    ([sorted-word-list '()]) ; 定义一个空列表用于存储排序后的 word
    (for ([ch char-list])
      (for ([wd word-list])
        (set! sorted-word-list 
          (append sorted-word-list ; 把符合条件的单词放进结果列表
            (filter-by-1st-char ch wd)))))
    sorted-word-list))

; 函数调用，正常运行时，应该输出 (dear dog eye bed)
(displayln
  (sort-words-by-char-list "dgecfboa" '("dear" "dog" "eye" "bed")))
```
