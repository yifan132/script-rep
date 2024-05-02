s=0 #初始化变量
i=1 #初始化变量
while i<11:
    s+=i
    if s>20:
        print('累加值为：',s)
        print('i当前值为：',i)
        break
    i=i+1