#用小括号创建元组
t=('hellow',[10,11,12],500)
print(t)

#使用tuple创建元组
tt=tuple('hellow')
print(tt)

t2=(10,20,2)
print(t2)

t3=([10,20,2])
print(t3)
print('t3.index:',t3.index(10))
print('t3.count:',t3.count(2))

#当元组只有一个元素时，输出元组类型 需要在创建元组的元素后加逗号
t4=(100)
print(t4,type(t4))

t5=(100,)
print(t5,type(t5))