#for 循环
##遍历字符串
for i in 'hello':
    print(i)

#range()函数，产生[n,m}

for i in range(1,11):
    print(i)


for i in range(1,11):
    if i%2==0:
        print(i)

#累加
s=0
for i in range(1,11):
    s+=i
    print(s)

#for else循环

#累加
s=0
for i in range(1,11):
    s+=i
else:
    print(s)


#while 循环

#累加
s=0
i=1
while i<=100:
    s+=i
    i+=1
    print('xx',s)


answer=input('y/n')
while answer=='y':
        print('y')
        answer=input('y/n')
    
#while 循环扩展

#累加
s=0
i=1
while i<=100:
    s+=i
    i+=1
else:
    print('xx',s)
    
    
#密码登录
i=0
success_flag='false'
while i<3 and success_flag=='false':
    user_name=input('username:')
    pwd=input('pwd:')
    
    if user_name== 'yyf' and pwd== '123':
        print('loading')
        success_flag='true'
    else:
        if i<2:
            print('还有',2-i,'次机会')
        i+=1
else:
    print('登录错误') 
    

#嵌套循环

#三行四列
for i in range(1,4):
    for j in range(1,5):
        print('*',end='')
    print() #换行
 
 #直角三角形
j=1
for i in range(1,6):
    while j<=5 and i>=j:
        print('*',end='')
        j+=1
    else:
        j=1
    print() 