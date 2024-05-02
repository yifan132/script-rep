lst=['hellow','world','python','php']
for item in lst:
    print(item)
    
for i in range(0,len(lst)):
    print(lst[i])
    
#第三种遍历形式,index和item是自己取的变量名
for index,item in enumerate(lst):
    print(index,item)
    
#修改列表的起始序号,start可省略不写
for index,item in enumerate(lst,start=1):
    print(index,item)
