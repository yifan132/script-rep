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

print('北\n京\n欢\n迎\n你')


#字符串索引和切片
s='HELLOWORLD'
print(s[0],s[-10]) #序号0 和序号-10表示的同一个字符
print('北京欢迎你'[4]) #获取字符串索引为4
print('北京欢迎你'[-1]) #获取字符串索引为4
print(s[2:7]) #正向左闭右开
print(s[-8:-3]) #反向左开右闭
print(s[:5])
print(s[1:])

#子串
x='2022年'
y='北京冬奥会'
print(x+y) #连接字符串
print(x*10) #x的字符串内容复制10次

#布尔类型
print('北京' in y)
print('上海' in y)

x=True
print(x)
print(type(x))
print(x+10)
print(False+10)

print(bool(18)) #测试整数18的布尔值
print(bool(0))
print(bool(0.0))
#总结，非0的整数的布尔值都是true

print(bool('北京欢迎你'))
print(bool(''))
#所有非空字符串的布尔值都是false

print(bool(False))
print(bool(True))