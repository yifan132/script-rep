s='helloworldhelloworldhsdleklaiids'
#(1)字符串拼接及not in
new_s=''
for item in s:
    if item not in new_s:
        new_s+=item
print(new_s)

#(2)索引加not in
new_s2=''
for i in range(len(s)):
    if s[i] not in new_s2:
        new_s2+=s[i]
print(new_s2)

#(3)通过集合去重（加列表排序）
new_s3=set(s)#创建集合
print(new_s3)
lst=list(new_s3)#将集合创建为列表
print(lst)
lst.sort(key=s.index)#按照原来s字符串的顺序排序
print(''.join(lst))