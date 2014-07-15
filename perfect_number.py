#!/usr/bin/env python
#coding:utf-8

"""
找出完全数
"""

#找出一个数的因数
def factors(n):
    #return [i for i in range(1,n/2+1) if n%i == 0]
    #如果仅仅是为了得到因数，可以用上面的
    #如果是配合下面完全数，最好使用下面的。因为在下面少循环一次，1肯定是任何整数的因数
    return [i for i in range(2,n/2+1) if n%i == 0]

#找出某个数n以内的所有完全数，即在[1,n]内(含n)
def perfect(n):
    #从上面的factors中得到的因数列表中，少1,因此在求因数和的时候，要把1加上。
    return [i for i in range(2,n+1) if (sum(factors(i))+1)==i]

if __name__=="__main__":
    print perfect(30)

