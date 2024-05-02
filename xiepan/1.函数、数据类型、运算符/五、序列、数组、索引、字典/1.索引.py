s='helloworld' #正向索引
for i in range(0,len(s)):
    print(i,s[i],end='  ')
    
print('--------------')
#反向递减索引
for i in range(-10,0):
    print(i,s[i],end='  ')
    
print()

s1=s[0:5:2] #索引从0开始，到5结束（不包含5），步长为2（每次迈两步）
print(s1)

print(max(s))
print(s.index('l'))
print(s.count('l'))
