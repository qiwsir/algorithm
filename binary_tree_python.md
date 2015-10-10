#问题

Python中的二叉树查找算法模块

#思路说明

二叉树查找算法，在开发实践中，会经常用到。按照惯例，对于这么一个常用的东西，Python一定会提供轮子的。是的，python就是这样，一定会让开发者省心，降低开发者的工作压力。

python中的二叉树模块内容：

- BinaryTree：非平衡二叉树
- AVLTree：平衡的AVL树
- RBTree：平衡的红黑树

以上是用python写的，相面的模块是用c写的，并且可以做为Cython的包。

- FastBinaryTree
- FastAVLTree
- FastRBTree

**特别需要说明的是：树往往要比python内置的dict类慢一些，但是它中的所有数据都是按照某个关键词进行排序的，故在某些情况下是必须使用的。**

#安装和使用

##安装方法

###安装环境：

ubuntu12.04, python 2.7.6

###安装方法

- 下载源码，地址：https://bitbucket.org/mozman/bintrees/src
- 进入源码目录，看到setup.py文件，在该目录内运行
    
    python setup.py install

安装成功，ok!下面就看如何使用了。

###应用

bintrees提供了丰富的API,涵盖了通常的多种应用。下面逐条说明其应用。

- 引用

如果按照一般模块的思路，输入下面的命令引入上述模块
    
    >>> import bintrees
    
