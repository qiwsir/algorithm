#! /usr/bin/env python
#coding:utf-8

"""
问题
定义一个20*5的二维数组，用来存储某班级20位学员的5门课的成绩；这5门课按存储顺序依次为：core C++，coreJava，Servlet，JSP和EJB。
（1）循环给二维数组的每一个元素赋0~100之间的随机整数。
（2）按照列表的方式输出这些学员的每门课程的成绩。
（3）要求编写程序求每个学员的总分，将其保留在另外一个一维数组中。
（4）要求编写程序求所有学员的某门课程的平均分。
"""
from __future__ import division
import random


def score(score_list,course_list,student_num):
    course_num = len(course_list)
    
    every_score = [[score_list[j][i] for j in range(course_num)] for i in range(student_num)]
    
    every_total = [sum(every_score[i]) for i in range(student_num)]
    
    ave_course = [sum(score_list[i])/len(score_list[i]) for i in range(len(score_list))]
    
    return (every_score,every_total,ave_course)

if __name__=="__main__":
    
    course_list = ["C++","Java","Servlet","JSP","EJB"]
    student_num = 20
    
    score_list = [[random.randint(0,100) for i in range(student_num)] for j in range(len(course_list))]
    for i in range(len(course_list)):
        print "score of every one in %s:"%course_list[i]
        print score_list[i]

    every_score,every_total,ave_one_course = score(score_list,course_list,student_num)
    print "\n"
    print "NEXT IS EVERY ONE SCORE IN EVERY COURSE:"
    for name in course_list:
        print name,
    print "\t"
    print every_score
    print "\n"
    print "every one all score:\t",every_total
    print "every course of average score:\t",ave_one_course
