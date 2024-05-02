#完整语法格式
#print(object(s), separator=separator, end=end, file=file, flush=flush)
print('abc','def', sep='_', end='\n', file=None)

print (3+1)
print('Hello', 'how are you?', sep=' ---//@@')
print('Hello', 'how are you?')
x = ('apple', 'banana', 'cherry')
print(x)



#输出文件
fp=open('D:/python/text.txt','a+')
print('hello','world','python',file=fp)
fp.close()



#转义字符
print('hello\tworld') #\t tab
print('helloooo\tworld')
print('hello\nworld')
print('hello11111111111\r1world')  #\r  replace
print('hello\bworld') #\b  back tab

print('http:\\\\www.baidu.com')
print('老师说:\'大家好\'')

#原字符（禁用转义字符）
print(r'hello\nworld')
print(r'hello\nworld\\')

#二进制
print(chr(0b100111001011000))
print(ord('乘'))

import keyword
print(keyword.kwlist)

name='abc'
name='bbb'
print(name);

n1=90
n2=-76
n3=0
print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))

n4=123.11
print(n4,type(n4))

from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))