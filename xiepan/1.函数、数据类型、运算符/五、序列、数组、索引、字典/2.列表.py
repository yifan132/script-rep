lst1=['hellow','35','world','0.5'] #创建列表
print(lst1)

lst2=list('helloworld') #使用内置函数list创建列表
print(lst2)

lst3=list(range(1,10,2)) #创建1到10，步长为2的列表
print(lst3)

#列表是序列的一种，对序列的操作符、运算符、函数均可使用
print(lst1+lst2+lst3)
print(lst1*3)
print(len(lst1))
print(max(lst1))
print(lst1.index('hellow'))
print(lst2.count('l'))

#列表的删除
lst4=[1,2,3]
print(lst4)
del lst4