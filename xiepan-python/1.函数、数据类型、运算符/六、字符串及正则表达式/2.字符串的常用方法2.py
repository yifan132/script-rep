s='helloworld'
new_s=s.replace('o','你好',1) #最后一次参数是替换次数，默认全部替换
print(new_s)

#字符串在指定的宽度范围内居中
print(s.center(20))

#去掉字符串左右空格
s='   hello  world  '
print(s.strip())#去掉字符串左右空格
print(s.lstrip())#去掉字符串左空格
print(s.rstrip())#去掉字符串右空格

#去掉指定的字符
s3='dl-helloworld'
print(s3.strip('ld'))#去除字符与顺序无关
print(s3.lstrip('ld'))
print(s3.rstrip('ld'))