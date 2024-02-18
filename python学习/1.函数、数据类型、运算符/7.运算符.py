print(10//1)

print(2*(2+3))

print(2*2+3)


##############赋值运算符
x=20
y=10
x=x+y
print(x)

x+=y
print(x)

x-=y
print(x)

x*=y
print(x)

x/=y
print(x)

x%=2 #x=x%2
print(x)

z=3
y//=z  #y=y//z
print(y)

y**=2 #ty=y**2
print(y)

#############链式赋值
a=b=c=100 #a=100,b=100,c=100
print(a,b,c)

###########系列解包赋值
a,b=10,20 #a=10 b=20
print(a,b)

#交换两个变量值
a,b=b,a
print(a,b)


##############逻辑运算符
print(True and True)
print(True and False)
print(False and False)

print(8>7 and 6>5)
print(8>7 and 6<5)
print(8<7 and 10/0) # 当8<7结果为false时，直接得结果，不计算10/0
#print(10/0 and 8<7)

print(True or True)
print(True or False)
print(False or False)

print(not(8>7))
