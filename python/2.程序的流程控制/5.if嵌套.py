answer=input('喝酒了吗？')

#多分支结构
if answer =='是':
    proof=eval(input('酒精度数：'))
    if proof < 20:
        print('不构成酒驾')
    if 20<=proof<80:
        print('构成酒后驾驶')
    if proof>80:
        print('构成醉驾')
else:
    print('没事了')