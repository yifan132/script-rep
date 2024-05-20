import re
pattern='黑客|破解|反爬'
s='我想学习Python，想破解一些VIP视频，Python可以实现无底线反爬吗？'
#sub用于实现对字符串指定子串的替换
new_s=re.sub(pattern,'XXX',s)
print(new_s)

#split用于对字符串的切分
pattern2='[?|&]'
s2='http://www.baidu.com/baidu?tn=34046034_10_dg&ie=utf-8&wd=xp'
lst=re.split(pattern,s2)
print(lst)
print('-'*20)

s3='美丽'
lst=['伟大','中国','meng']
s4=s3.join(lst)
print(s4)