lst=[4,5,23,7]
print(lst)

#排序，默认升序
lst.sort()
print(lst)

#降序
lst.sort(reverse=True)
print(lst)

print('-'*40)

#字符串列表页可排序，按ask码排，大写比小写小32
lst2=['apple','Car','Orange','cat']
print('原顺序:',lst2)

lst2.sort()
print('升序：',lst2)

lst2.sort(reverse=True)
print('降序：',lst2)

#忽略大小写进行比较（都转成大写upper，或都转成小写lower）
lst2.sort(key=str.upper)
print(lst2)

#通过排序生成新列表
asc_lst=sorted(lst2) #升序
print(asc_lst)

desc_lst=sorted(lst2,reverse=True) #降序
print(desc_lst)