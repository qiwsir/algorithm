--在LUA中，没有类似python的str.split()函数，如果要将一个字符串按照指定的符号分割，并存到table中。
--如将a="1,2,3"转换为{1,2,3}

a="1,2,3,4,"    --或者 a="1,2,3,4" 不论最后一个是否有","
t={}

for w in string.gmatch(a,"([^',']+)") do     --按照“,”分割字符串
    table.insert(t,w) 
end

for k,v in ipairs(t) do 
    print(k..":"..v) 
end
