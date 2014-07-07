#! /usr/bin/env python
#coding:utf-8

"""
Fibonacci数列定义：

F0 = 0     (n=0)
F1 = 1    (n=1)
Fn = F[n-1]+ F[n-2](n=>2)

"""

#递归，根据定义直接写
#这种方法不是一个好方法，因为它的开销太大，比如计算fib1(100),就需要耐心等待较长一段时间了。

def fib1(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)


#递归，进行初始化
#fib1的慢，就是因为每次都要计算前面已经算过的项目.这里将上述算法进行稍微改进。

memo = {0:0, 1:1}
def fib2(n):
    if not n in memo:
        memo[n] = fib2(n-1)+fib2(n-2)
    return memo[n]

#迭代

def fib3(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

#除了上述方法之外，还可以直接用数学运算的结果
#推荐参考：http://zh.wikipedia.org/wiki/%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0%E5%88%97中的结论

#这种方法来自：http://www.cprogramto.com/fibonacci-sequence-python-code/

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

#Output:
"""
!* Fibonacci Sequence python 

>>> Fibonacci_Series()
Enter Series length to print fibonacci sequence10
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
>>>
"""
if __name__=="__main__":
    
    Fibonacci_Series() 
