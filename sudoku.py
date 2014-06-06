#! /usr/bin/env python
#coding:utf-8


#判断输入的九宫格的格数是否为奇数
def if_odd(n):
    if n%2==1:
        return True
    else:
        return False

#九宫格填写数的法则
"""
按照下面的方式排列
-------------->x(从1到n)
|
|
|y方向（从1到n)

1、第一个数放在X方向的中间位置
2、其它数顺次放置各个位置，并依据如下原则：（假设第一个数是a,第二个数是b）
以a为中心的位置关系分别为：
左上|上|右上
左  |a |右
左下|下|右下

（1）b放在a的右上位置。a(x,y)-->b(x+1,y-1)
（2）如果仅有“右”位置超过边界，即x+1>n，则b(1,y-1)
（3）如果仅有“上”位置超过边界，即y-1<0，则b(x+1,n)
（4）如果“右”“上”位置都超过边界，即x+1>n,y-1<o,则b(x,y+1)
（5）如果“右上”已经有值，则b(x,y+1)
"""
def sudoku_rule(n,sudoku):

    tx = n/2
    ty = 0
    for i in range(n*n):
        sudoku[ty][tx] = i+1
        tx = tx+1
        ty = ty-1
        if ty<0 and tx>=n:      #条件（4）
            tx = tx-1
            ty = ty+2
        elif ty<0:              #(3)
            ty = n-1
        elif tx>=n:             #(2)
            tx = 0
        elif sudoku[ty][tx]!=0: #(5)
            tx = tx-1
            ty = ty+2
    return sudoku

if __name__=="__main__":
    n = 5 
    sudoku = [[0 for i in range(n)] for i in range(n)]
    s = sudoku_rule(n,sudoku)
    for line in s:
        print line
        

        

