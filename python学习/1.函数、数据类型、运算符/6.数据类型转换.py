x=10
y=3
z=x/y
print(z,type(z)) #隐式转换，通过运算隐式转换的结果类型

#float 类型转换为int类型
print(int(3.14))
print(int(-3.9))

#int转换为float
print(float(1))
print(float(-10))

#str转为int
print(int('100'))
print(int('-100'))

#chr ord()
print(ord('杨'))#在unicode表中的整数值
print(chr(26472))

#进制之间的转换
print('十->十六',hex(26472))
print('十->八',oct(26472))
print('十->二',bin(26472))


#eval函数
s='3.14+3'
print(s,type(s))
x=eval(s) #使用eval函数去掉s的左右引号，执行加法运算
print(x,type(x))

#eval经常与input函数使用，用来获取用户输入的数值
age=eval(input('请输入你的年龄：'))
print(age,type(age))
print(eval('age'))  #去掉引号后取到了age变量