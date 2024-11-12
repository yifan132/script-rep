answer=input('喝酒了吗？')

#多分支结构
if answer =='是':
    proof=eval(input('酒精度数：'))
    if proof < 20:
        print('不构成酒驾')
    if 20<=proof<=80:
        print('构成酒后驾驶')
    if proof>80:
        print('构成醉驾')
else:
    print('没事了')
    
    
#pass语句，是一个占位符，用到需要写语句的地方
answer = input('您是会员吗？y/n')

if answer=='y':
    pass
else:
    pass


#布尔值(0是false)
age =int(input('请输入你的年龄:'))
if age:
    print(age)
else:
    print('xxx')