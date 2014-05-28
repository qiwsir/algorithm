#问题

请写一个字符串转成驼峰的方法？

例如：border-bottom-color -> borderBottomColor

#解决

##python解决方法：
    def convert(one_string,space_character):    #one_string:输入的字符串；space_character:字符串的间隔符，以其做为分隔标志

        string_list = str(one_string).split(space_character)    #将字符串转化为list
        first = string_list[0].lower()
        others = string_list[1:] 

        others_capital = [word.capitalize() for word in others]      #str.capitalize():将字符串的首字母转化为大写

        others_capital[0:0] = [first]

        hump_string = ''.join(others_capital)     #将list组合成为字符串，中间无连接符。

        return hump_string

    if __name__=='__main__':
        print "the string is:ab-cd-ef"
        print "convert to hump:"
        print convert("ab-cd-ef","-")
        

##欢迎补充其它语言的解决方法

###racket解决方法 (racket 5.2.1)

```racket
#lang racket

; 定义字符串转换函数 train-to-camel
(define (train-to-camel train-str separator-char)
  (let
    [(splited-str (regexp-split separator-char train-str))]      ; 把原始字符串用 '-' 分成多个单独的单词
    (string-append
      (first splited-str)
      (apply
        string-append
        (map
          string-titlecase
          (rest splited-str))))))

; 调用字符串转换函数 train-to-camel
(train-to-camel "this-is-a-var" "-")  ; 正常运行的情况下, 应输出 "thisIsAVar"

```

--------------

### Ruby 解决方法

```ruby
str.split('-').map{|x| x.capitalize}.join
```

```ruby
str = 'border-bottom-color'
str.split('-').map{|x| x.capitalize}.join
# => "BorderBottomColor"
```

###联系我：老齐 qiwsir#gmail.com (# to @)
