#! /usr/bin/env python
#coding:utf-8

"""
最小生成树的Kruskal算法

描述：有A、B、C、D四个点，每两个点之间的距离（无方向）是(第一个数字是两点之间距离，后面两个字母代表两个点）：(1,'A','B'),(5,'A','C'),(3,'A','D'),(4,'B','C'),(2,'B','D'),(1,'C','D')
生成边长和最小的树，也就是找出一种连接方法，将各点连接起来，并且各点之间的距离和最小。

"""

#以全局变量X定义节点集合，即类似{'A':'A','B':'B','C':'C','D':'D'},如果A、B两点联通，则会更改为{'A':'B','B':'B",...},即任何两点联通之后，两点的值value将相同。

X = dict()      

#各点的初始等级均为0,如果被做为连接的的末端，则增加1

R = dict()

#设置X R的初始值

def make_set(point):
    X[point] = point
    R[point] = 0

#节点的联通分量

def find(point):
    if X[point] != point:
        X[point] = find(X[point])
    return X[point]

#连接两个分量（节点）

def merge(point1,point2):
    r1 = find(point1)
    r2 = find(point2)
    if r1 != r2:
        if R[r1] > R[r2]:
            X[r2] = r1
        else:
            X[r1] = r2
            if R[r1] == R[r2]: R[r2] += 1

#KRUSKAL算法实现

def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)

    minu_tree = set()
    
    edges = list(graph['edges'])
    edges.sort()                    #按照边长从小到达排序
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            merge(vertice1, vertice2)
            minu_tree.add(edge)
    return minu_tree


if __name__=="__main__":

    graph = {
        'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
        'edges': set([
            (1, 'A', 'B'),
            (5, 'A', 'C'),
            (3, 'A', 'D'),
            (4, 'B', 'C'),
            (2, 'B', 'D'),
            (1, 'C', 'D'),
            ])
        }

    result = kruskal(graph)
    print result

"""
参考:
1.https://github.com/qiwsir/Algorithms-Book--Python/blob/master/5-Greedy-algorithms/kruskal.py
2.《算法基础》(GILLES Brassard,Paul Bratley)
"""
