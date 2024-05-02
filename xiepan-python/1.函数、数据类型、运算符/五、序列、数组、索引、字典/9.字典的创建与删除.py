#字典是无序的
d={10:'cat',20:'dog',30:'pig',20:'tiger'} #若key相同，最后一个相同key的值会覆盖前一个的值
print(d)

lst1=[10,20,30,40]
lst2=['cat','dog','pig','zoo','tiger']
zipobj=zip(lst1,lst2)
print(zipobj) #<zip object at 0x0000027A481CEC80>
# print(list(zipobj)) #转成列表查看（是元组类型）
d=dict(zipobj) #转成字典看    注释第8行的原因是：第8行将zipobj转成了列表，已经没有元素了，所以不能再转成字典类型了
print(d)

#使用参数创建字典
d1=dict(cat=10,dog=20) #等号左边是key，右边是值
print(d1)

t=(10,20,30) #元组可以作为字典的key，元组不可变，是有hash的
print({t:10}) #t是key，10是值


# lst3=[1,2,3]#列表可变，不能作为字典的key
# print({lst3:10}) #unhashable type: 'list'

#字典属于序列
print('max:',max(d))
print('len:',len(d))

del(d) #删除
print(d)