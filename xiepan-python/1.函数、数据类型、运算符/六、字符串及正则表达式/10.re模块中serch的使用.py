import re #导入
s='i study python 3.11 every day Python2.7 i love you' #待匹配字符串
pattern='\d\.\d+' #匹配0~9的数字（\d)；，\.是将.转义 作为普通的.使用；+是匹配0~9的数字1次或多次

#search 搜索第一个匹配的值
search=re.search(pattern,s)
print(search) #<re.Match object; span=(15, 19), match='3.11'> 找到了3.11

s2='4.10 Python istudy every day'
s3='i study every day '
search2=re.search(pattern,s2)
print(search2) #<re.Match object; span=(0, 4), match='4.10'>

search3=re.search(pattern,s3)
print(search3) #None

print(search.group())#group()显示匹配到的值
print(search2.group())
print('-'*20)