#单分支结构
number=eval(input('输入号码:'))

if number==123456:
    print('中奖了')

if number!=123456:
    print('没中奖')


n=98
if n%2: #98%2=0，0是false
    print(n,'是奇数')
    
if not n%2:
    print(n,'是偶数')
    
    
x=input('输入字符：') 
if x: #python中一切皆对象，每个对象都有一个布尔值，非空字符串为true，反之为false
    print(x,'x是非空字符串')
if not x:
    print(x,'x是空字符串')
    

#使用if时，如果语句块只有一句代码，可以将语句块直接卸载冒号的后面 
a=10
b=5
if a>b:max=a 
print(max)

if a<b:max=b
print(max)