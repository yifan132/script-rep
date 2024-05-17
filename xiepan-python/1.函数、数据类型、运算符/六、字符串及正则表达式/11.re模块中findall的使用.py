import re #导入
pattern='\d\.\d+' #匹配0~9的数字（\d)；，\.是将.转义 作为普通的.使用；+是匹配0~9的数字1次或多次
s='i study python 3.11 every day Python2.7 i love you' #待匹配字符串
s2='4.10 Python istudy every day'
s3='i study every day '

#findall，找到多个匹配到的值
lst=re.findall(pattern,s) #若找到多个值，则是列表类型
lst2=re.findall(pattern,s2)
lst3=re.findall(pattern,s3)

print(lst)
print(lst2)
print(lst3)
