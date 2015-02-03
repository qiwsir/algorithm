#! /usr/bin python
#coding:utf-8

"""
问题：
定义一个int型的一维数组，包含40个元素，用来存储每个学员的成绩，循环产生40个0~100之间的随机整数，
(1)将它们存储到一维数组中，然后统计成绩低于平均分的学员的人数，并输出出来。
(2)将这40个成绩按照从高到低的顺序输出出来。
"""

#no need to import division from future just change num to float(num) 
import random

def make_score(num):
    score = [random.randint(0,100) for i in range(num)]
    return score

def less_average(score):
    num = len(score)
    sum_score = sum(score)
    ave_num = sum_score/float(num)
    less_ave = [i for i in score if i<ave_num]
    return (ave_num,len(less_ave))

if __name__=="__main__":
    score = make_score(40)
    average_num,less_num = less_average(score)
    print 'the score of average is:',average_num
    print "the number of less average is:",less_num
    print "the every score is[from big to small]:",sorted(score,reverse=True)
