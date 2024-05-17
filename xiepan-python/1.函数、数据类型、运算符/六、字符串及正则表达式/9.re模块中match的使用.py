import re #导入re ，re是python的内置模块
s='i study python 3.11 every day' #待匹配字符串
pattern='\d\.\d+' #匹配0~9的数字（\d)；，\.是将.转义 作为普通的.使用；+是匹配0~9的数字1次或多次
match=re.match(pattern,s,re.I) #re.I是忽略大小写
print(match)#返回None，match是从头开始匹配的，没有找到数字

s2='3.11Python i study every day'
match2=re.match(pattern,s2)
print(match2) #<re.Match object; span=(0, 4), match='3.11'>

print('匹配值的起始位置：',match2.start())
print('匹配值的结束位置：',match2.end())
print('匹配值的区间位置元素：',match2.span())
print('待匹配的字符串：',match2.string)
print('匹配的数据：',match2.group())