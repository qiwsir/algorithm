#! /usr/bin/env python
#coding:utf-8

class Node:
    """
    二叉树左右枝
    """
    def __init__(self, data):
        """
        节点结构

        """
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        """
        插入节点数据
        """
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def lookup(self, data, parent=None):
        """
        遍历二叉树
        """
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent

    def delete(self, data):
        """
        删除节点
        """
        node, parent = self.lookup(data)        #已有节点
        if node is not None:
            children_count = node.children_count()      #判断子节点数
            if children_count == 0:
                # 如果该节点下没有子节点，即可删除
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                del node
            elif children_count == 1:
                # 如果有一个子节点，则让子节点上移替换该节点（该节点消失)
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent:
                    if parent.left is node:
                        parent.left = n
                    else:
                        parent.right = n
                del node
            else:
                # 如果有两个子节点，则要判断节点下所有叶子
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                node.data = successor.data
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right

    def compare_trees(self, node):
        """
        比较两棵树
        """
        if node is None:
            return False
        if self.data != node.data:
            return False
        res = True
        if self.left is None:
            if node.left:
                return False
        else:
            res = self.left.compare_trees(node.left)
        if res is False:
            return False
        if self.right is None:
            if node.right:
                return False
        else:
            res = self.right.compare_trees(node.right)
        return res
                
    def print_tree(self):
        """
        按顺序打印数的内容
        """
        if self.left:
            self.left.print_tree()
        print self.data,
        if self.right:
            self.right.print_tree()

    def tree_data(self):
        """
        二叉树数据结构
        """
        stack = []
        node = self
        while stack or node: 
            if node:
                stack.append(node)
                node = node.left
            else: 
                node = stack.pop()
                yield node.data
                node = node.right

    def children_count(self):
        """
        子节点个数
        """
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt

