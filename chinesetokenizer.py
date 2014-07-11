#! /usr/bin/env python
#coding:utf-8

#本代码来自网络：http://ashin.sinaapp.com/article/118/

import jieba
from whoosh.analysis import Tokenizer,Token 
from whoosh.compat import text_type

class ChineseTokenizer(Tokenizer):  
    def __call__(self, value, positions=False, chars=False, keeporiginal=False, removestops=True, start_pos=0, start_char=0, mode='', **kwargs):  
        assert isinstance(value, text_type), "%r is not unicode" % value  
        t = Token(positions, chars, removestops=removestops, mode=mode, **kwargs)  
        seglist=jieba.cut_for_search(value)                       #使用结巴分词库进行分词  
        for w in seglist:  
            t.original = t.text = w  
            t.boost = 1.0  
            if positions:  
                t.pos=start_pos+value.find(w)  
            if chars:  
                t.startchar=start_char+value.find(w)  
                t.endchar=start_char+value.find(w)+len(w)  
            yield t                                               #通过生成器返回每个分词的结果token

def ChineseAnalyzer():  
    return ChineseTokenizer()

"""
测试脚本：

#!/usr/bin/env python  
# -*- coding: UTF-8 -*-  

from whoosh.index import create_in  
from whoosh.fields import *  
from chinesetokenizer import ChineseAnalyzer
#from whoosh.analysis import RegexAnalyzer  
#analyzer = RegexAnalyzer(ur"([\u4e00-\u9fa5])|(\w+(\.?\w+)*)")

analyzer = ChineseAnalyzer()

schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored=True, analyzer=analyzer))  
ix = create_in("schema", schema)  
writer = ix.writer()

writer.add_document(title=u"First document", path=u"/a", content=u"先生说我们都是好学生")  
writer.add_document(title=u"Second document", path=u"/b", content=u"我们要树立科学发展观")
writer.commit()

with ix.searcher() as searcher:
    results = searcher.find("content", u"发展")
    if 0 != len(results):
        for hit in results:
            print hit.highlights("content")


运行结果：


先<b class="match term0">生</b>说我们都是好<b class="match term1">学</b><b class="match term0">生</b>

先生说我们都是好<b class="match term0">学生</b>

我们要树立科学<b class="match term0">发</b><b class="match term1">展</b>观

我们要树立科学<b class="match term0">发展</b>观

"""