错了，这是错的，出现如下警告：(×××不可用，用×××）
    
    Warning: FastBinaryTree not available, using Python version BinaryTree.
    Warning: FastAVLTree not available, using Python version AVLTree.
    Warning: FastRBTree not available, using Python version RBTree.

正确的引入方式是：
     
    >>> from bintrees import BinaryTree     #只引入了BinartTree
    >>> from bintrees import *              #三个模块都引入了
    
- 实例化

看例子：

    >>> btree = BinaryTree()
    >>> btree
    BinaryTree({})
    >>> type(btree)
    <class 'bintrees.bintree.BinaryTree'>
    
- 逐个增加键值对：.__setitem__(k,v) .复杂度O(log(n))(后续说明中，都会有复杂度标示，为了简单，直接标明：O(log(n)).)

看例子：

    >>> btree.__setitem__("Tom","headmaster")
    >>> btree
    BinaryTree({'Tom': 'headmaster'})
    >>> btree.__setitem__("blog","http://blog.csdn.net/qiwsir")
    >>> btree
    BinaryTree({'Tom': 'headmaster', 'blog': 'http://blog.csdn.net/qiwsir'})
    
- 批量添加：.update(E)  E是dict/iterable，将E批量更新入btree. O(E*log(n))
    
看例子：

    >>> adict = [(2,"phone"),(5,"tea"),(9,"scree"),(7,"computer")]
    >>> btree.update(adict)
    >>> btree
    BinaryTree({2: 'phone', 5: 'tea', 7: 'computer', 9: 'scree', 'Tom': 'headmaster', 'blog': 'http://blog.csdn.net/qiwsir'})
    
- 查找某个key是否存在：.__contains__(k)  如果含有键k，则返回True,否则返回False. O(log(n))
    
看例子：

    >>> btree
    BinaryTree({2: 'phone', 5: 'tea', 7: 'computer', 9: 'scree', 'Tom': 'headmaster', 'blog': 'http://blog.csdn.net/qiwsir'})
    >>> btree.__contains__(5)
    True
    >>> btree.__contains__("blog")
    True
    >>> btree.__contains__("qiwsir")
    False
    >>> btree.__contains__(1)
    False
    
- 根据key删除某个key-value：.__delitem__(key), O(log(n))
    
看例子：

    >>> btree
    BinaryTree({2: 'phone', 5: 'tea', 7: 'computer', 9: 'scree', 'Tom': 'headmaster', 'blog': 'http://blog.csdn.net/qiwsir'})
    >>> btree.__delitem__(5)        #删除key=5的key-value,即：5:'tea' 被删除.
    >>> btree
    BinaryTree({2: 'phone', 7: 'computer', 9: 'scree', 'Tom': 'headmaster', 'blog': 'http://blog.csdn.net/qiwsir'})

- 根据key值得到该kye的value：.__getitem__(key)

看例子：

    >>> btree
    BinaryTree({2: 'phone', 7: 'computer', 9: 'scree', 'Tom': 'headmaster', 'blog': 'http://blog.csdn.net/qiwsir'})
    >>> btree.__getitem__("blog")
    'http://blog.csdn.net/qiwsir'
    >>> btree.__getitem__(7)
    'computer'
    >>> btree._getitem__(5)         #在btree中没有key=5，于是报错。
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    AttributeError: 'BinaryTree' object has no attribute '_getitem__'

- 迭代器：.__iter__()

看例子：

	>>> btree        
	BinaryTree({2: 'phone', 7: 'computer', 9: 'scree', 'Tom': 'headmaster', 'blog': 'http://blog.csdn.net/qiwsir'})
	>>> aiter = btree.__iter__()
	>>> aiter
	<generator object <genexpr> at 0xb7416dec>
	>>> aiter.next()        #注意：next()一个之后，该值从list中删除
	2
	>>> aiter.next()
	7
	>>> list(aiter)
	[9, 'Tom', 'blog']
    >>> list(aiter)         #结果是空
    []
    >>> bool(aiter)         #but,is True
    True

- 数的数据长度：.__len__(),返回btree的长度。O(1)

看例子：

    >>> btree
    BinaryTree({2: 'phone', 7: 'computer', 9: 'scree', 'Tom': 'headmaster', 'blog': 'http://blog.csdn.net/qiwsir'})
    >>> btree.__len__()
    5

- 找出key最大的k-v对：.__max__(),按照key排列，返回key最大的键值对。

- 找出key最小的键值对：.__min__()

看例子：

    >>> btree
    BinaryTree({2: 'phone', 7: 'computer', 9: 'scree'})
    >>> btree.__max__()
    (9, 'scree')
    >>> btree.__min__()
    (2, 'phone')

- 两棵树的关系运算

看例子：

    >>> other = [(3,'http://blog.csdn.net/qiwsir'),(7,'qiwsir')]
    >>> bother = BinaryTree()       #再建一个树
    >>> bother.update(other)        #加入数据

    >>> bother
    BinaryTree({3: 'http://blog.csdn.net/qiwsir', 7: 'qiwsir'})
    >>> btree
    BinaryTree({2: 'phone', 7: 'computer', 9: 'scree'})
    
    >>> btree.__and__(bother)       #重叠部分部分
    BinaryTree({7: 'computer'})

    >>> btree.__or__(bother)        #全部
    BinaryTree({2: 'phone', 3: 'http://blog.csdn.net/qiwsir', 7: 'computer', 9: 'scree'})

    >>> btree.__sub__(bother)       #btree不与bother重叠的部分
    BinaryTree({2: 'phone', 9: 'scree'})
    
    >>> btree.__xor__(bother)       #两者非重叠部分
    BinaryTree({2: 'phone', 3: 'http://blog.csdn.net/qiwsir', 9: 'scree'})

- 输出字符串模样，注意仅仅是输出的模样罢了：.__repr__()

看例子：

    >>> btree
    BinaryTree({2: 'phone', 7: 'computer', 9: 'scree'})
    >>> btree.__repr__()
    "BinaryTree({2: 'phone', 7: 'computer', 9: 'scree'})"

- 清空树中的所有数据:.clear(),O(log(n))

看例子：

    >>> bother   
    BinaryTree({3: 'http://blog.csdn.net/qiwsir', 7: 'qiwsir'})
    >>> bother.clear()
    >>> bother
    BinaryTree({})
    >>> bool(bother)
    False

- 浅拷贝：.copy(),官方文档上说是浅拷贝，但是我做了操作实现，是下面所示，还不是很理解其“浅”的含义。O(n*log(n))

看例子：

    >>> btree
    BinaryTree({2: 'phone', 7: 'computer', 9: 'scree'})
    >>> ctree = btree.copy()
    >>> ctree
    BinaryTree({2: 'phone', 7: 'computer', 9: 'scree'})

    >>> btree.__setitem__("github","qiwsir")    #增加btree的数据
    >>> btree
    BinaryTree({2: 'phone', 7: 'computer', 9: 'scree', 'github': 'qiwsir'})
    >>> ctree
    BinaryTree({2: 'phone', 7: 'computer', 9: 'scree'})     #这是不是在说明属于深拷贝呢？
    
    >>> ctree.__delitem__(7)    #删除ctree的一个数据
    >>> ctree
    BinaryTree({2: 'phone', 9: 'scree'})
    >>> btree
    BinaryTree({2: 'phone', 7: 'computer', 9: 'scree', 'github': 'qiwsir'})
    
- 移除树中的一个数据：.discard(key)，这个功能与.__delitem__(key)类似.两者都不反悔值。O(log(n))

看例子：

    >>> ctree
    BinaryTree({2: 'phone', 9: 'scree'})
    >>> ctree.discard(2)    #删除后，不返回值，或者返回None
    >>> ctree
    BinaryTree({9: 'scree'})
    >>> ctree.discard(2)    #如果删除的key不存在，也返回None
    >>> ctree.discard(3)
    >>> ctree.__delitem__(3) #但是，.__delitem__(key)则不同，如果key不存在，会报错。
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/usr/local/lib/python2.7/site-packages/bintrees/abctree.py", line 264, in __delitem__
      self.remove(key)
      File "/usr/local/lib/python2.7/site-packages/bintrees/bintree.py", line 124, in remove
      raise KeyError(str(key))
      KeyError: '3'

- 根据key查找，并返回或返回备用值：.get(key[,d])。如果key在树中存在，则返回value,否则如果有d，则返回d值。O(log(n))

看例子：

    >>> btree
    BinaryTree({2: 'phone', 7: 'computer', 9: 'scree', 'github': 'qiwsir'})
    >>> btree.get(2,"algorithm")
    'phone'
    >>> btree.get("python","algorithm") #没有key='python'的值，返回'algorithm'
    'algorithm'
    >>> btree.get("python")     #如果不指定第二个参数，若查不到，则返回None
    >>> 

- 判断树是否为空：is_empty().根据树数据的长度，如果数据长度为0,则为空。O(1)

看例子：

    >>> ctree
    BinaryTree({9: 'scree'})
    >>> ctree.clear()   #清空数据
    >>> ctree
    BinaryTree({})
    >>> ctree.is_empty()
    True
    >>> btree
    BinaryTree({2: 'phone', 7: 'computer', 9: 'scree', 'github': 'qiwsir'})
    >>> btree.is_empty()
    False

- 根据key、value循环从树中取值：

>>.items([reverse])--按照(key,value)结构取值;
>>.keys([reverse])--key
>>.values([reverse])--value. O(n)
>>.iter_items(s,e[,reverse]--s,e是key的范围，也就是生成在某个范围内的key的迭代器 O(n)

看例子：

    >>> btree
    BinaryTree({2: 'phone', 7: 'computer', 9: 'scree', 'github': 'qiwsir'})
    >>> for (k,v) in btree.items():
    ...     print k,v
    ... 
    2 phone
    7 computer
    9 scree
    github qiwsir
    >>> for k in btree.keys():
    ...     print k
    ... 
    2
    7
    9
    github
    >>> for v in btree.values():
    ...     print v
    ... 
    phone
    computer
    scree
    qiwsir
    >>> for (k,v) in btree.items(reverse=True):  #反序
    ...     print k,v
    ... 
    github qiwsir
    9 scree
    7 computer
    2 phone

    >>> btree
    BinaryTree({2: 'phone', 5: None, 7: 'computer', 8: 'eight', 9: 'scree', 'github': 'qiwsir'})
    >>> for (k,v) in btree.iter_items(6,9):  #要求迭代6<=key<9的键值对数据
    ...     print k,v
    ... 
    7 computer
    8 eight
    >>> 

       
- 删除数据并返回该值：

>>.pop(key[,d]), 根据key删除树的数据，并返回该value，但是如果没有，并也指定了备选返回的d，则返回d，如果没有d，则报错；
>>.pop_item(),在树中随机选择(key,value)删除，并返回。

看例子：

    >>> ctree = btree.copy()
    >>> ctree
    BinaryTree({2: 'phone', 7: 'computer', 9: 'scree', 'github': 'qiwsir'})

    >>> ctree.pop(2)    #删除key=2的数据，返回其value
    'phone'
    >>> ctree.pop(2)    #删除一个不存在的key，报错
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        File "/usr/local/lib/python2.7/site-packages/bintrees/abctree.py", line 350, in pop
        value = self.get_value(key)
        File "/usr/local/lib/python2.7/site-packages/bintrees/abctree.py", line 557, in get_value
        raise KeyError(str(key))
        KeyError: '2'
    
    >>> ctree.pop_item()   #随机返回一个(key,value),并已删除之
    (7, 'computer')
    >>> ctree
    BinaryTree({9: 'scree', 'github': 'qiwsir'})
    
    >>> ctree.pop(7,"sing")    #如果没有，可以返回指定值
    'sing'

- 查找数据,并返回value：.set_default(key[,d])，在树的数据中查找key,如果存在，则返回该value。如果不存在，当指定了d,则将该（key,d）添加到树内；当不指定d的时候，添加(key,None). O(log(n))

看例子：

    >>> btree
    BinaryTree({2: 'phone', 7: 'computer', 9: 'scree', 'github': 'qiwsir'})
    >>> btree.set_default(7)    #存在则返回
    'computer'
    
    >>> btree.set_default(8,"eight")  #不存在，则返回后备指定值，并加入到树
    'eight'
    >>> btree
    BinaryTree({2: 'phone', 7: 'computer', 8: 'eight', 9: 'scree', 'github': 'qiwsir'})
    
    >>> btree.set_default(5)    #如果不指定值，则会加入None
    >>> btree
    BinaryTree({2: 'phone', 5: None, 7: 'computer', 8: 'eight', 9: 'scree', 'github': 'qiwsir'})

    >>> btree.get(2)        #注意，.get(key)与.set_default(key[,d])的区别
    'phone'
    >>> btree.get(3,"mobile")   #不存在的 key,返回但不增加到树
    'mobile'
    >>> btree
    BinaryTree({2: 'phone', 7: 'computer', 8: 'eight', 9: 'scree', 'github': 'qiwsir'})

- 根据key删除值

>>.remove(key),删除(key,value)
>>.remove_items(keys),keys是一个key组成的list,逐个删除树中的对应数据

看例子：

    >>> ctree
    BinaryTree({2: 'phone', 5: None, 7: 'computer', 8: 'eight', 9: 'scree', 'github': 'qiwsir'})
    >>> ctree.remove_items([5,6])       #key=6，不存在，报错
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        File "/usr/local/lib/python2.7/site-packages/bintrees/abctree.py", line 271, in remove_items
        self.remove(key)
        File "/usr/local/lib/python2.7/site-packages/bintrees/bintree.py", line 124, in remove
        raise KeyError(str(key))
        KeyError: '6'
    
    >>> ctree
    BinaryTree({2: 'phone', 7: 'computer', 8: 'eight', 9: 'scree', 'github': 'qiwsir'})
    >>> ctree.remove_items([2,7,'github'])  #按照 列表中顺序逐个删除
    >>> ctree
    BinaryTree({8: 'eight', 9: 'scree'})
     
###以上只是入门的基本方法啦，还有更多内容，请移到文章开头的官方网站。
