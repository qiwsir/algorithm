#! /usr/bin/env python
#coding:utf-8

"""
#问题
用递归方式遍历二叉树
"""

from collections import namedtuple
from sys import stdout
 
Node = namedtuple('Node', 'data, left, right')
tree = Node(1,
            Node(2,
                 Node(4,
                      Node(7, None, None),
                      None),
                 Node(5, None, None)),
            Node(3,
                 Node(6,
                      Node(8, None, None),
                      Node(9, None, None)),
                 None))


#前序（pre-order，NLR）

def preorder(node):
    if node is not None:
        print node.data,
        preorder(node.left)
        preorder(node.right)


#中序（in-order，LNR）

def inorder(node):
    if node is not None:
        inorder(node.left)
        print node.data,
        inorder(node.right)


#后序（post-order，LRN）

def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print node.data,


#层序（level-order）

def levelorder(node, more=None):
    if node is not None:
        if more is None:
            more = []
        more += [node.left, node.right]
        print node.data,
    if more:    
        levelorder(more[0], more[1:])
 
print '  preorder: ',
preorder(tree)
print '\t\n   inorder: ',
inorder(tree)
print '\t\n postorder: ',
postorder(tree)
print '\t\nlevelorder: ',
levelorder(tree)
print '\n'
