#问题

无向图最小生成树的Prim算法

#思路说明

假设点A,B,C,D,E,F，两点之间有连线的，以及它们的距离分别是：(A-B:7);(A-D:5);(B-C:8);(B-D:9);(B-E:7);(C-E:5);(D-E:15);(D-F:6);(E-F:8);(E-G:9);(F-G:11)

关于Prim算法的计算过程，参与维基百科的词条：[普里姆算法](http://zh.wikipedia.org/wiki/%E6%99%AE%E6%9E%97%E5%A7%86%E7%AE%97%E6%B3%95)

将上述点与点关系以及两点之间距离（边长，有的文献中称之为权重）写成矩阵形式（在list中，每两个点及其之间的距离组成一个tuple)

edges = [ ("A", "B", 7), 
          ("A", "D", 5),
          ("B", "C", 8), 
          ("B", "D", 9), 
          ("B", "E", 7), 
          ("C", "E", 5),
          ("D", "E", 15), 
          ("D", "F", 6),
          ("E", "F", 8), 
          ("E", "G", 9),
          ("F", "G", 11)
        ]

在下面的解决方法中，要计算出与已经选出的若干个点有相邻关系的点中，相应边长最短的点。这本质上是排序之后取出最小的，因为这种排序是动态的，如果用sorted或者list.sort()之类的方法对list排序，一则速度慢（python中的sort方法对大数据时不是很快),二则代码也长了。幸好python提供了一个非常好用的模块：heapq。这个模块是堆排序方法实现排序，并能够随时取出最小值。简化代码，更重要是提升了速度。

就用这个来解决Prim算法问题了。

#解决（Python）
	
	#! /usr/bin/env python
	#coding:utf-8
	
	from collections import defaultdict
	from heapq import *
	
	def prim( vertexs, edges ):
	    adjacent_vertex = defaultdict(list)      
        
        """
        注意：defaultdict(list)必须以list做为变量，可以详细阅读：[collections.defaultdict](https://docs.python.org/2/library/collections.html#collections.defaultdict)
	    """
	    for v1,v2,length in edges:
            adjacent_vertex[v1].append((length, v1, v2))
            adjacent_vertex[v2].append((length, v2, v1))

        """
	    经过上述操作，将edges列表中各项归类成以某点为dictionary的key，其value则是其相邻的点以及边长。如下：
	
	    defaultdict(<type 'list'>, {'A': [(7, 'A', 'B'), (5, 'A', 'D')], 
                                    'C': [(8, 'C', 'B'), (5, 'C', 'E')], 
                                    'B': [(7, 'B', 'A'), (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E')], 
                                    'E': [(7, 'E', 'B'), (5, 'E', 'C'), (15, 'E', 'D'), (8, 'E', 'F'), (9, 'E', 'G')], 
                                    'D': [(5, 'D', 'A'), (9, 'D', 'B'), (15, 'D', 'E'), (6, 'D', 'F')], 
                                    'G': [(9, 'G', 'E'), (11, 'G', 'F')], 
                                    'F': [(6, 'F', 'D'), (8, 'F', 'E'), (11, 'F', 'G')]})
	
	    """
	
	    mst = []        #存储最小生成树结果
	
	    chosed = set(vertexs[0]) 
	
	    """
	    vertexs是顶点列表，vertexs = list("ABCDEFG")===>vertexs=['A', 'B', 'C', 'D', 'E', 'F', 'G']
	    >> chosed=set(vertexs[0])
	    >> chosed
	    set(['A'])
	    也就是，首先选一个点（这个点是可以任意选的），以这个点为起点，找其相邻点，以及最短边长。
	
	    """

        #得到adjacent_vertexs_edges中顶点是'A'（nodes[0]='A')的相邻点list，即adjacent_vertexs['A']=[(7,'A','B'),(5,'A','D')]
	
	    adjacent_vertexs_edges = adjacent_vertex[vertexs[0]]  
	    
        #将usable_edges加入到堆中，并能够实现用heappop从其中动态取出最小值。关于heapq模块功能，参考python官方文档

	    heapify(adjacent_vertexs_edges)
	
	    while adjacent_vertexs_edges:
            #得到某个定点（做为adjacent_vertexs_edges的键）与相邻点距离（相邻点和边长/距离做为该键的值）最小值，并同时从堆中清除。
	        w, v1, v2 = heappop(adjacent_vertexs_edges)     
	        if v2 not in chosed:

                #在used中有第一选定的点'A'，上面得到了距离A点最近的点'D',举例是5。将'd'追加到used中
	            chosed.add(v2)                          

	            mst.append((v1,v2,w))          #将v1,v2,w，第一次循环就是('A','D',5) append into mst
	            
                #再找与d相邻的点，如果没有在heap中，则应用heappush压入堆内，以加入排序行列 

                for next_vertex in adjacent_vertex[v2]:                    
	                if next_vertex[2] not in chosed:
	                    heappush( adjacent_vertexs_edges,next_vertex)
	    return mst
	
	
	#test
	vertexs = list("ABCDEFG")
	edges = [ ("A", "B", 7), ("A", "D", 5),
	          ("B", "C", 8), ("B", "D", 9), 
	          ("B", "E", 7), ("C", "E", 5),
	          ("D", "E", 15), ("D", "F", 6),
	          ("E", "F", 8), ("E", "G", 9),
	          ("F", "G", 11)]
	
	print "edges:",edges
	print "prim:", prim( vertexs, edges )

##运行结果

edges: [('A', 'B', 7), ('A', 'D', 5), ('B', 'C', 8), ('B', 'D', 9), ('B', 'E', 7), ('C', 'E', 5), ('D', 'E', 15), ('D', 'F', 6), ('E', 'F', 8), ('E', 'G', 9), ('F', 'G', 11)]

prim: [('A', 'D', 5), ('D', 'F', 6), ('A', 'B', 7), ('B', 'E', 7), ('E', 'C', 5), ('E', 'G', 9)]


