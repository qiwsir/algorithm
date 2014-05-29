#! /usr/bin/env python
#coding:utf-8

def char_to_number(by_list,char):    #根据排序依据字母顺序，给另外一个字母编号
    try:
        return by_list.index(char)
    except:
        return 1000

def sort_by_list(by_list,input_list):  

    result={}
    for word in input_list:
        number_list = [char_to_number(by_list,word[i]) for i in range(len(word))]
        
        #得到形如：{"good":[2,3,3,1],"book":[1,3,3,0]}样式的结果
        result[word] = number_list
    
    #将得到的result生成[(key1,value1),(key2,value2),...]列表，按照value值排序，取出排序结果中的key即v[0]，生产列表。
    return [v[0] for v in sorted(result.items(),lambda x,y:cmp(x[1],y[1]))]

if __name__=="__main__":
    word = ["bed","dog","dear","eye"]
    by_string = ['d','g','e','c','f','b','o','a']
    print "the word list is:"
    print word
    print "\nwill sorted by:"
    print by_string
    print "\nthe result is:"
    print sort_by_list(by_string,word)
    

 
