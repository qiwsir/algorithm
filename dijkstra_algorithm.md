#问题

最短路径问题的Dijkstra算法

是由荷兰计算机科学家艾兹赫尔·戴克斯特拉提出。迪科斯彻算法使用了广度优先搜索解决非负权有向图的单源最短路径问题，算法最终得到一个最短路径树。该算法常用于路由算法或者作为其他图算法的一个子模块。

这个算法的python实现途径很多，网上能够发现不少。这里推荐一个我在网上看到的，本来打算自己写，看了这个，决定自己不写了，因为他的已经太好了。

#解决（Python）

	#!/usr/bin/env python
	#coding:utf-8
	
	# Dijkstra's algorithm for shortest paths
	# David Eppstein, UC Irvine, 4 April 2002
	# code source:http://www.algolist.com/code/python/Dijkstra%27s_algorithm
	
	from priodict import priorityDictionary
	
	def Dijkstra(G,start,end=None):
	    D = {}  # dictionary of final distances
	    P = {}  # dictionary of predecessors
	    Q = priorityDictionary()   # est.dist. of non-final vert.
	    Q[start] = 0
	                    
	    for v in Q:
	        D[v] = Q[v]
	
	        if v == end: break
	        
	        for w in G[v]:
	            vwLength = D[v] + G[v][w]
	            if w in D:
	                if vwLength < D[w]:
	                    raise ValueError, "Dijkstra: found better path to already-final vertex"
	                    
	                elif w not in Q or vwLength < Q[w]:
	                    Q[w] = vwLength
	                    P[w] = v
	                                
	        return (D,P)
	
	def shortestPath(G,start,end):
	    D,P = Dijkstra(G,start,end)
	    Path = []
	    while 1:
	             
	        Path.append(end)
	        if end == start: break
	        end = P[end]
	        
	    Path.reverse()
	    return Path
	
