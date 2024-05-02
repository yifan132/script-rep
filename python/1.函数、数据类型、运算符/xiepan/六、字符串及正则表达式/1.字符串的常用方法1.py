#大小写转换，转换后是一个新的字符串
s1='HelloWorld'
new_s1=s1.upper()
print(new_s1)
new_s2=s1.lower()
print(new_s2)

#字符串的分隔
emil='xx@qq.com'
lst=emil.split('@') #按照@符号进行分割，分割出来的结果是一个列表
print(lst)

#统计某字符串出现的次数
print(s1.count('o'))

#检索操作
print(s1.find('o'))
print(s1.find('p')) # -1，没有找到

print(s1.index('o')) #返回第一次出现o的序号
#print(s1.index('p')) #ValueError: substring not found

#判断前缀后缀
print('demo.py'.endswith('.py')) #True
print(s1.startswith('H')) #True
print(s1.startswith('P')) #False