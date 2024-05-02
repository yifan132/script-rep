#{}直接创建集合
s={10,20,30,40}
print(s,type(s))

#集合只能存储不可变数据类型
#s={[10,20],[30,40]} #TypeError: unhashable type: 'list'
#print(s)

#使用set()创建集合
s1=set() #创建了一个空集合
print(s1)

s2={} #{}创建的是字典
print(s2,type(s2))

s3=set('helloworld')
print(s3) #集合是无序切不重复的

s4=set([10,20,30])
print(s4)

s5=set(range(1,10))
print(s5)

#集合属于序列中的一种
print('max:',max(s5))
print('len:',len(s5))

print('9在集合中存在吗？',9 in s5)
print('9在集合中不存在吗？',9 not in s5) 

#集合的删除
del s5
print(s5)