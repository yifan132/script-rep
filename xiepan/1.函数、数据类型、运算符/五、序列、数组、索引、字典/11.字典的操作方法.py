d={'hellow':10,'world':20,'python':30}
print(d)
print(d.keys()) #获取所有的key值
print(d.values()) #获取所有的value

#向字典中添加元素
d[100]='开心' #直赋值运算添加
print(d)

#获取所有的key值
keys=d.keys()
print(keys) #dict_keys(['hellow', 'world', 'python', 100])  是对象的形式
print(list(keys)) #列表方式查看
print(tuple(keys)) #元组方式查看

#获取所有的value值
values=d.values()
print(values) #dict_values([10, 20, 30, '开心'])  是对象的形式
print(list(values)) #列表方式查看
print(tuple(values)) #元组方式查看

#如果蒋字典中的数据转成key-value的形式，以元组的方式进行展现
lst=list(d.items())
print(lst)

d1=dict(lst) #转成字典类型
print(d1)

#使用pop ，先将key对应的value取出来，再将整个键值对删除 
print(d.pop(100))
print(d)

#pop删除不存在的键值对
print(d.pop(1008,'不存在'))

#使用popitem  随机删除
print(d.popitem())
print(d)

#清空字典中所有元素
d.clear()
print(d)

#python中一切皆对象
print(bool(d)) #空字典的布尔值是False