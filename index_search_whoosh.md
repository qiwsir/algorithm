#问题

Whoosh是python中解决索引查找的模块，在讨论[索引查找的文章](https://github.com/qiwsir/algorithm/blob/master/index_search.md)已经对有关索引查找进行了阐述，此处详细说明Whoosh模块的应用。

#思路说明

##Whoosh的安装

[这里有详细内容](https://github.com/qiwsir/algorithm/blob/master/index_search.md)

##whoosh的使用步骤

whoosh在应用上划分三个步骤：

1. 建立索引和模式对象
2. 写入索引文件
3. 搜索

下面依次阐述各步骤

##建立索引和模式对象

###建立索引模式

使用Whoosh的第一步就是要建立索引对象。首先要定义索引模式，以字段的形式列在索引中。例如：

    >>> from whoosh.fields import *
    >>> schema = Schema(title=TEXT, path=ID, content=TEXT)

title/path/content就是所谓的字段。每个字段对应索引查找目标文件的一部分信息，上面的例子中就是建立索引的模式：索引内容包括title/path/content。一个字段建立了索引，意味着它能够被搜索；也能够被存储，意味着返回结果。例如上面的例子，可以写成：

    >>> schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)

这里在某些字段后面添加了(stored=True)，意味着将返回该字段的搜索结果。

以上就建立好了索引模式，不需要重复建立索引模式，因为一旦此模式建立，将随索引保存。

在生产过程中，如果你愿意，还可以建立一个类用于建立索引模式。如下例子：

    from whoosh.fields import SchemaClass, TEXT, KEYWORD, ID, STORED

    class MySchema(SchemaClass):
        path = ID(stored=True)
        title = TEXT(stored=True)
        content = TEXT
        tags = KEYWORD

**索引字段类型**

在上例中，title=TEXT，title是字段名称，后面的TEXT是该字段的类型。这两个分别说明了索引内容和查找对象类型。whoosh有如下字段类型，供建立所以模式使用。

- whoosh.fields.ID:仅能为一个单元值，即不能分割为若干个词，通常用于诸如文件路径，URL，日期，分类。
- whoosh.fields.STORED:该字段随文件保存，但是不能被索引，也不能被查询。常用于显示文件信息。
- whoosh.fields.KEYWORD:用空格或者逗号（半角）分割的关键词，可被索引和搜索。为了节省空间，不支持词汇搜索。
- whoosh.fields.TEXT:文件的文本内容。建立文本的索引并存储，支持词汇搜索。
- whoosh.fields.NUMERIC:数字类型，保存整数或浮点数。
- whoosh.fields.BOOLEAN:布尔类值
- whoosh.fields.DATETIME:时间对象类型

关于[索引字段类型的更多内容，请看这里](https://pythonhosted.org/Whoosh/schema.html).

###建立索引存储目录

索引模式建立之后，还要建立索引存储目录。如下：

    import os.path
    from whoosh.index import create_in
    from whoosh.index import open_dir

    if not os.path.exists('index'):     #如果目录index不存在则创建
        os.mkdir('index') 
    ix = create_in("index",schema)      #按照schema模式建立索引目录
    ix = open_dir("index")　            #打开该目录一遍存储索引文件

上例中，用create_in创建一个具有前述索引模式的索引存储目录对象，所有的索引将被保存在该目录（index）中。

之后，用open_dir打开这个目录。

第一步到此结束。

把上面的代码整理一下，供参考：

    import os.path

    from whoosh import fields
    from whoosh import index

    schema = fields.Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
    
    if not os.path.exists("index"):
        os.mkdir("index")

    ix = index.create_in("index",schema)
    ix = index.open_dir("index")

##写索引文件

(待续）
