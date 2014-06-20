#! /usr/bin/env python
#coding:utf-8


from collections import defaultdict
from heapq import *


def prim( vertexs, edges ):
    adjacent_vertex = defaultdict(list)
    for v1,v2,length in edges:
        adjacent_vertex[v1].append((length, v1, v2))
        adjacent_vertex[v2].append((length, v2, v1))

    mst = []
    chosed = set(vertexs[0]) 

    adjacent_vertexs_edges = adjacent_vertex[vertexs[0]]  
    
    heapify(adjacent_vertexs_edges)

    while adjacent_vertexs_edges:
        w, v1, v2 = heappop(adjacent_vertexs_edges) 
        if v2 not in chosed:
            chosed.add(v2)                    
            mst.append((v1,v2,w))   
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
