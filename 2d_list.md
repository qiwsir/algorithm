#问题

定义一个20*5的二维数组，用来存储某班级20位学员的5门课的成绩；这5门课按存储顺序依次为：core C++，coreJava，Servlet，JSP和EJB。

（1）循环给二维数组的每一个元素赋0~100之间的随机整数。

（2）按照列表的方式输出这些学员的每门课程的成绩。

（3）要求编写程序求每个学员的总分，将其保留在另外一个一维数组中。

（4）要求编写程序求所有学员的某门课程的平均分。

#解决（python）

	#! /usr/bin/env python
	#coding:utf-8
	
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

##qiwsir#gmail.com (# to @)

#解法 (racket 5.2.1)

```racket
#lang racket

(define (2d-list)
  (let*
    ([rand-100 (lambda () (random 101))]
     [nth-picker (lambda (n) (lambda (l) (list-ref l n)))]
     [average (lambda (number-list) (exact->inexact (/ (apply + number-list) (length number-list))))]
     [course-list (list "coreC++" "coreJava" "Servlet" "JSP" "EJB")]
     [score-list (for/list ([i 20]) (for/list ([j 5]) (rand-100)))]
     [score-by-course-list (for/list ([i 5]) (list ((nth-picker i) course-list) (map (nth-picker i) score-list)))]
     [score-by-student-list (for/list ([i 20]) (list-ref score-list i))]
     [total-by-student-list (for/list ([i 20]) (apply + (list-ref score-list i)))]
     [average-by-course-list (for/list ([i 5]) (list ((nth-picker i) course-list) (average (map (nth-picker i) score-list))))])
    (for ([i 5]) 
      (display "score of every one in ")
      (displayln (first ((nth-picker i) score-by-course-list)))
      (displayln (second ((nth-picker i) score-by-course-list))))
    (displayln "")
    (displayln "NEXT IS EVERY ONE SCORE IN EVERY COURSE: ")
    (displayln course-list)
    (for ([i 10]) 
      (displayln (list-ref score-by-student-list i)))
    (displayln "")
    (displayln "every one all score: ")
    (displayln total-by-student-list)
    (displayln "")
    (displayln "every course of average score: ")
    (displayln average-by-course-list)))

; 调用函数, 正常时应输出类似如下结果
;score of every one in coreC++
;(12 58 60 28 78 23 34 83 19 83 78 26 51 94 93 74 53 89 8 23)
;... ...
;NEXT IS EVERY ONE SCORE IN EVERY COURSE: 
;(coreC++ coreJava Servlet JSP EJB)
;(12 49 75 88 68)
;(58 78 6 88 81)
;... ...
;every one all score: 
;(292 311 370 241 289 250 254 258 147 232 271 170 224 248 317 286 246 270 186 212)
;
;every course of average score: 
;((coreC++ 53.35) (coreJava 53.9) (Servlet 51.95) (JSP 49.6) (EJB 44.9))
(2d-list)

```
