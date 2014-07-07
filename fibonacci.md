#问题

费波那契数列（意大利语：Successione di Fibonacci），又译费波拿契数、斐波那契数列、斐波那契数列、黄金分割数列。

在数学上，费波那契数列是以递归的方法来定义：

    F0 = 0     (n=0)
    F1 = 1    (n=1)
    Fn = F[n-1]+ F[n-2](n=>2)

关于Fibonacci的精彩解释，请看下列视频：

[TED-神奇的斐波那契数列](http://swf.ws.126.net/openplayer/v02/-0-2_M9HKRT25D_M9HNA0UNO-vimg1_ws_126_net//image/snapshot_movie/2014/1/6/L/M9HNA8H6L-.swf)

如果要查看文字解释，请看维基百科词条：[斐波那契数列](http://zh.wikipedia.org/wiki/%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0%E5%88%97)

#思路说明

几乎所有的高级语言都要拿Fibonacci数列为例子，解释递归、循环等概念。这里，我要用Python来演示一下，各种不同的写法，供参考。

#解决（python）

##递归——按照定义直接写

这种方法不是一个好方法，因为它的开销太大，比如计算fib1(100),就需要耐心等待较长一段时间了。所以，这是一种不实用的方法。但是，因为简单，列为第一种。

    def fib1(n):
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return fib1(n-1) + fib1(n-2)

##递归，进行初始化

fib1的慢，就是因为每次都要计算前面已经算过的项目.这里将上述算法进行稍微改进。速度快了很多。

    memo = {0:0, 1:1}
    def fib2(n):
        if not n in memo:
            memo[n] = fib2(n-1)+fib2(n-2)
        return memo[n]

##迭代

    def fib3(n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a+b
        return a

#直接理论数学结论

在[维基百科的词条](http://zh.wikipedia.org/wiki/%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0%E5%88%97) 里面，已经列出了不同形式的Fibonacci数列的数学结果，可以直接将这些结果拿过来，通过程序计算，得到斐波那契数。此类程序，本文略。

#[这种方法来自网络](http://www.cprogramto.com/fibonacci-sequence-python-code/)

    print('!* Fibonacci Sequence python \n')
    def Fibonacci_Series():
        x = input('Enter Series length to print fibonacci sequence')

        d,e=0,1
        a = []
        a.append(d)
        a.append(e)
        while(x!=2):
            c = d + e
            d = e
            e = c
            a.append(c)
            x = x -1
        print(a)
