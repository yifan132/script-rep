d={'hellow':10,'world':20,'python':30}

#访问字典中的元素
#（1）使用d[key]
print(d['hellow'])
#（2）使用get(key)
print(d.get('hellow'))

#二者之间是有区别的，如果key不存在，d[key]报错，d.get(key)可以指定默认值
#print(d['java'])  #KeyError:'java'
print(d.get('java')) #None
print(d.get('java','不存在'))


#遍历
for item in  d.items():
    print(item) #返回的是元组
    
#遍历键和值
for key,value in d.items():
    print(key,'-->',value)