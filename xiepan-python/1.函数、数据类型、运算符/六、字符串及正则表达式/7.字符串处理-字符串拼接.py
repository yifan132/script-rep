s1='hello'
s2='world'
#(1)使用+拼接
print(s1+s2)

#(2)使用join()拼接
print(''.join([s1,s2]))
print('*'.join(['hello','world','java','php']))
print('你好'.join(['hello','world','java','php']))

#(3)直接拼接
print('hello''world')

#(4)使用格式化字符串拼接
print('%s%s' %(s1,s2))#元组
print(f'{s1}{s2}')
print('{0}{1}'.format(s1,s2))