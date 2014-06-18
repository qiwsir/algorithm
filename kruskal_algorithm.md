#问题

最小生成树的Kruskal算法

描述：有A、B、C、D四个点，每两个点之间的距离（无方向）是(第一个数字是两点之间距离，后面两个字母代表两个点）：(1,'A','B'),(5,'A','C'),(3,'A','D'),(4,'B','C'),(2,'B','D'),(1,'C','D')
生成边长和最小的树，也就是找出一种连接方法，将各点连接起来，并且各点之间的距离和最小。

#思路说明：

Kruskal算法是经典的无向图最小生成树解决方法。此处列举两种python的实现方法。这两种方法均参考网上，并根据所学感受进行了适当改动。

#解决1（Python）

	#! /usr/bin/env python
	#coding:utf-8
	
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


#解决2（Python）

以下代码参考http://www.ics.uci.edu/~eppstein/PADS/的源码

	#! /usr/bin/env python
	#coding:utf-8
	
	import unittest
	
	class UnionFind:
	    """
	    UnionFind的实例：
	    Each unionFind instance X maintains a family of disjoint sets of
	    hashable objects, supporting the following two methods:
	
	    - X[item] returns a name for the set containing the given item.
	      Each set is named by an arbitrarily-chosen one of its members; as
	      long as the set remains unchanged it will keep the same name. If
	      the item is not yet part of a set in X, a new singleton set is
	      created for it.
	
	    - X.union(item1, item2, ...) merges the sets containing each item
	      into a single larger set.  If any item is not yet part of a set
	      in X, it is added to X as one of the members of the merged set.
	    """
	
	    def __init__(self):
	        """Create a new empty union-find structure."""
	        self.weights = {}
	        self.parents = {}
	
	    def __getitem__(self, object):
	        """Find and return the name of the set containing the object."""
	
	        # check for previously unknown object
	        if object not in self.parents:
	            self.parents[object] = object
	            self.weights[object] = 1
	            return object
	
	        # find path of objects leading to the root
	        path = [object]
	        root = self.parents[object]
	        while root != path[-1]:
	            path.append(root)
	            root = self.parents[root]
	
	        # compress the path and return
	        for ancestor in path:
	            self.parents[ancestor] = root
	        return root
	        
	    def __iter__(self):
	        """Iterate through all items ever found or unioned by this structure."""
	        return iter(self.parents)
	
	    def union(self, *objects):
	        """Find the sets containing the objects and merge them all."""
	        roots = [self[x] for x in objects]
	        heaviest = max([(self.weights[r],r) for r in roots])[1]
	        for r in roots:
	            if r != heaviest:
	                self.weights[heaviest] += self.weights[r]
	                self.parents[r] = heaviest
	
	
	"""
	Various simple functions for graph input.
	
	Each function's input graph G should be represented in such a way that "for v in G" loops through the vertices, and "G[v]" produces a list of the neighbors of v; for instance, G may be a dictionary mapping each vertex to its neighbor set.
	
	D. Eppstein, April 2004.
	"""
	
	def isUndirected(G):
	    """Check that G represents a simple undirected graph."""
	    for v in G:
	        if v in G[v]:
	            return False
	        for w in G[v]:
	            if v not in G[w]:
	                return False
	    return True
	
	
	def union(*graphs):
	    """Return a graph having all edges from the argument graphs."""
	    out = {}
	    for G in graphs:
	        for v in G:
	            out.setdefault(v,set()).update(list(G[v]))
	    return out
	
	
	"""
	Kruskal's algorithm for minimum spanning trees. D. Eppstein, April 2006.
	"""
	
	def MinimumSpanningTree(G):
	    """
	    Return the minimum spanning tree of an undirected graph G.
	    G should be represented in such a way that iter(G) lists its
	    vertices, iter(G[u]) lists the neighbors of u, G[u][v] gives the
	    length of edge u,v, and G[u][v] should always equal G[v][u].
	    The tree is returned as a list of edges.
	    """
	    if not isUndirected(G):
	        raise ValueError("MinimumSpanningTree: input is not undirected")
	    for u in G:
	        for v in G[u]:
	            if G[u][v] != G[v][u]:
	                raise ValueError("MinimumSpanningTree: asymmetric weights")
	
	    # Kruskal's algorithm: sort edges by weight, and add them one at a time.
	    # We use Kruskal's algorithm, first because it is very simple to
	    # implement once UnionFind exists, and second, because the only slow
	    # part (the sort) is sped up by being built in to Python.
	    subtrees = UnionFind()
	    tree = []
	    for W,u,v in sorted((G[u][v],u,v) for u in G for v in G[u]):
	        if subtrees[u] != subtrees[v]:
	            tree.append((u,v))
	            subtrees.union(u,v)
	    return tree        
	
	
	# If run standalone, perform unit tests
	
	class MSTTest(unittest.TestCase):
	    def testMST(self):
	        """Check that MinimumSpanningTree returns the correct answer."""
	        G = {0:{1:11,2:13,3:12},1:{0:11,3:14},2:{0:13,3:10},3:{0:12,1:14,2:10}}
	        T = [(2,3),(0,1),(0,3)]
	        for e,f in zip(MinimumSpanningTree(G),T):
	            self.assertEqual(min(e),min(f))
	            self.assertEqual(max(e),max(f))
	
	if __name__ == "__main__":
	    unittest.main()   
