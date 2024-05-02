#二维列表创建
lst=[
    ['城市','同比','环比'],
    ['北京',100,35],
    ['成都',102,60],
    ['上海',101,55]
]
print(lst)

#遍历
for i in lst:
    for j in i:
        print(j,end='\t')
    print() #换行
    
print()
print('-'*40)
#生成一个4行5列的列表，外层控制行数，内层控制列数
lst2=[[j for j in range(5)] for i in range(4)]
print(lst2)