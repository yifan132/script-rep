s={10,20,30}
print(s)

#添加元素
s.add(100)
print(s)
#删除元素
s.remove(20)
print(s)
#删除集合
# s.clear()
# print(s)

#集合的遍历
for item in s:
    print(s)
    
#遍历集合的序号和值
for index,item in enumerate(s):
    print(index,'-->',item)
    
#集合的生成式
s={i for i in range(1,10)}
print(s)

s={i for i in range(1,10) if i%2==1}
print(s)