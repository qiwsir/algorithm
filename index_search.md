#问题

索引查找

索引查找的定义，[来源百度百科](http://baike.baidu.com/view/2131886.htm)

>>索引查找是在索引表和主表(即线性表的索引存储结构)上进行的查找。
>>索引查找的过程是：
>>- 首先根据给定的索引值K1，在索引表上查找出索引值等于K1的索引项，以确定K1对应的子表在主表中的开始位置和长度，
>>- 然后再根据给定的关键字K2，在对应的子表中查找出关键字等于K2的元素(结点)。

#思路说明

对于一个list或者dictionary类型的数据，python有专门的内置函数index()进行索引查找，当然，这个查找的过程完全由python自己完成，不需要我们重写。

##list索引：list.index(x)

python的官方解释是：

>>Return the index in the list of the first item whose value is x. It is an error if there is no such item.

翻译：返回list中的第一个值为x的元素索引，如果找不到返回错误。

例如：

    >>> alist = ['I','am','a','human','you','are','a','programmer']
    >>> alist.index('a')        #注意：alist中有两个"a",但是只返回第一个索引值
    2
    >>> alist.index('am')
    1
    >>> alist.index('he')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      ValueError: 'he' is not in list

这个索引查找的复杂度是O(n)

对于较小的数据，list.index(x)足矣，但是，如果对象数据量比较大了，这个就有点小马拉大车的感觉了，怎么办？熟悉本博客风格的朋友肯定会想到，绝对不是让我们自己动手写一个索引查找的东西，虽然写一个不是不可以，但是本着“拿来主义”的精神，一定要先查找一下，看看python是否已经为我们做好了轮子？

#Whoosh:全文索引

把[官方文档](https://pythonhosted.org/Whoosh/)的一段话拿过来：

>>Whoosh is a library of classes and functions for indexing text and then searching the index. It allows you to develop custom search engines for your content. For example, if you were creating blogging software, you could use Whoosh to add a search function to allow users to search blog entries.

简单翻译：

>>Whoosh是一个索引文本和搜索的库，允许你为你的内容设置自定义搜索引擎。比如如果创建一个博客，可以用whoosh为它添加一个搜索功能，以便用户来搜索博文。

python就是这么善解人意，就是这么高大上。

这个东西怎么用？

##Whoosh安装

在ubuntu环境下，如果已经有pip或者easy_install，只需要直接运行：

    $ sudo easy_install Whoosh

或者：

    $ sudo pip install Whoosh

即可轻松安装。windows的朋友，是不是用linux的优势在这里体现出来呢？请用。

当然，也可以到[官方下载源码进行安装](https://pypi.python.org/pypi/Whoosh/)

安装之后，输入下面的内容，如果不报错，就说明已经安装成功(一个就可以检验)。

    >>> from whoosh.fields import *
    >>> from whoosh.index import create_in

##Whoosh应用

在官方文档上，有完整的应用讲述：https://pythonhosted.org/Whoosh/quickstart.html#a-quick-introduction

此外，有几篇文章，是不错的，列在这里备查

- http://blog.sina.com.cn/s/blog_819588bc0101co4b.html
- http://www.cnblogs.com/chang/archive/2013/01/10/2855321.html
- http://ashin.sinaapp.com/article/118/

除了上述内容，在其源码存放地点，也有一些问题回答：https://bitbucket.org/mchaput/whoosh/overview
