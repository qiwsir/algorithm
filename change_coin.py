#!/usr/bin/env python
#coding:utf-8

"""
问题：

以人民币的硬币为例，假设硬币数量足够多。要求将一定数额的钱兑换成硬币。要求兑换硬币数量最少。

思路说明：

这是用贪婪算法的典型应用。在本例中用python来实现，主要思想是将货币金额除以某硬币单位，然后去整数，即为该硬币的个数；余数则做为向下循环计算的货币金额。

这个算法的问题在于，得出来的结果不一定是最有结果。比如，硬币单位是[1,4,6],如果将8兑换成硬币，按照硬币数量最少原则，应该兑换成为两个4（单位）的硬币，但是，按照本算法，得到的结果是一个6单位和两个1单位的硬币。这也是本算法的局限所在。所谓贪婪算法，本质就是只要找出一个结果，不考虑以后会怎么样。
"""

def change_coin(money):
    coin = [1,2,5,10,20,50,100]     #1分，2分，5分，1角，2角，5角，1元
    coin.sort(reverse=True)
    money = money*100               #以分为单位进行计算
    change = {}

    for one in coin:
        num_coin = money//one       #除法，取整，得到该单位硬币的个数
        if num_coin>0:
            change[one]=num_coin
        num_remain = money%one      #取余数，得到剩下的钱数
        if num_remain==0:
            break
        else:
            money = num_remain
    return change 

#以下方法，以动态方式，提供最小的硬币数量。避免了贪婪方法的问题。
def coinChange(centsNeeded, coinValues):
    minCoins = [[0 for j in range(centsNeeded + 1)] for i in range(len(coinValues))]
    minCoins[0] = range(centsNeeded + 1)
    
    for i in range(1,len(coinValues)):
        for j in range(0, centsNeeded + 1):
            if j < coinValues[i]:
                minCoins[i][j] = minCoins[i-1][j]
            else:
                minCoins[i][j] = min(minCoins[i-1][j], 1 + minCoins[i][j-coinValues[i]])
    return minCoins[-1][-1]

if __name__=="__main__":
    money = 3.42
    coin = [1,2,5,10,20,50,100]     #1分，2分，5分，1角，2角，5角，1元
    num_coin = change_coin(money)
    result = [(key,num_coin[key]) for key in sorted(num_coin.keys())]
    print "You have %s RMB"%money
    print "I had to change you:"
    print "    Coin    Number"
    for i in result:
        if i[0]==100:
            print "Yuan    %d    %d"%(i[0]/100,i[1])
        elif i[0]<10:
            print "Fen    %d    %d"%(i[0],i[1])
        else:
            print "Jiao    %d    %d"%(i[0]/10,i[1])
    num2 = coinChange(5,coin)
    print num2
#执行结果
#You have 3.42 RMB
#I had to change you:
#    Coin    Number
#    Fen    2    1
#    Jiao    2    2
#    Yuan    1    3

