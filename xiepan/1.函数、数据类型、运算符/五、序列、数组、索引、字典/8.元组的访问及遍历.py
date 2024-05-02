t=('python','hellow','world')
#根据索引访问元组
print(t[0])
t2=t[0:3:2] #元组支持切片操作
print(t2)

#遍历
for item in t:
    print(item)
    
#for + range + len()
for i in range(len(t)):
    print(i,t[i])
    
#enumerate()
for index,item in enumerate(t):
    print(index,'-->',item)
    
for index,item in enumerate(t,start=1):
    print(index,'-->',item)