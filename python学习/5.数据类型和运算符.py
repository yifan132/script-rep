#保留字，严格区分大小写
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))

#变量
#变量名=value，变量是动态类型，允许多个变量指向同一个值
luck_number=8
print(luck_number,type(luck_number))
luck_number='abc'
print(luck_number,type(luck_number))

no=number=1024
print(no,number)
print(id(no),id(number)) #值内存地址

#常量
#需要全大写，不允许修改
pi=3.1415926 #变量
PI=3.1415926 #常量

#整数
num=123 #默认十进制
num2=0b1010101 #二进制
num3=0o213 #八进制
num4=0x8A2FA #十六进制

print(num)
print(num2)
print(num3)
print(num4)

#浮点
height=185.12
print(height)
print(type(height))

x=1.5E14
print('科学计数法:',x,type(x))

#不确定尾数
print(0.1+0.2)
print(round(0.1+0.2,1))

#复数
x=123+456j
print('实数：',x.real)
print('虚数：',x.imag)

#转义字符
print('北京\n\n欢迎您')
print('北京\t欢迎你')
print('老师说：\'好好学习，天天向上\'')
print('老师说：\"好好学习，天天向上\"')

#原字符,使转义字符失效的符号 r或R
print(r'北\n京\n欢\n迎\n你')
print(R'北\n京\n欢\n迎\n你')